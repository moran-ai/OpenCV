import cv2 as cv
import numpy as np

img = cv.imread('test.png',0)
img1 = cv.imread('dog2.jpg',0)


# 二值化函数threshold
# ret 阈值, th1二值化结果
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret1,th4 = cv.threshold(img1,127,255,cv.THRESH_BINARY)


# 自适应函数adaptiveThreshold
th2 = cv.adaptiveThreshold(th1,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,10)
th3 = cv.adaptiveThreshold(th1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,10)
#
# th5 = cv.adaptiveThreshold(th4,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,0)
# th6 = cv.adaptiveThreshold(th4,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,0)



# cv.imshow('th1',th1)
# cv.imshow('img',img)
# cv.imshow('th2',th2)
# cv.imshow('th3',th3)
# cv.imshow('img1',img1)
# cv.imshow('th5',th5)
# cv.imshow('th6',th6)
cv.waitKey(0)