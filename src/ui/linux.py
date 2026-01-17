import sys
import os
import subprocess
import signal
import time


def send_notification(title, message):
    try:
        subprocess.run(
            ["notify-send", title, message, "-i", "discord"],
            capture_output=True
        )
    except Exception:
        pass


def launch_in_terminal():
    if hasattr(sys, 'frozen'):
        exe_path = sys.executable
    else:
        exe_path = os.path.abspath(sys.argv[0])

    cli_arg = [exe_path, "--cli"]

    terminals = [
        ("gnome-terminal", ["--"]),
        ("kitty", []),
        ("xfce4-terminal", ["-e"]),
        ("konsole", ["-e"]),
        ("xterm", ["-e"]),
        ("alacritty", ["-e"]),
    ]

    for term_name, term_flags in terminals:
        try:
            if subprocess.call(["command", "-v", term_name], shell=True) != 0:
                continue

            cmd = [term_name] + term_flags + cli_arg
            subprocess.Popen(cmd, start_new_session=True)
            time.sleep(0.5)
            return True
        except:
            continue
    return False


def run_linux_app():
    from .cli import run_cli

    if "--cli" in sys.argv:
        run_cli()
        return

    is_atty = sys.stdin.isatty() if sys.stdin else False
    if is_atty:
        run_cli()
        return

    signal.signal(signal.SIGINT, signal.SIG_IGN)

    if launch_in_terminal():
        time.sleep(1)
        sys.exit(0)

    run_cli()
