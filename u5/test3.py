# coding=gbk
import cv2 as cv
import numpy as np

image = cv.imread("dog1.jpg")
"""
ͼ��image�����ؼ�50
��image��Сһ���ľ���
"""
M = np.ones(image.shape,dtype="uint8")*50
added = cv.add(image,M)             # ��ͼ��image��M���
subtracted = cv.subtract(image,M)   # ��ͼ��image��M���
multiply = cv.multiply(image,M)
divide = cv.divide(image,M)

cv.imshow("Original_img",image)     # չʾԭͼ
cv.imshow("Added",added)            # ������ͼ
cv.imshow("subtracted",subtracted)  # ������ͼ
cv.imshow('multiply',multiply)      # ��
cv.imshow('divide',divide)          # ��
cv.waitKey(0)
cv.destroyAllWindows()
