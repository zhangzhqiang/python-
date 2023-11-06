#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/7

class People():

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def __str__(self):
        print("str内容可视化")
        return "Student(%s,%d)" % (self.name, self.age)

    def __repr__(self):
        print("repr内容可视化")
        return "Student(%s,%d)" % (self.name, self.age)

s1 = People("ike", 19)
print(s1)