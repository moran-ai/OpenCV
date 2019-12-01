import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR_')]  # 统计以COLOR_开头的词
# print(flags)
print(len(flags))

