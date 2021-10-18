# -------------------
# Test & Lint
# -------------------
test:
	poetry run pytest

lint:
	poetry run black . --check
	poetry run isort . --check
	poetry run mypy .
	poetry run flake8 .

format:
	poetry run black .
	poetry run isort .

audit:
	poetry run safety check

check:
	make test
	make lint
	make audit
