'''import cv2 as cv
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("OUTPUT.mp4",fourcc,30,(640,480))
while cap.isOpened():
    status,frame = cap.read()
    if status:
        out.write(frame)
        cv.imshow('bgr',frame)
        k = cv.waitKey(25)&0XFF
        if chr(k) =='q':
            break
cap.release()
out.release()
cv.destroyAllWindows()'''

import numpy as np
import cv2

# Create a black image
img=np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)

#draw rectangle
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#draw circle
cv2.circle(img,(447,63), 63, (0,0,255), -1)

#draw ellipse
cv2.ellipse(img,(256,256),(100,50),30,0,360,255,3)

#draw multi-lines
pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,0,255),3)#如果去掉中括号，只是画四个点

#add words
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

cv2.imshow('opencv',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
