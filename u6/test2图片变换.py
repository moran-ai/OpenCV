import cv2 as cv
import numpy as np

img = cv.imread('test.png')
img1 = cv.imread('img.jpg')
# print(img.shape)
rows,cols = img.shape[:2]  # 原图的高宽
# M = np.float32([[1,0,100],[0,1,50]])    # x平移100和y平移50
# M1 = np.float32([[1,0,-100],[0,1,-50]])    # 左上角移动
# dst=cv.warpAffine(img,M,(rows,cols))
# dst1=cv.warpAffine(img,M1,(rows,cols))
# cv.imshow('r1',dst)
# cv.imshow('r2',dst1)

#先缩小0.25倍，再平移
# M2 = np.float32([[0.25,0,3*rows/8],[0,0.25,3*cols/8]])  # 移动至中心
# dst2=cv.warpAffine(img1,M2,(rows,cols),borderValue=(255,44,138))

# 旋转
M3 = cv.getRotationMatrix2D((rows/2,cols/2),120,0.6)  # 1代表缩放比率，1不改变,30度
dst3 = cv.warpAffine(img,M3,(rows,cols))
dst4 = cv.rotate(dst3,cv.ROTATE_90_CLOCKWISE)   # 单独旋转函数rotate
dst5 = cv.rotate(dst3,cv.ROTATE_90_COUNTERCLOCKWISE)

# cv.imshow('M2',dst2)
cv.imshow('M3',dst4)
cv.imshow('2',dst5)
cv.waitKey(0)
