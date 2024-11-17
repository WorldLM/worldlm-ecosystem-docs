# SillyTavern Android 安装指南

## 前提条件
开始之前，请确保您有：
- Android 7.0 或更高版本，至少 1GB 可用存储空间
- 有效的 WorldLM API 密钥（在 worldlm.me 注册）
- 稳定的网络连接
- 基本的复制粘贴命令能力

## 快速安装

### 1. 安装 Termux
1. 从 F-Droid 下载 Termux
2. 打开 Termux 并更新包管理器：
```bash
pkg update -y && pkg upgrade -y
```
3. 安装必需的依赖：
```bash
pkg install git nodejs -y
```
4. 启用存储访问：
```bash
termux-setup-storage
```

### 2. 安装 SillyTavern
1. 克隆 SillyTavern 仓库：
```bash
git clone https://github.com/SillyTavern/SillyTavern.git
cd SillyTavern
```
2. 安装必要的依赖：
```bash
npm install
```

### 3. 配置 WorldLM API
1. 启动 SillyTavern 服务器：
```bash
node server.js
```
2. 打开浏览器访问：`http://localhost:5000`
3. 在设置菜单中配置 WorldLM API：
   - **API 类型：** 选择 "WorldLM"
   - **API URL：** 输入 `https://api.pplm.ai`
   - **API 密钥：** 粘贴您的个人密钥（例如：`sk-xxx`）
   - **模型：** 选择 `gemini-1.5-pro` 获得高性能或 `gemini-1.5-flash` 获得更快响应

### 4. 创建快速启动快捷方式
1. 创建自定义快捷方式：
```bash
mkdir -p ~/.shortcuts
nano ~/.shortcuts/start_st.sh
```
2. 将以下内容粘贴到脚本中：
```bash
#!/bin/bash
cd ~/SillyTavern
node server.js
```
3. 保存脚本并使其可执行：
```bash
chmod +x ~/.shortcuts/start_st.sh
```
4. 使用 Termux 应用将快捷方式添加到主屏幕

## 故障排除
- **服务器无法启动：**
  - 确保没有其他应用使用 5000 端口（如 VPN 或其他本地服务器）
- **API 连接失败：**
  - 仔细检查您的 API 密钥并验证设备是否有网络连接
- **响应时间慢：**
  - 切换到 `gemini-1.5-flash` 模型以获得更快但资源消耗更少的交互
- **存储问题：**
  - 重新运行 `termux-setup-storage` 并确保 Termux 有适当的权限

## 提示
- 要在后台运行 SillyTavern：
```bash
nohup node server.js &
```
- 检查日志以排查问题：
```bash
ls logs/
```
- 加入我们的 [Telegram 群组](https://t.me/+xun3ZpFI2Co2OTJl) 获取帮助和更新