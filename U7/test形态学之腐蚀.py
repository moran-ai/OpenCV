import cv2 as cv
import numpy as np
#
# img = cv.imread('j.png', 0)
# # OpenCV定义的结构元素
# kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
#
# # 腐蚀图像
# eroded = cv.erode(img, kernel)
# # 显示腐蚀后的图像
# # cv.imshow("Eroded Image", eroded)
#
# # 膨胀图像
# dilated = cv.dilate(img, kernel)
# # 显示膨胀后的图像
# # cv.imshow("Dilated Image", dilated)
# # 原图像
# # cv.imshow("Origin", img)
#
# # NumPy定义的结构元素
# NpKernel = np.uint8(np.ones((3, 3)))
# Nperoded = cv.erode(img, NpKernel)
# # 显示腐蚀后的图像
# # cv.imshow("Eroded by NumPy kernel", Nperoded)

# cv.waitKey(0)

# 直接读取灰度图
img = cv.imread('plate02.png',0)
img1 = cv.imread('j.png',0)

# 二值化
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret1,th2 = cv.threshold(img1,127,255,cv.THRESH_BINARY)
# 建立结构元，注意结构元不能出现0值,不建立默认为3*3
kernel = np.ones((3,3),np.float32)  # 结构元为5*5，津字看不到，腐蚀过度.

# 腐蚀操作，去掉白噪声,断连
eroison = cv.erode(th1,kernel,iterations=1)
# iterations=1 代表操作一次，操作次数默认为1

# # 膨胀操作
# dilated = cv.dilate(img1, kernel)
# cv.imshow('d',dilated)

# cv.imshow('img',img1)
cv.imshow('erode',eroison)
cv.waitKey(0)
cv.destroyAllWindows()
