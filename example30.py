# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/8 0008 下午 3:57'

# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

x = input("请输入一个数")
flag = True
l = len(x)-1
for i in range(int(len(x)/2)):
    if x[i] != x[l-i]:
        flag = False

if flag:
    print(x+"是回文数")
else:
    print(x+"不是回文数")
