#!/bin/bash
cd "$(dirname "$0")/.."

echo "Building Hytale RPC for Linux..."

pip3 install pyinstaller pypresence psutil pystray pillow --quiet

rm -rf build dist *.spec

python3 -m PyInstaller --onefile \
    --name "HytaleRPC" \
    --add-data "src:src" \
    --hidden-import pystray \
    --hidden-import PIL \
    --hidden-import pypresence \
    --hidden-import psutil \
    --hidden-import pystray._xorg \
    --exclude-module tkinter \
    --exclude-module test \
    --exclude-module unittest \
    hytale_rpc.py

mkdir -p releases

if [ -f "dist/HytaleRPC" ]; then
    cp "dist/HytaleRPC" "releases/HytaleRPC"
    chmod +x "releases/HytaleRPC"

    rm -rf build *.spec dist

    echo ""
    echo "Build complete!"
    ls -lh releases/HytaleRPC
else
    echo "Build failed!"
fi
