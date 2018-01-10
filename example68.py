# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/10 0010 下午 2:40'

# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

if __name__ == '__main__':
    n = int(input('整数 n 为:\n'))
    m = int(input('向后移 m 个位置为:\n'))


    def move(array, n, m):
        array_end = array[n - 1]
        for i in range(n - 1, -1, - 1):
            array[i] = array[i - 1]
        array[0] = array_end
        m -= 1
        if m > 0: move(array, n, m)


    a = []
    for i in range(n):
        a.append(int(input('输入一个数字:\n')))
    print('原始列表:', a)

    move(a, n, m)

    print('移动之后:', a)


# 使用切片完成（有问题）
print("使用切片完成")
b = a[m:len(a)]+a[0:m]
print(b)
if 2*m > len(a):
    c = b[len(a)-2*m:]
    b[len(a)-2*m:] = []
    b = c+b
else:
    c = b[len(a)-2*m:]
    b[len(a)-2*m:] = []
    b = b+c
print(b)
