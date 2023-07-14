import pyautogui

def centerClick(dir):
    # Obtém a posição do botão na tela
    position = pyautogui.locateOnScreen(dir)

    # Verifica se o botão foi encontrado
    if position is not None:
    # Obtém as coordenadas centrais do botão
        x, y, largura, altura = position
        x_centro = x + largura // 2
        y_centro = y + altura // 2

    # Move o mouse para o centro do botão e clica nele
        pyautogui.moveTo(x_centro, y_centro)
        pyautogui.click()
    else:
        print("O botão não foi encontrado.")
        s = pyautogui.screenshot(region=(position.left, position.top, position.width, position.height))
        s.save('teste.png')