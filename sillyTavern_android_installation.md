# SillyTavern on Android: Quick Installation and Setup Guide

This guide will help you set up SillyTavern on your Android device and connect it to the **WorldLM Key** service, leveraging models like `gemini-1.5-pro` and `gemini-1.5-flash`.

---

## Prerequisites

1. **Android Device** with internet access.
2. **WorldLM Key** service details:
   - **API Endpoint**: `https://api.pplm.ai`
   - **API Key**: Obtain your key from the service (e.g., `sk-xxx`).
3. **Termux App** (a Linux terminal emulator for Android).

---

## Step 1: Install Termux

1. **Download Termux**:
   - Visit the [F-Droid Termux page](https://f-droid.org/) or [Termux official site](https://termux.dev/).
   - Download and install the APK file.

2. **Open Termux**:
   - Launch Termux and update the package manager:
     ```bash
     pkg update -y && pkg upgrade -y
     ```

---

## Step 2: Install Dependencies

In Termux, install the required software:

1. Install **Git**:
   ```bash
   pkg install git -y
Install Node.js:

bash
Copy code
pkg install nodejs -y
Enable storage access (if needed):

bash
Copy code
termux-setup-storage
Step 3: Clone and Install SillyTavern
Clone the SillyTavern Repository:

bash
Copy code
git clone https://github.com/SillyTavern/SillyTavern.git
cd SillyTavern
Install Dependencies:

bash
Copy code
npm install
Start the SillyTavern Server:

bash
Copy code
node server.js
Access the Application:

Open your browser and visit: http://localhost:5000
Step 4: Configure the WorldLM Key API
Navigate to Settings:

In the SillyTavern interface, go to the Settings menu.
Enter API Details:

Endpoint URL: https://api.pplm.ai
API Key: Enter your WorldLM Key (e.g., sk-xxx).
Select a Model:

Choose between:
gemini-1.5-pro
gemini-1.5-flash
Save Settings:

Click Save to finalize the configuration.
Step 5: Create a Desktop Shortcut
Make launching SillyTavern more convenient by creating a shortcut:

Install Termux
:

Download and install Termux
.
Create a Shortcut Script:

Open Termux and create a script:
bash
Copy code
mkdir -p ~/.shortcuts
nano ~/.shortcuts/start_sillytavern.sh
Add the following content:
bash
Copy code
#!/bin/bash
cd ~/SillyTavern
node server.js
Save and Grant Permissions:

Save the file (Ctrl+O, then Ctrl+X).
Make it executable:
bash
Copy code
chmod +x ~/.shortcuts/start_sillytavern.sh
Add a Widget:

Add a Termux Widget to your home screen.
Assign the start_sillytavern.sh script to the widget.
Step 6: Troubleshooting and Tips
Cannot Access http://localhost:5000?

Ensure the server is running in Termux:
bash
Copy code
cd ~/SillyTavern
node server.js
Run in the Background:

To keep SillyTavern running after closing Termux:
bash
Copy code
nohup node server.js &
Reconfigure API Key:

Go back to Settings in SillyTavern to update your API key.