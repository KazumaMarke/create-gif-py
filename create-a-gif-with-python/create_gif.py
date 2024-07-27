# imageio library version 3
# Imageio is a Python library that provides an easy interface to read and write a wide range of image data.
import imageio.v3 as iio

filenames = ['badge_earth.png', 'badge_fork.png', 'badge_loop.png', 'badge_modules.png'] #  You can insert more than two PNG image files in the filenames list. Make sure that the pixel of pictures you will use are all same sizes.
images = [ ] # 'images' The list containing the image data.

for filename in filenames:
  images.append(iio.imread(filename))

# 'guitar.gif' This is the name you want to give to your new GIF file
# 'duration = 500'  How long each picture should show in the GIF, in milliseconds.
# 'loop = 0' How many times the GIF should repeat (0 means it keeps looping forever).
#  The '.imwrite()' method to turn the images into a GIF
  iio.imwrite('badge-icon.gif', images, duration = 500, loop = 0) 
