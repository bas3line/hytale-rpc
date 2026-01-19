import threading
import subprocess
import webbrowser


def send_notification(title, subtitle, message):
    script = f'display notification "{message}" with title "{title}" subtitle "{subtitle}"'
    subprocess.run(["osascript", "-e", script], capture_output=True)


def run_macos_app():
    import rumps
    from ..rpc_macos import HytaleRPC

    GITHUB_URL = "https://github.com/bas3line/hytale-rpc"
    DISCORD_URL = "https://discord.gg/D5S6dh9Ww9"

    class HytaleMenuBar(rumps.App):
        def __init__(self):
            super().__init__("H", quit_button=None)
            self.status_item = rumps.MenuItem("Status: Starting...")
            self.privacy_item = rumps.MenuItem("Privacy Mode", callback=self.toggle_privacy)

            try:
                import json
                import pathlib
                config_file = pathlib.Path.home() / ".hytale-rpc" / "settings.json"
                if config_file.exists():
                    with open(config_file, "r") as f:
                        data = json.load(f)
                    if data.get("privacy_mode", False):
                        self.privacy_item.state = 1
            except:
                pass

            self.menu = [
                rumps.MenuItem("Hytale RPC"),
                None,
                self.status_item,
                None,
                self.privacy_item,
                None,
                rumps.MenuItem("GitHub: bas3line/hytale-rpc", callback=self.open_github),
                rumps.MenuItem("Discord Server", callback=self.open_discord),
                None,
                rumps.MenuItem("Star on GitHub!", callback=self.open_github),
                None,
                "Quit"
            ]
            self.rpc = HytaleRPC(status_callback=self.update_status)
            self.rpc_thread = None
            self.last_notification = None

        def update_status(self, text):
            try:
                self.status_item.title = f"Status: {text}"

                if text != self.last_notification:
                    self.last_notification = text
                    self._send_notification(text)
            except Exception:
                pass

        def _send_notification(self, text):
            if "Connected" in text:
                send_notification("Hytale RPC", "Connected to Discord", "Now showing your activity")
            elif "In Main Menu" in text:
                send_notification("Hytale RPC", "In Main Menu", "Waiting in lobby")
            elif "Playing Singleplayer" in text:
                send_notification("Hytale RPC", "Entered World", "Playing singleplayer")
            elif "Playing Multiplayer" in text:
                send_notification("Hytale RPC", "Joined Server", "Playing multiplayer")
            elif "Loading" in text:
                send_notification("Hytale RPC", "Loading World", "Entering game...")
            elif "Joining" in text:
                send_notification("Hytale RPC", "Joining Server", "Connecting...")

        def toggle_privacy(self, sender):
            import json
            import pathlib
            config_dir = pathlib.Path.home() / ".hytale-rpc"
            config_dir.mkdir(parents=True, exist_ok=True)
            config_file = config_dir / "settings.json"

            if config_file.exists():
                with open(config_file, "r") as f:
                    data = json.load(f)
            else:
                data = {}

            data["privacy_mode"] = not data.get("privacy_mode", False)

            with open(config_file, "w") as f:
                json.dump(data, f)

            self.privacy_item.state = 1 if data["privacy_mode"] else 0

        def open_github(self, _):
            webbrowser.open(GITHUB_URL)

        def open_discord(self, _):
            webbrowser.open(DISCORD_URL)

        @rumps.clicked("Quit")
        def quit_app(self, _):
            if self.rpc:
                self.rpc.stop()
            rumps.quit_application()

        def start_rpc(self):
            self.rpc_thread = threading.Thread(target=self.rpc.run, daemon=True)
            self.rpc_thread.start()

    app = HytaleMenuBar()
    app.start_rpc()
    app.run()
