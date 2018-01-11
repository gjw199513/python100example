# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 上午 11:08'

# 题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

if __name__ == '__main__':
    n = int(input('输入一个数字'))

    i = 1
    sum = 9
    while 1:
        if sum % n == 0:
            break
        sum += 10**i*9
        i += 1

    print(str(i)+"个9可以被"+str(n)+"整除："+str(sum))
    r = sum / n
    print(str(sum)+"/"+str(n)+"="+str(int(r)))


    # while