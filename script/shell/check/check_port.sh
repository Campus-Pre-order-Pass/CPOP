#!/bin/bash

# 確認是否提供了 port 參數
if [ $# -eq 0 ]; then
  echo "Usage: $0 <port>"
  exit 1
fi

# 從命令行引數中取得 port
target_port=$1

# 使用 lsof 找到佔用指定 port 的進程
pid=$(lsof -ti tcp:$target_port)

if [ -z "$pid" ]; then
  echo "No process found on port $target_port."
else
  # 使用 kill 終止進程
  kill $pid
  echo "Process on port $target_port terminated."
fi
