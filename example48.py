# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 下午 3:59'

# 题目：数字比较。

x = int(input("请输入第一个数"))
y = int(input("请输入第一个数"))

if x > y:
    print(str(x)+"大于"+str(y))
elif x == y:
    print(str(x)+"等于"+str(y))
else:
    print(str(x)+"小于"+str(y))