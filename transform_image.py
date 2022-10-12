from PIL import Image
import numpy
from transformations import euler_matrix, concatenate_matrices, translation_matrix

img_in = Image.open("test_x_images/1.png")

# Create a "pose" (translation and rotation) of the image-plane relative
# to the camera expressed as a 4x4 transformation matrix.
pose = concatenate_matrices(translation_matrix((0, 10, 30)),
                            euler_matrix(0., 2.8, 0.2, 'rxyz'),
                            translation_matrix((-14, -14, 0)))

# From this transformation matrix create a 3x3 "Homography matrix". This
# requires some "magic": adding the 4rd column (translation) to the 3rd
# column (z-axis rotation), and keep only upper-left 3x3 part.
pose[:,2] += pose[:,3] 
pose = pose[0:3, 0:3]

# To compose a new image, we create a camera calibration matrix K given
# the image center (c_x, cy) and focal length f.
imsize = (100, 100)
cx = imsize[0]//2
cy = imsize[1]//2
f = 30
K = numpy.array([[f, 0, cx],
                 [0, f, cy],
                 [0, 0,  1]]);
pose = numpy.dot(K, pose)

# The call to transform, actually requires the transformation of the
# output image pixels to the input image pixels. This is the inverse of
# the pose we created:
invpose = numpy.linalg.inv(pose)
invpose /= invpose[2,2] 

# Image.transform will apply the perspective transformation of the image
img_out = img_in.transform(imsize, Image.Transform.PERSPECTIVE, invpose.flatten()[:8])
img_out.save("transformed.png")



# The 3x3 matrix "pose" transforms points from the input image space to the
# output image space. Below we transform a square (borders of the input
# image) to pixel locations of the output image.
points = [numpy.array([0, 0]),
          numpy.array([0, 28]),
          numpy.array([28, 28]),
          numpy.array([28, 0]),
          numpy.array([0, 0]),
         ]
def project_point(pose, point):
  point_homogenious = [point[0], point[1], 1.]
  transformed_point_homogenious = numpy.dot(pose, point_homogenious)
  transformed_point = transformed_point_homogenious[0:2] / transformed_point_homogenious[2]
  return transformed_point

transed = [project_point(pose, point) for point in points]
  
for point in transed:
  print(point[0], point[1]) 
