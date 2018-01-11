# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 上午 9:34'

# 题目：列表排序及连接。
# 程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]

    a.sort()
    print(a)
    # 连接列表a与b
    print(a+b)

    # 连接列表a与b
    a.extend(b)
    print(a)
