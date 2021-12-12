# Day18 notes

## 今日内容

- 组合与重用性

- 抽象类
- 多态与多态性
- 鸭子类型

### 组合与重用性

软件重用的重要方式除了继承之外还有另外一种方式，即：组合

组合指的是，在一个类中以另外一个类的对象作为数据属性，称为类的组合

示例：

```python
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
```

组合与继承都是有效地利用已有类的资源的重要方式。但是二者的概念和使用场景皆不同

- 继承的方式
    - 通过继承建立了派生类与基类之间的关系，它是一种'是'的关系，比如白马是马，人是动物
    - 当类之间有很多相同的功能，提取这些共同的功能做成基类，用继承比较好，比如老师是人，学生是人

- 组合的方式
    - 用组合的方式建立了类与组合的类之间的关系，它是一种‘有’的关系,比如学生有生日

### 抽象类

抽象类是一个特殊的类，它的特殊之处在于只能被继承，不能被实例化，且子类必须实现抽象方法。

示例：

```python
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
```

总结：其实就是父类对子类进行约束. 子类必须要写基类的方法. 在python中约束的。

### 多态与多态性

- 多态：指的是同一类事物的多种形态

- 多态性：指的是可以在不考虑对象的类型的情况下而直接使用对象，多态性分为静态多态性和动态多态性

    - 静态多态性：如任何类型都可以用运算符+进行运算

    - 动态多态性：如下

        ```python
        # 多态性:指的是可以在不考虑对象的类型的情况下而直接使用对象
        peo = People()
        dog = Dog()
        pig = Pig()
        cat = Cat()
        
        
        peo.talk()
        dog.talk()
        pig.talk()
        
        
        # 更进一步,我们可以定义一个统一的接口来使用
        def func(obj):
            obj.talk()
        
        
        func(peo)
        func(cat)
        func(pig)
        func(dog)
        ```

多态性的优点：

- 增加了程序的灵活性
    - 以不变应万变，不论对象千变万化，使用者都是同一种形式去调用，如`func(animal)`
- 增加了程序额可扩展性
    - 通过继承animal类创建了一个新的类，使用者无需更改自己的代码，还是用`func(animal)`去调用

### 鸭子类型

python中有一句谚语说的好，你看起来像鸭子，那么你就是鸭子。

鸭子类型很简单：

示例：

```python
class Disk:
    def read(self):
        print('disk read')

    def write(self):
        print('disk write')


class Text:
    def read(self):
        print('text read')

    def write(self):
        print('text write')


disk = Disk()
text = Text()

disk.read()
disk.write()

text.read()
text.write()
```

Disk和 Text两个类完全没有耦合性，但是在某种意义上他们却统一了一个标准。

对相同的功能设定了相同的名字，这样方便开发，这两个方法就可以互称为鸭子类型。

例如：序列类型有多种形态：字符串，列表，元组，但他们直接没有直接的继承关系

```python
l = list([1, 2, 3])
t = tuple((1, 2, 3, 4, 5))
s = 'hahaha'


# print(l.__len__())
# print(t.__len__())
# print(s.__len__())


def len(w):
    return w.__len__()


print(len(l))
print(len(t))
print(len(s))
```

这样的例子很多：字符串，列表，元组都有len方法，这就是统一了规范，这样的现象就是可以互称为鸭子类型。