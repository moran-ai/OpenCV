# coding:gbk
# �ݶȵķ��򣺴�ֱ��ˮƽ�������Խ���
import cv2 as cv
img = cv.imread('shape1.png',cv.IMREAD_GRAYSCALE)
# cv.imshow('img',img)

def nothing(x):
    pass

# ����������
cv.namedWindow('hubo')

# ����������
cv.createTrackbar('threshold1','hubo',0,255,nothing)
cv.createTrackbar('threshold2','hubo',0,255,nothing)

# ȡֵ
while True:
    threshold1 = cv.getTrackbarPos('threshold1','hubo')
    threshold2 = cv.getTrackbarPos('threshold2','hubo')

    egdes = cv.Canny(img,threshold1,threshold2)
    # cv2.Canny()��������һ������������ͼ�񣬵ڶ����͵�����������minVal��maxVal
    cv.imshow('hubo',egdes)
    k = cv.waitKey(25)&0XFF
    if chr(k) == 'q':
        break

cv.destroyAllWindows()
