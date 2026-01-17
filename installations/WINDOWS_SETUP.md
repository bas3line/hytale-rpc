# Windows Setup Guide

## Download

1. Go to the [Releases page](https://github.com/bas3line/hytale-rpc/releases)
2. Download `HytaleRPC.exe`

## Install

### Option 1: Run from Downloads

1. Open your Downloads folder
2. Double-click `HytaleRPC.exe`
3. If Windows Security warns you, click "More info" then "Run anyway"

### Option 2: Install to Program Files

1. Choose a location (e.g., `C:\Program Files\HytaleRPC`)
2. Create the folder and put `HytaleRPC.exe` inside
3. Right-click the exe → Create shortcut
4. Move the shortcut to your Desktop or Start Menu

## Usage

1. Launch `HytaleRPC.exe`
2. Look for the icon in your system tray (bottom right corner)
3. Launch Discord (required for RPC to work)
4. Launch Hytale
5. Your status will appear on Discord:
   - `Waiting for Hytale...` → Launching the app
   - `Connected!` → Discord RPC connected
   - `In Main Menu` → Waiting in lobby
   - `Loading World` → Entering a world
   - `Playing Singleplayer` → Playing with world name
   - `Playing Multiplayer` → Playing with server address

## System Tray Icon

Click the system tray icon to see:
- Current status
- GitHub link
- Discord server link
- Quit option

## Auto-Start

1. Press `Win + R`
2. Type `shell:startup` and press Enter
3. Copy `HytaleRPC.exe` to this folder
4. Done! It will start automatically

## Troubleshooting

### "Windows protected your PC"

1. Click "More info"
2. Click "Run anyway"

### Not showing on Discord

1. Make sure Discord is running
2. Make sure Hytale is running
3. Check the system tray icon - if it shows status, it's working
4. Try restarting Discord and HytaleRPC

### Can't find system tray icon

1. Check if the app is running (look in Task Manager)
2. Click the arrow in the system tray to show hidden icons
3. The icon should be there

### App crashes or doesn't start

1. Make sure you're using Windows 10 or later
2. Check your antivirus isn't blocking it
3. Try running as administrator

## Uninstall

1. Quit HytaleRPC (right-click system tray icon → Quit)
2. Delete `HytaleRPC.exe`
3. Remove from startup folder if added