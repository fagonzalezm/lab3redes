from read import read as read
from convolve import convolve as convolve
from write import write as write
import numpy as np
from scipy import signal
from scipy import misc
import sys

def main():
    image = read('leena512.bmp')
    kernel = np.array([
        [1,4,6,4,1],
        [4,16,24,16,4],
        [6,24,36,24,6],
        [4,16,24,16,4],
        [1,4,5,4,1]
    ])
    kernel = kernel/256
    convolution = convolve(kernel,kernel)
    #write('out.bmp', convolution)
    np.set_printoptions(threshold=sys.maxsize)
    print(convolution)

main()


