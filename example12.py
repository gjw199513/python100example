# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/4 0004 下午 5:14'

# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
h = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(101, 201):
    k = int(sqrt(m+1))
    for i in range(2, k+1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print("{0:-4d}".format(m))
        h += 1

    leap = 1
print("The total is"+str(h))

# 集合法
print("我是新方法")
l = []
for i in range(101, 200):
    k = int(sqrt(i+1))
    for j in range(2, k):
        if i%j == 0:
            break
    else:
        l.append(i)

print(l)
print("总数为:"+str(len(l)))