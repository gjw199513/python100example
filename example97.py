# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 下午 2:24'

# 题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

filename = input("输入文件名")
fp = open(filename, 'w')
ch = input("输入字符串：")
while ch != "#":
    fp.write(ch)
    print(ch, end="")
    ch = input("输入字符串：")
fp.close()