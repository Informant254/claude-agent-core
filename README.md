# 🤖 Claude Agent Core

[![Stars](https://img.shields.io/github/stars/Informant254/claude-agent-core?style=social)](https://github.com/Informant254/claude-agent-core/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Claude 3.5 Sonnet](https://img.shields.io/badge/Claude-3.5%20Sonnet-orange.svg)](https://www.anthropic.com/claude)

**High-performance, lightweight Python primitives for building Claude-powered agents.**

## 🚀 Main Entry Point: `ClaudeAgent`

The recommended way to use the library is through the new `ClaudeAgent` class in `agent.py`:

```python
from claude_agent_core import ClaudeAgent

agent = ClaudeAgent(api_key="your-anthropic-key")

response = agent.chat("Explain quantum computing in simple terms.")
print(response.content)
```

## Features

- Clean `ClaudeAgent` class as main interface
- Built-in conversation history management
- Strong policy enforcement
- Hardened error handling
- Low-level `ClaudeClient` still available for advanced use

## Installation

```bash
pip install git+https://github.com/Informant254/claude-agent-core.git
```

... (rest of your existing README content preserved)
