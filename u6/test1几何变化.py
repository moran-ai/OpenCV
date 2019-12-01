# 放大缩小
import cv2 as cv
import numpy as np

img = cv.imread('test.png')
img2 = img[0:300,100:400]   # 指定区域
# img1 = cv.resize(img,None,fx=0.25,fy=0.25,interpolation=cv.INTER_CUBIC)
img3 = cv.resize(img2,None,fx=1.5,fy=1.5,interpolation=cv.INTER_CUBIC)
print(img.shape)
# print(img1.shape)

cv.imshow('img',img)
# cv.imshow('img1',img1)
cv.imshow('img3',img3)
cv.waitKey(0)

