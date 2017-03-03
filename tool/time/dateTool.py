# coding:utf-8

import calendar
import time
from datetime import datetime, timedelta

__author__ = 'hzliyong'

format = '%Y-%m-%d'

#毫秒转化成日期
def from_millsecond(millsecond, format = '%Y-%m-%d'):
    t = time.localtime(millsecond)
    return time.strftime(format, t)

#该月的最后一天
def last_day_of_month(date, format = format):
    date = datetime.strptime(date, format)#strptime为将字符串日期转化成日期类型的日期的函数
    day, num_days = calendar.monthrange(date.year, date.month)
    return datetime(date.year, date.month, num_days).strftime(format)

#日期加days天
def add_days(current_date, days = 1, format = format):
    current_time = datetime.strptime(current_date, format)
    step = timedelta(days = days)
    current_time = current_time + step
    return current_time.strftime(format)

#date对应的那周的最后一天
def last_day_of_week(date, format = format):
    day = datetime.strptime(date, format).weekday()#weekday函数计算date为本周的第几天，从0开始
    return add_days(date, 6 - day)

#date所属周的第一天日期
def first_day_of_week(date, format = format):
    day = datetime.strptime(date, format).weekday()
    return add_days(date, -day)

#date所属月份的第一天的日期
def first_day_of_month(date, format = format):
    date = datetime.strptime(date, format)
    return datetime(date.year, date.month, 1).strftime(format)


if __name__ == "__main__":
    date = '2017-03-03'
    print(from_millsecond(1393840876.583188))
    print(last_day_of_month(date))
    print(add_days(date, 2, format))
    print(last_day_of_week(date, format))
    print(first_day_of_week(date, format))
    print(first_day_of_month(date, format))

