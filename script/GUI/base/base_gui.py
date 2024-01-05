import json
from subprocess import PIPE
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
from queue import Queue
from datetime import datetime
from psutil import Popen


from script.GUI.base.printer import PrinterTool

from script.GUI.command import CommandProcessor

import os


class BaseGUI(tk.Tk):
    """base gui class"""

    OK_CODE = 0
    ERROR = 1
    ORTHER = 127

    def __init__(self, path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.test = False

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
        # tags
        self.result_text.tag_configure("green", foreground="green")
        self.result_text.tag_configure("red", foreground="red")
        self.result_text.tag_configure("white", foreground="white")

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

            timestamp = f"\n \n{datetime.now().strftime('%Y-%m-%d %H:%M')} - "

            if process.returncode == 0:
                print(output.decode('utf-8'))
                # 插入標題文字到 Text widget 並套用 "green" 標籤
                self.result_text.insert(tk.END, timestamp, "white")
                # 插入內容文字到 Text widget 並套用 "white" 標籤
                self.result_text.insert(tk.END, "Info:\n", "green")
                self.result_text.insert(
                    tk.END, output.decode('utf-8') + "\n", "white")
            else:
                print(error.decode('utf-8'))
                # 插入標題文字到 Text widget 並套用 "red" 標籤
                self.result_text.insert(tk.END, timestamp, "white")
                # 插入內容文字到 Text widget 並套用 "white" 標籤
                self.result_text.insert(tk.END, "Error:\n", "red")
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
