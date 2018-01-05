# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/4 0004 下午 4:35'
# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
import time
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21...(类似斐波那契数列)
f1 = 1
f2 = 1
# 基本方法
for i in range(1, 22):
    print(f1, f2, end=" ")
    f1 = f1 + f2
    f2 = f1 + f2

# 递归
print("我是递归")
print(time.localtime())


def r(n):
    if n == 1 or n == 2:
        return 1
    return r(n-1)+r(n-2)


for i in range(1,36):
    print(r(i))

print(time.localtime())

# 优化方法
print("我是优化方法")
print(time.localtime())


def fib3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


# 输出前 10 个斐波那契数列
print(fib3(36))
print(time.localtime())