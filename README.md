# Claude Agent Core

**Lightweight • Secure • Zero-Trust** Claude 3.5 Sonnet Agent Framework

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A minimal, security-first Python library for building reliable agents with **Claude 3.5 Sonnet**.

## ✨ Why Choose Claude Agent Core?

- **Lightweight** — Minimal dependencies, fast startup
- **Security-First** — Built-in Fortress Gate (human + TOTP approval)
- **Zero-Trust Design** — Secrets never live in the agent process
- **Strong Policy Engine** — Automatic risk scoring and dangerous action blocking
- **Easy to Use** — Clean API for both beginners and advanced users

## 🚀 Quick Start

```bash
pip install claude-agent-core
```

```python
from claude_agent_core import ClaudeAgent, SecureFortressGate

# Initialize secure fortress (out-of-process)
fortress = SecureFortressGate()

agent = ClaudeAgent(
    api_key="sk-ant-...",
    fortress=fortress,           # Human + TOTP required for risky actions
    policy_enforcement="strict"
)

response = agent.chat("Summarize my latest research papers")
print(response.content)
```

## 🔥 Killer Demo: Secure Downloads Organizer

```bash
python examples/killer_downloads_organizer.py
```

This demo shows the agent intelligently organizing your Downloads folder while requiring **human approval + TOTP** for any file operations.

## Core Features

| Feature                    | Description |
|---------------------------|-----------|
| **SecureFortressGate**    | Out-of-process TOTP + human approval system |
| **ToolPolicy**            | Risk scoring, prompt injection protection, dangerous tool blocking |
| **Claude 3.5 Sonnet**     | Full tool calling + conversation memory |
| **DPAPI Vault**           | Secure secret storage (Windows 7 compatible) |
| **Audit Logging**         | Complete activity trail |

## Examples

- `examples/killer_downloads_organizer.py` → **Recommended starting point**
- `examples/secure_fortress_usage.py` → Full secure setup

## Security Philosophy

> "The agent is powerful, but never trusted blindly."

## Installation

```bash
git clone https://github.com/Informant254/claude-agent-core.git
cd claude-agent-core
pip install -e .
```

**Built with ❤️ in Nairobi**