# Day17 notes

## 今日内容

继承与派生

### 继承

概念：继承指的是类与类之间的关系，是一种什么“是”什么的关系，继承的功能之一就是用来解决代码重用问题，继承是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类，**父类又可以成为基类或超类**，**新建的类称为派生类或子类**。

示例：单继承与多继承：

```python
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
```

练习：

```python
class Hero:
    x = 3

    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


class Garen(Hero):
    x = 5
    pass


class Riven(Hero):
    pass


g1 = Garen('ike', 100, 30)  # 实例化一个对象
l1 = Riven('joker', 90, 20)  # 实例化一个对象
print(l1.life_value)  # 打印l1的生命值
g1.attack(l1)  # 调用父类的方法
print(l1.life_value)  # 打印l1的生命值
print(g1.nickname, g1.life_value, g1.aggressivity)
```

提示：用已经有的类建立一个新的类，这样就重用了已经有的软件中的一部分设置大部分，大大节省了编程工作量，这就是常说的软件重用，不仅可以重用自己的类，也可以继承别人的，比如标准库，来定制新的数据类型，这样就是大大缩短了软件开发周期，对大型软件开发来说，意义重大.

#### 属性查找

先从实例中找值，然后到自己的类中，最后到父类中找，直到最顶级父类

```python
class Foo:
    def f1(self):
        print('from Foo.f1')

    def f2(self):
        print('from Foo.f2')
        self.f1()  # b.F1()  先从自己找,自己没有去自己的类找,没有然后去自己的父类找


class Bar(Foo):
    def f1(self):
        print('from Bar.f2')


b = Bar()
b.f2()
```

### 派生

示例：在自己的类中派生出新的函数，并且与父类函数名一样

```python
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
print(g.camp)  # 自己(Garen('草丛伦', 100, 30))没有,去自己的类找.
g.attack(r)
print(r.life_value)

```

备注：子类可以添加自己新的属性或者在自己这里重新定义这些属性（不会影响到父类），需要注意的是，一旦重新定义了自己的属性且与父类重名，那么调用新增的属性时，就以自己为准了。

注意：在子类中，需要重用父类的中得函数功能，要用函数调用的普通方式，即：类名.func()，此时就与调用普通函数无异了，因此即便是self参数也要为其传值。

### 继承的原理

示例：

在 python2中-->经典类:没有继承object的类,以及他的子类,都称之为经典类

```python
class Foo:
    pass


class Bar(Foo):
    pass
```

在 python2中-->新式类:继承object的类,以及他的子类,都称之为新式类

```python
class Foo(object):
    pass


class Bar(Foo):
    pass
```

在python3中-->新式类:一个类没有继承object的类,默认都继承object类

```python
class Foo:
    pass


# print(Foo.__bases__)

```

python到底是如何实现继承的，对于你定义的每一个类，python会计算出一个方法解析顺序(MRO)列表，这个MRO列表就是一个简单的所有基类的线性顺序列表。

为了实现继承,python会在MRO列表上从左到右开始查找基类,直到找到第一个匹配这个属性的类为止。而这个MRO列表的构造是通过一个C3线性化算法来实现的。

- 子类会先于父类被检查

- 多个父类会根据它们在列表中的顺序被检查

- 如果对下一个类存在两个合法的选择,选择第一个父类

属性的查找方式有两种，分别是：深度优先和广度优先，在python3中没有深度优先，深度优先是基于类为经典类时。

```python
class A:
    def test(self):
        print('from A')
    # pass


class B(A):
    def test(self):
        print('from B')
        # pass


class C(A):
    def test(self):
        print('from C')
    # pass


class D(B):
    def test(self):
        print('from D')
    # pass


class E(C):
    def test(self):
        print('from E')
    # pass


class F(D, E):
    def test(self):
        print('from F')
    # pass


# F-D-B-E-C-A
print(F.mro())

f = F()
f.test()
```

### 在子类中调用父类的方法

在子类派生出的新方法中，往往需要重用父类的方法，我们有两种方式实现

方式一：指名道姓，即父类名.父类方法()

```python
class Hero:

    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


class Garen(Hero):
    camp = 'Demacia'

    def attack(self, enemy):
        Hero.attack(self, enemy)  # 指名道姓,不依赖于继承,在子类中重用父类的方法attack
        print('from Garen Class')


class Riven(Hero):
    pass


g1 = Garen('ike', 100, 30)
l1 = Riven('joker', 90, 20)
print(l1.__dict__)
print(g1.__dict__)
print(l1.life_value)
g1.attack(l1)
print(l1.life_value)
```

```python
class Hero:

    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


class Garen(Hero):
    camp = 'Demacia'

    def __init__(self, nickname, life_value, aggressivity, weapon):
        # self.nickname = nickname
        # self.life_value = life_value
        # self.aggressivity = aggressivity

        # 可以这样写--super()
        # Hero.__init__(self, nickname, life_value, aggressivity)  # 调用父类的__init__参数要一致,不依赖于继承
        # super(Garen, self).__init__(nickname, life_value, aggressivity)  # python2 super(Garen, self)要加参数
        super().__init__(nickname, life_value, aggressivity)  # python3不用加参数,默认加参数

        self.weapon = weapon

    def attack(self, enemy):
        Hero.attack(self, enemy)  # 指名道姓,不依赖于继承,在子类中重用父类的方法attack
        print('from Garen Class')


g = Garen('草丛伦', 100, 30, '大刀')
print(g.__dict__)
```

方式二：super()

```python
class Hero:

    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


class Garen(Hero):
    camp = 'Demacia'

    def attack(self, enemy):
        super().attack(enemy)  # 依赖于继承
        print('from Garen Class')


g = Garen('草丛伦', 100, 30)
r = Garen('瑞雯雯', 100, 30)
g.attack(r)
print(r.life_value)
```

这两种方式的区别：

- 方式一是跟继承没有关系
- 方式二的super()是依赖于继承，并且即使没有直接继承关系，super仍然会按照mro继续往后查找

```python
class A:
    def test(self):
        super().test()


class B:
    def test(self):
        print('from B')


class C(A, B):
    pass


c = C()
c.test()

# 打印结果:from B

print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
```

A没有继承B,但是A内super会基于C.mro()继续往后找

