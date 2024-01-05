# manage.py

import click
# GUI
from script.GUI.gui import GUI


@click.group()
def click():
    pass


@click.command()
def gui():
    # 在 Click 命令中调用 Tkinter GUI

    while True:
        try:
            app = GUI(path="./conf/gui.json")
            app.mainloop()
        except Exception as e:
            print(f"GUI crashed: {e}")


if __name__ == '__main__':
    click()
