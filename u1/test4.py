import numpy as np
import cv2
a = np.zeros((4,4),dtype=np.uint8)
print(a)
print(a.shape)

# 转换为BGR格式
a = cv2.cvtColor(a, cv2.COLOR_GRAY2BGR)  # cvtColor 颜色转换, a为图片
print(a)
print(a.shape)
