# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 下午 2:41'

# 题目：列表转换为字典

i = ['a', 'b']
l = [1, 2]
print(dict([i,l]))

i = ['a', 'b', 'c']
l = [1, 2, 3]
b = dict(zip(i, l))
print(b)