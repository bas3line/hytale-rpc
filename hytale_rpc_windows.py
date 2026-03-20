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
from src.settings import set_privacy_mode

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
