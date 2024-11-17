# SillyTavern macOS Installation Guide

This guide uses Docker for simplified installation and compatibility across Intel and Apple Silicon Macs.

## Prerequisites
- macOS 11 (Big Sur) or later
- WorldLM API key (obtain from [worldlm.me](https://worldlm.me))
- Internet connection

## Installation Steps

### 1. Install Docker Desktop
1. Download [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
   - Choose Apple Silicon or Intel version based on your Mac
2. Install Docker Desktop
3. Launch Docker Desktop from Applications

### 2. Install SillyTavern using Docker
1. Open Terminal
2. Run these commands:
```bash
# Create a directory for SillyTavern
mkdir ~/SillyTavern
cd ~/SillyTavern

# Download and run SillyTavern container
docker run -d \
  --name sillytavern \
  -p 5000:5000 \
  -v "${PWD}/data:/app/data" \
  ghcr.io/sillytavern/sillytavern:latest
```

### 3. Configure WorldLM API
1. Open your browser and go to `http://localhost:5000`
2. In SillyTavern settings:
   - API Type: Choose "WorldLM"
   - API URL: `https://api.pplm.ai`
   - API Key: Your WorldLM key
   - Model: Select `gemini-1.5-pro` or `gemini-1.5-flash`

### 4. Create Quick Launch Script (Optional)
1. Create a launch script:
```bash
echo '#!/bin/bash
docker start sillytavern
open http://localhost:5000' > ~/SillyTavern/start_st.sh

chmod +x ~/SillyTavern/start_st.sh
```

2. Create an Application shortcut:
```bash
# Create an Automator application
# 1. Open Automator
# 2. Create new Application
# 3. Add "Run Shell Script" action
# 4. Paste: ~/SillyTavern/start_st.sh
# 5. Save to Applications as "SillyTavern"
```

## Management Commands
```bash
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
- **Docker Desktop crashes**: Ensure sufficient system resources
- **Container won't start**: Check if port 5000 is in use
- **Performance issues**: 
  - For Apple Silicon: Enable "Use Rosetta for x86/amd64 emulation" in Docker settings
  - For Intel: Ensure sufficient RAM allocation in Docker settings

## Tips
- Keep Docker Desktop running in the background
- Regular updates ensure best performance
- Use Activity Monitor to check resource usage
- Join our [Telegram Group](https://t.me/+xun3ZpFI2Co2OTJl) for support