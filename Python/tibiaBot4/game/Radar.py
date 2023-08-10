import pyautogui
from config import config
import math

num_rows = 15
num_cols = 11
game_config = config.read_config('Game')
section_height = game_config.get('larg') // num_rows
section_width = game_config.get('alt') // num_cols


game_br_config = config.read_config('BrowseField')
eixoBrX = game_br_config.get('pos1')[0]
eixoBrY = game_br_config.get('pos1')[1]
section_br_height = game_br_config.get('larg')
section_br_width = game_br_config.get('alt')

game_bag_config = config.read_config('Bag')
eixoBagX = game_bag_config.get('pos2')[0]
eixoBagY = game_bag_config.get('pos2')[1]
eixoBgX = game_bag_config.get('pos1')[0]
eixoBgY = game_bag_config.get('pos1')[1]
section_bag_height = game_bag_config.get('larg')
section_bag_width = game_bag_config.get('alt')

Altenador = pyautogui.hotkey('alt', 'tab')


def radarFull():
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

def radarPersona(row, col):
    x = game_config.get('pos1')[0] + col * section_width
    y = game_config.get('pos1')[1] + row * section_height
    
    screenshot = pyautogui.screenshot(region=(x, y, section_width, section_height))
    filename = f'game/img/screenshot_{row}_{col}.png'
    screenshot.save(filename)
    return(x, y)

def radarPos(row, col):
    x = game_config.get('pos1')[0] + col * section_width
    y = game_config.get('pos1')[1] + row * section_height
    w = x + section_width // 2
    h = y + section_height // 2
    pyautogui.moveTo(w, h)
    return x, y, section_width, section_height
        

def find_all_images(image_path):
    # Exemplo de uso    
    # Radar.find_all_images('game/img/gold/gold_94.png')
    unique_matches = []
    min_distance_threshold = 35
    match = 0
    for match in pyautogui.locateAllOnScreen(image_path, confidence=0.971, region=(eixoBgX-2, eixoBgY-2, section_bag_width, section_bag_height)):
        x, y, width, height = match
        current_center = (x + width / 2, y + height / 2)
        
        # Verifica se a distância para todas as correspondências únicas é maior do que o limiar
        if not any(math.sqrt((current_center[0] - center[0]) ** 2 + (current_center[1] - center[1]) ** 2) < min_distance_threshold for center in unique_matches):
            unique_matches.append(current_center)
            #print(f"Imagem encontrada em ({x}, {y}) com largura {width}, altura {height}")
    
    
    total_unique_matches = len(unique_matches)
    #print(f"Total de correspondências únicas encontradas: {total_unique_matches}")
    return unique_matches

def find_all_images2(image_path, cof):
    # Exemplo de uso    
    # Radar.find_all_images('game/img/gold/gold_94.png')
    unique_matches = []
    min_distance_threshold = 35
    match = 0
    for match in pyautogui.locateAllOnScreen(image_path, confidence=cof, region=(eixoBgX-2, eixoBgY-2, section_bag_width, section_bag_height)):
        x, y, width, height = match
        current_center = (x + width / 2, y + height / 2)
        
        # Verifica se a distância para todas as correspondências únicas é maior do que o limiar
        if not any(math.sqrt((current_center[0] - center[0]) ** 2 + (current_center[1] - center[1]) ** 2) < min_distance_threshold for center in unique_matches):
            unique_matches.append(current_center)
            #print(f"Imagem encontrada em ({x}, {y}) com largura {width}, altura {height}")
    
    
    total_unique_matches = len(unique_matches)
    #print(f"Total de correspondências únicas encontradas: {total_unique_matches}")
    return unique_matches


def Guest(row,col):
    x,y, a, b = radarPos(row, col)
    tapete = pyautogui.locateOnScreen(f'game/img/screenshot_{row}_{col}.png', confidence = 0.75, region=(x,y,a,b))
    if tapete is None:
        return 0#retorno vazio significa que houve alteração na area a ser observada, logo pode ser que alguem tenha pisado ali.
    else:
        return 1
    
