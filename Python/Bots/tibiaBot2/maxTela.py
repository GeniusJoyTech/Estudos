from windowTibia import windowTibia
import pygetwindow as gw
import time

window = windowTibia()

def openTibia():
    if window is not None:
        window.maximize()
        time.sleep(1)