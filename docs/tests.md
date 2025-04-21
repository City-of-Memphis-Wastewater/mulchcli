# Run all tests
poetry run pytest

# Just one test
poetry run pytest -k test_init_creates_project

# Run test_edge_cases file
poetry run pytest tests/test_edge_cases.py

# Run verbose to see which passed/failed
poetry run pytest -v