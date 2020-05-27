import os

img_dir='/home/hongliang/PycharmProjects/yuanshi_tuxiang/'
txt_dir='/home/hongliang/PycharmProjects/ceshi_biaozhu/'
save_dir='/home/hongliang/PycharmProjects/ceshi_txt/'

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

def xiugai_xml():
    L3=list_xml()
    #print(L3)
    for i in L3:
        print(i)

        infile = open(txt_dir+i[0], 'r')
        a = infile.readlines()
        outfile = open(save_dir+i[0], 'w')
        b = ''.join(a[:-1])
        outfile.write(b)

        infile = open(txt_dir + i[1], 'r')
        a = infile.readlines()
        outfile = open(save_dir + i[1], 'w')
        b = ''.join(a[3:-1])
        outfile.write(b)

        infile = open(txt_dir + i[2], 'r')
        a = infile.readlines()
        outfile = open(save_dir + i[2], 'w')
        b = ''.join(a[3:-1])
        outfile.write(b)

        infile = open(txt_dir + i[3], 'r')
        a = infile.readlines()
        outfile = open(save_dir + i[3], 'w')
        b = ''.join(a[3:])
        outfile.write(b)

xiugai_xml()

# infile=open('/home/hongliang/000000.txt','r')
# a=infile.readlines()
# outfile=open('/home/hongliang/000000_xiugai.txt','w')
# b=''.join(a[:-1])
# outfile.write(b)