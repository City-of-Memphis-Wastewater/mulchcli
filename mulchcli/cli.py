# mulchcli/mulchcli/cli.py

import os
import click
from pathlib import Path
from mulchcli.commands import init, list_projects, config  # Import the commands

@click.group()
def main():
    """🌱 mulchcli — bootstrap and manage modular project trees."""
    pass

# Register the commands with the main group.
main.add_command(init.init_command)
main.add_command(list_projects.list_projects_command)
main.add_command(config.config_command)

# Run the CLI
if __name__ == "__main__":
    main()
