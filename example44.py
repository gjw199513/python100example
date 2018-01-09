# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 下午 2:46'

# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
"""
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
"""
# 程序分析：创建一个新的 3 行 3 列的矩阵，使用 for 迭代并取出 X 和 Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。

X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
# 使用迭代
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)


# 使用map+列表解析
# 由于改列表为多维列表，本题并不是适合，但是在一维列表中，列表解析还是更加快捷的
print("使用map")

for i in range(len(result)):
    result = map(lambda x, y: x+y, X[i], Y[i])
    print([x for x in result])

