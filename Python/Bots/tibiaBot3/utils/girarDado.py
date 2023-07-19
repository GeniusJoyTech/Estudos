import cv2
import numpy as np
import pyautogui
# Carrega a imagem de referência do objeto a ser detectado
reference_image = cv2.imread('game/img/dado.png', cv2.IMREAD_COLOR)

while True:
    # Captura da tela do jogo
    screenshot = pyautogui.screenshot()
    
    # Converte a imagem para formato OpenCV
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Realiza a detecção do objeto de referência
    result = cv2.matchTemplate(frame, reference_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Se a correspondência for encontrada acima de um limiar, faça algo
    if max_val > 0.8:
        # Obtém as coordenadas da detecção
        top_left = max_loc
        bottom_right = (top_left[0] + reference_image.shape[1], top_left[1] + reference_image.shape[0])
        
        # Realize a ação desejada com base na detecção
        object_center_x = (top_left[0] + bottom_right[0]) // 2
        object_center_y = (top_left[1] + bottom_right[1]) // 2
        pyautogui.rightClick(object_center_x, object_center_y)
        break
