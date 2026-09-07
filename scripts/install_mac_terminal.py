#!/usr/bin/env python3
"""Install DMA Theme profiles into macOS Terminal.app.

Prints instructions for importing .terminal files via Terminal.app GUI.
Modifying Terminal.plist directly causes corruption warnings on modern macOS.
"""
import os
import subprocess
import sys


def main():
    if sys.platform != "darwin":
        print("Error: This script only runs on macOS.", file=sys.stderr)
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    themes_dir = os.path.join(script_dir, "..", "themes", "mac-terminal")

    light_path = os.path.join(themes_dir, "dma-theme-light.terminal")
    dark_path = os.path.join(themes_dir, "dma-theme-dark.terminal")

    if not os.path.exists(light_path):
        print(f"Error: {light_path} not found", file=sys.stderr)
        sys.exit(1)

    print("DMA Theme — macOS Terminal Install")
    print("=" * 40)
    print()
    print("1. Open Terminal.app")
    print("2. Go to Terminal -> Settings -> Profiles")
    print("3. Click the Gear icon (bottom-left) -> Import...")
    print(f"4. Select: {os.path.abspath(light_path)}")
    print("   (or the dark variant: " + os.path.abspath(dark_path) + ")")
    print("5. Select 'DMA Theme Light' in the list")
    print('6. Click "Default" to make it your default profile')
    print()
    print("The profile includes CommitMonoDrDMac-Regular at 12pt")
    print("and the full DMA color palette.")
    print()

    # Also open the Profiles pane for convenience
    try:
        subprocess.run(
            ["open", "x-apple.systempreferences:com.apple.Terminal-Settings.Profiles"],
            timeout=5,
            capture_output=True,
        )
        print("Opened Terminal Settings for you.")
    except Exception:
        print("(Could not open Settings automatically — open it manually)")


if __name__ == "__main__":
    main()
