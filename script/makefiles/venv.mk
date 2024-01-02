# venv.mk
# 定義虛擬環境的名稱
VENV_NAME := .venv

# 設定 Python 命令
PYTHON := $(VENV_NAME)/bin/python

# 檢查系統類型
UNAME := $(shell uname)



# 虛擬環境是否存在的檢查
venv-check:
	@if [ ! -d "$(VENV_NAME)" ]; then \
		echo "Creating virtual environment..."; \
		python -m venv $(VENV_NAME); \
	fi

activate-venv:
	. $(VENV_NAME)/bin/activate && \


# 安裝依賴
install: venv-check
	$(PYTHON) -m pip install -r requirements.txt

# 清理虛擬環境
clean:
	@echo "Cleaning up virtual environment..."
	@rm -rf $(VENV_NAME)

.PHONY: venv-check install run clean
