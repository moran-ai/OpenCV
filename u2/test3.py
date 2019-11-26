import cv2
import matplotlib.pyplot as plt
# 彩色图转化为灰度图
image = cv2.imread('test_alpha1.png',cv2.IMREAD_GRAYSCALE)
# cv2.IMREAD_GRAYSCALE 总是返回一个灰度图
cv2.imwrite('test_alpha2.png',image)
print(image.shape)
print('*'*40)

# 与原图进行对比
image1 = cv2.imread('test_alpha.png')
print(image1.shape)
print("*" * 40)

# BGR转RGB
image2 = cv2.imread('test5.jpg')
B, G, R = cv2.split(image2)  # split函数通道分离
image2_rgb = cv2.merge([R, G, B])  # merge函数将多个单通道图像合成为一幅多通道图像
plt.figure('BGR_RGB')  # figure显示窗口的名字

# 显示opencv读进来的image2,通道顺序BGR
plt.subplot(3, 3, 1),plt.imshow(image2)
# subplot将多个画画到一个平面上，图排成3行3列，1代表图片的位置
# p=1代表从左至右从上到下的第一个位置

# 显示B通道
plt.subplot(3, 3, 4),plt.imshow(B)  # 图排成3行3列，4代表图片的位置

# 显示G通道
plt.subplot(3, 3, 5),plt.imshow(G)  # 图排成3行3列，5代表图片的位置

# 显示R通道
plt.subplot(3, 3, 6),plt.imshow(R)  # 图排成3行3列，6代表图片的位置

# 显示将BGR转换为RGB的图像
plt.subplot(3, 3, 7),plt.imshow(image2_rgb)  # 图排成3行3列，7代表图片的位置
plt.show()
