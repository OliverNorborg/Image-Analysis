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

"""
Missing Exercies 
Exercise 22 - Colour bones Blue
Exercise 23 - Understanding 

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


"""Exercise 13 - resclae and resize image"""

img = io.imread("data/Lena.png")
io.imshow(img)
plt.title('Lena')
io.show()
print("Dimensions of the original Lena is: ", img.shape)
print("The type that the pixels are: for the original image is: ",img.dtype)
#Rescale the image
image_rescaled = rescale(img, 0.25, anti_aliasing=True,channel_axis=2)
io.imshow(image_rescaled)
plt.title('Rescaled Lena')
io.show()
print("Dimensions of the rescaled Lena is: ", image_rescaled.shape)
print("The type that the pixels are for the rescaled image is: ",image_rescaled.dtype)
#resize the image
image_resized = resize(img, (img.shape[0] // 4, img.shape[1] // 6),anti_aliasing=True)
io.imshow(image_resized)
plt.title('Resized Lena')
io.show()

"""Exercise 15 - rescale image so width is always 400 """
scale = 400/img.shape[1]
image_rescaled_400 = rescale(img, scale, anti_aliasing=True,channel_axis=2)
io.imshow(image_rescaled_400)
plt.title('Rescaled Lena 400 width')
io.show()


"""Exercise 16 - transform into grey level image"""
im_gray = color.rgb2gray(img)
im_byte = img_as_ubyte(im_gray)
io.imshow(im_byte)
plt.title('Grey Lena')
io.show()

"""Exercise 17 - Histogram of Lena"""
plt.hist(img.ravel(), bins=256)
plt.title('Image histogram')
io.show()
#h = plt.hist(img.ravel(), bins=256)



"""Exercise 19 - DTU Sign - RGB"""
im_org = io.imread("data/DTUSign1.jpg")
io.imshow(im_org)
plt.title('DTU sign image')
io.show()


r_comp = im_org[:, :, 0]
g_comp = im_org[:, :, 1]
b_comp = im_org[:, :, 2]
#Display the red component
io.imshow(r_comp)
plt.title('DTU sign image (Red)')
io.show()
#Display the green component
io.imshow(g_comp)
plt.title('DTU sign image (Green)')
io.show()
#Display the blue component 
io.imshow(b_comp)
plt.title('DTU sign image (Blue)')
io.show()

"""Exercise 20 - black rectange (NumPy slicing)"""

black_square = im_org
black_square[500:1000, 800:1500, :] = 0
io.imshow(black_square)
plt.title('DTU sign with a black square')
io.show()

#Save the photo using io.imsave


"""Exercise 21 - Create blue rectangle """
blue_square = im_org
blue_square[1550:1750, 2300:2800, 0:2] = 0
io.imshow(blue_square)
plt.title('DTU sign with a blue square')
io.show()

"""Exercise 22 - colour the bones blue"""
img_bones = io.imread("data/metacarpals.png")
io.imshow(img_bones)
plt.title('X-ray original')
io.show()

bones_gray = color.gray2rgb(img_bones)
im_byte = img_as_ubyte(bones_gray)
io.imshow(bones_gray)
plt.title('Bones grey')
io.show()
print(bones_gray.shape)


"""Exercise 23 - """

p = profile_line(img_bones, (342, 77), (320, 160))
plt.plot(p)
plt.ylabel('Intensity')
plt.xlabel('Distance along line')
plt.show()

"""Exercise 24 - 3D white line intensity"""

in_dir = "data/"
im_name = "road.png"
im_org = io.imread(in_dir + im_name)
im_gray = color.rgb2gray(im_org)
ll = 200
im_crop = im_gray[40:40 + ll, 150:150 + ll]
xx, yy = np.mgrid[0:im_crop.shape[0], 0:im_crop.shape[1]]
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(xx, yy, im_crop, rstride=1, cstride=1, cmap=plt.cm.jet,
linewidth=0)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

"""Exercise 25 - DICOM"""
in_dir = "data/"
im_name = "1-442.dcm"
ds = dicom.dcmread(in_dir + im_name)
print(ds)
directory = ds.dir()

#Exercise 26- Type and shape
im = ds.pixel_array
print("Image shape: ", im.shape)
print("Image type: ", im.dtype)

#Visualize the slice
io.imshow(im, vmin=-1000, vmax=1000, cmap='gray')
io.show()



















