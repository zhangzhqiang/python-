# Day16 notes

## 今日内容

- 面向对象介绍

### 面向对象程序设计

编程范式

一个程序是程序员为了得到一个任务结果而编写的一组指令的集合，正所谓条条大路通罗马，实现一个任务的方式有很多种不同的方式， 对这些不同的编程方式的特点进行归纳总结得出来的编程方式类别，即为编程范式。

不同的编程范式本质上代表对各种类型的任务采取的不同的解决问题的思路， 大多数语言只支持一种编程范式，当然也有些语言可以同时支持多种编程范式。

两种最重要的编程范式分别是**面向过程**编程和**面向对象**编程。

#### 面向过程编程(Procedural Programming)

面向过程又被称为top-down languages， 就是程序从上到下一步步执行，一步步从上到下，从头到尾的解决问题 。核心是过程二字,过程指的是解决问题的步骤,设计一条流水线,机械式的思维方式。

优点：复杂的问题流程化,进而简单化

缺点：可扩展性差

应用场景：面向过程的程序设计思想一般用于那些功能一旦实现之后就很少需要改变的场景

示例：

``` python
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "ike"
"""
面向过程:核心是过程二字,过程指的是解决问题的步骤,设计一条流水线,机械式的思维方式
优点:复杂的问题流程化,进而简单化
缺点:可扩展性差
"""
import json
import re


def intercactive():
    username = input('>>:').strip()
    password = input('>>').strip()
    email = input('>>').strip()
    return {
        'username': username,
        'password': password,
        'email': email
    }


def check(user_info):
    flag = True

    if len(user_info['username']) == 0:
        print('用户名不能为空')
        flag = False
    if len(user_info['password']) < 6:
        print('密码不能少于6位')
        flag = False
    if not re.search(r'@.*?\.com$', user_info['email']):
        print('邮箱不合法')
        flag = False
    return {
        'flag': flag,
        'user_info': user_info
    }


def register(check_info):
    if check_info['flag']:
        with open('db.json', 'w', encoding='utf-8')as f:
            json.dump(check_info['user_info'], f)


def main():
    user_info = intercactive()
    check_info = check(user_info)
    register(check_info)


if __name__ == '__main__':
    main()
```

建议：如果你只是写一些简单的脚本，去做一些一次性任务，用面向过程的方式是极好的，但如果你要处理的任务是复杂的，且需要不断迭代和维护 的， 那还是用面向对象最方便了。

#### 面向对象编程(Object Oriented Programing)

