#!/bin/bash
cd "$(dirname "$0")/.."

echo "Building Hytale RPC for macOS..."

pip3 install pyinstaller pypresence psutil rumps --quiet

rm -rf build dist *.spec

python3 -m PyInstaller --windowed \
    --name "Hytale RPC" \
    --icon "assets/icon.icns" \
    --add-data "src:src" \
    --hidden-import rumps \
    --hidden-import pypresence \
    --hidden-import psutil \
    --exclude-module PIL \
    --exclude-module numpy \
    --exclude-module pandas \
    --exclude-module matplotlib \
    --exclude-module scipy \
    --exclude-module tkinter \
    --exclude-module test \
    --exclude-module unittest \
    --osx-bundle-identifier com.hytale.rpc \
    hytale_rpc_macos.py

mkdir -p releases

if [ -d "dist/Hytale RPC.app" ]; then
    echo "Setting LSUIElement (menu bar only, no dock icon)..."
    /usr/libexec/PlistBuddy -c "Add :LSUIElement bool true" "dist/Hytale RPC.app/Contents/Info.plist"

    echo "Creating DMG..."

    rm -rf /tmp/hytale-dmg
    mkdir -p /tmp/hytale-dmg
    cp -r "dist/Hytale RPC.app" /tmp/hytale-dmg/
    ln -s /Applications /tmp/hytale-dmg/Applications

    hdiutil create -volname "Hytale RPC" \
        -srcfolder /tmp/hytale-dmg \
        -ov -format UDZO \
        "releases/HytaleRPC.dmg"

    rm -rf /tmp/hytale-dmg build *.spec dist

    echo ""
    echo "Build complete!"
    ls -lh releases/HytaleRPC.dmg
else
    echo "Build failed!"
fi