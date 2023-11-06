#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/6

# class A:
#     __x = 1
#
#     def __init__(self, name):
#         self.__name = 19  # _A__name
#         pass
#
#     def __foo(self):
#         print("to foo")
#
#     def __bar(self):
#         self.__foo()
#         print("to bar")
#
#     def far(self):
#         self.__foo()
#         self.__bar()
#         print("to far")
#
#
# a = A("name")
# a.far()


# class Foo:
#     def __func(self):  # _Foo__func
#         print('from foo')
#
#     def bar(self):
#         print('A.bar')
#         self.__func()  # self._Foo__bar()
#
#
# class Bar(Foo):
#     def __func(self):
#         print('from bar')
#
#
# b = Bar()
# # b._Bar__func()  # 知道了类名和属性名就可以拼出名字：_类名__属性
#
# b.bar()


class demo:
    __age = 18

    def wt(self):
        pass


a = demo
a.__b = 20  # 变形的过程只在类的定义是发生一次,在定义后的赋值操作，不会变形
print(a.__dict__)

