# coding:gbk
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('sudoku.jpg')
rows,colums,ch = img.shape
print(rows,colums,ch)

# �����ĸ���,����͸�ӱ任
pts1 = np.float32([[56,65],[368,52],[28,419],[390,391]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

# ����任����M
M = cv.getPerspectiveTransform(pts1,pts2)

# ͸�ӱ任
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('input')
plt.subplot(1,2,2)
plt.imshow(dst)
plt.title('output')
plt.show()
