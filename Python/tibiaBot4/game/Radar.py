import pyautogui
from config import config

num_rows = 11
num_cols = 15
Altenador = pyautogui.hotkey('alt', 'tab')

game_config = config.read_config('Game')

# Calcula a altura e largura de cada seção
section_height = game_config.get('larg') // num_rows
section_width = game_config.get('alt') // num_cols

def radarFull():
    Altenador
    # Loop para capturar cada seção
    for row in range(num_rows):
        for col in range(num_cols):
            # Calcula as coordenadas da seção atual
            x = game_config.get('pos1')[0] + col * section_width
            y = game_config.get('pos1')[1] + row * section_height
            
            # Captura a tela da seção atual
            screenshot = pyautogui.screenshot(region=(x, y, section_width, section_height))
            
            # Salva a captura de tela com um nome único (opcional)
            filename = f'screenshot_{row}_{col}.png'
            screenshot.save(filename)

def radarPersona():
    Altenador
    positions_to_save = [
        (4, 6), #esquerda/cima 
        (4, 7), #cima
        (4, 8), #direita/cima
        (5, 6), #esquerda
        (5, 7), #meio
        (5, 8), #direita
        (6, 6), #esquerda/baixo
        (6, 7), #baixo
        (6, 8)  #direita/baixo
    ]

    # Loop para capturar cada seção
    for row, col in positions_to_save:

        x = game_config.get('pos1')[0] + col * section_width
        y = game_config.get('pos1')[1] + row * section_height
        
        screenshot = pyautogui.screenshot(region=(x, y, section_width, section_height))
        filename = f'screenshot_{row}_{col}.png'
        screenshot.save(filename)

def radarPos(positions_to_save):
    Altenador
    '''
    positions_to_save = [
        (5, 8), #direita
    ]
    '''
    for row, col in positions_to_save:
        x = game_config.get('pos1')[0] + col * section_width
        y = game_config.get('pos1')[1] + row * section_height
        x = x + section_width // 2
        y = y + section_height // 2
        
        pyautogui.moveTo(x, y)
        
