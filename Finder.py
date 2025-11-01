#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 File Finder
"""
import os
from colorama import Fore, init
init(autoreset=True)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "🔍 File Finder\n")
    start = input("Thư mục bắt đầu (Enter = hiện tại): ").strip() or "."
    patt = input("Từ khóa tìm file: ").strip()
    if not patt:
        return
    matches = []
    for root, dirs, files in os.walk(start):
        for f in files:
            if patt.lower() in f.lower():
                matches.append(os.path.join(root, f))
    if not matches:
        print(Fore.YELLOW + "Không tìm thấy file nào.")
    else:
        for m in matches[:200]:
            print(Fore.GREEN + "• " + m)
    input(Fore.CYAN + "\nNhấn Enter để thoát...")

if __name__ == "__main__":
    main()
