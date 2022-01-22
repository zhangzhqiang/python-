#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2022-01-03

"""请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li＝[‘alex’, ‘eric’, ‘rain’]"""
li = ['alex', 'eric', 'rain']
print("_".join(li))

"""查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。

li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}"""

li = ["alec", " aric", "Alex", "Tony", "rain"]
for i in li:
    new_i = i.replace(" ", "")
    if new_i.startswith("a") or new_i.startswith("A") and new_i.endswith("c"):
        print(new_i)

tu = ("alec", " aric", "Alex", "Tony", "rain")
for i in tu:
    new_i = i.replace(" ", "")
    if new_i.startswith("a") or new_i.startswith("A") and new_i.endswith("c"):
        print(new_i)

dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
for key in dic:
    new_dic = dic[key].replace(" ", "")
    if new_dic.startswith("a") or new_dic.startswith("A") and new_dic.endswith("c"):
        print(new_dic)


"""
li＝[‘alex’, ‘eric’, ‘rain’]

计算列表长度并输出

- 列表中追加元素“seven”，并输出添加后的列表
- 请在列表的第1个位置插入元素“Tony”，并输出添加后的列表
- 请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
- 请删除列表中的元素“eric”，并输出修改后的列表
- 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
- 请删除列表中的第3个元素，并输出删除元素后的列表
- 请删除列表中的第2至4个元素，并输出删除元素后的列表
- 请将列表所有的元素反转，并输出反转后的列表
- 请使用for、len、range输出列表的索引
- 请使用enumrate输出列表元素和序号（序号从100开始）
- 请使用for循环输出列表的所有元素
"""

li = ['alex', 'eric', 'rain']
li.append("seven")
li.insert(1, "Tony")
li.insert(2, "Kelly")
li.remove("eric")
print(li.pop(2))
li.pop(3)

li = ["ale", "eric", "rain", "alex", "luffy", "py"]
del li[2:4]

li.reverse()
for index in range(len(li)):
    print(index, li[index])

for index, i in enumerate(li, 100):
    print(index, i)

for i in li:
    print(i)

"""写代码，有如下列表，请按照功能要求实现每一个功能

li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]


"""
li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
# 1.请根据索引输出“Kelly
print(li[2][1][1])
# 2.请使用索引找到’all’元素并将其修改为“ALL”，如：li[0][1][9]…
print(li[2][2].upper())

"""tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
- 讲述元组的特性
- 请问tu变量中的第一个元素“alex”是否可被修改？
- 请问tu变量中的”k2”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
- 请问tu变量中的”k3”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven“
"""

# 元祖本身不可变，有序，如果存在可变元素则可变
# 不可被修改
# 列表，可以修改，
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
tu[1][2]["k2"].append("Seven")
print(tu[1][2]["k2"])
# 元祖，不可被修改
print(type(tu[1][2]["k3"]))


"""
转换

将字符串s = “alex”转换成列表

将字符串s = “alex”转换成元祖

将列表li = [“alex”, “seven”]转换成元组

将元组tu = (‘Alex’, “seven”)转换成列表

将列表li = [“alex”, “seven”]转换成字典且字典的key按照10开始向后递增"""

s = "alex"
print(list(s))
print(tuple(s))
#
li = ["alex", "seven"]
print(tuple(li))
#
tu = ("alex", "seven")
print(list(tu))
#
li = ["alex", "seven"]
dic = {}
for index, i in enumerate(li, 10):
    dic[index] = i
print(dic)


"""元素分类

有如下值列表[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。

即：{‘k1’:大于66的所有值, ‘k2’:小于66的所有值}。（编程题）

"""
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dic = {"k1": [], "k2": []}
l1 = []
l2 = []
for i in li:
    if i > 66:
        dic["k1"].append(i)
    dic["k2"].append(i)
print(dic)

"""在不改变列表数据结构的情况下找最大值li = [1,3,2,7,6,23,41,243,33,85,56]"""
li = [1, 3, 2, 7, 6, 23, 41, 243, 33, 85, 56]
max_val = li[0]

for i in li:
    if max_val < i:
        max_val = i
print(max_val)


l1 = [1, 3, 2, 7, 6, 23, 41, 243, 33, 85, 56]
l2 = [22, 44, 55, 66, 7, 23, 41, 243, 33, 85, 56]

new_li = []
old_li = []

for i in l1:
    if i not in l2:
        new_li.append(i)
    else:
        old_li.append(i)
print(new_li)
print(old_li)

"""在不改变列表中数据排列结构的前提下，找出以下列表中最接近最大值和最小值的平均值 的数
li = [-100,1,3,2,7,6,120,121,140,23,411,99,243,33,85,56]"""

li = [-100, 1, 3, 2, 7, 6, 142, 120, 121, 140, 23, 411, 99, 243, 33, 85, 56]
max_value = li[0]
min_value = li[0]
for i in li:
    if i > max_value:
        max_value = i
    elif i < min_value:
        min_value = i

avg_value = (max_value - min_value) / 2
avg_val = li[0]
for v in li:
    if abs(v - avg_val) < abs(v - avg_value):
        avg_val = v
print(avg_val)

"""利用for循环和range输出9 * 9乘法表"""
for i in range(1, 9):
    for v in range(1, i+1):
        print("%s*%s=%s" % (i, v, i * v), end=" ")
    print(end="\n")

"""求100以内的素数和"""
total = 0
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        total += i
print(total)

