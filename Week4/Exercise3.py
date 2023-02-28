#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:39:42 2022

@author: olivernorborg
"""

from skimage import io
from skimage.util import img_as_float, img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np

# Exercise 1

im_org = io.imread("data/vertebra.png")
io.imshow(im_org)
plt.title('Vertebra image')
io.show()

plt.hist(im_org.ravel(), bins=256)
plt.title('Image histogram')
io.show()

# The histogram is (not) a bimodal histogram

# %%%%%%%%%%%%%%%%%%%%%%
#Exercise 2
max_org = np.max(im_org)
min_org = np.min(im_org)
print("Max Value:",np.max(im_org))
print("Min Value:",np.min(im_org),'\n')
# the full scale of gray is not being used the min value is no 0 
# and the max is 255. 
# %%%%%%%%%%%%%%%%%%%%%%
#Exercise 3

img_float = img_as_float(im_org)
print("Original max values divided by 255:", max_org/255)
print("Max Value:",np.max(img_float))
print("Original min values divided by 255:", min_org/255)
print("Min Value:",np.min(img_float),'\n')

# %%%%%%%%%%%%%%%%%%%%%%
#Exercise 4
img_ubyte = img_as_ubyte(img_float)
print("Max Value:",np.max(img_ubyte))
print("Min Value:",np.min(img_ubyte),'\n')

# %%%%%%%%%%%%%%%%%%%%%%
#Exercise 5

def histogram_stretch(img_in):
    """
    Stretches the histogram of an image 
    :param img_in: Input image
    :return: Image, where the histogram is stretched so the min values is 0 and the maximum value 255
    """
    # img_as_float will divide all pixel values with 255.0
    img_float = img_as_float(img_in)
    min_val = img_float.min()
    max_val = img_float.max()
    min_desired = 0.0
    max_desired = 1.0
	
    # Do something here

    # img_as_ubyte will multiply all pixel values with 255.0 before converting to unsigned byte
    return img_as_ubyte(img_out)





















