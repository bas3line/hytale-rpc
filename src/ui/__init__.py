import platform

def run_app():
    system = platform.system()
    if system == "Darwin":
        from .macos import run_macos_app
        run_macos_app()
    elif system == "Windows":
        from .windows import run_windows_app
        run_windows_app()
    elif system == "Linux":
        from .linux import run_linux_app
        run_linux_app()
    else:
        from .cli import run_cli
        run_cli()
