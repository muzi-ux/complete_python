#! usr/bin/python
# -*- coding:utf-8 -*-
# lis = ['a', 'b', 'c', 'e']
# str1 = '-'.join(lis)
# print(str1)
# for i in lis:
#     print(i, sep="-", end="")

# 格式化字符串，吧列表变为字符串使用字符串方法 join()以 ’-‘连接 注意：列表内类型需要是字符串
# lis = ['2020', '10', '10', '21', '43']
# while True:
#     mi_input = input("请输入(输入0结束)：")
#     if mi_input == "0":
#         print(':'.join(lis))
#         break
#     else:
#         lis.append(mi_input)

# print 打印语句
# print('hello word !')
# print 打印语句结尾默认换行
# end='' 打印语句的结尾不进行换行，
# print('hello', end=' ')  # 打印语句以空格结束，end='xxx' 引号内部所放的内容会出现在该打印语句的最后
# print('word !', end='\n')
#
# name = '木子'
# age = 18
# print(name, age, sep='-')  # sep='xx' 引号内的符号会作为打印语句的连接符
#
# name = '张二狗'
# age = 18
# print(name, age, sep="-")

# import pymssql

# conn = pymssql.connect('DESKTOP-SPKTIB1\SQLEXPRESS', 'sa', '123456', 'student')
# # if conn:
# #     print('链接成功')
# # conn.close()


# def conn():
#     connect = pymssql.connect(server=r'DESKTOP-SPKTIB1\SQLEXPRESS', user=r'sa', password='123456', database='mi')
#     if connect:
#         print('链接成功！')
#     return connect


# login_timeout=10,
# charset="UTF-8"
# serve=r'SQLEXPRESS',
# conn()
#
# age = input("请输入年龄").77
# print(type(age))

