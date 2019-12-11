# coding:gbk
import cv2 as cv

img = cv.imread('o.jpg')

# 图片缩小
# cv.resize(img,None,fx=2,fy=10,interpolation=1)
# 颜色转换
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 二值化
ret,dst = cv.threshold(gray,90,255,cv.THRESH_BINARY_INV)

# 查找轮廓
# c代表所有的轮廓，h表示轮廓的层次信息
# contours, hierarchy=cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]])
c,h = cv.findContours(dst,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

# 画轮廓
# cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[
"""
image：目标输出图像 
contours：所有的轮廓，可直接传入findContours函数中的contours参数 
contourIdx：轮廓的索引，即绘制哪个轮廓，若为负值则绘制所有轮廓 
color：绘制的颜色，元祖形式，如（255）或（255, 255, 255） 
thickness：绘制的轮廓的线条粗细程度，若为负数，表示要填充整个轮廓

"""

cv.drawContours(img,c,-1,(0,255,0),2,8,h)

c0=c[0]
m = cv.moments(c0)
cx = int(m['m10']/m['m00'])
cy = int(m['m01']/m['m00'])

# print(m)
# cv.circle(img,(cx,cy),5,(0,0,255),1)

cv.imshow('img1',dst)
# cv.imshow('img',img)

cv.waitKey(0)
