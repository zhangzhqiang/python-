# Day22 notes

## 今日内容

- 元类
- 异常处理

### 元类

#### 储备介绍exec

- 参数一：字符串形式的命令
- 参数二：全局作用域(字典形式)如果不指定，默认使用globls()
- 参数三：局部作用域(字典形式)如果不指定，默认使用locals()

示例：exec

```python
# 全局
g = {'x': 1, 'y': 2}
# 局部
l = {}

exec("""
global x, m
x = 10
m = 100
z = 3
""", g, l
     )
print(g)
print(l)

# 把exec执行的命令当成是一个函数的执行，会将执行期间产生的名字存放于局部名称空间中
```

python中一切皆对象，类(class)本身也是一个对象，当使用关键字class的时候，python解释器在加载class的时候就会创建一个对象，我们可以把类当做一个对象去使用。

一切皆对象，满足以下四个条件都是对象：

- 都可以被引用，x = obj
- 都可以单做函数的参数传入
- 都可以当做函数的返回值
- 都可以当做容器类的元素

示例：

```python
class Foo:
    pass

obj = Foo()
print(type(obj))
print(type(Foo))
'''
结果：
<class '__main__.Foo'>
<class 'type'>
'''


class Bar:
    pass

print(type(Bar))

'''
结果：
<class 'type'>
'''
```

我们可以看出obj是Foo实例出的对象，而Foo本身也是一个对象，它是type实例出的对象。

#### 元类

元类是用来如何创建类的，元类就是类的类，是类的模板。就比如类是用来创建对象的，类就是对象的类，是对象的模板。元类的实例化的结果为我们用class定义的类，正如类的实例为对象。

type是python的一个内建元类，用来直接控制生成类，python中任何class定义的类其实都是type类实例化的对象。

创建类的两种方式：

方式一：使用class关键字创建

```python
class Chinese:  # Chinese = type(...)
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)


obj = Chinese('ike1', 28)
print(obj, obj.name, obj.age)
```

方式二：使用type创建

定义类的三要素：

- 类的名字
- 类的基类
- 类的名称空间

```python
# 类的名字
class_name = "Chinese"
# 类的基类
class_bases = (object,)

class_body = """
country = 'China'

def __init__(self, name, age):
    self.name = name
    self.age = age

def talk(self):
    print('%s is talking' % self.name)
"""
# 类的名称空间
class_dic = {}
# 字符串命令，全部变量，局部变量
exec(class_body, globals(), class_dic)
print(class_dic)

# 元类实例化得到一个类，类实例化得到一个对象
Chinese1 = type(class_name, class_bases, class_dic)
obj1 = Chinese1('ike', 18)
print(obj1, obj1.name, obj1.age)
```

#### 自定义元类控制类的行为

示例一：使用type定义一个类

```python
class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')

        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('注释必须有注释,且不能为空')

        super(Mymeta, self).__init__(class_name, class_bases, class_dic)


class Chinese(object, metaclass=Mymeta):
    """egon的徒弟"""
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)

```

示例二：在元类的实例中定义一个`__call__`方法，元类实例化后调用类执行，进而控制实例化的过程

```python
class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')

        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('注释必须有注释,且不能为空')

        super(Mymeta, self).__init__(class_name, class_bases, class_dic)

    # 只要实例化就执行
    def __call__(self, *args, **kwargs):  # obj = Chinese('ike', age=18)

        # print(self)  # self==Chines
        # print(args)  # args==('ike',)
        # print(kwargs)  # kwargs=={'age': 18}

        # 第一件事：造一个空对象obj
        obj = object.__new__(self)
        # 第二件事：初始化obj
        self.__init__(obj, *args, **kwargs)
        # 第三件事：返回obj
        return obj


class Chinese(object, metaclass=Mymeta):
    """中国人的注释"""
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)


obj = Chinese('ike', age=18)  # Chinese.__call__(Chinese, 'ike', age=18)
print(obj.__dict__)
```

示例三：单例模式

实现方式一：

```python
class MySQL:
    __instance = None

    def __init__(self):
        self.host = '127.0.0.1'
        self.post = 3306

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            obj = cls()
            cls.__instance = obj
        return cls.__instance

    def conn(self):
        pass

    def execute(self):
        pass


obj1 = MySQL()
obj2 = MySQL()
obj3 = MySQL()

print(obj1)
print(obj2)
print(obj3)

obj1 = MySQL.singleton()
obj2 = MySQL.singleton()
obj3 = MySQL.singleton()

print(obj1 is obj2)
```

实现方式二：元类实现

```python
class Mymeta(type):

    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')

        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('注释必须有注释,且不能为空')

        super(Mymeta, self).__init__(class_name, class_bases, class_dic)

        self.__instance = None

    def __call__(self, *args, **kwargs):
        if not self.__instance:
            # 造一个空对象
            obj = object.__new__(self)
            # 初始化self.__instance
            self.__init__(obj, *args, **kwargs)
            self.__instance = obj
        # 返回self.__instance
        return self.__instance


class Mysql(object, metaclass=Mymeta):
    """mysql"""
    __instance = None

    def __init__(self, host, post):
        self.host = host
        self.post = post

    def conn(self):
        pass

    def execute(self):
        pass


s1 = Mysql('127.0.0.1', 8080)
s2 = Mysql('127.0.0.1', 8080)

print(s1 is s2)  # True
```

