# 使用 Node.js 14 作为基础镜像
FROM node:18-alpine

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录

COPY . .

# 安装依赖项
RUN npm install

# 构建静态文件
RUN npm run build

# 暴露端口
EXPOSE 9001
# 使用 Node.js 14 作为基础镜像
FROM node:18-alpine

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录

COPY . .

# 安装依赖项
RUN npm install

# 构建静态文件
RUN npm run build

# 暴露端口
EXPOSE 9001

# 启动命令
CMD ["npm", "start"]

