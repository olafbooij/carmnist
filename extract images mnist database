from keras.datasets import mnist
from PIL import Image, ImageOps

# Load the mnist dataset
(train_X, train_y), (test_X, test_y) = mnist.load_data()

# Extract and save image as a file
train_images = []
test_images = []
for item in range(100):

    #select 'test' and 'train' image from the mnist database
    train_image_array = train_X[item]
    test_image_array = test_X[item]

    train_image = Image.fromarray(train_image_array)
    test_image = Image.fromarray(test_image_array)
    train_image.save(f"train_x_images/{item}.png")
    test_image.save(f"test_x_images/{item}.png")

    # add as a "pillow_image" to a list
    trainimage_x = Image.open(f"train_x_images/{item}.png")
    testimage_x = Image.open(f"test_x_images/{item}.png")
    train_images.append(trainimage_x)
    test_images.append(testimage_x)
print(train_images)
print(test_images)