### 异常

异常是错误发生的信号,一旦程序出错,并且程序没有处理这个错误,那么就会抛出异常,并且程序的运行随之终止。

一、错误分为两种：

- 语法错误：示例

    ```python
    # 语法错误一
    if
    # 语法错误二
    def test:
        pass
    # 语法错误三
    class Foo
        pass
    # 语法错误四
    print(haha)
    ......
    ```

- 逻辑错误：示例

    ```python
    # TypeError:int类型不可迭代
    for i in 3:
        pass
        
    # ValueError:输入不是int类型，值错误
    num=input(">>: ")  # 输入were
    int(num)
    
    # NameError：名字没有定义，名字错误
    aaa
    
    # IndexError：没有这个索引，索引错误
    l=['egon','aa']
    l[3]
    
    # KeyError：没有这个键，键错误
    dic={'name':'egon'}
    dic['age']
    
    # AttributeError：没有这个函数，属性错误
    class Foo:pass
    Foo.x
    
    # ZeroDivisionError:无法完成计算
    res1=1/0
    res2=1+'str'
    ```

二、异常种类：

在python中不同的异常可以用不同的类型（python中统一了类与类型，类型即类）去标识，一个异常标识一种错误。

常见的异常：

```python
AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
```

更多的异常：

```python
ArithmeticError
AssertionError
AttributeError
BaseException
BufferError
BytesWarning
DeprecationWarning
EnvironmentError
EOFError
Exception
FloatingPointError
FutureWarning
GeneratorExit
ImportError
ImportWarning
IndentationError
IndexError
IOError
KeyboardInterrupt
KeyError
LookupError
MemoryError
NameError
NotImplementedError
OSError
OverflowError
PendingDeprecationWarning
ReferenceError
RuntimeError
RuntimeWarning
StandardError
StopIteration
SyntaxError
SyntaxWarning
SystemError
SystemExit
TabError
TypeError
UnboundLocalError
UnicodeDecodeError
UnicodeEncodeError
UnicodeError
UnicodeTranslateError
UnicodeWarning
UserWarning
ValueError
Warning
ZeroDivisionError
```

三、异常处理：

强调一：错误发生的条件如果是可以预知的，此时应该用if判断去预防异常

```python
AGE=10
while True:
    age=input('>>: ').strip()
    if age.isdigit(): #只有在age为字符串形式的整数时,下列代码才不会出错,该条件是可预知的
        age=int(age)
        if age == AGE:
            print('you got it')
            break
```

强调二：错误发生的条件如果是不可以预知的，此时应该用try，异常处理机制

```python
try:
    f = open('a.txt')
    g = (line.strip() for line in f)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    f.close()

```

四、try  except的详细用法：

- 异常类只能用来处理指定的异常情况，如果非指定异常则无法处理

```python
s1 = 'hello'
try:
    int(s1)
except ValueError as e:
    print(e)
```

- 多分支：被监测的代码抛出的异常有多种可能性，针对每一种异常定制专门的处理逻辑

```python
try:
    w = [1,2,3]
    w[100]

    d = {}
    d['name']

except TypeError as e:
    print(e)

except IndexError as w:
    print(w)

print('下面的代码正常执行')
```

- 万能异常：Exception,也可以在最后加一个

```python
# 被监测的代码抛出的异常有多种可能性，针对所有的异常类型都只用一种处理逻辑，就只用Exception
try:
    w = [1,2,3]
    w[100]

    d = {}
    d['name']

except TypeError as e:
    print(e)

except IndexError as w:
    print(w)

except Exception as e:
    print('异常发生', e)
```

- 其他结构：else，finally

```python
try:
    w = [1,2,3]
    w[100]

    d = {}
    d['name']

except TypeError as e:
    print(e)

except IndexError as w:
    print(w)

except Exception as e:
    print('异常发生', e)

else:
    print('被监测的代码没有发生异常的时候执行')

finally:
    print('无论被监测的代码没有发生异常都执行')
```

- 主动触发异常：raise 异常类型（值）

```python
class People:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError('名字必须传入str类型')
        if not isinstance(age, int):
            raise TypeError('年龄必须传入int类型')
        self.name = name
        self.age = age


p = People('ike', 0)
```

- 自定义异常

```python
class MyException(BaseException):
    def __init__(self, msg):
        super(MyException, self).__init__()
        self.msg = msg

    def __str__(self):
        return '%s' % self.msg


raise MyException('自定义的异常')

```

- 断言 assert

```python
info = {}

info['name'] = 'egon'
info['age'] = 18

assert ('name' in info and 'age' in info)

if 'egon' == info['name'] and 18 == info['age']:
    print('欢迎！')
```

