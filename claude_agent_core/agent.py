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
    """Main high-level Agent class - this is the recommended entry point."""
    
    def __init__(
        self, 
        api_key: Optional[str] = None,
        model: str = "claude-3-5-sonnet-20240620",
        max_tokens: int = 4096,
        temperature: float = 0.7,
        policy: Optional[ToolPolicy] = None
    ):
        self.client = ClaudeClient(api_key=api_key, model=model)  # Note: client __init__ doesn't take model, we'll handle it
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.policy = policy or ToolPolicy()
        self.conversation_history: List[Dict] = []

    def chat(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None,
        tools: Optional[List[Dict]] = None,
        enforce_policy: bool = True
    ) -> AgentResponse:
        """Main chat method with policy enforcement."""
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty")

        # Apply policy check
        if enforce_policy:
            decision: PolicyDecision = self.policy.require_allowed(prompt)
            if not decision.allowed:
                raise PermissionError(f"Policy denied: {decision.reason}")

        # Build messages
        messages = self._build_messages(prompt, system_prompt)

        try:
            # Use client but override with full params
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

            # Add to history
            self.conversation_history.append({"role": "user", "content": prompt})
            self.conversation_history.append({"role": "assistant", "content": content})

            return AgentResponse(
                content=content,
                tool_calls=None,  # TODO: parse tool calls if needed
                usage={
                    "input_tokens": getattr(response, "usage", {}).get("input_tokens"),
                    "output_tokens": getattr(response, "usage", {}).get("output_tokens")
                } if hasattr(response, "usage") else None,
                raw_response=response
            )

        except Exception as e:
            raise RuntimeError(f"Agent failed to generate response: {str(e)}") from e

    def _build_messages(self, prompt: str, system_prompt: Optional[str] = None):
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        # Keep recent history
        messages.extend(self.conversation_history[-8:])
        messages.append({"role": "user", "content": prompt})
        return messages

    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []

    def add_to_history(self, role: str, content: str):
        """Manually add message to history."""
        self.conversation_history.append({"role": role, "content": content})
