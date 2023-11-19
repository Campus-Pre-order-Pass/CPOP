# 使用官方的 Python 基本映像作為基礎
FROM python:latest

# 將工作目錄設置為 Django 項目目錄
WORKDIR /app

# 安裝虛擬環境的依賴
RUN pip install virtualenv

# 創建一個名為 venv 的虛擬環境
RUN python -m venv venv

# 啟用虛擬環境
RUN . venv/bin/activate

# 複製 Django 項目代碼到容器中
COPY . /app

# 複製 requirements.txt 到容器中
COPY requirements.txt /app/

# 安裝 Django 和其他所需的依賴
RUN pip install -r requirements.txt

# 運行 Django 應用程序
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# docker build -t cpop-server-image .
