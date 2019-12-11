#coding=gbk
import cv2 as cv
import numpy as np

def nothing(x):
    pass

img = cv.imread('plate02.png')

cv.namedWindow('windows', 0)
cv.createTrackbar('d','windows',49,100,nothing)
cv.createTrackbar('sigmaSpace','windows',80,150,nothing)
cv.createTrackbar('sigmaColor','windows',80,150,nothing)
font = cv.FONT_HERSHEY_SIMPLEX

# ��whileѭ��ȡֵ
while True:
    # resize����
    # src	�����裩ԭͼ��
    # dsize	�����裩���ͼ�������С
    # fx	����ѡ����ˮƽ��ı�������
    # fy	����ѡ���ش�ֱ��ı�������
    # interpolation����ѡ)��ֵ��ʽ
    frame = cv.resize(img, None, fx=.5, fy=.5, interpolation=cv.INTER_LINEAR)
    d = cv.getTrackbarPos('d', 'windows')
    sigmaColor = cv.getTrackbarPos('sigmaColor', 'windows')
    sigmaSpace = cv.getTrackbarPos('sigmaSpace', 'windows')

    # kernelΪ������
    d = d if d % 2 == 1 else d + 1

    # 2D�������
    kernel = np.ones((d, d), np.float32) / (d *d)
    filter2D = cv.filter2D(frame, -1, kernel)
    filter2D = cv.putText(filter2D, "filter2D", (20, 20), font, .65, (255, 255, 255), 2)
    # ˫���˲�
    bfilter = cv.bilateralFilter(frame, d,  sigmaColor, sigmaSpace)
    bfilter = cv.putText(bfilter, 'bfilter',  (20, 20), font, .65, (255, 255, 255), 2)
    # putText�����������ǣ�ͼƬ����ӵ����֣����Ͻ����꣬���壬�����С����ɫ�������ϸ

    cv.imshow('windows', bfilter)
    k = cv.waitKey(24) & 0xFF
    if chr(k) == 'q':
        break
