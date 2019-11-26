# 绘制线条函数
import cv2 as cv
import numpy as np

img = np.zeros((500,500,3),np.uint8)
img1 = np.ones((500,500,3),np.uint8)*255
# cv.line(img,(0,0),(499,499),(255,255,255),5)  # 线段
# cv.rectangle(img1,(255,0),(0,25),(0,255,0),1)
# cv.rectangle(img1,(253,0),(66,26),(46,210,255),2)
# cv.rectangle(img1,(208,0),(64,19),(0,0,255),3)  # rectangle画矩形
# cv.rectangle(img,(255,0),(0,255),(0,255,0),1)
# cv.circle(img,(255,255),100,(255,0,0),-1)  # 圆心，半径，颜色，粗细,（-1):填充
# cv.circle(img,(255,255),150,(0,255,0),3)
# cv.ellipse(img,(150,150),(70,40),30,0,360,(0,180,200),-1,cv.LINE_AA)  # ellipse椭圆
# cv.ellipse(img,(150,150),(90,50),30,0,360,(200,100,200),3,cv.LINE_AA)
# 椭圆中心坐标；长半轴以及短半轴；angle椭圆沿逆时针旋转的角度；
# startAngle椭圆沿顺时针起始的角度;endAngle椭圆沿顺时针结束的角度
# pts = np.array([[100,50],[200,300],[300,200],[400,200]],np.int32)
# cv.polylines(img,[pts],True,(0,0,255),3,cv.LINE_AA) # True表示闭合多边形
# # polylines多边形
# cv.polylines(img1,[pts],False,(0,0,255),3,cv.LINE_AA)  # False表示不闭合多边形
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'learning OpenCV',(0,200),font,4,(255,255,255),cv.LINE_AA)
cv.putText(img1,'hu',(0,200),font,4,(0,0,255),cv.LINE_AA)
# putText在图像上绘制文字
cv.imshow('t3',img)
cv.imshow('t5',img1)
cv.waitKey(0)
