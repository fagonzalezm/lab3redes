import numpy as np
import sys

def reshape(matrix, kernel):

    [n,m] = kernel.shape
    times = (n-1)/2
    reshaped = matrix
    while times>0:
        [n,m] = reshaped.shape
        columnAux = np.zeros((1,n))
        reshaped = np.concatenate((reshaped,columnAux), axis=0)
        reshaped = np.concatenate((columnAux,reshaped), axis=0)
        [n,m] = reshaped.shape
        rowAux = np.zeros((n,1))
        reshaped = np.concatenate((reshaped,rowAux), axis=1)
        reshaped = np.concatenate((rowAux,reshaped), axis=1)
        times = times - 1
    np.set_printoptions(precision=3)
    return reshaped
    


def convolve(image, kernel):
    reshaped = reshape(image,kernel)
    convolution = np.array([])
    [nImage, mImage] = image.shape
    [nKernel, mKernel] = kernel.shape
    np.set_printoptions(threshold=sys.maxsize)
    i = 0
    while i < nImage:
        j = 0
        while j < mImage:
            aux = 0
            p = 0
            while p < nKernel:
                q = 0
                while q < mKernel:
                    aux = aux + kernel[p,q]*reshaped[i+p,j+q]
                    q += 1
                p += 1
            convolution = np.append(convolution,aux)
            j += 1
        i += 1
    convolution = np.reshape(convolution,image.shape)
    return convolution

