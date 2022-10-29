from keras.datasets import mnist
from PIL import Image
import random

def load_random_mnist_image():
    (train_X, _), _ = mnist.load_data()
    image_array = train_X[random.randint(0, len(train_X))]
    image = Image.fromarray(image_array)
    return image
