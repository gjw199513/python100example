# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 上午 10:25'

# 题目：求100之内的素数。
# 素数求解通用方法
lower = int(input("输入区间最小值:"))
upper = int(input("输入区间最大值:"))

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
