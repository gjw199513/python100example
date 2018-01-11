# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 上午 10:00'

"""
题目：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
"""

if __name__ == "__main__":
    i = 0
    j = 1
    x = 0
    while i < 5:
        x = 4 * j
        for i in range(0, 5):
            if x % 4 != 0:
                break
            else:
                i += 1
            # 总共桃子的数目
            x = (x/4) * 5 + 1
        j += 1
    print(int(x))

# 使用递归
num = int(input("输入猴子的数目:"))


def fn(n):
    if n == num:
        return 4 * x  # 最后剩的桃子的数目
    else:
        return fn(n + 1) * 5 / 4 + 1


x = 1
while 1:
    count = 0
    for i in range(1, num):
        if fn(i) % 4 == 0:
            count = count + 1
    if count == num - 1:
        print("海滩上原来最少有%d个桃子" % int(fn(0)))
        break
    else:
        x = x + 1