from colorama import Fore
while True:
    expr = input(Fore.YELLOW + "🧮 Nhập phép tính (hoặc exit): ")
    if expr.lower() == "exit": break
    try:
        print(Fore.GREEN + f"= {eval(expr)}")
    except Exception:
        print(Fore.RED + "❌ Lỗi cú pháp")
