#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/6

class People:
    school = 'luffycity'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(People):

    def __init__(self, name, age, sex, level, salary):
        super().__init__(name, age, sex)

        self.level = level
        self.salary = salary

    def teach(self):
        print('%s is teaching' % self.name)


class Student(People):
    school = 'luffycity'

    def __init__(self, name, age, sex, class_time):
        super().__init__(name, age, sex)

        self.class_time = class_time

    def learn(self):
        print('%s is learning' % self.name)


class Course:
    def __init__(self, course_name, course_price, course_period):
        self.course_name = course_name
        self.course_price = course_price
        self.course_period = course_period

    def tell_info(self):
        print('课程名<%s> 课程价钱<%s> 课程周期<%s>' % (self.course_name, self.course_price, self.course_period))


class Date:
    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day

    def tell_info(self):
        print('%s-%s-%s' % (self.year, self.mon, self.day))


stu1 = Student('zhagnaa', 28, 'male', '8:00')  # 实例化一个对象
d = Date(1988, 4, 20)  # 实例化一个对象

stu1.bith = d
stu1.bith.tell_info()  # 通过组合的方式,本身没有Date

python = Course('python', 3000, '3mons')  # 实例化一个python课程对象
linux = Course('linux', 2000, '2mons')  # 实例化一个linux课程对象
student1 = Student('张三', 28, 'female', '08:30:00')  # 实例化一个学生对象

# 为学生添加课程
student1.courses = []
student1.courses.append(python)
student1.courses.append(linux)

# 遍历学生所选择的课程
for i in student1.courses:
    i.tell_info()
