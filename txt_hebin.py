import os
import xml.etree.ElementTree as ET

img_dir='/home/hongliang/PycharmProjects/yuanshi_tuxiang/'
txt_dir='/home/hongliang/PycharmProjects/ceshi_txt/'
save_dir='/home/hongliang/PycharmProjects/hebin_txt/'

def list_xml():
    xml_list2=[]
    #xml_list=[xml_name for xml_name in os.listdir(img_dir)]
    for xml_name in os.listdir(img_dir):
        xml_name2=xml_name.replace('.jpg','.txt')
        xml_list2.append(xml_name2)

    L = [x for x in range(1, 17653)]  # 17653为xml数量+1
    # print(L)
    L2 = L[::4]  # L2每四个提取一个数字
    # print(L2)
    L3 = []
    for i in L2:  # 从知L中3个4数道
        L3.append(xml_list2[i - 1:i + 3])  # 切片是从0计数 所以从i-1 开始
    return L3

def txt_hebin():
    L3 = list_xml()
    #print(L3)
    count = 0

    for i in L3:
        print(i)
    # 要写入的文件
        file = open(save_dir + str(count) + '.txt', 'w+')

        file1 = open(txt_dir + i[0], 'r')
        s1 = file1.read()
        file.write(s1)

        file2 = open(txt_dir + i[1], 'r')
        s2 = file2.read()
        file.write(s2)

        file3 = open(txt_dir + i[2], 'r')
        s3 = file3.read()
        file.write(s3)

        file4 = open(txt_dir + i[3], 'r')
        s4 = file4.read()
        file.write(s4)

        file1.close()
        file2.close()
        file3.close()
        file4.close()
        file.close()

        count = count + 1

txt_hebin()
