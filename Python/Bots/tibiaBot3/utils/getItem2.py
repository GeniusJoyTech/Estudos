from pynput.mouse import Listener
def Localizador():    
    def on_click(x, y, button, pressed):
        if pressed:
            print(f"Clique detectado em ({x}, {y})")
            return False
    with Listener(on_click=on_click) as listener:
        listener.join()
    
Localizador()    
Localizador()    
Localizador()    
Localizador()