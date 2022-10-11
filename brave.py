import time
import pyautogui as pgui

sleep_time = 2

# Auto Start Brave via python 
pgui.press('win')
time.sleep(sleep_time)   

pgui.write('brave')   
time.sleep(sleep_time)

pgui.press('enter')
time.sleep(sleep_time)

