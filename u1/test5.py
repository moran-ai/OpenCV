import cv2 as cv
img = cv.imread('test_alpha.png')
img[:,:,1]=1  # 第一个:代表所有的行，第二个:代表所有的列；
              # 1代表BGR中的绿色去掉，0代表BGR中的蓝色去掉，2代表BGR中红色去掉
cv.imshow("windows",img)
cv.waitKey(0)

