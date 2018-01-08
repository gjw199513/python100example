# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/8 0008 上午 10:51'

# 题目：打印出如下图案（菱形）:
"""
   *
  ***
 *****
*******
 *****
  ***
   *   
"""
# 程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。
import math
r = int(input("打印几(奇数)行的菱形"))
if r%2 == 0:
    print("输入必须为奇数")
else:
    c = math.ceil(r/2)
    f = math.floor(r/2)
    for i in range(c):
        for j in range(c-1-i, 0, -1):
            print(" ", end="")
        for k in range(2*i+1):
            print("*", end="")
        print()
    for i in range(f):
        for j in range(0, i+1):
            print(" ", end="")
        for k in range(2*(f-i-1)+1):
            print("*", end="")
        print()
