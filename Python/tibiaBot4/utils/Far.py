import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def teste():
    # Caminho para a imagem que você deseja abrir
    caminho_imagem = 'teste/gold_50.png'

    # Usando a função cv2.imread() para abrir a imagem
    # O segundo argumento (cv2.IMREAD_COLOR) indica que a imagem será lida em cores (ignorando canais alfa, se houver)
    img = cv.imread(caminho_imagem, cv.IMREAD_GRAYSCALE)


    assert img is not None, "file could not be read, check with os.path.exists()"
    ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)#
    ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)#
    ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
    ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
    ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
        plt.show()