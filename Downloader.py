#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📥 File Downloader with progress bar
"""
import os
try:
    import requests
    from tqdm import tqdm
    from colorama import Fore, Style, init
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "tqdm", "colorama"])
    import requests
    from tqdm import tqdm
    from colorama import Fore, Style, init

init(autoreset=True)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "📥 File Downloader\n")
    url = input("Nhập URL cần tải: ").strip()
    if not url:
        return
    name = input("Tên file lưu (Enter = tự động): ").strip() or url.split("/")[-1]
    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()
        total = int(r.headers.get("content-length", 0))
        with open(name, "wb") as f, tqdm(total=total, unit="B", unit_scale=True, desc=name) as bar:
            for chunk in r.iter_content(8192):
                f.write(chunk)
                bar.update(len(chunk))
        print(Fore.GREEN + f"Tải xong: {name}")
    except Exception as e:
        print(Fore.RED + f"Lỗi: {e}")
    input(Fore.CYAN + "\nNhấn Enter để thoát...")

if __name__ == "__main__":
    main()
