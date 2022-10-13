from random import seed
import numpy
import curved_motion

# let's use this trajectory of homographies to plot the trajectory of a square.

# Creates corners of a square
def square_points_3d(size):
  return [numpy.array([0.  , 0   , 1.]),
          numpy.array([size, 0.  , 1.]),
          numpy.array([size, size, 1.]),
          numpy.array([0.  , size, 1.])]


def project_point_homography(transformation, point):
  point_homogenious = [point[0], point[1], 1.]
  transformed_point_homogenious = numpy.dot(transformation, point_homogenious)
  projected_point = transformed_point_homogenious[0:2] / transformed_point_homogenious[2]
  return projected_point


def curved_square_motion(square, input_image_size, output_image_size):
  for cam_homography_square in curved_motion.curved_motion_homography(input_image_size, output_image_size):
    yield [project_point_homography(cam_homography_square, point) for point in square]


def print_square(square):
  for point in square + [square[0]]:
    print(point[0], point[1])
  print()

seed(2)

input_image_size = (28, 28)
output_image_size = (100, 100)
square = square_points_3d(input_image_size[0])

for square_transformed in curved_square_motion(square, input_image_size, output_image_size):
  print_square(square_transformed)
