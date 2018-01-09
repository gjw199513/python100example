# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 下午 3:50'

# 题目：两个变量值互换。


def change(a, b):
    a, b = b, a
    return a, b


if __name__ == '__main__':
    x = int(input("输入第一个数"))
    y = int(input("输入第二个数"))
    print("x="+str(x)+", y="+str(y))
    x, y = change(x, y)
    print("x="+str(x)+", y="+str(y))