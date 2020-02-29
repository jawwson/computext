import time
def ctype(text, speed = 0.1):
    text = str(text)
    for x in range(0, len(text)):
        print(text[x], end='')
        time.sleep(speed)
    print()