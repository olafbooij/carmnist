from random import uniform

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

sign = random_sign()
for distance in range(60, 0, -1):
  print_bounding_box(straight_motion(distance/10, sign))
