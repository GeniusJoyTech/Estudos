import pyautogui as py
import os
import time
import keyboard
import sys
def chao():
    time.sleep(15)
# Carregar as imagens
    
    # Verificar se a pasta "tests" existe, caso contrário, criá-la
    pasta_tests = 'tests'
    if not os.path.exists(pasta_tests):
        os.makedirs(pasta_tests)

    x= None
    while(x is None):
        x = py.locateOnScreen('game/img/interfaceGame.png', confidence=0.6)
        if keyboard.is_pressed('esc'):
            sys.exit()

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
            caminho_quadrado = os.path.join(pasta_tests, f'quadrado_{row}_{col}.png')
            quadrado.save(caminho_quadrado)
#Funções de captura de moedas

#Função de pegar moeda no chão, a moeda deve estar ao lado do character
    #Função para selecionar a moeda no 'chão' e guardar na bolsa.

#Função de contar moeda
    # As moedas no jogo são Ouro, prata e diamante
        # 100 ouro é igual a 1Prata
        # 100 Prata é igual a 1Diamante
        # 1 Diamante é igual a 100prata
        # 1 prata é igual a 100ouro
        # Logo 10000o=100p=1d está regra não muda

#Função de separar moedas.
 