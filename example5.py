# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/4 0004 下午 2:33'

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

l = []
for i in range(3):
    x = int(input('请输入整数'))
    l.append(x)
l.sort()
print(l)

# 加入x，y，z标志
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
a = {'x': x, 'y': y, 'z': z}
for w in sorted(a, key=a.get):
    print(w, a[w])