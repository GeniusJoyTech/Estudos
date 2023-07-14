import pyautogui as py
import os
import sys

from utils.tempo import alarm
from utils.selectImage import imgshoted 

def getItem():
    alarm(2)
# Carregar as imagens
    py.hotkey('ctrl+alt+shift+pgdn')
    y = imgshoted()
    if y is not None:
        x = py.locateOnScreen(y, confidence=0.8)
    else:
        sys.exit("Encerrando por falta de dados, por favor verifique se você configurou a hotkey no tibia.")
    #x= None
    #while(x is None):
        
    #    py.hotkey('ctrl+alt+shift+pgdn')
    #    x = py.locateOnScreen('C:/Users/guwi/AppData/Local/HadesOTAscension/screenshots/2023-07-13_140639498_Gabzin_Hotkey.png', confidence=0.6)

    # Obter as informações da x encontrada
    left, top, width, height = x.left, x.top, x.width, x.height

    screenshot = py.screenshot(region=(left, top, width, height))

    # Salvar o print de tela em um arquivo
    screenshot.save('tests/screenshot.png')

    # Definir as dimensões dos quadrados
    tamanho_quadrado = (width // 15, height // 11)

    # Percorrer a grade de quadrados

    for row in range(11):
        for col in range(15):
            # Calcular as coordenadas de cada quadrado
            quadrado_left = left + col * tamanho_quadrado[0]
            quadrado_top = top + row * tamanho_quadrado[1]
            quadrado_right = quadrado_left + tamanho_quadrado[0]
            quadrado_bottom = quadrado_top + tamanho_quadrado[1]
            
            # Recortar o quadrado da x original
            quadrado = py.screenshot(region=(quadrado_left, quadrado_top, tamanho_quadrado[0], tamanho_quadrado[1]))
            
            # Salvar o quadrado na pasta "tests"
            caminho_quadrado = os.path.join('tests', f'quadrado_{row}_{col}.png')
            quadrado.save(caminho_quadrado)
 