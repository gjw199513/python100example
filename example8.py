# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/4 0004 下午 3:50'

# 题目：输出 9*9 乘法口诀表。
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。

for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j))

# 优化
print("我是格式打印的")
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end='   ')