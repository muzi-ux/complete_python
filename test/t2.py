a = 100


def main():
    global a  # global 关键字声明这里的a是全局变量
    a = 10
    s = 9
    print(a, s)  # 10


print(a)  # 10
print("全局变量有{} 局部变量有{}".format(globals(), locals()))
