import cv2 as cv
# img = cv.imread('plate01.jpg')
# # cv.imshow('t1',img)
# height,width = img.shape[:2]
# dis = img[100:height-200,190:width-320]  # 提取车牌部分
# cv.imshow('t2',dis)
# # print(img.shape)

img = cv.imread('cat.jpg')
# print(img.shape)
height,width = img.shape[:2]
# dis = img[100:height-300,180:width-200]

cv.imshow('t3',img)
cv.waitKey(0)

