import cv2 as cv
import numpy as np

img = np.ones((500,500,3),np.uint8) * 127 # 灰白色
cv.namedWindow('t1',0)

def nothing(x):
    pass

# 创建三个滑动条
cv.createTrackbar('B','t1',0,255,nothing)
cv.createTrackbar('G','t1',0,255,nothing)
cv.createTrackbar('R','t1',0,255,nothing)

# 获取滑动条值
while True:
    B = cv.getTrackbarPos('B', 't1')
    G = cv.getTrackbarPos('G', 't1')
    R = cv.getTrackbarPos('R', 't1')
    img[:] = [B,G,R]

    cv.imshow('t1',img)
    k = cv.waitKey(25) & 0XFF
    if  chr(k) == 'q':
        break

cv.destroyAllWindows()
