import time
import pyautogui

def spamscript():
    time.sleep(5)
    # this is a delay so you can switch to your desired target application
    with open('script.txt', encoding="utf-8") as d:
        lines = d.readlines()
    for i in lines:
        pyautogui.typewrite(i.strip())
        pyautogui.press('enter')

spamscript()
