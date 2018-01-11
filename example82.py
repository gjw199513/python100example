# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 上午 10:35'

# 题目：八进制转换为十进制

n = 0
p = input('input a octal number:\n')
for i in range(len(p)):
    n = n * 8 + ord(p[i]) - ord('0')
print(n)

# 内置函数
if __name__ == '__main__':
    n = 0
    p = input("输入一个八进制数：")
    p = int(p, 8)
    print(p)

