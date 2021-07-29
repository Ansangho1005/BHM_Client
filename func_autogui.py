import pyautogui
import time
#import win32gui

#https://pythondocs.net/pyautogui/pywinauto-pyautogui-를-이용한-특정-윈도우-창-활성화-타이틀명-이용/

CLIENTNAME = "League of Legends"
INGAMECLIENTNAME = "League of Legends (TM) Client"

def isLolClientOpened():
    if CLIENTNAME == pyautogui.getActiveWindowTitle() :
        return True
    else:
        return False

def makeLolTop():

    while(isLolClientOpened()):
        pyautogui.keyDown('alt')
        pyautogui.hotkey('tab')
    return 0
    

def findUntil(filename : str, confidence=0.8):
    cnt = -1

    if cnt == -1:
        cnt=86400 #24hours
        wait = 0.5

    for i in range(cnt):
        imgpos = pyautogui.locateCenterOnScreen(filename, confidence= confidence)
        if imgpos != None:
            break
        elif isgamestarted():
            return 0
        else:
            time.sleep(wait)
        
    if imgpos == None:
        return 1
    else:
        return imgpos

def isgamestarted():
    if INGAMECLIENTNAME == pyautogui.getActiveWindowTitle():
        return True
    else:
        return False
    
    