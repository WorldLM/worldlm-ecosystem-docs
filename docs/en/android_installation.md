# SillyTavern Android Installation Guide

## Prerequisites
Before you begin, ensure you have:
- Android 7.0 or higher with at least 1GB of free storage
- A valid WorldLM API Key (register at worldlm.me)
- A stable internet connection
- Basic familiarity with copy-pasting commands

## Quick Installation

### 1. Install Termux
1. Download Termux from F-Droid
2. Open Termux and update your package manager:
```bash
pkg update -y && pkg upgrade -y
```
3. Install required dependencies:
```bash
pkg install git nodejs -y
```
4. Enable storage access:
```bash
termux-setup-storage
```

### 2. Install SillyTavern
1. Clone the SillyTavern repository:
```bash
git clone https://github.com/SillyTavern/SillyTavern.git
cd SillyTavern
```
2. Install necessary dependencies:
```bash
npm install
```

### 3. Configure WorldLM API
1. Start the SillyTavern server:
```bash
node server.js
```
2. Open your browser and visit: `http://localhost:5000`
3. Configure the WorldLM API in the settings menu:
   - **API Type:** Select "WorldLM"
   - **API URL:** Enter `https://api.pplm.ai`
   - **API Key:** Paste your personal key (e.g., `sk-xxx`)
   - **Model:** Choose `gemini-1.5-pro` for high performance or `gemini-1.5-flash` for faster response

### 4. Create Quick Launch Shortcut
1. Create a custom shortcut:
```bash
mkdir -p ~/.shortcuts
nano ~/.shortcuts/start_st.sh
```
2. Paste the following into the script:
```bash
#!/bin/bash
cd ~/SillyTavern
node server.js
```
3. Save the script and make it executable:
```bash
chmod +x ~/.shortcuts/start_st.sh
```
4. Use the Termux app to add the shortcut to your home screen

## Troubleshooting
- **Server won't start:**
  - Ensure no other apps are using port 5000 (e.g., VPNs or other local servers)
- **API Connection Failed:**
  - Double-check your API key and verify that your device has internet access
- **Slow Response Times:**
  - Switch to the `gemini-1.5-flash` model for faster but less resource-intensive interactions
- **Storage Issues:**
  - Run `termux-setup-storage` again and ensure Termux has proper permissions

## Tips
- To run SillyTavern in the background:
```bash
nohup node server.js &
```
- Check logs for issues:
```bash
ls logs/
```
- Join the WorldLM Discord for help and updates