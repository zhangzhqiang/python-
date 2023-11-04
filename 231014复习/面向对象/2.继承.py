#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/4


class ParentClass:
    pass

class ParentClass1:
    pass

class Subclass(ParentClass):  # 单继承，基类是ParentClass，派生类是Subclass
    pass

class Subclass1(ParentClass, ParentClass1):  # python支持多继承，用逗号分隔开多个继承的类
    pass

# __bases__查看继承的类

print(Subclass.__bases__)
print(Subclass1.__bases__)
