import pyautogui
from utils import centerClick as c

def keySubMenu():
    pyautogui.keyDown('ctrl')
    pyautogui.click()
    pyautogui.keyUp('ctrl')

def openBrowseField():
    keySubMenu()
    c.centerClick(pyautogui.locateOnScreen('game/img/browse.png', confidence=0.7))
