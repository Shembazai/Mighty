# Mighty – Linux Post-Installer & Debloater

**Mighty** is a lightweight, smart post-installation script for Linux. It helps users rapidly clean up their systems, remove bloatware, and install essential tools — all while detecting the desktop environment (GNOME, XFCE, LXQt, etc.) automatically.

> "Petit mais puissant." – Designed by Shemba for clean, efficient Linux setups.

---

## Features

- ✅ Auto-detects desktop environment. (Gnome, KDE, LXQt, etc.)
- 🧹 Removes bloatware specific to each DE
- 📦 Installs essential tools (e.g. VLC, LibreOffice, git, Python tools, system monitors)
- 🔁 Performs full system maintenance and cleanup
- 💡 Uses native package manager: `apt`, `dnf`, or `pacman`
- 🔐 Dual-licensed under AGPL-3.0 and optional commercial terms

---

## 📸 Screenshot

*(Optional: Add a screenshot of the terminal running mighty.py here)*

---

## 📥 Installation

Clone the repository and run the script:

```bash
git clone https://github.com/shembazai/mighty.git
cd mighty
chmod +x mighty.py
sudo python3 mighty.py
