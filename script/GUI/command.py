import datetime
import os
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
from queue import Queue
from subprocess import PIPE
from psutil import Popen

from script.GUI.base.base_command import BaseCommand


class CommandProcessor(BaseCommand):
    pass
    # def run_command(self, docker_command: str):
    #     def run():
    #         process = Popen(docker_command, shell=True,
    #                         stdout=PIPE, stderr=PIPE)
    #         output, error = process.communicate()

    #         if process.returncode == 0:
    #             info_message = f"Info:\ninfo: {output.decode('utf-8')}\n"
    #             self.output_queue.put(f"{datetime.now()} - {info_message}")
    #         else:
    #             error_message = f"Error:\nerror: {error.decode('utf-8')}\n"
    #             self.output_queue.put(f"{datetime.now()} - {error_message}")

    #     # 使用线程运行 Docker 命令
    #     thread = Thread(target=run)
    #     thread.start()
