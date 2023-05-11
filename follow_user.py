import pyautogui
import pandas as pd
import os

def follow_users(url):
    acc_csv = pd.read_csv('twitter_accounts.csv')
    for i in acc_csv['Users']:
            try:
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
                pyautogui.typewrite(url)
                pyautogui.typewrite(['enter'])
                pyautogui.sleep(10)
                x,y = pyautogui.locateCenterOnScreen('./imagenes_follow/follow_button.PNG')
                pyautogui.click(x,y)
                pyautogui.sleep(5)
                x,y = pyautogui.locateCenterOnScreen('cruz.PNG')
                pyautogui.click(x,y)                 
            except:
                print('Except') 
                x,y = pyautogui.locateCenterOnScreen('cruz.PNG')
                pyautogui.click(x,y)   
                continue 
        
        
          
# follow_users('https://twitter.com/RickSanche55600')     
follow_users('https://twitter.com/NicoAlbornoz_ ')           