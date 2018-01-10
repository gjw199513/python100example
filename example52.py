# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/10 0010 上午 9:34'

# 题目：学习使用按位或 | 。
# 程序分析：0|0=0; 0|1=1; 1|0=1; 1|1=1

if __name__ == '__main__':
    a = 77
    b = a | 3
    print('a | b is %d' % b)
    b |= 7
    print('a | b is %d' % b)
