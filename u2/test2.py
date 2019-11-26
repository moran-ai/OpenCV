import cv2 as cv

# 图片的路径
img_path = './test_alpha1.png'
# 读入彩色图，注意OpenCv中颜色格式为BGR
img_bgr = cv.imread(img_path,-1)
print(img_bgr.ndim)
# 打印出形状
print(img_bgr.shape)
# 大小
print(img_bgr.size)
# 数据类型
print(img_bgr.dtype)

h, w, c = img_bgr.shape
print(h, w, c)
print("*" * 40)
print(img_bgr)
print("*" * 40)
image = cv.imread('./test1.png')
print(image)
print(image.shape)
print(image[520,499,:2])
