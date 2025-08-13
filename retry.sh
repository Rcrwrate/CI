#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <command> [args...]"
    echo "Example: $0 curl -I https://example.com"
    exit 1
fi

# 初始化尝试次数计数器
attempt=1

# 循环直到命令成功
while true; do
    echo "Attempt $attempt: Executing '$@'"
    
    # 执行命令
    "$@"
    
    # 检查命令的退出状态
    if [ $? -eq 0 ]; then
        echo "Command succeeded after $attempt attempt(s)"
        break
    else
        echo "Command failed, retrying..."
        sleep 1  # 可选：添加延迟防止过于频繁的重试
        ((attempt++))
    fi
done