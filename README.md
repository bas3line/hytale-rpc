# Hytale Discord Rich Presence

<a href="https://rpc.ykira.com">
  <img src="https://img.shields.io/badge/Website-rpc.ykira.com-blueviolet?style=flat-square">
</a>

Show your Hytale activity on Discord!

![Discord RPC Preview](assets/rpc.png)

![Menu Bar Preview](assets/image2.png)

## Download

| Platform | Download | File |
|----------|----------|------|
| macOS | [Download](https://github.com/bas3line/hytale-rpc/releases/download/latest/HytaleRPC.dmg) | `HytaleRPC.dmg` |
| Windows | [Download](https://github.com/bas3line/hytale-rpc/releases/download/latest/HytaleRPC.exe) | `HytaleRPC.exe` |
| Linux | [Download](https://github.com/bas3line/hytale-rpc/releases/download/latest/HytaleRPC) | `HytaleRPC` |

## How to Use

**[macOS Setup Guide](installations/MACOS_SETUP.md)** - Download, install, and configure on macOS

**[Windows Setup Guide](installations/WINDOWS_SETUP.md)** - Download and install on Windows

**[Linux Setup Guide](installations/LINUX_SETUP.md)** - Terminal based RPC for Linux

## What It Shows

- In Main Menu
- Playing Singleplayer (with world name)
- Playing Multiplayer (with server)
- Time played

## Auto-Start (Optional)

**macOS:** System Settings → Login Items → Add the app

**Windows:** Press `Win+R`, type `shell:startup`, paste the exe there

**Linux:** Add to your desktop environment's startup applications or create a systemd user service

## Privacy Mode

Hide your server address from Discord Rich Presence. When enabled, instead of showing "Server: play.example.com", it will show "Online" or "Connecting...".

### Enabling Privacy Mode

**macOS:**
- Click the "H" menu bar icon
- Toggle "Privacy Mode" in the menu

Or via terminal:
```bash
# Enable
/Applications/HytaleRPC.app/Contents/MacOS/Hytale\ RPC --Privacy ON

# Disable
/Applications/HytaleRPC.app/Contents/MacOS/Hytale\ RPC --Privacy OFF
```

**Windows:**
- Right-click the system tray icon (if available)
- Toggle Privacy Mode

Or via command prompt:
```cmd
# Enable
HytaleRPC.exe --Privacy ON

# Disable
HytaleRPC.exe --Privacy OFF
```

**Linux:**
```bash
# Enable
./HytaleRPC --Privacy ON

# Disable
./HytaleRPC --Privacy OFF
```

**Default:** Privacy Mode is disabled (server address is shown)

## Support

- Issues: [Open an issue](https://github.com/bas3line/hytale-rpc/issues)
- Email: social@ykira.com

## Links

[<img src="assets/github.svg" width="20" height="20"> GitHub](https://github.com/bas3line/hytale-rpc) · [<img src="assets/discord.svg" width="20" height="20"> Discord Server](https://discord.gg/D5S6dh9Ww9)

## License

MIT