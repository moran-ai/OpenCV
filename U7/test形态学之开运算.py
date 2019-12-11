# coding:gbk
import cv2 as cv
import numpy as np

img = cv.imread('bkrc.jpg')

# ����ṹԪ��,�˺ͽṹԪ��С
kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))  # cv.MORPH_RECT ������
# cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)) # cv.MORPH_ELLIPSE ������Բ
cv.getStructuringElement(cv.MORPH_CROSS,(5,5)) # cv.MORPH_CROSS ������

# ת��Ϊ�Ҷ�ͼ
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY)

# �û��������ú˵Ĵ�С
cv.namedWindow('OPEN')

# ����һ��nothing����
def nothing(x):
    pass
cv.createTrackbar('ks','OPEN',2,25,nothing) # 2Ϊ��������ʼֵ��25Ϊ���ֵ

while True:
    ks = cv.getTrackbarPos('ks','OPEN')
    # ȡ�������ϵ�ֵ
    if ks <= 1:
        ks += 1
    # �������ṹԪ,�ֱ��ȡ��ͬ�Ĳ�����������
    rectkernel = cv.getStructuringElement(cv.MORPH_RECT,(ks,ks))
    crosskernel = cv.getStructuringElement(cv.MORPH_CROSS,(ks,ks))
    ellipkernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(ks,ks))

    # ���������
    # ��һ�������Ƕ�ֵ��ͼƬ
    rect = cv.morphologyEx(thresh,cv.MORPH_OPEN,rectkernel)
    cross = cv.morphologyEx(thresh,cv.MORPH_OPEN,crosskernel)
    ellip = cv.morphologyEx(thresh,cv.MORPH_OPEN,ellipkernel)

    # ��ͼƬ��д����
    # ks�ǻ�������ֵ
    cv.putText(rect,'rect'+str(ks),(80,20),cv.FONT_HERSHEY_SIMPLEX,
               .65,(255,255,255),2)
    cv.putText(cross,'cross'+str(ks),(80,20),cv.FONT_HERSHEY_SIMPLEX,
               .65, (255, 255, 255), 2)
    cv.putText(ellip,'ellip'+str(ks),(80,20),cv.FONT_HERSHEY_SIMPLEX,
               .65,(255, 255, 255), 2)

    # ��ԭͼ��rect/cross/ellip�ų�2��2����ʾ
    h1 = np.hstack((thresh,rect))
    h2 = np.hstack((ellip,cross))

# ������,�ȸ�ʴ��������
# opend = cv.morphologyEx(img,cv.MORPH_CLOSE,(5,5))

    cv.imshow('OPEN',np.vstack((h1,h2)))
    k = cv.waitKey(100)&0xff
    if chr(k) == 'q':
        break
