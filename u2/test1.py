import numpy
import cv2
import os

# 随机生成12000个字节数,u表示无法预测的结果
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray) # 转化为一维矩阵

# 指定形状,变为黑白图
grayImage = flatNumpyArray.reshape(300,400)  # 转化为二维数组
cv2.imwrite('RandomGray.png', grayImage)     # 设置存储名称

# 转化为彩色图
bgrImage = flatNumpyArray.reshape(100,400,3)  # 指定三通道
cv2.imwrite('RandomColor.png',bgrImage)    # 设置存储名称
