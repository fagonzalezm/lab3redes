from read import read as read
from convolve import convolve as convolve
from write import write as write
from fourierTransform import fourierTransform as fourierTransform
import numpy as np
from scipy import signal
from scipy import misc
import sys

def main():
    #Se lee la imagen 'leena512.bmp'
    image = read('leena512.bmp')
    #Se guarda la imagen en dormato png
    write(image, "Leena")

    #Máscara del filtro de Suavizado Gaussiano
    kernel1 = np.array([
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 5, 4, 1]
    ])
    kernel1 = kernel1/256
    
    #Máscara del filtro Detector de Bordes
    kernel2 = np.array([
        [1, 2, 0, -2, -1],
        [1, 2, 0, -2, -1],
        [1, 2, 0, -2, -1],
        [1, 2, 0, -2, -1],
        [1, 2, 0, -2, -1]
    ])

    #Se realizan las convoluciones y se guardan
    gaussianFilter = convolve(image,kernel1)
    edgeFilter = convolve(image,kernel2)
    write(gaussianFilter, "LeenaFiltroGaussiano")
    write(edgeFilter, "LeenaFiltroBordes")

    #Se calcula la Transformada de Fourier de la imagen original, del filtro de Suavizado Gaussiano y del filtro Detector de Bordes. Se guardan
    ftOriginal = fourierTransform(image)
    ftGaussianFilter = fourierTransform(gaussianFilter)
    ftEdgeFilter = fourierTransform(edgeFilter)
    write(ftOriginal, "TransformadaDeFourierOriginal")
    write(ftGaussianFilter, "TransformadaDeFourierSuavizadoGaussiano")
    write(ftEdgeFilter, "TransformadaDeFourierDetectorDeBordes")    

main()


