# 🤖 Claude Agent Core

[![Stars](https://img.shields.io/github/stars/Informant254/claude-agent-core?style=social)](https://github.com/Informant254/claude-agent-core/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Defensive Excellence](https://img.shields.io/badge/Defensive%20Excellence-input%20validation%20%7C%20tool%20policy-blue)](https://github.com/Informant254/claude-agent-core)

**Small, security-conscious Python primitives for building Claude-powered agents with explicit input validation and tool-call policy gates.**

## 🚀 Overview

Claude Agent Core is designed for developers who want a readable foundation for agentic workflows without hiding safety decisions behind a large framework. It provides a thin Claude client plus a policy layer that can review tool calls before external side effects happen.

## 🛠️ Quick Start

Install directly from GitHub:
```bash
pip install git+https://github.com/Informant254/claude-agent-core.git
```

Basic Usage:
```python
from claude_agent_core.client import ClaudeClient

client = ClaudeClient(api_key="your-api-key")
response = client.generate_response("Explain quantum computing in simple terms.")
print(response)
```

Gate a tool call before execution:
```python
from claude_agent_core import ToolPolicy

policy = ToolPolicy(
    allowed_tools={"search_docs", "summarize_file"},
    confirmation_required={"summarize_file"},
    max_argument_bytes=4096,
)

decision = policy.evaluate("summarize_file", {"path": "SECURITY.md"})
if decision.allowed and not decision.requires_confirmation:
    print("safe to execute")
```

## 🔐 Security Notes

- Keep API keys out of source control. Use environment variables or a local `.env` file.
- The client validates prompts and token counts before sending a request.
- `.env` loading is optional at runtime and no longer happens at import time.
- For tests or dependency injection, you can pass a preconfigured SDK client into `ClaudeClient`.
- Tool policies can enforce allowlists, denylists, confirmation gates, and argument size limits.

## ✅ Defensive Design

This wrapper is intentionally small:

- Minimal surface area for easier review
- Explicit input validation before model calls
- Policy checks before tool execution
- Safer packaging metadata and file handling
- Test coverage for the core client path

## ✨ Key Features

- **Lightweight Client**: A small wrapper around the Anthropic SDK with explicit validation.
- **Tool Policy Gates**: Allow, deny, or require confirmation for agent tool calls.
- **Safe Configuration**: Environment loading is opt-in at runtime, not a global import side effect.
- **Testable Design**: Inject a preconfigured client for unit tests and controlled runtimes.

## 🧩 Where It Fits

- Internal agents that need clear tool boundaries.
- Developer automation where prompts and actions must be reviewed independently.
- Security research demos where the safety model should be visible in the code.

## 🤝 Contributing

If you find this project useful, please **give it a ⭐ Star**! Contributions are welcome.

---
Built with ❤️ by [Informant254](https://github.com/Informant254)
