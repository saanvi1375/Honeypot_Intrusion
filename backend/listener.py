# listener.py
import socket
import requests

HOST = "0.0.0.0"
PORT = 2222

def log_attempt(ip):
    data = {
        "port": str(PORT),
        "description": "Detected connection attempt",
        "severity": "medium",
        "fake_ip": "8.8.8.8"  # ← Add this line to simulate external IP
    }
    try:
        requests.post("http://localhost:5050/log", json=data)
        print(f"Logged attempt from {ip}")
    except Exception as e:
        print(f"Failed to log: {e}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[+] Listening on port {PORT}...")

    while True:
        conn, addr = s.accept()
        ip, _ = addr
        print(f"[!] Connection detected from {ip}")
        log_attempt(ip)
        conn.close()
