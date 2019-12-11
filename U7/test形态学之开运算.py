# coding:gbk
import cv2 as cv
import numpy as np

img = cv.imread('bkrc.jpg')

# 定义结构元素,核和结构元大小
kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))  # cv.MORPH_RECT 代表方形
# cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)) # cv.MORPH_ELLIPSE 代表椭圆
cv.getStructuringElement(cv.MORPH_CROSS,(5,5)) # cv.MORPH_CROSS 交叉形

# 转化为灰度图
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY)

# 用滑动条设置核的大小
cv.namedWindow('OPEN')

# 定义一个nothing方法
def nothing(x):
    pass
cv.createTrackbar('ks','OPEN',2,25,nothing) # 2为滑动条初始值，25为最大值

while True:
    ks = cv.getTrackbarPos('ks','OPEN')
    # 取滑动条上的值
    if ks <= 1:
        ks += 1
    # 定义结果结构元,分别读取不同的参数进行设置
    rectkernel = cv.getStructuringElement(cv.MORPH_RECT,(ks,ks))
    crosskernel = cv.getStructuringElement(cv.MORPH_CROSS,(ks,ks))
    ellipkernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(ks,ks))

    # 开运算操作
    # 第一个参数是二值化图片
    rect = cv.morphologyEx(thresh,cv.MORPH_OPEN,rectkernel)
    cross = cv.morphologyEx(thresh,cv.MORPH_OPEN,crosskernel)
    ellip = cv.morphologyEx(thresh,cv.MORPH_OPEN,ellipkernel)

    # 在图片上写文字
    # ks是滑动条的值
    cv.putText(rect,'rect'+str(ks),(80,20),cv.FONT_HERSHEY_SIMPLEX,
               .65,(255,255,255),2)
    cv.putText(cross,'cross'+str(ks),(80,20),cv.FONT_HERSHEY_SIMPLEX,
               .65, (255, 255, 255), 2)
    cv.putText(ellip,'ellip'+str(ks),(80,20),cv.FONT_HERSHEY_SIMPLEX,
               .65,(255, 255, 255), 2)

    # 把原图和rect/cross/ellip排成2行2列显示
    h1 = np.hstack((thresh,rect))
    h2 = np.hstack((ellip,cross))

# 开运算,先腐蚀，后膨胀
# opend = cv.morphologyEx(img,cv.MORPH_CLOSE,(5,5))

    cv.imshow('OPEN',np.vstack((h1,h2)))
    k = cv.waitKey(100)&0xff
    if chr(k) == 'q':
        break
