#! usr/bin/python
# -*- coding:utf-8 -*-
import pymssql

"""
掷骰子
1、欢迎进入游戏
2、输入用户名密码进入游戏，默认是没有币的
3、提示用户充值买币（100块钱3个币，充值必须是100的倍数，充值不成功可以再次充值）
4、玩一局需要扣除2个币，猜大小（系统产生随机数）
5、只要猜对了奖励1个币，可以继续玩，也可以主动退出，或者没有币强制退出
"""

print('*' * 10 + '欢迎进入掷骰子游戏' + '*' * 10)
# 用户名
username = ""
# 密码
password = ""

for i in range(3):
    username = input("请输入用户名:")
    password1 = input("请输入密码:")
    # server    数据库服务器名称或IP
    # user      用户名
    # password  密码
    # database  数据库名称
    server = 'DESKTOP-SPKTIB1'
    user = 'sa'
    password = '<LRZ+com-123>'
    database = 'username'
    conn = pymssql.connect(server, user, password, database)
    print(conn)
    if username == username and password == password1:
        print("\t\t", end="")
        print('*' * 5 + "欢迎进入游戏" + '*' * 5)
        break
    else:
        print("账户或密码错误！")
else:
    print("输入错误三次，账户已被锁定，请三分钟后尝试1")
