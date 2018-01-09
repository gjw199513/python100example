# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 上午 11:54'

# 题目：将一个数组逆序输出。
# 程序分析：用第一个与最后一个交换。

a = [9, 6, 5, 4, 1]
l = len(a)
print(a)
for i in range(int(l/2)):
    a[i], a[l-i-1] = a[l-i-1], a[i]

print("交换之后:"+str(a))

# 使用reverse
a = [9, 6, 5, 4, 1]
a.reverse()
print(a)