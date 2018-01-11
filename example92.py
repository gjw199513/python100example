# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 下午 2:05'

# 题目：时间函数举例2。

if __name__ == '__main__':
    import time

    start = time.time()
    for i in range(3000):
        print(i)
    end = time.time()

    print(end - start)