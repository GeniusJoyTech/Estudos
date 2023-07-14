import subprocess
import os

# Caminho completo para o executável do aplicativo
caminho_aplicativo = os.path.expanduser("game/Hades_Ascension_Launcher.exe")

# Verifica se o arquivo existe antes de abri-lo
if os.path.exists(caminho_aplicativo):
    subprocess.run([caminho_aplicativo])
else:
    print("O arquivo do aplicativo não foi encontrado.")
