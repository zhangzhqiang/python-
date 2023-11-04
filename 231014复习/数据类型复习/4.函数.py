#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/10/26


# def func(arg):
#     v1 = arg()
#     print(v1)
#
#
# def show():
#     return "ces"
#
#
# func(show)

# 2.lambda 函数

# DATA = 100


# def func():
#     DATA = 1000
#     func1 = lambda a1: a1 + DATA
#     ret = func1(1)
#     print(ret)
#
# func()

# func1 = lambda a1, a2: a1 if a1 > a2 else a2
# ret = func1(1000, 2000)
# print(ret)

# func1 = lambda x: x.split('l')
#
# v1 = func1('alex')
# print(v1)

# func_list = [lambda x: x.strip(), lambda y: y + 199, lambda x, y: x + y]
#
# v1 = func_list[0]('alex ')
# print(v1)
#
# v2 = func_list[1](100)
# print(v2)
#
# v3 = func_list[2](1, 2)
# print(v3)

# a, b = divmod(1001, 5)
# print(a, b)
#
# USER_LIST = []
# for i in range(1, 836):
#     temp = {'name': '你少妻-%s' % i, 'email': '123%s@qq.com' % i}
#     USER_LIST.append(temp)
#
# # 数据总条数
# total_count = len(USER_LIST)
#
# # 每页显示10条
# per_page_count = 10
#
# # 总页码数
# max_page_num, a = divmod(total_count, per_page_count)
# if a > 0:
#     max_page_num += 1
# print(max_page_num)
#
# while True:
#     pager = int(input('要查看第几页：'))
#     if pager < 1 or pager > max_page_num:
#         print('页码不合法，必须是 1 ~ %s' % max_page_num)
#     else:
#         """
#         # 第1页：USER_LIST[0:10] -> 0123456789
#         # 第2页：USER_LIST[10:20]
#         # 第3页：USER_LIST[20:30]
#         ...
#         """
#         start = (pager - 1) * per_page_count
#         end = pager * per_page_count
#         data = USER_LIST[start:end]
#         for item in data:
#             print(item)

# name = 'oldboy'
#
#
# def bar(name):
#     def inner():
#         print(name)
#
#     return inner
#
#
# v1 = bar('alex')  # { name=alex, inner }  # 闭包，为函数创建一块区域（内部变量供自己使用），为他以后执行提供数据。
# v2 = bar('eric')  # { name=eric, inner }
# v1()
# v2()

# name = 'alex'
#
#
# def func():
#     name = 'eric'
#
#     def base():
#         print(name)
#
#     base()
#
#
# func()

# def task(arg):
#     def inner():
#         print(arg)
#
#     return inner
#
#
# inner_func_list = []
# for val in [11, 22, 33]:
#     inner_func_list.append(task(val))
#
# inner_func_list[0]()  # 11
# inner_func_list[1]()  # 22
# inner_func_list[2]()  # 33

# v1 = [11, 22, 33, 44]
# result = map(lambda x: x + 100, v1)
# print(list(result))  # 特殊

# v1 = [11, 22, 33, 'asd',  'xf']
#
#
# def func(x):
#     if type(x) == int:
#         return True
#     return False
#
#
# result = filter(func, v1)  # [11,22,33,44]
# print(list(result))
#
# ret = filter(lambda x: True if type(x) == int else False, v1)
# print(list(ret))

# import functools
#
# v1 = ["wo", "hao", "e", "aaa", "bbb"]
#
# ret = functools.reduce(lambda x, y: x + y, v1)
# print(ret)

# import time
#
#
# def func(a, b):
#     time.sleep(2)
#     print(b)
#     func(b, a + b)
#
# func(0, 1)

# def func(a):
#     if a == 5:
#         return 10000
#     result = func(a + 1) + 10
#     return result
#
#
# v = func(1)
# print(v)

# name = 'alex'
# def func():
#     def inner():
#         print(name)
#     return inner
#
# v = func()
# print(v())

# def func():
#     print("我是func函数")
#     value = (11, 22, 33, 44)
#     return value
#
#
# def outer(origin):
#     def inner():
#         print('inner')
#         res = origin()
#         print("after")
#         return res
#     return inner
#
# func = outer(func)
# result = func()
# print(result)

# def outer(origin):
#     def inner():
#         print('inner')
#         res = origin()
#         print("after")
#         return res
#     return inner
#
#
# @outer
# def func():
#     print("我是func函数")
#     value = (11, 22, 33, 44)
#     return value
#
#
# func()


# 3. 装饰器
# def outer(origin):
#     def inner(*args, **kwargs):
#         print("before 110")
#         res = origin(*args, **kwargs)  # 调用原来的func函数
#         print("after")
#         return res
#
#     return inner
#
#
# @outer  # func1 = outer(func1)
# def func1(a1):
#     print("我是func1函数")
#     value = (11, 22, 33, 44)
#     return value
#
#
# @outer  # func2 = outer(func2)
# def func2(a1, a2):
#     print("我是func2函数")
#     value = (11, 22, 33, 44)
#     return value
#
#
# @outer  # func3 = outer(func3)
# def func3(a1):
#     print("我是func3函数")
#     value = (11, 22, 33, 44)
#     return value
#
#
# ret1 = func1(1)
# ret2 = func2(11, a2=22)
# func3(999)

