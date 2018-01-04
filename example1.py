# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/3 0003 上午 10:07'
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。


# 1.基础版
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print(i, j, k)


# 2.列表解析
l_num = [1, 2, 3, 4]

ls = [i*100 + j *10 + k for i in l_num for j in l_num for k in l_num if(j != k and j != i and i != k)]
print(ls)

