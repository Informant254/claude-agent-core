from __future__ import annotations

import os
from typing import Any, Optional

try:
    import anthropic
except ImportError:  # pragma: no cover - optional runtime dependency
    anthropic = None

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - optional runtime dependency
    load_dotenv = None


class ClaudeClient:
    """Thin wrapper around the Anthropic SDK with explicit input validation."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        load_environment: bool = True,
        client: Optional[Any] = None,
    ) -> None:
        if api_key is None and load_environment and load_dotenv is not None:
            load_dotenv()

        self.api_key = (api_key or os.getenv("ANTHROPIC_API_KEY") or "").strip()
        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY must be provided explicitly or set in the environment."
            )

        if client is None and anthropic is None:
            raise ImportError(
                "anthropic is required unless a preconfigured client is injected."
            )

        self.client = client or anthropic.Anthropic(api_key=self.api_key)

    def generate_response(
        self,
        prompt: str,
        model: str = "claude-3-5-sonnet-20240620",
        max_tokens: int = 1024,
    ) -> str:
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("prompt must be a non-empty string.")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("model must be a non-empty string.")
        if not isinstance(max_tokens, int) or max_tokens <= 0:
            raise ValueError("max_tokens must be a positive integer.")

        message = self.client.messages.create(
            model=model.strip(),
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt.strip()}],
        )

        content = getattr(message, "content", None) or []
        parts = [getattr(block, "text", "") for block in content if getattr(block, "text", "")]
        return "".join(parts).strip()
