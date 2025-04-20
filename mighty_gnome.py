#!/usr/bin/env python3
import subprocess
import logging
import shutil

logging.basicConfig(
    filename='/var/log/mighty_gnome.log',
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

def debloat_gnome():
    """Remove unnecessary GNOME packages."""
    logging.info("Starting GNOME debloating...")

    # List of GNOME packages to remove
    gnome_packages = [
        "gnome-games*", "gnome-maps", "gnome-music", "gnome-photos", 
        "gnome-weather", "cheese", "totem", "simple-scan",
        "remmina", "gnome-software", "gnome-contacts",
        "aisleriot", "gnome-sudoku", "quadrapassel", "iagno", 
        "hitori", "lightsoff", "gnome-mahjongg", "gnome-mines"
    ]

    for package in gnome_packages:
        logging.info(f"Removing package: {package}")
        run(["sudo", "apt-get", "remove", "--purge", "-y", package])

        logging.info("GNOME debloating completed.")

if __name__ == "__main__":
    try:
        debloat_gnome()
    except Exception as e:
        logging.exception(f"Fatal error occurred: {e}")
        print(f"❌ An error occurred: {e}")