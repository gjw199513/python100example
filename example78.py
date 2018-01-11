# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 上午 9:46'

# 题目：找到年龄最大的人，并输出。请找出程序中有什么问题。
if __name__ == '__main__':
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}

    for key, value in person.items():
        if value == max(person.values()):
            print(key, value)

