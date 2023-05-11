import pyautogui
import pyperclip
import requests
import os
from csv import writer
# pyautogui.mouseInfo()
# pyautogui.sleep(5)
# pyautogui.moveTo(723,251)
# pyautogui.mouseDown(button='left')
# pyautogui.moveTo(834,251)
# pyautogui.mouseUp(button='left')
# pyautogui.hotkey('ctrl', 'c')
# vari = pyperclip.paste()
# print(vari)


# counter = 1
# array_names = []
# while counter < 40:
#     api = requests.get(f'https://rickandmortyapi.com/api/character/?page={counter}').json()
#     for item in api['results']:
#         array_names.append(item['name'])
#     counter += 1    
# for i in array_names:
#     with open('names.csv', 'a' , encoding='UTF-8', newline='') as file:
#         write = writer(file)
#         write.writerow([i])

# if os.path.exists('C:\\Users\\PowCh\\Desktop\\AC 11940_2023.pdf'):
#     os.remove('C:\\Users\\PowCh\\Desktop\\AC 11940_2023.pdf')

# import os

# def url_pdf(url):
#     url_pdf = url
#     print(url_pdf)
#     if os.path.exists(url_pdf):
# 	    os.remove(url_pdf)


# url_pdf('C:\\Users\\PowCh\\Desktop\\AC 12066_2023.pdf')	

os.system('python -m http.server 5000')