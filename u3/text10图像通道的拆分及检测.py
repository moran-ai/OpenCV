import cv2 as cv
import numpy as np

img = cv.imread('./test5.jpg',1)
b,g,r = cv.split(img)

# img1 = img[:,:,::-1]

cv.imshow('t1',img)

B = b*1.3
B = B.astype(np.uint8)  # 转化为整数
B = B%255  # 取值范围
img1 = cv.merge((B,g,r))
cv.imshow('b2',img1)
cv.waitKey(0)
# cv.destroyAllWindows()
