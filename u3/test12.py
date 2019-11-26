import cv2 as cv
import numpy as np
ox = 0
oy = 0
sx = 0
sy = 0

# 回调函数，在回调函数中处理
def draw_rectangle(event, x, y, flags, param):
    # global 修饰的字段，表示使用全局变量
    global img
    global ox, oy, sx, sy

    # 鼠标左键双击清理图像
    if event == cv.EVENT_LBUTTONDBLCLK:
        img = np.ones((500, 500, 3), np.uint8) * 127
    elif event != cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        sx, sy = x, y
        ox, oy = x, y
    # 左键按下且鼠标移动事件
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.line(img, (ox, oy), (x, y), (255, 255, 255), 3, cv.LINE_AA)
        ox, oy = x, y
    elif flags != cv.EVENT_FLAG_LBUTTON and event != cv.EVENT_MOUSEMOVE:
        cv.rectangle(img, (sx, sy), (x, y), (255, 0, 255), 3, cv.LINE_AA)

# 创建一个窗体并为鼠标事件绑定监听回调函数
cv.namedWindow('image')
cv.setMouseCallback('image', draw_rectangle)

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
