#!/usr/bin/env python3
import subprocess
import logging
import shutil

logging.basicConfig(
    filename='/var/log/mighty_lxqt.log',
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

def debloat_lxqt():
    """Remove unnecessary LXQt packages."""
    logging.info("Starting LXQt debloating...")

    # List of LXQt packages to remove
    lxqt_packages = [
        "lximage-qt",          # Image viewer
        "qterminal",           # Terminal emulator
        "qps",                 # Process viewer
        "screengrab",          # Screenshot tool
        "lxqt-archiver",       # Archive manager
        "lxqt-powermanagement",# Power management tool
        "lxqt-about",          # About LXQt
        "lxqt-session",        # Session manager
        "lxqt-panel",          # Panel
        "lxqt-runner",         # Application launcher
        "pcmanfm-qt",          # File manager
        "lxqt-openssh-askpass" # SSH password prompt
    ]

    for package in lxqt_packages:
        logging.info(f"Removing package: {package}")
        run(["sudo", "apt-get", "remove", "--purge", "-y", package])

        logging.info("LXQt debloating completed.")

if __name__ == "__main__":
    try:
        debloat_lxqt()
    except Exception as e:
        logging.exception(f"Fatal error occurred: {e}")
        print(f"❌ An error occurred: {e}")