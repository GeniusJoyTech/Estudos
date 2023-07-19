import time

def alarm(x):
    print(f'---\npausa programada de {x} segundo(s).')
    time.sleep(x)
    print('\nContinuando.\n---\n')