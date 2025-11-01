#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🖥️ System Info Utility
Hiển thị thông tin CPU, RAM, Disk, OS
"""
import os, time
from datetime import datetime

try:
    import psutil
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    import psutil

try:
    from colorama import Fore, Style, init
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import Fore, Style, init

init(autoreset=True)

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "🖥️ Thông tin hệ thống\n" + Style.RESET_ALL)
    print(Fore.YELLOW + "Thời gian:", Style.BRIGHT + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(Fore.GREEN + "Hệ điều hành:", Style.BRIGHT + os.name.upper())

    cpu = psutil.cpu_percent(0.5)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    print(Fore.MAGENTA + f"CPU: {cpu}%")
    print(Fore.MAGENTA + f"RAM: {get_size(mem.used)} / {get_size(mem.total)} ({mem.percent}%)")
    print(Fore.MAGENTA + f"Disk: {get_size(disk.used)} / {get_size(disk.total)} ({disk.percent}%)")
    input(Fore.CYAN + "\nNhấn Enter để thoát...")

if __name__ == "__main__":
    main()
