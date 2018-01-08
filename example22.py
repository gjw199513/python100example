# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/8 0008 上午 9:46'

# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 通用版
for i in range(ord('x'), ord('z') + 1):
    for j in range(ord('x'), ord('z') + 1):
        if i != j:
            for k in range(ord('x'), ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s\t b -- %s\tc--%s' % (chr(i), chr(j), chr(k)))


# 进阶版
p1 = ['a','b','c']
p2 = []

for i in range(3):
    if p1[i] != 'a' and p1[i] != 'c':
        p2.insert(i,'x')
    elif p1[i] != "c":
        p2.insert(i,'z')
    else:
        p2.insert(i,'y')

print("a---"+p2[0]+" b---"+p2[1]+" c---"+p2[2])

