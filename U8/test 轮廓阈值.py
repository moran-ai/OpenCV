# coding:gbk
# import cv2 as cv
#
# # ��ȡͼƬ
# img = cv.imread('02.png')
#
# #  ��ɫת��
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
# #  ��ֵ����
# ret,s= cv.threshold(gray,200,255,cv.THRESH_BINARY_INV)
#
# # # ƽ��
# # img2 =cv.blur(s,(3,3))
#
# # ��������
# """
# ÿһ���������а���һЩ��Ϣ����νṹ��˭�Ǹ�������˭����������
# opencvʹ��һ�����������������Ϣ����������4��Ԫ�أ�[Next, Previous, First_Child, Parent]
# Next ��ʾͬһ����νṹ�е���һ������
# Previous ��ʾͬһ����νṹ�е�ǰһ��������
# First_Child ��ʾ��ǰ�����ĵ�һ����������
# Parent ��ʾ��ǰ�����ĸ�������
# """
#
# contours, hierarchy = cv.findContours(s, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#
# # # �����ĳ���
# # print(len(contours[0]))
# # # ������ǰһ�������ĸ���
# # print(contours[0])
#
# # print(hierarchy)
#
# cv.drawContours(img,contours,-1,(0,0,255),2,8,hierarchy)
# # cv.imshow('img',img)
# # cv.imshow('gray',gray)
# cv.imshow('s',s)
# cv.waitKey(0)
import  cv2 as cv
import  numpy as np
img =cv.imread('02.png')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)
ret,dst = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
# img2 = cv.blur(dst,(3,3))
# cv.imshow('img1',dst)

c,h = cv.findContours(dst,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# print(len(c[0]))

cv.drawContours(img,c,0,(255,0,0),2,8,h)
cv.drawContours(img,c,1,(0,255,255),2,8,h)

# cv.drawContours(img,c,-1,(0,0,255),2,8,h)
# print(c[0])
# print(h)
cv.imshow("ch",img)
cv.waitKey(0)
cv.destroyAllWindows()
