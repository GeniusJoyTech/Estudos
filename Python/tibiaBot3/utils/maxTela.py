from utils.windowTibia import windowTibia
from utils.tempo import alarm

window = windowTibia()

def maxTibia():
    if window is not None:
        window.maximize()
        alarm(1)