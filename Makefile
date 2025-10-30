# Files
REQ_RUNTIME := requirements.txt
REQ_DEV     := requirements-dev.txt

# Default goal
.DEFAULT_GOAL := help

.PHONY: help install-dev install-prod test pre-commit format lint typecheck clean

help: ## Show available targets
	@printf "\nUsage: make <target>\n\nTargets:\n"
	@awk -F':.*##' '/^[a-zA-Z0-9_\-]+:.*##/ {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install-dev: ## Install development dependencies
	@echo "Installing development dependencies..."
	python -m pip install -r $(REQ_DEV)

install-prod: ## Install production dependencies
	@echo "Installing production dependencies..."
	python -m pip install -r $(REQ_RUNTIME)

test: ## Run tests
	@echo "Running tests..."
	pytest

# “manual pre-commit” bundle (no git hooks involved)
pre-commit: format lint typecheck ## Run format+lint+types on demand

format: ## Auto-format code
	@echo "Formatting with Black and Ruff..."
	black .
	ruff format .

lint: ## Lint (Ruff); add --fix to auto-fix
	@echo "Linting with Ruff..."
	ruff check .

typecheck: ## Static type checking
	@echo "Type checking with mypy..."
	mypy .

clean: ## Remove caches
	@echo "Cleaning caches..."
	rm -rf .pytest_cache .mypy_cache .ruff_cache