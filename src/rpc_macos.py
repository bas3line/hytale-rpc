import time
import platform
from pypresence import Presence
if platform.system() == "Darwin":
    from .config_macos import CLIENT_ID, HYTALE_PROCESS_NAMES, DISCORD_PROCESS_NAMES
    from .log_watcher_macos import LogWatcher
else:
    from .config import CLIENT_ID, HYTALE_PROCESS_NAMES, DISCORD_PROCESS_NAMES
    from .log_watcher import LogWatcher
from .process import is_process_running, get_process_start_time


class HytaleRPC:
    def __init__(self, status_callback=None):
        self.rpc = None
        self.connected = False
        self.running = False
        self.log_watcher = LogWatcher()
        self.start_time = None
        self.last_state = ("", "")
        self.status_callback = status_callback

    def set_status(self, text):
        if self.status_callback:
            self.status_callback(text)

    def connect(self):
        if self.connected:
            return True
        try:
            self.rpc = Presence(CLIENT_ID)
            self.rpc.connect()
            self.connected = True
            return True
        except Exception:
            self.rpc = None
            return False

    def disconnect(self):
        if self.rpc and self.connected:
            try:
                self.rpc.clear()
                self.rpc.close()
            except Exception:
                pass
        self.connected = False
        self.rpc = None

    def update(self):
        if not self.connected:
            return
        try:
            self.log_watcher.update()
            details, state = self.log_watcher.get_presence()

            if (details, state) != self.last_state:
                self.last_state = (details, state)
                self.set_status(f"{details}")

            kwargs = {
                "details": details,
                "state": state,
                "large_image": "hytale_logo",
                "large_text": "Hytale",
                "buttons": [{"label": "Hytale Website", "url": "https://hytale.com"}]
            }

            if self.log_watcher.world_start_time:
                kwargs["start"] = self.log_watcher.world_start_time
            elif self.start_time:
                kwargs["start"] = self.start_time

            self.rpc.update(**kwargs)
        except Exception:
            self.connected = False

    def run(self):
        self.running = True
        rpc_active = False
        self.set_status("Waiting for Hytale...")

        while self.running:
            discord_on = is_process_running(DISCORD_PROCESS_NAMES)
            hytale_on = is_process_running(HYTALE_PROCESS_NAMES)

            if hytale_on and discord_on and not rpc_active:
                self.start_time = get_process_start_time(HYTALE_PROCESS_NAMES) or int(time.time())
                self.log_watcher.reset()
                if self.connect():
                    rpc_active = True
                    self.set_status("Connected!")

            elif not hytale_on and rpc_active:
                self.disconnect()
                rpc_active = False
                self.log_watcher.reset()
                self.set_status("Waiting for Hytale...")

            elif not discord_on and rpc_active:
                self.connected = False
                self.rpc = None
                rpc_active = False
                self.set_status("Discord not running")

            elif rpc_active:
                self.update()

            time.sleep(3)

        if rpc_active:
            self.disconnect()

    def stop(self):
        self.running = False