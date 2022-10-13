from pathlib import Path
from PIL import Image
import numpy
import curved_motion


def digit_in_motion(image_path):
  path_out = Path("digit_in_motion")
  path_out.mkdir(exist_ok=True)
  img_in = Image.open(image_path)
  for item, img_out in enumerate(image_in_motion(img_in)):
    img_out.save(f'{path_out}/img_{item}.png')


def image_in_motion(img_in):
    img_out_size = (100, 100)
    for homography in curved_motion.curved_motion_homography(img_in.size, img_out_size):
        yield transform_image(homography, img_in)


def transform_image(homography, img_in):
    img_out = img_in  # TODO
    return img_out


digit_in_motion(image_path="test_x_images/1.png")
