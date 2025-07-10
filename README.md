# 🔴 RAT-TOOL - Remote Access Trojan Tool
A powerful Python-based remote access tool for security research, penetration testing, and ethical red-teaming.

Python
License
Platform

## 📌 Description
RAT-TOOL is a Remote Administration Tool designed for security researchers, penetration testers, and ethical hackers to assess system vulnerabilities and demonstrate remote access risks.

This tool allows you to:
✔ Generate a payload (payload.exe) for target systems.
✔ Establish a reverse connection when the victim executes the payload.
✔ Remotely control the victim's machine with multiple functionalities.

# ⚠ Disclaimer: This tool is for educational and authorized security testing purposes only. Unauthorized use against systems without explicit permission is illegal.

## 🔥 Features
[📁] File System:
- file_list [path]        - List directory contents
- file_read [path]       - Download a file
- file_upload [loc] [rem] - Upload file to victim
- file_delete [path]     - Delete file/folder
- zip_folder [path]      - Compress folder
- autodownload           - Grab files from Desktop/Docs/Downloads

[🔒] Encryption:
- encrypt [file]         - Encrypt file (AES-256)
- decrypt [file] [key]   - Decrypt file

[🖥️] System Control:
- sysinfo                - Get detailed system info
- terminate [process]    - Kill a process
- escalate               - Attempt admin privileges
- shutdown               - Shutdown system
- restart                - Restart system
- logoff                 - Logoff current user

[📸] Surveillance:
- webcam                 - Take webcam photo
- screenshot             - Capture screen
- record_mic [seconds]   - Record microphone
- record_screen [seconds]- Record screen activity

[⌨️] Keylogger:
- keylogger start        - Start keylogger
- keylogger stop         - Stop keylogger
- keylogger dump         - Get keylogger data

[🌐] Network:
- wifi_passwords         - Get saved WiFi passwords
- port_scan [ip] [range] - Scan for open ports

[📋] Clipboard:
- clipboard_get          - Get clipboard contents
- clipboard_set [text]   - Set clipboard text

[⚙️] Other:
- melt                   - Self-destruct payload
- help                   - Show this menu
- exit                   - Close connection

## ⚙️ Installation & Usage
1️⃣ Setup (Attacker Machine)

git clone https://github.com/Threadlinee/RAT-TOOL.git
cd RAT-TOOL
2️⃣ Generate Payload
Run the payload generator:
python RAT.py
This creates payload.py and payload.exe (for Windows victims).

3️⃣ Start Listener
python listener.py
Wait for the victim to execute the payload.

4️⃣ Remote Control
Once connected, you can:

Use commands like webcam, screenshot, sysinfo, etc.

Browse files with file_list C:\

Download files with file_read C:\secret.txt

Execute system commands directly.

## ⚠ Legal & Ethical Notice
This tool is only for authorized security testing, educational purposes, and ethical hacking.

## 🚨 Illegal use is strictly prohibited.

You are responsible for complying with laws in your jurisdiction.

Never deploy this tool without explicit permission from the target system owner.

# 📜 License
This project is licensed under MIT License. See LICENSE for details.

## 📞 Contact
Created by Threadlinee — reach out for questions, suggestions, or collabs via GitHub issues or DM.

# ☕ Support
If you find this tool useful, drop a ⭐ or fork it. Contributions and proxy improvements are welcome.

[![Buy Me a Coffee](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/G2G114SBVV)

## Educational Purposes Only!! Stay safe, stay ethical. ✌️


