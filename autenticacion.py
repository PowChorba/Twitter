import pyautogui
import os
import pandas as pd


def auth():
    names = pd.read_csv('twitter_accounts.csv')
    for i in names['Users']:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        pyautogui.sleep(2)
        x,y = pyautogui.locateCenterOnScreen('primer_clic.PNG')
        pyautogui.click(x,y)
        pyautogui.hotkey('win', 'up')
        pyautogui.typewrite('https://twitter.com/')
        pyautogui.typewrite(['enter'])
        pyautogui.sleep(10)
        x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/login.PNG')
        pyautogui.click(x,y)
        pyautogui.sleep(5)
        x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/input_username.PNG')
        pyautogui.click(x,y)
        pyautogui.typewrite(i)
        pyautogui.sleep(1)
        pyautogui.typewrite(['enter'])
        pyautogui.sleep(3)
        pyautogui.typewrite('PerritoMavlado53@')
        pyautogui.sleep(2)
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(['enter'])
        pyautogui.sleep(90)
        x,y = pyautogui.locateCenterOnScreen('cruz.PNG')
        pyautogui.click(x,y)

auth()
        