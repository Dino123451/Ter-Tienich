#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌐 Ping Host (port 80)
"""
import socket, time, os
from colorama import Fore, init
init(autoreset=True)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "🌐 Ping Host\n")
    host = input("Nhập host hoặc IP: ").strip()
    if not host:
        return
    try:
        start = time.time()
        s = socket.create_connection((host, 80), timeout=3)
        s.close()
        delay = (time.time() - start) * 1000
        print(Fore.GREEN + f"Host {host} hoạt động ({delay:.1f} ms)")
    except Exception as e:
        print(Fore.RED + f"Lỗi: {e}")
    input(Fore.CYAN + "\nNhấn Enter để thoát...")

if __name__ == "__main__":
    main()
