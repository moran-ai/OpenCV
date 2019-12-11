# coding:gbk
"""
������cv.HoughLines()
���裺
1.�Ա�Եͼ����л���ռ�任
2.��4�������ҵ�����ռ�任�ļ���ֵ
3.����Щ����ֵ��װ�ɴ�С˳��������򣬼���ֵԽ��Խ�п�����ֱ��
4.���ֱ��
 ������
��һ������ͼƬΪ��ֵ��ͼ�����߽��б�Ե���
�ڶ����������ֱ����ȷ��
���ĸ���������ֵ,���Ƕ�ֵ������ֵ
Hough ֱ�߱任ԭ��
һ��ֱ�߿�������ѧ���ʽ��y=mx+c

"""

import cv2 as cv
import numpy as np

# ����ͼƬ
img = cv.imread('bmx.jpg')
# ��˹�˲�
blur = cv.GaussianBlur(img,(5,5),-5,-5)
# ��ɫת��
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# ��ֵ��
ret,g = cv.threshold(gray,180,255,cv.THRESH_BINARY)
# ��Ե���
edges = cv.Canny(g,120,200)

# ����任
lines = cv.HoughLines(edges,1,np.pi/180,130)
# print(lines)

# ѭ��
for line in lines:
    for rho,theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*(a))
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# cv.imshow('img',g)
# cv.imshow('img1',edges)
cv.imshow('lines',img)
cv.waitKey(0)
