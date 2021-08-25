#!python3

import time, pyautogui, schedule
from ctypes import Structure, windll, c_uint, sizeof, byref
import pygetwindow as gw

#set time (seconds) to minimize and check duration
minimizeTime = 30
schedulerTime = 10

#minimize check exceptions
exceptions = ['Backup and Sync', 'NVIDIA GeForce Overlay', 'Microsoft Store', 
'Settings', 'Program Manager', 'Malwarebytes Tray Application', 
'Microsoft Text Input Application', 'minimizeOnAFK.pyw - Untitled (Workspace) - Visual Studio Code']

#check if all windows are minimized
def are_all_minimized():
    min_check = []
    open_apps = gw.getAllWindows()

    for i in range(len(open_apps)):
        if (open_apps[i].title not in exceptions) and (open_apps[i].title):
            #print(open_apps[i].title + ' is minimized: ' + str(open_apps[i].isMinimized))
            min_check.append(open_apps[i].isMinimized)

    if False not in min_check:
        print("Python: All Windows Minimized")        
        return True
    else:
        return False

# minimize function
def minimize():
    x,y = pyautogui.size()
    pyautogui.moveTo(x - 2.5, y - 10, 0.2, pyautogui.easeOutCubic)
    pyautogui.click()
    pyautogui.moveTo(x/2, y/2, 0.2, pyautogui.easeOutCubic)

# use get_idle_duration() to get idle time in seconds
def idletime(): 
    
    class LASTINPUTINFO(Structure):
        _fields_=[('cbSize', c_uint), ('dwTime',c_uint)]

    def get_idle_duration():
            lastinputinfo = LASTINPUTINFO()
            lastinputinfo.cbSize = sizeof(lastinputinfo)
        
            windll.user32.GetLastInputInfo(byref(lastinputinfo))
            timediff = windll.kernel32.GetTickCount() - lastinputinfo.dwTime

            return timediff/1000
    print('Python: Idle time is ' + str(get_idle_duration()))

    if (get_idle_duration()) > minimizeTime:
        if not (are_all_minimized()):
             minimize()

schedule.every(schedulerTime).seconds.do(idletime)

#main loop
while 1: 
    print('Python: Minimize on AFK running')
    schedule.run_pending()
    time.sleep(1)

