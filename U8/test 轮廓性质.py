# coding:gbk
"""
函数:cv.moments()

计算质心
Cx = m10/m00
Cy = m01/m00
轮廓面积：area = cv.contourArea(contours[1])

轮廓周长：cv.arcLength()

"""

import  cv2 as cv
import  numpy as np
img =cv.imread('02.png')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)
ret,dst = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
# img2 = cv.blur(dst,(3,3))
# cv.imshow('img1',dst)

c,h = cv.findContours(dst,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# print(len(c[0]))
# print(h)
cv.drawContours(img,c,0,(255,0,0),2,8,h)
cv.drawContours(img,c,1,(0,255,255),2,8,h)

# 保存
c1 = c[1]
c0=c[0]
M = cv.moments(c1)  # 返回一个字典
M1 = cv.moments(c0)
# print(M)
# print(M1)

# # 计算
Cx = int(M['m10']/M['m00'])
Cy = int(M['m01']/M['m00'])

cx = int(M1['m10']/M1['m00'])
cy = int(M1['m01']/M1['m00'])

# print(Cx)
cv.circle(img,(Cx,Cy),8,(0,255,0),1)
cv.circle(img,(cx,cy),5,(255,0,0),2)

# 计算轮廓面积
Area = cv.contourArea(c[0])
Area1 = cv.contourArea(c[1])
print('矩形面积:')
print(Area)
print('三角形面积:')
print(Area1)
print('*'*50)

# 计算周长
arclenth = cv.arcLength(c[0],True)   # 第二个参数用来表示图形是闭合的还是打开的
arclenth1 = cv.arcLength(c[1],True)
print('矩形周长:')
print(arclenth)
print('三角形周长:')
print(arclenth1)

# cv.drawContours(img,c,-1,(0,0,255),2,8,h)
# print(c[0])
# print(h)
# cv.imshow("ch",img)
# cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
