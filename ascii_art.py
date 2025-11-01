#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎨 ASCII Art Generator
"""
import os
try:
    import pyfiglet
    from colorama import Fore, init
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet", "colorama"])
    import pyfiglet
    from colorama import Fore, init

init(autoreset=True)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "🎨 ASCII Art\n")
    txt = input("Nhập chữ: ").strip() or "Hello"
    font = input("Font (Enter = standard): ").strip() or "standard"
    print(Fore.GREEN + pyfiglet.figlet_format(txt, font=font))
    input(Fore.CYAN + "\nNhấn Enter để thoát...")

if __name__ == "__main__":
    main()
