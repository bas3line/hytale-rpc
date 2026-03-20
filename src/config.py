import platform
import os
from pathlib import Path

CLIENT_ID = "1461306150497550376"

def find_hytale_log_dir():
    if platform.system() == "Darwin":
        possible_dirs = [
            Path.home() / "Library/Application Support/Hytale/UserData/Logs",
            Path.home() / ".hytale/UserData/Logs",
        ]
    elif platform.system() == "Windows":
        appdata = Path(os.environ.get("APPDATA", ""))
        possible_dirs = [
            appdata / "Hytale/UserData/Logs",
            Path.home() / ".hytale/UserData/Logs",
        ]
    else:
        possible_dirs = [
            Path.home() / ".var/app/com.hypixel.HytaleLauncher/data/Hytale/UserData/Logs",
            Path.home() / ".var/app/com.hypixel.hytale/data/Hytale/UserData/Logs",
            Path.home() / ".local/share/Hytale/UserData/Logs",
            Path.home() / ".hytale/UserData/Logs",
            Path.home() / ".config/Hytale/UserData/Logs",
        ]

    for dir_path in possible_dirs:
        if dir_path.exists() and dir_path.is_dir():
            logs = list(dir_path.glob("*_client.log"))
            if logs:
                return dir_path

    return possible_dirs[0]

HYTALE_LOG_DIR = find_hytale_log_dir()

HYTALE_PROCESS_NAMES = [
    "hytale", "hytale.exe", "hytaleclient", "hytaleclient.exe",
    "hytalelauncher", "hytalelauncher.exe", "hytale-launcher",
]

DISCORD_PROCESS_NAMES = [
    "discord", "discord.exe", "discordcanary", "discordcanary.exe",
    "discordptb", "discordptb.exe",
]
