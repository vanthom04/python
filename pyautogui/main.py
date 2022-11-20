import pyautogui as pg
import pyperclip
import time
import io

time.sleep(5)

txt = io.open("animals.txt", "r", encoding="utf-8")

text = "Nội dung spam "

for i in txt:
    str = text + i
    pyperclip.copy(str)
    pg.hotkey("ctrl", "v")
    pg.press("Enter")
