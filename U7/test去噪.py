import cv2 as cv
import numpy as np

img = cv.imread('rt.jpg',0)
img1 = cv.imread('t.png',0)

ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)


# 大津算法 cv.THRESH_OTSU
# ret阈值,th2二值化
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# print(ret2)

# 降噪处理,高斯模糊函数
blur = cv.GaussianBlur(img,(5,5),0)
blur1 = cv.GaussianBlur(img1,(5,5),0)

ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# print(ret3)

ret4,th4 = cv.threshold(img1,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print(ret4)
# cv.imshow('blur',blur)
# cv.imshow('th1',th1)
# cv.imshow('th2',th2)
# cv.imshow('th3',th3)
# cv.imshow('th4',th4)
# cv.imshow('blur1',blur1)
cv.waitKey(0)
