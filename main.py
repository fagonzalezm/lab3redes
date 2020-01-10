from read import read as read
from convolve import convolve as convolve
from write import write as write
import numpy as np
from scipy import signal
from scipy import misc
import sys

def main():
    image = read('leena512.bmp')
    kernel1 = np.array([
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 5, 4, 1]
    ])
    kernel1 = kernel1/256
    
    kernel2 = np.array([
        [1, 2, 0, -2, -1],
        [1, 2, 0, -2, -1],
        [1, 2, 0, -2, -1],
        [1, 2, 0, -2, -1],
        [1, 2, 0, -2, -1]
    ])

    convolution1 = convolve(image,kernel1)
    convolution2 = convolve(image,kernel2)
    write(image, "Leena")
    write(convolution1, "LeenaFiltroGaussiano")
    write(convolution2, "LeenaFiltroBordes")

main()


