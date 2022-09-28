from random import uniform
from transformations import *   # TODO specialize

def random_sign():
  left, top, right, bottom = (-.3, -.3, .3, .3)  # 60 cm square sign
  horizontal_shift = uniform(-2., 2.)
  vertical_shift = uniform(0., 3.)
  left += horizontal_shift
  right += horizontal_shift
  top += vertical_shift
  bottom += vertical_shift
  return((left, top, right, bottom))


def straight_motion(distance, sign):
  def perspective(coordinate, distance):
    focal_length = 1
    return coordinate * focal_length / distance

  return tuple([perspective(i, distance) for i in sign])


def print_bounding_box(bounding_box):
  left, top, right, bottom = bounding_box
  print(left, top)
  print(right, top)
  print(right, bottom)
  print(left, bottom)
  print(left, top)
  print()

#sign = random_sign()
#for distance in range(60, 0, -1):
#  print_bounding_box(straight_motion(distance/10, sign))


#def interpolate_pose(motion, time)
#  return motion * time

#exp(interpolate_pose(motion, time)

#-> perhaps just bounding_box coordinates
#-> check what the input for interpolation function is
#-> check geometry library (need: 3d pose interpolation and point transformation),  let's hope this is not just numpy ....
#https://motion.cs.illinois.edu/software/klampt/latest/pyklampt_docs/Manual-Math.html
#smaller:
#https://github.com/ccorcos/se3
#https://raw.githubusercontent.com/ros/geometry/indigo-devel/tf/src/tf/transformations.py

def curved_motion(sign):
  # random car motion (one step) (position direction close to z)
  car_translation = translation_matrix((.001, .0001, -1))
  # bit of car rotation (bit of y, even less x)
  car_rotation = euler_matrix(.00001, .0001, 0.000001, 'rxyz')
  car_pose_delta = concatenate_matrices(car_rotation, car_translation)

  #camera_rotation_car = euler_matrix(-.1, .0001, 0.000001, 'rxyz')
  #camera_pose_car = camera_rotation_car  # later add projection

  def transform_point(pose, point):
    transformed_point = numpy.dot(pose, [point[0], point[1], point[2], 1.])
    return transformed_point[0:3] / transformed_point[3]

  current_car_pose = identity_matrix()
  for distance in range(0, 100):
    current_car_pose = concatenate_matrices(car_pose_delta, current_car_pose)
    yield [transform_point(current_car_pose, point) for point in sign]


def random_sign_points():
  left, top, right, bottom = random_sign()
  return [numpy.array([left , top   , 1.]),
          numpy.array([right, top   , 1.]),
          numpy.array([right, bottom, 1.]),
          numpy.array([left , bottom, 1.])]


sign = random_sign_points()
for sign_transformed in curved_motion(sign):
  print(sign_transformed[0][0], sign_transformed[0][1], sign_transformed[0][2])

# sign is car position at time 32
# or take the inverse and get it at time 0...
# tranform sign border points in camera for time 0-32
