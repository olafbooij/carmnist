from keras.datasets import mnist
from PIL import Image, ImageOps
from pathlib import Path


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


# Load the mnist dataset (caches in .keras/datasets/mnist.npz)
(train_X, train_y), (test_X, test_y) = mnist.load_data()

print(save_first_100_images(array=test_X, path="test_x_images"))
print(save_first_100_images(array=train_X, path="train_x_images"))
