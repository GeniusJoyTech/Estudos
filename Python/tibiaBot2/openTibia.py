import subprocess
import os
import pyautogui

from maxTela import openTibia
from isOpen import isOpen

TibiaOpened = isOpen()

if TibiaOpened:
   openTibia()
else:
    # Caminho completo para o executável do aplicativo
    caminho_aplicativo = os.path.expanduser("game/Hades_Ascension_Launcher.exe")

    # Verifica se o arquivo existe antes de abri-lo
    if os.path.exists(caminho_aplicativo):
        subprocess.Popen([caminho_aplicativo])
        coordenadas = None
        while coordenadas is None:
            coordenadas = pyautogui.locateOnScreen('game/img/Login_button.png', confidence=0.8)
            if coordenadas is not None:       
                pyautogui.click(coordenadas)
        
        coordenadas = None
        while coordenadas is None:
            coordenadas = pyautogui.locateOnScreen('game/img/Login.png', confidence=0.8)
            if coordenadas is not None:       
                break
        
    else:
        print("O arquivo do aplicativo não foi encontrado.")
