# coding:gbk
import cv2 as cv
import numpy as np

# 黑色背景
x = np.zeros((512,512,3),dtype=np.uint8)

# img = x[100:300,100:300]

# 进行颜色修改
# img[0,0] = (255,255,255)

x[100:300,100:300,:3] = 255

# 画线
x[100:300,400:401,:3] = 255
# cv.line(x,(0,0),(8,350),(255,255,255),2)

# 转化为黑白图
gray = cv.cvtColor(x,cv.COLOR_BGR2GRAY)

# 阈值处理
ret,img = cv.threshold(gray,200,255,cv.THRESH_BINARY_INV)

# 查找轮廓
contours,h = cv.findContours(img,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

# print(contours[0])
# print(h)
# print(len(contours))

cv.drawContours(img,contours,-1,(0,0,255),1,8,h)
# cv.circle(img,(93,93),10,(45,255,238),2)
# cv.circle(img,(90,300),10,(45,255,238),2)
# cv.circle(img,(400,306),10,(39,242,255),2)
# cv.circle(img,(100,306),10,(39,243,255),2)
cv.circle(img,tuple(contours[0][0][0]),3,(255,0,0),2)
cv.circle(img,tuple(contours[0][1][0]),3,(255,0,0),2)
cv.circle(img,tuple(contours[1][0][0]),3,(255,0,0),2)
cv.circle(img,tuple(contours[1][1][0]),3,(255,0,0),2)
cv.circle(img,tuple(contours[1][2][0]),3,(255,0,0),2)
cv.circle(img,tuple(contours[1][4][0]),3,(255,0,0),2)
# cv.circle(img,tuple(contours[0]),3,(0,255,0),2)

cv.imshow('img',img)

# cv.imshow('img',x)
cv.waitKey(0)

