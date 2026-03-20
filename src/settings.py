import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".hytale-rpc"
CONFIG_FILE = CONFIG_DIR / "settings.json"


def get_privacy_mode() -> bool:
    try:
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
            return bool(data.get("privacy_mode", False))
        return False
    except Exception:
        return False


def set_privacy_mode(enabled: bool) -> None:
    try:
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        data: dict = {}
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
        data["privacy_mode"] = enabled
        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f)
    except Exception:
        pass
