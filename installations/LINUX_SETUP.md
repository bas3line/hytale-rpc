# Linux Setup Guide

## Download

1. Go to the [Releases page](https://github.com/bas3line/hytale-rpc/releases)
2. Download `HytaleRPC`

## Install

### Option 1: Run from Download Folder

1. Open terminal in your Downloads folder
2. Make executable:
   ```bash
   chmod +x HytaleRPC
   ```
3. Run:
   ```bash
   ./HytaleRPC
   ```

### Option 2: Install System-Wide

1. Open terminal in your Downloads folder
2. Make executable and copy:
   ```bash
   chmod +x HytaleRPC
   cp HytaleRPC ~/.local/bin/
   ```
3. Now you can run from anywhere:
   ```bash
   HytaleRPC
   ```

### Option 3: Double-Click

1. Right-click `HytaleRPC` → Properties → Permissions → Check "Allow executing file"
2. Close properties
3. Double-click the file

A terminal will open automatically and show status updates.

## Usage

1. Launch HytaleRPC (either from terminal or double-click)
2. Launch Discord (required for RPC to work)
3. Launch Hytale
4. Your status will appear on Discord:
   - `Waiting for Hytale...` → Launching the app
   - `Connected!` → Discord RPC connected
   - `In Main Menu` → Waiting in lobby
   - `Loading World` → Entering a world
   - `Playing Singleplayer` → Playing with world name
   - `Playing Multiplayer` → Playing with server address

## Supported Terminals

When double-clicking, the app automatically detects and uses your terminal:
- gnome-terminal (GNOME, Ubuntu)
- kitty
- xfce4-terminal (XFCE)
- konsole (KDE)
- xterm
- alacritty

## Troubleshooting

### Terminal doesn't open on double-click

Run from terminal instead:
```bash
./HytaleRPC
```

### Not showing on Discord

1. Make sure Discord is running
2. Make sure Hytale is running
3. Check you're in a supported region (RPC is blocked in some countries)
4. Look at the terminal output for status updates

### Permission denied

Make the file executable:
```bash
chmod +x HytaleRPC
```

## Auto-Start

### GNOME
1. Open Settings → Applications → Startup Applications
2. Add `HytaleRPC` with command: `/home/$USER/.local/bin/HytaleRPC`

### KDE
1. System Settings → Startup and Shutdown → Autostart
2. Add application: `HytaleRPC`

### XFCE
1. Settings Manager → Session and Startup → Application Autostart
2. Add application: `HytaleRPC`

### Other Desktop Environments
Or use systemd:
```bash
# Create service file
~/.config/systemd/user/hytale-rpc.service

# With content:
[Unit]
Description=Hytale Discord Rich Presence
After=graphical.target

[Service]
Type=simple
ExecStart=/home/$USER/.local/bin/HytaleRPC
Restart=always

[Install]
WantedBy=default.target

# Enable
systemctl --user enable --now hytale-rpc
```