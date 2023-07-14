import time
import pyautogui

# Espera por 10 segundos (ajuste o tempo conforme necessário)
time.sleep(5)

# Obtém a posição do botão na tela
posicao_botao = pyautogui.locateOnScreen('game/img/Login_button.png')

# Verifica se o botão foi encontrado
if posicao_botao is not None:
    # Obtém as coordenadas centrais do botão
    x, y, largura, altura = posicao_botao
    x_centro = x + largura // 2
    y_centro = y + altura // 2

    # Move o mouse para o centro do botão e clica nele
    pyautogui.moveTo(x_centro, y_centro)
    pyautogui.click()
else:
    print("O botão não foi encontrado.")
