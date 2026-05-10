# Contributing to Claude Agent Core

 readme-improvements
We welcome contributions to `claude-agent-core`! By contributing, you help us build a more secure and robust foundation for AI agent development.

## How to Contribute

1.  **Fork the Repository:** Start by forking the `claude-agent-core` repository to your GitHub account.
2.  **Clone Your Fork:** Clone your forked repository to your local machine:
    ```bash
    git clone https://github.com/YOUR_USERNAME/claude-agent-core.git
    cd claude-agent-core
    ```
3.  **Create a New Branch:** Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    # or
    git checkout -b bugfix/issue-description
    ```
4.  **Set up Your Development Environment:**
    ```bash
    pip install -e .
    pip install -r requirements-dev.txt # if applicable
    ```
5.  **Make Your Changes:** Implement your feature or fix the bug. Ensure your code adheres to the existing style and conventions.
6.  **Write Tests:** Add unit tests for your changes to ensure they work as expected and prevent regressions. Run tests using `pytest`.
7.  **Update Documentation:** If your changes introduce new features or modify existing behavior, update the `README.md` and any relevant docstrings.
8.  **Commit Your Changes:** Write clear and concise commit messages.
    ```bash
    git commit -m "feat: Add new feature for X"
    # or
    git commit -m "fix: Resolve bug in Y"
    ```
9.  **Push to Your Fork:**
    ```bash
    git push origin feature/your-feature-name
    ```
10. **Create a Pull Request:** Open a pull request from your forked repository to the `main` branch of `Informant254/claude-agent-core`. Provide a detailed description of your changes and reference any related issues.

## Code Style

We generally follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code. Please use a linter (like `flake8` or `ruff`) and a formatter (like `black`) to ensure consistency.

## Reporting Bugs

If you find a bug, please open an issue on GitHub with a clear description, steps to reproduce, and expected behavior.

## Feature Requests

We welcome ideas for new features! Please open an issue to discuss your ideas before submitting a pull request.

Thank you for contributing!

First off, thank you for considering contributing to Claude Agent Core! It's people like you who make this tool better for everyone.

## 🚀 How Can I Contribute?

### Reporting Bugs
- Check the [GitHub Issues](https://github.com/Informant254/claude-agent-core/issues) to see if the bug has already been reported.
- If not, open a new issue. Include a clear title, a description of the problem, and steps to reproduce it.

### Suggesting Enhancements
- Open a new issue with the tag "enhancement".
- Explain why the feature would be useful and how it should work.

### Pull Requests
1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. Ensure the test suite passes.
4. Make sure your code follows the existing style.
5. Issue a pull request!

## 🛠️ Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/claude-agent-core.git
cd claude-agent-core

# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e .
pip install pytest
```

## 📜 Code of Conduct
By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

---
Built with ❤️ by [Informant254](https://github.com/Informant254)
 main
