# SillyTavern Windows Installation Guide

This guide uses Docker for simplified installation and maximum compatibility across Windows versions.

## Prerequisites
- Windows 10/11
- WorldLM API key (obtain from [worldlm.me](https://worldlm.me))
- Internet connection

## Installation Steps

### 1. Install Docker Desktop
1. Download [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Run the installer
3. Follow the installation wizard
4. Restart your computer when prompted

### 2. Install SillyTavern using Docker
1. Open PowerShell as Administrator
2. Run these commands:
```powershell
# Create a directory for SillyTavern
mkdir C:\SillyTavern
cd C:\SillyTavern

# Download and run SillyTavern container
docker run -d `
  --name sillytavern `
  -p 5000:5000 `
  -v "${PWD}/data:/app/data" `
  ghcr.io/sillytavern/sillytavern:latest
```

### 3. Configure WorldLM API
1. Open your browser and go to `http://localhost:5000`
2. In SillyTavern settings:
   - API Type: Choose "WorldLM"
   - API URL: `https://api.pplm.ai`
   - API Key: Your WorldLM key
   - Model: Select `gemini-1.5-pro` or `gemini-1.5-flash`

### 4. Create Desktop Shortcut (Optional)
1. Create a new file `start_sillytavern.bat`:
```batch
@echo off
docker start sillytavern
start http://localhost:5000
```
2. Right-click > Send to > Desktop (create shortcut)

## Management Commands
```powershell
# Stop SillyTavern
docker stop sillytavern

# Start SillyTavern
docker start sillytavern

# View logs
docker logs sillytavern

# Update SillyTavern
docker pull ghcr.io/sillytavern/sillytavern:latest
docker rm -f sillytavern
# Then repeat the installation command
```

## Troubleshooting
- **Docker Desktop won't install**: Enable virtualization in BIOS
- **Container won't start**: Check if port 5000 is already in use
- **API Connection Failed**: Verify your API key and internet connection

## Tips
- Keep Docker Desktop running in the background
- Regular updates ensure best performance
- Join our [Discord](https://discord.gg/worldlm) for support
