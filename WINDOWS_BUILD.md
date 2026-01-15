# Building Hytale RPC for Windows

## Step 1: Install Python

1. Go to https://www.python.org/downloads/
2. Click the big yellow "Download Python" button
3. Run the installer
4. **IMPORTANT:** Check the box that says "Add Python to PATH"
5. Click "Install Now"

## Step 2: Download This Project

1. Go to https://github.com/bas3line/hytale-rpc
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file to your Desktop

## Step 3: Build the App

1. Press `Win + R` on your keyboard
2. Type `cmd` and press Enter
3. Copy and paste this command and press Enter:
```
cd %USERPROFILE%\Desktop\hytale-rpc-main
```
4. Copy and paste this command and press Enter:
```
scripts\build_windows.bat
```
5. Wait for it to finish (takes a few minutes)

## Step 4: Run the App

1. Open the `releases` folder on your Desktop inside `hytale-rpc-main`
2. Double-click `HytaleRPC.exe`
3. Look for the icon in your system tray (bottom right corner)
4. Done! Play Hytale and your Discord status will update automatically

## Run at Startup (Optional)

Want it to start automatically when Windows boots?

1. Press `Win + R`
2. Type `shell:startup` and press Enter
3. Copy `HytaleRPC.exe` from the `releases` folder into this window
4. Done! It will now start automatically

## Need Help?

Join our Discord: https://discord.gg/D5S6dh9Ww9
