# coding:gbk

# ���Һ���
# cv.findContours()

#  ����������
# cv.drawContours()

import cv2 as cv
img = cv.imread('7.jpg')
# תΪ�Ҷ�ͼ
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# ���ж�ֵ������
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# ���ص�����ֵ
# �������
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(contours)
# print(hierarchy)

cv.drawContours(img, contours, -1, (0, 0, 255),3)

cv.imshow("img", img)
cv.imshow('binary',binary)
cv.waitKey(0)
