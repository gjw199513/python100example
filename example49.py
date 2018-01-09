# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 下午 4:05'

# 题目：使用lambda来创建匿名函数。

# 运用了布尔值为假时，其结果与0相等
MAXIMUM = lambda x, y:  (x > y) * x + (x < y) * y
MINIMUM = lambda x, y:  (x > y) * y + (x < y) * x

a = 10
b = 20
print('The largar one is '+str(MAXIMUM(a,b)))
print('The lower one is '+str(MINIMUM(a,b)))