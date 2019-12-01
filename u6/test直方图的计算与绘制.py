import numpy as np
import cv2 as cv

x = cv.imread('img.jpg')

y = np.bincount(x,None,0)
# print(y)

