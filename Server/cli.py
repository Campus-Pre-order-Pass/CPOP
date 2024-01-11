# manage.py

import os
from django.core.management import execute_from_command_line
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--port', default=8000, help='Port number for the development server')
@click.option('--test', is_flag=True, help='Use test settings')
def runser(port, test):
    if test:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'Backend.settings_dev')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'Backend.settings_prod')

    execute_from_command_line(
        ['manage.py', 'runserver', f"0.0.0.0:{str(port)}"])


if __name__ == '__main__':
    cli()
