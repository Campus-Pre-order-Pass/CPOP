#!/bin/bash

# 虛擬環境名稱
venv_name=".venv"

# 判斷作業系統
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS"
    activate_script="activate"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Detected Windows"
    activate_script="Scripts/activate"
else
    echo "Unsupported operating system"
    exit 1
fi

# 檢查虛擬環境是否已存在
if [ -d "$venv_name" ]; then
  echo "Virtual environment '$venv_name' already exists."
  exit 1
fi

# 使用 python3 創建虛擬環境
python3 -m venv "$venv_name"

# 啟動虛擬環境
source "$venv_name/$activate_script"

# 在虛擬環境中安裝任何需要的套件
# 例如：pip install package_name

# 在這裡可以執行虛擬環境內的其他指令或操作

# 離開虛擬環境
deactivate

echo "Virtual environment '$venv_name' created and activated."
