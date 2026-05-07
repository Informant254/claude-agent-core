# Security Policy

## Supported Versions

This repository is maintained on the `main` branch.

## Reporting a Vulnerability

If you find a security issue in this project:

1. Do not open a public issue with exploit details.
2. Contact the repository owner directly.
3. Include the affected version, impact, and clear reproduction steps.
4. Avoid sharing secrets, credentials, or tokens in the report.

## Defensive Expectations

- Treat API keys and environment variables as sensitive data.
- Do not commit `.env` files or hard-coded credentials.
- Validate all external inputs before sending them to model APIs.
