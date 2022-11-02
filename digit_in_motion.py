from pathlib import Path
from keras.datasets import mnist
from PIL import Image
import numpy
import curved_motion
import random

SIZE = (100, 100)


def digit_in_motion(img_in):
    for item, img_out in enumerate(image_in_motion(img_in)):
        img_out.save(f'{path_out}/{"frame{:02d}.png".format(item)}')


def image_in_motion(img_in):
    img_out_size = SIZE
    for homography in curved_motion.curved_motion_homography(img_in.size, img_out_size):
        yield transform_image(homography, img_in)


def transform_image(homography, img_in):
    invhomography = numpy.linalg.inv(homography)
    invhomography /= invhomography[2, 2]
    img_out = img_in.transform(SIZE, Image.Transform.PERSPECTIVE, invhomography.flatten())
    return img_out


def load_random_mnist_image(use_test_set=False):
    (trainset, testset), _ = mnist.load_data()
    dataset = testset if use_test_set else trainset
    image_array = random.choice(dataset)
    image = Image.fromarray(image_array)
    return image

for video in range(100):
    path_out = Path("videos/video{:03d}".format(video))
    path_out.mkdir(parents=True, exist_ok=True)

    image = load_random_mnist_image(use_test_set=False)
    digit_in_motion(image)

