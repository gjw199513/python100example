# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/4 0004 下午 1:49'

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
year = int(input('年:'))
month = int(input('月:'))
day = int(input('日:'))


days = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sum = days[month-1]
else:
    print("您输入的月份有误")

sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('这一天是:第'+str(sum)+'天')


print("我是新版")
months1 = (0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366)  # 闰年
months2 = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365)  # 平年

if ((year%4==0)and(year%100!=0)) or (year%400 == 0):
    date = months1[month-1]+day
else:
    date = months2[month-1]+day

print("是该年的第"+str(date)+"天")