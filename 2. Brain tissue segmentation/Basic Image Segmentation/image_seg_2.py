''''
    1. Input image
    2. Convert image to grayscale (it is already)
    3. Convert image to binary image by tresholding
    4. Find the number of connected objects
    5. Find mask by assigning 1 to inside and 0 to outside of the object that show brain region
    6. Multiply the mask with T1, T2 and FLAIR MR images to get their skull-stripped MR image
'''

import matplotlib.pyplot as plt
import cv2
import skimage

im = cv2.imread('MRI_Brain_Image_Example.jpg')
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# plot histogram with 255 bins
b, bins, patches = plt.hist(vals, 255)
plt.xlim([0,255])
plt.show()


# convert the image to grayscale
gray_image = skimage.color.rgb2gray(im)
# blur the image to denoise
blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)
fig, ax = plt.subplots()
plt.imshow(blurred_image, cmap="gray")
plt.show()

# create a mask based on the threshold

# perform automatic thresholding with 
t = skimage.filters.threshold_otsu(blurred_image) - 0.02
print("Found automatic threshold t = {}.".format(t))

binary_mask = blurred_image > t

fig, ax = plt.subplots()
plt.imshow(binary_mask, cmap="gray")
plt.show()


# apply the binary mask to select the foreground
selection = im.copy()
selection[~binary_mask] = 0

fig, ax = plt.subplots()
plt.imshow(selection)
plt.show()