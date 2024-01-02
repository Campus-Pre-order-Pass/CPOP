#!/bin/bash

# 虛擬環境名稱
venv_name=".venv"

# 判斷作業系統
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS"
    activate_script="bin/activate"
    Source="source"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Detected Windows"
    activate_script="Scripts/activate"
    Source=""
else
    echo "Unsupported operating system"
    exit 1
fi

# 檢查虛擬環境是否存在
#if [ ! -d "$venv_name" ]; then
#  echo "Virtual environment '$venv_name' does not exist."
#  exit 1
#fi

# 進入虛擬環境
#$Source "$venv_name/$activate_script"

# 在這裡可以執行虛擬環境內的指令或操作

# 離開虛擬環境（選擇性）
# deactivate

echo "Entered virtual environment '$venv_name'."
