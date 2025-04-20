#!/usr/bin/env python3
import subprocess
import logging
import shutil

logging.basicConfig(
    filename='/var/log/mighty_mate.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run(command):
    """Run a command safely and log its output."""
    if not shutil.which(command[0]):
        logging.warning(f"Command not found: {command[0]}")
        return

    try:
        subprocess.run(command, check=True)
        logging.info(f"Executed: {' '.join(command)}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to run: {' '.join(command)}: {e}")

def debloat_mate():
    """Remove unnecessary MATE packages."""
    logging.info("Starting MATE debloating...")

    # List of MATE packages to remove
    mate_packages = [
        "pluma",               # Text editor
        "engrampa",            # Archive manager
        "mate-terminal",       # Terminal emulator
        "mate-system-monitor", # System monitor
        "mate-power-manager",  # Power manager
        "mate-utils",          # Utilities
        "mate-calc",           # Calculator
        "atril",               # Document viewer
        "eom",                 # Eye of MATE image viewer
        "mozo",                # Menu editor
        "mate-applets",        # Applets for the panel
        "mate-media",          # Media player
        "mate-netbook",        # Netbook interface
        "mate-notification-daemon", # Notification daemon
        "mate-polkit",         # PolicyKit authentication agent
        "mate-session-manager" # Session manager
    ]

    for package in mate_packages:
        logging.info(f"Removing package: {package}")
        run(["sudo", "apt-get", "remove", "--purge", "-y", package])

    # Clean up unused dependencies
    logging.info("Cleaning up unused dependencies...")
    run(["sudo", "apt-get", "autoremove", "-y"])
    run(["sudo", "apt-get", "clean"])

    logging.info("MATE debloating completed.")

if __name__ == "__main__":
    try:
        debloat_mate()
    except Exception as e:
        logging.exception(f"Fatal error occurred: {e}")
        print(f"❌ An error occurred: {e}")