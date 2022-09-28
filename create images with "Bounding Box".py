from pathlib import Path
import cv2 as cv

for item in range(100):
    image = cv.imread(f"train_x_images/{item}.png")

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    thresh_image = cv.threshold(gray_image, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

    contours = cv.findContours(thresh_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    for i in contours:
        x, y, w, h = cv.boundingRect(i)
        cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 4)

    box_path = Path("box_images")
    box_path.mkdir(exist_ok=True)

    roi = image[y:y + h, x:x + w]
    cv.imwrite(f"{box_path}/roi{item}.jpg", roi)
