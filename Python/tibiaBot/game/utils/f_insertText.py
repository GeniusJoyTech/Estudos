import time
import pyautogui

def iTxt(diretorio_imagem, txt, Place_holder_name):
    # Espera por 5 segundos (ajuste o tempo conforme necessário)
    time.sleep(3)

    # Obtém a posição do campo de texto na tela
    posicao_campo = pyautogui.locateOnScreen(diretorio_imagem)

    # Verifica se o campo de texto foi encontrado
    if posicao_campo is not None:
        # Obtém as coordenadas do canto superior esquerdo do campo
        x, y, largura, altura = posicao_campo

        # Move o mouse para o campo de texto e clica nele
        x_centro = x + largura // 2
        y_centro = y + altura // 2
        pyautogui.moveTo(x_centro, y_centro)
        pyautogui.click()

        # Insere o texto no campo de texto simulando a digitação
        pyautogui.typewrite(txt)
    else:
        print(f"O campo de texto para '{Place_holder_name}' não foi encontrado.")

