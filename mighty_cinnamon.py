#!/usr/bin/env python3
import subprocess
import logging
import shutil

logging.basicConfig(
    filename='/var/log/mighty_cinnamon.log',
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

def debloat_cinnamon():
    """Remove unnecessary Cinnamon packages."""
    logging.info("Starting Cinnamon debloating...")

    # List of Cinnamon packages to remove
    cinnamon_packages = [
        "cinnamon-screensaver",    # Screensaver
        "cinnamon-control-center",# Control center
        "cinnamon-session",       # Session manager
        "cinnamon-settings-daemon", # Settings daemon
        "cinnamon-common",        # Common files for Cinnamon
        "cinnamon-desktop-data",  # Desktop data
        "cinnamon-translations",  # Translations
        "nemo",                   # File manager
        "nemo-fileroller",        # Archive manager for Nemo
        "cinnamon-backgrounds",   # Background images
        "cinnamon-themes",        # Themes
        "cinnamon-sounds",        # Sound effects
        "cinnamon-doc",           # Documentation
        "cinnamon-dbg"            # Debugging symbols
    ]

    for package in cinnamon_packages:
        logging.info(f"Removing package: {package}")
        run(["sudo", "apt-get", "remove", "--purge", "-y", package])

    # Clean up unused dependencies
    logging.info("Cleaning up unused dependencies...")
    run(["sudo", "apt-get", "autoremove", "-y"])
    run(["sudo", "apt-get", "clean"])

    logging.info("Cinnamon debloating completed.")

if __name__ == "__main__":
    try:
        debloat_cinnamon()
    except Exception as e:
        logging.exception(f"Fatal error occurred: {e}")
        print(f"❌ An error occurred: {e}")