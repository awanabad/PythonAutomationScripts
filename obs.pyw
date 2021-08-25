#!python3

#Program starts Obsidian and loops image mover.

import os, shutil, time, psutil, schedule
import pyautogui as pg

interval = 15
sleep = 1

#Opens Obsidian
pg.press('win')
time.sleep(0.25)
pg.write('Obsidian')
pg.press('enter')

#Image Mover Code
fromDirectory = 'C:/Users/abadu/Google Drive/Work/Obsidian Vault'
toDirectory = 'C:/Users/abadu/Google Drive/Work/Obsidian Vault/_imageData'

def imageMover():

    Files = os.listdir(fromDirectory)
    fileIndex = -1
    i=0

    for file in Files:
        if (file.find('Pasted image') == 0) or (file.find('IMG') == 0):
            fileIndex = i
            fileName = Files[fileIndex]

            print('Python: '+ fileName +' found at ' + str(fileIndex))
            shutil.move(fromDirectory + '/' + fileName, toDirectory + '/' + fileName)
            print('Python: File has been moved')

        i = i + 1

    if fileIndex == -1:
        print('Python: No files found.')
    else:
        print('Python: All files moved successfully.')

schedule.every(interval).seconds.do(imageMover)

#main loop
while True: 

    if (("Obsidian.exe" in (i.name() for i in psutil.process_iter()))==False):
        print('Python: Obsidian is closed, disabling Image Mover.')
        exit()

    print('Python: Obsidian Image Mover Active')
    schedule.run_pending()
    time.sleep(sleep)