# coding=gbk
import cv2 as cv
import numpy as np

img = cv.imread('apple.jpg')
scharrx = cv.Scharr(img,cv.CV_64F,1,0)
scharry = cv.Scharr(img,cv.CV_64F,0,1)
scharrx = cv.convertScaleAbs(scharrx)
scharry = cv.convertScaleAbs(scharry)
scharr_xy = cv.addWeighted(scharrx,0.5,scharry,0.5,0)
cv.imshow('img',img)
cv.imshow('x',scharrx)
cv.imshow('y',scharry)
cv.imshow('xy',scharr_xy)
cv.waitKey(0)
cv.destroyAllWindows()
