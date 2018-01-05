# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/5 0005 下午 3:58'

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# 程序分析：利用while语句,条件为输入的字符不为'\n'。


import string
word = input("输入字符串")
l = 0
s = 0
d = 0
o = 0
for c in word:
    if c.isalpha():
        l += 1
    elif c.isspace():
        s += 1
    elif c.isdigit():
        d += 1
    else:
        o += 1

print("字符串："+str(l)+",空格："+str(s)+"，数字："+str(d)+"其他字符："+str(o))


# 列表
InPut = input('输入任意字符:')
letters = []
spaces = []
digits = []
others = []
for i in iter(InPut):
    if i.isalpha():
        letters.append(i)
    elif i.isspace():
        spaces.append(i)
    elif i.isdigit():
        digits.append(i)
    else:
        others.append(i)
print('''
字母: {}, 个数: {};
空字符: {}, 个数: {};
数字: {}, 个数: {};
其他: {}, 个数: {}'''.format(letters, len(letters), spaces, len(spaces), digits, len(digits), others, len(others)))