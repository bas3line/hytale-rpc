import re
import time
import os
from .config import HYTALE_LOG_DIR

LOG_PATTERNS = {
    "main_menu": re.compile(r"Changing from Stage \w+ to MainMenu"),
    "singleplayer_world": re.compile(r'Connecting to singleplayer world "([^"]+)"'),
    "singleplayer_create": re.compile(r'Creating new singleplayer world in ".*/Saves/([^"]+)"'),
    "multiplayer_connect": re.compile(r'Connecting to (?:multiplayer|dedicated) server'),
    "server_connect": re.compile(r'Opening Quic Connection to ([^:]+):(\d+)'),
    "in_game": re.compile(r'GameInstance\.StartJoiningWorld\(\)'),
}


class LogWatcher:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current_log = None
        self.log_position = 0
        self.game_state = "main_menu"
        self.world_name = ""
        self.server_address = ""
        self.is_multiplayer = False
        self.world_start_time = None
        self.initialized = False

    def find_latest_log(self):
        if not HYTALE_LOG_DIR.exists():
            return None
        logs = list(HYTALE_LOG_DIR.glob("*_client.log"))
        return max(logs, key=lambda f: f.stat().st_mtime) if logs else None

    def update(self):
        latest = self.find_latest_log()
        if not latest:
            return

        if self.current_log != latest:
            self.current_log = latest
            self.game_state = "main_menu"
            self.world_name = ""
            self.is_multiplayer = False
            self.world_start_time = None
            try:
                self.log_position = os.path.getsize(self.current_log)
            except:
                self.log_position = 0
            self.initialized = True
            return

        if not self.initialized:
            return

        try:
            with open(self.current_log, 'r', errors='ignore') as f:
                f.seek(self.log_position)
                for line in f:
                    self._parse(line)
                self.log_position = f.tell()
        except (IOError, OSError):
            pass

    def _parse(self, line):
        if LOG_PATTERNS["main_menu"].search(line):
            self.game_state = "main_menu"
            self.world_name = ""
            self.is_multiplayer = False
            self.world_start_time = None
            return

        m = LOG_PATTERNS["singleplayer_world"].search(line)
        if m:
            self.game_state = "loading"
            self.world_name = m.group(1)
            self.is_multiplayer = False
            return

        m = LOG_PATTERNS["singleplayer_create"].search(line)
        if m:
            self.game_state = "loading"
            self.world_name = m.group(1)
            self.is_multiplayer = False
            return

        if LOG_PATTERNS["multiplayer_connect"].search(line):
            self.game_state = "loading"
            self.is_multiplayer = True
            return

        m = LOG_PATTERNS["server_connect"].search(line)
        if m and m.group(1) not in ("127.0.0.1", "localhost"):
            self.is_multiplayer = True
            self.server_address = m.group(1)

        if LOG_PATTERNS["in_game"].search(line):
            self.game_state = "in_game"
            self.world_start_time = int(time.time())

    def get_presence(self):
        if self.game_state == "main_menu":
            return "In Main Menu", "Idle"
        if self.game_state == "loading":
            if self.is_multiplayer:
                return "Joining Server", self.server_address or "Connecting..."
            return "Loading World", self.world_name or "..."
        if self.game_state == "in_game":
            if self.is_multiplayer:
                return "Playing Multiplayer", f"Server: {self.server_address}" if self.server_address else "Online"
            return "Playing Singleplayer", f"World: {self.world_name}" if self.world_name else "Exploring Orbis"
        return "Playing Hytale", "Exploring Orbis"
