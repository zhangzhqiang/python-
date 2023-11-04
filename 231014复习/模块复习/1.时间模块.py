#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/4

# time模块
# 1.获取当前时间戳
import time

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

# 1.获取当前时间
v1 = datetime.now()
print(v1)

# 获取东7区的时间
v2 = timezone(timedelta(hours=7))
v3 = datetime.now(v2)
print(v3)

# 获取当前UTC时间
v4 = datetime.utcnow()
print(v4)

