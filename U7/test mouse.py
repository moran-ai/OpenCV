# coding=gbk
import cv2 as cv
import numpy as np

img = cv.imread('./IMG/mouse.jpg')

# ��ֵģ��
blur = cv.blur(img,(5,5))

# ��ֵ�˲�
median = cv.medianBlur(img,(5))

# ��˹ģ��
gblur = cv.GaussianBlur(img,(5,5),0)

# ˫���˲�
bfilter = cv.bilateralFilter(img,-1,60,70)   # -1��ʾ���,60��ʾ��ɫ��Χ

cv.imshow('img',img)
cv.imshow('blur',blur)
cv.imshow('median',median)
cv.imshow('gblur',gblur)
cv.imshow('bfilter',bfilter)
cv.waitKey(0)

