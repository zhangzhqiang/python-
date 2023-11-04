#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/4


class LuffyStudent:
    school = 'luffycitry'  # 数据属性

    def learn(self):  # 函数属性
        print('is learning')

    def eat(self):  # 函数属性
        print('is eating')

    def sleep(self):  # 函数属性
        print('is sleeping')


print(LuffyStudent.__dict__)
print(LuffyStudent.__dict__["school"])
print(LuffyStudent.school)
print(LuffyStudent.learn)


