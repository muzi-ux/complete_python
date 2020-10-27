import os
import pypinyin

# 设置创建后文件夹存放的位置
path = './test/tt1/'

lis = []


def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s


# 这里创建10个文件夹
for i in lis:
    # *定义一个变量判断文件是否存在,path指代路径,str(i)指代文件夹的名字*
    isExists = os.path.exists(str(i))
    # 判断如果文件不存在,则创建
    if not isExists:
        os.makedirs(path + str(i))
        # print("%s 目录创建成功"%i)
    else:
        print("%s 目录已经存在" % i)
        # 如果文件不存在,则继续上述操作,直到循环结束
        continue
    print(i + pinyin(i))
