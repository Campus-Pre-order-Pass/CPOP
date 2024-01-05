# manage.py

import click
from django.core.management import execute_from_command_line


# GUI
from script.GUI.gui import GUI


@click.group()
def click():
    pass


@click.command()
def gui():
    # 在 Click 命令中调用 Tkinter GUI
    app = GUI(path="./conf/gui.json")
    app.mainloop()


if __name__ == '__main__':
    click()
