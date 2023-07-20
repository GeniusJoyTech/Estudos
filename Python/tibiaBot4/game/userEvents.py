import pyautogui
from utils import centerClick as c

def cPosition():
    current_position = pyautogui.position()
    x = current_position.x
    y = current_position.y
    print(f"Coordenadas do mouse: x={x}, y={y}")


def ctrlClick():
    pyautogui.keyDown('ctrl')
    pyautogui.click()
    pyautogui.keyUp('ctrl')

def moveToBag(x1,y1,x2,y2):
    pyautogui.moveTo(x1,y1)
    pyautogui.mouseDown()
    pyautogui.moveTo(x2,y2)
    pyautogui.mouseUp()
    
def openBrowseField():
    ctrlClick()
    b= pyautogui.locateOnScreen('game/img/browse.png', confidence=0.7)
    while b is None:
        b = pyautogui.locateOnScreen('game/img/browse.png', confidence=0.7)
    c.centerClick(b)

def contador():
    x=100
    while x > 0: 
            screenshot = p.screenshot(region=(1138, 488, 43, 43))
            filename = f'gold_{x}.png'
            screenshot.save(filename)
            p.click(1199,532)
            x=x-1
