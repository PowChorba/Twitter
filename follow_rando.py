import pandas as pd
import random
import pyautogui
import os

csv_accs = pd.read_csv('twitter_accounts.csv')
#Cantidad de lineas adentro del csv
csv_range = csv_accs.index[-1]

# Genero un numero random para definir la primer cuenta
csv_range += 1
random_number = random.randint(1, csv_range)
random_number_followers = random.randint(1,csv_range)
nombre_acc_url = csv_accs.loc[random_number]['Users']
nombre_acc_url = nombre_acc_url.replace('@', '')

# Aca la url
url = f'https://twitter.com/{nombre_acc_url}'
print(random_number, '\n', random_number_followers, '\n', nombre_acc_url)
# Hago un loop para que agarre cuentas al azar
for i in range(random_number_followers):
    acc_random = random.randint(1,csv_range)
    follower_user = csv_accs.loc[acc_random]['Users']
    if follower_user == nombre_acc_url:
        print('Es la misma')
        continue
    else:
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
        pyautogui.typewrite(follower_user)
        pyautogui.sleep(1)
        pyautogui.typewrite(['enter'])
        pyautogui.sleep(3)
        pyautogui.typewrite('PerritoMavlado53@')
        pyautogui.sleep(2)
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(['enter'])
        pyautogui.sleep(10)
        # x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/start.PNG')
        # print(x, 'Despues se los 10 segundos')
        if pyautogui.locateCenterOnScreen('./imagenes_follow/start.PNG'):
            x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/start.PNG')
            pyautogui.click(x,y)
            pyautogui.sleep(50)
            x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/continue.PNG')
            pyautogui.click(x,y)
            pyautogui.sleep(10)
            x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/url_new.PNG')
            pyautogui.click(x,y)
            pyautogui.sleep(5)
            pyautogui.typewrite(url)
            pyautogui.typewrite(['enter'])
            pyautogui.sleep(5)
        elif pyautogui.locateCenterOnScreen('./imagenes_follow/continue.PNG'):
            x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/continue.PNG')
            pyautogui.click(x,y)
            pyautogui.sleep(10)
            x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/url_new.PNG')
            pyautogui.click(x,y)
            pyautogui.sleep(5)
            pyautogui.typewrite(url)
            pyautogui.typewrite(['enter'])
            pyautogui.sleep(5) 
        else:   
            x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/url.PNG')
            pyautogui.click(x,y)
        pyautogui.sleep(2)
        pyautogui.typewrite(['F5'])
        pyautogui.sleep(2)
        x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/url.PNG')
        pyautogui.click(x,y)
        pyautogui.sleep(2)
        pyautogui.typewrite(url)
        pyautogui.typewrite(['enter'])
        pyautogui.sleep(10)
        if pyautogui.locateCenterOnScreen('./imagenes_follow/view_profile.PNG'):
            x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/view_profile.PNG')
            pyautogui.click(x,y) 
        pyautogui.sleep(5)   
        x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/follow_button.PNG')
        pyautogui.click(x,y)
        pyautogui.sleep(5)
        x,y = pyautogui.locateCenterOnScreen('cruz.PNG')
        pyautogui.click(x,y)                 
            # except:
            #     print('Except') 
            #     x,y = pyautogui.locateCenterOnScreen('cruz.PNG')
            #     pyautogui.click(x,y)   
            #     continue



