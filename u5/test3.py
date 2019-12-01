# coding=gbk
import cv2 as cv
import numpy as np

image = cv.imread("dog1.jpg")
"""
图像image各像素加50
与image大小一样的矩阵
"""
M = np.ones(image.shape,dtype="uint8")*50
added = cv.add(image,M)             # 将图像image与M相减
subtracted = cv.subtract(image,M)   # 将图像image与M相减
multiply = cv.multiply(image,M)
divide = cv.divide(image,M)

cv.imshow("Original_img",image)     # 展示原图
cv.imshow("Added",added)            # 加运算图
cv.imshow("subtracted",subtracted)  # 减运算图
cv.imshow('multiply',multiply)      # 乘
cv.imshow('divide',divide)          # 除
cv.waitKey(0)
cv.destroyAllWindows()
