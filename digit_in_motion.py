from pathlib import Path
from PIL import Image
import numpy
import curved_motion

SIZE = (100,100)


def digit_in_motion(image_path):
  path_out = Path("digit_in_motion")
  path_out.mkdir(exist_ok=True)
  img_in = Image.open(image_path)
  for item, img_out in enumerate(image_in_motion(img_in)):
    img_out.save(f'{path_out}/img_{item}.png')


def image_in_motion(img_in):
    img_out_size = SIZE
    for homography in curved_motion.curved_motion_homography(img_in.size, img_out_size):
        yield transform_image(homography, img_in)


def transform_image(homography, img_in):
    invhomography = numpy.linalg.inv(homography)
    invhomography /= invhomography[2, 2]
    img_out = img_in.transform(SIZE, Image.Transform.PERSPECTIVE, invhomography.flatten())
    return img_out


digit_in_motion(image_path="test_x_images/1.png")
