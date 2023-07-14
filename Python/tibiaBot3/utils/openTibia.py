import subprocess
import os

from utils.playGame import playGame 
from utils.maxTela import maxTibia
from utils.isOpen import isOpen

from game.config.config import app

def openTibia():
    TibiaOpened = isOpen()
    if TibiaOpened:
        maxTibia()
    else:
        # Iniciando o game
        tibia = os.path.expanduser(app)
    
        if os.path.exists(tibia):
            subprocess.Popen(tibia)
            playGame()        
        else:
            print("Verifique se o executavel ou a aplicação estão corretamente configuradas.")
