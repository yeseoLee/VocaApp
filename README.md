# Python-AI-Template

Template repository for Python AI Project

## Features

### Code Formatting & Linting

- [ruff (black, isort, flake8)](https://github.com/astral-sh/ruff)

```bash
make setup # only run at project initialization
make style # run when Formatting & Linting
```

### Issue Template

- Feature
- Question
- Bug Report

### PR Template

## Getting Started

### Setup

1. **Clone this template:**

   ```bash
   git clone <your-repo-url>
   cd python-ai-template
   ```

2. **Install dependencies:**

   ```bash
   uv sync
   ```

3. **Setup development environment:**

   ```bash
   make setup
   ```

### Available Commands

- `make help` - Show all available commands
- `make setup` - Set up development environment
- `make test` - Run tests
- `make style` - Format and lint code
- `make quality` - Check code quality
- `make clean` - Clean build artifacts

## Testing

This template includes basic testing setup with pytest.

```bash
make test
```

## Project Structure

```
python-ai-template/
├── .github/
│   ├── ISSUE_TEMPLATE/     # GitHub issue templates
│   └── workflows/          # GitHub Actions workflows
├── src/                    # Source code
│   ├── __init__.py
│   └── main.py           # Main module
├── tests/                  # Test files
│   ├── __init__.py
│   └── test_sample.py     # Basic test examples
├── pyproject.toml         # Project configuration and dependencies
├── Makefile              # Development commands
└── README.md             # This file
```

## Configuration

- **Ruff**: Code linting and formatting (line length: 120, Python 3.11+)
- **Pytest**: Test discovery in `tests/` directory

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and run tests: `make test`
4. Format and lint your code: `make style`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
