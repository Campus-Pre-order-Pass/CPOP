# 定義虛擬環境的名稱
VENV_NAME := .venv

# 設定 Python 命令
PYTHON := $(VENV_NAME)/bin/python

# 虛擬環境是否存在的檢查
venv-check:
    @if [ ! -d "$(VENV_NAME)" ]; then \
        echo "Creating virtual environment..."; \
        python3 -m venv $(VENV_NAME); \
    fi

# 安裝依賴
install: venv-check
    $(PYTHON) -m pip install -r requirements.txt

# 執行某些操作
run: venv-check
    $(PYTHON) your_script.py

# 清理虛擬環境
clean:
    @echo "Cleaning up virtual environment..."
    @rm -rf $(VENV_NAME)

.PHONY: venv-check install run clean
