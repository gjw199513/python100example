# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 上午 9:26'

# 按相反的顺序输出列表的值。
a = ["a", "b", "c"]
for i in a[::-1]:
    print(i)

# 不是使用循环
b = a[::-1]
print(b)