import cv2 as cv
import numpy as np

x = np.uint8([250])
y = np.uint8([10])
cv.add(x,y)
print(cv.add(x,y))
print(x+y)

dog1 = cv.imread('dog1.jpg')
dog2 = cv.imread('dog2.jpg')
dogcvadd = cv.add(dog1,dog2)
a = dog1+dog2
cv.imshow('cvadd',dogcvadd)
cv.imshow('cvadd1',a)
cv.waitKey(0)
cv.destroyAllWindows()
