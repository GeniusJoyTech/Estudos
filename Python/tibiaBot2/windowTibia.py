import pygetwindow as gw

# Prefixo do título da janela do jogo
window_title_prefix1 = "Tibia"
window_title_prefix2 = "Hades Launcher"

# Encontra a janela pelo título que inicia com o prefixo fixo
def windowTibia():
    window = None
    for w in gw.getAllTitles():
        if w.startswith(window_title_prefix1) or w.startswith(window_title_prefix2):
            window = gw.getWindowsWithTitle(w)[0]
            break
    return window

