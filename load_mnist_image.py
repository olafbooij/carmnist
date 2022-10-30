from keras.datasets import mnist
from PIL import Image
import random

def load_random_mnist_image(use_test_set=False):
    (trainset, testset), _ = mnist.load_data()
    dataset = testset if use_test_set else trainset
    image_array = random.choice(dataset)
    image = Image.fromarray(image_array)
    return image
