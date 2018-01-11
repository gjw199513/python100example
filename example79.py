# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 上午 9:56'

# 题目：字符串排序。

if __name__ == "__main__":
    str1 = input("请输入字符串")
    str2 = input("请输入字符串")
    str3 = input("请输入字符串")
    print(str1, str2, str3)

    l = []
    l.extend([str1, str2, str3])
    l.sort()
    print(l)