import time
import pyautogui

def iTxt(diretorio_imagem, txt, Place_holder_name):
    time.sleep(1)

    # Obtém a posição do campo de texto na tela
    posicao_campo = pyautogui.locateOnScreen(diretorio_imagem, 0.9)

    # Verifica se o campo de texto foi encontrado
    if posicao_campo is not None:
        x, y, largura, altura = posicao_campo
        x_centro = x + largura // 2
        y_centro = y + altura // 2
        # Insere o texto no campo de texto simulando a digitação
        pyautogui.typewrite(txt)
    else:
        print(f"O campo de texto '{Place_holder_name}' não foi encontrado.")

