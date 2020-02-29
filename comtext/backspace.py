import time, os, keyboard
def backspace(text, speed = 0.1):
    text = str(text)
    g = len(text)
    for x in range(0, len(text)):
        print(text[0:g], end='')
        time.sleep(speed)
        os.system('cls' if os.name == 'nt' else print(f"\033c"))
        g -= 1