OOP(Object Oriented Programing）编程是利用“类”和“对象”来创建各种模型来实现对真实世界的描述，核心就是对象二字，对象就是特征与技能的结合体。

优点：可扩展性强

缺点：编程复杂度高

应用场景：用户需求经常变化,互联网应用,游戏,企业内部应用

```python
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "ike"
# Email: 13870492666@163.com
# Date: 2/19/2019 9:43 PM
"""
面向对象:核心就是对象二字,对象就是特征与技能的结合体
优点:可扩展性强
缺点:编程复杂度高
应用场景:用户需求经常变化,互联网应用,游戏,企业内部应用
类:就是一系列对象相似的特征与技能的结合体
强调:站在不同的角度,得到的分类不同
在现实世界中:一定先有对象,后有种类
在程序中:一定先定义类,后调用类来产生对象
"""


# 先定义类
class LuffyStudent:
    shool = 'luffycitry'

    def learn(self):
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')


# 后产生对象  实例化一个对象
stu1 = LuffyStudent()
stu2 = LuffyStudent()
stu3 = LuffyStudent()
stu4 = LuffyStudent()
print(stu1)
print(stu2)
print(stu3)
```

#### 什么是对象

对象是从类中产生的，只要是类名加上（），这就是一个实例化过程，这个就会实例化一个对象。

#### 名词解释

**类：**一个类即是对一类拥有相同属性的对象的抽象、蓝图、原型、模板。在类中定义了这些对象的都具备的属性（variables(data)）、共同的方法

**属性：**人类包含很多特征，把这些特征用程序来描述的话，叫做属性，比如年龄、身高、性别、姓名等都叫做属性，一个类中，可以有多个属性

**方法：**人类不止有身高、年龄、性别这些属性，还能做好多事情，比如说话、走路、吃饭等，相比较于属性是名词，说话、走路是动词，这些动词用程序来描述就叫做方法。

**实例(对象)：**一个对象即是一个类的实例化后实例，一个类必须经过实例化后方可在程序中调用，一个类可以实例化多个对象，每个对象亦可以有不同的属性，就像人类是指所有人，每个人是指具体的对象，人与人之前有共性，亦有不同

**实例化：**把一个类转变为一个对象的过程就叫实例化

#### 如何使用类

示例：

```python
class LuffyStudent:
    shool = 'luffycitry'  # 数据属性

    def learn(self):  # 函数属性
        print('is learning')

    def eat(self):  # 函数属性
        print('is eating')

    def sleep(self):  # 函数属性
        print('is sleeping')

# 类的数据属性是所有对象共享的,id都一样
# 类的函数数据是绑定给对象用的，称为绑定到对象的方法
```

1.查看类的名称空间

```python
# 查看类的名称空间
print(LuffyStudent.__dict__)
print(LuffyStudent.__dict__['shool'])
print(LuffyStudent.__dict__['eat'])
```

2.增、删、改、查四种方法

```python
# 查看
print(LuffyStudent.shool)  # 等同于 print(LuffyStudent.__dict__['shool'])
print(LuffyStudent.learn)  # 等同于 print(LuffyStudent.__dict__['eat'])

# 增加
LuffyStudent.county = 'China'
print(LuffyStudent.__dict__)
print(LuffyStudent.county)

# 删除
del LuffyStudent.county
print(LuffyStudent.__dict__)

# 修改
LuffyStudent.shool = '社会'
print(LuffyStudent.__dict__)
```

`__init__`方法介绍：

`__init__(...)`被称为 构造方法或初始化方法，在例实例化过程中自动执行，目的是初始化实例的一些属性。每个实例通过`__init__`初始化的属性都是自己独有的特征。

示例：

```python
class LuffyStudent:
    school = 'luffycitry'

    def __init__(self, name, sex, age):
        # self 和 stu1 指向的是同一个内存地址同一个空间，下面就是通过self给这个对象空间封装三个属性。

        self.Name = name
        self.Sex = sex
        self.Age = age

    def learn(self):
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')
```

实例化一个对象三个步骤：

- 在内存中开辟了一个对象空间。
- 自动执行类中的`__init__`方法，并将这个对象空间（内存地址）传给了`__init__`方法的第一个位置参数self。
- 在`__init__` 方法中通过self给对象空间添加属性。

对上边的代码进行验证：

```python
# 实例化一个对象
stu1 = LuffyStudent('王二丫', '女', 18)


# 查
print(stu1.__dict__)
print(stu1.Name)
print(stu1.Age)
print(stu1.Sex)

# 改
stu1.Nname = '李二丫'
print(stu1.__dict__)
print(stu1.Nname)

# 删
del stu1.Name
print(stu1.__dict__)

# 增
stu1.class_name = 'python'
print(stu1.__dict__)
```

### 类与对象

类即类别、种类，是面向对象设计最重要的概念，上边我们说过对象是特征与技能的结合体，而类则是一系列对象相似的特征与技能的结合体。

疑问：先有的一个个具体存在的对象，还是先有的人类这个概念？

这个问题需要分两种情况去看：

- 在现实世界中：肯定是先有对象，再有类

    ```python
    在地球上肯定是先出现各种物体，然后随着物体的进化然后产生种类：比如：人类，动物类，植物类等。也就说，对象是具体的存在，而类仅仅只是一个概念，并不真实存在，比如动物类，具体指的是哪种动物。
    ```

- 在程序中：务必保证先定义类，后产生对象

    ```python
    这与函数的使用是类似的：
    先定义函数，后调用函数；类也是一样的，程序中需要先定义类，后调用类。
    不一样的是：
    调用函数会执行函数体代码返回的是函数体执行的结果，调用类会产生对象，返回的是对象
    ```

示例：

现实生活中：先有对象，再有类

```python
在现实世界中:
    对象一:王二丫
        特征:
            学校 = 'luffycity'
            名字 = '王二丫'
            性别 = '女'
            年龄 = 18
        技能:
            学习
            吃饭
            睡觉
    对象二:李三炮
        特征:
            学校 = 'luffycity'
            名字 = '李三炮'
            性别 = '男'
            年龄 = 38
        技能:
            学习
            吃饭
            睡觉
    对象二:张铁蛋
        特征:
            学校 = 'luffycity'
            名字 = '张铁蛋'
            性别 = '男'
            年龄 = 48
        技能:
            学习
            吃饭
            睡觉


总结:现实中路飞学院的学生类:
    相似特征:
    	学校 = 'luffycity'
    相似技能:
    	学习
    	吃饭
		睡觉
```

在程序中：务必保证先定义类，后产生对象

```python
# 先定义类
class LuffyStudent:
    shool = 'luffycitry'
	# Python中类用class关键字定义，而在程序中特征用变量标识，技能用函数标识，因而类中最常见的无非是：变量和函数的定义
    def __init__(self, name, sex, age):
        self.Nname = name
        self.Sex = sex
        self.Age = age

    def learn(self, age):
        print('%s is learning %s' % (self.Nname, 18))

    def eat(self):
        print('%s is eating' % self.Nname)

    def sleep(self):
        print('%s is sleeping' % self.Nname)


# 后产生对象
# 调用类，或称为实例化，得到程序中的对象
stu1 = LuffyStudent('王二丫', '女', 18)
stu2 = LuffyStudent('李三炮', '男', 38)
stu3 = LuffyStudent('张铁丹', '男', 48)
# 如此，stu1、stu2、stu3，而这三者除了相似的属性之外还各种不同的属性，这就用到了__init__
```

总结：

对象：特征与技能的结合体

类：是一系列对象相似的特征与相似的技能的结合体

类中的数据属性：所有对象直接共有的：

```python
print(LuffyStudent.shool, id(LuffyStudent.shool))
print(stu1.shool, id(stu1.shool))
print(stu2.shool, id(stu2.shool))
print(stu3.shool, id(stu3.shool))
```

类中的函数属性：绑定给对象使用的，绑定到不同的对象是不同的绑定方法，对象调用绑定方法时，会把对象本身当做第一个参数传入,传给self：

```python
print(LuffyStudent.learn)  # 普通函数
print(stu1.learn)  # 绑定方法
print(stu2.learn)  # 绑定方法
print(stu3.learn)  # 绑定方法
```

总结

- 在没有学习类这个概念时，数据与功能是分离的

    ```python
    def name(name):
        print('wo shi %s' % (name,))
    
    
    def age(age):
        print('wo %s sui' % age)
    
    # 每次调用都需要重复传入参数
    name('ike')
    age(18)
    ```

- 面向过程编程：解决方法是，把这些变量都定义成全局变量

    ```python
    Name = 'ike'
    Age = 18
    
    
    def name(name):
        print('wo shi %s' % (name,))
    
    
    def age(age):
        print('wo %s sui' % age)
    
    
    name(Name)
    age(Age)
    ```

- 面向对象编程：将数据与专门操作该数据的功能整合到一起，可扩展性高

    ```python
    class People:
        def __init__(self, names, age):
            self.names = names
            self.age = age
    
        def name(self):
            print('wo shi %s' % self.names)
    
        def age(self):
            print('wo %s sui' % self.age)
    
    
    stu1 = People('ike', 18)
    stu2 = People('opk', 19)
    stu1.name()
    stu2.name()
    ```

    

