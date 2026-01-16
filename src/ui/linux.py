import threading
import webbrowser
import subprocess


def send_notification(title, message):
    try:
        subprocess.run(
            ["notify-send", title, message, "-i", "discord"],
            capture_output=True
        )
    except Exception:
        pass


def run_linux_app():
    import pystray
    from PIL import Image
    from ..rpc import HytaleRPC

    GITHUB_URL = "https://github.com/bas3line/hytale-rpc"
    DISCORD_URL = "https://discord.gg/D5S6dh9Ww9"

    icon = None
    status_text = "Starting..."
    last_notification = None

    def notify(text):
        if "Connected" in text:
            send_notification("Connected to Discord", "Now showing your activity")
        elif "In Main Menu" in text:
            send_notification("In Main Menu", "Waiting in lobby")
        elif "Playing Singleplayer" in text:
            send_notification("Entered World", "Playing singleplayer")
        elif "Playing Multiplayer" in text:
            send_notification("Joined Server", "Playing multiplayer")
        elif "Loading" in text:
            send_notification("Loading World", "Entering game...")
        elif "Joining" in text:
            send_notification("Joining Server", "Connecting...")

    def update_status(text):
        nonlocal status_text, last_notification
        status_text = text

        if text != last_notification:
            last_notification = text
            notify(text)

    rpc = HytaleRPC(status_callback=update_status)

    def on_quit(ic, item):
        rpc.stop()
        ic.stop()

    def open_github(ic, item):
        webbrowser.open(GITHUB_URL)

    def open_discord(ic, item):
        webbrowser.open(DISCORD_URL)

    def rpc_thread():
        rpc.run()

    img = Image.new('RGB', (64, 64), color=(114, 137, 218))
    menu = pystray.Menu(
        pystray.MenuItem("Hytale RPC", None, enabled=False),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(lambda text: f"Status: {status_text}", None, enabled=False),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("GitHub: bas3line/hytale-rpc", open_github),
        pystray.MenuItem("Discord Server", open_discord),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Star on GitHub!", open_github),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Quit", on_quit)
    )
    icon = pystray.Icon("Hytale RPC", img, "Hytale RPC", menu)

    t = threading.Thread(target=rpc_thread, daemon=True)
    t.start()

    icon.run()
