from pathlib import Path
from PIL import Image
import numpy
from scipy import ndimage

size = Path("size")
size.mkdir(exist_ok=True)
number_in_frame = Path("numberinframe")
size.mkdir(exist_ok=True)

def simple_movement(image_path):
    for item in range(1, 25):
        img_in = Image.open(image_path)
        array = numpy.array(img_in)

        zoom_array = ndimage.zoom(array, (item, item))

        img_out = Image.fromarray(zoom_array)
        img_out.save(f'size/size{item}.jpg')

        black_frame = Image.new("RGBA", (220, 220), (0, 0, 0))
        img = Image.open(f"size/size{item}.jpg").convert("L")
             x, y = img.size
        black_frame.paste(img, (0, 0, x, y), img)
        black_frame.save(f"numberinframe/{item}.png", format="png")
        transform = Image.open(f"numberinframe/{item}.png")

simple_movement(image_path="test_x_images/1.png")
