# 创建窗口函数 namedWindow
import cv2 as cv
img_path = './test5.jpg'
img = cv.imread(img_path,0)
cv.namedWindow('imgt1',0)  # 0代表窗口大小可变，1不可变++++++
cv.imshow('imgt1',img)
# 参数一：窗口名; WARP_FILL_OUTLIERS不可改
cv.waitKey(0)
cv.destroyAllWindows()
