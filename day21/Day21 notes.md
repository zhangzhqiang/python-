# Day21 notes

## 今日内容

- 反射

### 内置方法

**反射**：

通过字符串的映射到对象的属性，python中一切事物都是对象，都可以使用反射。

四个自省的函数

- hasattr，判断有没有属性
- getattr，获取属性
- setattr，修改属性
- delattr，删除属性

示例：

```python
class People:
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)


obj = People('ike', 18)

# 判断有没有属性
print(hasattr(obj, 'sex'))  # obj.name  # obj.__dict__['name']
print(hasattr(obj, 'talk'))  # obj.talk

# 获取
print(getattr(obj, 'op', None))  # None没有属性不会报错,返回None
print(getattr(obj, 'talk', None))

# 修改
setattr(obj, 'sex', 'male')  # obj.sex = 'male'
print(obj.__dict__)

# 删除
delattr(obj, 'age')  # del obj.age
print(obj.__dict__)

# 适用于类,例子
print(getattr(People, 'country'))  # People.country
```

反射的应用

```python
class Service:
    def run(self):
        while True:
            inp = input('>>:').strip()
            cmd = inp.split()

            if hasattr(self, cmd[0]):  # 用户输入get  xx.txt
                func = getattr(self, cmd[0])
                func(cmd)

    def get(self, cmd):
        print('get....', cmd)

    def put(self, cmd):
        print('put.....', cmd)


obj = Service()
obj.run()
```

**isinstance和issubclass**：

isinstance(obj,cls)检查是否obj是否是类 cls 的对象

```python
class Foo(object):
    pass


obj = Foo()

print(isinstance(obj, Foo))
```

issubclass(sub, super)检查sub类是否是 super 类的派生类

```python
class Foo(object):
    pass


class Bar(Foo):
    pass


print(issubclass(Bar, Foo))
```

**tiem系列**：

示例：

```python
class Foo:
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):  # item = 'name'
        # print('getitem', item)
        return self.__dict__.get(item)

    def __setitem__(self, key, value):
        # print('setitem')
        # print(key, value)
        self.__dict__[key] = value

    def __delitem__(self, key):
        # print('delitem')
        # print(key)
        # self.__dict__.pop(key)
        del self.__dict__[key]


obj = Foo('ike')
# print(obj.__dict__)

# 获取属性名:
print(obj['name'])

# 设置属性:
obj['sex'] = 'male'
print(obj.__dict__)
print(obj.sex)

# 删除属性:
del obj['name']  # 现在删除
print(obj.__dict__)
```

**`__str__`,`__repr__`,`__format__`**

`__str__`的功能与用法：

- `__str__`功能：将实例对象按照自定义的格式用字符串的形式显示出来，提高可读性
- 实例化的对象在打印时会默认调用`__str__`方法，如果类没有重写这个方法，默认调用父类object的`__str__`方法
- object的`__str__`方法内部是pass，所以打印的是内存地址。如果当前类重写了这个方法，会自动调用重写后的方法

```python
class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):    # 在打印的时候执行,以字符串的形式显示
        print("str内容可视化了")
        return "Student(%s,%d)" % (self.name, self.age)
    
    def __repr__(self):
        print("repr内容可视化了")
        return "Student(%s,%d)" % (self.name, self.age)


s1 = People("ike", 19)
print(s1)  # print(s1)时，默认会调用用户重写后的s1.__str__方法。
```

`__repr__`的功能与用法

- `__repr__`如果用IDE软件操作，功能与`__str__`完全一样，都是实例可视化显示
- 开发中如果用户需要可视化实例内容，只需要重写`__str__`或者`__repr__`方法之一即可。如果两个都有的话，默认调用`__str__`.

两者的区别：

- `__str__`是面向用户显示的，若重构`__str__`则使用print(Object)可以显示想显示的内容
- `__repr__`是面向程序员显示的，若重构`__repr__`，则直接输出类对象和print(Object)均可以显示想显示的内容。

**`__del__`**

析构方法，当对象在内存中被释放时，自动触发执行

示例：

```python
class Open:
    def __init__(self, filename):
        print('open file......')
        self.filename = filename

    def __del__(self):
        print('回收操作系统资源:self.close')


f = Open('settings.py')
	
del f  # f.__del__()
print('------mian------')  # del f  # f.__del__()
```

