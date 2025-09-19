# Contributing

1. Fork & clone
2. Create a branch: `git checkout -b feature/your-feature`
3. Run `pre-commit install` and `make test`
4. Commit with conventional message
5. Push & open a Pull Request using the template

### Standards
- Formatting: `black`, `isort`, `ruff`
- Tests: `pytest`
- Secrets: do not commit; use GitHub Actions secrets
