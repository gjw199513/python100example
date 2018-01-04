# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/4 0004 下午 4:15'

# 题目：暂停一秒输出，并格式化当前时间。

import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))