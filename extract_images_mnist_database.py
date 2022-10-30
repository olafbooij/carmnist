from keras.datasets import mnist
from PIL import Image, ImageOps
from pathlib import Path
import random

def save_first_100_images(array, path):
    # Extract and save image as a file
    images = []

    for item in range(100):
        # select 'test' or 'train' image from the mnist database
        image_array = array[item]

        image = Image.fromarray(image_array)

        path = Path(path)
        path.mkdir(exist_ok=True)
        image.save(path / f"{item}.png")

        # add as a "pillow_image" to a list
        image_x = Image.open(f"{path}/{item}.png")

        images.append(image_x)

    return images

def load_random_mnist_image():
    image_list = []
    (train_X, _), (test_X, _) = mnist.load_data()
    image_array_train = train_X[random.randint(0, len(train_X))]
    image_array_test = test_X[random.randint(0, len(test_X))]
    test_image = Image.fromarray(image_array_test)
    train_image = Image.fromarray(image_array_train)
    image_list.append(test_image)
    image_list.append(train_image)
    return image_list

print(load_random_mnist_image())

# Load the mnist dataset (caches in .keras/datasets/mnist.npz)
# (train_X, train_y), (test_X, test_y) = mnist.load_data()

# print(save_first_100_images(array=test_X, path="test_x_images"))
# print(save_first_100_images(array=train_X, path="train_x_images"))

