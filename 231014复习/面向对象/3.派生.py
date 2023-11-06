#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/4


class Hero:
    x = 3

    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity
        print('from Hero class')


class Garen(Hero):  # Garen叫做派生类或子类，Hero叫做父类或基类或超类
    camp = 'Demacia'

    def attack(self, enemy):  # 在自己这里定义新的attack,不再使用父类的attack,且不会影响父类
        print('from Garen class')
        Hero.attack(self, enemy)  # 调用父类功能


class Riven(Hero):
    camp = 'Noxus'


g = Garen('草丛伦', 100, 30)
r = Riven('瑞雯', 90, 20)
# print(g.camp)  # 自己(Garen('草丛伦', 100, 30))没有,去自己的类找.
g.attack(r)
print(r.life_value)
r.attack(g)
print(g.life_value)