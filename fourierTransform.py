import numpy as np

#Función:   Aplica la transformada de Fourier a una imagen 2D
#Entrada:   Imagen (numpy.ndarray)
#Salida:    Transformada de Fourier (numpy.ndarray)
def fourierTransform(image):
    #Transformada de frecuencia
    frequency = np.fft.fft2(image)
    #Se desplaza para tener la componente de frecuancia cero en el centro
    fshift = np.fft.fftshift(frequency)
    #Se obtiene el espectro de magnitudes
    magnitudFFT = 20*np.log(np.abs(fshift))
    return magnitudFFT