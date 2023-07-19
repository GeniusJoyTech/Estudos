import pytesseract
from PIL import Image
import cv2
import numpy as np
pytesseract.pytesseract.tesseract_cmd = 'C:/Tesseract-OCR/tesseract.exe'

# Defina o caminho para a imagem
caminho_imagem = 'C:/Git/Estudos/Python/tibiaBot4/teste/Cap.jpg'

# Abra a imagem usando o Pillow
imagem = Image.open(caminho_imagem)

# Converta a imagem para escala de cinza diretamente com o OpenCV
imagem_cinza = cv2.cvtColor(cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)

# Binarize a imagem (números brancos, fundo preto)
_, imagem_bin = cv2.threshold(imagem_cinza, 200, 255, cv2.THRESH_BINARY)

# Converta a imagem binarizada de volta para o formato PIL
imagem_bin_pil = Image.fromarray(imagem_bin)

# Use o pytesseract para capturar o texto da imagem binarizada
texto_capturado = pytesseract.image_to_string(imagem_bin_pi)

# Imprima o texto capturado
print(f'Texto: {texto_capturado}')
