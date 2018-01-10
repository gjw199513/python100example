# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/10 0010 下午 2:25'

# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

a=[32,121,232154,12265,133,121]

for i in range(len(a)):
    if a[i] == max(a):
        a[0], a[i] = a[i], a[0]

for i in range(len(a)):
    if a[i] == min(a):
        a[len(a)-1], a[i] = a[i], a[len(a)-1]

print(a)


# 使用列表内置的函数
print("我是函数使用")

# 最小的放到最后
min = min(a)
a.remove(min)
a.append(min)
# 最大的放到最前面
max = max(a)
a.remove(max)
a.insert(0,max)
print(a)