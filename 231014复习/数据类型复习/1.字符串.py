#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/10/14

#  打印1-10，不打印7
# for i in range(1, 10):
#     if i == 7:
#         pass
#     else:
#         print(i)

# count = 0
# while count < 11:
#     if count != 7:
#         print(count)
#     count += 1

# count = 0
# while count < 11:
#     if count == 7:
#         count += 1
#         continue
#     print(count)
#     count += 1

count = input("请输入内容：")
index = 0
total = 0
while True:
    val = count[index]
    value = val.isdigit()
    if value:
        total += 1
    elif index +1 == len(count):
        print("共输入{}个字符".format(len(count)))
        break
    index += 1
print("共输入{}个数字".format(total))
