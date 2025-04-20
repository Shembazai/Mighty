#!/usr/bin/env python3
import subprocess
import logging
import shutil

logging.basicConfig(
    filename='/var/log/mighty_xfce.log',
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

def debloat_xfce():
    """Remove unnecessary XFCE packages."""
    logging.info("Starting XFCE debloating...")

    # List of XFCE packages to remove
    packages_to_remove = [
        "xfce4-notes-plugin",  # Notes application
        "parole",              # Media player
        "xfburn",              # Disc burning tool
        "mousepad",            # Text editor
        "xfce4-terminal",      # Terminal emulator
        "orage",               # Calendar application
        "xfce4-weather-plugin",# Weather plugin
        "xfce4-taskmanager",   # Task manager
        "xfce4-appfinder",     # Application finder
        "xfce4-panel-profiles" # Panel configuration tool
    ]

    for package in packages_to_remove:
        logging.info(f"Removing package: {package}")
        run(["sudo", "apt-get", "remove", "--purge", "-y", package])

        logging.info("XFCE debloating completed.")

if __name__ == "__main__":
    try:
        debloat_xfce()
    except Exception as e:
        logging.exception(f"Fatal error occurred: {e}")
        print(f"❌ An error occurred: {e}")