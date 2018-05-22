.DEFAULT_GOAL := help

.PHONY: clean
clean: clean-tox clean-build clean-py ## Remove all file artifacts

.PHONY: clean-tox
clean-tox: ## Remove tox file artifacts
	rm -rf .tox/

.PHONY: clean-build
clean-build: ## Remove build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

.PHONY: clean-py
clean-py: ## Remove Python file artifacts
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
