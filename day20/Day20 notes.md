# Day20 notes

## 今日内容

- 绑定方法与非绑定方法

### 绑定与非绑定

类内部定义的函数分成两大类：

```
类内部定义的函数分成两大类：
    一.绑定方法:绑定给谁,就应该由谁来调用,谁来调用就会把调用者当做第一个参数自动传入
        1.绑定到对象的方法:在类内定义的没有被任何装饰器修饰的
        2.绑定到类的方法:在类内部定义的被装饰器@classmethod修饰的方法
    二.非绑定方法:没有自动传值这么一说,就是这种定义的普通工具,对象和类都可以使用
        不与类或对象绑定
```

示例1：

```python
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "ike"
# Email: 13870492666@163.com
# Date: 2/23/2019 10:28 PM
"""
在类内部定义的函数,分为两大类:
    一.绑定方法:绑定给谁,就应该由谁来调用,谁来调用就会把调用者当做第一个参数自动传入
        1.绑定到对象的方法:在类内定义的没有被任何装饰器修饰的
        2.绑定到类的方法:在类内部定义的被装饰器@classmethod修饰的方法
    二.非绑定方法:没有自动传值这么一说,就是这种定义的普通工具,对象和类都可以使用
        不与类或对象绑定
"""


class Foo:

    def __init__(self, name):
        self.name = name

    def tell(self):
        print('名字是%s' % self.name)

    @classmethod  # 绑定给类
    def func(cls):  # cls =Foo
        print(cls)

    @staticmethod  # 对象和类都可以调用
    def func1(x, y):
        print(x + y)


f = Foo('ike')

f.tell()  # 调用tell方法
f.func()  # classmethod绑定给类,只能类来调用
print(Foo.func)

# 打印结果:
'''
名字是ike
<class '__main__.Foo'>
<bound method Foo.func of <class '__main__.Foo'>>
'''

# 非绑定方法都可以来调用
Foo.func1(1, 2)
f.func1(5, 6)

# 打印结果:
'''
3
11
'''
```

示例2：

```python
import hashlib
import time

Name = 'egon'
Age = 18
Sex = 'female'


class People:
    def __init__(self, name, age, sex):
        self.id = self.create_id()
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):  # 绑定到对象的方法
        print('Name:%s Age:%s Sex:%s' % (self.name, self.age, self.sex))

    @classmethod  # 绑定到类的方法
    def from_conf(cls):
        obj = cls(Name, Age, Sex)
        return obj

    @staticmethod
    def create_id():
        m = hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()


p = People('ike', 18, 'male')

# 绑定给对象,就应该由对象来调用,自动将对象本身当做第一个参数传入
p.tell()

# 绑定给类,就应该由类来调用,自动将类本身当做第一个参数传入
p = People.from_conf()
p.tell()

# 非绑定方法,不与类或者对象绑定,谁都可以调用,没有自动传值一说
p1 = People('ike', 18, 'male')
p2 = People('egon', 28, 'male')
p3 = People('make', 19, 'male')
print(id(p1))
print(id(p2))
print(id(p3))
```

`classmethod`与`staticmethod`的对比

```python
class MySQL:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @staticmethod
    def from_conf():
        return MySQL('192.168.1.203', 9090)

    # @classmethod  # 哪个类来调用,就将哪个类当做第一个参数传入
    # def from_conf(cls):
    #     return cls('192.168.1.203', 9090)

    def __str__(self):
        return '就不告诉你'


class Mariadb(MySQL):
    def __str__(self):
        return '<%s:%s>' % (self.host, self.port)


m = Mariadb.from_conf()
print(m)
```

我们发现：

- `@classmethod`修饰后，自动将类当作第一个参数传入
- `@staticmethod`修饰后，不会自动将类当作第一个参数传入