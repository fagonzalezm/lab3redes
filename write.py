from matplotlib import pyplot as plt

#Función:   Guarda un gráfico (imagen) en disco
#Entrada:   Imagen por guardar (numpy.ndarray) y título de la imágen (String)
#Salida:    --
def write(image, title):
    plt.title(title)
    plt.imshow(image, cmap='gray')
    plt.savefig(title)