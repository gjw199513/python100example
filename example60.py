# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/10 0010 上午 10:40'

# 题目：计算字符串长度。

s = input("输入字符串")
print("该字符串长度为："+str(len(s)))

# 第二种
print("第二种方法")
print("该字符串长度为："+str(s.__len__()))