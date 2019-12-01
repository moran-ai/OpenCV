import cv2 as cv
import numpy as np

img = cv.imread('rub00.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)  # 转换为hsv
lower_green = np.array([35, 43, 46])
upper_green = np.array([77, 255, 255])
green = cv.inRange(hsv,lower_green,upper_green)   # 分割
img_1 = cv.bitwise_and(img,img,mask=green)

lower_green1 = np.array([0, 43, 46])
upper_green1 = np.array([5,255,255])
maskred = cv.inRange(hsv,lower_green1,upper_green1)
img_3 = cv.bitwise_and(img,img,mask=maskred)

lower_green2 = np.array([170,43,46])
upper_green2 = np.array([180,255,255])
maskred1 = cv.inRange(hsv,lower_green2,upper_green2)
img_2 = cv.bitwise_and(img,img,mask=maskred1)

lower_green3 = np.array([20,43,46])
upper_green3 = np.array([34,255,255])
maskred2 = cv.inRange(hsv,lower_green3,upper_green3)
img_4  = cv.bitwise_and(img,img,mask=maskred2)

lower_blue = np.array([100,43,46])
upper_blue = np.array([124,255,255])
maskblue = cv.inRange(hsv,lower_blue,upper_blue)
img_blue = cv.bitwise_and(img,img,mask=maskblue)
# cv.imshow('r3',img_1)
# cv.imshow('r1',green)

# cv.imshow('r2',img)
# cv.imshow('r5',maskred)
# cv.imshow('r4',maskred1)
# cv.imshow('r6',img_2)
cv.imshow('r7',img_4)
# cv.imshow('r8',img_blue)

cv.waitKey(0)
