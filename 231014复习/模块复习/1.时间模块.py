#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/4

# time模块
# 1.获取当前时间戳
import time, datetime
print(time.localtime())
print(time.strptime('2019-06-23 12:53:26', '%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y-%m-%d'))
print(time.strftime('%Y-%m-%d', time.localtime()))
print(time.asctime())
print(datetime.datetime(2019, 6, 23, 12, 37, 59, 45))

# v1 = time.time()
# print(v1)

# 2. 获取当前时区
# v2 = time.timezone
# print(v2)

# 3.获取当前时间戳
# v3 = time.mktime(time.localtime())
# print(v3)

# datetime模块

from datetime import datetime, timedelta, timezone

# # 1.获取当前时间
# v1 = datetime.now()
# print(v1)
#
# # 获取东7区的时间
# v2 = timezone(timedelta(hours=7))
# v3 = datetime.now(v2)
# print(v3)
#
# # 获取当前UTC时间，世界标准时间
# v4 = datetime.utcnow()
# print(v4)
#
# v5 = datetime.now()
# print(v5)
#
# v6 = v5 + timedelta(days=10, minutes=5)
# print(v6)

# 2.字符串与datetime之间的转换
# text = "2021-11-11"
# v1 = datetime.strptime(text, '%Y-%m-%d')
# print(v1)  # 2021-11-11 00:00:00

# datetime格式--->转换为字符串格式
# v1 = datetime.now()
# v2 = v1.strftime("%Y-%m-%d %X")
# print(v2)
# print(type(v2))

# 3.时间戳与datetime之间的转换
# import time
# from datetime import datetime
# ctime = time.time()
# print(ctime)  # 1623923966.2895925
# v1 = datetime.fromtimestamp(ctime)
# print(v1)  # 2021-06-17 17:59:26.289593
# print(type(v1))  # <class 'datetime.datetime'>

