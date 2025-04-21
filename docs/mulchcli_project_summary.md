# mulchcli — Project Summary

**Purpose**: Modular CLI for managing multi-project configuration environments.  
**Theme**: Planting seeds, preparing soil — metaphors for scalable software foundations.

## CLI Use Cases
- Scaffold new project directories under `projects/`
- Initialize TOML-based configuration schemas
- List available projects
- Validate or visualize project structure
- Future: rename, archive, or switch between environments

## mulchcli Directory Structure
```
mulchcli/
├── __init__.py
├── cli.py
├── project.py
├── config.py
tests/
└── test_cli.py
scripts/
├── install.sh
└── install.ps1
pyproject.toml
README.md
Makefile
```

## Target Environment Template (mysoftware_version)
Rooted in:
```
mysoftware_version/
├── projects/
├── src/mysoftware/
├── docs/
├── scripts/
├── media/
├── run.sh / .ps1 / .bat
├── pyproject.toml
├── Makefile
└── README.md
```

## Build + Publish Commands (Poetry)
```bash
poetry install
poetry build
poetry publish --build
poetry add mulchcli  # From other project
```

## Testing (with pytest)
```bash
poetry install --with dev
pytest
```

## Configuration Notes
- Default format: TOML
- Access pattern: `config.get(["some_key"])`
- Recommended folders: `configs/`, `addresses/`, `env/`
