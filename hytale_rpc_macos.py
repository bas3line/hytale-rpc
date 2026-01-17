import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from pypresence import Presence
    import psutil
except ImportError:
    print("Installing dependencies...")
    os.system(f"{sys.executable} -m pip install pypresence psutil rumps --quiet")

from src.ui import run_app

if __name__ == "__main__":
    run_app()