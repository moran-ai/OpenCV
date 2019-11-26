# 实时视频转片并保存
import cv2 as cv
import datetime
cap = cv.VideoCapture(0)
while cap.isOpened():
    status,frame = cap.read()
    if status:
        k = cv.waitKey(2000) & 0XFF
        key = chr(k)
        if k == 'q':
            break
        else:
            curr_time = datetime.datetime.now()
            timestr = datetime.datetime.strftime(curr_time, '%Y%m%d_%H%M%S')
            filename = timestr + '.jpg'
            print(filename)
            cv.imwrite(filename,frame)
        cv.imshow('video',frame)
cv.destroyAllWindows()

