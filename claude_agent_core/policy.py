from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Mapping, Optional, Set


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    reason: str
    requires_confirmation: bool = False


@dataclass
class ToolPolicy:
    """Evaluate agent tool calls before any external side effect happens."""

    allowed_tools: Optional[Set[str]] = None
    denied_tools: Set[str] = field(default_factory=set)
    confirmation_required: Set[str] = field(default_factory=set)
    max_argument_bytes: int = 8192

    def evaluate(self, tool_name: str, arguments: Mapping[str, Any]) -> PolicyDecision:
        if not isinstance(tool_name, str) or not tool_name.strip():
            return PolicyDecision(False, "tool_name must be a non-empty string")
        if not isinstance(arguments, Mapping):
            return PolicyDecision(False, "arguments must be a mapping")
        if self.max_argument_bytes <= 0:
            return PolicyDecision(False, "max_argument_bytes must be positive")

        normalized_name = tool_name.strip()
        if normalized_name in self.denied_tools:
            return PolicyDecision(False, f"{normalized_name} is denied by policy")
        if self.allowed_tools is not None and normalized_name not in self.allowed_tools:
            return PolicyDecision(False, f"{normalized_name} is not in the allowed tool set")

        argument_size = len(
            json.dumps(arguments, sort_keys=True, default=str).encode("utf-8")
        )
        if argument_size > self.max_argument_bytes:
            return PolicyDecision(
                False,
                f"arguments exceed {self.max_argument_bytes} bytes",
            )

        if normalized_name in self.confirmation_required:
            return PolicyDecision(
                True,
                f"{normalized_name} requires human confirmation",
                requires_confirmation=True,
            )

        return PolicyDecision(True, "allowed")

    def require_allowed(self, tool_name: str, arguments: Mapping[str, Any]) -> None:
        decision = self.evaluate(tool_name, arguments)
        if not decision.allowed or decision.requires_confirmation:
            raise PermissionError(decision.reason)
