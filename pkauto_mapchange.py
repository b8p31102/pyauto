import pyautogui as pgui
import time

def mapchange():
    pgui.FAILSAFE = True
    for i in range(400):
            
            pgui.click(x=1287, y=1047, duration = 1)
            pgui.click(x=1234, y=601, duration = 1)
            pgui.click(x=821, y=384, duration = 1)
            pgui.click(x=1002, y=524, duration = 1)
            pgui.click(x=1148, y=671, duration = 1)
            pgui.click(x=612, y=359, duration = 1)
            pgui.click(x=601, y=422, duration = 1)
            pgui.click(x=1263, y=806, duration = 1)
            time.sleep(1)
            pgui.click(x=989, y=526, duration = 1)
            #pgui.click(x=1407, y=322, duration = 1)
            pgui.hotkey('Y')
            pgui.hotkey('Enter')
            
            time.sleep(1)
            
            pgui.click(x=933, y=4, duration = 1)
            pgui.click(x=94, y=33, duration = 1)
            pgui.hotkey('R')
            time.sleep(58)
mapchange()

