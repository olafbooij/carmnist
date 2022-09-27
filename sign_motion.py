def straight_motion(distance):
  def perspective(coordinate, distance):
    focal_length = 1
    return coordinate * focal_length / distance

  left, top, right, bottom = (-1., -1., 1., 1.)
  horizontal_shift = -5
  vertical_shift = 2
  left += horizontal_shift
  right += horizontal_shift
  top += vertical_shift
  bottom += vertical_shift
  
  return tuple([perspective(i, distance) for i in [left, top, right, bottom]])


def print_bounding_box(bounding_box):
  left, top, right, bottom = bounding_box
  print(left, top)
  print(right, top)
  print(right, bottom)
  print(left, bottom)
  print(left, top)
  print()

print_bounding_box(straight_motion(50))
print_bounding_box(straight_motion(40))
print_bounding_box(straight_motion(30))
print_bounding_box(straight_motion(20))
print_bounding_box(straight_motion(10))
