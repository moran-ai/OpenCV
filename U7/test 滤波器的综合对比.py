# coding=gbk
import cv2 as cv
import numpy as np

def nothing(x):
    pass
cap = cv.VideoCapture(0) # ����0������������ͷ
cv.namedWindow('windows')
cv.createTrackbar('ks','windows',3,31,nothing)  # ����������
font = cv.FONT_HERSHEY_SIMPLEX
while cap.isOpened():
    ret,frame = cap.read()   # ret ֡,frame ͼƬ
    # �ߴ�
    frame = cv.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv.INTER_LINEAR)
    ks = cv.getTrackbarPos('ks','windows')
    # ��֤ksΪ������
    ks = ks if ks%2==1 else ks+1
    # �����
    kernel = np.ones((ks,ks),np.float32)/(ks*ks)
    # 2D���
    filter2D = cv.filter2D(frame,-1,kernel)   # -1���ݺ˽��м���
    # д��
    filter2D = cv.putText(filter2D,'filter2d',(20,20),font,0.65,(255,255,255),2)
    # ��ֵģ��
    blur = cv.blur(frame,(ks,ks))
    blur = cv.putText(blur, 'blur',(20, 20), font, 0.65, (255, 255, 255), 2)
    # ��˹ģ��
    gblur = cv.GaussianBlur(frame,(ks,ks),0)
    gblur = cv.putText(gblur,'gblur',(20, 20), font, 0.65, (255, 255, 255), 2)
    # ��ֵģ��
    medianblur = cv.medianBlur(frame,ks)  # ksΪ������
    medianblur = cv.putText(medianblur,'medianblur',(20, 20), font, 0.65, (255, 255, 255), 2)
    # ˫���˲�
    bfilter = cv.bilateralFilter(frame,-1,2*ks,int(0.7*ks))
    bfilter = cv.putText(bfilter,'bfilter',(20,20),font,0.65,(255,255,255),2)

    # ƴ��
    hs1 = np.hstack((frame,blur,filter2D))
    hs2 = np.hstack((gblur,medianblur,bfilter))

    vs = np.vstack((hs1,hs2))
    cv.imshow('windows',vs)
    k = cv.waitKey(25)

cv.destroyAllWindows()
