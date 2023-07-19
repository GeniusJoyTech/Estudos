import pyautogui
from utils.maxTela import maxTibia
def playGame():
    coordenadas = None
    while coordenadas is None:
        coordenadas = pyautogui.locateOnScreen('game/img/objetos/Login_button.png', confidence=0.8)
        if coordenadas is not None:       
            pyautogui.click(coordenadas)
    
    coordenadas = None

    while coordenadas is None:
        coordenadas = pyautogui.locateOnScreen('game/img/objetos/Login.png', confidence=0.8)
        if coordenadas is not None:       
            break
