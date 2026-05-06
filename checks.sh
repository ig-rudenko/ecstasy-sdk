uv run ruff check --fix ecstasy_sdk scripts tests
uv run black -l 110 ecstasy_sdk scripts tests
uv run mypy ecstasy_sdk scripts tests
uv run --extra dev pytest