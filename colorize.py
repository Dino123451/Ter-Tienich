#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌈 Colorize Text Demo
"""
import os
from colorama import Fore, Back, init
init(autoreset=True)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    txt = input("Nhập chữ: ").strip() or "Xin chào!"
    for color in [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]:
        print(color + txt)
    print(Back.WHITE + Fore.BLACK + txt)
    input(Fore.CYAN + "\nNhấn Enter để thoát...")

if __name__ == "__main__":
    main()
