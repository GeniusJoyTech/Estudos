import pyautogui

def centerClick(dir):

    if dir is not None:
        x, y, largura, altura = dir
        x_centro = x + largura // 2
        y_centro = y + altura // 2

        pyautogui.moveTo(x_centro, y_centro)
        pyautogui.click()
    else:
        print("Objeto não encontrado. __centerClick__")
        