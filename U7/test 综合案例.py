# coding=gbk
import cv2 as cv
import numpy as np
img = cv.imread('color.jpg')

# ��RGBתΪHSV������ɫ��ȡ
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# ������ɫ��ֵ
lower_green = np.array([35,43,46])
upper_green = np.array([60,255,255])

# ��ȡ��ɫ
green = cv.inRange(hsv,lower_green,upper_green)

#�˲�
median = cv.medianBlur(green, 5)
cv.imshow('green',median)

# �������ε��ں�
rectKernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))

# ������
green = cv.morphologyEx(green,cv.MORPH_CLOSE,rectKernel)
cv.imshow('close',green)

# ������
green = cv.morphologyEx(green,cv.MORPH_OPEN,rectKernel)
cv.imshow('open',green)

cv.waitKey(0)
cv.destroyAllWindows()
