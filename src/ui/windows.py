import threading
import webbrowser


def run_windows_app():
    import pystray
    from PIL import Image
    from ..rpc_windows import HytaleRPC

    GITHUB_URL = "https://github.com/bas3line/hytale-rpc"
    DISCORD_URL = "https://discord.gg/D5S6dh9Ww9"

    icon = None
    status_text = "Starting..."
    last_notification = None

    def send_notification(text):
        if not icon:
            return
        if "Connected" in text:
            icon.notify("Now showing your activity", "Connected to Discord")
        elif "In Main Menu" in text:
            icon.notify("Waiting in lobby", "In Main Menu")
        elif "Playing Singleplayer" in text:
            icon.notify("Playing singleplayer", "Entered World")
        elif "Playing Multiplayer" in text:
            icon.notify("Playing multiplayer", "Joined Server")
        elif "Loading" in text:
            icon.notify("Entering game...", "Loading World")
        elif "Joining" in text:
            icon.notify("Connecting...", "Joining Server")

    def update_status(text):
        nonlocal status_text, last_notification
        status_text = text

        if text != last_notification:
            last_notification = text
            send_notification(text)

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
