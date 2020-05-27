import os
import xml.etree.ElementTree as ET

img_dir='/home/hongliang/PycharmProjects/yuanshi_tuxiang/'
xml_dir='/home/hongliang/PycharmProjects/tuxiang_biaozhu/'
save_dir='/home/hongliang/PycharmProjects/ceshi_biaozhu/'

def list_xml():
    xml_list2=[]
    #xml_list=[xml_name for xml_name in os.listdir(img_dir)]
    for xml_name in os.listdir(img_dir):
        xml_name2=xml_name.replace('.jpg','.xml')
        xml_list2.append(xml_name2)

    L = [x for x in range(1, 17653)]  # 17653为xml数量+1
    # print(L)
    L2 = L[::4]  # L2每四个提取一个数字
    # print(L2)
    L3 = []
    for i in L2:  # 从知L中3个4数道
        L3.append(xml_list2[i - 1:i + 3])  # 切片是从0计数 所以从i-1 开始
    return L3

def hebin_xml():
    L3=list_xml()
    #print(L3)
    for i in L3:
        print(i)
# 第一幅图
        tree=ET.parse(xml_dir+i[0])
        root=tree.getroot()
        obj=root.find('frame')
        for elem in root.iter('xmin'):
            new_elem=(int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('ymin'):
            new_elem=(int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('xmax'):
            new_elem=(int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('ymax'):
            new_elem=(int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        tree.write(save_dir + i[0])
#第二幅图
        tree=ET.parse(xml_dir+i[1])
        root=tree.getroot()
        obj=root.find('frame')
        for elem in root.iter('xmin'):
            new_elem=(360+int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('ymin'):
            new_elem=(int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('xmax'):
            new_elem=(360+int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('ymax'):
            new_elem=(int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        tree.write(save_dir +i[1])
#第三幅图
        tree = ET.parse(xml_dir + i[2])
        root = tree.getroot()
        obj=root.find('frame')
        for elem in root.iter('xmin'):
            new_elem=(int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('ymin'):
            new_elem=(202+int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('xmax'):
            new_elem=(int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('ymax'):
            new_elem=(202+int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        tree.write(save_dir +i[2])
#第四幅图
        tree = ET.parse(xml_dir + i[3])
        root = tree.getroot()
        obj=root.find('frame')
        for elem in root.iter('xmin'):
            new_elem=(360+int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('ymin'):
            new_elem=(202+int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('xmax'):
            new_elem=(360+int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        for elem in root.iter('ymax'):
            new_elem=(202+int(elem.text)//2+int(elem.text)%2)
            elem.text=str(new_elem)
        tree.write(save_dir+i[3])

hebin_xml()
