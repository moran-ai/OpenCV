# coding:gbk
# import cv2 as cv
#
# # 读取图片
# img = cv.imread('02.png')
#
# #  颜色转换
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
# #  阈值处理
# ret,s= cv.threshold(gray,200,255,cv.THRESH_BINARY_INV)
#
# # # 平滑
# # img2 =cv.blur(s,(3,3))
#
# # 查找轮廓
# """
# 每一个轮廓都有包含一些信息：层次结构，谁是父轮廓，谁是子轮廓。
# opencv使用一个数组来保存相关信息，该数组有4个元素：[Next, Previous, First_Child, Parent]
# Next 表示同一级层次结构中的下一个轮廓
# Previous 表示同一级层次结构中的前一个轮廓。
# First_Child 表示当前轮廓的第一个子轮廓。
# Parent 表示当前轮廓的父轮廓。
# """
#
# contours, hierarchy = cv.findContours(s, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#
# # # 轮廓的长度
# # print(len(contours[0]))
# # # 轮廓的前一个轮廓的个数
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
