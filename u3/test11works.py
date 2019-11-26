import cv2 as cv
import numpy as np
# from PIL import Image, ImageDraw, ImageFont

# 创建一张黑色图片
img = np.zeros((600,600,3),np.uint8) * 127

# 画椭圆
cv.ellipse(img,(110,110),(114,50),180,0,360,(24,255,17),4,cv.LINE_AA)
cv.ellipse(img,(110,110),(30,70),100,0,180,(255,255,255),2,cv.LINE_AA)
cv.ellipse(img,(110,110),(40,80),270,0,90,(24,255,17),2,cv.LINE_AA)
cv.ellipse(img,(110,110),(40,80),270,90,180,(255,36,17),2,cv.LINE_AA)
cv.ellipse(img,(110,110),(20,40),270,0,90,(255,118,13),2,cv.LINE_AA)
cv.ellipse(img,(110,110),(20,40),270,90,180,(38,33,255),2,cv.LINE_AA)
# 画矩形
cv.rectangle(img,(10,500),(300,300),(28,255,254),2,cv.LINE_AA)
cv.rectangle(img,(50,310),(270,490),(28,255,254),2,cv.LINE_AA)
cv.rectangle(img,(80,350),(240,460),(28,255,254),2,cv.LINE_AA)

# 画线
cv.line(img,(10,400),(300,400),(174,177,255),5)
cv.line(img,(150,300),(150,500),(76,188,255),5)

# 画圆
cv.circle(img,(150,400),100,(255,207,59),3)
cv.circle(img,(150,400),90,(255,207,59),2)
cv.circle(img,(150,400),80,(255,207,59),3)
cv.circle(img,(150,400),70,(255,207,59),1)
cv.circle(img,(500,400),70,(245,245,245),-1)

# 闭合图形
pts = np.array([[400,100],[450,200],[300,200],[490,50],[380,40]],np.int32)
cv.polylines(img,[pts],True,(0,0,255),4,cv.LINE_AA)

# 显示文字
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(1,580),font,4,(243,255,177),cv.LINE_AA)
cv.putText(img,'35',(490,200),font,2,(175,175,175),cv.LINE_AA)
cv.putText(img,'HuBo',(440,300),font,2,(175,175,175),cv.LINE_AA)

cv.imshow('img',img)
cv.waitKey(0)