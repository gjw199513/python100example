# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/5 0005 下午 4:13'

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制

# 程序分析：关键是计算出每一项的值。
from functools import reduce

T = 0
s = []
n = int(input('n='))
a = int(input('a='))
for count in range(n):
    T += a
    a *= 10
    s.append(T)
    print(T)

s = reduce(lambda x, y: x+y, s)

print("计算总和为:", s)