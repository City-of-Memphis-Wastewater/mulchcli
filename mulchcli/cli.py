import click
from mulchcli.commands import init, config, list_projects

@click.group()
def main():
    """MulchCLI: Plant the seeds of your project."""
    pass

main.add_command(init.init_command)
main.add_command(config.config_command)
main.add_command(list_projects.list_projects_command)
