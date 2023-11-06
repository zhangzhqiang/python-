#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/6

import abc  # 利用abc模块实现抽象类


class Animal(metaclass=abc.ABCMeta):  # 抽象类只能被继承,不能被实例化
    all_type = 'animal'

    @abc.abstractmethod  # 加装饰器,继承后,必须遵循类的方法
    def run(self):
        pass

    @abc.abstractmethod  # 加装饰器,继承后,必须遵循类的方法
    def eat(self):
        pass


class People(Animal):  # 子类继承抽象类，但是必须定义run和eat方法
    def run(self):
        print('people is walking')

    def eat(self):
        print('people is eating')


class Pig(Animal):  # 子类继承抽象类，但是必须定义run和eat方法
    def run(self):
        print('pig is walking')

    def eat(self):
        print('pig is eating')


class Dog(Animal):  # 子类继承抽象类，但是必须定义run和eat方法
    def run(self):
        print('dog is walking')

    def eat(self):
        print('dog is eating')


peo = People()
pig = Pig()
dog = Dog()

# 归一化设计：不管是哪一个类的对象，都调用同一个函数去完成相似的功能
peo.eat()
pig.eat()
dog.eat()

print(peo.all_type)
print(pig.all_type)
print(dog.all_type)
