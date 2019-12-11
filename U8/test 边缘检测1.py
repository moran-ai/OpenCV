# coding:gbk
# 梯度的方向：垂直，水平和两个对角线
import cv2 as cv
img = cv.imread('shape1.png',cv.IMREAD_GRAYSCALE)
# cv.imshow('img',img)

def nothing(x):
    pass

# 创建窗口名
cv.namedWindow('hubo')

# 创建滑动条
cv.createTrackbar('threshold1','hubo',0,255,nothing)
cv.createTrackbar('threshold2','hubo',0,255,nothing)

# 取值
while True:
    threshold1 = cv.getTrackbarPos('threshold1','hubo')
    threshold2 = cv.getTrackbarPos('threshold2','hubo')

    egdes = cv.Canny(img,threshold1,threshold2)
    # cv2.Canny()函数，第一个参数是输入图像，第二个和第三个参数是minVal和maxVal
    cv.imshow('hubo',egdes)
    k = cv.waitKey(25)&0XFF
    if chr(k) == 'q':
        break

cv.destroyAllWindows()
