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

Here's Mighty in action (errors shown are because I already ran it on this system):

![mighty_terminal_screenshot](https://github.com/user-attachments/assets/4d492b99-b5a2-407c-b9ea-30ee1ee46540)


---

## 📥 Installation

Clone the repository and run the script:

```bash
git clone https://github.com/shembazai/mighty.git
cd mighty
chmod +x mighty.py
sudo python3 mighty.py


🧠 How It Works

Removes pre-defined lists of bloat packages

Installs developer tools and productivity apps

Cleans up package caches

Reboots the system at the end

Everything is logged in post_installer.log.

🛡️ License
This project is dual-licensed:

AGPL-3.0 License: Free for open-source use.

Commercial License: Required for proprietary or internal business use.

For commercial licensing, see LICENSE_COMMERCIAL.md or contact:

Website: https://out-of-the-matrix.org
Email: outofthematrix2026@gmail.com

💬 Credits
Created by me, Shemba, a self-taught Linux and AI systems architect with a passion for minimalist efficiency and off-grid independence.

🌱 Support & Contributions
Want to help improve Mighty? Fork the repo and open a pull request.

Feature requests and issues are welcome on the Issues page.

Commercial support available.

✨ Related Projects

Off-grid AI system assistants

Linux setup automators for clean, fast, AI-ready environments

Nature is calling. Will you answer?
