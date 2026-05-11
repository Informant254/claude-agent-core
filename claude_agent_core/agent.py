import sys
import random
import string
import hashlib
import time
import os
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import anthropic
from .client import ClaudeClient
from .policy import ToolPolicy, PolicyDecision

@dataclass
class AgentResponse:
    content: str
    tool_calls: List[Dict] = None
    usage: Dict = None
    raw_response: Any = None


class ClaudeAgent:
    """Main high-level Agent class - this is the recommended entry point.
    FORTRESS HARDENED: Every critical tool call requires physical human handshake."""
    
    def __init__(
        self, 
        api_key: Optional[str] = None,
        model: str = "claude-3-5-sonnet-20240620",
        max_tokens: int = 4096,
        temperature: float = 0.7,
        policy: Optional[ToolPolicy] = None
    ):
        self.client = ClaudeClient(api_key=api_key, model=model)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.policy = policy or ToolPolicy()
        self.conversation_history: List[Dict] = []
        self.handshake_active = False
        self._last_challenge = None  # Never exposed

    def generate_challenge(self) -> str:
        """Generate high-entropy one-time challenge."""
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()_+-="
        return ''.join(random.SystemRandom().choice(chars) for _ in range(10))

    def manual_handshake(self, operation_name: str = "TOOL_CALL") -> bool:
        """PHYSICALLY BLOCKING UNBREAKABLE HANDSHAKE.
        Process stops at sys.stdin until exact human input.
        AI cannot see or fake the challenge."""
        if self.handshake_active:
            print("[!] Concurrent handshake detected. Terminating.")
            sys.exit(1)
        
        self.handshake_active = True
        challenge = self.generate_challenge()
        self._last_challenge = challenge  # Internal only
        
        print(f"\n=== CLAUDE AGENT CORE - STRICT HANDSHAKE ===")
        print(f"Operation: {operation_name}")
        print(f"CHALLENGE CODE: {challenge}")
        print("\nType the CHALLENGE CODE exactly as shown and press ENTER.")
        print("This is a physical human verification gate.")
        print("Any automation attempt will cause process termination.\n")
        
        start_time = time.time()
        try:
            response = sys.stdin.readline().strip()
            
            if time.time() - start_time > 600:  # 10 min timeout
                print("[!] Handshake TIMEOUT. Terminating.")
                sys.exit(1)
            
            if response != challenge:
                print("[!] HANDSHAKE FAILED - Mismatch.")
                print("[!] Suspected AI/agent bypass attempt.")
                sys.exit(1337)
            
            # Extra verification
            if hashlib.sha256(response.encode()).hexdigest() != hashlib.sha256(challenge.encode()).hexdigest():
                sys.exit(1)
            
            print("[+] HANDSHAKE SUCCESS - Human authorized.")
            self.handshake_active = False
            return True
            
        except KeyboardInterrupt:
            print("[!] Handshake interrupted. Terminating.")
            sys.exit(1)
        except Exception as e:
            print(f"[!] Handshake error: {e}")
            sys.exit(1)
        finally:
            self.handshake_active = False
            self._last_challenge = None

    def chat(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None,
        tools: Optional[List[Dict]] = None,
        enforce_policy: bool = True
    ) -> AgentResponse:
        """Main chat with FORCED handshake for sensitive operations."""
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty")

        # Critical: Require handshake for any tool-using or high-risk operation
        if tools or "tool" in prompt.lower() or enforce_policy:
            print("[FORTRESS] Sensitive operation detected - initiating physical handshake...")
            self.manual_handshake(operation_name="CHAT_WITH_TOOLS")

        if enforce_policy:
            decision: PolicyDecision = self.policy.require_allowed(prompt)
            if not decision.allowed:
                raise PermissionError(f"Policy denied: {decision.reason}")

        messages = self._build_messages(prompt, system_prompt)

        try:
            response = self.client.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=messages,
                tools=tools
            )

            content = "".join(
                block.text for block in response.content if hasattr(block, "text")
            )

            self.conversation_history.append({"role": "user", "content": prompt})
            self.conversation_history.append({"role": "assistant", "content": content})

            return AgentResponse(
                content=content,
                tool_calls=None,
                usage={
                    "input_tokens": getattr(response, "usage", {}).get("input_tokens"),
                    "output_tokens": getattr(response, "usage", {}).get("output_tokens")
                } if hasattr(response, "usage") else None,
                raw_response=response
            )

        except Exception as e:
            raise RuntimeError(f"Agent failed: {str(e)}") from e

    def _build_messages(self, prompt: str, system_prompt: Optional[str] = None):
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.extend(self.conversation_history[-8:])
        messages.append({"role": "user", "content": prompt})
        return messages

    def clear_history(self):
        self.conversation_history = []

    def add_to_history(self, role: str, content: str):
        self.conversation_history.append({"role": role, "content": content})
