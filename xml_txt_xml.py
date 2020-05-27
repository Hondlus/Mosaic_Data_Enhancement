import os

xml_dir='/home/hongliang/PycharmProjects/hebin_txt/'

def xml_to_txt():
    files = os.listdir(xml_dir)  # 列出当前目录下所有的文件

    for filename in files:
        portion = os.path.splitext(filename)  # 分离文件名字和后缀
        print(portion)

        if portion[1] == ".xml":  # 根据后缀来修改,如无后缀则空
            newname = portion[0] + ".txt"  # 要改的新后缀
            os.chdir(xml_dir)  # 切换文件路径,如无路径则要新建或者路径同上,做好备份
            os.rename(filename, newname)

def txt_to_xml():
    files = os.listdir(xml_dir)  # 列出当前目录下所有的文件

    for filename in files:
        portion = os.path.splitext(filename)  # 分离文件名字和后缀
        print(portion)

        if portion[1] == ".txt":  # 根据后缀来修改,如无后缀则空
            newname = portion[0] + ".xml"  # 要改的新后缀
            os.chdir(xml_dir)  # 切换文件路径,如无路径则要新建或者路径同上,做好备份
            os.rename(filename, newname)

#xml_to_txt()
txt_to_xml()