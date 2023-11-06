#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/4

# class A:
#     def test(self):
#         print('from A')
#     # pass
#
#
# class B(A):
#     def test(self):
#         print('from B')
#         # pass
#
#
# class C(A):
#     def test(self):
#         print('from C')
#     # pass
#
#
# class D(B):
#     def test(self):
#         print('from D')
#     # pass
#
#
# class E(C):
#     def test(self):
#         print('from E')
#     # pass
#
#
# class F(D, E):
#     def test(self):
#         print('from F')
#     # pass
#
#
# # F-D-B-E-C-A
# print(F.mro())
#
# # f = F()
# # f.test()


# 子类继承父类
# class Hero:
#
#     def __init__(self, nickname, life_value, aggressivity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggressivity = aggressivity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggressivity
#
#
# class Garen(Hero):
#     camp = 'Demacia'
#
#     def __init__(self, nickname, life_value, aggressivity, weapon):
#         # self.nickname = nickname
#         # self.life_value = life_value
#         # self.aggressivity = aggressivity
#
#         # 可以这样写--super()
#         # Hero.__init__(self, nickname, life_value, aggressivity)  # 调用父类的__init__参数要一致,不依赖于继承
#         # super(Garen, self).__init__(nickname, life_value, aggressivity)  # python2 super(Garen, self)要加参数
#         super().__init__(nickname, life_value, aggressivity)  # python3不用加参数,默认加参数
#
#         self.weapon = weapon
#
#     def attack(self, enemy):
#         Hero.attack(self, enemy)  # 指名道姓,不依赖于继承,在子类中重用父类的方法attack
#         print('from Garen Class')
#
#
# g = Garen('草丛伦', 100, 30, '大刀')
# print(g.__dict__)


# super 方法
# class Hero:
#
#     def __init__(self, nickname, life_value, aggressivity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggressivity = aggressivity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggressivity
#
#
# class Garen(Hero):
#     camp = 'Demacia'
#
#     def attack(self, enemy):
#         super().attack(enemy)  # 依赖于继承
#         print('from Garen Class')
#
#
# g = Garen('草丛伦', 100, 30)
# r = Garen('瑞雯雯', 100, 30)
# g.attack(r)
# print(r.life_value)
