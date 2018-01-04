# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/4 0004 下午 4:03'

# 题目：暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。
import time

data = {1: 'a', 2: 'b'}
for key, value in dict.items(data):
    print(key, value)
    time.sleep(1)