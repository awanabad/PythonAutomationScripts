#! python3 

import pyautogui as pg
import pygetwindow as gw
import time, sys 

#image detection
def detect_image(path):
    while True:
        image_location = pg.locateCenterOnScreen(path, confidence = 0.75)
        if image_location:
            time.sleep(0.15)
            pg.click(image_location[0], image_location[1])
            break

############################################################################################

y_shift = 40
y_shift_multiply = 0

if len(sys.argv) > 1:

        #open armoury crate app 
        pg.press('win')
        time.sleep(0.3)
        pg.write('armoury crate')
        pg.press('enter')

        AuraCrate = gw.getWindowsWithTitle('Armoury Crate')[0]

        detect_image('C:/Users/abadu/Google Drive/Scripts/screenshots/AuraSyncButton.PNG')
        time.sleep(0.5)
        pg.click()

        detect_image('C:/Users/abadu/Google Drive/Scripts/screenshots/AuraEffects.PNG')
        time.sleep(0.5)
        pg.click()

        if (sys.argv[1].isnumeric()):
        
            y_shift_multiply= int(sys.argv[1])
            
            detect_image('C:/Users/abadu/Google Drive/Scripts/screenshots/AuraEffectsDropdown.PNG')
            
            pg.move(0, y_shift*y_shift_multiply)
            pg.click()

        elif (sys.argv[1] == 'def'):

            detect_image('C:/Users/abadu/Google Drive/Scripts/screenshots/AuraEffectsDropdown.PNG')
            detect_image('C:/Users/abadu/Google Drive/Scripts/screenshots/AuraDefault.PNG')

        elif (sys.argv[1] == 'music'):

            detect_image('C:/Users/abadu/Google Drive/Scripts/screenshots/AuraEffectsDropdown.PNG')
            detect_image('C:/Users/abadu/Google Drive/Scripts/screenshots/AuraMusic.PNG')

        elif (sys.argv[1] == 'calm'):

            detect_image('C:/Users/abadu/Google Drive/Scripts/screenshots/AuraEffectsDropdown.PNG')
            detect_image('C:/Users/abadu/Google Drive/Scripts/screenshots/AuraCalm.PNG')

        elif (sys.argv[1] == 'off'):
            
            detect_image('C:/Users/abadu/Google Drive/Scripts/screenshots/AuraOff.PNG')

        AuraCrate.close()

else:
        print('Python: use input arguements.')
