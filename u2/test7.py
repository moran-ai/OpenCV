# 图片切片
import cv2 as cv

img_path = './test_alpha1.png'
img = cv.imread(img_path,1)

print(img[0,0])
print(img[1,1,1])
print(img.shape)
print('*' * 40)
# img.itemset((0, 0, 0),255)
# img.itemset((0, 1, 1), 255)

brimg = img.copy()
print("BGR转RGB")
brimg = img[:,:,::-1]  # BGR转RGB
print(brimg)
cv.imshow("t2",brimg)
cv.waitKey(0)
# print("*" * 40)
# print(img[0,0])
