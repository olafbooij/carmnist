from random import uniform
from transformations import identity_matrix, euler_matrix, concatenate_matrices, translation_matrix
import numpy


# Creates corners of a square, shifted randomly
def random_square_points_3d():
  left, top, right, bottom = -.3, -.3, .3, .3  # 60 cm square square
  horizontal_shift = uniform(-1., 1.)
  vertical_shift   = uniform(-1., 1.)
  left   += horizontal_shift
  right  += horizontal_shift
  top    += vertical_shift
  bottom += vertical_shift
  return [numpy.array([left , top   , 0.]),
          numpy.array([right, top   , 0.]),
          numpy.array([right, bottom, 0.]),
          numpy.array([left , bottom, 0.])]


# Projects 3d points moving further and further away from camera (in 32 steps).
# The movement follows a curved trajectory (fixed random translation and
# rotation.
def curved_motion(square):
  # random car motion (one step) (position direction close to z)
  car_translation = translation_matrix((uniform(.01, .01), uniform(.01, .01), uniform(-1.5, -.5)))
  # bit of car rotation (bit of y, even less x)
  car_rotation = euler_matrix(uniform(-.001,.001), uniform(-.01, .01), 0., 'rxyz')
  car_pose_delta = concatenate_matrices(car_rotation, car_translation)

  def project_point(pose, point):
    point_homogenious = [point[0], point[1], point[2], 1.]
    transformed_point_homogenious = numpy.dot(pose, point_homogenious)
    transformed_point = transformed_point_homogenious[0:3] / transformed_point_homogenious[3]
    projected_point = transformed_point[0:2] / numpy.linalg.norm(transformed_point)
    return projected_point

  car_pose_square = identity_matrix()
  for distance in range(0, 32):
    car_pose_square = concatenate_matrices(car_pose_delta, car_pose_square)
    yield [project_point(car_pose_square, point) for point in square]


def print_square(square):
  for point in square + [square[0]]:
    print(point[0], point[1])
  print()


#square = random_square_points_3d()
#for square_transformed in curved_motion(square):
#  print_square(square_transformed)
