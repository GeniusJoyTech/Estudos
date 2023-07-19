from pynput.mouse import Listener
import config as c
import pymsgbox

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

msg = '\nPrimeiro no topo esquerdo.\nSegundo na lateral abaixo a direita.'
pymsgbox.alert(text=f'Clique no dois cantos laterais da tela do jogo. {msg}', title='Coordenadas do jogo', button='OK')
print('Coordenadas do jogo.')
cliques = armazenar_cliques()
a=cliques[0]
cliques = armazenar_cliques()
b=cliques[0]
larg = abs(a[0] - b[0])
alt = abs(a[1] - b[1])

c.update_config("Game", a, b, alt, larg)


pymsgbox.alert(text=f'Clique no dois cantos laterais da tela da mochila. {msg}', title='Coordenadas da bag', button='OK')

print('Coordenadas da backpack ou mochila.')
cliques = armazenar_cliques()
a=cliques[0]
cliques = armazenar_cliques()
b=cliques[0]
larg = abs(a[0] - b[0])
alt = abs(a[1] - b[1])

c.update_config("Bag", a, b, alt, larg)

pymsgbox.alert(text=f'Clique no dois cantos laterais do broseField. {msg}', title='Coordenadas.', button='OK')
cliques = armazenar_cliques()
a=cliques[0]
cliques = armazenar_cliques()
b=cliques[0]
larg = abs(a[0] - b[0])
alt = abs(a[1] - b[1])

c.update_config("BrowseField", a, b, alt, larg)


Game = c.read_config("Game")
print(f"Tela do Game: '{Game}'")
Bag = c.read_config("Bag")
print(f"Tela da Bag: '{Bag}'")
BrowseField = c.read_config("BrowseField")
print(f"Tela do BrowseField: '{BrowseField}'")
