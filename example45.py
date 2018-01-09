# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 下午 3:26'

# 题目：统计 1 到 100 之和。

sum = 0
for i in range(1,101):
    sum += i

print("总数是："+str(sum))


# 通用版
print("---我是通用版---")


def sumsm(s,m,g):
    sum = 0
    if g == 0:
        for i in range(s, m+1):
            sum += i
    else:
        for i in range(s, m+1, g):
            sum += i
    print(sum)


s = int(input("请输入首项"))
m = int(input("请输入末项"))
g = int(input("请输入公差"))
sumsm(s, m, g)