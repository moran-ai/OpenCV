# coding:gbk
"""
函数：cv.HoughLines()
步骤：
1.对边缘图像进行霍夫空间变换
2.在4领域内找到霍夫空间变换的极大值
3.对这些极大值安装由大到小顺序进行排序，极大值越大，越有可能是直线
4.输出直线
 参数：
第一个参数图片为二值化图，或者进行边缘检测
第二三个参数分别代表精确度
第四个参数是阈值,不是二值化的阈值
Hough 直线变换原理
一条直线可以用数学表达式：y=mx+c

"""

import cv2 as cv
import numpy as np

# 读入图片
img = cv.imread('bmx.jpg')
# 高斯滤波
blur = cv.GaussianBlur(img,(5,5),-5,-5)
# 颜色转换
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 二值化
ret,g = cv.threshold(gray,180,255,cv.THRESH_BINARY)
# 边缘检测
edges = cv.Canny(g,120,200)

# 霍夫变换
lines = cv.HoughLines(edges,1,np.pi/180,130)
# print(lines)

# 循环
for line in lines:
    for rho,theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*(a))
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# cv.imshow('img',g)
# cv.imshow('img1',edges)
cv.imshow('lines',img)
cv.waitKey(0)
