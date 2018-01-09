# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 下午 2:31'

# 题目：模仿静态变量(static)另一案例。
# 程序分析：演示一个python作用域使用方法


class Num:
    nNum = 1

    def inc(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)


if __name__ == '__main__':
    # 创建了同一个实例
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print('The num = %d' % nNum)
        inst.inc()
    print(Num.nNum)

    # 创建多个实例
    print("---创建多个实例---")
    for i in range(3):
        inst1 = Num()
        nNum += 1
        print('The num = %d' % nNum)
        inst1.inc()
    print(Num.nNum)