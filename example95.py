# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 下午 2:16'

# 题目：字符串日期转换为易读的日期格式。

from dateutil import parser
dt = parser.parse("Aug 28 2015 12:00AM")
print(dt)