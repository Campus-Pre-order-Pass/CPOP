import tkinter as tk
from subprocess import Popen, PIPE
from threading import Thread
from queue import Queue
from tkinter import scrolledtext


def start_command_container(docker_command_entry, result_text, output_queue):
    # 获取文本框中的 Docker 命令
    docker_command = docker_command_entry.get()

    # 启动 Docker 容器的命令
    def run_command():
        process = Popen(docker_command, shell=True, stdout=PIPE,
                        stderr=PIPE, text=True, bufsize=1)

        # 開始監聽stdout和stderr
        for line in process.stdout:
            output_queue.put(line)
            result_text.insert(tk.END, line)

        for line in process.stderr:
            output_queue.put(line)
            result_text.insert(tk.END, line)

        result_text.see(tk.END)  # 滾動到最底部

    # 使用线程运行 Docker 命令
    thread = Thread(target=run_command)
    thread.start()


def update_output(result_text, output_queue):
    # 從Queue中不斷取得輸出，並顯示在Tkinter文本框中
    while True:
        line = output_queue.get()
        result_text.insert(tk.END, line)
        result_text.see(tk.END)  # 滾動到最底部
