# coding:gbk
import cv2 as cv
import numpy as np

"""
边界矩形的面积,使用函数cv.boundingRect()
(x,y)为矩形的左上角的坐标
(w,h)是矩形的宽和高
x,y,w,h = cv.boundingRect(cnt)
画矩形
cv.rectangle()
"""
'''
# 读入图片
img = cv.imread('o.jpg')
# 转为黑白图
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 二值化
ret,dst = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
# 查找轮廓
c,h1 = cv.findContours(dst, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# c = c[0]
# 绘制 旋转 矩形
rect = cv.minAreaRect(c[1])
# print(rect)
box = cv.boxPoints(rect)
box = np.int0(box)
# 画轮廓
img1 = cv.drawContours(img, [box], 0, (0,0,255), 1)
# cv.drawContours(img, c, 0, (255,0,0), 2, 8, h1)

x, y, w, h = cv.boundingRect(c[1])

# 绘制矩形
cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0))

# 绘制最小外接矩形
points = c[1]
(x,y), raidus = cv.minEnclosingCircle(points)
center = (int(x), int(y))
raidus = int(raidus)
cv.circle(img, center, raidus, (255,0,0))

# 画凸线
hull = cv.convexHull(c[0])
cv.drawContours(img,[hull],0,(0,255,0),2,cv.LINE_AA)

cv.imshow('img',img)
cv.imshow('img1',gray)
cv.waitKey(0)
'''

img = cv.imread('o.jpg')
# imgs = cv.resize(img,(300,300),fx=1.5,fy=1.5)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret,dst = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)

c,h1 = cv.findContours(dst, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# 绘制 旋转 矩形
rect = cv.minAreaRect(c[1])
box = cv.boxPoints(rect)
box = np.int0(box)

img1 = cv.drawContours(img, [box], 0, (0,0,255), 1)
# cv.drawContours(img, c, 0, (255,0,0), 2, 8, h)

x, y, w, h = cv.boundingRect(c[1])

# 绘制矩形cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0))

# 绘制最小外接圆
points = c[1]
(x,y), raidus = cv.minEnclosingCircle(points)
center = (int(x), int(y))
raidus = int(raidus)
# cv.circle(img, center, raidus, (255,0,0))

hull = cv.convexHull(points)
cv.drawContours(img,[hull],0,(0,0,255),2,cv.LINE_AA)

cv.imshow('img',img)
cv.waitKey(0)
