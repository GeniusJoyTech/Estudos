from game import Radar as r
from game import userEvents as user




#pyautogui.moveTo(1898, 628)

p = [
        (5, 8) #direita
    ]

r.radarPos(p)
user.openBrowseField()

'''
pyautogui.hotkey('alt', 'tab')
i = pyautogui.locateOnScreen('C:/Git/Estudos/Python/tibiaBot4/teste/Cap.png', region=(1699,560,72,220), confidence=0.8)

if i:
    # A imagem foi encontrada, e 'image_location' é a região onde foi localizada dentro da área específica
    print("Imagem encontrada na região:", i)
    #screenshot = pyautogui.screenshot(region=i)
    #screenshot.show()
    pyautogui.moveTo(i)
else:
    print("Imagem não encontrada na região específica.")
'''
