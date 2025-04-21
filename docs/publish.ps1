# 1. Install deps
poetry install

# 2. Run tests / verify things work

# 3. Build package
poetry build

# 4. Publish (Test PyPI first)
poetry publish -r test-pypi

# 5. (Optional) Publish to real PyPI
poetry publish
