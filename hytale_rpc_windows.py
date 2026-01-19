import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from pypresence.presence import Presence
    import psutil
except ImportError:
    print("Installing dependencies...")
    os.system(f"{sys.executable} -m pip install pypresence psutil pystray pillow --quiet")

from src.ui import run_app

def set_privacy_mode(enabled):
    import json
    import pathlib
    config_dir = pathlib.Path.home() / ".hytale-rpc"
    config_dir.mkdir(parents=True, exist_ok=True)
    config_file = config_dir / "settings.json"
    data = {}
    if config_file.exists():
        with open(config_file, "r") as f:
            data = json.load(f)
    data["privacy_mode"] = enabled
    with open(config_file, "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--Privacy":
        if sys.argv[2] == "ON":
            set_privacy_mode(True)
            print("Privacy mode enabled")
        elif sys.argv[2] == "OFF":
            set_privacy_mode(False)
            print("Privacy mode disabled")
        else:
            print("Usage: HytaleRPC.exe --Privacy ON|OFF")
        sys.exit(0)
    run_app()