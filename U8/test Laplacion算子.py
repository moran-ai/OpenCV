# coding:gbk
# 边缘检测之一
"""
求一阶导数，用绝对值
求二阶导数不用绝对值
原图与二阶导数进行计算

"""

import cv2 as cv

def nothing(x):
    pass
cv.namedWindow('laplacoin')

# 创建滑动条
cv.createTrackbar('Ksize','laplacion',1,10,nothing)
img = cv.imread('sudoku.jpg',cv.IMREAD_GRAYSCALE)

# while循环取值
# while True:
