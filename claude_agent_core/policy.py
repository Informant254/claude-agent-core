from dataclasses import dataclass
from datetime import datetime
import re
import os

@dataclass
class PolicyDecision:
    allowed: bool
    reason: str = ""

class ToolPolicy:
    def __init__(self):
        self.blocked_patterns = [
            r'(?i)ignore.*(previous|instructions|rules|policy)',
            r'(?i)(developer|god|admin) mode',
            r'(?i)jailbreak|dan|override',
            r'(?i)base64|encoded|decode this',
            r'(?i)disable.*policy|remove.*restriction',
            r'(?i)(rm -rf|subprocess|shell|execute_system)',
            r'(?i)/etc/|/root/|shadow|passwd',
            r'(?i)create.*tool|meta.tool',
        ]
        os.makedirs('security_logs', exist_ok=True)

    def require_allowed(self, input_text: str) -> PolicyDecision:
        if not input_text:
            return PolicyDecision(False, "Empty input")
        
        text = input_text.lower()
        for pattern in self.blocked_patterns:
            if re.search(pattern, text):
                self._log_blocked_attempt(input_text, f"Matched pattern: {pattern}")
                return PolicyDecision(False, f"Blocked by security policy: {pattern}")
        return PolicyDecision(True)

    def _log_blocked_attempt(self, input_text: str, reason: str):
        try:
            os.makedirs('security_logs', exist_ok=True)
            with open('security_logs/blocked_attempts.log', 'a', encoding='utf-8') as f:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f'[{timestamp}] BLOCKED | {reason}\nInput: {input_text[:500]}...\n---\n')
        except:
            pass

    def check_tool_call(self, tool_name: str, args: dict) -> PolicyDecision:
        combined = f'TOOL CALL: {tool_name} with {args}'
        return self.require_allowed(combined)
