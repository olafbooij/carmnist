from random import uniform
from transformations import identity_matrix, euler_matrix, concatenate_matrices, translation_matrix, scale_matrix
import numpy


# Create trajectory of transformations moving further and further away from the
# camera. The movement follows a curved path (with fixed random translation and
# rotation). These transformations are expressed as 4x4 transformation
# matrices.
def curved_motion(nr_of_steps):
  # random camera motion (one step) (position direction close to z)
  cam_translation = translation_matrix((uniform(-.05, .05), uniform(-.05, .05), uniform(.2, 1.0)))
  # bit of camera rotation (bit of y, even less x)
  cam_rotation = euler_matrix(uniform(-.002,.002), uniform(-.03, .03), 0., 'rxyz')
  cam_trans_delta = concatenate_matrices(cam_rotation, cam_translation)
  # begin with a first step of cam_trans_delta, and then iteratively add
  # another step.
  cam_trans_square = identity_matrix()
  for distance in range(0, nr_of_steps):
    cam_trans_square = concatenate_matrices(cam_trans_delta, cam_trans_square)
    yield cam_trans_square


# Use this trajectory to create homographies, expressing an input image in the
# output image at the end of the trajectory.
def curved_motion_homography(input_image_size, output_image_size):
  # Define camera calibration K_in for the input image given an image center
  # a focal length f_in, based on the size of the image input.
  f_in = input_image_size[0]
  K_in_inv = numpy.array([[ 1. / f_in, 0.       , -.5 ],
                          [ 0.       , 1. / f_in, -.5 ],
                          [ 0.       , 0.       , 1.  ]])
  # Define camera calibration K_out for the output image given an image center
  # c_out and focal length f_out, both based on the size of hte output image.
  c_out = output_image_size[0]//2
  f_out = output_image_size[0]
  K_out = numpy.array([[f_out, 0.   , c_out],
                       [0.   , f_out, c_out],
                       [0.   , 0.   , 1.   ]]);
  # Define position of input image relative to the start of the trajectory
  start_trans_in_image = translation_matrix((uniform(-1., 1.), uniform(-1., 1.), 0))
  for transformation in curved_motion(32):
    # Concatenate the start with the transformation of the trajectory
    homography = concatenate_matrices(transformation, start_trans_in_image)
    # From the 4x4 transformation matrix create a 3x3 "Homography matrix". This
    # requires some "magic": adding the 4rd column (translation) to the 3rd
    # column (z-axis rotation), and keep only upper-left 3x3 part.
    homography[:,2] += homography[:,3]
    homography = homography[0:3, 0:3]
    # Apply th camera calibrations
    homography = numpy.dot(homography, K_in_inv)
    homography = numpy.dot(K_out, homography)
    yield homography

