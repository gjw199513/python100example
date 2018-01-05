# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/5 0005 上午 10:48'

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""
程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
"""
from math import sqrt,isnan
def reduceNum(n):
    if not isinstance(n, int) or n<=0:
        print("您输入的数字有误")
        exit(0)
    else:
        l = []
        r = n
        if n == 1:
            print(1, end="")
        while r not in [1]:
            for i in range(2, int(n/2)+1):
                if r%i == 0:
                    r /= i
                    l.append(i)
                    break
            if r == n:
                l = [1,r]
                r = 1


        l = sorted(l)

        for i, v in enumerate(l):
            if i == 0:
                print(str(n)+" = "+ str(v),end="")
            else:
                print(" * " + str(v),end="")


reduceNum(64)


