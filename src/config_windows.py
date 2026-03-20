import os
from pathlib import Path

CLIENT_ID = "1461306150497550376"

HYTALE_LOG_DIR = Path(os.environ.get("APPDATA", "")) / "Hytale/UserData/Logs"

HYTALE_PROCESS_NAMES = [
    "hytale", "hytale.exe", "hytaleclient", "hytaleclient.exe",
    "hytalelauncher", "hytalelauncher.exe", "hytale-launcher",
]

DISCORD_PROCESS_NAMES = [
    "discord", "discord.exe", "discordcanary", "discordcanary.exe",
    "discordptb", "discordptb.exe",
]
