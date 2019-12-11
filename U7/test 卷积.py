# coding=gbk
import numpy as np
import cv2 as cv

img = cv.imread('./IMG/mouse.jpg')

# 自定义kernel
kernel = np.ones ((5,5),np.float32) /25
kernel_user_1 = np.array([[0,0,1,0,0],
                          [0,0,1,0,0],
                          [1,1,1,1,1,],
                          [0,0,1,0,0],
                          [0,0,1,0,0]]) / 9

kelnel_user_2 = np.array([[1,0,0,0,1],
                          [0,1,0,1,0],
                          [0,0,1,0,0],
                          [0,1,0,1,0],
                          [1,0,0,0,1]]
                         )/9

dst1 = cv.filter2D(img,-1,kernel)
dst2 = cv.filter2D(img,-1,kernel_user_1)
dst3 = cv.filter2D(img,-1,kelnel_user_2)

# print(kelnel_user_2)
cv.imshow('img',img)
cv.imshow('img1',dst1)
cv.imshow('img2',dst2)
cv.imshow('img3',dst3)
cv.waitKey(0)
cv.destroyAllWindows()
