# coding:gbk
#!/usr/bin/env python3
# -*- coding:UTF8 -*-

"""
����ԭ�����£�
    convexHull(points[, hull[, clockwise[, returnPoints]]]) -> hull
    �ص����������
        points:����Ҫ�����������Ϣ��
        hull�����ͨ������Ҫ��
        clockwise�������־���������Ϊ True�����͹����˳ʱ�뷽��ġ�
        ����Ϊ��ʱ�뷽��
        returnPoints��Ĭ��ֵΪTrue�����᷵��͹���ϵ�����ꡣ�������
        Ϊ False�ͻ᷵����͹�����Ӧ�������ϵĵ㡣
͹��ȱ�ݷ���
    convexityDefects(contour, convexhull[, convexityDefects]) -> convexityDefects
        ����������
        contour��һ�����������⺯��findContours�����
        convexhull��convexHull���������������洢����͹����Ϣ��
        convexityDefects ������ÿһ��͹��ȱ�ݣ�ʵ���Ͼ���һϵ�е㣬��Щ������á�
        �������أ�[-1, 4]���͵�list
            ��һ�����ֽ���
            start_index,��ʾȱ���������ϵĿ�ʼ��������ֵ�ǿ�ʼ���ں�����һ������ contour �е��±�������

            Vec4i �ڶ���Ԫ�ص����ֽ�
            end_index�� ����˼�����Ӧ��ֵ����ȱ�ݽ������� contour �е��±�������

            Vec4i ������Ԫ��
            farthest_pt_index ��ȱ���Ͼ�������͹��(convexhull)��Զ�ĵ㣻

            Vec4i����Ԫ�ؽ�
            fixpt_depth��fixpt_depth/256  ��ʾ��
            �������� farthest_pt_index Ϊ�±�ĵ㵽 ����͹����(convexhull)�ľ���,������Ϊ��λ��
"""

import cv2 as cv

if __name__ == "__main__":

    img = cv.imread('star.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

    if (cv.__version__[0] == '4'):
        # ��������
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    else:
        _, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # ����͹��
    hull_cv = cv.convexHull(contours[0])   # ����
    cv.drawContours(img, [hull_cv], 0, (0, 0, 255), 2, cv.LINE_AA)

    # ���һ�������ǲ���͹�ģ�����True��Flase
    k = cv.isContourConvex(hull_cv)   # ���ؽ��Ϊ����ֵ
    # print(k)

    # Ѱ��͹ȱ��
    # ����ȱ���Ͼ�������͹��(convexhull)��Զ�ĵ�
    hull = cv.convexHull(contours[0], returnPoints = False)
    defects = cv.convexityDefects(contours[0], hull)
    print(defects, defects.shape)
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        far = tuple(contours[0][f][0])
        cv.circle(img, far, 5, (0, 0, 255), -1)

    cv.imshow('img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
