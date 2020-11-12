# def fibonacci(i):
#     if i == 2 or i == 1:
#         return 1
#     return fibonacci(i - 2) + fibonacci(i - 1)
#
#
# print(fibonacci(20))


# lis = []
# for i in range(25):
#     lis.append(50 + i + 1)
#
# print(lis)
# print(len(lis))
# print(sum(lis))


# def my_sum(m, b):
#     return m + b
#
#
# def sum1(z, n):
#     return my_sum(z, n)
#
#
# print(sum1(1, 4))

def external():
    print('我是外部函数')

    def internal():  # 在函数外部是没有办法调用函数呢部的变量的
        print('我是内部函数')

    return internal


external()  # 我是外部函数

internal = external()
internal()  # 我是内部函数
