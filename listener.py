#!/usr/bin/env python3

import socket
import argparse
import os
import subprocess

def listen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    print(f"[+] Listening on {ip}:{port} ...")
    conn, addr = s.accept()
    print(f"[+] Connection from {addr[0]}:{addr[1]}")

    while True:
        cmd = input("$ ")
        if cmd.lower() in ["exit", "quit"]:
            break
        if cmd.strip():
            conn.send(cmd.encode() + b"\n")
            result = conn.recv(4096).decode()
            print(result)
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reverse Shell Listener")
    parser.add_argument("port", type=int, help="Port to listen on")
    parser.add_argument("--ip", default="0.0.0.0", help="IP to bind to (default: 0.0.0.0)")
    args = parser.parse_args()

    listen(args.ip, args.port)
