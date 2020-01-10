from matplotlib import pyplot as plt

def write(image, title):
    plt.title(title)
    plt.imshow(image, cmap='gray')
    plt.savefig(title)