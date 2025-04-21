# mulchcli/tests/test_cli.py

import pytest
from click.testing import CliRunner
from mulchcli.cli import main

@pytest.fixture
def runner():
    return CliRunner()

def test_version_command(runner):
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "mulchcli" in result.output.lower()

def test_help_command(runner):
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.output

def test_init_creates_project(runner, tmp_path):
    result = runner.invoke(main, ["init", "myproject"], obj={"root": tmp_path})
    assert result.exit_code == 0
    assert (tmp_path / "myproject").exists()

def test_list_projects_empty(runner, tmp_path):
    result = runner.invoke(main, ["list-projects"], obj={"root": tmp_path})
    assert "No projects found" in result.output
    
def test_init_creates_project(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(main, ["init", "testproj"])
        assert result.exit_code == 0
        assert "testproj" in (tmp_path / "projects").iterdir().__str__()

def test_list_projects(tmp_path):
    runner = CliRunner()
    (tmp_path / "projects" / "demo").mkdir(parents=True)
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(main, ["list-projects"])
        assert "demo" in result.output

# You could add tests for:
# - config generation (`mulchcli config`)
# - error conditions
# - edge cases (invalid characters, duplicate names, etc.)
