# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 上午 9:48'

# 题目：练习函数调用。


def hello_world():
    print('hello world')


def three_hellos():
    for i in range(3):
        hello_world()


if __name__ == '__main__':
    three_hellos()
