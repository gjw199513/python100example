# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 上午 9:32'

# 题目：反向输出一个链表。
if __name__ == "__main__":
    s = []
    for i in range(5):
        num = int(input("请输入数字\n"))
        s.append(num)
    print(s)
    s.reverse()
    print(s)