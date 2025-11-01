import time, os
from colorama import Fore
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + time.strftime("🕒 %H:%M:%S\n📅 %d/%m/%Y"))
    time.sleep(1)
