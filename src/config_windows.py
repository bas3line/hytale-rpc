import platform
import os
from pathlib import Path

CLIENT_ID = "1461306150497550376"

if platform.system() == "Darwin":
    HYTALE_LOG_DIR = Path.home() / "Library/Application Support/Hytale/UserData/Logs"
elif platform.system() == "Windows":
    HYTALE_LOG_DIR = Path(os.environ.get("APPDATA", "")) / "Hytale/UserData/Logs"
else:
    HYTALE_LOG_DIR = Path.home() / ".hytale/UserData/Logs"

HYTALE_PROCESS_NAMES = [
    "hytale", "hytale.exe", "hytaleclient", "hytaleclient.exe",
    "hytalelauncher", "hytalelauncher.exe", "hytale-launcher",
]

DISCORD_PROCESS_NAMES = [
    "discord", "discord.exe", "discordcanary", "discordcanary.exe",
    "discordptb", "discordptb.exe",
]