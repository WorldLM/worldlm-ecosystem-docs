# SillyTavern macOS 安装指南

本指南使用 Docker 进行简化安装，适用于 Intel 和 Apple Silicon Mac。

## 前提条件

- macOS 11 (Big Sur) 或更高版本
- WorldLM API 密钥（从 [worldlm.me](https://worldlm.me) 获取）
- 网络连接

## 安装步骤

### 1. 安装 Docker Desktop

1. 下载 [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
   - 根据您的 Mac 选择 Apple Silicon 或 Intel 版本
2. 安装 Docker Desktop
3. 从应用程序启动 Docker Desktop

### 2. 使用 Docker 安装 SillyTavern

1. 打开终端
2. 运行以下命令：
```bash
# 创建 SillyTavern 目录
mkdir ~/SillyTavern
cd ~/SillyTavern

# 下载并运行 SillyTavern 容器
docker run -d \
  --name sillytavern \
  -p 5000:5000 \
  -v "${PWD}/data:/app/data" \
  ghcr.io/sillytavern/sillytavern:latest
```

### 3. 配置 WorldLM API

1. 打开浏览器访问 `http://localhost:5000`
2. 在 SillyTavern 设置中：
   - API 类型：选择 "WorldLM"
   - API URL：输入 `https://api.pplm.ai`
   - API 密钥：输入您的 WorldLM 密钥
   - 模型：选择 `gemini-1.5-pro` 或 `gemini-1.5-flash`

### 4. 创建快速启动脚本（可选）

1. 创建启动脚本：
```bash
echo '#!/bin/bash
docker start sillytavern
open http://localhost:5000' > ~/SillyTavern/start_st.sh

chmod +x ~/SillyTavern/start_st.sh
```

2. 创建应用程序快捷方式：
```bash
# 创建自动操作应用程序
# 1. 打开自动操作
# 2. 创建新应用程序
# 3. 添加"运行 Shell 脚本"操作
# 4. 粘贴：~/SillyTavern/start_st.sh
# 5. 保存到应用程序文件夹，命名为 "SillyTavern"
```

## 管理命令

```bash
# 停止 SillyTavern
docker stop sillytavern

# 启动 SillyTavern
docker start sillytavern

# 查看日志
docker logs sillytavern

# 更新 SillyTavern
docker pull ghcr.io/sillytavern/sillytavern:latest
docker rm -f sillytavern
# 然后重复安装命令
```

## 故障排除

- **Docker Desktop 崩溃**：确保系统资源充足
- **容器无法启动**：检查端口 5000 是否被占用
- **性能问题**：
  - Apple Silicon：在 Docker 设置中启用"使用 Rosetta 进行 x86/amd64 模拟"
  - Intel：在 Docker 设置中确保足够的内存分配

## 提示

- 保持 Docker Desktop 在后台运行
- 定期更新以确保最佳性能
- 使用活动监视器检查资源使用情况
- 加入我们的 [Telegram 群组](https://t.me/+xun3ZpFI2Co2OTJl) 获取支持