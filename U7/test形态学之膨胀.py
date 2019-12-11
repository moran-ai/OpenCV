import cv2 as cv
import numpy as np

img = cv.imread('j.png',0)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
kernel = np.ones((3,3),np.float32) # 内核

# 腐蚀操作
dilated = cv.dilate(img, kernel,iterations=1)

# eroison = cv.erode(img,kernel,iterations=1)
# c = dilated- eroison

# cv.imshow('img',img)
cv.imshow('c',dilated)
cv.waitKey(0)
cv.destroyAllWindows()
