#coding=gbk
import cv2 as cv
import numpy as np

def nothing(x):
    pass

img = cv.imread('plate02.png')

cv.namedWindow('windows', 0)
cv.createTrackbar('d','windows',49,100,nothing)
cv.createTrackbar('sigmaSpace','windows',80,150,nothing)
cv.createTrackbar('sigmaColor','windows',80,150,nothing)
font = cv.FONT_HERSHEY_SIMPLEX

# 用while循环取值
while True:
    # resize参数
    # src	（必需）原图像
    # dsize	（必需）输出图像所需大小
    # fx	（可选）沿水平轴的比例因子
    # fy	（可选）沿垂直轴的比例因子
    # interpolation（可选)插值方式
    frame = cv.resize(img, None, fx=.5, fy=.5, interpolation=cv.INTER_LINEAR)
    d = cv.getTrackbarPos('d', 'windows')
    sigmaColor = cv.getTrackbarPos('sigmaColor', 'windows')
    sigmaSpace = cv.getTrackbarPos('sigmaSpace', 'windows')

    # kernel为正奇数
    d = d if d % 2 == 1 else d + 1

    # 2D卷积运算
    kernel = np.ones((d, d), np.float32) / (d *d)
    filter2D = cv.filter2D(frame, -1, kernel)
    filter2D = cv.putText(filter2D, "filter2D", (20, 20), font, .65, (255, 255, 255), 2)
    # 双边滤波
    bfilter = cv.bilateralFilter(frame, d,  sigmaColor, sigmaSpace)
    bfilter = cv.putText(bfilter, 'bfilter',  (20, 20), font, .65, (255, 255, 255), 2)
    # putText各参数依次是：图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细

    cv.imshow('windows', bfilter)
    k = cv.waitKey(24) & 0xFF
    if chr(k) == 'q':
        break
