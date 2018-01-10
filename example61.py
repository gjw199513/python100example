# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/10 0010 上午 11:07'

# 题目：打印出杨辉三角形（要求打印出10行如下图）。　

if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append([])
        for j in range(10):
            a[i].append(0)

    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1

    for i in range(2, 10):
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]

    for i in range(10):
        for j in range(i+1):
            print(str(a[i][j]), end=" ")
        print()

# 递归
print("我是递归方法")
n = 10


def lst(i, j):
    if i == j or j == 1:
        return 1
    else:
        return lst(i-1, j-1)+lst(i-1, j)


for i in range(1, n+1):
    for j in range(1, i+1):
        print(lst(i, j),end=" ")
    print()