.PHONY: help clean clean-pyc clean-test quality style setup test install dev-install

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

clean: clean-pyc clean-test ## Remove all build, test, coverage and Python artifacts

quality: check-quality ## Run code quality checks

style: format lint ## Run code formatting and linting

setup: install-dev ## Set up development environment (only run at project initialization)

test: run-tests ## Run tests

install: ## Install the package
	uv pip install -e .

install-dev: ## Install development dependencies
	uv pip install -e ".[dev]"

##### basic #####
run-tests:
	uv run pytest

format:
	uv run ruff format .

lint:
	uv run ruff check --fix .

check-quality:
	uv run ruff check .
	uv run ruff format --check .

#####  clean  #####
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf htmlcov/
	rm -rf .coverage
