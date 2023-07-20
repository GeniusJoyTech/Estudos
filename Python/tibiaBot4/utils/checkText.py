import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:/Tesseract-OCR/tesseract.exe'

# Defina o caminho para a imagem
caminho_imagem = 'C:/Git/Estudos/Python/tibiaBot4/game/font/font_0.png'

# Leia a imagem em escala de cinza
imagem = cv2.imread(caminho_imagem)

# Binarize a imagem usando cv2.THRESH_BINARY
_, imagem_binarizada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

imagem_maximizada = cv2.resize(imagem_binarizada, (600, 600))

_, imagem_maximizada2 = cv2.threshold(imagem_maximizada, 220, 255, cv2.IMREAD_GRAYSCALE)

# Defina as coordenadas do canto superior esquerdo e do canto inferior direito da região que deseja cortar
x_inicial, y_inicial = 200, 350
x_final, y_final = 600, 590

# Corte a região de interesse (ROI) da imagem binarizada
regiao_cortada = imagem_maximizada2[y_inicial:y_final, x_inicial:x_final]

# Exiba a imagem original, a imagem binarizada e a região cortada
cv2.imshow('Imagem Original', imagem)
cv2.waitKey(0)
cv2.imshow('Imagem Binarizada', imagem_maximizada2)
cv2.waitKey(0)
cv2.imshow('Região Cortada', regiao_cortada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Use o pytesseract para capturar o texto da região cortada
texto_capturado = pytesseract.image_to_string(imagem_maximizada)

# Imprima o texto capturado
print(f'Texto: {texto_capturado}')




'''
import cv2
import numpy as np

# 2. Carregar as imagens - imagem principal e imagem a ser procurada
imagem_principal = cv2.imread('game/font/gold_100.png')
imagem_procurada = cv2.imread('game/font/font_0.png')

# 3. Encontrar correspondências usando o método de casamento de características ORB
orb = cv2.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(imagem_procurada, None)
keypoints2, descriptors2 = orb.detectAndCompute(imagem_principal, None)

# 4. Verificar se os descritores não são None antes de converter para o tipo de dados correto
if descriptors1 is not None and descriptors2 is not None:
    descriptors1 = descriptors1.astype(np.float32)
    descriptors2 = descriptors2.astype(np.float32)

    # 5. Encontrar correspondências entre as duas imagens
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)

    # 6. Desenhar correspondências na imagem principal
    resultado = cv2.drawMatches(imagem_procurada, keypoints1, imagem_principal, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # 7. Mostrar o resultado
    cv2.imshow('Resultado', resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Não foi possível encontrar características suficientes na imagem principal.")
'''