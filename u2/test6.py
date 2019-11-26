# 输出图像到文件
import cv2 as cv
img_path = '111.jpg'
img = cv.imread("img_path",1)
cv.imwrite("tuxiang.jpg",img)
