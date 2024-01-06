from ttkbootstrap.constants import *
import json
from subprocess import PIPE
from time import strftime
import tkinter as tk
from threading import Thread
from queue import Queue
from datetime import datetime
from tkinter import messagebox
from psutil import Popen

import ttkbootstrap as ttk
from ttkbootstrap.dialogs.dialogs import Messagebox
from script.GUI.base.printer import PrinterTool

from script.GUI.command import CommandProcessor

import os


class BaseGUI(ttk.Window):
    """base gui class"""

    OK_CODE = 0
    ERROR = 1
    ORTHER = 127

    def __init__(self, path: str, *args, **kwargs):
        super().__init__(*args, **kwargs, themename="superhero")

        self.test = False
        self.start_time = datetime.now()

        self.conf = self.get_conf(path=path)

        self.current_folder = os.getcwd()

        self.output_queue = Queue()

        self.printer = PrinterTool()

        # self.command = CommandProcessor()

    def setTestFromCheckbox(self):
        # 在這裡執行當 Checkbutton 狀態更改時要執行的操作
        # print(self.test_var.get())
        self.test = bool(self.test_var.get())

        print(f"test  = {self.test}")

    def update_output(self):
        # tags colors
        self.result_text.tag_configure("green", foreground="green")
        self.result_text.tag_configure("red", foreground="red")
        self.result_text.tag_configure("white", foreground="white")
        self.result_text.tag_configure("orange", foreground="#FFA500")

        while True:
            line = self.output_queue.get()
            self.result_text.insert(tk.END, line)
            self.result_text.see(tk.END)

    def run_command(self, docker_command: str):
        def run():
            process = Popen(docker_command, shell=True,
                            stdout=PIPE, stderr=PIPE)
            output, error = process.communicate()

            self.result_text.insert(tk.END, "="*60, "white")
            self.result_text.insert(
                tk.END, f"\n \ncommand = {docker_command}", "orange")

            timestamp = f"\n \n{datetime.now().strftime('%Y-%m-%d %H:%M')} - "

            if process.returncode == 0:
                print(output.decode('utf-8'))
                # 插入標題文字到 Text widget 並套用 "green" 標籤
                self.result_text.insert(tk.END, timestamp, "white")
                # 插入內容文字到 Text widget 並套用 "white" 標籤
                self.result_text.insert(tk.END, "Info:\n \n", "green")
                self.result_text.insert(
                    tk.END, output.decode('utf-8') + "\n", "white")
            else:
                print(error.decode('utf-8'))
                # 插入標題文字到 Text widget 並套用 "red" 標籤
                self.result_text.insert(tk.END, timestamp, "white")
                # 插入內容文字到 Text widget 並套用 "white" 標籤
                self.result_text.insert(tk.END, "Error:\n \n", "red")
                self.result_text.insert(
                    tk.END, error.decode('utf-8') + "\n", "white")

            self.result_text.see(tk.END)  # 捲動到最底部

        # 使用線程運行 Docker 命令
        thread = Thread(target=run)
        thread.start()

        return thread

    def setup_update_thread(self):
        update_thread = Thread(target=self.update_output)
        update_thread.daemon = True
        update_thread.start()

    def execution_time_frame(self):
        self.runtime_label = tk.Label(self)
        self.runtime_label.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

        # 更新程序运行时间
        self.update_runtime()

    def update_runtime(self):
        # 计算程序运行时间
        elapsed_time = datetime.now() - self.start_time
        hours, remainder = divmod(elapsed_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # 格式化时间显示
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

        # 更新 Label 的文本
        self.runtime_label.config(
            text=f"Time: {formatted_time}")

        # 每隔1000毫秒（1秒）调用一次update_runtime方法
        self.after(1000, self.update_runtime)

    def show_messgaebox_with_run_command(self, name: str, title: str, description: None) -> None:
        c = self.get_conf_command_v0(title)
        self.run_command(c)
        # messagebox.showinfo(f"{name}", f"{description} {name} {c}")
        Messagebox.show_info(
            message=f"{name} {description} {name} {c}", title="COMMAND", parent=self)

    # def print_terminal_message(self, message: any, returncode: int = 0,  *args, **kwargs):
    #     """"Print a terminal message and color"""
    #     return f"error: {message.decode('utf-8')}\n"

    def get_conf(self, path: str) -> any:
        try:
            with open(path, 'r') as file:
                config_data = json.load(file)
                # test
                self.test = config_data["default"].get("test", False)
                return config_data
        except FileNotFoundError:
            print(
                f"Error: File not found at path {path} in {self.__class__.__module__}. in. {self.__class__.__name__}")
            return None
        except json.JSONDecodeError as e:
            print(
                f"Error decoding JSON: {e} in {self.__class__.__module__}. in {self.__class__.__name__}")
            return None

    def get_conf_command_v0(self, name: str) -> str | None:
        # print(self.test)

        if self.conf is not None and "commands" in self.conf:
            if not self.test:
                matching_commands = [
                    cmd["command"] for cmd in self.conf["commands"] if cmd.get("title") == name]
            else:
                matching_commands = [cmd["test-command"]
                                     for cmd in self.conf["commands"] if cmd.get("title") == name]

            if matching_commands:
                return matching_commands[0]
            else:
                print(f"No matching command found for title '{name}'")
                return None
        else:
            print("Error: Configuration data is missing or invalid.")
            return None

    # @staticmethod
    # def show_info(message, title=" ", parent=None, alert=False, **kwargs):
    #     """Display a modal dialog box with an OK button and an INFO
    #     icon.

    #     ![](../../assets/dialogs/messagebox-show-info.png)

    #     Parameters:

    #         message (str):
    #             A message to display in the message box.

    #         title (str):
    #             The string displayed as the title of the messagebox. This
    #             option is ignored on Mac OS X, where platform guidelines
    #             forbid the use of a title on this kind of dialog.

    #         parent (Union[Window, Toplevel]):
    #             Makes the window the logical parent of the message box. The
    #             message box is displayed on top of its parent window.

    #         alert (bool):
    #             Specified whether to ring the display bell.

    #         **kwargs (Dict):
    #             Other optional keyword arguments.
    #     """
    #     dialog = MessageDialog(
    #         message=message,
    #         title=title,
    #         alert=alert,
    #         parent=parent,
    #         buttons=["OK:primary"],
    #         icon=Icon.info,
    #         localize=True,
    #         **kwargs
    #     )
    #     if "position" in kwargs:
    #         position = kwargs.pop("position")
    #     else:
    #         position = None
    #     dialog.show(position)


class TestGui(ttk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, themename="superhero")

        b1 = ttk.Button(self, text="Submit", bootstyle="success")
        b1.pack(side=tk.LEFT, padx=5, pady=10)

        b2 = ttk.Button(self, text="Submit", bootstyle="info-outline")
        b2.pack(side=tk.LEFT, padx=5, pady=10)
