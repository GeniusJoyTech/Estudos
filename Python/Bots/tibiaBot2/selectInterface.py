from utils.centerClick import centerClick
#---
import config
import pyautogui
#---

def switchInterface():
    # Localizar a imagem "imagem_exemplo.png" na tela
    coordenadas = pyautogui.locateOnScreen('game/img/login.png', confidence=0.8)

    if coordenadas is not None:
        pyautogui.typewrite(config.email)
        pyautogui.hotkey('tab')
        pyautogui.typewrite(config.senha)
        coordenadas = None
        while coordenadas is None:
            coordenadas = pyautogui.locateOnScreen('game/img/rememberOk.png', confidence=0.8)
            if coordenadas is not None:
                centerClick('game/img/rememberOk.png')
                break
            else:
                coordenadas = pyautogui.locateOnScreen('game/img/rememberNull.png', confidence=0.8)
                if coordenadas is not None:
                    break
        #Click no botão de login
        pyautogui.hotkey('enter')
        coordenadas = None
        #Aguardar aparecer persona
        while coordenadas is None:
            coordenadas = pyautogui.locateOnScreen('game/img/selectCharacter.png', confidence=0.5)
            if coordenadas is not None:
                pyautogui.hotkey('enter')

    else:
        # A imagem não foi encontrada
        print("Area de login não foi encontrada na tela.")