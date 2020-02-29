import os
def clear():
    os.system('cls' if os.name == 'nt' else print(f"\033c"))
