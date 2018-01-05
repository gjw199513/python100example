# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/5 0005 下午 2:49'

# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

# 程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。

score = int(input("输入分数:"))

if score >= 90:
    g = "A"
elif score >= 60:
    g = "B"
else:
    g = "C"

print("属于"+g)

# 进阶
print('A' if score > 89 else ('B' if score > 59 else 'C'))

# print('A' and score > 89 or 'B' and score > 59 or 'C')