#!/usr/bin/env python3
import subprocess
import logging
import shutil

logging.basicConfig(
    filename='/var/log/mighty_budgie.log',
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

def debloat_budgie():
    """Remove unnecessary Budgie packages."""
    logging.info("Starting Budgie debloating...")

    # List of Budgie packages to remove
    budgie_packages = [
        "budgie-welcome",       # Welcome screen
        "budgie-desktop-environment", # Budgie desktop environment meta-package
        "gnome-screenshot",     # Screenshot tool
        "gnome-system-monitor", # System monitor
        "gnome-terminal",       # Terminal emulator
        "gnome-calculator",     # Calculator
        "gnome-characters",     # Character map
        "gnome-logs",           # Logs viewer
        "gnome-disk-utility",   # Disk utility
        "yelp",                 # Help browser
        "thunderbird",          # Email client
        "rhythmbox",            # Music player
        "totem",                # Video player
        "simple-scan"           # Document scanner
    ]

    for package in budgie_packages:
        logging.info(f"Removing package: {package}")
        run(["sudo", "apt-get", "remove", "--purge", "-y", package])

    # Clean up unused dependencies
    logging.info("Cleaning up unused dependencies...")
    run(["sudo", "apt-get", "autoremove", "-y"])
    run(["sudo", "apt-get", "clean"])

    logging.info("Budgie debloating completed.")

if __name__ == "__main__":
    try:
        debloat_budgie()
    except Exception as e:
        logging.exception(f"Fatal error occurred: {e}")
        print(f"❌ An error occurred: {e}")