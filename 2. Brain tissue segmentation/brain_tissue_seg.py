''''
    0. Input image
    1. Convert image to grayscale (it is already), & blur the image to denoise
    2. Convert image to binary image by tresholding
    3. Find contours of all the objects on the image
    4. Find the longest contour, cuz it will always represent the brain contour
    5. Create the brain mask depending on brain contour
    6. Apply the brain mask on the original image to extract brain from it

    And that's how brain extraction is performed
'''

import matplotlib.pyplot as plt
import cv2
import numpy as np
import skimage

# return the index of the longest list in a nested list
def longest(lst):
   longestList = max(lst, key = lambda i: len(i))
   ind = lst.index(longestList)
   return ind


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

# create a mask based on the threshold by performing automatic thresholding with 
t = skimage.filters.threshold_otsu(blurred_image) - 0.01 # print("Found automatic threshold t = {}.".format(t))
binary_mask = blurred_image > t
fig, ax = plt.subplots()
plt.imshow(binary_mask, cmap="gray")
plt.show()

# Find contours at a constant value of 0 = Black
contours = skimage.measure.find_contours(binary_mask, 0)
fig, ax = plt.subplots()
plt.imshow(binary_mask, cmap=plt.cm.gray)
for i in range(25) :
    plt.plot(contours[i][:, 1], contours[i][:, 0], linewidth=2)
plt.show()
# Longest contour = brain contour
index_brain_contour = longest(contours)
fig, ax = plt.subplots()
plt.imshow(binary_mask, cmap=plt.cm.gray)
plt.plot(contours[index_brain_contour][:, 1], contours[index_brain_contour][:, 0], linewidth=2)
plt.show()

# Create the brain mask depending on brain contour
brain_mask = np.full((256, 256), False)
contour = contours[index_brain_contour].astype(int)

'''
    IF x < 128 AND y < 128 THEN -> Take every point from selection where x' > x and y' > y
    IF x < 128 AND y > 128 THEN -> Take every point from selection where x' > x and y' < y
    IF x > 128 AND y < 128 THEN -> Take every point from selection where x' < x and y' > y
    IF x > 128 AND y > 128 THEN -> Take every point from selection where x' < x and y' < y
'''

for x in contour:
    if x[0] < 128 and x[1] < 128 :
        for y in brain_mask[x[0]:128]:
            y[x[1]:128] = [True for c in y[x[1]:128]]
    elif x[0] > 128 and x[1] < 128 :
        for y in brain_mask[128:x[0]]:
            y[x[1]:128] = [True for c in y[x[1]:128]]
    elif x[0] < 128 and x[1] > 128 :
        for y in brain_mask[x[0]:128]:
            y[128:x[1]] = [True for c in y[128:x[1]]]
    elif x[0] > 128 and x[1] > 128 :
        for y in brain_mask[128:x[0]]:
            y[128:x[1]] = [True for c in y[128:x[1]]]

# print(brain_mask)
fig, ax = plt.subplots()
plt.imshow(brain_mask, cmap=plt.cm.gray)
# plt.plot(contours[index_brain_contour][:, 1], contours[index_brain_contour][:, 0], linewidth=2)
plt.show()

# apply the brain mask to select the brain
selection = im.copy()
selection[~brain_mask] = 0

cv2.imwrite('project_images/segmented_image.png',selection)

fig, ax = plt.subplots()
plt.imshow(selection)
plt.show()