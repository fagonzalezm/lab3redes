import numpy as np

#Función:   Agrega los ceros necesarios en los bordes de la matriz objetivos para luego aplicar un filtro
#Entrada:   Matriz por agrandar (numpy.ndarray) y máscara del filtro numpy.ndarray
#Salida:    Matriz ampliada (numpy.ndarray)
def reshape(matrix, kernel):
    #Dimnesiones de la máscara
    [n,m] = kernel.shape
    #Veces que se agregarán ceros en los bordes
    times = (n-1)/2
    #En reshaped se arma la matriz final
    reshaped = matrix
    #Se agregan 'times' veces ceros en los bordes de la matriz
    while times > 0:
        #Se actualiza la catidad de filas y columnas de la matriz final
        [n,m] = reshaped.shape
        #Matriz auxiliar para agregar ceros en los extremos laterales
        columnAux = np.zeros((1,n))
        #Se concatenan las matrices auxiliares a la matriz resultante
        reshaped = np.concatenate((reshaped,columnAux), axis=0)
        reshaped = np.concatenate((columnAux,reshaped), axis=0)
        [n,m] = reshaped.shape
        #Matriz auxiliar para agregar ceros en el extremo superior e inferior
        rowAux = np.zeros((n,1))
        reshaped = np.concatenate((reshaped,rowAux), axis=1)
        reshaped = np.concatenate((rowAux,reshaped), axis=1)
        times = times - 1
    return reshaped
    
#Función:   Función que realiza la convolución
#Entrada:   Imagen de entrada (numpy.ndarray) y máscara del filtro (numpy.ndarray)
#Salida:    Imagen con el filtro aplicado (numpy.ndarray)
def convolve(image, kernel):
    #Se agregan los ceros en los bordes para poder aplicar la máscara en los bordes de la imagen
    reshaped = reshape(image,kernel)
    #En 'convolution' se arma la matriz final
    convolution = np.array([])
    #Dimensiones de la imágen y la máscara
    [nImage, mImage] = image.shape
    [nKernel, mKernel] = kernel.shape
    #Se recorre la imagen
    i = 0
    while i < nImage:
        j = 0
        while j < mImage:
            #En 'aux' se calcula el valor de las sumas ponderadas de la convolución 
            aux = 0
            #Se recorre la máscara
            p = 0
            while p < nKernel:
                q = 0
                while q < mKernel:
                    #Se le va sumando a 'aux' las sumas ponderadas de la iteración local
                    aux = aux + kernel[p,q]*reshaped[i+p,j+q]
                    q += 1
                p += 1
            #Se agrega a 'convolution' el resultado de las suma ponderada local 'aux'
            convolution = np.append(convolution,aux)
            j += 1
        i += 1
    #Se ordenan los elementos de 'convolution' para que quede con la misma dimensión que la imagen original
    convolution = np.reshape(convolution,image.shape)
    return convolution

