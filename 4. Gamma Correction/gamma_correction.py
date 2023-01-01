import cv2
import numpy as np


img = cv2.imread('project_images/img_equ_opencv.png')


# 4th preprocessing : Gamma correction --------------------------
def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)

gammaImg = gammaCorrection(img, 2.2)
# ---------------------------------------------------------------

# cv2.imshow('Original image', img)
cv2.imshow('Gamma corrected image', gammaImg)
cv2.imwrite('project_images/img_equ_gamma_opencv.png',gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()