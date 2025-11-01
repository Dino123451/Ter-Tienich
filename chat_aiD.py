#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
💬 Console Chat AI (GPT) v3
Tác giả: Kai (GPT-5)
Tương thích: Termux, Linux, Windows, macOS
"""

import os
import sys
import json
import time
import requests
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# ====================================================
# ⚙️ CẤU HÌNH CHÍNH - chỉ cần sửa ở đây
# ====================================================
API_KEY = "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"  # 🔑 Dán API key vào đây
MODEL = "gpt-4o-mini"  # hoặc "gpt-4o", "gpt-3.5-turbo"
TEMPERATURE = 0.8
API_URL = "https://api.openai.com/v1/chat/completions"
SYSTEM_PROMPT = "Bạn là KaiBot, trợ lý AI thân thiện, nói chuyện tự nhiên bằng tiếng Việt."

# ====================================================
# 🚫 KIỂM TRA API KEY
# ====================================================
if not API_KEY or not API_KEY.startswith("sk-"):
    print(Fore.RED + "⚠️  Bạn chưa dán API key!")
    print(Fore.YELLOW + "👉  Mở file và thêm vào dòng đầu: API_KEY = 'sk-...'")
    sys.exit(1)

HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# ====================================================
# 🎨 HIỆN TIÊU ĐỀ ĐẸP MẮT
# ====================================================
def banner():
    os.system("clear" if os.name != "nt" else "cls")
    print(Fore.CYAN + "╔════════════════════════════════════════════════╗")
    print(Fore.CYAN + "║        🤖 CONSOLE CHAT AI (GPT) v3.0           ║")
    print(Fore.CYAN + "╚════════════════════════════════════════════════╝")
    print(
        Fore.YELLOW + "\nLệnh có sẵn:\n"
        + Fore.GREEN + " /help " + Fore.WHITE + "- xem hướng dẫn\n"
        + Fore.GREEN + " /clear " + Fore.WHITE + "- xóa hội thoại\n"
        + Fore.GREEN + " /save <tên.json> " + Fore.WHITE + "- lưu hội thoại\n"
        + Fore.GREEN + " /load <tên.json> " + Fore.WHITE + "- tải hội thoại\n"
        + Fore.GREEN + " /model <tên_model> " + Fore.WHITE + "- đổi model (vd: gpt-4o)\n"
        + Fore.GREEN + " /key <API_Key> " + Fore.WHITE + "- đổi API key trực tiếp\n"
        + Fore.GREEN + " /exit " + Fore.WHITE + "- thoát chương trình\n"
    )

# ====================================================
# 🧠 GỌI API OPENAI
# ====================================================
def call_gpt(messages, model=MODEL, temp=TEMPERATURE):
    payload = {"model": model, "messages": messages, "temperature": temp}
    res = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)

    if res.status_code == 429:
        return "⚠️ Quá nhiều yêu cầu. Hãy đợi vài giây rồi thử lại!"
    elif res.status_code >= 400:
        return f"⚠️ Lỗi API: {res.status_code} - {res.text[:100]}"

    data = res.json()
    return data["choices"][0]["message"]["content"]

# ====================================================
# 💬 IN TEXT CHẬM (hiệu ứng chat thật)
# ====================================================
def slow_print(text, delay=0.015):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

# ====================================================
# 🧩 CHƯƠNG TRÌNH CHÍNH
# ====================================================
def main():
    banner()
    model = MODEL
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    history = []

    while True:
        try:
            user_input = input(Fore.BLUE + "🧑 You: " + Style.RESET_ALL).strip()
        except (KeyboardInterrupt, EOFError):
            print(Fore.RED + "\n🚪 Thoát.")
            break

        if not user_input:
            continue

        # ========== LỆNH QUẢN LÝ ==========
        if user_input in ["/exit", "exit", "quit"]:
            print(Fore.RED + "👋 Tạm biệt nhé!")
            break

        if user_input == "/help":
            banner()
            continue

        if user_input == "/clear":
            os.system("clear" if os.name != "nt" else "cls")
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            history.clear()
            banner()
            print(Fore.GREEN + "🧹 Đã xóa hội thoại.")
            continue

        if user_input.startswith("/save "):
            _, fname = user_input.split(maxsplit=1)
            with open(fname, "w", encoding="utf-8") as f:
                json.dump(history, f, ensure_ascii=False, indent=2)
            print(Fore.GREEN + f"💾 Đã lưu hội thoại vào {fname}")
            continue

        if user_input.startswith("/load "):
            _, fname = user_input.split(maxsplit=1)
            try:
                with open(fname, "r", encoding="utf-8") as f:
                    history = json.load(f)
                messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                for item in history:
                    messages.append({"role": "user", "content": item["user"]})
                    messages.append({"role": "assistant", "content": item["assistant"]})
                print(Fore.GREEN + f"📂 Đã tải hội thoại từ {fname}")
            except Exception as e:
                print(Fore.RED + f"⚠️ Không thể tải file: {e}")
            continue

        if user_input.startswith("/model "):
            _, model = user_input.split(maxsplit=1)
            print(Fore.YELLOW + f"🔁 Đổi model sang: {model}")
            continue

        if user_input.startswith("/key "):
            _, new_key = user_input.split(maxsplit=1)
            global API_KEY, HEADERS
            API_KEY = new_key.strip()
            HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
            print(Fore.GREEN + "🔑 Đã đổi API key thành công!")
            continue

        # ========== GỌI GPT ==========
        messages.append({"role": "user", "content": user_input})
        print(Fore.MAGENTA + "🤔 Đang nghĩ...\n")

        try:
            reply = call_gpt(messages, model)
            print(Fore.GREEN + Style.BRIGHT + "🤖 KaiBot: " + Style.RESET_ALL, end="")
            slow_print(reply)
            messages.append({"role": "assistant", "content": reply})
            history.append({"user": user_input, "assistant": reply, "time": datetime.now().isoformat()})
        except Exception as e:
            print(Fore.RED + f"⚠️ Lỗi API: {e}")

# ====================================================
if __name__ == "__main__":
    main()
