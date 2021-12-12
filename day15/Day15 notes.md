# Day15 notes

## 今日内容

- 生成器
- 迭代器

## 今日概要

### 1. 生成器

在Python中,边循环边计算的后面元素机制的算法,称为生成器:**generator**.

普通生成器:

```python
f = [x * x for x in range(3)]
print(f)
# 结果:[0, 1, 4]

# 生成器创建方式
s = (x * x for x in range(3))
print(s)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
# 结果:<generator object <genexpr> at 0x0000000002920A98>
# 报错:# StopIteration
```

备注:

- 只要把列表生成式的`[]`改成`()`就创建了一个生成器.

- 可以通过`next()`函数获得生成器的下一个返回值.
- 元素超出范围后会报一个`StopIteration`的错误.

函数生成器:

函数:斐波那契

```py
def fbnq(num):
    a, b, n = 0, 1, 0
    while n < num:
        n = a + b
        a = b  # 把b的值赋值给a
        b = n  # ab+f赋值给b
        print(n)
fbnq(10)
```

生成器:斐波那契

```
def fbnq(num):
    a, b, n = 0, 1, 0
    while n < num:
        n = a + b
        a = b  # 把b的值赋值给a
        b = n  # ab+f赋值给b
        yield n


f = fbnq(5)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

```

备注:

- 把fbnq函数编程生成器,把`print`改成`yield`就可以了
- 函数是按顺序执行,遇到return或到最后一行就返回,生成器函数每次调用`next`执行,遇到yield语句就会暂停,并且把值返回,程序并没自终止,再次next调用时会接着上次继续执行.

### 2. 迭代器

可以直接用于for循环的对象称为可迭代对象：**Iterable**,可迭代的意思就是可循环/遍历.

判断一个对象是否可迭代:Iterable

```
from collections import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('web', Iterable))
print(isinstance(123, Iterable))
print(isinstance((x for x in range(10)), Iterable))
```

可以被next()函数调用并不断返回下一个值的对象称为迭代器：**Iterator**.

判断一个对象是否是迭代器:lterator

```
from collections import Iterable,Iterator

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('web', Iterator))
print(isinstance(123, Iterator))
print(isinstance((x for x in range(10)), Iterator))
```

把`list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用`iter()`函数

```
from collections import Iterable,Iterator

print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('web'), Iterator))
print(isinstance((x for x in range(10)), Iterator))
```

备注:

- 凡是可作用于`for`循环的对象都是`Iterable`类型
- 凡是可作用于`next()`函数的对象都是`Iterator`类型

- 生成器都是`Iterator`对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`,可以通过`iter()`函数获得一个`Iterator`对象
- 生成器一定是迭代器,但迭代器不一定是生成器

