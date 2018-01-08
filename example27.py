# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/8 0008 下午 3:05'

# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def output(s, l):
    if l == 0:
        return
    else:
        print(s[l-1])
        output(s, l-1)


s = input("输入字符串")
l = len(s)
output(s, l)


# 不是用递归
print("不使用递归")
li = list(s)
li.reverse()
for i in range(0, len(li)):
    print(li[i])
