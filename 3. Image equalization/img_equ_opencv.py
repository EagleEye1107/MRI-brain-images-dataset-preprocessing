import cv2
import numpy as np

img = cv2.imread('MRI_Brain_Image_Example.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imwrite('res.png',res)