# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/9 0009 下午 2:05'

# 题目：模仿静态变量的用法。


def varfunc():
    # 函数中var变量是局部变量，调用函数，不会改变var的值
    var = 0
    print('var = %d' % var)
    var += 1


if __name__ == '__main__':
    for i in range(3):
        varfunc()

# 类的属性
# 作为类的一个属性吧


class Static:
    StaticVar = 5

    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)


# 类属性是不变的
# 调用方法只会让变量在方法中输出发生改变，并不会改变类属性的值
print("aa:"+str(Static.StaticVar))
a = Static()
for i in range(3):
    a.varfunc()
print("aa:"+str(Static.StaticVar))