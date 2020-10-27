#! usr/bin/python
# -*- coding:utf-8 -*-
"""
掷骰子
1、欢迎进入游戏
2、输入用户名密码进入游戏，默认是没有币的
3、提示用户充值买币（100块钱3个币，充值必须是100的倍数，充值不成功可以再次充值）
4、玩一局需要扣除2个币，猜大小（系统产生随机数）
5、只要猜对了奖励1个币，可以继续玩，也可以主动退出，或者没有币强制退出
"""


def countdown(time_left):
    """
    倒计时函数
    :param time_left: 倒计时秒数
    :return: True
    """
    import time
    while time_left > 0:
        time.sleep(1)
        second = time_left % 60
        minute = time_left // 60
        time_left = time_left - 1
        print("%d分钟%d秒" % (minute, second))
    return True


def main():
    # 游戏币的数量
    game_currency = 2
    print('*' * 10 + '欢迎进入掷骰子游戏' + '*' * 10)
    username1 = "admin"
    for i in range(3):
        username = input("请输入用户名:")
        password1 = input("请输入密码:")
        if username1 == username and password1 == password1:
            print("\t\t", end="")
            print('*' * 5 + "欢迎进入游戏" + '*' * 5)
            if game_currency <= 2:
                game_currency = money(game_currency)
                if game_currency == 0:
                    print('游戏结束，再见!')
                    return None
            else:
                game_currency = game(game_currency)
            break
        else:
            print("账户或密码错误！")
    else:
        print("输入错误三次，账户已被锁定，请三分钟后尝试!")
        return None


def money(time):
    """
    充值函数
    :param time: 剩余的游戏币数量
    :return: 充值的游戏币数量
    """
    while True:
        print('亲爱的玩家，你的游戏币不足了，请充值后继续游戏！')
        moneys = float(input('请输入你要充值的金额\n(必须是100的倍数,输入零表示退出游戏)：'))
        if moneys == 0:
            return 0
        if moneys % 100 == 0:
            print('充值成功！')
            return (moneys / 100) * 3
        else:
            print('充值失败！')


def game(time):
    """
    游戏竞猜
    :param time:游戏币数量
    :return: 剩余游戏币数量
    """
    import random
    while True:
        print('游戏开始，猜大小！')
        time -= 2
        mum = float(input('请输入你要竞猜的数字(必须是整数):'))
        sums = random.randint(1, 6)
        if mum == sums:
            print('竞猜正确恭喜您，获得三个币的奖励！\n结果为：%d' % sums)
            time += 3
        else:
            print('再接再厉，下一把说不定有好运!\n结果为：%d' % sums)
        if time <= 2:
            return time
        carry_on = input('是否继续游戏（y/n):')
        if carry_on == 'n':
            return time


if __name__ == '__main__':
    while True:
        main()
        countdown(180)
