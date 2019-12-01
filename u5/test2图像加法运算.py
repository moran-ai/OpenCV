import cv2 as cv
import numpy as np

m = cv.imread('meixi.jpg')
o = cv.imread('opencv.png')
# print(m.shape)
# print(o.shape)

h,w = o.shape[:2]  # 拿出前两行
# print(h,w)
roi = m[:h,:w] # 感兴趣的区域
# cv.imshow('r1',roi)
# a = cv.add(roi,o)
# cv.imshow('r2',a)

B = cv.cvtColor(o,cv.COLOR_BGR2GRAY)# 转化为灰度图
# cv.imshow('r3',B)
ret,mask = cv.threshold(B,200,255,cv.THRESH_BINARY)  # 阈值处理
C=cv.bitwise_not(mask)  # mask取反
# cv.imshow('r5',C)
img_b1 = cv.bitwise_and(roi,roi,mask=mask) # 掩模
# roi中非零的地方会保留
# cv.imshow('img_b1',img_b1)
img_fg = cv.bitwise_and(o,o,mask=C) # 掩模取反
# cv.imshow('img_fg',img_fg)
dst = cv.add(img_b1,img_fg)  # 叠加
# cv.imshow('a',dst)
m[:h,:w] = dst # 还原
cv.imshow('1',m)
cv.imshow('r',dst)
cv.waitKey(0)
