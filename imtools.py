try:
    from PIL import Image
except:
    print ("PIL.Image not found, now trying with Image")
    from Image import *
import numpy as np
import matplotlib.pyplot as plt

def open_image(path):
    """Convert PNG image to numpy 2D float array"""
    i = Image.open(path).convert('L')
    try:
        a = np.frombuffer(i.tobytes(), np.uint8).astype(np.float64)
    except:
        a = np.fromstring(i.tostring(), np.uint8).astype(np.float64)
    return a.reshape((i.size[1], i.size[0]))

def display_image(array, now = True, vmin = None, vmax = None):
    """Display 2D array as image"""
    plt.imshow(array, cmap = plt.cm.gray, interpolation = 'nearest', vmin = vmin, vmax = vmax)
    if now:
        plt.show()

def display_images(images, lines = None, columns = None, indices = None, vmin = None, vmax = None):
    """Display a list of 2D arrays as images"""
    if columns is None:
        if lines is None:
            columns = int(np.ceil(np.sqrt(len(images))))
        else:
            columns = int(np.ceil(float(len(images)) / lines))
    if lines is None:
        lines = int(np.ceil(float(len(images)) / columns))
    if indices is None:
        indices = range(1, len(images) + 1)
    for k in range(len(images)):
        if not images[k] is None:
            plt.subplot(lines, columns, indices[k])
            display_image(images[k], vmin = vmin, vmax = vmax, now = False)
    plt.show()

def save_image(array, path):
    """Convert numpy 2D float array to PNG image"""
    array[array < 0] = 0
    array[array > 255] = 255
    try:
        i = Image.frombytes('L', (array.shape[1], array.shape[0]), array.astype(np.uint8).tostring())
    except:
        i = Image.fromstring('L', (array.shape[1], array.shape[0]), array.astype(np.uint8).tostring())
    i.save(path, 'PNG')
    
def shift_image(u, k, l):
    """Returns a shifted numpy 2D array"""
    return np.roll(u, (k, l), axis = (0, 1))
