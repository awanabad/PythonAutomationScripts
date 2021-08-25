#! python3 

import pyautogui as pg
import time, sys

#open any app 
pg.press('win')
time.sleep(0.25)

if len(sys.argv) > 1:
    searchApp = ' '.join(sys.argv[1:])
    pg.write(searchApp)
    pg.press('enter')



