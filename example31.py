# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/8 0008 下午 4:50'

# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。

# 使用字典的特性进行优化，将字典中键进行切片，选出符合的字典值
letter1 = input("输入星期首字母:")
data = {"m": "Monday", "w": "Wednesday", "f": "Friday",
        "t": {"tu": "Tuesday", "th": "Thursday"}, "s": {"sa": "Saturday", "su": "Sunday"}}

if letter1 not in list(data.keys()):
    print("输入的首字母有误")

else:
    for key1, value1 in data.items():
        if letter1 == key1[0]:
            if isinstance(value1, str):
                print(str(key1)+":"+str(value1))
            else:
                letter2 = input("第一个字母有重复，请输入第二个字母:")
                for key2, value2 in value1.items():
                    if letter2 == key2[1]:
                        print(str(key2)+": "+str(value2))
                        break
                else:
                    print("第二个字母不在范围内")
