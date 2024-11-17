# SillyTavern Windows 安装指南

本指南使用 Docker 进行简化安装，确保在各种 Windows 版本上的最大兼容性。

## 前提条件
- Windows 10/11
- WorldLM API 密钥（从 [worldlm.me](https://worldlm.me) 获取）
- 网络连接

## 安装步骤

### 1. 安装 Docker Desktop
1. 下载 [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. 运行安装程序
3. 按照安装向导进行操作
4. 根据提示重启计算机

### 2. 使用 Docker 安装 SillyTavern
1. 以管理员身份打开 PowerShell
2. 运行以下命令：
```powershell
# 创建 SillyTavern 目录
mkdir C:\SillyTavern
cd C:\SillyTavern

# 下载并运行 SillyTavern 容器
docker run -d `
  --name sillytavern `
  -p 5000:5000 `
  -v "${PWD}/data:/app/data" `
  ghcr.io/sillytavern/sillytavern:latest
```

### 3. 配置 WorldLM API
1. 打开浏览器访问 `http://localhost:5000`
2. 在 SillyTavern 设置中：
   - API 类型：选择 "WorldLM"
   - API URL：输入 `https://api.pplm.ai`
   - API 密钥：输入您的 WorldLM 密钥
   - 模型：选择 `gemini-1.5-pro` 或 `gemini-1.5-flash`

### 4. 创建桌面快捷方式（可选）
1. 创建新文件 `start_sillytavern.bat`：
```batch
@echo off
docker start sillytavern
start http://localhost:5000
```
2. 右键点击 > 发送到 > 桌面快捷方式

## 管理命令
```powershell
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
- **Docker Desktop 无法安装**：在 BIOS 中启用虚拟化
- **容器无法启动**：检查端口 5000 是否已被占用
- **API 连接失败**：验证您的 API 密钥和网络连接

## 提示
- 保持 Docker Desktop 在后台运行
- 定期更新以确保最佳性能
- 加入我们的 [Telegram 群组](https://t.me/+xun3ZpFI2Co2OTJl) 获取支持
