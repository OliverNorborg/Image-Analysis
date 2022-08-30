#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:45:14 2022

@author: olivernorborg
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 22:12:12 2022
@author: olivernorborg
"""

from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom

# Directory containing data and images
in_dir = "data/"
# X-ray image
im_name = "metacarpals.png"
# Read the image.
# Here the directory and the image name is concatenated
# by "+" to give the full path to the image.
im_org = io.imread(in_dir + im_name)


#Finding dimensions
print(im_org.shape)

#finding the type that the pixels are 
print(im_org.dtype)

io.imshow(im_org)
plt.title('Metacarpal image')
io.show()

# you can zoom in on specific pixels with
""" Add zooming of image Exercise 4 """


#adddign colour to the image 
io.imshow(im_org, cmap="jet") #can change the colour map here to cool, pink, jet etc...
plt.title('Metacarpal image (with colormap)')
io.show()

#Add a scaling in order to force the pixels into all black and all white
# Here the pixels with 20 and below will be displayed as black 
# and the pixels values 170 and above will be displayed as white
io.imshow(im_org, vmin=20, vmax=170)
plt.title('Metacarpal image (with gray level scaling)')
io.show()

""" Exercise 6 Automatically scale the visualization """
# The pixel with the lowest value in the image is shown as black and the 
# pixel with the highest value in the image is shown as white.
io.imshow(im_org, vmin=np.min(im_org), vmax=np.max(im_org))
plt.title('Metacarpal image (with gray level scaling)')
io.show()

""" Histogram - Exercise 7 """
plt.hist(im_org.ravel(), bins=256)
plt.title('Image histogram')
io.show()
h = plt.hist(im_org.ravel(), bins=256)

bin_no = 100
count = h[0][bin_no]
print(f"There are {count} pixel values in bin {bin_no}")

bin_left = h[1][bin_no]
bin_right = h[1][bin_no + 1]
print(f"Bin edges: {bin_left} to {bin_right}")



y, x, _ = plt.hist(im_org.ravel(), bins=256)

"""Exercise 8 - find the most common range of intensities"""
print("The x values that has the most amount of 'hits' is: ", np.argmax(y))
print("The amount of hits that the the ", np.argmax(y), " pixel has is: ", np.max(y))


"""Exercise 9 - Pixel value at specific row and coloum"""
r = 100
c = 50
im_val = im_org[r, c]
print(f"The pixel value at (r,c) = ({r}, {c}) is: {im_val}")
print(f"The pixel value at (r,c) = (110, 90) is: {im_org[110,90]}")

#Here to reset the image
io.imshow(im_org)
plt.title('Metacarpal image')
io.show()

"""Exercise 10 - what does the code below do?"""
im_org[:30] = 0
io.imshow(im_org)
io.show()
#This take the first 30 rows of pixels and sets them to black 

"""Exercise 11 - Mask """
# A mask is a binary image same size and the original where the values 
# are either 0 or 1. The values above 150 are set to black and below are white
mask = im_org > 150
io.imshow(mask)
io.show()

#What does this code do?
im_org[mask] = 255
io.imshow(im_org)
io.show()


"""Exercise 12 - RGB"""
img_ardeche = io.imread("data/ardeche.jpg")
io.imshow(img_ardeche)
plt.title('Ardeche image')
io.show()
print("Dimensions of Ardeche: ", img_ardeche.shape)
print("The type that the pixels are: ",img_ardeche.dtype)

print("The RBG vlaues og the pixel in position (110,90) is: ",img_ardeche[110,90])
r = 110
c = 90
img_ardeche[r, c] = [255, 0, 0]
rows = img_ardeche.shape[0]
r2 = int(rows/2)
img_ardeche[:r2] = [0,255,0]
io.imshow(img_ardeche)
io.show()
