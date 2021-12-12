# Day19 notes

## 今日内容

- 封装

### 封装

#### 如何将属性设为私有

在python中用双下划线开头的方式将属性隐藏起来（设置成私有的）

```python
class A:
    __x = 1  # 类的数据属性就应该是共享的,但是语法上是可以把类的数据属性设置成私有的如 __x 就会变为 _A__x

    def __init__(self, name):
        self.__name = 19  # _A__foo
        pass

    def __foo(self):  # _A__foo
        print('tun foo')

    def bar(self):
        self.__foo()  # 只有在类内部才可以通过__foo的形式访问到
        print('from bar')

a.bar()  # 内部可以访问
```

这种变形的特点:

- 外部无法直接obj.__AttrName访问
- 在类内部是可以直接调用obj.__AttrName
- 子类无法覆盖父类__开头的属性

正常情况：

```python
# 正常情况
class Foo:
    def func(self):
        print('from foo')

    def bar(self):
        print('A.bar')
        self.func()


class Bar(Foo):
    def func(self):
        print('from bar')


b = Bar()
b.func()  # from bar
```

把__func设置成私有：

```python
# 把__func设置成私有
class Foo:
    def __func(self):  # _Foo__func
        print('from foo')

    def bar(self):
        print('A.bar')
        self.__func()  # self._Foo__bar()


class Bar(Foo):
    def __func(self):
        print('from bar')


b = Bar()
# b._Bar__func()  # 知道了类名和属性名就可以拼出名字：_类名__属性


b.bar()  # A.bar  from foo
```

这种变形注意的问题：

- 这种机制也并没有真正意义上限制我们从外部直接访问属性，知道了类名和属性名就可以拼出名字：_类名.__属性，然后就可以访问了，如a._A__N

- 变形的过程只在类的定义是发生一次,在定义后的赋值操作，不会变形

    ```python
    class demo:
        __age = 18
    
        def wt(self):
            pass
    
    
    a = demo
    a.__b = 20  # 变形的过程只在类的定义是发生一次,在定义后的赋值操作，不会变形
    print(a.__dict__)
    
    print(a._demo__age)  # 知道了类名和属性名就可以拼出名字：_类名.__属性
    print(a.__b)  # 知道了类名和属性名就可以拼出名字：_类名.__属性
    ```

- 在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的

#### 封装的意义

封装数据属性:明确的区分内外,控制外部对隐藏的属性的操作行为

```python
class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def tell_info(self):  # 内部开一个接口,外部调用
        print('Name:<%s> Age:<%s>' % (self.__name, self.__age))

    def set_info(self, name, age):  # 开一个接口外部调用
        if not isinstance(name, str):
            print('名字必须是字符串类型')
            return
        if not isinstance(age, int):
            print('年龄必须是数字类型')
            return
        self.__name = name
        self.__age = age


p = People('ike', 18)
p.tell_info()
p.set_info('ikeer', 18)
p.tell_info()
```

封装方法:隔离复杂度

```python
class ATM:

    def __card(self):
        print('插卡')

    def __auth(self):
        print('用户认证')

    def __input(self):
        print('输入取款金额')

    def __print_bill(self):
        print('打印账单')

    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()


a = ATM()
a.withdraw()
```

提示：在编程语言里，对外提供的接口（接口可理解为了一个入口），可以是函数，称为接口函数，这与接口的概念还不一样，接口代表一组接口函数的集合体。

#### 特性（property）

property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值

```python
"""
例一：BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）

成人的BMI数值：

过轻：低于18.5

正常：18.5-23.9

过重：24-27

肥胖：28-32

非常肥胖, 高于32

体质指数（BMI）=体重（kg）÷身高^2（m）

EX：70kg÷（1.75×1.75）=22.86
"""

class People:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property  # 调用的时候不用加括号()  伪装起来
    def bmi(self):
        return self.weight / (self.height ** 2)


p = People('ike', 69, 1.73)
print(p.bmi)  # @property调用的时候不用加括号()
```

计算圆的周长与面积：

```python
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2  # 计算面积

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius  # 计算周长


c = Circle(10)
print(c.area)
print(c.perimeter)
```

#### 用property的意义

将一个类的函数定义成特性以后，对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数然后计算出来的，这种特性的使用方式**遵循了统一访问的原则**

```
ps：面向对象的封装有三种方式:
【public】
这种其实就是不封装,是对外公开的
【protected】
这种封装方式对外不公开,但对朋友(friend)或者子类(形象的说法是“儿子”,但我不知道为什么大家 不说“女儿”,就像“parent”本来是“父母”的意思,但中文都是叫“父类”)公开
【private】
这种封装对谁都不公开
```

python并没有在语法上把它们三个内建到自己的class机制中，在python中通过property方法可以实现

```python
class People:
    def __init__(self, name):
        self.__name = name

    @property  # name被@property装饰过,一般用在计算中,把计算的数据属性,封装起来
    def name(self):
        # print('getter')
        return self.__name

    @name.setter  # name被@property装饰过,用setter修改
    def name(self, val):
        # print('setter')
        if not isinstance(val, str):
            raise TypeError('名字必须是字符串类型')
        self.__name = val

    @name.deleter  # name被@property装饰过,用deleter删除
    def name(self):
        print('deleter')
        raise TypeError('不允许删除')


p = People('ike')

print(p.name)
p.name = '102'  # TypeError: 名字必须是字符串类型
del p.name  # TypeError: 不允许删除
```

#### 封装与扩展性

封装在于明确区分内外，使得类实现者可以修改封装内的东西而不影响外部调用者的代码；而外部使用用者只知道一个接口(函数)，只要接口（函数）名、参数不变，使用者的代码永远无需改变。这就提供一个良好的合作基础——或者说，只要接口这个基础约定不变，则代码改变不足为虑。

```python
# 类的设计者
class Room:
    def __init__(self,name,owner,width,length,high):
        self.name=name
        self.owner=owner
        self.__width=width
        self.__length=length
        self.__high=high
    def tell_area(self):  # 对外提供的接口，隐藏了内部的实现细节，此时我们想求的是面积
        return self.__width * self.__length


# 使用者
>>> r1=Room('卧室','egon',20,20,20)
>>> r1.tell_area()  # 使用者调用接口tell_area


# 类的设计者，轻松的扩展了功能，而类的使用者完全不需要改变自己的代码
class Room:
    def __init__(self,name,owner,width,length,high):
        self.name=name
        self.owner=owner
        self.__width=width
        self.__length=length
        self.__high=high
    def tell_area(self):  # 对外提供的接口，隐藏内部实现，此时我们想求的是体积,内部逻辑变了,只需求修该下列一行就可以很简答的实现,而且外部调用感知不到,仍然使用该方法，但是功能已经变了
        return self.__width * self.__length * self.__high


# 对于仍然在使用tell_area接口的人来说，根本无需改动自己的代码，就可以用上新功能
>>> r1.tell_area()
```


