# manage.py

import os
from django.core.management import execute_from_command_line
import click
from script.GUI.base.base_gui import TestGui
# GUI
from script.GUI.gui import GUI


@click.group()
def cli():
    pass


@cli.command()
def gui():
    # 在 Click 命令中调用 Tkinter GUI
    while True:
        try:
            app = GUI(path="./conf/gui.json")
            app.mainloop()
        except Exception as e:
            print(f"GUI crashed: {e}")


@cli.command()
def test():
    g = TestGui()
    g.mainloop()


@cli.command()
@click.option('--port', default=8000, help='Port number for the development server')
@click.option('--test', is_flag=True, help='Use test settings')
def runser(port, test):
    print(test)
    if test:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'Server.Backend.settings_test')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'Server.Backend.settings_test')

    execute_from_command_line(
        ['manage.py', 'runserver', f"0.0.0.0:{str(port)}"])


if __name__ == '__main__':
    cli()
