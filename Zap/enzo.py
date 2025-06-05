import pywhatkit as py
import pyautogui
import time

py.sendwhatmsg_instantly("+55 19 99804-8226", "vc achou que iria sair impune!")
while True:
    pyautogui.write("você achou que iria sair impune MAGU!")
    pyautogui.press("enter")
    time.sleep(8)
