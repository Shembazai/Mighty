#!/usr/bin/env python3
import subprocess
import logging
import shutil

logging.basicConfig(
    filename='/var/log/mighty_kde.log',
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

def debloat_kde():
    """Remove unnecessary KDE packages."""
    logging.info("Starting KDE debloating...")

    # List of KDE packages to remove
    kde_packages = [
        "konversation",        # IRC client
        "ktorrent",            # Torrent client
        "kmail",               # Email client
        "kontact",             # Personal information manager
        "akregator",           # RSS feed reader
        "korganizer",          # Calendar application
        "kaddressbook",        # Address book
        "dragonplayer",        # Video player
        "juk",                 # Music player
        "kget",                # Download manager
        "krdc",                # Remote desktop client
        "krfb",                # Desktop sharing tool
        "kde-games*",          # KDE games
        "kde-edu*",            # KDE educational tools
        "kcalc",               # Calculator
        "kmouth",              # Text-to-speech tool
        "kcharselect",         # Character selector
        "kwrite"               # Text editor
    ]

    for package in kde_packages:
        logging.info(f"Removing package: {package}")
        run(["sudo", "apt-get", "remove", "--purge", "-y", package])

        logging.info("KDE debloating completed.")

if __name__ == "__main__":
    try:
        debloat_kde()
    except Exception as e:
        logging.exception(f"Fatal error occurred: {e}")
        print(f"❌ An error occurred: {e}")