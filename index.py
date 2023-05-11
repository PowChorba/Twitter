import time
import os
import pyautogui
import pyperclip
import pandas as pd
from csv import writer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def account_creator():
    counter = 1
    names_csv = pd.read_csv('names.csv')
    # username = 'MartenBoc'
    while counter < 10000:
        for i in names_csv['Nombres']:
            username = i
            try:
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                pyautogui.sleep(2)
                x,y = pyautogui.locateCenterOnScreen('primer_clic.PNG')
                pyautogui.click(x,y)
                pyautogui.hotkey('win', 'up')
                pyautogui.typewrite('https://twitter.com/i/flow/login')
                pyautogui.typewrite(['enter'])
                pyautogui.sleep(5)
                pyautogui.typewrite(['F5'])
                pyautogui.sleep(5)
                x,y = pyautogui.locateCenterOnScreen('register.PNG')
                pyautogui.click(x,y)
                pyautogui.sleep(2)
                x,y = pyautogui.locateCenterOnScreen('create_acc.PNG')
                pyautogui.click(x,y)
                pyautogui.sleep(10)
                pyautogui.typewrite(username)
                pyautogui.typewrite(['tab'])
                # Combino con Selenium
                driver = webdriver.Chrome()
                driver.get('https://tempail.com/es/')
                pyautogui.sleep(20)
                input_value = driver.find_element(By.XPATH, '//*[@id="eposta_adres"]').get_attribute('value')
                # Vuelvo a PyAutoGui
                time.sleep(2)
                windows = pyautogui.getWindowsWithTitle("Regístrate en Twitter / Twitter - Google Chrome")
                if len(windows) > 0:
                    window = windows[0]
                    window.activate()
                    time.sleep(3)
                pyautogui.typewrite(input_value)  
                pyautogui.sleep(1)
                # Para elegir la fecha de nacimiento
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite('F')
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite('15')  
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite('1999')
                pyautogui.typewrite(['tab'])
                pyautogui.sleep(3)
                pyautogui.typewrite(['enter'])
                pyautogui.sleep(2)
                x,y = pyautogui.locateCenterOnScreen('next.PNG')
                pyautogui.click(x,y)
                pyautogui.sleep(3)
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['enter'])
                pyautogui.sleep(90)
                windows = pyautogui.getWindowsWithTitle("(1) Correo Temporal - Gratis Temp Mail - Google Chrome")
                if len(windows) > 0:
                    window = windows[0]
                    window.activate()
                    time.sleep(3)
                x,y = pyautogui.locateCenterOnScreen('correo_verificacion.PNG')
                pyautogui.click(x,y)
                pyautogui.typewrite(['F5'])
                pyautogui.sleep(10)    
                x,y = pyautogui.locateCenterOnScreen('correo_verificacion.PNG')
                pyautogui.click(x,y)
                pyautogui.sleep(5)
                # iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/iframe[1]')))
                # driver.switch_to.frame(iframe)    
                codigo_verificacion = driver.find_element(By.XPATH, '//*[@id="eposta_oku"]/div[2]/strong').text
                codigo_verificacion = codigo_verificacion[:6]
                print(codigo_verificacion)
                pyautogui.sleep(2)
                windows = pyautogui.getWindowsWithTitle("Regístrate en Twitter / Twitter - Google Chrome")
                if len(windows) > 0:
                    window = windows[0]
                    window.activate()
                    time.sleep(3)
                pyautogui.typewrite(codigo_verificacion)
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['tab'])
                pyautogui.sleep(2)
                pyautogui.typewrite(['enter'])
                pyautogui.sleep(2)
                pyautogui.typewrite('PerritoMavlado53@')
                pyautogui.typewrite(['tab'])
                pyautogui.typewrite(['tab'])
                pyautogui.sleep(2)
                pyautogui.typewrite(['enter'])
                print('imagen')
                pyautogui.sleep(40)
                pyautogui.typewrite(['tab'])
                # pyautogui.typewrite(['tab'])
                pyautogui.sleep(2)
                pyautogui.typewrite(['enter'])
                pyautogui.sleep(2)
                x,y = pyautogui.locateCenterOnScreen('start.PNG')
                pyautogui.click(x,y)
                pyautogui.sleep(10)
                # username_created = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/span').text 
                # pyautogui.moveTo(723,251)
                pyautogui.moveTo(675,249)
                pyautogui.mouseDown(button='left')
                # pyautogui.moveTo(845,251)
                pyautogui.moveTo(820,246)
                pyautogui.mouseUp(button='left')
                pyautogui.hotkey('ctrl', 'c')
                pyautogui.sleep(2)
                username_created = pyperclip.paste()
                pyautogui.sleep(2)
                x,y = pyautogui.locateCenterOnScreen('continue.PNG')
                pyautogui.click(x,y)
                pyautogui.sleep(10)
                x,y = pyautogui.locateCenterOnScreen('cruz.PNG')
                pyautogui.click(x,y)
                driver.close()
                print(username_created)
                # pyautogui.typewrite(['tab'])
                # pyautogui.typewrite(['tab'])    
                # pyautogui.typewrite(['tab'])
                # pyautogui.typewrite(['tab'])  
                # pyautogui.sleep(2)
                # pyautogui.typewrite(['enter']) 
                # pyautogui.sleep(2)
                # pyautogui.typewrite(['tab'])  
                # pyautogui.sleep(2)
                # pyautogui.typewrite(['enter'])  
                # pyautogui.sleep(2)
                # pyautogui.typewrite(['tab'])
                # pyautogui.typewrite(['tab'])    
                # pyautogui.typewrite(['tab'])
                # pyautogui.typewrite(['tab'])  
                # pyautogui.sleep(2)
                # pyautogui.typewrite(['enter'])
                # pyautogui.sleep(2)
                # x,y = pyautogui.locateCenterOnScreen('musica.PNG')
                # pyautogui.click(x,y)
                # pyautogui.sleep(2)
                # x,y = pyautogui.locateCenterOnScreen('entre.PNG')
                # pyautogui.click(x,y)
                # pyautogui.sleep(2)
                # x,y = pyautogui.locateCenterOnScreen('deportes.PNG')
                # pyautogui.click(x,y)
                # pyautogui.sleep(2)
                # x,y = pyautogui.locateCenterOnScreen('siguiente.PNG')
                # pyautogui.click(x,y)
                # pyautogui.sleep(2)
                # x,y = pyautogui.locateCenterOnScreen('otro_siguiente.PNG')
                # pyautogui.click(x,y)
                # pyautogui.sleep(2)
                with open('twitter_accounts.csv', 'a' , encoding='UTF-8', newline='') as file:
                    write = writer(file)
                    write.writerow([username_created])
                counter += 1
            except:
                x,y = pyautogui.locateCenterOnScreen('cruz.PNG')
                pyautogui.click(x,y)
                counter += 1
                driver.close()
                continue
    
    
account_creator()   