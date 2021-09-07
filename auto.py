import pyautogui as pgui
import time

def open_excel():
    pgui.click(x=1105, y=1065, duration = 1)
    pgui.hotkey('Enter')
    time.sleep(3)
    pgui.click(x=1105, y=1065, duration = 1)
    pgui.click(x=20, y=48, duration = 1)
    pgui.click(x=272, y=225, duration = 1)
open_excel()

def excel_command():
    time.sleep(1)
    pgui.hotkey('Ctrl','Shift','space')
    pgui.click(x=382, y=46, duration = 1)
    #pgui.click(x=1022, y=95, duration = 1)
    pgui.hotkey('ctrl','s')
excel_command()