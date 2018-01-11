# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 上午 9:38'

# 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
# 当输入n为奇数时，调用函数1/1+1/3+...+1/n


def ieven(n):
    s = 0.0
    for i in range(2, n+1, 2):
        s += 1.0 / i
    return s


def iodd(n):
    s = 0.0
    for i in range(1, n+1, 2):
        s += 1.0 / i
    return s


def call(fn, n):
    s = fn(n)
    return s


if __name__ == "__main__":
    n = int(input("输入一个数：\n"))
    if n % 2 == 0:
        sum = call(ieven, n)
    else:
        sum = call(iodd, n)
    print(sum)