# coding=gbk
import cv2 as cv
import numpy as np

img = cv.imread('./IMG/mouse.jpg')

# 均值模糊
blur = cv.blur(img,(5,5))

# 中值滤波
median = cv.medianBlur(img,(5))

# 高斯模糊
gblur = cv.GaussianBlur(img,(5,5),0)

# 双边滤波
bfilter = cv.bilateralFilter(img,-1,60,70)   # -1表示深度,60表示颜色范围

cv.imshow('img',img)
cv.imshow('blur',blur)
cv.imshow('median',median)
cv.imshow('gblur',gblur)
cv.imshow('bfilter',bfilter)
cv.waitKey(0)

