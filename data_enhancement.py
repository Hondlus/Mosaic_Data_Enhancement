import cv2
import os
import numpy as np


img_dir='/home/hongliang/PycharmProjects/yuanshi_tuxiang/'
save_dir='/home/hongliang/PycharmProjects/zengqiang_tuxiang/'

def list_image():
    select_list= [img_name for img_name in os.listdir(img_dir)]
    #print(select_list)
    L = [x for x in range(1, 17653)]#13为图像数量+1
    #print(L)
    L2 = L[::4]  # L2每四个提取一个数字
    #print(L2)
    L3 = []
    for i in L2:  # 从知L中3个4数道
        L3.append(select_list[i -1:i + 3])  # 切片是从0计数 所以从i-1 开始
    return L3
    #print(L3[0][0])

def pinjie_image():
    L3=list_image()
    #print(L3)
    count = 0
    for i in L3:
        print(i)
        img=cv2.imread(img_dir+i[0])
        img=cv2.resize(img,None,fx=0.5,fy=0.5)
        #cv2.imshow("1", img)

        img2=cv2.imread(img_dir+i[1])
        img2=cv2.resize(img2, None, fx=0.5, fy=0.5)
        #cv2.imshow("2", img2)

        img3=cv2.imread(img_dir+i[2])
        img3=cv2.resize(img3, None, fx=0.5, fy=0.5)
        #cv2.imshow("3", img3)

        img4=cv2.imread(img_dir+i[3])
        img4=cv2.resize(img4, None, fx=0.5, fy=0.5)
        #cv2.imshow("4", img4)

        htich=np.hstack((img,img2))
        htich2=np.hstack((img3,img4))
        vtich=np.vstack((htich,htich2))
        vtich2=cv2.resize(vtich,(720,405))
        #cv2.imshow('merge.jpg', vtich2)

        cv2.imwrite(save_dir + str(count) + '.jpg', vtich2)
        count=count+1
        #cv2.waitKey(0)
        #cv2.destroyWindows()

pinjie_image()

