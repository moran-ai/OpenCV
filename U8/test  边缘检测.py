# coding:gbk

"""
��Ե���Ĳ��裺
1.ȥ������
2.���ݶ�
3.ȷ���߽�
4.�������ı߽�
������cv.Canny()
��Ե�������ݶȹ�ϵ�ʴ�ֱ��ϵ
"""

import cv2 as cv
img = cv.imread('y.jpg',cv.IMREAD_GRAYSCALE)
cv.imshow('img',img)

def nothing(x):
    pass

# ����������
cv.namedWindow('Canny')

# ����������
cv.createTrackbar('threshold1','Canny',0,255,nothing)
cv.createTrackbar('threshold2','Canny',0,255,nothing)


# ȡֵ
while True:
    threshold1 = cv.getTrackbarPos('threshold1','Canny')
    threshold2 = cv.getTrackbarPos('threshold2','Canny')

    egdes = cv.Canny(img,threshold1,threshold2)
    # cv2.Canny()��������һ������������ͼ�񣬵ڶ����͵�����������minVal��maxVal
    cv.imshow('Canny',egdes)
    k = cv.waitKey(25)&0XFF
    if chr(k) == 'q':
        break

cv.destroyAllWindows()
