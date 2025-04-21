#mulchcli/tests/test_edge_cases.py

import pytest
from click.testing import CliRunner
from pathlib import Path
from mulchcli.cli import main

@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture
def isolated(runner, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path) as fs:
        yield fs, tmp_path

# ✅ Test 1: Double Init (idempotency)
def test_double_init_is_safe(isolated):
    runner = CliRunner()
    _, tmp_path = isolated
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result1 = runner.invoke(main, ["init", "proj1"])
        result2 = runner.invoke(main, ["init", "proj1"])

        assert result1.exit_code == 0
        assert "created" in result1.output.lower()

        assert result2.exit_code == 0
        assert "already exists" in result2.output.lower()

# ⚠️ Test 2: Set config on nonexistent project
def test_config_on_nonexistent_project(isolated):
    runner = CliRunner()
    _, tmp_path = isolated
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(main, [
            "config", "set", "app.mode", "production", "--project", "ghost"
        ])
        assert "not exist" in result.output.lower() or "config not found" in result.output.lower()

# 🧠 Test 3: Nested key handling
def test_nested_key_in_config(isolated):
    import tomllib
    _, tmp_path = isolated
    runner = CliRunner()

    # Setup
    runner.invoke(main, ["init", "proj1"])

    # Act
    runner.invoke(main, [
        "config", "set", "app.db.settings.host", "localhost", "--project", "proj1"
    ])

    # Assert
    config_file = tmp_path / "projects" / "proj1" / "configs" / "config.toml"
    assert config_file.exists()

    with open(config_file, "rb") as f:
        data = tomllib.load(f)

    assert data["app"]["db"]["settings"]["host"] == "localhost"
