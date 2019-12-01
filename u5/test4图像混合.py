import cv2 as cv

img1 = cv.imread('sea.jpg')
img2 = cv.imread('sun.jpg')

res = cv.addWeighted(img1, 0.6, img2, 0.5, 0)
cv.imshow('res',res)
cv.waitKey(0)

