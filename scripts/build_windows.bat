@echo off
cd /d "%~dp0\.."

echo Building Hytale RPC for Windows...

pip install pyinstaller pypresence psutil pystray pillow --quiet

pyinstaller --onefile --windowed ^
    --name "HytaleRPC" ^
    --add-data "src;src" ^
    --hidden-import pystray ^
    --hidden-import PIL ^
    --hidden-import pypresence ^
    --hidden-import psutil ^
    hytale_rpc_windows.py

rd /s /q build dist *.spec 2>nul

if not exist "releases" mkdir releases
copy "dist\HytaleRPC.exe" "releases\HytaleRPC.exe"

echo.
echo Build complete!
echo Executable: releases\HytaleRPC.exe
echo.
pause
