# 使用官方的 Python 基本映像作為基礎
FROM python:latest AS builder

# 將工作目錄設置為 Django 項目目錄
WORKDIR /app

# 安裝虛擬環境的依賴
RUN pip install virtualenv

# 創建一個名為 venv 的虛擬環境
RUN python -m venv venv

# 複製 Django 項目代碼到容器中
COPY . /app

# 複製 requirements.txt 到容器中
COPY requirements.txt /app/

# 安裝 Django 和其他所需的依賴
RUN . venv/bin/activate && pip install -r requirements.txt

# 第二阶段：最终镜像
FROM python:latest

# 将工作目录设置为 Django 项目目录
WORKDIR /app

# 从构建阶段复制虚拟环境
COPY --from=builder /app/venv /app/venv

# 复制 Django 项目代码到容器中
COPY . /app

# 运行 Django 应用程序
CMD ["venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
