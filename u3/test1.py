import numpy as np
import cv2 as cv
imgpath='./test1.png'
img1=cv.imread(imgpath,1)
img1[:,:,2]=0
img2=cv.imread(imgpath,cv.IMREAD_GRAYSCALE)
cv.imshow('gray1',img2)
cv.imshow('bgrl',img1)
cv.waitKey(0)
