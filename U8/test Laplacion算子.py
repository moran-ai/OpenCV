# coding:gbk
# ��Ե���֮һ
"""
��һ�׵������þ���ֵ
����׵������þ���ֵ
ԭͼ����׵������м���

"""

import cv2 as cv

def nothing(x):
    pass
cv.namedWindow('laplacoin')

# ����������
cv.createTrackbar('Ksize','laplacion',1,10,nothing)
img = cv.imread('sudoku.jpg',cv.IMREAD_GRAYSCALE)

# whileѭ��ȡֵ
# while True:
