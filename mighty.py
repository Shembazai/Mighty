#!/usr/bin/env python3
import subprocess
import shutil
import logging
import time
import os

logging.basicConfig(
    filename='/var/log/mighty.log',
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

def install_required_programs():
    """Install all required programs at the beginning."""
    logging.info("Installing required programs...")
    programs_to_install = [
        "vlc",          # Media player
        "btop",         # Resource monitor
        "htop",         # Interactive process viewer
        "tilix",        # Terminal emulator
        "bleachbit",    # Disk cleanup tool
        "gparted",      # Partition editor
        "neofetch",     # System information tool
        "brave-browser" # Web browser
    ]

    for program in programs_to_install:
        logging.info(f"Installing: {program}")
        run(["sudo", "apt-get", "install", "-y", program])

    logging.info("Required programs installation completed.")

def enforce_gnome_app_grid_only():
    """Apply GNOME settings to enforce app grid as the primary launcher."""
    logging.info("Applying GNOME app grid enforcement...")

    run(["gsettings", "set", "org.gnome.shell", "favorite-apps", "[]"])
    run(["gsettings", "set", "org.gnome.shell.extensions.dash-to-dock", "dock-fixed", "false"])
    run(["gsettings", "set", "org.gnome.shell.extensions.dash-to-dock", "autohide", "true"])
    run(["gsettings", "set", "org.gnome.shell.extensions.dash-to-dock", "intellihide", "true"])
    run(["gsettings", "set", "org.gnome.shell.extensions.dash-to-dock", "click-action", "'focus-or-previews'"])
    run(["gsettings", "set", "org.gnome.shell.extensions.dash-to-dock", "show-apps-at-top", "true"])

    logging.info("GNOME app grid enforced. Hot corners remain enabled.")

def debloat_gnome():
    """Delegate GNOME debloating to mighty_gnome.py."""
    logging.info("Delegating GNOME bloatware removal to mighty_gnome.py...")
    try:
        run(["python3", "/media/shemba/mighty/mighty_gnome.py"])
        logging.info("GNOME bloatware removal completed via mighty_gnome.py.")
    except Exception as e:
        logging.error(f"Error while running mighty_gnome.py: {e}")

def debloat_xfce():
    """Delegate XFCE debloating to mighty_xfce.py."""
    logging.info("Delegating XFCE bloatware removal to mighty_xfce.py...")
    try:
        run(["python3", "/media/shemba/mighty/mighty_xfce.py"])
        logging.info("XFCE bloatware removal completed via mighty_xfce.py.")
    except Exception as e:
        logging.error(f"Error while running mighty_xfce.py: {e}")

def debloat_kde():
    """Delegate KDE debloating to mighty_kde.py."""
    logging.info("Delegating KDE bloatware removal to mighty_kde.py...")
    try:
        run(["python3", "/media/shemba/mighty/mighty_kde.py"])
        logging.info("KDE bloatware removal completed via mighty_kde.py.")
    except Exception as e:
        logging.error(f"Error while running mighty_kde.py: {e}")

def debloat_lxqt():
    """Delegate LXQt debloating to mighty_lxqt.py."""
    logging.info("Delegating LXQt bloatware removal to mighty_lxqt.py...")
    try:
        run(["python3", "/media/shemba/mighty/mighty_lxqt.py"])
        logging.info("LXQt bloatware removal completed via mighty_lxqt.py.")
    except Exception as e:
        logging.error(f"Error while running mighty_lxqt.py: {e}")

def debloat_mate():
    """Delegate MATE debloating to mighty_mate.py."""
    logging.info("Delegating MATE bloatware removal to mighty_mate.py...")
    try:
        run(["python3", "/media/shemba/mighty/mighty_mate.py"])
        logging.info("MATE bloatware removal completed via mighty_mate.py.")
    except Exception as e:
        logging.error(f"Error while running mighty_mate.py: {e}")

def debloat_cinnamon():
    """Delegate Cinnamon debloating to mighty_cinnamon.py."""
    logging.info("Delegating Cinnamon bloatware removal to mighty_cinnamon.py...")
    try:
        run(["python3", "/media/shemba/mighty/mighty_cinnamon.py"])
        logging.info("Cinnamon bloatware removal completed via mighty_cinnamon.py.")
    except Exception as e:
        logging.error(f"Error while running mighty_cinnamon.py: {e}")

def debloat_budgie():
    """Delegate Budgie debloating to mighty_budgie.py."""
    logging.info("Delegating Budgie bloatware removal to mighty_budgie.py...")
    try:
        run(["python3", "/media/shemba/mighty/mighty_budgie.py"])
        logging.info("Budgie bloatware removal completed via mighty_budgie.py.")
    except Exception as e:
        logging.error(f"Error while running mighty_budgie.py: {e}")

def reboot_system():
    """Reboot the system automatically after changes."""
    logging.info("Rebooting system in 5 seconds...")
    print("✅ Changes applied. Rebooting in 5 seconds...")
    time.sleep(5)
    run(["sudo", "reboot"])

def detect_desktop_environment():
    """Detect the installed desktop environment and apply appropriate actions."""
    try:
        # Get the current desktop environment from the environment variable
        desktop_env = os.environ.get("XDG_CURRENT_DESKTOP", "").strip().lower()

        if "gnome" in desktop_env:
            logging.info("GNOME desktop detected.")
            debloat_gnome()
        elif "kde" in desktop_env or "plasma" in desktop_env:
            logging.info("KDE/Plasma desktop detected.")
            debloat_kde()
        elif "xfce" in desktop_env:
            logging.info("XFCE desktop detected.")
            debloat_xfce()
        elif "lxqt" in desktop_env:
            logging.info("LXQt desktop detected.")
            debloat_lxqt()  # Call the LXQt debloating function
        elif "mate" in desktop_env:
            logging.info("MATE desktop detected.")
            debloat_mate()  # Call the MATE debloating function
        elif "cinnamon" in desktop_env:
            logging.info("Cinnamon desktop detected.")
            debloat_cinnamon()  # Call the Cinnamon debloating function
        elif "budgie" in desktop_env:
            logging.info("Budgie desktop detected.")
            debloat_budgie()  # Call the Budgie debloating function
        else:
            logging.warning(f"Unknown desktop environment detected: {desktop_env}")
    except Exception as e:
        logging.error(f"Error detecting desktop environment: {e}")

def clean_up_system():
    """Clean up unused dependencies and package cache."""
    logging.info("Cleaning up unused dependencies and package cache...")
    try:
        run(["sudo", "apt-get", "autoremove", "-y"])
        run(["sudo", "apt-get", "clean"])
        logging.info("System cleanup completed.")
    except Exception as e:
        logging.error(f"Error during system cleanup: {e}")

def main():
    print("🔧 Applying system configuration...")

    install_required_programs()  # Install required programs at the beginning
    enforce_gnome_app_grid_only()
    debloat_gnome()
    clean_up_system()
    reboot_system()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.exception(f"Fatal error occurred: {e}")
        print(f"❌ An error occurred: {e}")
