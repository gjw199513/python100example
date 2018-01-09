# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = 'r018/1/9 0009 上午 11:09'

# 题目：求一个r*r矩阵主对角线元素之和。

# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。

r = int(input("请输入矩阵的行列"))
l = []
sum = 0.0
for i in range(r):
    l.append([])
    for j in range(r):
        l[i].append(float(input("请对应输入值：")))


for i in range(r):
    sum += l[i][i]
print(sum)