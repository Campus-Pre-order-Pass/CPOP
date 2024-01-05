import os
from subprocess import PIPE
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import IntVar

from discord import Thread

# BaseGUI
from script.GUI.base.base_gui import BaseGUI


class GUI(BaseGUI):
    MAX_HEIGHT = 70
    MAX_WIDTH = 200

    def __init__(self, path: str, *args, **kwargs):
        super().__init__(path, *args, **kwargs)

        self.setup_window()

        self.setup_test_button()

        self.set_up_docker_button_frame()

        self.setup_input_frame()

        # self.setup_button_frame()

        self.setup_output_frame()

        self.setup_update_thread()

        self.bind('<Return>', self.on_enter_pressed)

    def setup_window(self):
        self.title("CPOP GUI")
        self.geometry("800x600")
        logo_path = os.path.abspath(os.path.join(
            os.getcwd(), "script/GUI/logo.png"))

        self.iconphoto(True, tk.PhotoImage(file=logo_path))

        # 創建 Label 顯示當前資料夾
        label = tk.Label(self, text=f"Root file: {self.current_folder}")
        label.pack(pady=10)

        # 创建 Label 显示版本信息
        version_label = tk.Label(self, text=f"Version: {self.conf['version']}")
        version_label.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

    def setup_test_button(self):
        # 創建一個 Frame，將 Checkbutton 放在這個 Frame 內
        self.button = tk.Frame(self, padx=10, pady=10)
        self.button.pack()

        # 使用 IntVar 來存儲勾選狀態
        self.test_var = IntVar()

        # Checkbutton 放在 self.button Frame 內，並指定 command
        test_checkbox = tk.Checkbutton(
            self.button, text="執行測試", variable=self.test_var, command=self.setTestFromCheckbox)
        test_checkbox.pack(pady=10)

        self.test_var.set(self.test)

    def setup_input_frame(self):
        self.frame1 = tk.Frame(self, padx=10, pady=10)
        self.frame1.pack()
        self.docker_command_label = tk.Label(self.frame1, text="Command:")
        self.docker_command_label.pack(side=tk.LEFT)
        self.docker_command_entry = tk.Entry(self.frame1, width=50)
        self.docker_command_entry.pack(side=tk.LEFT, padx=10)

    # def setup_button_frame(self):
    #     self.frame2 = tk.Frame(self, pady=10)
    #     self.frame2.pack()
    #     self.start_button = tk.Button(
    #         self.frame2, text="Start Docker Container", command=self.start_command_container)
    #     self.start_button.pack()

    def setup_output_frame(self):
        self.frame3 = tk.Frame(self, padx=10, pady=10)
        self.frame3.pack()
        self.result_text = scrolledtext.ScrolledText(
            self.frame3, height=self.MAX_HEIGHT, width=self.MAX_WIDTH)
        self.result_text.pack()

    def set_up_docker_button_frame(self):
        self.frame4 = tk.Frame(self, pady=10)
        self.frame4.pack()

        # 建立show
        show_button = tk.Button(
            self.frame4, text="show", command=self.show_docker)
        show_button.grid(row=0, column=1, padx=5)

        # 建立啟動按鈕
        start_button = tk.Button(
            self.frame4, text="strat", command=self.start_docker)
        start_button.grid(row=0, column=2, padx=5)

        # 建立建立按鈕
        create_button = tk.Button(
            self.frame4, text="rebuild", command=self.create_docker)
        create_button.grid(row=0, column=3, padx=5)

        # 建立刪除按鈕
        delete_button = tk.Button(
            self.frame4, text="rm", command=self.delete_docker)
        delete_button.grid(row=0, column=4, padx=5)

        # 建立停止按鈕
        stop_button = tk.Button(self.frame4, text="stop",
                                command=self.stop_docker)
        stop_button.grid(row=0, column=5, padx=5)

    def start_docker(self):
        # 同时显示信息消息框
        c = self.get_conf_command_v0("start")
        self.run_command(c)
        messagebox.showinfo("Docker", f"启动 Docker {c}")

    def show_docker(self):
        c = self.get_conf_command_v0("show")
        self.run_command(c)
        messagebox.showinfo("Docker", f"顯示 Docker {c}")

    def create_docker(self):
        c = self.get_conf_command_v0("build")
        self.run_command(c)
        messagebox.showinfo("Docker", f"build Docker {c}")

    def delete_docker(self):
        c = self.get_conf_command_v0("rm")
        self.run_command(c)
        messagebox.showinfo("Docker", f"刪除 Docker {c}")

    def stop_docker(self):
        c = self.get_conf_command_v0("stop")
        self.run_command(c)
        messagebox.showinfo("Docker", f"停止 Docker {c}")

    def start_command_container(self):
        docker_command = self.docker_command_entry.get()

        print(docker_command)
        thread = Thread(target=self.run_command, args=(docker_command,))
        thread.start()

    def on_enter_pressed(self, event=None):
        # 獲取當前具有焦點的 widget
        focused_widget = self.focus_get()

        # 檢查焦點的 widget 是否是 docker_command_entry
        if focused_widget == self.docker_command_entry:
            self.run_command(docker_command=self.docker_command_entry.get())


# if __name__ == "__main__":
#     app = GUI()
#     app.mainloop()
