# coding:gbk
import cv2 as cv

img = cv.imread('o.jpg')

# ͼƬ��С
# cv.resize(img,None,fx=2,fy=10,interpolation=1)
# ��ɫת��
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# ��ֵ��
ret,dst = cv.threshold(gray,90,255,cv.THRESH_BINARY_INV)

# ��������
# c�������е�������h��ʾ�����Ĳ����Ϣ
# contours, hierarchy=cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]])
c,h = cv.findContours(dst,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

# ������
# cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[
"""
image��Ŀ�����ͼ�� 
contours�����е���������ֱ�Ӵ���findContours�����е�contours���� 
contourIdx���������������������ĸ���������Ϊ��ֵ������������� 
color�����Ƶ���ɫ��Ԫ����ʽ���磨255����255, 255, 255�� 
thickness�����Ƶ�������������ϸ�̶ȣ���Ϊ��������ʾҪ�����������

"""

cv.drawContours(img,c,-1,(0,255,0),2,8,h)

c0=c[0]
m = cv.moments(c0)
cx = int(m['m10']/m['m00'])
cy = int(m['m01']/m['m00'])

# print(m)
# cv.circle(img,(cx,cy),5,(0,0,255),1)

cv.imshow('img1',dst)
# cv.imshow('img',img)

cv.waitKey(0)
