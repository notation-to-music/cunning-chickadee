# coding:utf8
import cv2
import numpy as np
from function_pakage.pre_treatment import PreTreat
from function_pakage.get_shadow import GetShadow
from function_pakage.get_rows import GetRows
from function_pakage.get_columns import GetColumns
imgx = cv2.imread('test1.jpg', 0) #直接读为灰度图像
imgc = PreTreat(imgx)
img1 = imgc.pre_treat()           #预处理,otsu二值化
kernel_1 = np.ones((2, 2), np.uint8)
img2 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel_1) #形态学闭运算，减少黑线连通
imgs2 = GetShadow(img2)           #水平投影
listy2,listyy2 = imgs2.get_shadowy()
rowsx = GetRows(listy2, listyy2, img1)
rows = rowsx.getrows()            #分行
parti = []
for eachrow in rows:
    columnsx = GetColumns(eachrow, img1)
    columns = columnsx.getcolumns()
    parti.append(columns)         #获得每个子图像的边界
for each_part1 in parti:
    for each_part in each_part1:
        up, down, left, right = int(each_part[0]), int(each_part[1]), \
                                int(each_part[2]), int(each_part[3])
        cv2.imshow('', img1[up:down + 1, left:right + 1])
        cv2.waitKey()
