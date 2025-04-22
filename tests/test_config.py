#mulchcli/tets/test_config.py

import pytest
from click.testing import CliRunner
from mulchcli.cli import main
import os
from pathlib import Path

@pytest.fixture
def runner():
    return CliRunner()

def test_set_and_get_config(tmp_path, runner): 
    project = "demo"
    key = "db.port"
    value = "5432"

    # Create project directory
    project_dir = tmp_path / "projects" / project / "configs"
    project_dir.mkdir(parents=True)

    config_path = project_dir / "config.toml"
    
    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Set config
        result = runner.invoke(main, ["config", "set", key, value, "--project", project])
        assert result.exit_code == 0
        assert config_path.exists()

        # Get config
        result = runner.invoke(main, ["config", "get", key, "--project", project])
        assert result.exit_code == 0
        assert value in result.output
