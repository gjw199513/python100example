# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 下午 3:44'

# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。
Flag = 1
print('如果输入的数字小于 50，程序将停止运行。')


def sq(x):
    return x*x


while Flag:
    n = int(input("请输入一个数字"))
    print("运算结果为"+str(sq(n)))

    if sq(n) < 50:
        Flag = 0
