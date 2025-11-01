#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
💬 Chat AI — sử dụng OpenAI API (ChatGPT)
⚙️ Tự động dùng API key có sẵn, không cần nhập.
"""

import requests, json, os, sys
from colorama import Fore, Style, init

init(autoreset=True)

# ===================================================
# 🔑 API Key của bạn (điền vào đây)
API_KEY = "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"  # 🧠 GẮN API TẠI ĐÂY
# ===================================================

API_URL = "https://api.openai.com/v1/chat/completions"  # endpoint mặc định
MODEL = "gpt-3.5-turbo"  # có thể đổi thành "gpt-4-turbo"

if not API_KEY or not API_KEY.startswith("sk-"):
    print(Fore.RED + "❌ API key chưa được cấu hình trong code!")
    sys.exit()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

messages = [
    {"role": "system", "content": "Bạn là trợ lý AI thân thiện, nói chuyện ngắn gọn và tự nhiên bằng tiếng Việt."}
]

print(Fore.MAGENTA + Style.BRIGHT + r"""
╔════════════════════════════════════════════╗
║          💬 CHAT AI — GPT CONSOLE          ║
╚════════════════════════════════════════════╝
""" + Fore.CYAN + "Gõ 'exit' để thoát.\n")

while True:
    user_input = input(Fore.YELLOW + "👤 Bạn: ").strip()
    if user_input.lower() in ["exit", "quit"]: break
    messages.append({"role": "user", "content": user_input})

    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.8
    }

    try:
        res = requests.post(API_URL, headers=headers, json=data, timeout=60)
        if res.status_code == 200:
            reply = res.json()["choices"][0]["message"]["content"].strip()
            print(Fore.GREEN + f"🤖 AI: {reply}\n")
            messages.append({"role": "assistant", "content": reply})
        else:
            print(Fore.RED + f"⚠️ API lỗi {res.status_code}: {res.text}")
    except Exception as e:
        print(Fore.RED + f"❌ Lỗi kết nối: {e}")
