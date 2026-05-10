# 🤖 Claude Agent Core

[![Stars](https://img.shields.io/github/stars/Informant254/claude-agent-core?style=social)](https://github.com/Informant254/claude-agent-core/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Defensive Excellence](https://img.shields.io/badge/Defensive%20Excellence-input%20validation%20%7C%20tool%20policy-blue)](https://github.com/Informant254/claude-agent-core)

**Small, security-conscious Python primitives for building Claude-powered agents with explicit input validation and tool-call policy gates.**

## 🚀 Overview

In the rapidly evolving landscape of AI agents, ensuring security and predictable behavior is paramount. `claude-agent-core` addresses this critical need by providing a minimalist, auditable foundation for building Claude-powered agents. It empowers developers to implement robust safety measures, preventing unintended actions and maintaining control over agentic workflows. Unlike larger frameworks that might obscure security-critical logic, `claude-agent-core` offers transparent policy enforcement and explicit input validation, making it ideal for applications where trust and reliability are non-negotiable.



## 🛠️ Quick Start

Getting started with `claude-agent-core` is straightforward. Follow these steps to integrate secure AI agent capabilities into your Python projects.

### Installation

```bash
pip install git+https://github.com/Informant254/claude-agent-core.git
```

### Basic Usage

Here's how to make a basic call to the Claude API with built-in validation:
```python
from claude_agent_core.client import ClaudeClient

client = ClaudeClient(api_key="your-anthropic-api-key") # Ensure your API key is securely managed
response = client.generate_response("Explain quantum computing in simple terms.")
print(response)
```

### Policy-Driven Tool Calls

One of the core strengths of `claude-agent-core` is its ability to gate tool calls based on predefined policies, ensuring that your agent's actions are always within acceptable boundaries. This example demonstrates how to set up a `ToolPolicy` to control tool execution:
```python
from claude_agent_core import ToolPolicy

policy = ToolPolicy(
    allowed_tools={"search_docs", "summarize_file"}, # Only allow these tools
    confirmation_required={"summarize_file"}, # Require human confirmation for sensitive actions
    max_argument_bytes=4096, # Limit the size of tool arguments to prevent abuse
)

# Example: Evaluating a tool call
decision = policy.evaluate("summarize_file", {"path": "SECURITY.md"})

if decision.allowed and not decision.requires_confirmation:
    print("Tool call is safe to execute.")
elif decision.requires_confirmation:
    print(f"Tool call requires human confirmation: {decision.reason}")
else:
    print(f"Tool call denied: {decision.reason}")
```

This policy layer acts as a crucial safeguard, allowing you to define explicit boundaries for your agent's autonomy.





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

We welcome and appreciate contributions from the community! Whether it's a bug report, a new feature, or an improvement to the documentation, your input helps make `claude-agent-core` better.

Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on how to get started.

If you find this project useful, please **give it a ⭐ Star**! It helps us gain visibility and encourages continued development.

---
Built with ❤️ by [Informant254](https://github.com/Informant254)
