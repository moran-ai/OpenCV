# coding=gbk
import cv2 as cv
import numpy as np

def nothing(x):
    pass
cap = cv.VideoCapture(0) # 参数0代表内置摄像头
cv.namedWindow('windows')
cv.createTrackbar('ks','windows',3,31,nothing)  # 创建滑动条
font = cv.FONT_HERSHEY_SIMPLEX
while cap.isOpened():
    ret,frame = cap.read()   # ret 帧,frame 图片
    # 尺寸
    frame = cv.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv.INTER_LINEAR)
    ks = cv.getTrackbarPos('ks','windows')
    # 保证ks为正奇数
    ks = ks if ks%2==1 else ks+1
    # 卷积核
    kernel = np.ones((ks,ks),np.float32)/(ks*ks)
    # 2D卷积
    filter2D = cv.filter2D(frame,-1,kernel)   # -1根据核进行计算
    # 写字
    filter2D = cv.putText(filter2D,'filter2d',(20,20),font,0.65,(255,255,255),2)
    # 均值模糊
    blur = cv.blur(frame,(ks,ks))
    blur = cv.putText(blur, 'blur',(20, 20), font, 0.65, (255, 255, 255), 2)
    # 高斯模糊
    gblur = cv.GaussianBlur(frame,(ks,ks),0)
    gblur = cv.putText(gblur,'gblur',(20, 20), font, 0.65, (255, 255, 255), 2)
    # 中值模糊
    medianblur = cv.medianBlur(frame,ks)  # ks为正奇数
    medianblur = cv.putText(medianblur,'medianblur',(20, 20), font, 0.65, (255, 255, 255), 2)
    # 双边滤波
    bfilter = cv.bilateralFilter(frame,-1,2*ks,int(0.7*ks))
    bfilter = cv.putText(bfilter,'bfilter',(20,20),font,0.65,(255,255,255),2)

    # 拼接
    hs1 = np.hstack((frame,blur,filter2D))
    hs2 = np.hstack((gblur,medianblur,bfilter))

    vs = np.vstack((hs1,hs2))
    cv.imshow('windows',vs)
    k = cv.waitKey(25)

cv.destroyAllWindows()