# 4.带参数的装饰器
# def xxx(counter):
#     print('x函数')
#
#     def wrapper(func):
#         print('wrapper函数')
#
#         def inner(*args, **kwargs):
#             v = []
#             for i in range(counter):
#                 data = func(*args, **kwargs)  # 执行原函数并获取返回值
#                 v.append(data)
#             return v
#         return inner
#
#     return wrapper
#
#
# @xxx(5)
# def index():
#     print("index函数")
#     return 8
#
#
# v = index()
# print(v)

# def xxx(counter):
#     print('x函数')
#
#     def wrapper(func):
#         print('wrapper函数')
#
#         def inner(*args, **kwargs):
#             for i in range(counter):
#                 data = func(*args, **kwargs)  # 执行原函数并获取返回值
#             return data
#
#         return inner
#
#     return wrapper
#
#
# @xxx(5)
# def index():
#     print("index函数")
#     return 8
#
#
# v = index()
# print(v)

# def xxx(counter):
#     print('x函数')
#
#     def wrapper(func):
#         print('wrapper函数')
#
#         def inner(*args, **kwargs):
#             v = []
#             for i in range(counter):
#                 data = func(*args, **kwargs)  # 执行原函数并获取返回值
#             v.append(data)
#             return v
#
#         return inner
#
#     return wrapper
#
#
# @xxx(5)
# def index():
#     print("index函数")
#     return 8
#
#
# v = index()
# print(type(v))
# print(v)

# def xxx(counter):
#     print('x函数')
#
#     def wrapper(func):
#         print('wrapper函数')
#
#         def inner(*args, **kwargs):
#             value = 0
#             for i in range(counter):
#                 data = func(*args, **kwargs)  # 执行原函数并获取返回值
#                 if data > value:
#                     value = data
#             return value
#
#         return inner
#
#     return wrapper
#
#
# @xxx(5)
# def index():
#     return 8
#
#
# v = index()
# print(v)

# a = [1, 2, 3, 4, 5, 5]
#
# max_num = a[0]
#
# for i in a:
#
#     if i > max_num:
#
#         max_num = i
#
# print(max_num)

# from functools import reduce
#
# a = [1, 2, 3, 4, 5, 5]
# max_num = reduce(lambda x, y: x if x > y else y, a)
# print(max_num)

# 推导式
# v3 = [99 if i>5 else 66  for i in range(10)]
# print(v3)

# v5 = [lambda: 100 for i in range(10)]
# # result = v5[2]()
# for i in v5:
#     ret = i()
#     print(ret)

# v8 = [lambda x: x * i for i in range(10)]
# ret = v8[7](2)
# print(ret)

# v9 = [i for i in range(10) if i > 5]
# print(v9)
#
# v1 = {'k' + str(i): i for i in range(10)}
# print(v1)

# info = {
#     "name": "武沛齐",
#     "email": "xxx@live.com",
#     "gender": "男",
# }
#
# res = ";".join(["{}-{}".format(k, v) for k, v in info.items()])
# print(res)
#
# def func():
#     print(123)
#
#
# data_list = [func for i in range(10)]
#
# print(data_list)

# def num():
#     return (lambda x: i * x for i in range(4))
#
#
# # 1. num()并获取返回值  生成器对象
# # 2. for循环返回值
# # 3. 返回值的每个元素(2)
# result = [m(2) for m in num()]  # [0,2,4,6 ]
# print(result)


# 生成器

# def func():
#     print(111)
#     yield 1
#
#     print(222)
#     yield 2
#
#     print(333)
#     yield 3
#
#     print(444)
#
#
# data = func()
# for item in data:
#     print(item)

# import random
#
# def get_random_num(max_count):
#     counter = 0
#     while counter < max_count:
#         yield random.randint(1000, 9999)
#         counter += 1
# data_list = get_random_num(2000000)
# print(next(data_list))
# # 使用时，去data_list中获取

# def func():
#     print(111)
#     v1 = yield 1
#     print(v1)
#
#     print(222)
#     v2 = yield 2
#     print(v2)
#
#     print(333)
#     v3 = yield 3
#     print(v3)
#
#     print(444)
#
#
# data = func()
#
# n1 = data.send(None)
# print(n1)
#
# n2 = data.send(666)
# print(n2)
#
# n3 = data.send(777)
# print(n3)
#
# n4 = data.send(888)
# print(n4)


import random


def get_random_code(length=6):
    data = []
    for i in range(length):
        v = random.randint(65, 90)
        data.append(chr(v))
    return "".join(data)

ret = get_random_code()
print(ret)
