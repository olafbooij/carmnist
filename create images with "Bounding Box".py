from pathlib import Path
import cv2 as cv
from PIL import Image, ImageOps

box_path = Path("box_images")
number_in_frame = Path("numberinframe")
number_in_frame.mkdir(exist_ok=True)
box_path.mkdir(exist_ok=True)

for item in range(100):

    white_frame = Image.new("RGBA", (220, 220), (255, 255, 255))
    img_num = Image.open(f"test_x_images/{item}.png").convert("L")
    img = inverted_image = ImageOps.invert(img_num)
    x, y = img.size
    white_frame.paste(img, (0, 0, x, y), img)
    white_frame.save(f"numberinframe/{item}.png", format="png")

    image = cv.imread(f"numberinframe/{item}.png")

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    thresh_image = cv.threshold(gray_image, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

    contours = cv.findContours(thresh_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    for i in contours:
        x, y, w, h = cv.boundingRect(i)
        cv.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 4)

    roi = image[y:y + h, x:x + w]
    cv.imwrite(f"{box_path}/roi{item}.jpg", roi)
