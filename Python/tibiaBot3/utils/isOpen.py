from utils.windowTibia import windowTibia
window = windowTibia()
def isOpen():
    if window is None:
        print("Janela não encontrada.")
        return False
    else:
            window.minimize()
            return True