# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/8 0008 下午 3:38'

# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

# 程序分析：学会分解出每一位数。
x = input("请输入一个不多于五位数的整数")
ix = int(x)
a = int(ix/10000)
b = int(ix % 10000/1000)
c = int(ix % 1000/100)
d = int(ix % 100/10)
e = int(ix % 10)

if a != 0:
    print("五位数：", e, d, c, b, a)
elif b != 0:
    print("四位数：", e, d, c, b, )
elif c != 0:
    print("三位数：", e, d, c)
elif d != 0:
    print("两位数：", e, d)
else:
    print("一位数：", e)


# 列表方式
print("我是进阶版")
print(str(len(x))+"位数：", end="")
for i in range(len(x)-1, -1, -1):
    print(x[i], end=" ")
