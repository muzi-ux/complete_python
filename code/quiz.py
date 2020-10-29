#! usr/bin/python
# -*- coding:utf-8 -*-
"""
掷骰子 v1.1
1、欢迎进入游戏
2、输入用户名密码进入游戏，默认是没有币的
3、提示用户充值买币（100块钱3个币，充值必须是100的倍数，充值不成功可以再次充值）
4、玩一局需要扣除2个币，猜大小（系统产生随机数）
5、只要猜对了奖励1个币，可以继续玩，也可以主动退出，或者没有币强制退出
"""


# 主函数,负责调用函数执行功能
def main():
    pass


# 身份验证函数，主要负责用户的身份验证，读取用户的用户名，游戏币等信息
def authentication(name, password):
    # 导入需要使用的第三方包
    from openpyxl import load_workbook
    # 创建文件对象
    server = load_workbook('../test/server.xlsx')
    # 操作一个页面
    sheet = server['Sheet1']
    # 创建布尔变量控制while循环
    bol = True
    # 计数器
    i = 1
    # 操作的单元格
    cell = 'A'
    cells = 'B'
    cell1 = 'C'
    while bol:
        cell = cell + str(i)
        cells = cells + str(i)
        cell1 = cell1 + str(i)
        if password == sheet[cells].value and sheet[cell].value == name:
            print('登录成功！')
            server.close()
            return sheet[cell1].value
        else:
            i += 1
            txt = sheet[cell].value
            if txt == None:
                bol = False
                print('用户名或密码错误！')
                server.close()


# 注册函数
def registered():
    import re
    from openpyxl import load_workbook
    # .{4-6}
    while True:
        name = input('请输入用户名(4-6个字符)：')
        password = input('请输入密码：')
        result = re.search(r'.{4,6}', name)
        if result != None:
            server = load_workbook('../test/server.xlsx')
            sheet = server['Sheet1']
            # 创建布尔变量控制while循环
            bol = True
            # 计数器
            i = 1
            # 操作的单元格
            cell = 'A'
            cells = 'B'
            cell1 = 'C'
            while bol:
                cell = cell + str(i)
                cells = cells + str(i)
                if sheet[cell].value == None:
                    sheet[cell].value = name
                    sheet[cells].value = password
                    print('注册成功！')
                    server.save('../test/server.xlsx')
                    server.close()
                    return None
                else:
                    i += 1


# 充值函数，负责用户的充值
def recharge():
    pass


# 游戏函数，负责游戏的进行，当游戏币不足是退出，用户主动退出
def game():
    pass


# 程序入口
if __name__ == '__main__':
    authentication('测试用户3', '1234')
