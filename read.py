from matplotlib.pyplot import imread

#Función:   Lee una imagen del disco
#Entrada:   Nombre de la imagen (String)
#Salida:    Imagen (numpy.ndarray)
def read(path):
    image = imread(path)
    return image
