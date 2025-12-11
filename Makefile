.PHONY: format

install:
	poetry install

install-dev:
	poetry install --with dev

lint:
	poetry run ruff check .

lint-fix:
	poetry run ruff check --fix .

format:
	poetry run ruff format .

check: lint
	poetry run ruff format --check .