import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('MRI_Brain_Image_Example.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imwrite('project_images/img_equ_opencv.png',res)

'''
# Check the Histograms
im = cv2.imread('MRI_Brain_Image_Example.jpg')
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# plot histogram with 255 bins
b, bins, patches = plt.hist(vals, 255)
plt.xlim([0,255])
plt.savefig('project_images/im_histogram.png')
plt.show()

vals = equ.mean(axis=1).flatten()
# plot histogram with 255 bins
b, bins, patches = plt.hist(vals, 255)
plt.xlim([0,255])
plt.savefig('project_images/equ_histogram.png')

im = cv2.imread('project_images/im_histogram.png')
equ = cv2.imread('project_images/equ_histogram.png')
res = np.hstack((im,equ))
cv2.imwrite('project_images/img_equ_opencv_hist.png',res)
'''