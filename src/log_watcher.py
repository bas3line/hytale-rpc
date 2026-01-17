import re
import time
import os
from .config import HYTALE_LOG_DIR

LOG_PATTERNS = {
    "main_menu": re.compile(r'Changing Stage to MainMenu|Changing from Stage (?:Loading|GameLoading) to MainMenu', re.IGNORECASE),
    "singleplayer_world": re.compile(r'Connecting to singleplayer world "([^"]+)"', re.IGNORECASE),
    "singleplayer_create": re.compile(r'Creating new singleplayer world in|Creating world', re.IGNORECASE),
    "multiplayer_connect": re.compile(r'Connecting to (?:multiplayer|dedicated) server|Server connection established', re.IGNORECASE),
    "server_connect": re.compile(r'Opening Quic Connection to ([\d\w\.-]+):(\d+)', re.IGNORECASE),
    "in_game": re.compile(r'Changing from Stage (?:GameLoading|Loading) to InGame|GameInstance\.StartJoiningWorld\s*\(\s*\)|GameInstance\.OnWorldJoined\s*\(\s*\)', re.IGNORECASE),
    "world_loaded": re.compile(r'World loaded|World finished loading|World ready|Loading world:', re.IGNORECASE),
    "server_name": re.compile(r'Server name:?\s*"([^"]+)"|Joined server:?\s*"([^"]+)"', re.IGNORECASE),
    "playing_singleplayer": re.compile(r'Singleplayer world "([^"]+)"|Playing in singleplayer|Singleplayer mode', re.IGNORECASE),
    "playing_multiplayer": re.compile(r'Playing in multiplayer|Multiplayer mode|Multi player|dedicated server', re.IGNORECASE),
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
            self.server_address = ""
            self.is_multiplayer = False
            self.world_start_time = None

            try:
                file_size = os.path.getsize(self.current_log)
                read_from = max(0, file_size - 200000)

                with open(self.current_log, 'r', errors='ignore') as f:
                    f.seek(read_from)
                    lines_to_skip = True
                    for line in f:
                        lines_to_skip = False
                        self._parse(line)
                    self.log_position = f.tell()

                self.initialized = True
            except:
                self.log_position = 0
            return

        if not self.initialized:
            return

        if not self.current_log:
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
            self.server_address = ""
            self.is_multiplayer = False
            self.world_start_time = None
            return

        m = LOG_PATTERNS["singleplayer_world"].search(line)
        if m:
            self.game_state = "loading"
            world_name = m.group(1) if m.groups() and m.group(1) else m.group(2) if len(m.groups()) >= 2 and m.group(2) else ""
            if world_name:
                self.world_name = world_name
            self.is_multiplayer = False
            return

        m = LOG_PATTERNS["singleplayer_create"].search(line)
        if m:
            self.game_state = "loading"
            self.world_name = ""
            self.is_multiplayer = False
            return

        if LOG_PATTERNS["multiplayer_connect"].search(line):
            self.game_state = "loading"
            self.is_multiplayer = True
            return

        m = LOG_PATTERNS["server_connect"].search(line)
        if m:
            addr = m.group(1) if m.groups() and m.group(1) else m.group(3) if len(m.groups()) >= 3 and m.group(3) else ""
            if addr and addr not in ("127.0.0.1", "localhost"):
                self.is_multiplayer = True
                self.server_address = addr

        m = LOG_PATTERNS["server_name"].search(line)
        if m:
            server_name = m.group(1) if m.groups() and m.group(1) else m.group(2) if len(m.groups()) >= 2 and m.group(2) else ""
            if server_name:
                self.server_address = server_name

        if LOG_PATTERNS["in_game"].search(line) or LOG_PATTERNS["world_loaded"].search(line):
            self.game_state = "in_game"
            if not self.world_start_time:
                self.world_start_time = int(time.time())

        if LOG_PATTERNS["playing_singleplayer"].search(line):
            self.game_state = "in_game"
            self.is_multiplayer = False
            if not self.world_start_time:
                self.world_start_time = int(time.time())

        if LOG_PATTERNS["playing_multiplayer"].search(line):
            self.game_state = "in_game"
            self.is_multiplayer = True
            if not self.world_start_time:
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
