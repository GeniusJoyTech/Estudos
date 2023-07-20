import pyautogui as p

p.hotkey('alt', 'tab')

x=100
while x > 0: 
        screenshot = p.screenshot(region=(1138, 488, 43, 43))
        filename = f'gold_{x}.png'
        screenshot.save(filename)
        p.click(1199,532)
        x=x-1



















'''
from pynput.mouse import Listener

def armazenar_cliques():
    coordenadas = []

    def on_click(x, y, button, pressed):
        if pressed:
            print(f"Posicao ({x}, {y})")
            coordenadas.append((x, y))
            listener.stop()

    with Listener(on_click=on_click) as listener:
        listener.join()

    return coordenadas

cliques = armazenar_cliques()
a=cliques[0]
cliques = armazenar_cliques()
b=cliques[0]
larg = abs(a[0] - b[0])
alt = abs(a[1] - b[1])


print(f'Coordenadas do jogo:\n x = {a}\ny = {b}\nwidth = {larg}\nheight = {alt}'
      )
'''























#from game import Radar as r
#from game import userEvents as user

#from utils import checkText

#checkText

'''
p = [
        (5, 8) #direita
    ]
r.Altenador
r.radarPos(p)
user.openBrowseField()
user.moveToBag(1736, 872, 1911, 722)
user.moveToBag(1736, 872, 1911, 722)
user.moveToBag(1736, 872, 1911, 722)
user.moveToBag(1736, 872, 1911, 722)
user.moveToBag(1736, 872, 1911, 722)
user.moveToBag(1736, 872, 1911, 722)
user.moveToBag(1736, 872, 1911, 722)
user.moveToBag(1736, 872, 1911, 722)
user.moveToBag(1736, 872, 1911, 722)
user.moveToBag(1736, 872, 1911, 722)
user.moveToBag(1736, 872, 1911, 722)
user.moveToBag(1736, 872, 1911, 722)
'''