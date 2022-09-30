from pathlib import Path
from PIL import Image, ImageOps


number_in_frame = Path("numberinframe")
number_in_frame.mkdir(exist_ok=True)


for item in range(100):

    black_frame = Image.new("RGBA", (220, 220), (0, 0, 0))
    img = Image.open(f"test_x_images/{item}.png").convert("L")
    # img = inverted_image = ImageOps.invert(img_num)
    x, y = img.size
    black_frame.paste(img, (0, 0, x, y), img)
    black_frame.save(f"numberinframe/{item}.png", format="png")
