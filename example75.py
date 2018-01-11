# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 上午 9:37'

# 题目：放松一下，算一道简单的题目。

if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1: n += 1
        if i == 3: n += 1
        if i == 4: n += 1
        if i != 4: n += 1
        if n == 3: print(64 + i)