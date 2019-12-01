# 使用摄像头进行颜色识别

'''import cv2 as cv
import numpy as np
# 创建窗口
cv.namedWindow('color')

def nothing(x):
    pass
# 创建滑动条
cv.createTrackbar('HMAX','color',0,180,nothing)
cv.createTrackbar('HMIN','color',0,180,nothing)


# 调用摄像头
cap = cv.VideoCapture(0)
while cap.isOpened():        # 判断摄像头是否打开
    ret,frame = cap.read()   # 状态，帧
    if ret:
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)   # 画面由BGR转为HSV
        lower = cv.getTrackbarPos('HMIN','color')   # 获取滑动条上的值
        upper = cv.getTrackbarPos('HMAX','color')
        hsvmin = np.array([lower,60,60])
        hsvmax = np.array([upper,255,255])
        mask = cv.inRange(hsv,lower,upper)             # 掩模
        img = cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow('color',img)
        cv.waitKey(25) & 0xFF
    else:
        break


cap.release()
cv.destroyAllWindows()'''''


# 使用摄像头进行颜色转换
import cv2 as cv
import numpy as np
cv.namedWindow('color',0)
def nothing(x):
    pass
cv.createTrackbar("HMAX","color",0,180,nothing)
cv.createTrackbar("HMIN","color",0,180,nothing)
cap = cv.VideoCapture(0)
while cap.isOpened():  # 判断摄像头是否打开
    ret,frame = cap.read()  # 状态，帧
    if ret:
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower = cv.getTrackbarPos("HMIN",'color')
        upper = cv.getTrackbarPos("HMAX",'color')
        hsvmin = np.array([lower,0,0])
        hsvmax = np.array([upper,70,255])
        mask = cv.inRange(hsv,hsvmin,hsvmax)  # 建立掩模
        img = cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow('color',img)
        cv.waitKey(25)
    else:
        break
cap.release()
cv.destroyAllWindows()

