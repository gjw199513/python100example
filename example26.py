# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/8 0008 下午 2:31'

# 题目：利用递归方法求5!。

# 程序分析：递归公式：fn=fn_1*4!


def fact(x):
    i = 0
    if x == 0:
        i = 1
    else:
        i = x * fact(x-1)
    return i


for i in range(8):
    print(str(i)+"!="+str(fact(i)))
