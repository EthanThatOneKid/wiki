# Contributing to wiki-framework

Thank you for your interest in contributing to wiki-framework! This guide will help you get started.

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/EthanThatOneKid/wiki.git
   cd wiki
   ```

2. **Install dependencies with uv:**
   ```bash
   uv sync --group dev
   ```

3. **Install pre-commit hooks (optional):**
   ```bash
   uv run pre-commit install
   ```

## Running Tests

```bash
# Run all tests
uv run pytest tests/ -v

# Run tests with coverage
uv run pytest tests/ -v --cov=wiki --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_shacl.py -v
```

## Linting and Type Checking

```bash
# Run ruff linter
uv run ruff check wiki/

# Run ruff formatter (auto-fix)
uv run ruff check wiki/ --fix

# Run mypy type checker
uv run mypy wiki/
```

## Commit Convention

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` - A new feature
- `fix:` - A bug fix
- `docs:` - Documentation only changes
- `style:` - Changes that do not affect the meaning of the code
- `refactor:` - A code change that neither fixes a bug nor adds a feature
- `test:` - Adding missing tests or correcting existing tests
- `chore:` - Changes to the build process or auxiliary tools

Examples:
```
feat: add wiki sync command for template updates
fix(shacl): handle empty shape directories gracefully
docs: update README with new CLI examples
test: add tests for frontmatter parsing
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Make your changes
4. Run tests and linting
5. Commit with conventional commit messages
6. Push to your fork (`git push origin feat/my-feature`)
7. Open a Pull Request

## Reporting Issues

Please use the [GitHub Issues](https://github.com/EthanThatOneKid/wiki/issues) page to report bugs or request features.

## Code of Conduct

By participating in this project, you agree to abide by our code of conduct (to be added).
