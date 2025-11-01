#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📝 To-Do List
"""
import json, os
from pathlib import Path
from colorama import Fore, init
init(autoreset=True)
FILE = Path(".todo_data.json")

def load():
    return json.loads(FILE.read_text()) if FILE.exists() else []

def save(data):
    FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    todos = load()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.CYAN + "📝 To-Do List\n")
        for i, t in enumerate(todos, 1):
            status = "[x]" if t.get("done") else "[ ]"
            print(f"{i}. {status} {t.get('task')}")
        print(Fore.YELLOW + "\nA) Thêm  D) Đánh dấu  X) Xóa  Q) Thoát")
        ch = input("Chọn: ").lower()
        if ch == "a":
            task = input("Nội dung: ").strip()
            if task:
                todos.append({"task": task, "done": False})
                save(todos)
        elif ch == "d":
            i = input("Số nhiệm vụ: ")
            if i.isdigit() and 1 <= int(i) <= len(todos):
                todos[int(i)-1]["done"] = not todos[int(i)-1]["done"]
                save(todos)
        elif ch == "x":
            i = input("Số nhiệm vụ: ")
            if i.isdigit() and 1 <= int(i) <= len(todos):
                todos.pop(int(i)-1)
                save(todos)
        elif ch == "q":
            break

if __name__ == "__main__":
    main()
