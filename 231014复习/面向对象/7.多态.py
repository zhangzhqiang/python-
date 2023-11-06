#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/6

import abc  # 利用abc模块实现抽象类


class Animal(metaclass=abc.ABCMeta):  # 抽象类只能被继承,不能被实例化
    all_type = 'animal'

    @abc.abstractmethod  # 继承后,加装饰器的,必须遵循类的方法
    def run(self):
        pass

    @abc.abstractmethod  # 继承后,加装饰器的,必须遵循类的方法
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


# 多态性:指的是可以在不考虑对象的类型的情况下而直接使用对象
peo = People()
dog = Dog()
pig = Pig()


# 更进一步,我们可以定义一个统一的接口来使用
def func(obj):
    obj.eat()


func(peo)
func(dog)
func(pig)
