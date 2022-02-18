# Python全栈开发 学习笔记

## 第一章 计算机基础

### 1.1 计算机概念

- 计算机（`computer`）[俗称](https://baike.baidu.com/item/俗称/6538506)[电脑](https://baike.baidu.com/item/电脑/124859)，是现代一种用于高速计算的电子计算机器，可以进行数值计算，又可以进行逻辑计算，还具有存储记忆功能。是能够按照程序[运行](https://baike.baidu.com/item/运行/5480697)，自动、高速处理海量数据的现代化智能电子设备。

### 1.2 计算机硬件

- 计算机基本的硬件由：CPU / 内存 / 主板 / 硬盘 / 网卡 / 显卡 等组成，只有硬件但硬件之间无法进行交流和通信；

### 1.3 操作系统类型

- Windows: 丰富的图形化桌面系统,具有丰富的资源库,适用于个人办公；
  - `windows xp`
  - `windows server`
  - `windows 7`
  - `windows 10`
- Linux: 性能好,开源,占用资源少,程序猿必备的技能,适用于服务器.
  - `ubuntu`
  - `redhat`
  - `centos`
- Mac: 界面独特,交互好,装逼神本,适用于办公.

### 1.4 解释器或编译器

编程语言的开发者写的一个工具，将用户写的代码转换成010101交给操作系统去执行。

#### 1.4.1 解释和编译型语言

解释型

- 解释器（[英语](https://baike.baidu.com/item/英语/109997)：Interpreter），又译为直译器，是一种电脑[程序](https://baike.baidu.com/item/程序)，能够把高级[编程语言](https://baike.baidu.com/item/编程语言)一行一行直接转译运行；

  解释型语言就类似于： 实时翻译，代表：`Python` /` PHP` /` Ruby` /` Perl`

编译型

- [编译器](https://baike.baidu.com/item/编译器/8853067)就是将“一种语言（通常为高级语言）”翻译为“另一种语言（通常为低级[语言](https://baike.baidu.com/item/语言/72744)）”的程序；

  编译型语言类似于：说完之后，整体再进行翻译，代表：`C `/ `C++ `/ `Java` / `Go `

### 1.5 软件(应用程序)

软件又称为应用程序，就是我们在电脑上使用的工具，类似于：记事本 / 图片查看 / 游戏；

程序员的工作：

- 通过编程,使软件代替人类的行为活动,提高人类工作效率,推动人类的发展；

![img](https://pythonav.com/media/uploads/2019/03/26/%E8%A7%A3%E9%87%8A%E5%99%A8.png)

### 1.6 进制

对于计算机而言无论是文件存储 / 网络传输输入本质上都是：二进制（010101010101），如：电脑上存储视频/图片/文件都是二进制； `QQ`/微信聊天发送的表情/文字/语言/视频 也全部都是二进制。

进制：

- 2进制，计算机内部。
- 8进制
- 10进制，人来进行使用一般情况下计算机可以获取10进制，然后再内部会自动转换成二进制并操作。
- 16进制，一般用于表示二进制（用更短的内容表示更多的数据），一版是：\x 开头。

| 二进制 | 八进制 | 十进制 | 十六进制 |
| ------ | ------ | ------ | :------- |
| 0      | 0      | 0      | 0        |
| 1      | 1      | 1      | 1        |
| 10     | 2      | 2      | 2        |
| 11     | 3      | 3      | 3        |
| 100    | 4      | 4      | 4        |
| 101    | 5      | 5      | 5        |
| 110    | 6      | 6      | 6        |
| 111    | 7      | 7      | 7        |
| 1000   | 10     | 8      | 8        |
| 1001   | 11     | 9      | 9        |
| 1010   | 12     | 10     | A        |
| 1011   | 13     | 11     | B        |
| 1100   | 14     | 12     | C        |
| 1101   | 15     | 13     | D        |
| 1110   | 16     | 14     | E        |
| 1111   | 17     | 15     | F        |
| 10000  | 20     | 16     | 10       |

---

## 第二章 Python入门

### 2.1 Python起源

- Python的创始人为`Guido van Rossum`；
- 1989年圣诞节期间，在阿姆斯特丹，Guido为了打发圣诞节的无趣，决心开发一个新的脚本解释程序，作为ABC 语言的一种继承；

### 2.2 解释器种类

由于python这门编程语言越来越火，各编程语言为了可以支持Python专门给他开发了可以快速支持Python语法的解释器

- `Cpython`（**推荐**）
  Python的官方版本，使用C语言实现，使用最为广泛，`CPython`实现会将源文件（`py`文件）转换成字节码文件（`pyc`文件），然后运行在Python虚拟机上。
- `Jyhton`
  Python的Java实现，`Jython`会将Python代码动态编译成Java字节码，然后在`JVM`上运行。
- `IronPython`
  Python的C#实现，`IronPython`将Python代码编译成C#字节码，然后在`CLR`上运行。（与`Jython`类似）
- `PyPy`
  Python实现的Python，将Python的字节码字节码再编译成机器码。
- `RubyPython`、`Brython` 等

### 2.3 环境安装

#### 2.3.1 解释器安装

- 1.打开官网:https://www.python.org/,选择Downloads

- 2.选择对应的操作系统,我用的是windows系统

- 3.根据操作系统选择对应的安装包

- 4.安装，勾选 Add Python 3.3 to PATH

<img src="https://pythonav.com/media/uploads/2019/02/21/1548322161259.png" alt="img" style="zoom:50%;" />

- 5.下一步

<img src="https://pythonav.com/media/uploads/2019/02/21/1548322484875.png" alt="img" style="zoom:50%;" />

- 6.勾选并安装

<img src="https://pythonav.com/media/uploads/2019/02/21/1548322828889.png" alt="img" style="zoom:50%;" />

- 7.安装成功

<img src="https://pythonav.com/media/uploads/2019/02/21/1548322916218.png" alt="img" style="zoom:50%;" />

- 8.进行验，打开终端,输入python，进入到交互模式,说明安装成功

![1639296246484](\Python_notes.assets\1639296246484.png)

#### 2.3.2 开发工具安装

- 下载`Pycharm`
  - 1.官网:`<http://www.jetbrains.com/pycharm/download/#section=windows>`，选择专业版下载<img src="J:\homework\Python学习笔记\Python_notes.assets\1548323345533.png" alt="img" style="zoom:50%;" />
- 2.双击安装，一路下一步,显示下图为成功<img src="J:\homework\Python学习笔记\Python_notes.assets\1548324124987.png" alt="img" style="zoom:50%;" />
- 3.首次使用![img](J:\homework\Python学习笔记\Python_notes.assets\1548326046866.png)
- 4.用户许可选择Accept![img](J:\homework\Python学习笔记\Python_notes.assets\1548326092371.png)
- 5.激活`Pycharm`
  - 激活详情`<http://idea.lanyus.com/>`页面![img](J:\homework\Python学习笔记\Python_notes.assets\1548326302535.png)
- 6.启动成功![img](J:\homework\Python学习笔记\Python_notes.assets\1548326451573.png)

### 2.4 编码基础

#### 2.4.1 编码基础

- `ascii` 【英文，8位表示一个字符】
- `unicode` 【万国码，32位 4字节表示一个字符】
- `utf-8` 【万国码的压缩版，使用1 - 4字节表示一个字符，常用的中文占用3字节，但超大字符集中的更大多数汉字要占4个字节】
- `gbk` /` gb2312`【中文占用2字节】

#### 2.4.2 解释器编码

对于Python默认解释器编码：

- `py2`：`ascii`
- `py3`：`utf-8`

如果想要修改默认编码，则可以使用：

```python
# -*- coding:utf-8 -*-
print('我是pytho2')
```

- 建议：编写文件时，保存文件要用`utf-8`格式保存。
- 注意：以什么编码保存，就要用什么编码方式打开，否则会出现乱码。

在`linux`上有一种特殊的执行方法：

```python
#! /usr/bin/env python 在Linux中指定解释器的路径
# -*- coding:utf-8 -*-
print('hello world')
```

环境头只在`linux`上生效：

运行：解释器+文件路径

- 给文件赋予一个可执行的权限
- `./a.py ` 通过文件的第一行找python解释器 = `/usr/bin/env/python a.py`

### 2.5 输出

```python
print('你想要打印的内容')
```

特殊:

```python
# python2输出:
print "hello"
# python3输出:
print("hello")
```

### 2.6 输入

在生活中，我们访问一个网页或登录`QQ`，第一步都需要输入账号和密码，在python中input就是输入内容的语法

- `python3`的写法

```python
user_name = input('username:')
msg = user_name + '我是谁'
print(msg)
```

- `python2`的写法

```python
user_name = raw_input('username:')
msg = user_name + '我是谁'
print(msg)
```

### 2.7 变量

变量是可变的，一旦定义后会加载到内存，方便以后的调用，变量定义不仅可以使用数字，还可以使用任意数据类型，但是我们一般定义的时候要遵循一定的规范，在代码中会更清晰，更整洁,容易理解。

变量定义规范：

- 变量只能包含数字、字母、下划线

- 变量不能以数字开头

- 变量不能使用python内置函数关键字 

  ```python
  [‘and’, ‘as’, ‘assert’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘exec’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘not’, ‘or’, ‘pass’, ‘print’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’]
  ```

- 变量一般使用英文，不要使用拼音

- 变量要以下划线连接两个英文单词

- 变量可以使用驼峰式命名：BaseName = 'ike'，但一般是使用下划线

建议：变量命名要见名知意，比如:name = "ike"  age = 18

```python
# 第一题
age = 18
new_age = age + 1
print(new_age)
# 第二题
name = '李静'
hobby = name + '爱吃蒜'
print(hobby)
# 第三题
age = '66'
new_age = age + '77'
print(new_age)
# 第四题(报错:字符串和整型不能相加)
age = '888'
new_age = age + 666
print(new_age)
# 第五题
age = 6
new_age = age * 2
print(new_age)
# 第六题(字符串可以相乘)
name = '李静'
new_name = name * 6
print(new_name)
# 第七题
age = 18
value = age > 19
print(value)
# 第八题(变量命名)
_ = 9
_9 = 9
9name = 'ike' # 以数字开头
True = 9 # 关键字
print = 666 # 关键字
```

### 2.8 常量

常量一旦定义，一般不会去修改。但Python中针对常量没有一个规范，程序猿一般使用变量大写来定义常量，这也是Python中的'潜规则'

```python
USER_LIST = [11,22,3]

def func():
    name = 'asdf'
    USER_LIST.append(12)
    USER_LIST.append(name)

func()
print(USER_LIST)
```

### 2.9 注释

在我们学习中，经常会对一些不好理解的东西在旁边会加一些标记或说明，在我们的代码中也是这样的。

我们写代码的时候，有些逻辑过于复杂，我们在写的时候能看懂，但随着代码量的增加，回头再让你看某一段代码。也许你不是一下能看明白的。所以在写代码的时候，我们要养成加注释的习惯。

```python
# print('hello') 这样就是对这个代码进行注释,并且这个代码不会执行
'''
print(1)
print(2)
这种就是多行注释,这样的注释也不会执行
'''
```

### 2.10 流程控制

1.初级条件语句

```python
# 请事先一个功能:让用户输入性别,如果是男,输出再见,如果是女,输出来呀来呀!
while True:
    gender = input('请输入性别:').strip()
    if gender == '男':
        print('再见!')
    else:
        print('来呀来呀!')
```

2.elif条件

```python
# 请事先一个功能:让用户输入性别,如果是男,输出再见,如果是女,输出来呀来呀!如果是人妖,找alex去,否则,滚

while True:
    gender = input('请输入性别:').strip()
    if gender == '男':
        print('再见!')
    elif gender == '女':
        print('来呀来呀!')
    elif gender == '人妖':
        print('找alex去')
    else:
        print('滚!')
    print('end')
```

3.最简单

```python
gender = input('请输入性别:').strip() # 女
if gender == '男':
	print('再见!')
```

4.练习题

```python
# 第一题:让用户输入一个数字,猜:如果数字>50,则输入大了;如果数字<=50,则输出小了.
while True:
    num = input('输入数字:').strip()
    number = int(num)
    if number > 50:
        print('大了')
    else:
        print('小了')
# 第二题:用户名密码登录
username = input('username:').strip()
password = input('password:')
if username == 'alex' and password == '123':
    print('登录成功!')
else:
    print('用户名或密码错误!')
```

---

## 第三章 基础和运算符

### 3.1 while循环

#### 3.1.1 基本循环

- 循环打印"人生苦短,我用Python'"

  ```python
  while True:
  	print('人生苦短,我用Python!')
  # 无限循环
  ```

- 通过循环，让count每次循环+1，控制循环次数

  ```python
  count = 1
  while count < 11:
      print(count)
      count += 1
  ```

- 通过循环，打印1-10

  ```python
count = 1
  while True:
      print(count)
      if count == 10:
          break
      count += 1
  ```

- 通过循环，打印1-10，但不打印7

  ```python
  count = 1
  while count <11:
  	if count != 7:
  		print(count)
  	count += 1
  ```

#### 3.1.2 break

- break代表终止当前循环，代码运行到break即终止

  ```python
  count = 1
  while True:
      print(count)
      if count == 10:
          break  # break 终止当前循环
      count += 1
  print('完了')
  ```

#### 3.1.3 continue

- continue退出当前循环，进行下一次循环

```python
count = 1
while count <= 10:
    print(count)
    continue  # 本次循环遇到continue,则不再继续往下走,而是回到while条件位置;无限循环
count += 1
```

- 练习：continue打印1-10，不打印7

```python
count = 1
while count <= 10:
    if count == 7:  # 循环到7,不再往下走,回到while条件位置继续执行.
        count += 1
        continue
    print(count)
    count += 1
```

#### 3.1.4 while else

- while else结构，while条件不满足，则执行else中的内容，break终止循环则不执行else

  ```python
  count = 1
  while count <= 10:
      print(count)
      count += 1
  else:
      print('已结束')
  ```

### 3.2 格式化输出

- %s,占位符，指的是字符串

  ```python
  name = input('请输入姓名:')
  age = input('请输入年龄:')
  job = input('请输入职业:')
  hobby = input('请输入爱好:')
  msg = '''
  ------------ info of %s Li ----------
  Name  : %s
  Age   : %s 
  job   : %s 
  Hobbie: %s 
  ------------- end ----------------'''
  print(msg%(name,name,age,job,hobby))
  ```

- %d,占位符，指的是数字

  ```python
  name = input('>>>')
  s1 = '1234%d'%int(name)
  print(s1)
  ```

- %%，在需求中要求有%符号，在代码中要用2个%来转义

  ```python
  name = 'alex'
  print('%s的手机电量是100%%' % name)
  ```

- %f，占位符，指的是小数

  ```python
  name = input('>>>:')
  s1 = '12345,%f' % int(name)
  print(s1
  ```

### 3.3 运算符

计算机可以进行的运算有很多种，可不只加减乘除这么简单，运算按种类可分为算数运算、比较运算、逻辑运算、赋值运算、成员运算、身份运算、位运算。

#### 3.3.1 算数运算

- +(相加)

  ```python
  a = 10
  b = 30
  print(a + b)
  ```

- -(相减)

  ```python
  a = 10
  b = 30
  print(a - b)
  ```

- *(相乘)

  ```python
  a = 10
  b = 30
  print(a * b)
  ```

- /(相除)

  ```
  a = 10
  b = 30
  print(a / b)
  ```

- %(取模，只取余数)

  ```python
  value = 11 % 3
  print(value)
  ```

- //(取整数)

  ```python
  value = 11 // 3
  print(value)
  ```

- **(次幂)

  ```python
  value = 2 ** 8
  print(value)
  ```

- 练习

  ```python
  # 练习题:打印1-100之间的奇数
  count = 1
  while count < 101:
      if count % 2 == 1:
          print(count)
      count += 1
  # 练习题:打印1-100所有的数相加
  total = 0
  count = 1
  while count < 101:
      total = total + count
      count += 1
  print(total)
  # 练习题:打印1-100之内减偶数加奇数
  total = 0
  count = 1
  while count < 101:
      if count % 2 == 1:
          total = total + count
      elif count % 2 == 0:
          total = total - count
      count += 1
  print(total)
  ```

#### 3.3.2 比较运算

- `==`(相等)

  ```python
  a = 10
  b = 11
  print(a == b)
  ```

- `!=` 或` <>`(不相等)

  ```python
  a = 10
  b = 11
  print(a != b)  # 或 print(a <> b)
  ```

- `>`(大于)

  ```python
  a = 10
  b = 11
  print(a > b)
  ```

- `<`(小于)

  ```python
  a = 10
  b = 11
  print(a < b)
  ```

- `<=`(小于等于)

  ```python
  a = 10
  b = 11
  print(a <= b)
  ```

- `>=`(大于等于)

  ```python
  a = 10
  b = 11
  print(a >= b)
  ```

#### 3.3.3 赋值运算符

- `=`(赋值)

  ```python
  a = 10
  b = 11
  c = a+b
  print(c)
  ```

- `+=`(加法赋值)

  ```python
  a = 10
  b = 11
  b += a  # 等同于 b = b + a
  print(b)
  ```

- `-=`(减法赋值)

  ```python
  a = 10
  b = 11
  b -= a # 等同于 b = b - a
  print(b)
  ```

- `*=`(乘法赋值)

  ```python
  a = 10
  b = 11
  b *= a # 等同于 b = b * a
  print(b)
  ```

- `/=`(除法赋值)

  ```python
  a = 10
  b = 11
  b /= a # 等同于 b = b / a
  print(b)
  ```

- `%=`(取模赋值)

  ```python
  a = 10
  b = 11
  b %= a # 等同于 b = b % a
  print(b)
  ```

- `**=`(次幂赋值)

  ```python
  a = 10
  b = 11
  b **= a
  print(b)
  ```

- `//=`(取整赋值)

  ```python
  a = 10
  b = 11
  b //= a
  print(b)
  ```

#### 3.3.4 逻辑运算

- 一般用在判断

  ```python
  if 1 > 0 and 5 > 4:
  	print('打印了')
  ```

- 特殊用在取值

  - or

  ```python
  # 第一个值如果是转换成布尔值,如果是真,则value=第一个值
  # 第一个值如果是转换成布尔值,如果是假,则value=第二个值
  # 如果有多个or条件,则从坐左到右依次进行上述的流程
  # 注意:0在or中为假
  # 示例:
      v1 = 0 or 1
      v2 = 8 or 10
      v3 = 0 or 9 or 10
  ```

  - and

  ```python
  # 如果第一个值转换成布尔值是True,则value=第二个值
  # 如果第一个值转换成布尔值是False,则value=第一个值
  # 如果有多个and条件,则从左到右依次进行上述流程
  # 注意:0 和 ""在and中为假
  # 示例:
      v1 = 1 and 9
      v2 = 1 and 0
      v3 = 0 and 7
      v4 = 0 and ''
      v5 = 1 and 0 and 9
  ```

  - and 和 or 结合

  ```python
  # 先看and后看or
  v1 = 1 and 9 or 0 and 6
  ```

  总结：优先级在没有()的情况下，not优先级最高，and优先级高于or，优先级的顺序为

  ```python
  # () > not > and > or
  ```

#### 3.3.5 成员运算

- 判断子元素是否在原字符串/字典/列表/集合中：

- in

  ```python
  print('i' in 'ike')
  ```

- not in

  ```python
  print('i' not in 'ike')
  ```

### 3.4 编码

- ASCII表

![img](https://img2018.cnblogs.com/blog/1369254/201902/1369254-20190227145507982-920914642.png)

- ASCII（`American Standard Code for Information Interchange`，美国信息交换标准代码）是基于[拉丁字母](http://baike.baidu.com/item/拉丁字母)的一套电脑编码系统，主要用于显示现代[英语](http://baike.baidu.com/item/英语/109997)和其他[西欧](http://baike.baidu.com/item/西欧)语言。它是现今最通用的单字节编码系统，并等同于[国际](http://baike.baidu.com/item/国际)标准`ISO`/`IEC 646`。

  由于计算机是美国人发明的，因此，最早只有127个字母被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为`ASCII`编码，比如大写字母 `A`的编码是`65`，小写字母 `z`的编码是`122`。后128个称为[扩展ASCII](http://baike.baidu.com/item/扩展ASCII)码。

  那现在我们就知道了上面的字母符号和数字对应的表是早就存在的。那么根据现在有的一些十进制，我们就可以转换成二进制的编码串。

- 正是由于这些字符串长的长，短的短，写在一起让我们难以分清每一个字符的起止位置，所以聪明的人类就想出了一个解决办法，既然一共就这255个字符，那最长的也不过是11111111八位，不如我们就把所有的二进制都转换成8位的，不足的用0来替换。

  这样一来，刚刚的两个空格一个对勾就写作000000000000000011111011，读取的时候只要每次读8个字符就能知道每个字符的二进制值啦。

  在这里，每一位0或者1所占的空间单位为bit(比特)，这是计算机中最小的表示单位

  每8个bit组成一个字节，这是计算机中最小的存储单位(毕竟你是没有办法存储半个字符的)

  ```python
  bit位，计算机中最小的表示单位
  8bit = 1bytes字节，最小的存储单位，1bytes缩写为1B
  1KB=1024B
  1MB=1024KB
  1GB=1024MB
  1TB=1024GB
  1PB=1024TB
  1EB=1024PB
  1ZB=1024EB
  1YB=1024ZB
  ```

- **GBK和GB2312**

  `GBK`，国标码占用2个字节。 对应ASCII码 `GBK`直接兼容。因为计算机底层是用英文写的。你不支持英文肯定不行。而英文已经使用了`ASCII`码。所以`GBK`要兼容`ASCII`。
  这里`GBK`国标码，前⾯的ASCII码部分。由于使⽤两个字节，所以对于ASCII码⽽言。前9位都是0

  ```python
  字母A:0100 0001 # ASCII字母A:0000 0000 0100 0001 # 国标码
  ```

  随着全球化的普及，发展到欧洲，亚洲等国家，发现这些根本不够用，所以创建了万国码。
  因为全球语言很多，`ascii`不足以存储这么多对应关系，创建了一个超级密码本：万国码`unicode`

  ```python
  8 位 == 1个字节.hello h一个字符,e一个字符,he就不是一个字符.中国:中是一个字符,国是一个字符.
  ```

  Unicode

  Unicode：万国码 可以统计世界上的所有语言，一般用于内存计算，最少2个字节，最多4个字节

  - `ecs2 `   2**16
  - `ecs4`    2**32

- **UTF-8**

  对Unicode进行升级： utf-8，utf-8 用最少用8位数，去表示一个字符。
  英文：8位，1个字节表示。
  欧洲文字：16位，两个字节表示一个字符。 
  中文，亚洲文字：24位，三个字节表示。
  

utf-16 用最少用16位数。

gbk：国标，只能中国人自己用，一个中文用16位，两个字节表示。

---

## 第四章 数据类型

### 4.1 整型(int)

```python
age = 18
```

- python2

  - int

    - 32位电脑：-2147483648～2147483647
    - 64位电脑：-9223372036854775808～9223372036854775807
    - 超出范围后python自动将其转换成long（长整形）

  - 整型除法只能保留整数位

    ```python
    from __future__ import divisio
    v = 9 /2
    print(v)
    ```

- python3

  - 只有int
  - 整型除法只能保留所有

### 4.2 布尔值(bool)

判断真假：

- 只有两个值：True/False
- 转换
  - 数字转布尔：0是False，其他都是True
  - 字符串转布尔：“”是False，其他都是True
  - 空列表[]/元组()/空字典{}/空集合set()都是False

### 4.3 字符串(str)

字符串是写代码中最常见的，python内存中的字符串是按照：`unicode` 编码存储。对于字符串是不可变，有序的数据类型。

#### 4.3.1 字符串方法

- `.upper()`转换大写

  ```python
  v = 'ike'
  v1 = v.upper()
  print(v1)
  v2 = v.isupper() # 判断是否全部是大写
  print(v2)
  ```

- `.lower()`转换小写

  ```python
  v = 'ike'
  v1 = v.lower()
  print(v1)
  v2 = v.islower() # 判断是否全部是小写
  print(v2)
  
  ############ 了解即可
  v = 'ß'
  # 将字符串变小写（更牛逼）
  v1 = v.casefold()
  print(v1) # ss
  v2 = v.lower()
  print(v2)
  ```

- `.join()`字符串拼接

  ```python
  name = 'alex'
  print('_'.join(name))
  ```

- `.isnumeric()`判断是否是10进制的数

  ```python
  v = '1'
  # v = '二'
  # v = '②'
  v1 = v.isdigit()  # '1'-> True; '二'-> False; '②' --> True
  v2 = v.isdecimal() # '1'-> True; '二'-> False; '②' --> False
  v3 = v.isnumeric() # '1'-> True; '二'-> True; '②' --> True
  print(v1,v2,v3)
  # 以后推荐用 isdecimal 判断是否是 10进制的数。
  
  # ############## 应用 ##############
  
  v = ['alex','eric','tony']
  
  for i in v:
      print(i)
  
  num = input('请输入序号：')
  if num.isdecimal():
      num = int(num)
      print(v[num])
  else:
      print('你输入的不是数字')
  ```

- `.isalnum()`判断是不是字母和数字

  ```python
  name = 'alex7dasx'
  new_name = name.isalnum()
  print(new_name)
  # 判断是不是字母和数字,返回结果是布尔值
  ```

- `.isalpha()`判断是不是纯字母和汉字

  ```python
  name = 'alexdasx'
  new_name = name.isalpha()
  print(new_name)
  # 判断是不是纯字母和汉字,返回的是布尔值
  ```

- `.strip()`  /` .lstrip()`  / `.rstrip()`去空和换行

  ```python
  v1 = "alex "
  print(v1.strip())
  
  v2 = "alex\t"
  print(v2.strip())
  
  v3 = "alex\n"
  print(v3.strip())
  
  v1 = "alexa"
  print(v1.strip('al'))
  ```

- `.replace`("被替换的字符/子序列","要替换为的内容")  /  `.replace`("被替换的字符/子序列","要替换为的内容", 前几个)

  ```python
  s = 'alex'
  print(s.replace('a', 'A'))
  ```

- `.split`('根据什么东西进行分割')  /  `.split`('根据什么东西进行分割', 前几个 )  / `rsplit `

  ```python
  name = 'alexdasx'
  new_name = name.split("x")
  print(new_name)
  #通过x将字符串name进行切割
  ```

- `.capitalize()`首字母大写

  ```python
  name = 'alexdasx'
  new_name = name.capitalize()
  print(new_name)
  # 首字母大写
  ```

- `.swapcase()`字符串大小写转换

  ```python
  name = 'alexdasx'
  new_name = name.swapcase()
  print(new_name)
  # 字符串大小写转换
  ```

- `startswith()`首字母大写

  ```python
  s = 'alex'
  print(s.startswith('a'))
  ```

- `.endswith()`最后一个字母大写

  ```python
  s = 'alex'
  print(s.endswith('x'))
  ```

- `.encode()`编码

  ```python
  s = 'alex'
  print(s.encode('utf-8'))
  ```

- `.decode()`解码

  ```python
  v = b'\xe6\xad\xa5\xe5\xb1\xa5\xe5\x86\xb0\xe5\xb7\x9d'
  v1 = v.decode('utf-8')
  print(v1)
  ```

- `.count()`统计

  ```python
  name = 'alexdasx'
  new_name = name.count('a')
  print(new_name)
  # 统计name这个字符串中a出现的次数
  ```

- `.find()`通过元素查找下标

  ```python
  name = 'alexdasx'
  new_name = name.find('e')
  print(new_name)
  # 通过元素查找下标,不存在就返回-1
  ```

- `.format()`字符串格式化

  ```python
  name = 'abcdefg{}'
  new_name = name.format('你说的对')
  print(new_name)
  # 字符串格式化
  ```

- `len()`长度

  ```python
  v = "abcdefg"
  v1 = v[0]  # 0 1 2 3 ... 从前向后
  v2 = v[-1] # -1 -2 -3 ...从后向前
  ```

- 切片

  ```python
  v = "abcdefg"
  
  # v1 = v[2:4] # 取值规则为左闭右开
  # v2 = v[3:6]
  # v2 = v[3:-1]
  # v2 = v[3:]
  # v2 = v[:-1]
  # print(v2)
  
  # 示例: 取最后两个字符
  # data = input('请输入：')
  # 方式一
  # v = data[-2:]
  # print(v)
  # 方式二
  # total_len = len(data)
  # v = data[total_len-2:total_len]
  # print(v)
  ```

- 步长

  ```python
  name = 'oldboyalex'
  # val = name[0:-1:2]
  # val = name[1:-1:2]
  # val = name[1::2]
  # val = name[::2]
  # val = name[-1:0:-2]  # 倒着隔步
  # 将字符串反转
  # val = name[::-1]
  val = ''.reversed(name)
  print(val)
  ```

- for循环

  ```python
  name = 'alex'
  for item in name:
      print(item)
  ```

  ```python
  name = 'alex'
  for item in name:
      print(item)
      break
      print(234)
  ```

  ```python
  name = 'alex'
  for item in name:
      print(item)
      continue
      print(234)
  ```

  ```python
  # 练习题
  # 请打印：1-10 跳过7
  for i in range(1, 11):
      if i == 7:
          pass
      else:
          print(i)
  ```

注意：for和while的应用场景，有穷尽优先使用for，无穷尽用while

- 练习

  ```python
  """
  需求：让用户输入任意字符串，获取字符串之后并计算其中有多少个数字。
  """
  content = input('请输入内容:')
  index = 0
  total = 0
  while True:
      val = content[index]
      value = val.isdigit()
      if value:
          total += 1
      if index +1 == len(content):
          print('共输入{}个字符.'.format(len(content)))
          break
      index += 1
  print('共输入{}个数字.'.format(total))
  ```

### 4.4 列表

列表是python的基础数据类型之一，它是以[ ]括起来, 每个元素用 "," 隔开而且可以存放各种数据类型。列表相比于字符串，不仅可以储存不同的数据类型，而且可以储存大量数据，列表是有序的，可变的数据类型。

- 如果想要表示两个同学 user = "张三","李四"

- 以后想要表示多个"事物"，可以使用列表。

  ```python
  user ＝ ["张三","李四",89]
  ```

#### 4.4.1 列表的方法

- `len()`

  ```python
  user ＝ ["张三","李四",89]
  val ＝ len(user)
  print(val)  # 3
  ```

- 索引

  ```python
  user ＝ ["张三","李四",89]
  val ＝ user[0]
  print(val)  # 张三
  ```

- 切片

  ```python
  user ＝ ["张三","李四",89]
  val ＝ user[0:2]
  print(val)
  ```

- 删除系列（数字、布尔、字符串除外）

  ```python
  # 方式一
  users = ["张三", "李四", "王五", "王五"]
  users.pop(1)
  print(users)
  # 方式二
  users = ["张三", "李四", "王五", "王五"]
  del users[1]
  print(users)
  # 方式三
  users = ["张三", "李四", "王五", "王五"]
  users.remove('张三')
  print(users)
  ```

  注意:

  - 字符串本身不能修改或删除(不可变类型)
  - 列表是可变类型

- 修改（字符串、数字、布尔除外）

  ```python
  users = ["张三", "李四", "王五", "王五"]
  users[2] = 66
  
  users[0] = '中国'
  users[0][1]
  ```

- 步长

  ```python
  user ＝ ["张三","李四",89]
  val ＝ user[0:2:2]
  print(val) 
  ```

- for循环

  ```python
  # 方式一：
  users = ["张三","李四","王五"]
  count = 0
  for i in users:
      print(count, i)
      count += 1
  
  # 方式二：
  users = ["张三","李四","王五"]
  for index in range(0, len(users)):
      print(index, users[index])
  ```

- 登录验证示例

  ```python
  # 录入用户名和密码
  users = []
  for i in range(0, 2):
      name = input('username and password:').strip()
      users.append(name)
  print(users)
  
  # 用户名和密码校验
  
  user = input('username:').strip()
  pwd = input('password:').strip()
  for item in users:
      res = item.split(',')
      print(res)
      username = res[0]
      password = res[1]
      if user == username and pwd == password:
          print('登录成功')
          break
  ```

- insert()添加

  ```python
  users = ["张三","李四","王五"]
  users.insert(1, '赵八')
  	print(users)
  # insert,在指定索引位置插入元素
  ```

- append()追加

  ```python
  user = []
  while True:
      name = input('username:').strip()
      user.append(name)  # 追加一个元素
      print(user)
  ```

- clear()清除

  ```python
  users = ["张三", "李四", "王五", "王五"]
  users.clear()
  print(users)
  ```

- extend()循环追加到列表中

  ```python
  ls = [1,2,3]
  ls2 = [4,5,6]
  ls.extend(ls2)
  print(ls)
  ```

- reverse()反转

  ```python
  v1 = [1, 2, 3, 4, 5]
  print(v1)
  v1.reverse()
  print(v1)
  ```

- sort()排序 reverse=false 从小到大(默认是false) reverse=true 从大到小排序

  ```python
  V1 = [1, 2, 3, 4988944, 5, 6565, 9999]
  print(v1)
  # v1.sort(reverse=False)  # 从小到大(默认)
  # v1.sort(reverse=True)  # 从大到小
  print(v1)
  ```

- index()索引取值

  ```python
  li = [1,2,3,4,84,5,2,8,2,11,88,2]
  n = li.index(5)
  print(n)
  ```

### 4.5 元祖

对于容器型数据类型list，无论谁都可以对其增删改查，那么有一些重要的数据放在list中是不安全的，所以需要一种容器类的数据类型存放重要的数据，创建之初只能查看而不能增删改，这种数据类型就是元祖。

元祖：俗称不可变的列表，又被成为只读列表,元祖也是python的基本数据类型之一，元组是不可变，有序数据类型。

#### 4.5.1 元组的方法

- 元组的书写规范

  ```python
  users = ["张三", "李四", "王五", "王五"] # 列表
  users = ("张三", "李四", "王五", "王五") # 元组（不可变）
  ```

- 索引（排除：`int`、`bool`）

  ```python
  users = ("张三", "李四", "王五", "王五")
  print(users[0])
  print(users[-1])
  ```

- 切片（排除：`int`、`bool`）

  ```python
  users = ("张三", "李四", "王五", "王五")
  print(users[0:3])
  ```

- 步长（排除：`int`、`bool`）

  ```python
  users = ("张三", "李四", "王五", "王五")
  print(users[0:3:2])
  ```

- 删除（排除：`str`、`int`、`bool`、`tuple`）

- 修改（排除：`str`、`int`、`bool`、`tuple`）

- for循环（排除：`int`、`bool`）

  ```python
  users = ("张三", "；李四", "王五", "王五")
  for item in users:
  	print(item)
  ```

- 长度（排除：`int`、`bool`）

  ```python
  users = ("张三", "李四", "王五", "王五")
  print(len(users))
  ```

- 嵌套

  ```python
  v1 = (11,22,33)
  v1[1] = 9 # 错误
  v1 = 999 # 正确
  
  # 可以嵌套
  v1 = (11,22,33,(44,55,66),(11,66,(99,88,(55,))))
  # 嵌套
  v1 = [11,22,33,(44,55,66)]
  v1[-1][1] = 887 # 错误
  v1[-1] = 123 # 正确
  # 嵌套
  v1 = (11,22,33,[44,55,66])
  v1[-1] = 666 # 错误
  v1[-1][2] = 777 # 正确
  ```

### 4.6 字典

字典(`dict`)是python中唯一的一个映射类型。他是以{ }括起来的键值对组成。

字典中的key是可哈希的，不可变的，字典是无序的数据类型。

#### 4.6.1 字典的方法

- 帮助用户去表示一个事物的信息(事物是有多个属性)

  ```python
  info = {"name": "WuSir", "age": 18, "gender": "男", "hobby": "同桌"} # 键值对
  # 请输出:我的名字叫%s,几年%s岁,性别%s,喜欢%s
  ```

- 字典格式：

  ```python
  info = {"name": "WuSir", "age": 18, "gender": "男", "hobby": "同桌"} # 键值对
  # 取值
  info["name"]
  info["age"]
  ```

  ```python
  # 练习题
  userinfo = {'username': 'wusir', 'password': 'oldboy'}
  user = input('usernam:')
  pwd = input('password:')
  if userinfo['username'] == user and userinfo['password'] = pwd:
  	print('登录成功')
  else:
  	print('登录失败')
  ```

- 字典方法

  ```python
  info = {"name": "WuSir", "age": 18, "gender": "男", "hobby": "同桌"}
  print(info)
  ```

  - keys--->获取字典中所有的键  ["name","age","gender","hobby"]

    ```python
    for item in info.keys():
        print(item)
    ```

  - values--->获取字典中所有的值  ["`WuSir`",18,男,同桌]

    ```python
    for item in info.values():
        print(item)
    ```

  - items--->获取字典中所有的键值对

    ```python
    for v1, v2 in info.items():
        print(v1, v2)
    ```

  - get()--->获取字典中键的值

    ```python
    # None数据类型,表示空(无任何功能,专门用于提供空值)
    info = {'k1': 'v1', 'k2': 'v2'}
    v2 = info.get('k33')  # None就是Python中的空
    v3 = info.get('k33', '没有')  # 空,打印没有
    print(v2)
    print(v3)
    ```

  - pop()--->删除

    ```python
    # info = {'k1': 'v1', 'k2': 'v2'}
    #
    # res = info.pop('k2')
    # print(info, res)
    #
    # del info['k1']
    # print(info)
    ```

    - update--->键不存在,则添加,存在,则更新

    ```python
    info = {'k1': 'v1', 'k2': 'v2'}
    
    # 键不存在,则添加,存在,则更新
    info.update({'k3': 'v3', 'k4': 'v4', 'k5': 'v5', 'k2': 999})
    print(info)
    ```

  - clear()--->清除

    ```python
    info = {'k1': 'v1', 'k2': 'v2'}
    info.clear()
    print(info)
    ```

  - len--->长度

    ```python
    info = {"name": "WuSir", "age": 18, "gender": "男", "hobby": "同桌"}
        print(len(info))
    ```

  - 键取值

    ```python
    info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
    info['name']
    info['age']
    ```

  - 切片【无】

  - 步长【无】

  - for循环

    ```python
    info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
    
    for item in info.keys():
        print(item)
    
    for item in info.values():
        print(item)
    
    for k,v in info.items():
        print(k,v)
    ```

  - 修改

    ```python
    # 修改值
    info = {"name": "WuSir", "age": 18, "gender": "男", "hobby": "同桌"}
    info['age'] = 28
    print(info)
    
    # 改建--->删除后再增加
    del info['gender']
    info['gender'] = '女'
    ```

  - 删除

    ```python
    info = {"name": "WuSir", "age": 18, "gender": "男", "hobby": "同桌"}
    del info['hobby']
    print(info)
    ```

  - 判断一个字符串是否有敏感字符?

    - str

    ```python
    v = 'Python全栈21期开发'
    if "全栈" in v:
    	print('含敏感字符')
    ```

    - list/tuple

    ```python
    v = ['alex', 'oldboy', '苍老师', '麻花藤']
    if '麻花藤' in v:
    	print('含敏感字符')
    ```

    - dict

    ```python
    v = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
    # 默认按照键判断,即:判断x是否是字典的键
    if i in v:
    	pass
    	
    # 请判断:v1是否在其中
    if i in v:
    	pass
    	
    # 请判断:v2是否在其中
    # 方式一
    flag = '不存在'
    for v in v.valuse():
    	if v == 'v2':
    		flag = '存在'
    print(flag)
    
    # 方式二
    if 'v2 in list(v.valuse())  # 强制转换成列表['v1', 'v2', 'v3'...]
    	pass
    # 请判断:k2,v2是否在其中
    val = v.get('k2')
    if val == 'v2':
    	print('存在')
    else:
    	print('不存在')
    ```

  - 练习题

    ```python
    # 让用户输入任意字符串,然后判断此字符串是否包含指定的敏感字符
    char_list = ['张三', '李四', '渣渣辉']
    cont = input('请输入内容:')
    
    flag = True
    for i in char_list:
        if i in cont:
            flag = False
            break
    if flag:
        print(cont)
    else:
        print('敏感字符')
    # 示例:
    # 1.昨天最后一题
    # 2.判断'v2'是否在字典的value中
    # 3.敏感字
    ```

  - fromkeys

    ```python
    dic = {}
    dic1 = dic.fromkeys(['a','b','c'],['你好'])
    print(dic1)
    # 结果  {'a': ['你好'], 'b': ['你好'], 'c': ['你好']}
    '''
    fromkeys里第一个参数是可迭代的对象,里边的每个元素就是字典中的健,第二个参数就是值 现在创建的字典中后边的值用的是同一个
    '''
    dic1['a'].append('我好')
    print(dic1)
    # 结果 {'a': ['你好', '我好'], 'b': ['你好', '我好'], 'c': ['你好', '我好']}
    ```

### 4.7 集合

set集合是python的一个基本数据类型，set中的元素是不重复的。无序的，里边的元素必须是可hash的(`int`, `str`, `tuple`,`bool`)。

注意：set本身是不可hash的，set是可变的。

#### 4.7.1 集合的方法

Python不支持dict的key为list或dict类型，因为list和dict类型是unhashable（不可哈希）的。

```python
set1 = {'1','alex',2,True,[1,2,3]} # 报错
set2 = {'1','alex',2,True,{1:2}} # 报错
set3 = {'1','alex',2,True,(1,2,[2,3,4])} # 报错

# TypeError: unhashable type: 'list'
```

- set中的元素是不重复的，且无序的。

  ```python
  s = {"周杰伦", "周杰伦", "周星星"}
  print(s)
  结果:
  {'周星星', '周杰伦'}
  ```

- 使用这个特性。我们可以使用set来去掉重复

  ```python
  # 给list去重复
  lst = [45, 5, "哈哈", 45, '哈哈', 50]
  lst = list(set(lst)) # 把list转换成set, 然后再转换回list
  print(lst)
  ```

- add()增加

  ```python
  v = {1, 2}
  v.add('zhangsan')
  v.add('lisi')
  print(v)
  ```

- discard()删除

  ```python
  v = {1, 2, 'zhangsan'}
  v.discard('zhangsan')
  print(v)
  ```

- update()批量添加,更新

  ```python
  v = {1, 2, 'zhangsan'}
  v.update({11, 22, 33})
  print(v)
  ```

- intersection()交集  &

  ```python
  v = {1, 2, 'zhangsan'}
  v1 = v.intersection({1, 2, 3})
  print(v1)
  ```

- union()并集  |

  ```python
  v = {1, 2, 'zhangsan'}
  v1 = v.union({1, 2, 3})
  print(v1)
  ```

- difference()差集  -

  ```python
  v = {1, 2, 'zhangsan'}
  v1 = v.difference({1, 2, 3})
  print(v1)
  ```

- symmetric_difference(对称差集)  ^

  ```python
  v = {1, 2, 'zhangsan'}
  v1 = v.symmetric_difference({1, 2, 3})
  print(v1)
  ```

- pop()删除

  ```python
  s = {1,2,3,4}
  s.pop()
  print(s)
  ```

- remove()删除

  ```python
  s = {1,2,3,4,'alex'}
  s.remove('alex')
  print(s)
  ```

- clear()清除

  ```python
  s = {1,2,3,4}
  s.clear()
  print(s)
  ```

- len(长度)

  ```python
  v = {1, 2, 'zhangsan'}
  print(len(v))
  ```

- for循环

  ```python
  v = {1, 2, 'zhangsan'}
  for i in v:
      print(i)
  ```

- 嵌套问题

  ```python
  # 1.列表/字典/集合 -->不能放在集合中,不能做为字典的key(unhashable)
  # info = {1, 2, 3, True, '里脊', None, {'sss', 22}}
  # print(info)
  
  # 2.hash--->哈希是怎么回事?
  # 因为在内部会将值进行哈希算法并得到一个数值(对应的内存地址),以后用于快速查找
  
  # 3.特使情况 False/True 和 0/1 会去重
  # info = {1, 2, 3, False, '里脊', None, }
  # print(info)
  
  info = {
      1: '中国',
      True: '世界'
  }
  print(info)
  ```

### 4.8 内存相关

- 示例一：

  ```python
  v1 = [11, 22, 33]
  v2 = [11, 22, 33]
  
  v1 = 666
  v2 = 666
  
  v1 = 'abcd'
  v1 = 'adsd'
  # 按理 v1 和 v2 应该是不同的内存地址,特殊:
  1.整型: -5 ~ 256  ---python机制会重新开辟内存。
  2.字符串: "alex",'asfasd asdf asdf d_asdf '   "f_*" * 3  ---python机制会重新开辟内存。
  ```

- 示例二：

  ```python
  v1 = [11, 22, 33, 44]
  print(v1)
  v1 = [55, 66, 78]
  print(v1)
  ```

- 示例三：

  ```python
  v1 = [88, 99]
  v2 = v1
  
  # 练习1:(内部修改)
  v1 = [88, 99]
  v2 = v1
  v1.append(777)
  print(v2)
  
  # 练习2:(重新赋值)
  v1 = [88, 99]
  v2 = v1
  v1 = [1, 2, 3]
  print(v2)
  
  # 练习3:(重新赋值)
  v1 = 'alex'
  v2 = v1
  v1 = 'peiqi'
  print(v2)
  ```

- 示例四：

  ```python
  v1 = [1, 2, 3]
  value = [11, 22, v1]
  
  # 练习题1:
  v1.append(9)
  print(value) # [11, 22, [1, 2, 3, 9]]
  
  # 练习题2:
  value[2].append(999)
  print(v1)  # [1, 2, 3, 999]
  
  # 练习题3:
  v1 = 999
  print(values)  # [11, 22, [1, 2, 3]]
  
  # 练习题4:
  value[2] = 666
  print(v1)  # [1, 2, 3]
  ```

- 示例五：

  ```python
  v1 = [1, 2]
  v2 = [2, 3]
  v3 = [11, 22, v1, v2, v1]
  ```

- 查看内存地址

  ```python
  """
  v1 = [1,2,3]
  v2 = v1
  v1.append(999)
  print(v1,v2)
  print(id(v1),id(v2))
  """
  
  """
  v1 = [1,2,3]
  v2 = v1
  print(id(v1),id(v2))
  v1 = 999
  print(id(v1),id(v2))
  """
  ```

- 问题: == 和 is 有什么区别?

  - == 用于比较直是否相等.
  - is用于比较内存地址是否相等.

### 4.9 深浅拷贝

- **浅拷贝(copy)：** 拷贝父对象，不会拷贝对象的内部的子对象。

- **深拷贝(deepcopy)：** copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象 

- 浅拷贝

  ```python
  # 浅拷贝
  import copy
  v1 = [1, 2, 3, 4, [11, 22, 33, 44]]
  v2 = copy.copy(v1)
  print(id(v1), id(v2))
  print(id(v1[4]), id(v2[4]))
  ```

- 深拷贝

  ```python
  import copy
  v1 = [1, 2, 3, 4, [11, 22, 33, 44]]
  v2 = copy.deepcopy(v1)
  print(id(v1), id(v2))
  print(id(v1[4]), id(v2[4]))
  ```

示例：浅拷贝

```python
>>>a = {1: [1,2,3]}
>>> b = a.copy()
>>> a, b
({1: [1, 2, 3]}, {1: [1, 2, 3]})
>>> a[1].append(4)
>>> a, b
({1: [1, 2, 3, 4]}, {1: [1, 2, 3, 4]})
```

深拷贝：

```python
>>>import copy
>>> c = copy.deepcopy(a)
>>> a, c
({1: [1, 2, 3, 4]}, {1: [1, 2, 3, 4]})
>>> a[1].append(5)
>>> a, c
({1: [1, 2, 3, 4, 5]}, {1: [1, 2, 3, 4]})
```

- 练习

  ```python
  import copy
  
  # 练习1
  v1 = [1, 2, 3]
  v2 = copy.copy(v1)
  print(v1 == v2)  # true
  print(v1 is v2)  # false
  print(v1[0] is v2[0])  # true
  
  # 练习2
  v1 = [1, 2, 3]
  v2 = copy.deepcopy(v1)
  print(v1 == v2)  # true
  print(v1 is v2)  # false
  print(v1[0] is v2[0])  # true
  
  # 练习3
  v1 = [1, 2, 3, {'k1': 123, 'k2:': 456}]
  v2 = copy.deepcopy(v1)
  print(v1 == v2)  # True
  print(v1 is v2)  # False
  print(v1[0] is v2[0])  # True
  print(v1[3] == v2[3])  # True
  print(v1[3] is v2[3])  # False
  # 总结:
  # 浅拷贝:只拷贝第一层
  # 深拷贝:拷贝嵌套层次中的所有可变类型
  ```

- 特殊情况

  ```python
  # 练习一
  import copy
  v1 = (1, 2, 3, 4)
  v2 = copy.copy(v1)
  print(id(v1), id(v2))
  
  v3 = copy.deepcopy(v1)
  print(id(v1), id(v3))
  # 练习二
  v1 = (1, 2, 3, [1, 2, 3], 4)
  v2 = copy.copy(v1)
  print(id(v1), id(v2))
  v3 = copy.deepcopy(v1)
  print(id(v1), id(v3))
  ```

---

## 第五章 文件操作

### 5.1 文件的基本操作

```python
# ====================读取======================
# 打开
# f = open('log.txt', mode='rt', encoding='utf-8')
# 读取内容
# f1 = f.read()
# print(f1)
# 关闭
# f.close()

# ====================写入=======================
# f = open('log.txt', mode='wt', encoding='utf-8')
# 写入内容
# f.write('写入内容')
# f.close()

# ====================追加=======================
# f = open('log.txt', mode='at', encoding='utf-8')
# f.write('kljl')
# f.close()

# -----------------------------------------------
# 方式一:
# 打开文件
f = open('文件存放的路径', mode = 'r\w\a', encoding = '文件原来写入时的编码')

# 操作
data = f.read() # 读取文件内容存放到内存
f.write('要写入的内容')

# 关闭
f.close() # 关闭文件

# 方式二:
with open('a.txt',mode='a',encoding='utf-8') as v:
    data = v.read()
	# 缩进中的代码执行完毕后，自动关闭文件
```

### 5.2 文件的打开模式

- 只读：`r`、`rt`、`rb` （用）
  - 存在，读
  - 不存在，报错
- 只写：`w`、`wt`、`wb`（用）

  - 存在，清空再写
  - 不存在，创建再写

- 只写：`x`、`xt`、`xb`

  - 存在，报错
  - 不存在，创建再写。

- 只写：`a`、`at`、`ab`【尾部追加】（用）

  - 存在，尾部追加。
  - 不存在，创建再写。

注意：rb/wb/ab：以二进制打开文件，不必指定编码（指定报错），用于读取/写入图片，音频，视频等文件;

```python
========= ===============================================================
Character Meaning
--------- ---------------------------------------------------------------
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists

'b'       binary mode
't'       text mode (default)

'+'       open a disk file for updating (reading and writing)

The default mode is 'rt' (open for reading text).
```

### 5.3 操作(只读只写)

#### 5.3.1 读文件

- read() 把文件全部读到内存

  ```python
  file_object = open('log.txt',mode='r',encoding='utf-8')
  # 读取文件的所有内容到内存
  data = file_object.read()
  print(data)
  file_object.close()
  ```

- read(2)

  - rt表示读取字节

  ```python
  file_object = open('log.txt',mode='r',encoding='utf-8')
  # 从当前光标所在的位置向后读取文件两个字符
  data = file_object.read(2)
  print(data)
  file_object.close()
  ```

  - rb表示读取字节

  ```python
  obj = open('a.txt',mode='rb')
  data = obj.read() # 中文3个字节，
  obj.close()
  ```

- readlines() 读所有行，每一行作为列表中的一个元素

  ```python
  file_object = open('log.txt',mode='r',encoding='utf-8')
  # 读取文件的所有内容到内存，并按照每一行进行分割到列表中。
  data_list = file_object.readlines()
  print(data_lis)
  file_object.close()
  ```

- readline() 读一行

  ```python
  f = open('info.txt', mode='r', encoding='utf-8')
  
  v1 = f.readline()
  print(v1)
  
  v2 = f.readline()
  print(v2)
  
  f.close()
  ```

- for循环读取  读大文件（readline加强版）常用

  ```python
  file_object = open('log.txt',mode='r',encoding='utf-8')
  # 如果以后读取一个特别大的文件 
  for line in file_object:
      line = line.strip()
      print(line)
  
  file_object.close()
  ```

注意事项：文件路径

- 相对路径：运行程序中写的文件路径为相对路径，在终端运行可能报找不到文件路径

![image-20210531133025734](j:\homework\Python学习笔记\Python_notes.assets\image-20210531133025734.png)

![image-20210531132954308](j:\homework\Python学习笔记\Python_notes.assets\image-20210531132954308.png)

解决：

```python
import os

file_path = r"E:\Luffycity\VScode\1.文件操作相关\test1.txt"
file_exists = os.path.exists(file_path)  # 使用os内置模块判断文件是否存在
if not file_exists:
    print("文件不存在")

a = open(file_path, mode='r', encoding='utf-8')

data = a.read()

print(data)
a.close()
```

- 绝对路径：windows中文件绝对路径容易出现问题，需要加r或双\\

![image-20210531133237191](j:\homework\Python学习笔记\Python_notes.assets\image-20210531133237191.png)

#### 5.3.2 写文件

- writ()

```python
obj = open('a.txt',mode='wt',encoding='utf-8')
obj.write('中意你')
obj.close()
```

- write(二进制)

```python
obj = open('a.png',mode='wb')

# wb模式要求写入文件是字节类型，大部分用于写入图片
# obj.write('中午你'.encode('utf-8'))
v = '中午你'.encode('utf-8')
obj.write(v)

obj.close()
```

案例：

```python
# 用户注册
user = input("请输入用户名:")
password = input("请输入密码：")

file_obj = open("user_info.txt", mode='wt', encoding="utf-8")

file_obj.write("{}:{}".format(user, password))

file_obj.close()

# 多用户注册
file_obj = open("user_info.txt", mode='wt', encoding="utf-8")
while True:
    user = input("请输入用户名:")
    password = input("请输入密码：")
    if user.upper() == "Q":
        break
    file_obj.write("{}:{}\n".format(user, password))
file_obj.close()

```

小高级案例：

> 利用Python向某个网址发请求并获取结果，利用第三方模块
>
> - 下载第三方模块
>
>   ```python
>   pip install requests
>   ```
>
> - requests模块使用方式
>
> ```python
> import requesets
> 
> ret = requests.get(ulr="网址")
> print(ret)
> ```

```python
# 案件： 去网上下载一张图片，写入本地文件
import requests

ret = requests.get(
    url="https://hbimg.huabanimg.com/c7e1461e4b15735fbe625c4dc85bd19904d96daf6de9fb-tosv1r_fw1200",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    })

file_obj = open("files/nn.png", mode="wb")
print(file_obj.content)  # 网络传输原始的二进制信息
file_obj.write(ret.content)
file_obj.close()
```

写文件注意事项：文件存在时，会清空原有的内容，然后再写入文件，文件不存在时，会创建新的文件。

#### 5.3.3 追加

- 追加

```python
f = open('log.txt', mode='a', encoding='utf-8')
f.write('kljl')
f.close()
```

- 二进制追加

```python
file_object = open('log.txt', mode='ab')

file_object.seek(0)  # 写的时候永远在最后追加
file_object.write('666'.encode('utf-8'))
v = '我是谁'.encode('utf-8')
file_object.write(v)

file_object.close()
```

### 5.4 操作(可读可写)

#### 5.4.1 读写

r+、rt+、rb+，默认光标位置：起始位置（不清空文件）

```python
file_object = open('log.txt', mode='r+', encoding='utf-8')
# file_object.seek(2) # 调整光标的位置

content = file_object.read()
print(content)
file_object.write('浪')  # 写入后，光标定位到最后的位置

# 关闭文件
file_object.close()
```

```python
file_object = open('log.txt', mode='r+', encoding='utf-8')

file_object.write('666')  # 从光标开始位置进行写入
content = file_object.read()  # 写入后光标定位到第3个字节的位置
print(content)

# 关闭文件
file_object.close()
```

- 读：默认从0的光标开始读，可以通过seek调整光标的位置
- 写：从光标所在的位置开始写,默认光标的位置在开始的位置,直接写入，会从光标开始的位置替换到后边的内容
- 可以通过seek调整光标的位置,进行写入

#### 5.4.2 写读

w+、wt+、wb+，默认光标位置：起始位置（清空文件）

```python
file_object = open('log.txt',mode='w+',encoding='utf-8')

data = file_object.read()  # 内容被清空，读取不到内容
print(data)

# 写入内容
file_object.write('alex')

# 将光标移动到开始的位置
file_object.seek(0)

# 读取文件内容
data = file_object.read()

# 打印光标后边的内容
print(data)
file_object.close()
```

- 读：默认光标在写入到最后或0，可以通过seek调整光标的位置
- 写：在原文件先清空文件再写，不是原文件会新建一个文件

#### 5.4.3 追加读

a+、at+、ab+，默认光标位置：末尾

```python
file_object = open('log.txt',mode='a+',encoding='utf-8')

content = file_object.read()
print(content)  # 光标在最后的位置，无法读取到内容

file_object.write('写在了最后')
file_object.seek(0)  # 将光标移动到开始的位置
data = file_object.read()  # 读取光标所在位置以后的内容
print(data)

file_object.close()
```

- 读：默认光标在最后，可以通过seek调整光标的位置，然后再去读
- 写：永远在最后追加

```python
file_obj = open("user_info.txt", mode="a", encoding="utf-8")

while True:
    user = input("请输入用户名：").strip()
    if user.upper() == 'Q':
        break
    password = input("请输入密码：").strip()
    file_obj.write("用户名:{}   密码:{}\n".format(user, password))

file_obj.close()
```

### 5.5  移动光标

- seek(光标按字节移动)，无论模式是否带b，都是按照字节进行处理

```python
obj = open('a.txt',mode='r',encoding='utf-8')  # 读模式打开
obj.seek(3) # 跳转到指定字节位置
data = obj.read()
obj.close()
print(data)


obj = open('a.txt',mode='rb')  # 二进制读模式
obj.seek(3) # 跳转到指定字节位置
data = obj.read()
obj.close()
print(data)
```

### 5.6  光标位置

- tell()，获取光标当前所在的字节位置

```python
obj = open('a.txt',mode='rb')
# obj.seek(3) # 跳转到指定字节位置
obj.read()
data = obj.tell()
print(data)
obj.close()
```

### 5.7  强制写入内存

- flush不是写到硬盘，而是写在缓冲区，关闭后系统会将缓冲区的内容刷到硬盘。

```python
v = open('user_info.txt',mode='a',encoding='utf-8')
while True:
    val = input('请输入：')
    v.write(val)
    v.flush()

v.close()
```

- flush，强制将缓存区中的数据写入到硬盘

```python
v = open('user_info.txt',mode='a',encoding='utf-8')
while True:
    val = input('请输入：')
    v.write(val)
    v.flush()  # 

v.close()
```

### 5.8 文件内容修改

- 若要修改文件内容，需要先将文件内容读到内存，在内存中修改后，再重新写入文件；

- 若文件过大，可以打开两个文件，边修改边写入；

  ```python
  f1 = open("test1.txt",mode="r",encoding="utf-8")
  f2 = open("test2.txt",mode="w",encoding="utf-8")
  for line in f1:
      content = line.replace("123","456")
      f2.write(content)
      f1.close()
      f2.close()
  ```


### 5.9 上下文管理

之前对文件操作时，每次都要打开和关闭文件，比较繁琐且容易忘记关闭文件。以后对文件操作时，推荐使用with上下文管理，它可以自动实现关闭文件。

在Python2.7以后，with支持同时对多个文件真的上下文进行管理，eg：

```python
with open("test1.txt",mode="r",encoding="utf-8") as f1,open("test2.txt",mode="w",encoding="utf-8") as f2:
	for line in f1:
    	content = line.replace("123","456")
    	f2.write(content)
```

### 6.0 练习题

1. 补充代码：实现下载视频并保存到本地

```python
import requests

res = requests.get(
    url="https://f.video.weibocdn.com/000pTZJLgx07IQgaH7HW010412066BJV0E030.mp4?label=mp4_720p&template=1280x720.25.0&trans_finger=1f0da16358befad33323e3a1b7f95fc9&media_id=4583105541898354&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=2&ot=h&ps=3lckmu&uid=3ZoTIp&ab=3915-g1,966-g1,3370-g1,3601-g0,3601-g0,3601-g0,1493-g0,1192-g0,1191-g0,1258-g0&Expires=1608204895&ssig=NdYpDIEXSS&KID=unistore,video",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
)

# 视频的文件内容
res.content
```

```python
import requests

res = requests.get(
    url="https://f.video.weibocdn.com/000pTZJLgx07IQgaH7HW010412066BJV0E030.mp4?label=mp4_720p&template=1280x720.25.0&trans_finger=1f0da16358befad33323e3a1b7f95fc9&media_id=4583105541898354&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=2&ot=h&ps=3lckmu&uid=3ZoTIp&ab=3915-g1,966-g1,3370-g1,3601-g0,3601-g0,3601-g0,1493-g0,1192-g0,1191-g0,1258-g0&Expires=1608204895&ssig=NdYpDIEXSS&KID=unistore,video",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
)

with open("练习题/1-demo.avi", 'wb') as video_obj:
    video_obj.write(res.content)
```

2. 日志分析，计算某用户`223.73.89.192`访问次数。日志文件如下：`access.log`

```
49.89.167.91 - - [17/Dec/2020:03:43:50 +0800] "GET /wiki/detail/3/40 HTTP/1.1" 301 0 "-" "Mozilla/5.0(Linux;Android 5.1.1;OPPO A33 Build/LMY47V;wv) AppleWebKit/537.36(KHTML,link Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 LieBaoFast/4.51.3" "-"
49.89.167.91 - - [17/Dec/2020:03:44:11 +0800] "GET /wiki/detail/3/40/ HTTP/1.1" 200 8033 "-" "Mozilla/5.0(Linux;Android 5.1.1;OPPO A33 Build/LMY47V;wv) AppleWebKit/537.36(KHTML,link Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 LieBaoFast/4.51.3" "-"
203.208.60.66 - - [17/Dec/2020:03:47:58 +0800] "GET /media/uploads/2019/11/17/pic/s1.png HTTP/1.1" 200 710728 "-" "Googlebot-Image/1.0" "-"
223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /wiki/detail/3/40/ HTTP/1.1" 200 8033 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/stark/plugins/font-awesome/css/font-awesome.css HTTP/1.1" 200 37414 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/stark/plugins/bootstrap/css/bootstrap.css HTTP/1.1" 200 146010 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/web/css/commons.css HTTP/1.1" 200 3674 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/mdeditor/editormd/css/editormd.preview.css HTTP/1.1" 200 60230 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/stark/js/jquery-3.3.1.min.js HTTP/1.1" 200 86927 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/stark/plugins/bootstrap/js/bootstrap.min.js HTTP/1.1" 200 37045 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:26 +0800] "GET /static/mdeditor/editormd/lib/marked.min.js HTTP/1.1" 200 19608 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:27 +0800] "GET /static/mdeditor/editormd/lib/prettify.min.js HTTP/1.1" 200 17973 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:27 +0800] "GET /static/mdeditor/editormd/fonts/fontawesome-webfont.woff2?v=4.3.0 HTTP/1.1" 200 56780 "https://pythonav.com/static/mdeditor/editormd/css/editormd.preview.css" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:27 +0800] "GET /static/mdeditor/editormd/editormd.js HTTP/1.1" 200 163262 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:28 +0800] "GET /static/mdeditor/mdeditor-preview-init.js HTTP/1.1" 200 261 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:29 +0800] "GET /static/stark/plugins/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0 HTTP/1.1" 200 77160 "https://pythonav.com/static/stark/plugins/font-awesome/css/font-awesome.css" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
223.73.89.192 - - [17/Dec/2020:03:48:29 +0800] "GET /media/uploads/2019/02/22/Gobook/_book/ssl2.png HTTP/1.1" 200 203535 "https://pythonav.com/wiki/detail/3/40/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60" "-"
```

```python
count = 0
with open("练习题/access.log", "r", encoding="utf-8") as file_obj:
    for line in file_obj:
        if "223.73.89.192" in line:
            count += 1
    print(count)
```

3. 日志分析升级，计算所有用户的访问次数。

```python
user_ip_dict = {}

with open("练习题/access.log", "r", encoding="utf-8") as file_obj:
    for line in file_obj:
        user_ip = line.split(" - - ")[0]
        if user_ip not in user_ip_dict:
            user_ip_dict[user_ip] = 1
        else:
            user_ip_dict[user_ip] += 1

    print(user_ip_dict)
```

4. 筛选出股票 当前价大于 20 的所有股票数据

```python
with open("练习题/gupiap.log", "r", encoding="utf-8") as file_obj:
    print(file_obj.readline())
    for line in file_obj:
        ret = float(line.split(",")[2])
        if ret > 20:
            print(line.strip())
```

5. 根据要求修改文件的内容，原文件内容如下：`ha.conf`  

```python
global
        log 127.0.0.1 local2
        daemon
        maxconn 256
        log 127.0.0.1 local2 info
defaults
        log global
        mode http
        timeout connect 5000ms
        timeout client 50000ms
        timeout server 50000ms
        option  dontlognull

listen stats :8888
        stats enable
        stats uri       /admin
        stats auth      admin:1234

frontend oldboy.org
        bind 0.0.0.0:80
        option httplog
        option httpclose
        option  forwardfor
        log global
        acl www hdr_reg(host) -i www.pythonav.org
        use_backend www.pythonav.com if www

backend www.pythonav.com
        server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000
...
```

请将文件中的 `luffycity`修改为 `pythonav` 。

```python
with open("练习题/ha.conf", "r", encoding="utf-8") as f1, open("练习题/new_ha.conf", "w", encoding="utf-8")as f2:
    for line in f1:
        new = line.replace("luffycity", "pythonav")
        f2.write(new)
```

### 6.1 其他格式文件操作

#### 6.1.1 csv格式文件

逗号分隔值（Comma-Separated Values，CSV，有时也称为**字符分隔值**，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。

对于这种格式的数据，我们需要利用open函数来读取文件并根据逗号分隔的特点来进行处理。

示例：下载文档中的所有图片且以用户名为图片名称存储。

```python
ID,用户名,头像
26044585,Hush,https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb88cacc46869954f478-aP4Q3V
19318369,柒十一,https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO
15529690,Law344,https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzoQd
18311394,Jennah·,https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz
18009711,可洛爱画画,https://hbimg.huabanimg.com/03331ef39b5c7687f5cc47dbcbafd974403c962ae88ce-Co8AUI
30574436,花姑凉~,https://hbimg.huabanimg.com/2f5b657edb9497ff8c41132e18000edb082d158c2404-8rYHbw
17740339,小巫
```

```python
with open("files/mv.csv", "r", encoding="utf-8")as file_obj:
    file_obj.readline()
    for line in file_obj:
        user_id, username, avatar_url = line.strip().split(",")
        if not os.path.exists("images"):
            os.makedirs("images")

        ret = requests.get(url=avatar_url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        })

        with open("images/{}.jpg".format(username), "wb") as f:
            f.write(ret.content)
```

#### 6.1.2 ini格式文件

ini文件是Initialization File的缩写，平时用于存储软件的的配置文件。例如：MySQL数据库的配置文件。

```ini
[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
log-bin=py-mysql-bin
character-set-server=utf8
collation-server=utf8_general_ci
log-error=/var/log/mysqld.log
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

[mysqld_safe]
log-error=/var/log/mariadb/mariadb.log
pid-file=/var/run/mariadb/mariadb.pid

[client]
default-character-set=utf8
```

这种格式是可以直接使用open打开的，考虑到自己处理比较麻烦，所以Python为我们提供了更为方便的方式。

```python
import configparser

config = configparser.ConfigParser()
config.read("files/my.ini", encoding="utf-8")

# 1.获取所有节点
ret = config.sections()
print(ret)

# 2.获取节点下的值
ret = config.items("mysqld_safe")
print(ret)

# 3.获取某节点下的键对应的值
ret = config.get("mysqld_safe", "pid-file")
print(ret)

# 4.检查节点下是否有值
ret = config.has_section("mysqld")
print(ret)

# 5.添加节点
config.add_section("linux")

# 6.节点中设置值
config.set("linux", "key1", "value1")
config.set("linux", "key3", "value3")
ret = config.items("linux")
print(ret)

# 7.内容写入新的文件
config.write(open("files/new_my.ini", "w"))

# 8.删除节点
config.read("files/new_my.ini", encoding="utf-8")
config.remove_section("linux")
ret = config.sections()
print(ret)

# 9.删除节点中的值
config.remove_option("client", "default-character-set")
ret = config.items("client")
print(ret)
```

#### 6.1.3 xml格式文件

可扩展标记语言，是一种简单的数据存储语言，XML 被设计用来传输和存储数据。

- 存储，可用来存放配置文件，例如：java的配置文件。
- 传输，网络传输时以这种格式存在，例如：早期ajax传输的数据、soap协议等。

```xml
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2026</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
```

备注：再Python开发中用的相对来比较少（在后期讲微信公众号、微信支付消息处理时会用到基于xml传输输入据）

例如：https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Receiving_standard_messages.html

##### 6.1.3.1 读取文件和内容

```python
from xml.etree import ElementTree as ET

# 打开文件
tree = ET.parse("files/xo.xml")

# 获取根标签
root = tree.getroot()
print(root)

```

```python
from xml.etree import ElementTree as ET
content = """
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2026</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
"""

root = ET.XML(content)
print(root)  # <Element 'data' at 0x00000217E6955778>
```

![image-20210601141917428](j:\homework\Python学习笔记\Python_notes.assets\image-20210601141917428.png)

##### 6.1.3.2 读取节点数据

```python
from xml.etree import ElementTree as ET
content = """
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2026</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
"""

root = ET.XML(content)
country_obj = root.find("country")
# print(country_obj.tag, country_obj.attrib)

rank_obj = country_obj.find("rank")
# 获取标签名  标签属性  标签文本
print(rank_obj.tag, rank_obj.attrib, rank_obj.text)
```

```python
from xml.etree import ElementTree as ET

content = """
<data>
    <country name="Liechtenstein">
        <rank>2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
     <country name="Panama">
        <rank>69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
"""
root = ET.XML(content)

# 获取子标签的标签名  标签文本内容
for child in root.iter("year"):
    print(child.tag, child.text)

# 获取data标签的子标签
for child in root:
    # 获取二级标签的标签名  属性
    # print(child.tag, child.attrib)

    # 获取三级标签的标签名  属性  文本内容
    for node in child:
        print(node.tag, node.attrib, node.text)
```

```python
from xml.etree import ElementTree as ET
content = """
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2026</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
"""

root = ET.XML(content)

# 查找所有country标签
country_obj = root.findall("country")
print(country_obj)

# 查找country子标签的文本
rank_obj = root.find("country").find("rank")
print(rank_obj.text)
```

##### 6.1.3.3 修改和删除节点

```python
from xml.etree import ElementTree as ET
content = """
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2026</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
"""

root = ET.XML(content)

# 修改节点内容和属性
rank = root.find("country").find("rank")
print(rank.text)

# 修改内容  设置属性
rank.text = "999"
rank.set("updated", "2021-06-01")
print(rank.attrib, rank.text)

# 保存修改后的文件
tree = ET.ElementTree(root)
tree.write("files/new.xml", encoding="utf-8")

# 删除节点
root.remove(root.find("country"))
print(root.findall("country"))

# 保存文件
tree = ET.ElementTree(root)
tree.write("files/new.xml", encoding="utf-8")
```

##### 6.1.3.4 构建文档

```python
'''
<home>
    <son name="儿1">
        <grandson name="儿11"></grandson>
        <grandson name="儿12"></grandson>
    </son>
    <son name="儿2"></son>
</home>
'''

# 构建以上的xml文件结构
from xml.etree import ElementTree as ET

# 创建根标签
root = ET.Element("home")

# 创建二级标签
son1 = ET.Element("son", {"name": "val1"})

# 创建二级标签
son2 = ET.Element("son", {"name": "val2"})

# 创建三级标签
grandson1 = ET.Element("grandson", {"name": "valval1"})
grandson2 = ET.Element("grandson", {"name": "valval2"})

# 把三级标签添加到二级标签
son1.append(grandson1)
son1.append(grandson2)

# 把二级标签添加到一级标签
root.append(son1)
root.append(son2)

# 保存文件
tree = ET.ElementTree(root)
# 是唯一一个关键字参数，是Python 3.4新增加的参数。它用于控制那些不包含任何内容的elements的格式
# 如果该参数值为Ture则这些标签将会被输出为一个单独的自关闭标签（如: <a/>）,如果值为False则这些标签将会被输出为一个标签对（如：<a></a>）
tree.write("xml_demo.xml", encoding="utf-8", short_empty_elements=False)

```

**案例：**

```python
content = """<xml>
    <ToUserName><![CDATA[gh_7f083739789a]]></ToUserName>
    <FromUserName><![CDATA[oia2TjuEGTNoeX76QEjQNrcURxG8]]></FromUserName>
    <CreateTime>1395658920</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[TEMPLATESENDJOBFINISH]]></Event>
    <MsgID>200163836</MsgID>
    <Status><![CDATA[success]]></Status>
</xml>"""

from xml.etree import ElementTree as ET

info = dict()

root = ET.XML(content)
for node in root:
    # print(node.tag, node.attrib, node.text)
    info[node.tag] = node.text
print(info)
```

#### 6.1.4 excel格式文件

Python内部未提供处理Excel文件的功能，想要在Python中操作Excel需要按照第三方的模块。

```
pip install openpyxl
```

##### 6.1.4.1 读Excel文件

- 读取sheet内容

```python
from openpyxl import load_workbook

wb = load_workbook("files/p1.xlsx")

# 1.获取excel文件中所有sheet页名称
# print(wb.sheetnames)

# 2.基于sheet名称，获取表格内容
# sheet = wb["数据导出"]
# cell = sheet.cell(1, 4)
# print(cell.value)

# 3.基于sheet索引位置，获取表格内容
# sheet = wb.worksheets[0]
# cell = sheet.cell(1, 2)
# print(cell.value)

# 4.循环所有的sheet页
# for sheet in wb.sheetnames:
#     name = wb[sheet]
#     cell = name.cell(1, 1)
#     print(cell.value)

# for sheet in wb.worksheets:
#     cell = sheet.cell(1, 1)
#     print(cell.value)

for sheet in wb:
    cell = sheet.cell(2, 2)
    print(cell.value)
```

- 读取sheet单元格的数据

```python
wb = load_workbook("files/p1.xlsx")

sheet = wb.worksheets[0]

# 1.获取第N行第N列的单元格
# cell = sheet.cell(1, 1)
# print(cell.value)
# print(cell.style)
# print(cell.font)
# print(cell.alignment)

# 2.获取某个单元格
# c2 = sheet["c2"]
# print(c2.value)

# 3.获取第N行所有单元格
# for cell in sheet[1]:
# print(cell.value)

# 4.获取所有行的数据sheet.rows  及某一列的数据
# for row in sheet.rows:
# print(row[0].value, row[1].value)
# print(row)

# 5.获取所有列的数据sheet.columns  及某一行的数据
# for columns in sheet.columns:
    # print(columns[0].value)
```

- 读取合并单元格的数据

![image-20210602201719149](j:\homework\Python学习笔记\Python_notes.assets\image-20210602201719149.png)

```python
# 读取合并单元格
wb = load_workbook("files/p1.xlsx")

sheet = wb.worksheets[2]

# 获取第N行列的单元格(位置从1开始)
c1 = sheet.cell(1, 1)
# print(c1)  # <Cell 'Sheet1'.A1>
# print(c1.value)  # 用户信息

# c2 = sheet.cell(1, 2)  # <MergedCell 'Sheet1'.B1>
# print(c2.value)  # None
```

##### 6.1.4.2 写Excel文件

在Excel中想要写文件，大致要分为两种情况：

- 在原Excel文件基础上写内容

```python
wb = load_workbook("files/p1.xlsx")

sheet = wb.worksheets[0]

# 定位到单元格，修改内容
cell = sheet.cell(1, 1)
cell.value = "需要修改的"

# 将修改后的文件保存到p2.xlsx
wb.save("files/p2.xlsx")
```

- 新创建Excel文件写内容

```python
#  创建excel且默认创建一个sheet页
wb = workbook.Workbook()
sheet = wb.worksheets[0]

# 找到单元格，并修改单元格的内容
cell = sheet.cell(1, 1)
cell.value = "新创建修改"

wb.save("files/p3.xlsx")
```

- Excel的基本操作

```python
# 1.创建一个sheet页
wb = workbook.Workbook()

# 2.修改sheet名称
# sheet = wb.worksheets[0]
# sheet.title = "第一个sheet"
# wb.save("files/创建sheet.xlsx")

# 3.创建sheet并设置sheet颜色
# sheet = wb.create_sheet("工作嘉华", 0)
# sheet.sheet_properties.tabColor = "1072BA"
# wb.save("files/创建sheet1.xlsx")

# 4.默认打开的sheet
# wb.active = 0
# wb.save("files/创建sheet2.xlsx")

# 5.拷贝sheet
# sheet = wb.create_sheet("工作计划")
# sheet.sheet_properties.tabColor = "1072BA"

# new_sheet = wb.copy_worksheet(wb["Sheet"])
# new_sheet.title = "新sheet"
# wb.save("files/创建sheet3.xlsx")

# 6.删除sheet
# del wb["Sheet"]
# wb.save("files/创建sheet1.xlsx")
```

```python
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Side, Font, PatternFill, GradientFill


wb = load_workbook('files/p1.xlsx')

sheet = wb.worksheets[1]

# 1. 获取某个单元格，修改值
"""
cell = sheet.cell(1, 1)
cell.value = "开始"
wb.save("p2.xlsx")
"""

# 2.  获取某个单元格，修改值
"""
sheet["B3"] = "Alex"
wb.save("p2.xlsx")
"""

# 3. 获取某些单元格，修改值
"""
cell_list = sheet["B2":"C3"]
for row in cell_list:
    for cell in row:
        cell.value = "新的值"
wb.save("p2.xlsx")
"""

# 4. 对齐方式
"""
cell = sheet.cell(1, 1)

# horizontal，水平方向对齐方式："general", "left", "center", "right", "fill", "justify", "centerContinuous", "distributed"
# vertical，垂直方向对齐方式："top", "center", "bottom", "justify", "distributed"
# text_rotation，旋转角度。
# wrap_text，是否自动换行。
cell.alignment = Alignment(horizontal='center', vertical='distributed', text_rotation=45, wrap_text=True)
wb.save("p2.xlsx")
"""

# 5. 边框
# side的style有如下：dashDot','dashDotDot', 'dashed','dotted','double','hair', 'medium', 'mediumDashDot', 'mediumDashDotDot','mediumDashed', 'slantDashDot', 'thick', 'thin'
"""
cell = sheet.cell(9, 2)
cell.border = Border(
    top=Side(style="thin", color="FFB6C1"), 
    bottom=Side(style="dashed", color="FFB6C1"),
    left=Side(style="dashed", color="FFB6C1"),
    right=Side(style="dashed", color="9932CC"),
    diagonal=Side(style="thin", color="483D8B"),  # 对角线
    diagonalUp=True,  # 左下 ~ 右上
    diagonalDown=True  # 左上 ~ 右下
)
wb.save("p2.xlsx")
"""

# 6.字体
"""
cell = sheet.cell(5, 1)
cell.font = Font(name="微软雅黑", size=45, color="ff0000", underline="single")
wb.save("p2.xlsx")
"""

# 7.背景色
"""
cell = sheet.cell(5, 3)
cell.fill = PatternFill("solid", fgColor="99ccff")
wb.save("p2.xlsx")
"""

# 8.渐变背景色
"""
cell = sheet.cell(5, 5)
cell.fill = GradientFill("linear", stop=("FFFFFF", "99ccff", "000000"))
wb.save("p2.xlsx")
"""

# 9.宽高（索引从1开始）
"""
sheet.row_dimensions[1].height = 50
sheet.column_dimensions["E"].width = 100
wb.save("p2.xlsx")
"""

# 10.合并单元格
"""
sheet.merge_cells("B2:D8")
sheet.merge_cells(start_row=15, start_column=3, end_row=18, end_column=8)
wb.save("p2.xlsx")
"""
"""
sheet.unmerge_cells("B2:D8")
wb.save("p2.xlsx")
"""

# 11.写入公式
"""
sheet = wb.worksheets[3]
sheet["D1"] = "合计"
sheet["D2"] = "=B2*C2"
wb.save("p2.xlsx")
"""
"""
sheet = wb.worksheets[3]
sheet["D3"] = "=SUM(B3,C3)"
wb.save("p2.xlsx")
"""

# 12.删除
"""
# idx，要删除的索引位置
# amount，从索引位置开始要删除的个数（默认为1）
sheet.delete_rows(idx=1, amount=20)
sheet.delete_cols(idx=1, amount=3)
wb.save("p2.xlsx")
"""

# 13.插入
"""
sheet.insert_rows(idx=5, amount=10)
sheet.insert_cols(idx=3, amount=2)
wb.save("p2.xlsx")
"""

# 14.循环写内容
"""
sheet = wb["Sheet"]
cell_range = sheet['A1:C2']
for row in cell_range:
    for cell in row:
        cell.value = "xx"

for row in sheet.iter_rows(min_row=5, min_col=1, max_col=7, max_row=10):
    for cell in row:
        cell.value = "oo"
wb.save("p2.xlsx")
"""

# 15.移动
"""
# 将H2:J10范围的数据，向右移动15个位置、向上移动1个位置
sheet.move_range("H2:J10",rows=1, cols=15)
wb.save("p2.xlsx")
"""
"""
sheet = wb.worksheets[3]
sheet["D1"] = "合计"
sheet["D2"] = "=B2*C2"
sheet["D3"] = "=SUM(B3,C3)"
sheet.move_range("B1:D3",cols=10, translate=True) # 自动翻译公式
wb.save("p2.xlsx")
"""

# 16.打印区域
"""
sheet.print_area = "A1:D200"
wb.save("p2.xlsx")
"""

# 17.打印时，每个页面的固定表头
"""
sheet.print_title_cols = "A:D"
sheet.print_title_rows = "1:3"
wb.save("p2.xlsx")
"""
```

#### 6.1.5 压缩与解压文件

基于Python内置的shutil模块可以实现对压缩文件的操作

```python
import shutil

# 参数：
# base_name：压缩后的文件名
# format：压缩文件的格式
# root_dir：要压缩文件的路径

# 压缩文件
# shutil.make_archive(base_name=r"datafile", format="zip", root_dir=r"images")

# 解压文件
# filename：要解压的压缩文件名
# extract_dir：文件解压到的路径
# format：解压文件的格式
shutil.unpack_archive(filename="datafile.zip", extract_dir=r'E:\Luffycity\VScode\1.文件操作相关\newimg', format="zip")

```

#### 6.1.6 路径相关

```python
import shutil
import os

# 1. 获取当前脚本绝对路径
"""
abs_path = os.path.abspath(__file__)
print(abs_path)
"""

# 2. 获取当前文件的上级目录
"""
base_path = os.path.dirname( os.path.dirname(路径) ）
print(base_path)
"""

# 3. 路径拼接
"""
p1 = os.path.join(base_path, 'xx')
print(p1)

p2 = os.path.join(base_path, 'xx', 'oo', 'a1.png')
print(p2)
"""

# 4. 判断路径是否存在
"""
exists = os.path.exists(p1)
print(exists)
"""

# 5. 创建文件夹
"""
os.makedirs(路径)
"""
"""
path = os.path.join(base_path, 'xx', 'oo', 'uuuu')
if not os.path.exists(path):
    os.makedirs(path)
"""

# 6. 是否是文件夹
"""
file_path = os.path.join(base_path, 'xx', 'oo', 'uuuu.png')
is_dir = os.path.isdir(file_path)
print(is_dir) # False

folder_path = os.path.join(base_path, 'xx', 'oo', 'uuuu')
is_dir = os.path.isdir(folder_path)
print(is_dir) # True

"""

# 7. 删除文件或文件夹
"""
os.remove("文件路径")
"""
"""
path = os.path.join(base_path, 'xx')
shutil.rmtree(path)
"""

# 8. 拷贝文件夹
"""
shutil.copytree("/Users/wupeiqi/Desktop/图/csdn/","/Users/wupeiqi/PycharmProjects/CodeRepository/files")
"""

# 9.拷贝文件
"""
shutil.copy("/Users/wupeiqi/Desktop/图/csdn/WX20201123-112406@2x.png","/Users/wupeiqi/PycharmProjects/CodeRepository/")
shutil.copy("/Users/wupeiqi/Desktop/图/csdn/WX20201123-112406@2x.png","/Users/wupeiqi/PycharmProjects/CodeRepository/x.png")
"""

# 10.文件或文件夹重命名
"""
shutil.move("/Users/wupeiqi/PycharmProjects/CodeRepository/x.png","/Users/wupeiqi/PycharmProjects/CodeRepository/xxxx.png")
shutil.move("/Users/wupeiqi/PycharmProjects/CodeRepository/files","/Users/wupeiqi/PycharmProjects/CodeRepository/images")
"""
```

## 第六章 函数

函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可.

**特性:**

- 减少重复代码

- 使程序变的可扩展

- 使程序变得易维护

### 6.1 三元运算(三目运算)

```python
v = 前面 if 条件 else 后面
if 条件:
    v = '前面'
else:
    v = '后面'
# 让用户输入值，如果值是整数，则转换成整数，否则赋值为None
data = input('>>>:')
value = int(data) if data.isdecimal() else None
```

注意：先做出来，再思考如何简化。

### 6.2 函数和函数名

#### 6.2.1 函数

对于函数编程：

- 本质：将N行代码拿到别处并给他起个名字，以后通过名字就可以找到这段代码并执行。
- 场景：
  - 代码重复执行
  - 代码量特别多，超过一屏，key选择通过函数进行代码的分割。

函数的基本结构：

```python
# 函数的定义
def 函数名():
	# 函数内容
	pass
	
# 执行函数
函数名()
```

示例一：

```python
def get_list():
	v = [11,22,33]
	print(v[0])
get_list()
# 注意:函数如果不被调用,则内部代码永远不会执行
```

示例二：

```python
# 假如:管理员/业务员/老板用的是同一个邮箱,可以这样写
def send_email():
	print('发送邮件成功')
	
user_input = input('请输入角色:').strip()
if user_input == '管理员':
	send_email()
if user_input == '业务员':
	send_email()
if user_input == '老板':
	send_email()
```

> 函数可被哈希，所以函数名通常也可以当作集合的元素、字典的值、列表的元素

截至目前：面向过程编程【缺点：可读性差/可重用性差】

```python
# 面向过程编程
user_input = input('请输入角色：')

if user_input == '管理员':
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('管理员，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
    msg['From'] = formataddr(["男一号", 'nanyihao@163.com'])
    msg['To'] = formataddr(["管理员", '344522251@qq.com'])
    msg['Subject'] = "情爱的导演"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("nanyihao@163.com", "mima")
    server.sendmail('nanyihao@163.co', ['管理员', ], msg.as_string())
    server.quit()
elif user_input == '业务员':
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('业务员，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
    msg['From'] = formataddr(["男一号", 'nanyihao@163.com'])
    msg['To'] = formataddr(["业务员", '业务员'])
    msg['Subject'] = "艾奇的导演"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("nanyihao@163.com", "mima")
    server.sendmail('nanyihao@163.com', ['业务员', ], msg.as_string())
    server.quit()
elif user_input == '老板':
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('老板，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
    msg['From'] = formataddr(["男一号", 'nanyihao@163.com'])
    msg['To'] = formataddr(["老板", '老板邮箱'])
    msg['Subject'] = "艾奇的导演"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("nanyihao@163.com", "mima")
    server.sendmail('nanyihao@163.com', ['老板邮箱', ], msg.as_string())
    server.quit()
```

函数式编程：

```python
def send_email():
	import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    msg = MIMEText('老板，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
    msg['From'] = formataddr(["男一号", 'nanyihao@163.com'])
    msg['To'] = formataddr(["老板", '老板邮箱'])
    msg['Subject'] = "艾奇的导演"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("nanyihao@163.com", "mima")
    server.sendmail('nanyihao@163.com', ['老板邮箱', ], msg.as_string())
    server.quit()


user_input = input('请输入角色：')

if user_input == '管理员':
    send_email()
elif user_input == '业务员':
    send_email()
elif user_input == '老板':
    send_email()
```

#### 6.2.2 函数名

将函数名赋值给其他变量，函数名其实就是个变量，代指某函数；如果将函数名赋值给另一个变量，则此变量也会代指该函数。

示例一：

```python
def func(a1, a2):
    print(a1, a2)
    
test = func
func(1, 2)
test(2, 2)
# 此时，test和func都代指上边的函数，所以都可以被执行
```

示例二：

```python
def func(a1,a2):
    print(a1,a2)
    
func_list = [func,func,func]

func(11,22)
func_list[0](11,22)
func_list[1](33,44)
func_list[2](55,66)
```

对函数名重新赋值，如果将该函数名对应的值重新赋值，函数名便不再代指该函数。

示例：

```python
def func(a1, a2):
    print(a1, a2)


func(1, 1)
func = "joker"
print(func)
```

```python
def func(a1,a2):
    print(a1+a2)
    
func(1,2)

def func():
    print(666)
    
func()
```

函数名其实就一个变量，代指某个函数，所以，他和其他的数据类型一样，也可以当做函数的参数和返回值。

- 参数

```python
def plus(num):
    return num + 100

def handler(func):
    res = func(10) # 110
    msg = "执行func，并获取到的结果为:{}".format(res)
    print(msg) # 执行func，并获取到的结果为:110
   
# 执行handler函数，将plus作为参数传递给handler的形式参数func
```

- 返回值

```python
def plus(num):
    return num + 100

def handler():
	print("执行handler函数")
    return plus
    
result = handler()
data = result(20) # 120
print(data)
```

### 6.3 参数

#### 6.3.1 形参和实参

```python
def get_data(val):  # val叫做形式参数,简称形参
    v = [11,22,33,44]
    print(v[val])    
  
get_dta(0)  # 调用的时候传入的参数叫做实际参数,简称实参
get_dta(1)
get_dta(2)
```

示例：

```python
def send_email(to_email):
	import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    msg = MIMEText('老板，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
    msg['From'] = formataddr(["男一号", 'nanyihao@163.com'])
    msg['To'] = formataddr(["老板", to_email])
    msg['Subject'] = "艾奇的导演"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("nanyihao@163.com", "mima")
    server.sendmail('nanyihao@163.com', [to_email, ], msg.as_string())
    server.quit()
    
user_input = input('请输入角色:').strip()

if user_input == '管理员':
    send_email('xxx@qq.com')
if user_input == '业务员':
    send_input('xxx@163.com')
if user_input == '老板':
    send_input('xxx.162.com')
```

练习题:

```python
# 1. 请写一个函数，函数计算列表 info = [11,22,33,44,55] 中所有元素的和
def val_sum():
    info = [11,22,33,44,55]
    data = 0
    fot i in info:
        data += i
    print(data)
    
val_sum()

# 2. 请写一个函数，函数计算列表中所有元素的和。
def get_list_sum(a1):
   	data = 0
    for item in a1:
        data += item
   	print(data)
    
get_list_sum([11,22,33])
get_list_sum([99,77,66])
v1 = [8712,123,123]

get_list_sum(v1)

# 3. 请写一个函数，函数将两个列表拼接起来。
def join_list(l1, l2):
    res = []
    res.extend(l1)
    res.extend(l2)
    print(res)
join_list([11,22,33],[55,66,77])

# 4. 计算一个列表的长度
def my_len(arg):
	count = 0
	for item in arg:
          count += 1
	print(count)

data = [11,22,33]
my_len(data)
len(data)


# 5. 发邮件的示例
def send_email(role,to):
    template = "要给%s%s发送邮件" %(role,to,)
    print(template)
 

user_input = input('请输入角色：')

if user_input == '管理员':
    send_email('管理员','xxxx@qq.com')
elif user_input == '业务员':
    send_email('业务员','xxxxo@qq.com')
elif user_input == '老板':
    send_email('老板','xoxox@qq.com')

```

#### 6.3.2 位置参数(调用函数执行并传入参数)

> 调用时传入参数

```python
def func(a1,a2):
    print(a1,a2)
    
func(1,3)
```

#### 6.3.3 关键字传参(调用函数执行并传入参数)

> 调用时传入参数

```python
def func(a1, a2):
    print(a1, a2)

func(a2=99,a1=2)

# 关键字传参数和位置传参可以混合使用（位置传入的参数 > 关键字参数在后 = 总参数个数）
def func1(a1, a2, a3):
    print(a1, a2, a3)

# func(1, 2, a3=9)
# func(1, a2=2, a3=9)
# func(a1=1, a2=2, a3=9)
# func(a1=1, 2,3) # 错误
```

#### 6.3.4 默认参数(定义函数时,写入)

> 定义函数时，写入

```python
def func(a1,a2,a3=9,a4=10):
    print(a1,a2,a3,a4)

func(11,22)
func(11,22,10)
func(11,22,10,100)
func(11,22,10,a4=100)
func(11,22,a3=10,a4=100)
func(11,a2=22,a3=10,a4=100)
func(a1=11,a2=22,a3=10,a4=100)
```

注意：对于函数的默认值慎用可变类型

```python
# 如果要给value设置默认是空列表
# 不推荐
def func(data, value = []):
    pass

# 推荐
def func(data, value = None):
    if not value:
        value = []
```

示例一：

```python
def func(a, b = []):
	b.append(a)
	return b

v1 = func(1)
v2 = func(22, [33,11,44])
v3 = func(3)
# [1,3] [33,11,44,22] [1,3]
print(v1,v2,v3)
```

示例二：

```python
def func(a, b = []):
	b.append(a)
	print(b)
func(1)
func(22, [33,11,44])
func(3)
# [1] [33,11,44,22] [1,3]
```

#### 6.3.5 动态参数

动态参数，定义函数时再形参位置用*或**可以接收任意个参数。

```python
def func(*args, **kwargs):
    print(args, kwargs)

func("周一", "周二", n1="周三", n2="周四")
```

在定义函数时可以用*和**，在执行函数时，同样也可以用

- 形参固定，实参用*和**

```python
def func(a1,a2):
    print(a1,a2)
    
func( 11, 22 )
func( a1=1, a2=2 )

func( *[11,22] )
func( **{"a1":11,"a2":22} )
```

- 形参用*和**，实参也用 * 和 * *

```python
def func(*args, **kwargs):
    print(args, kwargs)


func( 11, 22 )
func( 11, 22, name="joker", age=18 )

# 小坑，([11,22,33], {"k1":1,"k2":2}), {}
func( [11,22,33], {"k1":1,"k2":2} )

# args=(11,22,33),kwargs={"k1":1,"k2":2}
func( *[11,22,33], **{"k1":1,"k2":2} ) 
```

so，再使用format字符串格式化时，可以这样写：

```python
# 一般写法
v1 = "我是{},年龄{}".format("joker", 18)
v2 = "我是{name},年龄{age}".format(name="joker", age=18)

# 参数写法
v3 = "我是{},年龄{}".format(*["joker", 18])
v4 = "我是{name},年龄{age}".format(**{"name":"joker", "age":18})
```

- 综合使用：(`*args`, `**kwargs`)无敌

```python
def func(*args,**kwargs):
    print(args,kwargs)

func(1,2,3,4,5,k1=2,k5=9,k19=999)
func(*[1,2,3],k1=2,k5=9,k19=999)
func(*[1,2,3],**{'k1':1,'k2':3})
func(111,222,*[1,2,3],k11='joker',**{'k1':1,'k2':3})
```

**参数重点：**

```python
# 定义函数
def func1(a1,a2):
    pass 

def func2(a1,a2=None):
    pass 

def func3(*args,**kwargs):
    pass
```

#### 6.3.6 参数内存地址

> 谨记：函数执行传参时，传递的时内存地址

Python参数的这一特性有两个好处：

- 节省内存
- 对于可变类型且在函数中修改元素的内容，所有的地方都会修改，可变类型包括：列表、字典、集合

```python
# 可变类型可在函数内修改
def func(data):
    data.append(666)
    
v1 = [11,22,33]
func(v1)

print(v1) # [11,22,33,666]

# 可变类型重新赋值
def func(data):
    data = [11,22,33]

v1 = ["test", "重新复制"]
func(v1)

# 特殊情况：不可变类型，无法修改内部元素，只能重新赋值。
def func(data):
	data = 123
    
v1 = "test"
func(v1)
```

如果你不想让外部的变量和函数内部参数的变量一致，也可以选择将外部值拷贝一份，再传给函数。

```python
# 可变类型可在函数内修改
def func(data):
    data.append(999)


v1 = [11, 22, 33]
new_v1 = copy.deepcopy(v1) # 拷贝一份数据
func(new_v1)

print(v1)  # [11,22,33]
```

参数练习题，这个知识点在面试题中出现概率比较高，但实际开发中用的比较少。

```python
def func(a1, a2=20):
    print(a1, a2)
    print(id(a1), id(a2))
```

> 原理：Pyhton在创建函数(未执行)时，如果发现函数的参数中有默认值，则在函数内部会创建一块区域并维护这个内存地址。
>
> - 执行函数默认值未传值，则让a2指向函数维护的那个内存地址
>
> ```python
> func("root")
> ```
>
> - 执行默认值函数传值时，则让a3指向新传入的值的内存地址
>
> ```python
> func("root", 16)
> ```

在特定情况<span style="color:red;">默认参数的值时可变类型(list/dict/set)&函数内部会修改这个值</span>的情况下，参数默认值有坑。

示例一：

```python
# 在函数内存中会维护一块区域存储[11, 22, 33, 33]这个列表，内存地址：2239111939400
def func(a1, a2=[11,22]):
    a2.append(33)
    print(a1, a2)
    
func(100) #  100 [11, 22, 33]      1667927248 2239111939400
func(200) #  200 [11, 22, 33, 33]  1667930448 2239111939400

func(66, [44,55]) #  66 [44, 55, 33]  1667926160 2239111939336
func(88)  # 88 [11, 22, 33, 33, 33]  1667926864 2239111939400
```

示例二：

```python
# 在函数内存中会维护一块区域存储[11, 22, 100, 200, 400]这个列表，内存地址：2541783991624
def func(a1, a2=[11,22]):
    a2.append(a1)
    return a2

v1 = func(100)
print(v1, id(v1))  # [11, 22, 100] 2541783991624

v2 = func(200)
print(v2, id(v2))  # [11, 22, 100, 200] 2541783991624

v3 = func(300, [44,55])
print(v3, id(v3))  # [44, 55, 300] 2541783994312

v4 = func(400)
print(v4, id(v4))  # [11, 22, 100, 200, 400] 2541783991624
```

### 6.4 返回值

```python
def func(arg):
    # ....
    return 9 # 返回值为9 函数没有返回值时，默认返回：None

val = func('adsfadsf')


# return 可以返回任意类型
def func():
    return (1,2,3)

v = func()
print(v)

# 特殊:返回元组
def func():
    return 5,8,"alex"

v = func()
print(v)

# 返回列表
def func():
    data = [11, 22, 33]
    return data

v1 = func()
print(v1) # [11,22,33]
```

上述代码的执行过程：

- 执行func函数
- data = [11, 22, 33]创建一块内存区域，内部存储[11, 22, 33]，data变量指向这块内存地址
- return data 返回data指向的内存地址
- v1接收返回值，所以v1和data指向同一块内存地址[11, 22, 33]（两个变量指向此内存，引用计数器为2）
- 由函数执行完毕后，函数内部的变量都会被释放（data变量被删除，内存地址引用计数器-1）

- 所以，最终v1指向的函数内部创建的那块内存地址

示例：

```python
def func():
    data = [11, 22, 33]  # 1567715476808  1567715479496
    return data
v1 = func()
print(v1, id(v1))  # [11, 22, 33] 1567715476808

v2 = func()
print(v2, id(v2))  # [11, 22, 33] 1567715479496
```

练习:

```python
# 1. 让用户输入一段字符串，计算字符串中有多少A字符的个数。有多少个就在文件a.txt中写多少个“Python”.
def get_count(data):
    sum_count = 0
    for i in data:
        if i == 'A':
            sum_count += 1
    return sum_count


def write_file(data):
    if len(data) == 0:
        return False  # 函数执行过程中,一旦遇到return,则停止函数执行
    with open('a.txt', 'w', encoding='utf-8')as f:
        f.write(data)
    return True


cont = input('请输入:').strip()
res_data = get_count(cont)
write_data = res_data * 'Python'
status = write_file(write_data)
if status:
    print('写入成功!')
else:
    print('写入失败!')

```

总结：

```python
# 情况一:
def f1():
    pass
f1()

# 请况二:
def f2(a1):
    pass
f2(123456)

# 情况3
def f3():
    return 1 
v1 = f3()

# 情况4
def f4(a1,a2):
    # ... 
    return 999
v2 = f4(1,7)
```

练习题：

```python
'''# 1. 写函数，计算一个列表中有多少个数字，打印： 列表中有%s个数字。
#    提示：type('x') == int 判断是否是数字。'''


# 方式一:
def count_val(data):
    count = 0
    for i in data:
        if type(i) == int:
            count += i
    return '列表中有%s个数字' % count


res = count_val([1, 2, 3, 6, 'a', 'b', 'c'])
print(res)


# 方式二:
def count_val(data):
    count = 0
    for i in data:
        if type(i) == int:
            count += i
    msg = '列表中有%s个数字' % count
    print(msg)


count_val([1, 2, 3, 6, 'a', 'b', 'c'])


'''# 2. 写函数，计算一个列表中偶数索引位置的数据构造成另外一个列表，并返回。
'''
# 方式一
def count_lis(data):
    return data[::2]

res = count_lis([1, 2, 3, 4, 5, 6, 8, 7, 4, 5])
print(res)

# 方式二

def count_lis(data):
    lis = []
    for i in range(0, len(data)):
        if i % 2 == 0:
            lis.append(data[i])
    return lis


res = count_lis([1, 2, 3, 4, 5, 6, 8, 7, 4, 5])
print(res)

# 3. 读取文件，将文件的内容构造成指定格式的数据，并返回。
"""
a.log文件
    alex|123|18
    eric|uiuf|19
    ...
目标结构：
a.  ["alex|123|18","eric|uiuf|19"] 并返回。
b. [['alex','123','18'],['eric','uiuf','19']]
c. [
	{'name':'alex','pwd':'123','age':'18'},
	{'name':'eric','pwd':'uiuf','age':'19'},
]
"""

# 第一题:
# 方式一:
def data_type():
    with open('a.log', 'r', encoding='utf-8')as f:
        f1 = f.read()
        f2 = f1.split('\n')
    return f2


res = data_type()
print(res)

# 方式二:
def data_type():
    lis = []
    with open('a.log', 'r', encoding='utf-8')as f:
        for i in f:
            f1 = i.strip()
            lis.append(f1)
    return lis


res = data_type()
print(res)


# 第二题:
# 方式一:
def data_type():
    lis = []
    with open('a.log', 'r', encoding='utf-8')as f:
        f1 = f.readlines()
        for i in f1:
           lis.append(i.strip().split('\n'))
        return lis

res = data_type()
print(res)

# 方式二:
def data_type():
    lis = []
    with open('a.log', 'r', encoding='utf-8')as f:
        for i in f:
            f1 = i.strip().split('\n')
            lis.append(f1)
    return lis


res = data_type()
print(res)

# 第三题

def data_type():
    info = []
    with open('a.log', 'r', encoding='utf-8')as f:
        for i in f:
            f1 = i.strip().split('|')
            dic = {}
            dic['name'] = f1[0]
            dic['pwd'] = f1[1]
            dic['age'] = f1[2]
            info.append(dic)
    return info


res = data_type()
print(res)
```

注意：函数执行过程中只要遇到return语句，就会停止执行并返回结果，可以理解为return语句代表函数结束，如果未定义函数中指定return，那这个函数的返回值默认为None。

返回值与print的区别：

- 函数中使用print，只是用于再某个位置输入内容而已
- 函数中使用return，是为了将函数的执行结果返回给调用者，以便于后续其他操作

示例一：

```python
def f1():
    print(123)


def f2(arg):
    ret = arg()
    return ret


v1 = f2(f1)
print(v1)

# 输出
123
None
```

示例二：

```python
def f1():
    print(123)


def f2(arg):
    ret = arg()
    return f1


v1 = f2(f1)

v2 = v1()
print(v2)

# 输出
123
123
None
```

### 6.5 嵌套函数与作用域

作用域，可以理解为一块空间，这块空间的数据是可以共享的。通俗点来说，作用域就类似于一个房子，房子中的东西归里面的所有人共享，其他房子的人无法获取。

- python文件：全局作用域

- 函数：局部作用域

    ```python
    a = 1
    def s1():
        x1 = 666
        print(x1)
        print(a)
        print(b)
    
    b = 2
    print(a)
    s1()
    a = 88888
    def s2():
        print(a,b)
        s1()
    
    s2()
    ```


**总结：**

- 一个函数是一个作用域

    ```python
    def func():
        x = 9
        print(x)
    func()
    print(x)
    ```

- 作用域中查找数据规则：优先在自己的作用域找数据，自己没有就去 "父级" -> "父级" -> 直到全局，全部没有就报错。

    ```python
    x = 10
    def func():
        x = 9
        print(x)
    
    func()
    ```

- 练习题

    ```python
    # 第一题
    x = 10
    def func():
        x = 9
        print(x)
        def x1():
            x = 999
            print(x)
    func()  # 9
    
    # 第二题
    x = 10
    def func():
        x = 9
        print(x)
        def x1():
            x = 999
            print(x)
        x1()
    func()  # 9 999
    
    # 第三题
    x = 10
    def func():
        x = 9
        print(x)
        def x1():
            x = 999
            print(x)
        print(x)
        x1()
    
    func()  # 9 9 999
    
    # 第四题
    x = 10
    def func():
        x = 8
        print(x)
        def x1():
            x = 999
            print(x)
        x1()
        print(x)
    
    func()  # 8 999 8
    
    
    # 第五题
    x = 10
    def func():
        x = 8
        print(x)
        def x1():
            print(x)
        x1()
        print(x)
    
    func()  # 8 8 8
    
    
    # 第六题
    x = 10
    def func():
        x = 8
        print(x)
        def x1():
            print(x)
        x = 9
        x1()
        x = 10
        print(x)
    
    func()  # 8 9 10
    
    # 第七题
    x = 10
    def func():
        x = 8
        print(x)
        def x1():
            print(x)
    
        x1()
        x = 9
        x1()
        x = 10
        print(x)
    
    func()  # 8 8 9 10
    ```

- 子作用域中只能找到父级中的值 ，默认无法重新为父级/全局的变量进行赋值。(global/nonlocal可以强制做)

    ```python
    # 没有对全局变量赋值
    # 示例一:
    name = '在学校'
    def func():
        name = '写作业' # 在自己作用域再创建一个这样的值。
        print(name)
    func()
    print(name)
    
    # 示例二:
    name = [1,2,43]
    def func():
        name.append(999)
        print(name)
    func()
    print(name)
    
    # 对全局变量进行赋值
    # 示例一:global
    name = ["我好饿",'alex']
    def func():
        global name
        name = '哈哈'
    func()
    print(name)
    
    # 示例二:global
    name = "老男孩"
    def func():
        name = 'alex'
        def inner():
            global name  # 找到全局的name，重新赋值全局的name，局部作用域的没有修改
            name = 999
        inner()
        print(name)
    func()
    print(name)
    
    # 示例三:nonlocal
    name = "老男孩"
    def func():
        name = 'alex'
        def inner():
            nonlocal name # 找到上一级的name，重新赋值上一级的name，全局的name没有修改
            name = 999
        inner()
        print(name)
    func()
    print(name)
    ```

### 6.6 函数小高级

函数赋值：

```python
def func():
    print(123)
    
v1 = func 

func()
v1（）
```

```python
def func():
    print(123)
    
func_list = [func, func, func]
# func_list[0]()
# func_list[1]()
# func_list[2]()
for item in func_list:
    v = item()
    print(v)
```

```python
def func():
    print(123)

def bar():
    print(666)

info = {'k1': func, 'k2': bar}

info['k1']()
info['k2']()
```

容易混淆：

```python
def func():
    return 123

func_list1 = [func,func,func]
func_list2 = [func(),func(),func()]

print(func_list1)
print(func_list2)

info = {
    'k1':func,
    'k2':func(),
}

print(info)
```

函数可以当作参数进行传递：

```python
def func(arg):
    print(arg)
    
func(1)
func([1,2,3,4])

def show():
    return 999
func(show)
```

```python
def func(arg):
    v1 = arg()
    print(v1)
    
def show():
    print(666)
    
func(show)
```

```python
def func(arg):
    v1 = arg()
    print(v1)
    
def show():
    print(666)
    
result = func(show)
print(result)
```

面试题：

```python
def func():
    print('花费查询')


def bar():
    print('语音沟通')


def base():
    print('xxx')


def show():
    print('xxx')


def test():
    print('xxx')

info = {
    'f1': func,
    'f2': bar,
    'f3':base,
    'f4':show,
    'f5':test
}
choice = input('请选择要选择功能：')
function_name = info.get(choice)
if function_name:
    function_name()
else:
    print('输入错误')
```

### 6.7 lambda表达式

用于表示简单的函数(又称匿名函数)

```python
# 三元运算，为了解决简单的if else的情况，如：
if 1 == 1:
    a = 123
else:
    a = 456

a =  123  if 1 == 1 else 456

# lambda表达式，为了解决简单函数的情况，如：
def func(a1,a2):
    return a1 + 100 

func = lambda a1,a2: a1+100
```

```python
func1 = lambda : 100 

func2 = lambda x1: x1 * 10

func3 = lambda *args,**kwargs: len(args) + len(kwargs)

DATA = 100
func4 = lambda a1: a1 + DATA
v = func4(1)
print(v)


DATA = 100
def func():
    DATA = 1000
    func4 = lambda a1: a1 + DATA
    v = func4(1)
    print(v)
func()


func5 = lambda n1,n2: n1 if n1 > n2 else n2
v = func5(1111,2)
print(v)
```

练习题：

```python
# 练习题1
USER_LIST = []
def func0(x):
    v = USER_LIST.append(x)
    return v 

result = func0('alex')
print(result)


# 练习题2

def func0(x):
    v = x.strip()
    return v 

result = func0(' alex ')
print(result)

# 总结：列表所有方法基本上都是返回None；字符串的所有方法基本上都是返回新值

# 练习题3
USER_LIST = []
func1 = lambda x: USER_LIST.append(x)

v1 = func1('alex')
print(v1)
print(USER_LIST)

# 练习题4
func1 = lambda x: x.split('l')

v1 = func1('alex')
print(v1)

# 练习题5
func_list = [lambda x:x.strip(), lambda y:y+199,lambda x,y:x+y]

v1 = func_list[0]('alex ')
print(v1)

v2 = func_list[1](100)
print(v2)

v3 = func_list[2](1,2)
print(v3)
```

### 6.8 内置函数

- 自定义函数

- 内置函数

    - 其他
        - `len`
        - `open`
        - `range`
        - `id`
        - `type`
    - 输入输出
        - `print`
        - `input`
    - 强制转换
        - `dict()`
        - `list()`
        - `tuple()`
        - `int()`
        - `str()`
        - `bool()`
        - `set()`

    - 数学相关
        - `abs`，绝对值

            ```python
            v = abs(-1)
            print(v)
            ```

        - `float`，转换成浮点型（小数）

            ```python
            v = 55
            v1 = float(55)
            print(v1)
            ```

        - `max`，找到最大值

            ```python
            v = [1,2,311,21,3,]
            result = max(v)
            print(result)
            ```

        - `min`，找最小值

            ```python
            v = [1,2,311,21,3,]
            result = min(v)
            print(result)
            ```

        - `sum`，求和

            ```python
            v = [1,2,311,21,3,]
            result = sum(v)
            print(result)
            ```

        - `divmod`，两数相除的商和余数

            ```python
            a,b = divmod(1001,5)
            print(a,b)
            ```

            ```python
            # 练习题  请通过分页对数据进行展示
            """
            要求：
                每页显示10条数据
                让用户输入要查看的页面：页码
            """
            
            USER_LIST = []
            for i in range(1,836):
                temp = {'name':'你少妻-%s' %i,'email':'123%s@qq.com' %i }
                USER_LIST.append(temp)
            
            # 数据总条数
            total_count = len(USER_LIST)
            
            # 每页显示10条
            per_page_count= 10
            
            # 总页码数
            max_page_num,a = divmod(total_count,per_page_count)
            if a>0:
                max_page_num += 1
            
            while True:
                pager = int(input('要查看第几页：'))
                if pager < 1 or pager > max_page_num:
                    print('页码不合法，必须是 1 ~ %s' %max_page_num )
                else:
                    """
                    # 第1页：USER_LIST[0:10] -> 0123456789
                    # 第2页：USER_LIST[10:20]
                    # 第3页：USER_LIST[20:30]
                    ...
                    """
                    start = (pager-1) * per_page_count
                    end = pager * per_page_count
                    data = USER_LIST[start:end]
                    for item in data:
                        print(item)
            ```

    - 进制转换相关

        - `bin`，将十进制转化成二进制

            ```python
            num = 13
            v1 = bin(num)
            print(v1)
            ```

        - `oct`，将十进制转换成八进制

            ```python
            num = 8
            v1 = oct(num)
            print(v1)
            ```

        - `int`，将其他进制转化成十进制

            ```python
            # 二进制转化成十进制
            v1 = '0b1101'
            result = int(v1,base=2)
            print(result)
            
            # 八进制转化成十进制
            v1 = '0o1101'
            result = int(v1,base=8)
            print(result)
            
            # 十六进制转化成十进制
            v1 = '0x1101'
            result = int(v1,base=16)
            print(result)
            ```

        - `hex`，将十进制转换成十六进制

            ```python
            num = 16
            v1 = hex(num)
            print(v1)
            ```

        - 面试题

            ```python
            # 1字节等于8位
            # IP: 192.168.12.79  ->  001010010 . 001010010 . 001010010 . 001010010
            
            # 1. 请将 ip = "192.168.12.79" 中的每个十进制数转换成二进制并通过,连接起来生成一个新的字符串。
            ip = "192.168.12.79"
            ip_list = ip.split('.') # ['192','168','12','79']
            result = []
            for item in ip_list:
                result.append(bin(int(item)))
            print(','.join(result))
            
            
            # 2. 请将 ip = "192.168.12.79" 中的每个十进制数转换成二进制: 
            #   0010100100001010010001010010001010010 -> 十进制的值。
            
            # 3232238671
            ```

### 6.9 函数中的高级

#### 6.9.1 函数可以做返回值

示例一：

```python
def func():
    print(123)

def bar():
    return func

v = bar()

v()
```

示例二：

```python
name = 'oldboy'
def func():
    print(name)
    
def bar():
    return func

v = bar()

v()
```

示例三：

```python
def bar():
    def inner():
        print(123)
    return inner
v = bar()
v()
```

示例四：

```python
name = 'oldboy'
def bar():
    name = 'alex'
    def inner():
        print(name)
    return inner
v = bar()
v()
```

示例五：

```python
name = 'oldboy'
def bar(name):
    def inner():
        print(name)
    return inner
v1 = bar('alex') # { name=alex, inner }  # 闭包，为函数创建一块区域（内部变量供自己使用），为他以后执行提供数据。
v2 = bar('eric') # { name=eric, inner }
v1()
v2()
```

练习题：

```python
# 第一题
name = 'alex'
def base():
    print(name)

def func():
 	name = 'eric'
    base()

func()
    

# 第二题
name = 'alex'

def func():
 	name = 'eric'
    def base():
    	print(name)
    base()
func()

# 第三题
name = 'alex'

def func():
 	name = 'eric'
    def base():
    	print(name)
    return base 
base = func()
base()
```

注意：函数在何时被谁创建？

示例一：

```python
info = []

def func():
    print(item)
    
for item in range(10):
    info.append(func)

info[0]()
```

实例二：

```python
info = []

def func(i):
    def inner():
        print(i)
	return inner

for item in range(10):
    info.append(func(item))

info[0]()
info[1]()
info[4]()
```

### 6.10 闭包

闭包，简而言之就是将数据封装在一个包（区域）中，使用时再去里面取。（本质上闭包是基于函数嵌套搞出来一个特殊嵌套）

返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，这使得，该函数无论在何处调用，优先使用自己外层包裹的作用域

闭包函数必须满足两个条件：

- 函数内部定义的函数

- 包含对外部作用域而非全局作用域的引用

```python
def func(name):
    def inner():
        print(name)  # 封装值 + 内层函数需要使用
	return inner 

v1 = func('alex')
v1()
v2 = func('eric')
v2()
```

- 闭包应用场景1：封装数据防止污染全局

```python
name = "joker"

def f1():
    print(name)

def f2():
	print(name)

def f3():
    print(name)

def f4():
	print(name)
```

```python
def func(age):
    name = "joker"
    def f1():
    	print(name, age)

    def f2():
        print(name, age)
        
	def f3():
	    print(name, age)

    def f4():
        print(name, age)
    f1()
    f2()
    f3()
    f4()

func(108)
```

- 闭包应用场景2：封装数据封到一个包里，使用时在取。

```python
def task(arg):
    def inner():
        print(arg)
    return inner

v1 = task(11)
v2 = task(22)
v3 = task(33)
v1()
v2()
v3()
```

```python
def task(arg):
    def inner():
        print(arg)
    return inner

inner_func_list = []
for val in [11,22,33]:
    inner_func_list.append( task(val) )
    
inner_func_list[0]() # 11
inner_func_list[1]() # 22
inner_func_list[2]() # 33
```

```python
""" 基于多线程去下载视频 """
from concurrent.futures.thread import ThreadPoolExecutor

import requests


def download_video(url):
    res = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
        }
    )
    return res.content


def outer(file_name):
    def write_file(response):
        content = response.result()
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)

    return write_file


POOL = ThreadPoolExecutor(10)

video_dict = [
    ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
    ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
    ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
]
for item in video_dict:
    future = POOL.submit(download_video, url=item[1])
    future.add_done_callback(outer(item[0]))

POOL.shutdown()
```

### 6.11 内置函数

![image-20201230201618164](j:\homework\Python学习笔记\Python_notes.assets\image-20201230201618164.png)

- 编码相关

    - `chr`，将十进制数字转换成` unicode `编码中的对应字符串。

        ```python
        v = chr(99)
        print(v)
        ```

    - `ord`，根据字符在`unicode`编码中找到其对应的十进制。

        ```python
        num = ord('中')
        ```

- 高级一点的内置函数

    - map，循环每个元素（第二个参数），然后让每个元素执行函数（第一个参数），将每个函数执行的结果保存到新的列表中，并返回。

        ```python
        v1 = [11,22,33,44]
        result = map(lambda x:x+100,v1)
        print(list(result)) # 特殊
        ```

    - filter，对于序列中的元素进行筛选，最终获取符合条件的序列。

        ```python
        v1 = [11,22,33,'asd',44,'xf']
        
        def func(x):
            if type(x) == int:
                return True
            return False
        result = filter(func,v1) # [11,]
        print(list(result))
        
        
        result = filter(lambda x: True if type(x) == int else False ,v1)
        print(list(result))
        
        result = filter(lambda x: type(x) == int ,v1)
        print(list(result))
        ```

    - reduce，对于序列内所有元素进行累计操作。

        ```python
        import functools
        v1 = ['wo','hao','e']
        
        def func(x,y):
            return x+y
        result = functools.reduce(func,v1) 
        print(result)
        
        result = functools.reduce(lambda x,y:x+y,v1)
        print(result)
        ```

### 6.12 递归

函数自己调用自己(效率低)

示例一：

```python
def func():
	print(1)
	func()
func()
```

示例二：

```python
def func(i):
	print(i)
	func(i + 1)
func(1)
```

示例三：

```python
import time
def func(a, b):
    time.sleep(2)
	print(b)
	func(b, a+b)
func(0, 1)
# 实现斐波那契
```

示例四：

```python
def func(a):
	if a == 5:
		return 10000
	result  = func(a+1) + 10
	return result

v = func(1)
```

示例五:

```python
# 递归的返回值
def func(a):
	if a == 5:
		return 10000
	result = func(a+1) + 10
	
v = func(1)

name = 'alex'
def func():
	def inner():
		print(name)
	return inner

v = func()
```

递归与栈的关系总结：

- 必须有一个明确的结束条件
- 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
- 递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）

### 6.13 装饰器

实现原理：基于@语法和函数闭包，将原函数封装在闭包中，然后将函数赋值为一个新的函数（内层函数），执行函数时，再在内层函数中执行闭包中的原函数。

实现效果：可以在不改变原函数内部代码和调用方式的前提下，实现在函数执行和执行扩展功能。

适用场景：多个函数系统统一在执行前后自定义一些功能。

现在给你一个函数，在不修改函数源码的前提下，实现在函数执行前和执行后分别输入 "before" 和 "after"。

```python
def func():
    print("我是func函数")
    value = (11,22,33,44) 
    return value
    
result = func()
print(result)
```

#### 6.13.1 第一回合

你的实现思路：

```python
def func():
    print("before")
    
    print("我是func函数")
    value = (11,22,33,44) 
    
    print("after")
    
    return value
    
result = func()
```

实现思路：

```python
def func():
    print("我是func函数")
    value = (11, 22, 33, 44)
    return value


def outer(origin):
    def inner():
        print('inner')
        origin()
        print("after")

    return inner

func = outer(func)
result = func()
```

处理返回值：

```python
def func():
    print("我是func函数")
    value = (11, 22, 33, 44)
    return value


def outer(origin):
    def inner():
        print('inner')
        res = origin()
        print("after")
        return res
    return inner

func = outer(func)
result = func()
```

#### 6.13.2 第二回合

在Python中有个一个特殊的语法糖：

```python
def outer(origin):
    def inner():
        print('inner')
        res = origin()
        print("after")
        return res
    return inner


@outer
def func():
    print("我是func函数")
    value = (11, 22, 33, 44)
    return value


func()
```

#### 6.13.3 第三回合

请在这3个函数执行前和执行后分别输入 "before" 和 "after"

```python
def func1():
    print("我是func1函数")
    value = (11, 22, 33, 44)
    return value
    
    
def func2():
    print("我是func2函数")
    value = (11, 22, 33, 44)
    return value
    
def func3():
    print("我是func3函数")
    value = (11, 22, 33, 44)
    return value
    
func1()
func2()
func3()
```

你的实现思路：

```python
def func1():
    print('before')
    print("我是func1函数")
    value = (11, 22, 33, 44)
    print("after")
    return value
    
    
def func2():
    print('before')
    print("我是func2函数")
    value = (11, 22, 33, 44)
    print("after")
    return value
    
def func3():
    print('before')
    print("我是func3函数")
    value = (11, 22, 33, 44)
    print("after")
    return value
    
func1()
func2()
func3()
```

我的实现思路：

```python
def outer(origin):
    def inner():
        print("before 110")
        res = origin()  # 调用原来的func函数
        print("after")
        return res

    return inner


@outer
def func1():
    print("我是func1函数")
    value = (11, 22, 33, 44)
    return value


@outer
def func2():
    print("我是func2函数")
    value = (11, 22, 33, 44)
    return value


@outer
def func3():
    print("我是func3函数")
    value = (11, 22, 33, 44)
    return value


func1()
func2()
func3()
```

装饰器，在不修改原函数内容的前提下，通过@函数可以实现在函数前后自定义执行一些功能（批量操作会更有意义）。

**优化**

优化以支持多个参数的情况。

```python
def outer(origin):
    def inner(*args, **kwargs):
        print("before 110")
        res = origin(*args, **kwargs)  # 调用原来的func函数
        print("after")
        return res

    return inner


@outer  # func1 = outer(func1)
def func1(a1):
    print("我是func1函数")
    value = (11, 22, 33, 44)
    return value


@outer  # func2 = outer(func2)
def func2(a1, a2):
    print("我是func2函数")
    value = (11, 22, 33, 44)
    return value


@outer  # func3 = outer(func3)
def func3(a1):
    print("我是func3函数")
    value = (11, 22, 33, 44)
    return value


func1(1)
func2(11, a2=22)
func3(999)
```

- 其中，我的那种写法就称为装饰器。

    - 实现原理：基于@语法和函数闭包，将原函数封装在闭包中，然后将函数赋值为一个新的函数（内层函数），执行函数时再在内层函数中执行闭包中的原函数。

    - 实现效果：可以在不改变原函数内部代码 和 调用方式的前提下，实现在函数执行和执行扩展功能。

    - 适用场景：多个函数系统统一在执行前后自定义一些功能。

- 装饰器示例：

    ```python
    def outer(origin):
        def inner(*args, **kwargs):
    		# 执行前
            res = origin(*args, **kwargs)  # 调用原来的func函数
            # 执行后
            return res
        return inner
    
    
    @outer
    def func():
        pass
    
    func()
    ```

- 带参数的装饰器

    ```python
    # ################## 普通装饰器 #####################
    def wrapper(func):
        def inner(*args,**kwargs):
            print('调用原函数之前')
            data = func(*args,**kwargs) # 执行原函数并获取返回值
            print('调用员函数之后')
            return data
        return inner 
    
    @wrapper
    def index():
        pass
    
    # ################## 带参数装饰器 #####################
    def x(counter):
        def wrapper(func):
            def inner(*args,**kwargs):
                data = func(*args,**kwargs) # 执行原函数并获取返回值
                return data
            return inner 
    	return wrapper 
    
    @x(9)
    def index():
        pass
    ```
    
    练习题:
    
    ```python
    # 写一个带参数的装饰器，实现：参数是多少，被装饰的函数就要执行多少次，把每次结果添加到列表中，最终返回列表。
    def xxx(counter):
        print('x函数')
        def wrapper(func):
            print('wrapper函数')
            def inner(*args,**kwargs):
                v = []
                for i in range(counter):
                data = func(*args,**kwargs) # 执行原函数并获取返回值
                    v.append(data)
            return v
            return inner
        return wrapper
    
    @xxx(5)
    def index():
        return 8
    
    v = index()
    print(v)
    
    # 写一个带参数的装饰器，实现：参数是多少，被装饰的函数就要执行多少次，并返回最后一次执行的结果【面试题】
    def xxx(counter):
        print('x函数')
        def wrapper(func):
            print('wrapper函数')
            def inner(*args,**kwargs):
                for i in range(counter):
                    data = func(*args,**kwargs) # 执行原函数并获取返回值
                return data
            return inner
        return wrapper
    
    @xxx(5)
    def index():
        return 8
    
    v = index()
    print(v)
    
    # 写一个带参数的装饰器，实现：参数是多少，被装饰的函数就要执行多少次，并返回执行结果中最大的值。
    def xxx(counter):
        print('x函数')
        def wrapper(func):
            print('wrapper函数')
            def inner(*args,**kwargs):
                value = 0
                for i in range(counter):
                    data = func(*args,**kwargs) # 执行原函数并获取返回值
                    if data > value:
                        value = data 
                return value
            return inner
        return wrapper
    
    @xxx(5)
    def index():
        return 8
    
    v = index()
    print(v)
    
    # 多种情况判断写到一个装饰器里
    def x(counter):
        print('x函数')
        def wrapper(func):
            print('wrapper函数')
            def inner(*args,**kwargs):
                if counter:
                    return 123
                return func(*args,**kwargs)
            return inner
        return wrapper
    
    @x(True)
    def fun990():
        pass
    
    @x(False)
    def func10():
        pass
    ```

总结：

- 目的：在不改变原函数的基础上，在函数执行前后自定义功能。

- 编写装饰器和应用

    ```python
    # 装饰器的编写
    def x(func):
        def y():
            # 前
            ret = func()
            # 后
            return ret 
       	return y 
    
    # 装饰器的应用
    @x
    def index():
        return 10
    
    @x
    def manage():
        pass
    
    # 执行函数，自动触发装饰器了
    v = index()
    print(v)
    ```

- 应用场景：想要为函数扩展功能时，可以选择用装饰器。

- 记住：

    - 装饰器编写格式

        ```python
        def 外层函数(参数): 
            def 内层函数(*args,**kwargs):
                return 参数(*args,**kwargs)
            return 内层函数
        ```

    - 装饰器应用格式

        ```python
        @外层函数
        def index():
            pass
        
        index()
        ```

    - 带参数的装饰器

        ```python
        def x(counter):
            def wrapper(func):
                def inner(*args,**kwargs):
                    data = func(*args,**kwargs) # 执行原函数并获取返回值
                    return data
                return inner 
        	return wrapper 
        
        @x(9)
        def index():
            pass
        ```

### 6.14 推导式

列表推导式

- 基本格式

    ```python
    """
    目的：方便的生成一个列表。
    格式：
    	v1 = [i for i in 可迭代对象 ]
    	v2 = [i for i in 可迭代对象 if 条件 ] # 条件为true才进行append
    """
    v1 = [ i for i in 'alex' ]  
    v2 = [i+100 for i in range(10)]
    v3 = [99 if i>5 else 66  for i in range(10)]
    
    def func():
        return 100
    v4 = [func for i in range(10)]
    
    v5 = [lambda : 100 for i in range(10)]
    result = v5[9]()
    
    def func():
        return i
    v6 = [func for i in range(10)]
    result = v6[5]()
    
    v7 = [lambda :i for i in range(10)]
    result = v7[5]()
    
    
    v8 = [lambda x:x*i for i in range(10)] # 新浪微博面试题
    # 1.请问 v8 是什么？
    # 2.请问 v8[0](2) 的结果是什么？
    
    # 面试题
    def num():
        return [lambda x:i*x for i in range(4)]
    # num() -> [函数,函数,函数,函数]
    print([ m(2) for m in num() ]) # [6,6,6,6]
    
    # ##################### 筛选 #########################
    v9 = [i for i in range(10) if i > 5]
    ```

- 集合推导式

    ```python
    v1 = { i for i in 'alex' }
    ```

- 字典的推导式

    ```python
    v1 = { 'k'+str(i):i for i in range(10) }
    ```

**练习题**

1. 去除列表中每个元素的.mp4后缀

```python
data_list = [
    '1-5 编译器和解释器.mp4',
    '1-17 今日作业.mp4',
    '1-9 Python解释器种类.mp4',
    '1-16 今日总结.mp4',
    '1-2 课堂笔记的创建.mp4',
    '1-15 Pycharm使用和破解（win系统）.mp4',
    '1-12 python解释器的安装（mac系统）.mp4',
    '1-13 python解释器的安装（win系统）.mp4',
    '1-8 Python介绍.mp4', '1-7 编程语言的分类.mp4',
    '1-3 常见计算机基本概念.mp4',
    '1-14 Pycharm使用和破解（mac系统）.mp4',
    '1-10 CPython解释器版本.mp4',
    '1-1 今日概要.mp4',
    '1-6 学习编程本质上的三件事.mp4',
    '1-18 作业答案和讲解.mp4',
    '1-4 编程语言.mp4',
    '1-11 环境搭建说明.mp4'
]
res = [item.split(".")[0] for item in data_list]
print(res)
```

2. 将字典中的元素按照  键-值 格式化，并最终使用 ；连接起来。

```python
info = {
    "name":"武沛齐",
    "email":"xxx@live.com",
    "gender":"男",
}

res = ";".join(["{}-{}".format(k, v) for k, v in info.items()])
print(res)
```

3. 将字典按照键从小到大排序，然后再按照如下格式拼接起来。（微信支付API内部处理需求）

```python
info = {
    'sign_type': "MD5",
    'out_refund_no': "12323",
    'appid': 'wx55cca0b94f723dc7',
    'mch_id': '1526049051',
    'out_trade_no': "ffff",
    'nonce_str': "sdfdffd",
    'total_fee': 9901,
    'refund_fee': 10000
}

data = "&".join(["{}={}".format(key, value) for key, value in sorted(info.items(), key=lambda x: x[0])])
print(data)
```

4. 看代码写结果

```python
def func():
    print(123)


data_list = [func for i in range(10)]

print(data_list)
```

5. 看代码写结果

```python
def func(num):
    return num + 100


data_list = [func(i) for i in range(10)]

print(data_list)
```

6. 看代码写结果（执行出错，通过他可以让你更好的理解执行过程）

```python
def func(x):
    return x + i

data_list = [func for i in range(10)]

val = data_list[0](100)
print(val)
```

7. 看代码写结果（新浪微博面试题）

```python
data_list = [lambda x: x + i for i in range(10)]  # [函数,函数,函数]   i=9

v1 = data_list[0](100)
v2 = data_list[3](100)
print(v1, v2)  # 109 109
```

**小高级**

1. 推导式支撑嵌套

```python
data = [ (i,j) for j in range(5) for i in range(10)]

data = []
for i in range(10):
    for j in range(5):
        data.append( (i,j) )
```

```python
# 一副扑克牌

poker_list = [ (color,num) for num in range(1,14) for color in ["红桃", "黑桃", "方片", "梅花"]]

poker_list = [ [color, num] for num in range(1, 14) for color in ["红桃", "黑桃", "方片", "梅花"]]

print(poker_list)	
```

2. 烧脑面试题

```python
def num():
    return [lambda x: i * x for i in range(4)]


# 1. num()并获取返回值  [函数,函数,函数,函数] i=3
# 2. for循环返回值
# 3. 返回值的每个元素(2)
result = [m(2) for m in num()]  # [6,6,6,6]
print(result)
```

```python
def num():
    return (lambda x: i * x for i in range(4))


# 1. num()并获取返回值  生成器对象
# 2. for循环返回值
# 3. 返回值的每个元素(2)
result = [m(2) for m in num()]  # [0,2,4,6 ]
print(result)
```

### 6.15 生成器

> - **在 Python 中，使用了 yield 的函数被称为生成器（generator）。**
>
> - **跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。**
>
> - **在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值，并在下一次执行 next() 方法时从当前位置继续运行。**
>
> - **调用一个生成器函数，返回的是一个迭代器对象。**

<font color="red">**生成器是由函数+yield关键字创造出来的写法，在特定情况下，用他可以帮助我们节省内存。**</font>

- 生成器函数，当函数中有yield存在时，这个函数就是生成器函数。

```python
def func():
    print(111)
    yield 1
    
    print(222)
    yield 2

    print(333)
    yield 3

    print(444)
```

- 生成器对象，执行生成器函数时，会返回一个生成器对象。

```python
def func():
    print(111)
    yield 1
    
    print(222)
    yield 2

    print(333)
    yield 3

    print(444)

data = func()

print(data)  #  <generator object func at 0x000001BFB0C7A2B0>
# 执行生成器函数func()，返回生成器对象
# 注意：执行生成器函数时，函数内部代码不会被执行
```

```python
def func():
    print(111)
    yield 1
    
    print(222)
    yield 2

    print(333)
    yield 3

    print(444)
    
data = func()

# 执行方式next
v1 = next(data)
print(v1)
v2 = next(data)
print(v2)
v3 = next(data)
print(v3)
v4 = next(data)
print(v4)  # 结束或中途遇到return，程序报错：StopIteration
```

```python
# 执行方式for循环--常用
data = func()
for item in data:
    print(item)
```

生成器得特点：记录在函数中的执行位置，下次执行next时，会基于上一次得位置基础上再继续向下执行。

**引用场景**

- 假设要让你生成200W个随机4位数，并打印出来
  - 在内存中一次性创建200w个
  - 动态创建，用一个创建一个

```python
import random

val = random.randint(1000, 9999)
print(val)
```

第一种方式：

```python
import random

data_list = []
for i in range(2000000):
    val = random.randint(1000, 999)
    data_list.append(val)
# 使用时，去data_list中获取
```

  第二种方式：

  ```python
import random
  
def get_random_num(max_count):
    counter = 0
    while counter < max_count:
      yield random.randint(1000, 9999)
      counter += 1
data_list = get_random_num(2000000)
print(next(data_list))
# 使用时，去data_list中获取
  ```

**扩展**

```python
def func():
    print(111)
    v1 = yield 1
    print(v1)

    print(222)
    v2 = yield 2
    print(v2)

    print(333)
    v3 = yield 3
    print(v3)

    print(444)


data = func()

n1 = data.send(None)
print(n1)

n2 = data.send(666)
print(n2)

n3 = data.send(777)
print(n3)

n4 = data.send(888)
print(n4)
```

在Python中，边循环边计算的后面元素机制的算法，称为生成器：**generator**。

普通生成器：

```python
f = [x * x for x in range(3)]
print(f)
# 结果:[0, 1, 4]

# 生成器创建方式
s = (x * x for x in range(3))
print(s)  # 结果:<generator object <genexpr> at 0x0000000002920A98>
print(next(s))
print(next(s))
print(next(s))
print(next(s))  # 报错:# StopIteration
```

备注:

- 只要把列表推导式的`[]`改成`()`就创建了一个生成器。
- 可以通过`next()`函数获得生成器的下一个返回值。
- 元素超出范围后会报一个`StopIteration`的错误。

函数生成器：

函数：斐波那契

```python
def fbnq(num):
    a, b, n = 0, 1, 0
    while n < num:
        n = a + b
        a = b  # 把b的值赋值给a
        b = n  # ab+f赋值给b
        print(n)
fbnq(10)
```

生成器：斐波那契

```python
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

- 想把fbnq函数变更生成器，把`print`改成`yield`就可以了
- 函数是按顺序执行，遇到return或到最后一行就返回，生成器函数每次调用`next`执行，遇到yield语句就会暂停，并且把值返回，程序并没自终止，再次next调用时会接着上次继续执行。

### 6.16 迭代器

> - **迭代是Python最强大的功能之一，是访问集合元素的一种方式。**
>
> - **迭代器是一个可以记住遍历的位置的对象。**
>
> - **迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。**
>
> - **迭代器有两个基本的方法：iter() 和 next()。**

字符串，列表或元组对象都可用于创建迭代器：

```python
list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))  # 通过 StopIteration 异常标识迭代的完成
```

可以直接用于for循环遍历的对象称为可迭代对象：**Iterable**，可迭代的意思就是可循环/遍历。

```python
list = [1, 2, 3, 4]
it = iter(list)
for i in it:
    print(i, end="")
```

也可以用next函数

```python
import sys
list = [1, 2, 3, 4]
it = iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
```

**创建一个迭代器**

把一个类作为一个迭代器使用需要在类中实现两个方法 `__iter__()` 和 `__next__()` 。

Python的初始化函数为 `__init__()` 它会在对象初始化的时候执行。

`__iter__()` 方法返回一个特殊的迭代对象，这个迭代对象实现了 `__next__()` 方法并通过StopLteration异常表示迭代的完成。

`__next__()` 方法会返回下一个迭代对象。

```python
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
```

**StopIteration**

StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

判断一个对象是否可迭代：Iterable

```python
from collections import Iterable

print(isinstance([], Iterable))  # True
print(isinstance((), Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance("web", Iterable))  # True
print(isinstance(123, Iterable))  # False
print(isinstance((x for x in range(10)), Iterable))  # True
```

可以被next()函数调用并不断返回下一个值的对象称为迭代器：**Iterator**。

判断一个对象是否是迭代器：lterator

```python
from collections import Iterable,Iterator

print(isinstance([], Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance('web', Iterator))  # False
print(isinstance(123, Iterator))  # False
print(isinstance((x for x in range(10)), Iterator))  # True
```

把`list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用`iter()`函数

```python
from collections import Iterable,Iterator

print(isinstance(iter([]), Iterator))  # True
print(isinstance(iter({}), Iterator))  # True
print(isinstance(iter('web'), Iterator))  # True
print(isinstance((x for x in range(10)), Iterator))  # True
```

备注:

- 凡是可作用于 `for` 循环的对象都是 `Iterable` 类型
- 凡是可作用于 `next()` 函数的对象都是 `Iterator` 类型
- 生成器都是 `Iterator` 对象，但 `list` 、 `dict` 、`str` 虽然是 `Iterable` ，却不是 `Iterator` ，可以通过`iter()` 函数获得一个 `Iterator` 对象
- 生成器一定是迭代器，但迭代器不一定是生成器

---

## 第七章 模块

为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。在Python中，一个.py文件就称之为一个模块（Module）。

模块分为三种：

- 内置标准模块（又称标准库）执行help('modules')查看所有python自带模块列表
- 第三方开源模块，可通过pip install 模块名，连网安装
- 自定义模块

### 7.1 字符串加密（hashlib）

将指定的 “字符串” 进行加密。

```python
import hashlib

def get_md5(data):
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result

val = get_md5('123')
print(val)
```

加盐：

```python
import hashlib

def get_md5(data):
    obj = hashlib.md5("sidrsicxwersdfsaersdfsdfresdy54436jgfdsjdxff123ad".encode('utf-8'))
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result

val = get_md5('123')
print(val)
```

应用：

```python
import hashlib
USER_LIST = []
def get_md5(data):
    obj = hashlib.md5("12:;idrsicxwersdfsaersdfsdfresdy54436jgfdsjdxff123ad".encode('utf-8'))
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result


def register():
    print('**************用户注册**************')
    while True:
        user = input('请输入用户名:')
        if user == 'N':
            return
        pwd = input('请输入密码:')
        temp = {'username':user,'password':get_md5(pwd)}
        USER_LIST.append(temp)

def login():
    print('**************用户登陆**************')
    user = input('请输入用户名:')
    pwd = input('请输入密码:')

    for item in USER_LIST:
        if item['username'] == user and item['password'] == get_md5(pwd):
            return True


register()
result = login()
if result:
    print('登陆成功')
else:
    print('登陆失败')
```

### 7.2 不显示密码（getpass）

```python
# 密码不显示（只能在终端运行）
import getpass

pwd = getpass.getpass('请输入密码：')
if pwd == '123':
    print('输入正确')
```

### 7.3 随机生成（random）

程序中有很多地方需要用到随机字符，比如登录网站的随机验证码，通过random模块可以很容易生成随机字符串。

```python
import random

def get_random_code(length=6):
    data = []
    for i in range(length):
        v = random.randint(65,90)
        data.append(chr(v))

    return  ''.join(data)


code = get_random_code()
print(code)


import random # 导入一个模块 
v = random.randint(起始, 终止) # 得到一个随机数
```

### 7.4  运行环境的变量和函数（sys）

python解释器相关的数据。

- `sys.getrefcount` , 获取一个值的应用计数

    ```python
    import sys
    
    a = [11, 22, 33]
    b = a
    print(sys.getrefcount(a))
    ```

- `sys.getrecursionlimit` , python默认支持的递归数量

    ```python
    print(sys.getrecursionlimit())
    ```

- `sys.stdout.write` --> print (进度)

    ```python
    import time
    for i in range(1,101):
        msg = "%s%%\r" %i
        print(msg,end='')
        time.sleep(0.05)
    ```

    ```python
    import os
    
    # 1. 读取文件大小（字节）
    file_size = os.stat('20190409_192149.mp4').st_size
    
    # 2.一点一点的读取文件
    read_size = 0
    with open('20190409_192149.mp4',mode='rb') as f1,open('a.mp4',mode='wb') as f2:
        while read_size < file_size:
            chunk = f1.read(1024) # 每次最多去读取1024字节
            f2.write(chunk)
            read_size += len(chunk)
            val = int(read_size / file_size * 100)
            print('%s%%\r' %val ,end='')
    ```

- `sys.argv`

    ```python
    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
    """
    让用户执行脚本传入要删除的文件路径，在内部帮助用将目录删除。
    C:\Python36\python36.exe D:/code/s21day14/7.模块传参.py D:/test
    C:\Python36\python36.exe D:/code/s21day14/7.模块传参.py
    
    """
    import sys
    
    # 获取用户执行脚本时，传入的参数。
    # C:\Python36\python36.exe D:/code/s21day14/7.模块传参.py D:/test
    # sys.argv = [D:/code/s21day14/7.模块传参.py, D:/test]
    path = sys.argv[1]
    
    # 删除目录
    import shutil
    shutil.rmtree(path)
    ```

- `sys.path`

### 7.5 操作系统相关（os）

和操作系统相关的数据。

- `os.path.exists(path)` ， 如果path存在，返回True；如果path不存在，返回False

- `os.stat('20190409_192149.mp4').st_size` ， 获取文件大小

- `os.path.abspath() `， 获取一个文件的绝对路径

    ```python
    path = '20190409_192149.mp4' # D:\code\s21day14\20190409_192149.mp4
    
    import os
    v1 = os.path.abspath(path)
    print(v1)
    ```

- `os.path.dirname `，获取路径的上级目录

    ```python
    import os
    v = r"D:\code\s21day14\20190409_192149.mp4"
    
    print(os.path.dirname(v))
    ```

- `os.path.join` ，路径的拼接

    ```python
    import os
    path = "D:\code\s21day14" # user/index/inx/fasd/
    v = 'n.txt'
    
    result = os.path.join(path,v)
    print(result)
    result = os.path.join(path,'n1','n2','n3')
    print(result)
    ```

- `os.listdir` ， 查看一个目录下所有的文件【第一层】

    ```python
    import os
    
    result = os.listdir(r'D:\code\s21day14')
    for path in result:
        print(path)
    ```

- `os.walk` ， 查看一个目录下所有的文件【所有层】

    ```python
    import os
    
    result = os.walk(r'D:\code\s21day14')
    for a,b,c in result:
        # a,正在查看的目录 b,此目录下的文件夹  c,此目录下的文件
        for item in c:
            path = os.path.join(a,item)
            print(path)
    ```

- 补充：

    - 两种转义方式，推荐第一种

        ```python
        v1 = r"D:\code\s21day14\n1.mp4"  (推荐)
        print(v1)
        
        
        v2 = "D:\\code\\s21day14\\n1.mp4"
        print(v2)
        ```

### 7.6 文件相关处理模块（shutil）

- `shutil.rmtree`，递归删除目录

```python
# 递归删除目录
import shutil
shutil.rmtree(path)
```

- `shutil.copyfileobj`，将文件内容拷贝到另一个文件中

```python
import shutil
shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))
```

- `shutil.copytree`，递归的去拷贝文件夹

```python
import shutil
 
shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
```

- `shutil.move`，递归的去移动文件，它类似`mv`命令，其实就是重命名。

```python
import shutil
 
shutil.move('folder1', 'folder3')
```

### 7.7 时间处理模块

- UTC/GMT：世界时间
- 本地时间：本地时区的时间

python中关于时间处理的模块有两个，分别是time和datetime

#### 7.7.1 time

```python
import time

# 获取当前时间戳（自1970-01-01 00：00）
v1 = time.time()
print(v1)  # 1623898825.3944983

# 获取当前时间戳
print(time.mktime(time.localtime()))  

# 时区
v2 = time.timezone
print(v2)

# 停止n秒，再执行后边的代码
time.sleep(3)
```

#### 7.7.2 datetime

开发中常用的三种时间格式：

```python
from datetime import datetime, timezone, timedelta

# 获取当前时间
v1 = datetime.now()
print(v1)  # 2021-06-17 11:12:32.589368

# 获取东七区的时间
tz = timezone(timedelta(hours=7))
v2 = datetime.now(tz)
print(v2)

# 当前UTC时间
v3 = datetime.utcnow()
print(v3)
```

```python
from datetime import datetime, timezone, timedelta

v1 = datetime.now()
print(v1)

# 时间的加减  datetime类型+timelta类型
v2 = v1 + timedelta(days=10, minutes=5)
print(v2)
```

```python
from datetime import datetime, timezone, timedelta

v1 = datetime.now()
print(v1)

# 获取UTC时间
v2 = datetime.utcnow()
print(v2)

# datetime之间相减，计算间隔时间不能相加  
# datetime类型 - datetime类型  datetime类型 比较 datetime类型
date = v1 - v2
print(date)
print(date.days, date.seconds / 60 / 60, date.microseconds)
```

- 字符串

```python
# 字符串格式的时间--->转换为datetime格式时间
from datetime import datetime
text = "2021-11-11"
v1 = datetime.strptime(text, '%Y-%m-%d')
print(v1)  # 2021-11-11 00:00:00
```

```python
# datetime格式--->转换为字符串格式
v1 = datetime.now()
v2 = v1.strftime("%Y-%m-%d %X")
print(v2)
print(type(v2))  # <class 'str'>
```

- 时间戳

```python
# 时间戳戈斯和--->转换为datetime格式
import time
form datetime import datetime
ctime = time.time()
print(ctime)  # 1623923966.2895925
v1 = datetime.fromtimestamp(ctime)
print(v1)  # 2021-06-17 17:59:26.289593
print(type(v1))  # <class 'datetime.datetime'>
```

```python
# datetime格式--->转换为时间戳格式
v1 = datetime.now()
v2 = v1.timestamp()
print(v2)  # 1623924093.286256
```

![image-20210104171741529](j:\homework\Python学习笔记\Python_notes.assets\image-20210104171741529.png)

时间相关的操作，时间有三种表示方式：

- 时间戳               1970年1月1日之后的秒，即：`time.time()`

- 格式化的字符串    2014-11-11，    即：`time.strftime('%Y-%m-%d')`

- 结构化时间          元组包含了：年、日、星期等... `time.struct_time`    即：`time.localtime()`

    ```python
    索引（Index）    属性（Attribute）    值（Values）
    0     tm_year（年）                 比如2011 
    1     tm_mon（月）             1 - 12
    2     tm_mday（日）                 1 - 31
    3     tm_hour（时）                 0 - 23
    4     tm_min（分）             0 - 59
    5     tm_sec（秒）             0 - 61
    6     tm_wday（weekday）            0 - 6（0表示周日）
    7     tm_yday（一年中的第几天）    1 - 366
    8     tm_isdst（是否是夏令时）            默认为-1
    ```

示例：

```python
import time


print(time.time())  # 获取当前时间戳
print(time.mktime(time.localtime()))  # 获取当前时间戳

print(time.gmtime())  # 是将一个时间戳转换为UTC时区（0时区）的struct_time。
print(time.localtime())  # 将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
print(time.strptime('2019-06-23 12:53:26', '%Y-%m-%d %H:%M:%S'))  # 把一个格式化时间字符串转化为struct_time

print(time.strftime('%Y-%m-%d'))  # 默认当前时间
print(time.strftime('%Y-%m-%d', time.localtime()))  # 默认当前时间
print(time.asctime())  # 年月日,星期,当前时间

import datetime

print(datetime.date(2019, 6, 27))  # 表示日期的类。常用的属性有year, month, day
print(datetime.time(12, 36, 52))  # 表示时间的类。常用的属性有hour, minute, second, microsecond
print(datetime.datetime(2019, 6, 23, 12, 37, 59, 45))  # 表示日期时间

dt = datetime.datetime(2019, 6, 23, 21, 28, 45, 100000)  # 表示时间间隔，即两个时间点之间的长度
tdelta = datetime.timedelta(days=12)
print(dt + tdelta)
```

### 7.8 数据格式转换模块

#### 7.8.1 json

json模块，是python内部的一个模块，可以将python的数据格式转换为json格式的数据，也可以将json格式的数据转换为python格式的数据。

json格式，是一种数据格式（本质上就是字符串，常用于网路数据传输）

> json格式的作用：
>
> 跨语言数据传输，例如：
>
> 1.用python开发的系统，有列表类型和字典等类型的数据
>
> 2.用java开发的系统，有数据和map等l欸行的数据
>
> 语言不同，基础数据类型格式都不同，为了方便数据传输，大家约定一个格式，json格式，每种语言都是将自身的数据类型转换为json格式，也可以将json格式转换为自身的数据类型。

- 把数据类型转换成`jsno`这个行为，一般称为序列化

- 编译器收到`json`转化成数据类型叫反序列化

- `json`格式要求：

    - `json`格式里面只能有`str`，`int`，`dict`，`list`，`bool`，`tuple`
    - `json`的外层必须是字典或列表
    - 在`json`中如包含字符串，必须是双引号

- `json.dumps`把python的数据类型转化为`json`格式，这个行为就叫序列化

- `json.loads()`把`json`格式转化成python的数据类型，这个行为就是反序列化

- `json.dump`，将数据序列化并写入文件

    ```python
    import json
    
    data = [
        {
            "id": 1,
            "name": "joker",
            "age": 18
        },
        {
            "id": 1,
            "name": "iker",
            "age": 18
        },
    ]
    
    file_object = open('xxx.json', mode='w', encoding='utf-8')
    
    json.dump(data, file_object)
    
    file_object.close()
    ```

- `json.load`，读取文件种的数据并反序列化为python的数据类型

    ```python
    import json
    file_object = open('xxx.json', mode='r', encoding='utf-8')
    
    data = json.load(file_object)
    print(data)
    
    file_object.close()
    ```

- 如果序列化以后`json`里面有中文，默认是`unicode`对照表，想中文显示，需要在`json.dumps()`加上参数`ensure_ascii`=False

    实例：python数据类型转化为json格式

    ```python
    import json
    
    data = [
        {
            "id": 1,
            "name": "joker",
            "age": 18
        },
        {
            "id": 1,
            "name": "iker",
            "age": 18
        },
    ]
    
    print(type(data))
    
    ret = json.dumps(data)
    print(ret)  # <class 'list'>
    print(type(ret))  # <class 'str'>
    
    
    ret = json.dumps(data, ensure_ascii=False)
    print(ret)  # '[{"id": 1, "name": "joker", "age": 18}, {"id": 1, "name": "iker", "age": 18}]
    ```

    实例：json格式数据类型转化为python格式

    ```python
    import json
    
    data_str = '[{"id": 1,"name": "joker","age": 18},{"id": 1,"name": "iker","age": 18}]'
    
    print(type(data_str))  # <class 'str'>
    data_list = json.loads(data_str)
    print(data_list)  # [{'id': 1, 'name': 'joker', 'age': 18}, {'id': 1, 'name': 'iker', 'age': 18}]
    print(type(data_list))  # <class 'list'>
    ```

- python的数据类型转换为json格式，对数据类型是有要求的，默认只支持：

    ```
        +-------------------+---------------+
        | Python            | JSON          |
        +===================+===============+
        | dict              | object        |
        +-------------------+---------------+
        | list, tuple       | array         |
        +-------------------+---------------+
        | str               | string        |
        +-------------------+---------------+
        | int, float        | number        |
        +-------------------+---------------+
        | True              | true          |
        +-------------------+---------------+
        | False             | false         |
        +-------------------+---------------+
        | None              | null          |
        +-------------------+---------------+
    ```

    其他类型如果想要支持，需要自定义`JSONEncoder`才能实现。

    实例：

    ```python
    import json
    from decimal import Decimal
    from datetime import datetime
    data = [
        {
            "id": 1,
            "name": "joker",
            "age": 18,
            "size": Decimal("18.99"),
            "ctime": datetime.now()
        },
        {
            "id": 1,
            "name": "iker",
            "age": 18,
            "size": Decimal("8.17"),
            "ctime": datetime.now()
        },
    ]
    
    class MyJSONEncode(json.JSONEncoder):
        def default(self, f):
            if type(f) == Decimal:
                return str(f)
            elif type(f) == datetime:
                return f.strftime("%Y-%m-%d")
            return supper().default(f)
    
    ret = json.dumps(data, cls=MyJSONEncode)
    print(ret)  # [{"id": 1, "name": "joker", "age": 18, "size": "18.99", "ctime": "2021-06-17"}, {"id": 1, "name": "iker", "age": 18, "size": "8.17", "ctime": "2021-06-17"}]
    ```

    

- `json`和`picke`：

    - `json`：所有语言通用，缺点只能转化基本数据类型
    - `pickle`：有点python所有东西都能数据化，缺点只能python反序列化

####  7.8.2 pickle

- `pickle.dumps`把python的数据类型转化为字节格式
- `pickle.loads()`把字节格式转化成python的数据类型
- 把`uincode`通过`utf-8`，`gbk`.........等压缩得到的被称为字节，一般前面带b的就是字节类型

### 7.9 持久化文件模块（shelve）

shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式.

序列化：

```python
import shelve

f = shelve.open('shelve_test')  # 打开一个文件

names = ["alex", "rain", "test"]
info = {'name': 'alex', 'age': 22}

f["names"] = names  # 持久化列表
f['info_dic'] = info

f.close()
```

反序列化：

```python
import shelve

d = shelve.open('shelve_test')  # 打开一个文件

print(d['names'])
print(d['info_dic'])


#del d['test'] #还可以删除
```

### 7.10 数据交换（xml）

`xml`是实现不同语言或程序之间进行数据交换的协议，跟`json`差不多，但`json`使用起来更简单，不过，以前，在`json`还没诞生的年代，大家只能选择用`xml`，至今很多传统公司如金融行业的很多系统的接口还主要是`xml`。

xml的格式如下，就是通过<>节点来区别数据结构的:

```xml
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
```

xml协议在各个语言里的都 是支持的，在python中可以用以下模块操作xml 　　

```python
import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
print(root.tag)

# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag,i.text)

# 只遍历year节点
for node in root.iter('year'):
    print(node.tag,node.text)
```

修改和删除`xml`文档内容

```python
import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated","yes")

tree.write("xmltest.xml")


# 删除node
for country in root.findall('country'):
   rank = int(country.find('rank').text)
   if rank > 50:
     root.remove(country)

tree.write('output.xml')
```

自己创建xml文档

```python
import xml.etree.ElementTree as ET


new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
sex.text = '33'
name2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
age = ET.SubElement(name2,"age")
age.text = '19'

et = ET.ElementTree(new_xml) #生成文档对象
et.write("test.xml", encoding="utf-8",xml_declaration=True)

ET.dump(new_xml) #打印生成的格式
```

### 7.11 修改配置文档（ConfigParser）

此模块用于生成和修改常见配置文档

settings：

~~~ini
[DEFAULT]
ServerAliveInterval = 45   
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no
~~~

解析配置文件：

~~~python
>>> import configparser # 导入模块
>>> config = configparser.ConfigParser()  #实例化(生成对象)
>>> config.sections()  #调用sections方法
[]
>>> config.read('example.ini')  # 读配置文件(注意文件路径)
['example.ini']
>>> config.sections() #调用sections方法(默认不会读取default)
['bitbucket.org', 'topsecret.server.com']
>>> 'bitbucket.org' in config #判断元素是否在sections列表内
True
>>> 'bytebong.com' in config
False
>>> config['bitbucket.org']['User'] # 通过字典的形式取值
'hg'
>>> config['DEFAULT']['Compression']
'yes'
>>> topsecret = config['topsecret.server.com']
>>> topsecret['ForwardX11']
'no'
>>> topsecret['Port']
'50022'
>>> for key in config['bitbucket.org']: print(key) # for循环 bitbucket.org 字典的key
...
user
compressionlevel
serveraliveinterval
compression
forwardx11
>>> config['bitbucket.org']['ForwardX11']
'yes'

~~~

其它增删改查语法：

~~~python

[group1] # 支持的两种分隔符“=”, “:”
k1 = v1
k2:v2

[group2]
k1 = v1

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('i.cfg')

# ########## 读 ##########
#secs = config.sections()
#print(secs)
#options = config.options('group2') # 获取指定section的keys
#print(options)

#item_list = config.items('group2') # 获取指定 section 的 keys & values ,key value 以元组的形式
#print(item_list)

#val = config.get('group1','key') # 获取指定的key 的value
#val = config.getint('group1','key')

# ########## 改写 ##########
#sec = config.remove_section('group1') # 删除section 并返回状态(true, false)
#config.write(open('i.cfg', "w")) # 对应的删除操作要写入文件才会生效

#sec = config.has_section('wupeiqi')
#sec = config.add_section('wupeiqi')
#config.write(open('i.cfg', "w")) # 


#config.set('group2','k1',11111)
#config.write(open('i.cfg', "w"))

#config.remove_option('group2','age')
#config.write(open('i.cfg', "w"))
```
~~~

### 7.12 进程执行命令（subprocess）

subprocess模块是python从2.4版本开始引入的模块。主要用来取代 一些旧的模块方法，如`os.system`、`os.spawn`、`os.popen`、`commands`等。subprocess通过子进程来执行外部指令，并通过input/output/error管道，获取子进程的执行的返回信息。

`subprocess.call()`：执行命令，并返回执行状态，其中shell参数为False时，命令需要通过列表的方式传入，当shell为True时，可直接传入命令

```python
>>> import subprocess
>>> a = subprocess.call(['df','-hT'],shell=False)
Filesystem                      Type  Size  Used Avail Use% Mounted on
C:                              ntfs  232G   50G  183G  22% /c
F:/cmder/vendor/git-for-windows ntfs  310G   12G  298G   4% /
D:                              ntfs  175G  108G   68G  62% /d
E:                              ntfs  175G   18G  158G  10% /e
j:                              ntfs   40G   93M   40G   1% /g
>>> a = subprocess.call('df -hT',shell=True)
Filesystem                      Type  Size  Used Avail Use% Mounted on
C:                              ntfs  232G   50G  183G  22% /c
F:/cmder/vendor/git-for-windows ntfs  310G   12G  298G   4% /
D:                              ntfs  175G  108G   68G  62% /d
E:                              ntfs  175G   18G  158G  10% /e
j:                              ntfs   40G   93M   40G   1% /g
>>> print(a)
0
```

`subprocess.check_call()`：用法与`subprocess.call()`类似，区别是，当返回值不为0时，直接抛出异常

```python
>>> a = subprocess.check_call('df -hT',shell=True)
Filesystem                      Type  Size  Used Avail Use% Mounted on
C:                              ntfs  232G   50G  183G  22% /c
F:/cmder/vendor/git-for-windows ntfs  310G   12G  298G   4% /
D:                              ntfs  175G  108G   68G  62% /d
E:                              ntfs  175G   18G  158G  10% /e
j:                              ntfs   40G   93M   40G   1% /g
>>> print(a)
0
>>> a = subprocess.check_call('dfdsf',shell=True)
'dfdsf' 不是内部或外部命令，也不是可运行的程序
或批处理文件。
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "F:\program\python36\lib\subprocess.py", line 311, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command 'dfdsf' returned non-zero exit status 1.
```

`subprocess.check_output()`：用法与上面两个方法类似，区别是，如果当返回值为0时，直接返回输出结果，如果返回值不为0，直接抛出异常。需要说明的是，该方法在`python3.x`中才有。

```python
>>> f = subprocess.check_output('df -hT',shell=True)
>>> print(f)
b'Filesystem                      Type  Size  Used Avail Use% Mounted on\nC:                              ntfs  232G   50G  183G  22% /c\nF:/cmder/vendor/git-for-windows ntfs  310G   12G  298G   4% /\nD:
           ntfs  175G  108G   68G  62% /d\nE:                              ntfs  175G   18G  158G  10% /e\nG:
                            ntfs   40G   93M   40G   1% /g\n'
>>> f = subprocess.check_output('asdadadw',shell=True)
'asdadadw' 不是内部或外部命令，也不是可运行的程序
或批处理文件。
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "F:\program\python36\lib\subprocess.py", line 356, in check_output
    **kwargs).stdout
  File "F:\program\python36\lib\subprocess.py", line 438, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command 'asdadadw' returned non-zero exit status 1.
```

`subprocess.Popen()`：

常用参数：

- `args：shell`命令，可以是字符串或者序列类型（如：list，元组）
- `bufsize`：缓冲区大小，可不用关心
- stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
- preexec_fn：只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
- shell：同上
- cwd：用于设置子进程的当前目录
- env：用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。

下面这2条语句执行会有什么区别？

```python
a=subprocess.run('sleep 10',shell=True,stdout=subprocess.PIPE)
a=subprocess.Popen('sleep 10',shell=True,stdout=subprocess.PIPE)
```

区别是Popen会在发起命令后立刻返回，而不等命令执行结果。这样的好处是什么呢？

如果你调用的命令或脚本 需要执行10分钟，你的主程序不需卡在这里等10分钟，可以继续往下走，干别的事情，每过一会，通过一个什么方法来检测一下命令是否执行完成就好了。

Popen调用后会返回一个对象，可以通过这个对象拿到命令执行结果或状态等，该对象有以下方法

```python
poll()
```

Check if child process has terminated. Returns returncode

```python
wait()
```

Wait for child process to terminate. Returns returncode attribute.

`terminate()`终止所启动的进程Terminate the process with SIGTERM

`kill()` 杀死所启动的进程 Kill the process with SIGKILL

`communicate()`与启动的进程交互，发送数据到stdin,并从stdout接收输出，然后等待任务结束

```python
>>> a = subprocess.Popen('python3 guess_age.py',stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)

>>> a.communicate(b'22')

(b'your guess:try bigger\n', b'')
```

`send_signal(signal.xxx)`发送系统信号

`pid` 拿到所启动进程的进程号

### 7.13 日志模块（logging）

很多程序都有记录日志的需求，并且日志中包含的信息即有正常的程序访问日志，还可能有错误、警告等信息输出，python的logging模块提供了标准的日志接口，你可以通过它存储各种格式的日志，logging的日志可以分为 `debug(), info(), warning(), error() and critical()`5个级别，下面我们看一下怎么用。

最简单用法：

```python
import logging

logging.warning("user [alex] attempted wrong password more than 3 times")
logging.critical("server is down")
```

输出：

```python
WARNING:root:user [alex] attempted wrong password more than 3 times
CRITICAL:root:server is down
```

看一下这几个日志级别分别代表什么意思：

| Level      | When it’s used                                               |
| :--------- | :----------------------------------------------------------- |
| `DEBUG`    | Detailed information, typically of interest only when diagnosing problems. |
| `INFO`     | Confirmation that things are working as expected.            |
| `WARNING`  | An indication that something unexpected happened, or indicative of some problem in the near future (eg. ‘disk space low’). The software is still working as expected. |
| `ERROR`    | Due to a more serious problem, the software has not been able to perform some function. |
| `CRITICAL` | A serious error, indicating that the program itself may be unable to continue running. |

如果想把日志写到文件里，也很简单

```python
import logging

logging.basicConfig(filename='example.log',level=logging.INFO)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```

其中下面这句中的level=loggin.INFO意思是，把日志纪录级别设置为INFO，也就是说，只有比日志是INFO或比INFO级别更高的日志才会被纪录到文件里，在这个例子， 第一条日志是不会被纪录的，如果希望纪录debug的日志，那把日志级别改成DEBUG就行了。

```python
logging.basicConfig(filename='example.log',level=logging.INFO)
```

自定义日志格式：

感觉上面的日志格式忘记加上时间啦，日志不知道时间怎么行呢，下面就来加上!

```python
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')

# 输出
12/12/2010 11:46:36 AM is when this event was logged.
```

除了加时间，还可以自定义一大堆格式，下表就是所有支持的格式：

| %(name)s            | Logger的名字                                                 |
| :------------------ | :----------------------------------------------------------- |
| %(levelno)s         | 数字形式的日志级别                                           |
| %(levelname)s       | 文本形式的日志级别                                           |
| %(pathname)s        | 调用日志输出函数的模块的完整路径名，可能没有                 |
| %(filename)s        | 调用日志输出函数的模块的文件名                               |
| %(module)s          | 调用日志输出函数的模块名                                     |
| %(funcName)s        | 调用日志输出函数的函数名                                     |
| %(lineno)d          | 调用日志输出函数的语句所在的代码行                           |
| %(created)f         | 当前时间，用UNIX标准的表示时间的浮 点数表示                  |
| %(relativeCreated)d | 输出日志信息时的，自Logger创建以 来的毫秒数                  |
| %(asctime)s         | 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒 |
| %(thread)d          | 线程ID。可能没有                                             |
| %(threadName)s      | 线程名。可能没有                                             |
| %(process)d         | 进程ID。可能没有                                             |
| %(message)s         | 用户输出的消息                                               |

日志同时输出到屏幕和文件：

如果想同时把log打印在屏幕和文件日志里，就需要了解一点复杂的知识 了

Python 使用logging模块记录日志涉及四个主要类，使用官方文档中的概括最为合适：

- **logger提供了应用程序可以直接使用的接口；**
- **handler将(logger创建的)日志记录发送到合适的目的输出；**
- **filter提供了细度设备来决定输出哪条日志记录；**
- **formatter决定日志记录的最终输出格式。**

每个组件的主要功能：

**logger**：

每个程序在输出信息之前都要获得一个Logger。Logger通常对应了程序的模块名，比如聊天工具的图形界面模块可以这样获得它的Logger：

```python
LOG=logging.getLogger(”chat.gui”)
```

而核心模块可以这样：

```python
LOG=logging.getLogger(”chat.kernel”)
```

还可以绑定handler和filters

```python
Logger.setLevel(lel) # 指定最低的日志级别，低于lel的级别将被忽略。debug是最低的内置级别，critical为最高
Logger.addFilter(filt)、Logger.removeFilter(filt) # 添加或删除指定的filter
Logger.addHandler(hdlr)、Logger.removeHandler(hdlr) # 增加或删除指定的handler
```

Logger.debug()、Logger.info()、Logger.warning()、Logger.error()、Logger.critical()：可以设置的日志级别

**handler**：

handler对象负责发送相关的信息到指定目的地。Python的日志系统有多种Handler可以使用。有些Handler可以把信息输出到控制台，有些Handler可以把信息输出到文件，还有些 Handler可以把信息发送到网络上。如果觉得不够用，还可以编写自己的Handler。可以通过addHandler()方法添加多个多handler

```python
Handler.setLevel(lel) # 指定被处理的信息级别，低于lel级别的信息将被忽略
Handler.setFormatter() # 给这个handler选择一个格式
Handler.addFilter(filt)、Handler.removeFilter(filt) # 新增或删除一个filter对象
```

每个Logger可以附加多个Handler。接下来我们就来介绍一些常用的Handler：

1. **logging.StreamHandler** 使用这个Handler可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息。

2. **logging.FileHandler** 和StreamHandler 类似，用于向一个文件输出日志信息。不过FileHandler会帮你打开这个文件

3. **logging.handlers.RotatingFileHandler**

    这个Handler类似于上面的FileHandler，但是它可以管理文件大小。当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建 一个新的同名日志文件继续输出。比如日志文件是chat.log。当chat.log达到指定的大小之后，RotatingFileHandler自动把 文件改名为chat.log.1。不过，如果chat.log.1已经存在，会先把chat.log.1重命名为chat.log.2。。。最后重新创建 chat.log，继续输出日志信息。它的函数是：

    ```python
     RotatingFileHandler( filename[, mode[, maxBytes[, backupCount]]])
    ```

    其中filename和mode两个参数和FileHandler一样。

    - maxBytes用于指定日志文件的最大文件大小。如果maxBytes为0，意味着日志文件可以无限大，这时上面描述的重命名过程就不会发生。
    - backupCount用于指定保留的备份文件的个数。比如，如果指定为2，当上面描述的重命名过程发生时，原有的chat.log.2并不会被更名，而是被删除。

4. **logging.handlers.TimedRotatingFileHandler**

    这个Handler和RotatingFileHandler类似，不过，它没有通过判断文件大小来决定何时重新创建日志文件，而是间隔一定时间就 自动创建新的日志文件。重命名的过程与RotatingFileHandler类似，不过新的文件不是附加数字，而是当前时间。它的函数是：

    ```python
    TimedRotatingFileHandler( filename [,when [,interval [,backupCount]]])
    ```

    其中filename参数和backupCount参数和RotatingFileHandler具有相同的意义。

    `interval`是时间间隔。

    `when`参数是一个字符串。表示时间间隔的单位，不区分大小写。它有以下取值：

    - S 秒
    - M 分
    - H 小时
    - D 天
    - W 每星期（interval==0时代表星期一）
    - midnight 每天凌晨

**formatter 组件**：

日志的formatter是个独立的组件，可以跟handler组合

```python
fh = logging.FileHandler("access.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter) #把formmater绑定到fh上
```

**filter 组件**：

如果你想对日志内容进行过滤，就可自定义一个filter：

```python
class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        return   "db backup" not in record.getMessage()
```

> 注意：filter函数会返加True or False，logger根据此值决定是否输出此日志

然后把这个filter添加到logger中：

```python
logger.addFilter(IgnoreBackupLogFilter())
```

下面的日志就会把符合filter条件的过滤掉：

```python
logger.debug("test ....")
logger.info("test info ....")
logger.warning("start to run db backup job ....")
logger.error("test error ....")
```

一个同时输出到屏幕、文件、带filter的完成例子：

```python
import logging


class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        return   "db backup" not in record.getMessage()

#console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
#file handler
fh = logging.FileHandler('mysql.log')
#fh.setLevel(logging.WARNING)

#formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#bind formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger = logging.getLogger("Mysql")
logger.setLevel(logging.DEBUG) #logger 优先级高于其它输出途径的

#add handler   to logger instance
logger.addHandler(ch)
logger.addHandler(fh)


#add filter
logger.addFilter(IgnoreBackupLogFilter())

logger.debug("test ....")
logger.info("test info ....")
logger.warning("start to run db backup job ....")
logger.error("test error ....")
```

文件自动截断例子：

```python
import logging

from logging import handlers

logger = logging.getLogger(__name__)

log_file = "timelog.log"
#fh = handlers.RotatingFileHandler(filename=log_file,maxBytes=10,backupCount=3)
fh = handlers.TimedRotatingFileHandler(filename=log_file,when="S",interval=5,backupCount=3)

formatter = logging.Formatter('%(asctime)s %(module)s:%(lineno)d %(message)s')

fh.setFormatter(formatter)

logger.addHandler(fh)


logger.warning("test1")
logger.warning("test12")
logger.warning("test13")
logger.warning("test14")
```

### 7.14 正则匹配模块（re）

正则表达式就是字符串的匹配规则，在多数编程语言里都有相应的支持，python里对应的模块是re

**常用的表达式规则：**

```python
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾， 若指定flags MULTILINE ,re.search('foo.$','foo1\nfoo2\n',re.MULTILINE).group() 会匹配到foo1
'*'     匹配*号前的字符0次或多次， re.search('a*','aaaabac')  结果'aaaa'
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次 ,re.search('b?','alex').group() 匹配b 0次
'{m}'   匹配前一个字符m次 ,re.search('b{3}','alexbbbs').group()  匹配到'bbb'
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配， re.search("(abc){2}a(123|45)", "abcabca456c").group() 结果为'abcabca45'


'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的，相当于re.match('abc',"alexabc") 或^
'\Z'    匹配字符结尾，同$ 
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'

'(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}
```

#### 7.14.1 正则表达式

**1.字符相关**

- 匹配文中的joker

```python
import re
text = "我的名字叫joker，我喜欢北京，记住我的名字joker"
data_list = re.findall("joker", text)
print(data_list)  # ['joker', 'joker']
```

- 匹配o或e或r

```python
import re
text = "我的名字叫joker，我喜欢北京，记住我的名字joker"
data_list = re.findall("[oer]", text)
print(data_list)  # ['o', 'e', 'r', 'o', 'e', 'r']
```

```python
# 匹配jo
import re
text = "我的名字叫joker，我喜欢北京，记住我的名字joker"

data_list = re.findall("j[oer]", text)
print(data_list)  # ['jo', 'jo']
```

- 匹配除了oer以外的其他字符

```python
import re
text = "我的名字叫joker，我喜欢北京，记住我的名字joker"
data_list = re.findall("[^oer]", text)
print(data_list)  # ['我', '的', '名', '字', '叫', 'j', 'k', '，', '我', '喜', '欢', '北', '京', '，', '记', '住', '我', '的', '名', '字', 'j', 'k']
```

- 匹配a~z的任意字符

```python
import re
text = "asd是的flm的nv"
data_list = re.findall("[a-z]", text)
print(data_list)  # ['a', 's', 'd', 'f', 'l', 'm', 'n', 'v']
```

- 匹配除换行以外的任意字符

```python
import re
text = "It is very important to take care of our environmen"
data_list = re.findall(".t", text)
print(data_list)  # ['It', 'rt', 'nt', ' t', ' t']
```

```python
# 匹配r什么a
import re
text = "It is very important to take care of our environmen"
data_list = re.findall("r.a", text)
print(data_list)  # ['rta']
```

```python
# 贪婪匹配
import re
text = "It is very important to take care of our environmen"
data_list = re.findall("v.+r", text)
print(data_list)  # ['very important to take care of our envir']
```

```python
# 非贪婪匹配
import re
text = "It is very important to take care of our environmen"
data_list = re.findall("v.?r", text)
print(data_list)  # ['ver', 'vir']
```

- 匹配字母数字下划线汉字

```python
import re
text = "城市city1_北京beijing  城市city天津"
data_list = re.findall("y\w+e", text)
print(data_list)  # ['y1_北京be']
```

- 匹配数字

```python
import re
text = "root-123admin-456administortra-789"
data_list = re.findall("-\d", text)
print(data_list)  # ['-1', '-4', '-7']
```

```python
import re
text = "root-123admin-456administortra-789"
data_list = re.findall("-\d+", text)
print(data_list)  # ['-123', '-456', '-789']
```

- 匹配任意的空白符，包括空格、制表符等

```python
import re
text = "It is very important to take care of our environmen"
data_list = re.findall("t\w+\s\w", text)
print(data_list)  # ['tant t', 'take c']
```

**2.数量相关**

- 重复0次或更多次

```python
import re
text = "这是a大,这是1a大"
data_list = re.findall("是1*a", text)
print(data_list)  # ['是a', '是1a']
```

- 重复1次或更多次

```python
import re
text = "这是a大，这是1a大，这是123456a"
data_list = re.findall("是\d+a", text)
print(data_list)  # ['是1a', '是123456a']
```

- 重复0次或1次

```python
import re
text = "这是a大，这是1a大，这是123456a"
data_list = re.findall("是\d?a", text)
print(data_list)  # ['是a', '是1a']
```

- 重复n次

```python
import re
text = "这是a大，这是1a大，这是123456baa1a"
data_list = re.findall("a{2}", text)
print(data_list)  # ['aa']
```

```python
import re
text = "这是a大，这是1a大，这是123456baa1a"
data_list = re.findall("\d{6}", text)
print(data_list)
```

- 重复n次或更多次

```python
import re
text = "这是a大，这是1a大，这是123456baa1a"
data_list = re.findall("\d{6,9}", text)
print(data_list)
```

**3.括号（分组）**

- 提取数据区域

```python
import re
text = "神舟十二号，简称“神十二”，为中国载人航天工程发射的第十二艘飞船20210617062227，是空间站关键技术验证阶段第四次飞行任务"
data_list = re.findall("2021(0\d{7})", text)
print(data_list)  # ['06170622']
```

```python
import re
text = "神舟十二号，简称“神十二”，为中国载人航天工程发射的第十二艘飞船20210617062227，是空间站关键技术验证阶段第四次飞行任务"
data_list = re.findall("2021(06)17(0\d+)", text)
print(data_list)  # [('06', '062227')]
```

```python
import re
text = "神舟十二号，简称“神十二”，为中国载人航天工程发射的第十二艘飞船20210617062227，是空间站关键技术验证阶段第四次飞行任务"
data_list = re.findall("(2021(06)17)(0\d+)", text)
print(data_list)  # [('20210617', '06', '062227')]
```

- 获取指定区域 + 条件

```python
text = "神舟十二号，2021简称太“神十二”，为中国载人航天工程发射的第十二艘飞船20210617062227，是空间站关键技术验证阶段第四次飞行任务"
data_list = re.findall("2021(06\d{2}|简\w+太)", text)
print(data_list)  # ['简称太', '0617']
```

```python
import re
text = "神舟十二号，2021简称太“神十二”，为中国载人航天工程发射的第十二艘飞船20210617062227，是空间站关键技术验证阶段第四次飞行任务"
data_list = re.findall("(2021(06\d{2}|简\w+太))", text)
print(data_list)  # [('2021简称太', '简称太'), ('20210617', '0617')]
```

**4.起始和结束**

上述示例中都是去一段文本中提取数据，只要文本中存在即可。

但真实开发中很多场景需要实现指定的内容开头和结尾，这样就需要用到如下两个字符。

- ^ 开始
- $ 结束

```python
import re
text = "如有什么问题请练习43815687@qq.com帮你解决"
data_list = re.findall("^\w+@\w+.\w+$", text, re.ASCII)
print(data_list)  # []
```

```python
import re
text = "43815687@qq.com"
data_list = re.findall("^\w+@\w+.\w+$", text, re.ASCII)
print(data_list)  # ['43815687@qq.com']
```

这种一般用于对用户输入数据格式的校验，示例：

```python
import re
text = input("请输入邮箱：")
email = re.findall("^\w+@\w+.\w+$", text, re.ASCII)
if not email:
    print("邮箱格式错误")
else:
    print(email)
```

**5.特殊字符**
由于正则表达式中`*.{}()`等都具有特殊的含义，所以如果想要再正则中匹配这种指定的字符，需要转义，例如：

```python
import re

text = "我是你{}的什么"
data_list = re.findall("你{5}", text)
print(data_list)
```

```python
import re
text = "我是你{5}的什么"
data_list = re.findall("你\{5\}的", text)
print(data_list)
```

#### 7.14.2 re模块

python中提供了re模块，可以处理正则表达式并对文本进行处理。

**re的匹配语法有以下几种:**

> `re.match`从头开始匹配
>
> `re.search` 匹配包含
>
> `re.findall` 把所有匹配到的字符放到以列表中的元素返回
>
> `re.split` 以匹配到的字符当做列表分隔符
>
> `re.sub` 匹配字符并替换
>
> `re.fullmatch` 全部匹配

参数：

1. pattern 正则表达式

2. string 要匹配的字符串

3. flags 标志位，用于控制正则表达式的匹配方式

示例：

- findall，获取匹配到的所有数据

```python
import re
text = "dsf130429191912015219k13042919591219521Xkk"
data_list = re.findall("(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)", text)
print(data_list)  # [('130429', '1919', '12', '01', '521', '9'), ('130429', '1959', '12', '19', '521', 'X')]
```

- match(pattern, string, flags=0)，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None

```python
import re
text = "qabc130429191912015219k13042919591219521Xkk"
ret = re.match("abc\d", text)
print(ret)  # None  未匹配成功
```

```python
text = "abc130429191912015219k13042919591219521Xkk"
ret = re.match("abc\d", text)
if not ret:
    print("匹配不成功")
else:
    content = ret.group()
    print(content)
```

- serach，浏览挣个字符串去匹配第一个，未匹配成功返回None

```python
import re
text = "qabc130429191912015219k13042919591219521Xkk"
ret = re.search("abc\d", text)
if ret:
    content = ret.group()
    print(content)  # abc1
```

match and search均用于匹配单值，即：只能匹配字符串中的一个，如果想要匹配到字符串中所有符合条件的元素，则需要使用 findall。

- sub，替换匹配成功的位置

```python
import re
text = "qabc130429191912015219Xk13042919591219521Xkk"
content = re.sub("\dX", "替换", text)
print(content)  # qabc13042919191201521替换k1304291959121952替换kk
```

```python
import re
text = "qabc130429191912015219Xk13042919591219521Xkk"
content = re.sub("\dX", "替换", text, 1)
print(content)  # qabc13042919191201521替换k13042919591219521Xkk
```

- split，根据匹配成的位置分割

```python
import re
text = "qabc130429191912015219Xk13042919591219521Xkk"
content = re.split("\dX", text)
print(content)  # ['qabc13042919191201521', 'k1304291959121952', 'kk']
```

```python
import re
text = "qabc130429191912015219Xk13042919591219521Xkk"
content = re.split("\dX", text, 1)
print(content)  # ['qabc13042919191201521', 'k13042919591219521Xkk']
```

- finditer

```python
import re
text = "qabc130429191912015219Xk13042919591219521Xkk"
content = re.finditer("\dX", text)
for item in content:
    print(item.group())  # 9X 1X
```

```python
import re
text = "qabc130429191912015219Xk13042919591219521Xkk"
content = re.finditer("(?P<xx>\dX)", text)
for item in content:
    print(item.groupdict())  # {'xx': '9X'} {'xx': '1X'}
```

```python
import re
text = "qabc130429191912015219Xk13042919591219521Xkk"
content = re.finditer("\d{6}(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})\d{3}[\d|X]", text)
for item in content:
    info_dict = item.groupdict()
    print(info_dict)  # {'year': '1919', 'month': '12', 'day': '01'}  {'year': '1959', 'month': '12', 'day': '19'}
```

- fullmatch，整个字符串匹配成功就返回object, 否则返回None

```python
import re
text = "joker4381@qq.net"
content = re.fullmatch("(\w+@\w+\.(com|net|cn))", text)
if content:
    val = content.groups()
    print(val)  # ('joker4381@qq.net', 'net')
```

**Flags标志符**：

- re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
- M(MULTILINE): 多行模式，改变'^'和'$'的行为
- S(DOTALL): 改变'.'的行为,make the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline.
- X(re.VERBOSE) 可以给你的表达式写注释，使其更可读，下面这2个意思一样

```python
a = re.compile(r"""\d + # the integral part
                \. # the decimal point
                \d * # some fractional digits""", 
                re.X)

b = re.compile(r"\d+\.\d*")
```

#### 7.14.3 项目开发规范

- 基于python开发简单应用时，一个py文件就是实现功能，需要注意以下几点

```python
"""					
文件注释
"""									# 1.脚本功能注释

import re
import random

import requests
from openpyxl import load_workbook	# 2.导入模块顺序（内置、第三方、自定义）

DB = "XXX"							# 3.全局变量大写


def do_something():					# 4.函数名命名规范，函数功能注释
    """ 函数注释 """

    # TODO 待完成时，下一期实现xxx功能	# 5.TODO信息注释
    for i in range(10):
        pass


def run():
    """ 函数注释 """

    # 对功能代码进行注释					# 6.部分代码注释
    text = input(">>>")
    print(text)


if __name__ == '__main__':			  # 7.主文件调试代码
    run()
```

- 单可执行文件

参照以下目录架构来存放代码及数据

```powershell
crm
├── app.py        文件，程序的主文件（尽量精简）
├── config.py     文件，配置文件（放相关配置信息，代码中读取配置信息，如果想要修改配置，即可以在此修改，不用再去代码中逐一修改了）
├── db            文件夹，存放数据
├── files         文件夹，存放文件
├── src           包，业务处理的代码
└── utils         包，公共功能
```

- 多可执行文件

```powershell
killer
├── bin					文件夹，存放多个主文件（可运行）
│   ├── app1.py
│   └── app2.py
├── config              包，配置文件
│   ├── __init__.py
│   └── settings.py
├── db                  文件夹，存放数据
├── files               文件夹，存放文件
├── src                 包，业务代码
│   └── __init__.py
└── utils               包，公共功能
    └── __init__.py
```

---

## 第八章 面向对象

### 8.1 面向对象程序设计

编程范式

一个程序是程序员为了得到一个任务结果而编写的一组指令的集合，正所谓条条大路通罗马，实现一个任务的方式有很多种不同的方式， 对这些不同的编程方式的特点进行归纳总结得出来的编程方式类别，即为编程范式。

不同的编程范式本质上代表对各种类型的任务采取的不同的解决问题的思路， 大多数语言只支持一种编程范式，当然也有些语言可以同时支持多种编程范式。

两种最重要的编程范式分别是**面向过程**编程和**面向对象**编程。

#### 8.1.1 面向过程编程(Procedural Programming)

面向过程又被称为top-down languages， 就是程序从上到下一步步执行，一步步从上到下，从头到尾的解决问题 。核心是过程二字，过程指的是解决问题的步骤，设计一条流水线,机械式的思维方式。

优点：复杂的问题流程化,进而简单化

缺点：可扩展性差

应用场景：面向过程的程序设计思想一般用于那些功能一旦实现之后就很少需要改变的场景

示例：

```python
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

#### 8.1.2 面向对象编程(Object Oriented Programing)

面向对象(Object Oriented Programing）编程是利用“类”和“对象”来创建各种模型来实现对真实世界的描述，核心就是对象二字，对象就是特征与技能的结合体。

应用场景：用户需求经常变化，互联网应用，游戏，企业内部应用

```python
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "ike"
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

#### 8.1.3 什么是对象

对象是从类中产生的，只要是类名加上（），这就是一个实例化过程，这个就会实例化一个对象。

- 什么是面向对象？

  **面向过程：**将需要解决的问题按步骤划分，一步一步完成每一个步骤，而且     步骤之间有联系。

  优点：复杂问题可以分步完成

  缺点：扩展性很差，维护性差。如果中间某一环节有问题整体都会发生问题

  使用的场景：对扩展性要求较低的软件，比如系统软件，脚本程序

  **面向对象（oop）：**将程序看作一堆对象的集合，实现功能的方式就是通过对象之间的交互来实现。

  优点：扩展性高。对象之间的影响几乎没有

  缺点：当某些程序不需要扩展性时书写就很复杂，无法预知结果

- 什么是对象？

  对象就是具备某些特征与技能的结合体

- 什么是类？

  类即类别、种类，是面向对象设计最重要的概念，对象是特征与技能的结合体，而类则是一系列对象相似的特征与技能的结合体

- 类与对象之间的关系

  类的作用是标识对象与对象之间的差异

  对象是某个类的实例。对象是实际的，类是抽象的

- 先有类还是先有对象？

  在现实世界中：先有对象，再总结出类

  在编程中：先有类，才能创建符合类特征的对象

总结：面对对象的思想就是用类和对象来解决问题

面对对象编程的本质：通过使用不同的对象来完成程序

#### 8.1.4 名词解释

**类：**一个类即是对一类拥有相同属性的对象的抽象、蓝图、原型、模板。在类中定义了这些对象的都具备的属性（variables(data)）、共同的方法

**属性：**人类包含很多特征，把这些特征用程序来描述的话，叫做属性，比如年龄、身高、性别、姓名等都叫做属性，一个类中，可以有多个属性

**方法：**人类不止有身高、年龄、性别这些属性，还能做好多事情，比如说话、走路、吃饭等，相比较于属性是名词，说话、走路是动词，这些动词用程序来描述就叫做方法。

**实例(对象)：**一个对象即是一个类的实例化后实例，一个类必须经过实例化后方可在程序中调用，一个类可以实例化多个对象，每个对象亦可以有不同的属性，就像人类是指所有人，每个人是指具体的对象，人与人之前有共性，亦有不同

**实例化：**把一个类转变为一个对象的过程就叫实例化

#### 8.1.5 如何使用类

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

# 注意：
  1.类中可以有任意python代码，这些代码在类定义阶段便会执行
  2.因而会产生新的名称空间，用来存放类的变量名与函数名，可以通过ThisIsPerson.__dict__查看
  3.对于经典类来说我们可以通过该字典操作类名称空间的名字（新式类有限制），但python为我们提供专门的.语法
  4.点是访问属性的语法，类中定义的名字，都是类的属性
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
stu1.Name = '李二丫'
print(stu1.__dict__)
print(stu1.Name)

# 删
del stu1.Name
print(stu1.__dict__)

# 增
stu1.class_name = 'python'
print(stu1.__dict__)
```

### 8.2 类与对象

类即类别、种类，是面向对象设计最重要的概念，上边我们说过对象是特征与技能的结合体，而类则是一系列对象相似的特征与技能的结合体。

疑问：先有的一个个具体存在的对象，还是先有的人类这个概念？

这个问题需要分两种情况去看：

- 在现实世界中：肯定是先有对象，再有类

    ```powershell
    在地球上肯定是先出现各种物体，然后随着物体的进化然后产生种类：比如：人类，动物类，植物类等。也就说，对象是具体的存在，而类仅仅只是一个概念，并不真实存在，比如动物类，具体指的是哪种动物。
    ```

- 在程序中：务必保证先定义类，后产生对象

    ```powershell
    这与函数的使用是类似的：
    先定义函数，后调用函数；类也是一样的，程序中需要先定义类，后调用类。
    不一样的是：
    调用函数会执行函数体代码返回的是函数体执行的结果，调用类会产生对象，返回的是对象。
    ```

示例：

现实生活中：先有对象，再有类

```
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
        self.Name = name
        self.Sex = sex
        self.Age = age

    def learn(self):
        print('%s is learning %s' % (self.Name, self.Age))

    def eat(self):
        print('%s is eating' % self.Name)

    def sleep(self):
        print('%s is sleeping' % self.Name)


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

类中的数据属性：所有对象直接共有的

```python
print(LuffyStudent.shool, id(LuffyStudent.shool))	# 4561031280
print(stu1.shool, id(stu1.shool))	# 4561031280
print(stu2.shool, id(stu2.shool))	# 4561031280
print(stu3.shool, id(stu3.shool))	# 4561031280
```

类中的函数属性：绑定给对象使用的，绑定到不同的对象是不同的绑定方法，对象调用绑定方法时，会把对象本身当做第一个参数传入，传给self

```python
print(LuffyStudent.learn)  # 普通函数
print(stu1.learn)  # 绑定方法
print(stu2.learn)  # 绑定方法
print(stu3.learn)  # 绑定方法
```

总结：

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

### 8.3 继承

概念：继承指的是类与类之间的关系，是一种什么“是”什么的关系，继承的功能之一就是用来解决代码重用问题，继承是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类，**父类又可以成为基类或超类**，**新建的类称为派生类或子类**。

示例：单继承与多继承

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

提示：用已经有的类建立一个新的类，这样就重用了已经有的软件中的一部分设置大部分，大大节省了编程工作量，这就是常说的软件重用，不仅可以重用自己的类，也可以继承别人的，比如标准库，来定制新的数据类型，这样就是大大缩短了软件开发周期，对大型软件开发来说，意义重大。

### 8.4 属性查找

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

### 8.5 派生

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

注意：在子类中，需要重用父类中得函数功能，要用函数调用的普通方式，即：类名.func()，此时就与调用普通函数无异了，因此即便是self参数也要为其传值。

### 8.6 继承的原理

示例：

在 python2中-->经典类：没有继承object的类，以及他的子类，都称之为经典类

```python
class Foo:
    pass


class Bar(Foo):
    pass
```

在 python2中-->新式类：继承object的类，以及他的子类，都称之为新式类

```python
class Foo(object):
    pass


class Bar(Foo):
    pass
```

在python3中-->新式类：一个类没有继承object的类，默认都继承object类

```python
class Foo:
    pass


# print(Foo.__bases__)

```

python到底是如何实现继承的，对于你定义的每一个类，python会计算出一个方法解析顺序(MRO)列表，这个MRO列表就是一个简单的所有基类的线性顺序列表。

为了实现继承，python会在MRO列表上从左到右开始查找基类，直到找到第一个匹配这个属性的类为止。而这个MRO列表的构造是通过一个C3线性化算法来实现的。

- 子类会先于父类被检查
- 多个父类会根据它们在列表中的顺序被检查
- 如果对下一个类存在两个合法的选择，选择第一个父类

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

### 8.7 在子类中调用父类的方法

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

A没有继承B，但是A内super会基于C.mro()继续往后找。

### 8.8 组合与重用性

软件重用的重要方式除了继承之外还有另外一种方式，即：组合

组合指的是，在一个类中以另外一个类的对象作为数据属性，称为**类的组合**

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
    - 用组合的方式建立了类与组合的类之间的关系，它是一种‘有’的关系，比如学生有生日，老师也有生日

### 8.9 抽象类

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

总结：其实就是父类对子类进行约束，子类必须要写基类的方法， 在python中约束的。

### 8.10 多态与多态性

<font color="red"> **让具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容(功能)的函数**</font>

- 多态：指的是同一类事物的多种形态

    - 1.只关心对象的实例方法是否同名，不关心对象所属的类型；
    - 2.对象所属的类之间，继承关系可有可无；
    - 3.多态的好处可以增加代码的外部调用灵活度，让代码更加通用，兼容性比较强；
    - 4.多态是调用方法的技巧，不会影响到类的内部设计；

- 多态性：指的是可以在不考虑对象的类型的情况下而直接使用对象，多态性分为静态多态性和动态多态性

    - 静态多态性：如任何类型都可以用运算符进行运算

    - 动态多态性：如下

        调用同一个函数`func()`, 传入不同的参数（对象），可以调用不同的功能 
        
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
        
        
        # 多态性:指的是可以在不考虑对象的类型的情况下而直接使用对象
        peo = People()
        dog = Dog()
        pig = Pig()
        
        # peo.eat()
        # dog.eat()
        # pig.eat()
        
        
        # 更进一步,我们可以定义一个统一的接口来使用
        def func(obj):
            obj.eat()
        
        
        func(peo)
        func(dog)
        func(pig)
        ```

多态性的优点：

- 增加了程序的灵活性
    - 以不变应万变，不论对象千变万化，使用者都是同一种形式去调用，如`func(animal)`
- 增加了程序的可扩展性
    - 通过继承animal类创建了一个新的类，使用者无需更改自己的代码，还是用`func(animal)`去调用

### 8.11 鸭子类型

调用不同的子类将会产生不同的行为，而无须明确知道这个子类实际上是什么，这是多态的重要应用场景。而在python中，因为鸭子类型(duck typing)使得其多态不是那么酷。
鸭子类型是动态类型的一种风格。在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定。这个概念的名字来源于由James Whitcomb Riley提出的鸭子测试，“鸭子测试”可以这样表述：“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”
在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的。例如，在不使用鸭子类型的语言中，我们可以编写一个函数，它接受一个类型为"鸭子"的对象，并调用它的"走"和"叫"方法。在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的"走"和"叫"方法。如果这些需要被调用的方法不存在，那么将引发一个运行时错误。任何拥有这样的正确的"走"和"叫"方法的对象都可被函数接受的这种行为引出了以上表述，这种决定类型的方式因此得名。
**鸭子类型通常得益于不测试方法和函数中参数的类型，而是依赖文档、清晰的代码和测试来确保正确使用。** 

python中有一句谚语说的好，你看起来像鸭子，那么你就是鸭子。

鸭子类型示例：

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

# 鸭子类型：我们并不关心这个对象的类型本身，而是这个类是如何被使用的
def func(obj):
    obj.write()
    obj.read()

disk = Disk()
text = Text()

func(disk)
func(text)
```

可以很明显的看出，`Disk`类拥有跟`Text`类一样的方法，当有一个函数调用`Disk`类，并利用到了两个方法`read()`和`write()`。我们传入`Disk`类也一样可以运行，函数并不会检查对象的类型是不是`Disk`，只要他拥有`read()`和`write()`方法，就可以正确的被调用。 
再举例，如果一个对象实现了`__getitem__`方法，那python的解释器就会把它当做一个`collection`，就可以在这个对象上使用切片，获取子项等方法；如果一个对象实现了`__iter__`和`next`方法，python就会认为它是一个`iterator`，就可以在这个对象上通过循环来获取各个子项。 

Disk和 Text两个类完全没有耦合性，但是在某种意义上他们却统一了一个标准。

以上可以看出，func函数不会检查对象的类型，而是直接调用这个对象的走和游的方法，如果所需要的方法不存在就会报错。

对相同的功能设定了相同的名字，这样方便开发，这两个方法就可以互称为鸭子类型。

例如：序列类型有多种形态：字符串，列表，元祖，字典，但他们之间没有直接的继承关系

```python
l = [1, 2, 3]
t = (1, 2, 3, 4, 5)
s = 'hahaha'
d = {"a": 100}


# print(l.__len__())
# print(t.__len__())
# print(s.__len__())


def len(w):
    return w.__len__()


print(len(l))
print(len(t))
print(len(s))
```

```python
a = [1, 2, 3]
b = (4, 5, 6)  # 元祖
c = "123"  # 字符串
d = {"a": 100}  # 字典
e = 1  # 整型

# a.extend(b)
# print(a)
# a.extend(c)
# print(a)
a.extend(d)
print(a)
# a.extend(e)  # e 不可迭代，无法调用extend函数
# print(a)

# 打印：
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, '1', '2', '3']
[1, 2, 3, 4, 5, 6, '1', '2', '3', 'a']
Traceback (most recent call last):
  File "H:/Luffycity/test_pro/trademark_apply/test.py", line 13, in <module>
    a.extend(e)  # e 不可迭代，无法调用extend函数
TypeError: 'int' object is not iterabl
```

这样的例子很多：字符串，列表，元祖都有len方法，这就是统一了规范，这样的现象就是可以互称为鸭子类型。

### 8.12 封装

#### 8.12.1 如何将属性设为私有

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
        
a = A()
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

- 这种机制也并没有真正意义上限制我们从外部直接访问属性，知道了类名和属性名就可以拼出名字：_ 类名.__ 属性，然后就可以访问了，如a. _ A__ N

- 变形的过程只在类的定义是发生一次，在定义后的赋值操作，不会变形

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

#### 8.12.2 封装的意义

封装数据属性：明确的区分内外，控制外部对隐藏的属性的操作行为

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

封装方法：隔离复杂度

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

#### 8.12.3 特性（property）

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

#### 8.12.4 用property的意义

将一个类的函数定义成特性以后，对象再去使用的时候obj.name，根本无法察觉自己的name是执行了一个函数然后计算出来的，这种特性的使用方式**遵循了统一访问的原则**

```powershell
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
p.name = 102  # TypeError: 名字必须是字符串类型
del p.name  # TypeError: 不允许删除
```

#### 8.12.5 封装与扩展性

封装在于明确区分内外，使得类实现者可以修改封装内的东西而不影响外部调用者的代码；而外部使用用者只知道一个接口(函数)，只要接口（函数）名、参数不变，使用者的代码永远无需改变。这就提供一个良好的合作基础，或者说，只要接口这个基础约定不变，则代码改变不足为虑。

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
    def tell_area(self):  # 对外提供的接口,隐藏内部实现,此时我们想求的是体积,内部逻辑变了,只需修该下列一行就可以很简答的实现,而且外部调用感知不到,仍然使用该方法,但是功能已经变了
        return self.__width * self.__length * self.__high

# 对于仍然在使用tell_area接口的人来说，根本无需改动自己的代码，就可以用上新功能
>>> r1.tell_area()
```

### 8.13 绑定与非绑定

- 什么是绑定方法？

方法就是函数，面向对象编程中函数就是方法。绑定方法就是对象或类与函数进行绑定。

绑定方法有两种，一种是绑定给对象，一种是绑定给类

- 为什么要绑定？

对象本质上就是存放数据的容器，绑定方法就是将函数与数据绑定在一起，这个函数的功能就是处理数据。

- 为什么要将这样的函数和数据绑定？如何使用？

```python
# 一.对象的绑定方法
class ThisIsPerson:
    address = 'LiuHe'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self): #  这就是一个绑定给对象的方法
        print('%s😄%s是老板,%s岁' % (self.address, self.name, self.age))
        
obj6 = ThisIsPerson('tiandi', 23)
# 注意:用对象来调用没有传入参数，因为参数就是调用的对象本身
obj6.print_info() 
#LiuHe😄tiandi是老板,23岁

# 1.默认情况下，在类中定义的函数就是绑定方法
# 2.当用对象本身来调用类中的方法时，默认会把对象本身作为参数传入方法中。而用类名调用时则需要传入参数（对象）。
obj6 = ThisIsPerson('tiandi', 23)
ThisIsPerson.print_info(obj6)  # 这就是用类名进行调用，必须传入被绑定对象作为参数
#LiuHe😄tiandi是老板,23岁

总结：
# 1.默认情况下，在类中定义的函数就是绑定方法
# 2.当用对象本身来调用类中的方法时，默认会把对象本身作为参数传入方法中。而用类名调用时则需要传入参数（对象）。


# 二.类的绑定方法
class ThisIsPerson:
    address = 'LiuHe'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        print('%s😄%s是老板,%s岁' % (self.address, self.name, self.age))
    @classmethod
    def print_address(cls):  # 这就是一个类的绑定方法
        print('hello,here is%s' %ThisIsPerson.address)
        print(cls)
        
# 用类来调用时候
ThisIsPerson.print_address()

# 调用结果
#hello,here isLiuHe
#<class '__main__.ThisIsPerson'>

# 用对象来调用的时候
obj7 = ThisIsPerson('mingsheng', 26)
obj7.print_address()
# 结果不变

# 注意！
1.绑定给类的方法是利用解释器内置的装饰器 @classmethod  定义类的绑定方法时参数cls就是被绑定类本身，建议不要修改
2.类的绑定方法在调用时候可以用类或者对象调用，都不需要传入参数

# 分析：一个方法到底应该绑定给对象还是绑定给类呢？
1.当需要处理的数据包含在类中，就应该绑定给类
2.当需要处理的数据包含在对象中，就应绑定给对象

# 三.非绑定方法
# 既不绑定给类，也不绑定给对象
# 使用在数据既不需要访问类，也不需要访问对象
class ThisIsPerson:
    address = 'LiuHe'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        print('%s😄%s是老板,%s岁' % (self.address, self.name, self.age))
    @classmethod
    def print_address(cls):
        print('hello,here is%s' %ThisIsPerson.address)
        print(cls)
    @staticmethod
    def test_func(*args, **kwargs): # 非绑定方法
        print('这是一个非绑定方法')
        
# 通过类调用非绑定方法
ThisIsPerson.test_func()

# 通过对象调用非绑定方法
obj7 = ThisIsPerson('mingsheng', 26)
obj7.test_func(100)
#这是一个非绑定方法
#这是一个非绑定方法
```

类内部定义的函数分成两大类：

```powershell
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
    addr = "厦门"

    def __init__(self, name, age, sex):
        self.id = self.create_id()
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):  # 绑定到对象的方法
        print('Name:%s Age:%s Sex:%s AAA:%s' % (self.name, self.age, self.sex, self.addr))

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
p.tell()  # Name:ike Age:18 Sex:male

# 绑定给类,就应该由类来调用,自动将类本身当做第一个参数传入
p = People.from_conf()
p.tell()  # Name:egon Age:18 Sex:female

a = p.from_conf()
print(a.addr)  # egon

# 注意：绑定给对象，可以由类的对象来调用成员变量和类变量；绑定给类，可以调用类变量，不能调用成员变量；

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
print(m)	# classmethod：<192.168.1.203:9090>	staticmethod：就不告诉你
```

我们发现：

- `@classmethod` 修饰后，自动将类当作第一个参数传入
- `@staticmethod` 修饰后，不会自动将类当作第一个参数传入

### 8.14 内置方法

**反射**：通过字符串的映射到对象的属性，python中一切事物都是对象，都可以使用反射。

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
print(hasattr(obj, 'sex'))
print(hasattr(obj, 'talk'))

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

isinstance(obj,cls)检查obj是否是类 cls 的对象，判断一个对象是否是一个已知的类型，类似 type()

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

**item系列**：

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

**`__str__`，`__repr__`，`__format__`**

`__str__` 的功能与用法：

- `__str__` 功能：将实例对象按照自定义的格式用字符串的形式显示出来，提高可读性
- 实例化的对象在打印时会默认调用 `__str__` 方法，如果类没有重写这个方法，默认调用父类object的`__str__` 方法
- object的 `__str__` 方法内部是pass，所以打印的是内存地址。如果当前类重写了这个方法，会自动调用重写后的方法

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

`__repr__` 的功能与用法：

- `__repr__` 如果用IDE软件操作，功能与 `__str__` 完全一样，都是实例可视化显示
- 开发中如果用户需要可视化实例内容，只需要重写 `__str__` 或者 `__repr__` 方法之一即可。如果两个都有的话，默认调用 `__str__` 。

两者的区别：

- `__str__` 是面向用户显示的，若重构 `__str__` 则使用print(Object)可以显示想显示的内容
- `__repr__` 是面向程序员显示的，若重构 `__repr__`，则直接输出类对象和print(Object)均可以显示想显示的内容。

**`__del__`** 销毁实例方法，当对象在内存中被释放时，自动触发执行：

我们知道，Python 通过调用 __init__() 方法构造当前类的实例化对象，而本节要学的 __del__() 方法，功能正好和 __init__() 相反，其用来销毁实例化对象。事实上在编写程序时，如果之前创建的类实例化对象后续不再使用，最好在适当位置手动将其销毁，释放其占用的内存空间（整个过程称为垃圾回收（简称GC））。

> 大多数情况下，Python 开发者不需要手动进行垃圾回收，因为 Python 有自动的垃圾回收机制（下面会讲），能自动将不需要使用的实例对象进行销毁

无论是手动销毁，还是 Python 自动帮我们销毁，都会调用 __del__() 方法。举个例子：

```python
class CLanguage:
    def __init__(self):
        print("调用 __init__() 方法构造对象")
    def __del__(self):
        print("调用__del__() 销毁对象，释放其空间")
clangs = CLanguage()
del clangs

# 运行结果
调用 __init__() 方法构造对象
调用__del__() 销毁对象，释放其空间
```

⚠注意，千万不要误认为，只要为该实例对象调用 __del__() 方法，该对象所占用的内存空间就会被释放。举个例子：

```python
class CLanguage:
    def __init__(self):
        print("调用 __init__() 方法构造对象")
    def __del__(self):
        print("调用__del__() 销毁对象，释放其空间")
clangs = CLanguage()
# 添加一个引用clangs对象的实例对象
cl = clangs
del clangs
print("***********")

# 运行结果
调用 __init__() 方法构造对象
***********
调用__del__() 销毁对象，释放其空间
```

> 注意，最后一行输出信息，是程序执行即将结束时调用 __del__() 方法输出的。

可以看到，当程序中有其它变量（比如这里的 cl）引用该实例对象时，即便手动调用 __del__() 方法，该方法也不会立即执行。这和 Python 的垃圾回收机制的实现有关。

Python 采用自动引用计数（简称 ARC）的方式实现垃圾回收机制。该方法的核心思想是：每个 Python 对象都会配置一个计数器，初始 Python 实例对象的计数器值都为 0，如果有变量引用该实例对象，其计数器的值会加 1，依次类推；反之，每当一个变量取消对该实例对象的引用，计数器会减 1。如果一个 Python 对象的的计数器值为 0，则表明没有变量引用该 Python 对象，即证明程序不再需要它，此时 Python 就会自动调用 __del__() 方法将其回收。

以上面程序中的 clangs 为例，实际上构建 clangs 实例对象的过程分为 2 步，先使用 CLanguage() 调用该类中的 __init__() 方法构造出一个该类的对象（将其称为 C，计数器为 0），并立即用 clangs 这个变量作为所建实例对象的引用（ C 的计数器值 + 1）。在此基础上，又有一个 c1 变量引用 clangs（其实相当于引用 CLanguage()，此时 C 的计数器再 +1 ），这时如果调用`del clangs`语句，只会导致 C 的计数器减 1（值变为 1），因为 C 的计数器值不为 0，因此 C 不会被销毁（不会执行 __del__() 方法）。

如果在上面程序结尾，添加如下语句：

```python
del cl
print("-----------")

# 运行结果
调用 __init__() 方法构造对象
***********
调用__del__() 销毁对象，释放其空间
-----------
```

可以看到，当执行 del cl 语句时，其应用的对象实例对象 C 的计数器继续 -1（变为 0），对于计数器为 0 的实例对象，Python 会自动将其视为垃圾进行回收。

需要额外说明的是，如果我们重写子类的 __del__() 方法（父类为非 object 的类），则必须显式调用父类的 __del__() 方法，这样才能保证在回收子类对象时，其占用的资源（可能包含继承自父类的部分资源）能被彻底释放。为了说明这一点，这里举一个反例：

```python
class CLanguage:
    def __del__(self):
        print("调用父类 __del__() 方法")
class cl(CLanguage):
    def __del__(self):
        print("调用子类 __del__() 方法")
c = cl()
del c

# 运行结果
调用子类 __del__() 方法
```

在Python的类中存在一些特殊的方法，这些方法都是 `__方法__` 格式，这种方法在内部均有特殊的含义，接下来我们来讲一些常见的特殊成员：

- `__init__` 初始化方法

```python
class Foo(object):
    def __init__(self, name):
        self.name = name


obj = Foo("武沛齐")
```

- `__new__` 构造方法

```python
class Foo(object):
    def __init__(self, name):
        print("第二步：初始化对象，在空对象中创建数据")
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("第一步：先创建空对象并返回")
        return object.__new__(cls)


obj = Foo("武沛齐")
```

- `__call__` 该方法的功能类似于在类中重载 () 运算符，使得类实例对象可以像调用普通函数那样，以“对象名()”的形式使用。

```python
class Foo(object):
    def __call__(self, *args, **kwargs):
        print("执行call方法")


obj = Foo()
obj()
```

- `__dict__` 查看类中包含哪些属性

```python
class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Foo("武沛齐",19)
print(obj.__ict__)
```

- `__enter__`、`__exit__`

```python
class Foo(object):

    def __enter__(self):
        print("进入了")
        return 666

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("出去了")


obj = Foo()
with obj as data:
    print(data)
```

```python
超前知识：数据连接，每次对远程的数据进行操作时候都必须经历。
1.连接 = 连接数据库
2.操作数据库
3.关闭连接
```

```python
class SqlHelper(object):

    def __enter__(self):
        self.连接 = 连接数据库
        return 连接

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.连接.关闭

        
        
with SqlHelper() as 连接:
    连接.操作..
    
    
with SqlHelper() as 连接:
    连接.操作...
```

```python
# 面试题（补充代码，实现如下功能）

class Context:
    
    def do_something(self):
        print('内部执行')


with Context() as ctx:
    print('内部执行')
    ctx.do_something()

```

上下文管理的语法。

- `__add__` 等。

```python
class Foo(object):
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return "{}-{}".format(self.name, other.name)


v1 = Foo("alex")
v2 = Foo("sb")

# 对象+值，内部会去执行 对象.__add__方法，并将+后面的值当做参数传递过去。
v3 = v1 + v2
print(v3)
```

- `__iter__`

  - 迭代器

    ```python
    # 迭代器类型的定义：
        1.当类中定义了 __iter__ 和 __next__ 两个方法。
        2.__iter__ 方法需要返回对象本身，即：self
        3. __next__ 方法，返回下一个数据，如果没有数据了，则需要抛出一个StopIteration的异常。
    	官方文档：https://docs.python.org/3/library/stdtypes.html#iterator-types
            
    # 创建 迭代器类型 ：
    	class IT(object):
            def __init__(self):
                self.counter = 0
    
            def __iter__(self):
                return self
    
            def __next__(self):
                self.counter += 1
                if self.counter == 3:
                    raise StopIteration()
                return self.counter
    
    # 根据类实例化创建一个迭代器对象：
        obj1 = IT()
        
        # v1 = obj1.__next__()
        # v2 = obj1.__next__()
        # v3 = obj1.__next__() # 抛出异常
        
        v1 = next(obj1) # obj1.__next__()
        print(v1)
    
        v2 = next(obj1)
        print(v2)
    
        v3 = next(obj1)
        print(v3)
    
    
        obj2 = IT()
        for item in obj2:  # 首先会执行迭代器对象的__iter__方法并获取返回值，一直去反复的执行 next(对象) 
            print(item)
            
    迭代器对象支持通过next取值，如果取值结束则自动抛出StopIteration。
    for循环内部在循环时，先执行__iter__方法，获取一个迭代器对象，然后不断执行的next取值（有异常StopIteration则终止循环）。
    ```

  - 生成器

    ```python
    # 创建生成器函数
        def func():
            yield 1
            yield 2
        
    # 创建生成器对象（内部是根据生成器类generator创建的对象），生成器类的内部也声明了：__iter__、__next__ 方法。
        obj1 = func()
        
        v1 = next(obj1)
        print(v1)
    
        v2 = next(obj1)
        print(v2)
    
        v3 = next(obj1)
        print(v3)
    
    
        obj2 = func()
        for item in obj2:
            print(item)
    
    # 如果按照迭代器的规定来看，其实生成器类也是一种特殊的迭代器类（生成器也是一个特殊的迭代器）。
    ```

  - 可迭代对象

    ```python
    # 如果一个类中有__iter__方法且返回一个迭代器对象 ；则我们称以这个类创建的对象为可迭代对象。
    
    class Foo(object):
        
        def __iter__(self):
            return 迭代器对象(生成器对象)
        
    obj = Foo() # obj是 可迭代对象。
    
    # 可迭代对象是可以使用for来进行循环，在循环的内部其实是先执行 __iter__ 方法，获取其迭代器对象，然后再在内部执行这个迭代器对象的next功能，逐步取值。
    for item in obj:
        pass
    ```

    ```python
    class IT(object):
        def __init__(self):
            self.counter = 0
    
        def __iter__(self):
            return self
    
        def __next__(self):
            self.counter += 1
            if self.counter == 3:
                raise StopIteration()
            return self.counter
    
    
    class Foo(object):
        def __iter__(self):
            return IT()
    
    
    obj = Foo() # 可迭代对象
    
    
    for item in obj: # 循环可迭代对象时，内部先执行obj.__iter__并获取迭代器对象；不断地执行迭代器对象的next方法。
        print(item)
    ```

    ```python
    # 基于可迭代对象&迭代器实现：自定义range
    class IterRange(object):
        def __init__(self, num):
            self.num = num
            self.counter = -1
    
        def __iter__(self):
            return self
    
        def __next__(self):
            self.counter += 1
            if self.counter == self.num:
                raise StopIteration()
            return self.counter
    
    
    class Xrange(object):
        def __init__(self, max_num):
            self.max_num = max_num
    
        def __iter__(self):
            return IterRange(self.max_num)
    
    
    obj = Xrange(100)
    
    for item in obj:
        print(item)
    ```

    ```python
    class Foo(object):
        def __iter__(self):
            yield 1
            yield 2
    
    
    obj = Foo()
    for item in obj:
        print(item)
    ```

    ```python
    # 基于可迭代对象&生成器 实现：自定义range
    
    class Xrange(object):
        def __init__(self, max_num):
            self.max_num = max_num
    
        def __iter__(self):
            counter = 0
            while counter < self.max_num:
                yield counter
                counter += 1
    
    
    obj = Xrange(100)
    for item in obj:
        print(item)
    ```

    常见的数据类型：

    ```python
    v1 = list([11,22,33,44])
    
    v1是一个可迭代对象，因为在列表中声明了一个 __iter__ 方法并且返回一个迭代器对象。
    ```

    ```python
    from collections.abc import Iterator, Iterable
    
    v1 = [11, 22, 33]
    print( isinstance(v1, Iterator) )  # false，判断是否是迭代器；判断依据是__iter__ 和 __next__。
    v2 = v1.__iter__()
    print( isinstance(v2, Iterator) )  # True
    
    
    
    v1 = [11, 22, 33]
    print( isinstance(v1, Iterable) )  # True，判断依据是是否有 __iter__且返回迭代器对象。
    
    v2 = v1.__iter__()
    print( isinstance(v2, Iterable) )  # True，判断依据是是否有 __iter__且返回迭代器对象。
    ```


### 8.15 元类

#### 8.15.1 储备介绍exec

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

#### 8.15.2 元类解释

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

#### 8.15.3 自定义元类控制类的行为

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

示例二：在元类的实例中定义一个 `__call__` 方法，元类实例化后调用类执行，进而控制实例化的过程

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

### 8.16 异常

异常是错误发生的信号，一旦程序出错，并且程序没有处理这个错误，那么就会抛出异常，并且程序的运行随之终止。

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

```powershell
AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python 代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
```

更多的异常：

```powershell
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
    if age.isdigit(): # 只有在age为字符串形式的整数时,下列代码才不会出错,该条件是可预知的
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

- 万能异常：Exception，也可以在最后加一个

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
    print('无论被监测的代码有没有发生异常都执行')
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

---

## 第九章 网络编程

计算机基础知识：

我们开发的软件都是应用软件，应用软件必须应用于操作系统上，操作系统必须运行硬件上，应用软件是无法直接应用到硬件上的，应用软件对硬件的操作必须调用操作系统的接口，由操作系统操控硬件。

**TCP的三次握手和四次挥手**

三次握手

 ![三次握手](J:\homework\Python学习笔记\Python_notes.assets\format,png) 

  ![1643078023700](J:\homework\Python学习笔记\Python_notes.assets\1643078023700.png)

这张图展示了建立TCP连接所需的三次握手过程。

首先需要明确，三次握手的目的是建立可靠的通信信道，即双方确认彼此的信息发送与接收是正常的。

其次需要明确，客户端与服务器的身份并不是固定的，在某些情况下的客户端，在另外的情况下可能会承担服务器的角色。

下面我们依次来看三次握手的过程和目的。

第一次握手：客户端向服务端发送SYN。此时客户端什么都不能确认；服务端确认对方发送正常，自己接收正常。

第二次握手：服务端向客户端发送SYN/ACK。此时客户端确认自己发送、接收正常，对方发送、接收正常；服务端确认对方发送正常，自己接收正常。

第三次握手：客户端向服务端发送ACK。此时客户端确认自己发送、接收正常，对方发送、接收正常；服务端确认自己发送、接收正常，对方发送、接收正常。

综上所述，当且仅当三次握手之后，双方都能够确认收发功能正常。

四次挥手：

  ![四次挥手](J:\homework\Python学习笔记\Python_notes.assets\format1,png) 

 ![1643078043420](J:\homework\Python学习笔记\Python_notes.assets\1643078043420.png)

这张图展示了断开TCP连接所需的四次挥手过程。

下面我们依次来看四次挥手的过程和目的。

第一次挥手：客户端向服务端发送FIN。用来关闭客户端到服务器的数据传送。

第二次挥手：服务器向客户端发送ACK。表示服务端收到了客户端的连接释放通知。

第三次挥手：服务器向客户端发送FIN。用来关闭与客户端的数据传送。

第四次挥手：客户端向服务端发送ACK。表示客户端收到了服务端的连接释放通知。

同样，这里所说的客户端和服务器并不是一个固定的概念。事实上，建立TCP连接的任何一方都可以在数据传送结束后发出连接释放通知，待对方确认后进入半关闭状态。当另一方也没有数据再发送的时候，则发出连接释放通知，对方确认后就完全关闭了TCP连接。

另外，值得注意的是，在第四次挥手之后，客户端并非立马进入关闭状态，而是会进入TIME-WAIT状态，在等待2MSL时间后，才会进入关闭状态。这样做的原因主要有以下两点：

第一，防止客户端发送的最后一个ACK报文丢失而引起服务端不能正常关闭。

第二，防止已经失效的连接请求报文段对新连接造成影响。

### 9.1 网络应用开发架构

- C/S架构
    - C指的是client（客户端）
    - S值得是server（服务端）
- B/S架构
    - B指的是browser（浏览器）
    - S值得是server（服务端）

比如一个登陆功能的流程：

- 用户输入账号和密码后，存放于客户端内存地址中，然后调用接口将数据发送给操作系统
- 客户端操作系统收到数据后，按照客户端软件指定的协议，调用网卡发送数据
- 网络传输数据
- 服务端软件调用系统接口，将数据从客户端操作系统的内存拷贝到自己的内存
- 服务端操作系统收到指令后，使用与客户端相同的协议，从网卡接收数据，然后拷贝给服务端软件

### 9.2 TCP/IP的基础知识

Transmission Control Protocol/Internet Protocol的简写，中译名为传输控制协议/因特网互联协议，又名网络通讯协议，是Internet最基本的协议、Internet国际互联网络的基础。

TCP/IP五层协议：

- 物理层

    - 主要是基于电器特性发送高低电压(电信号)，高电压对应数字1，低电压对应数字0

- 数据链路层

    - 协议：两台物理设备之间对于要发送的内容，长度和顺序做的一些规范
    - mac地址：每一块网卡上都有一个全球唯一的mac地址
    - 交换机：是连接多台机器并帮助通讯的物理设备，只可以识别mac地址

- 网络层

    - ip地址：

        - ipv4协议，位的点分十进制，32位的2进制表示，范围：0.0.0.0 ~ 255.255.255.255

        - ipv6协议，8位的冒分十六制，128位十进制来表示 (点分十进制不足以表示)，范围：0:0:0:0:0:0:0:0 ~ FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF

        - ip使用：

            - 如果一个ip地址想被所有人都看到，这个ip地址是必须要申请的，即公网IP

            - 提供内网ip，供局域网使用：

                192.168.0.0 - 192.168.255.255

                172.16.0.0 - 172.31.255.255

                10.0.0.0 - 10.255.255.255

        - 网关ip:一个局域网的网络出口，访问局域网以外的区域都需要经过路由器的网关

        - 网段： 一般是一个末尾为0的地址段

        - 子网掩码： 判断两个机器是否在同一个网段，子网掩码不能单独存在，它必须结合IP地址一起使用

    - 交换机实现的arp协议：

        - 通过ip地址和子网掩码获取一台机器的mac地址
        - 交换机工作原理：收到一个请求，通知所有连接他的ip地址，获取对应ip地址的mac地址并返回给请求的ip地址

    - ip地址可以确认一台机器，port端口可以确认一台机器的一个应用，一般有65535个端口

    - 一般实现互联，使用127.0.0.1 是自己的地址，不过交换机 ip地址是可以过交换机的

- 传输层：https://www.cnblogs.com/cnike/p/10726069.html

    - 传输层功能：建立端口到端口的通信
    - TCP协议：
        - 面向连接的，可靠，但是慢，可以实现全双工通信，即双方都是实时的，区别于半双工（传呼机）
        - 无边界，流式传输
        - 具体的连接方式，在建立连接的时候，需经过三次握手，即请求方向服务器发送链接请求是第一次，服务器同意并向请求方发送链接请求是第二次，请求方通过是第三次，即三次握手。
        - 具体的断开连接方式，需要经过四次挥手，即请求方向服务器发送断开请求是第一次，服务器同意是第二次，服务器向请求方发送断开请求是第三次，请求方通过是第四次。
        - 在建立连接的时候，tcp协议发送的每一条信息都会有回执，而且为了保证数据的完整性，还会有重传机制，即发送不过去的，会自动再次发送
        - 长连接：会一直占用双方的端口
        - 能够传输的数据长度几乎没有限制
        - IO操作 I: input O:output 输入输出都是相对内存来说
            - write send 输出 output
            - read recv 输入 input
    - UDP协议：
        - 面向数据报的，无连接，速度很快，类似于发短信，能实现一对一，多对一，一对多的高效通讯
        - 由于没有回执，对于发送信息和接受信息的双方来说，可能存在丢失消息的情况
        - 能够传递的长度有限，是根据数据传递设备的位置有关系

- 应用层

    - 我们开发的软件都在应用层

### 9.3 Socket（套接字）

- Socket是应用层与传输层的中间软件抽象层，它是一组接口，可以帮我们完成所有信息的组织和拼接

- 通过socket建立起2台机器的连接后，本质上socket只干2件事，一是收数据，一是发数据，没数据时就等着

- 通过python的socket模块完成socket的功能

示例：

服务端：

```python
import socket

# 基于网络通信,基于TCP协议
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定之前加,内存中有,重复使用端口
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定服务器地址
phone.bind(('127.0.0.1', 8083))

# 开始监听
phone.listen(5)
while True:
    # 等待接收数据
    conn, client_addr = phone.accept()

    while True:
        try:
            # 接收数据
            data = conn.recv(1024)
            # 打印接收到的数据
            print('Client recv:', data)
            # 服务端收不到数据,就直接break
            if not data:  
                break
            # 回复消息
            response = input('>>>:').strip()
            conn.send(response.encode())
            # 打印回复消息
            print('Server send:', response)
        except ConnectionResetError:
            print('客户端强制关闭')
            break

    conn.close()

phone.close()
```

客户端：

```python
import socket

# 基于网络通信,基于TCP协议
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器地址
phone.connect(('127.0.0.1', 8083))

while True:
    # 给服务端发送消息
    msg = input('>>>:').strip()
    if not msg: continue
    phone.send(msg.encode('utf-8'))
    # 接收服务端消息
    data = phone.recv(1024)
    # 打印服务端消息
    print(data)

phone.close()
```

### 9.4 粘包现象

示例：

服务端：

```python
import socket
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 8083))  # 0-65535:0-1024个操作系统使用,1024以后随便用

phone.listen(5)

print('staring...')
while True:
    conn, client_addr = phone.accept()  # 接收链接对象
    print(client_addr)

    # 5.收 发消息
    while True:  # 通信循环
        try:
            # 1.收命令
            cmd = conn.recv(1024)  # 1.单位:bytes 2.1024代表最大接受1024个bytes
            # if not data:break  # 适用于linux操作系统  如果没有接收,break 客户端强制关闭
            print('客户端的数据', cmd)

            # 2.执行命令,拿到结果
            obj = subprocess.Popen(cmd.decode('gbk'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            # 正确的命令
            stdout = obj.stdout.read()
            # 错误的命令
            stderr = obj.stderr.read()

            # 3.把命令的结果返回个客户端
            print(len(stdout)+len(stderr))
            conn.send(stdout+stderr)

        except ConnectionResetError:  # 适用于windows系统
            print('客户端强制关闭')
            break

    conn.close()

phone.close()
```

客户端：

```python
import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8083))

# 3.发 收消息
while True:
    # 1.发命令
    cmd = input('>>>:').strip()  # msg = ''  输入空
    if not cmd:continue  # 不能输入空
    phone.send(cmd.encode('gbk'))  # phont.send(b'')

    # 2.拿到命令的结果,并打印
    data = phone.recv(1024)  # 1024是一个坑
    print(data.decode('gbk'))

# 4.关闭
phone.close()
```

操作：

- 启动服务端和客户端
- 命令行输入dir，然后再输入tasklist，最后输入dir看结果
- 此时产生粘包现象

粘包的产生分析：

- 发送的数据小于TCP发送缓冲区的空间，TCP将多次写入缓冲区的数据一起发出去，产生粘包

    服务端：

    ```python
    import socket
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9903))
    server.listen(5)
    
    conn, addr = server.accept()
    
    
    res1 = conn.recv(1024)
    print('第一次', res1)
    
    res2 = conn.recv(10)
    print('第二次', res2)
    ```

    客户端：

    ```python
    import socket
    import time
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9903))
    
    client.send('hello'.encode('utf-8'))
    client.send('world'.encode('utf-8'))
    ```

- 接收数据没收干净，导致数据滞留在接收管道中，产生粘包

    服务端：

    ```python
    import socket
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9903))
    server.listen(5)
    
    conn, addr = server.accept()
    
    
    res1 = conn.recv(3)
    print('第一次', res1)
    
    res2 = conn.recv(10)
    print('第二次', res2)
    ```

    客户端：

    ```python
    import socket
    import time
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9903))
    
    client.send('hello'.encode('utf-8'))
    client.send('world'.encode('utf-8'))
    ```

补充问题：

- 为何说tcp是可靠传输，udp是不可靠传输

    - tcp在数据传输时，发送端先把数据发送到自己的缓存中，然后协议控制将缓存中的数据发往另一端，另一端返回一个ack=1，发送端则清理缓存中的数据，另一端返回ack=0，则重新发送数据，所以tcp是可靠的

    - 而udp发送数据，另一端是不会返回确认信息的，因此不可靠

- send与recv对比

    - recv：服务端等待数据到服务器的操作系统缓存区，耗时长，由服务器操作系统缓存器拷贝到服务端程序
    - send：客户端程序把数据拷贝到操作系统缓存区

### 9.5 解决粘包

示例：方式一

服务端

```python
import socket
import struct
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 8088))

phone.listen(5)

print('staring...')
while True:
    conn, client_addr = phone.accept()  # 接收链接对象
    print(client_addr)

    while True:
        try:
            cmd = conn.recv(1024)
            print('客户端的数据', cmd)

            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            # 第一步:把报头(固定长度)发给客户端
            total_size = len(stdout)+len(stderr)
            header = struct.pack('i', total_size)

            # 第二步:把报头发给客户端
            conn.send(header)

            # 第三步:再发送真实的数据
            conn.send(stdout+stderr)

        except ConnectionResetError:
            print('客户端强制关闭')
            break

    conn.close()

phone.close()
```

客户端：

```python
import socket
import struct  

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8088))

while True:
    cmd = input('>>>:').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))

    # 第一步:先收报头
    header = phone.recv(4)

    # 第二步:从报头中解析出对帧数数据的描述信息(数据的长度)
    total_size = struct.unpack('i', header)[0]

    # 第三步:接收真实的数据
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:
        res = phone.recv(1024)
        recv_data += res
        recv_size += len(res)
        print(recv_data.decode('utf-8'))

phone.close()
```

方式二：

服务端：

```python
import json
import socket
import struct  # 该模块可以把一个类型，如数字，转成固定长度的bytes
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 8083))

phone.listen(5)

print('staring...')
while True:
    conn, client_addr = phone.accept()  # 接收链接对象
    print(client_addr)

    while True:
        try:
            cmd = conn.recv(1024)  # 接收命令
            print('客户端的数据', cmd)

            obj = subprocess.Popen(cmd.decode('utf-8'),  # 该系统命令必须是字符串格式，所以必须进行解码
            					   shell=True,
                                   stdout=subprocess.PIPE,  # 正确命令输出结果
                                   stderr=subprocess.PIPE)  # 错误命令输出结果
            stdout = obj.stdout.read()  # 从管道中读取正确的结果
            stderr = obj.stderr.read()  # 从管道中读取错误的结果
            # 第一步:制作报头，把报头(固定长度)发给客户端  # 模拟文件的上传和下载，则报头中应该包括文件名，文件的大小，文件的md5值....
            header_dic = {
                'filename': 'a.txt',
                'md5': 'xxx',
                'total_size': len(stdout)+len(stderr)  # 真实数据的总大小
            }
            header_json = json.dumps(header_dic)  # 将报头这种数据类型即字典转换成json格式(是一种json格式的字符串)，可以基于网络传输
            header_bytes = header_json.encode('utf-8')  # 将json格式的字符串转换成bytes,基于网络进行传输给客户端

            # 第二步:先发送报头的长度
            conn.send(struct.pack('i', len(header_bytes)))  # 通过struct模块将报头的长度转换成固定长度的bytes大小（i格式是4个字节大小），并将固定报头长度 发送给客户端

            # 第三步:再发送报头
            conn.send(header_bytes)  # 将报头的内容发送给客户端

            # 第四步:再发送真实的数据
            conn.send(stdout+stderr)  # 将正确和错误的真实数据发送给客户端

        except ConnectionResetError:
            print('客户端强制关闭')
            break

    conn.close()

phone.close()
```

客户端：

```python
import json
import socket
import struct

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8083))

while True:
    cmd = input('>>>:').strip()
    if not cmd:continue  # 输入的命令不能为空
    phone.send(cmd.encode('utf-8'))  # 将字符串形式的命令转换成bytes类型，发送给服务端

    # 第一步:先收报头长度
    header_size = struct.unpack('i', phone.recv(4))[0]  # 将服务端打包过来报头的长度进行解包(是一个元组，第一个值是报头的大小)，解析出报头的长度

    # 第二步:再收报头
    header_bytes = phone.recv(header_size)  # 已接收报头的长度，可以通过报头的长度来接收bytes类型的报头

    # 第三步:从报头中解析出对帧数数据的描述信息
    header_json = header_bytes.decode('utf-8')  # 将bytes类型的报头的解码成json格式的字符串
    header_dic = json.loads(header_json)  # 将json格式的字符串反序列化成字典，也就是拿到了字典形式的报头
    print(header_dic)
    total_size = header_dic['total_size']  # 拿到字典形式的报头，就可以通过key值，取到服务端发送真实数据的总大小

    # 第四步:接收真实的数据
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:  # 循环接收真实数据
        res = phone.recv(1024)  # 每次接收数据的大小1024个字节
        recv_data += res  # 每次接收的真实数据拼接到空字符串中
        recv_size += len(res)  # 每循环一次接收的大小加每次接收真实数据的大小的长度
        print(recv_data.decode('utf-8'))  # 接收完真实数据将其解码打印

phone.close()
```

步骤解析：

服务端：

1. 把报头做成字典，包含将要发送的详细信息

2. 把字典通过序列化转换成一个json字符串

3. 把json字符串编码成bytes类型

4. 通过struct模块打包bytes类型的报头长度发送给客户端

5. 再发送bytes类型的报头

6. 再发送真实数据

客户端：

1. 收报头的长度，通过struck解包报头
2. 再收报头
3. 把收到的报头解码
4. 通过反序列化转成字典格式
5. 从字典中的key取出数据
6. 循环接收数据

### 9.6 UDP协议不会粘包

示例：

服务端：

```python
from socket import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('127.0.0.1', 8089))

res1 = server.recvfrom(1)
print('第一次', res1)

res2 = server.recvfrom(1024)
print('第二次', res2)

server.close()
```

客户端：

```python
from socket import *

client = socket(AF_INET, SOCK_DGRAM)


client.sendto(b'hello', ('127.0.0.1', 8089))
client.sendto(b'world', ('127.0.0.1', 8089))

client.close()

```

练习：

服务端：

```python
from socket import *

server = socket(AF_INET, SOCK_DGRAM)  # UDP协议
server.bind(('127.0.0.1', 8088))

while True:
    data, client = server.recvfrom(1024)
    print(data)

    server.sendto(data.upper(), client)

server.close()
```

客户端：

```python
from socket import *

client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('>>:').strip()
    client.sendto(msg.encode('gbk'), ('127.0.0.1', 8088))

    data, server_addr = client.recvfrom(1024)
    print(data, server_addr)

client.close()
```

---

## 第十章 并发编程

### 10.1 操作系统发展史

- 人机矛盾：CPU利用率低
- 磁带存储+批处理：降低数据的读取时间,提高CPU的利用率
- 多道操作系统：在一个任务中遇到IO操作让出CPU
    - 数据隔离概念
    - 时空复用概念
    - 能够在一个任务遇到io操作的时候动把CPU让出来，给其他的任务使用
- 分时操作系统：
    - 短作业优先算法
    - 先来先服务算法
    - 时间分片
        - CPU的轮转:每一个程序分配一个时间片
        - 需要切换,要占用时间
        - 降低了CPU的利用率
        - 提高了用户体验
- 分时+多道操作系统
    - 多个程序一起在计算机中执行
    - 一个程序如果遇到IO操作,切出去让出CPU
    - 一个程序如果没有遇到IO,但是时间片到时了,切出去让出CPU
- 实时操作系统
- 网络操作系统
- 分布式操作系统

### 10.2 进程

#### 10.2.1 概念

进程是计算机中资源分配的最小单元；一个进程中可以有多个线程，同一个进程中的线程共享资源；

进程与进程之间则是相互隔离。

Python中通过多进程可以利用CPU的多核优势，计算密集型操作适用于多进程。

- 定义：运行中的程序叫做进程
- 程序和进程之间的区别：程序只是一个文件，进程代表这个文件被cpu运行起来的过程
- 进程是计算机中最小的资源分配单位，进程的pid（port id）并不与程序绑定，每次随机分配
- 在操作系统中得唯一标识符是pid

**进程调度**

- 操作系统调度进程的算法
    - 短作业优先
        - 根据任务量大小来划分谁先谁后执行。
    - 先来先服务
        - 哪个任务先来，哪个任务先执行，其他需要等待。
    - 时间片轮转
        - 来的每个任务都轮流执行固定N分钟。
    - 多级反馈算法
        - 主要工作机制，设有N个队列（Q1,Q2....QN），其中各个队列对于处理机制的优先级是不一样的，也就是说位于各个队列中的作业(进程)的优先级也是不一样的。
        - 对于N个作业，先来先服务，再来的等待，此时最先来的任务如果进行到规定时间片还没有执行完毕，会被重新放回到下一个队列等待，如果在Q2中此任务还不能完成，再依次放到下一个。
        - 单个队列遵循，先来先服务和时间片轮转原则，队列之间遵循短作业优先，Q1一定比Q2时间片短，且Q1优先级最高，依次类推。即使第QN个有N个人物在等待，第1~N-1个作业中有任意一个还在运行，此N任务中作业就不执行，只有上述全部处理完毕，才执行QN。

**并行与并发**

- 并行
    - 两个程序，两个cpu，每个程序分别占用一个cpu自己执行自己的
    - 看起来是同时执行，实际在每一个时间点上都在各自执行着
- 并发
    - 两个程序，一个cpu，两个程序交替的在一个cpu上执行
    - 看起来是在同时执行，但是实际上仍然是串行

**同步和异步**

- 同步
    - 程序1调用程序2时，程序1停止工作，直到程序2完成后，程序1才继续工作
    - 同步阻塞：调用函数，这个函数并没有完全利用cpu，即存在io操作
    - 同步非阻塞：调用函数，整个运行过程中没有io操作
- 异步
    - 程序1调用程序2时，程序1继续自己的下一个动作，不受程序2的的影响
    - 异步非阻塞：
        - func扔到其他异步任务里执行
        - 本身的任务和func任务各自执行各自的，没有io操作
    - 异步阻塞：\
- 阻塞
  
    - 阻塞的概念往往伴随着线程。线程一般是指：在调用结果返回前，当前线程会被挂起。调用线程只有在得到结果后才会被唤醒执行后续的操作。
- 非阻塞
  
    - 阻塞的反向操作，非阻塞的调用是指：在结果没有返回前，该调用不会阻塞住当前的线程
- 阻塞/非阻塞 同步/异步
    - 两者有本质的区别，主要是面向对象的不同
    - 阻塞/非阻塞：进程/线程需要操作的数据如果尚未就绪，是否妨碍了当前进程/线程的后续操作。
    - 同步/异步 ：数据尚未准备就绪，是否等待数据结果。
- 运行的三状态图
  
    - 就绪、运行、阻塞
    
    ![1643078171945](J:\homework\Python学习笔记\Python_notes.assets\1643078171945.png)

#### 10.2.2 进程介绍

方式一：

```python
import time
from multiprocessing import Process


def task(name):
    print('%s is running' % name)
    time.sleep(3)
    print('%s is done' % name)


if __name__ == '__main__':
    # 在主进程下开启子进程
    p = Process(target=task, args=('子进程',))
    p = Process(target=task, kwargs={'name':'子进程'})
    p.start()  # 给操作系统发送一个信号
    # 异步--调用开启进程的方法，但是并不等待这个进程是否开启，只是负责通知操作系统进行，开启进程后，主进程和子进程，各自进行
    print('主进程/主线程')
```

- 几乎是t.start ()的同时就将线程开启了，然后先打印出了 主进程/主线程，证明线程的创建开销极小
- p.start ()将开启进程的信号发给操作系统后，操作系统要申请内存空间，然后拷贝父进程地址空间到子进程，开销远大于线程
- p.start ()将开启进程的信号发给操作系统后，操作系统要申请内存空间，让好拷贝父进程地址空间到子进程，开销远大于线程

方式二：使用面向对象重写Process方法

```python
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):  # 函数名必须是run
        print('%s is running!' % self.name)
        time.sleep(2)
        print('%s is done' % self.name)


if __name__ == '__main__':
    p = MyProcess('子进程')
    p.start()
    print('ok')
```

查看进程的pid和ppid：

```python
import os
import time
from multiprocessing import Process

# getpid查看自己的进程id，getppid查看他爹的进程id

def task():
    print('%s is running, parent is <%s>====%s' % (os.getpid(), os.getppid(), os.getppid()))
    time.sleep(3)
    print('%s is done, parent is <%s>=======%s' % (os.getpid(), os.getppid(), os.getppid()))


if __name__ == '__main__':
    p = Process(target=task,)
    p.start()  # 给操作系统发送一个信号
    print('主流程', os.getpid(), os.getppid())  # windows查看：tasklist | findstr pycharm
    
'''
结果：
主流程 12140 9932
11540 is running, parent is <12140>====12140
11540 is done, parent is <12140>=======12140
'''
```

- 在主进程下开启子进程，子进程的ppid就是主进程的pid

关于在Python中基于multiprocessiong模块操作的进程：

Depending on the platform, [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) supports three ways to start a process. These *start methods* are

> - *fork*，【“拷贝”几乎所有资源】【支持文件对象/线程锁等传参】【unix】【任意位置开始】【快】
>
> The parent process uses [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork) to fork the Python interpreter. The child process, when it begins, is effectively identical to the parent process. All resources of the parent are inherited by the child process. Note that safely forking a multithreaded process is problematic.Available on Unix only. The default on Unix.
>
> - *spawn*，【run参数传必备资源】【不支持文件对象/线程锁等传参】【unix、win】【main代码块开始】【慢】
>
> The parent process starts a fresh python interpreter process. The child process will only inherit those resources necessary to run the process object’s [`run()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.run) method. In particular, unnecessary file descriptors and handles from the parent process will not be inherited. Starting a process using this method is rather slow compared to using *fork* or *forkserver*.Available on Unix and Windows. The default on Windows and macOS.
>
> - *forkserver*，【run参数传必备资源】【不支持文件对象/线程锁等传参】【部分unix】【main代码块开始】
>
> When the program starts and selects the *forkserver* start method, a server process is started. From then on, whenever a new process is needed, the parent process connects to the server and requests that it fork a new process. The fork server process is single threaded so it is safe for it to use [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork). No unnecessary resources are inherited.Available on Unix platforms which support passing file descriptors over Unix pipes.

```python
import multiprocessing
multiprocessing.set_start_method("spawn")
```

*Changed in version 3.8:* On macOS, the *spawn* start method is now the default. The *fork* start method should be considered unsafe as it can lead to crashes of the subprocess. See [bpo-33725](https://bugs.python.org/issue33725).

*Changed in version 3.4:* *spawn* added on all unix platforms, and *forkserver* added for some unix platforms. Child processes no longer inherit all of the parents inheritable handles on Windows.

On Unix using the *spawn* or *forkserver* start methods will also start a *resource tracker* process which tracks the unlinked named system resources (such as named semaphores or [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory) objects) created by processes of the program. When all processes have exited the resource tracker unlinks any remaining tracked object. Usually there should be none, but if a process was killed by a signal there may be some “leaked” resources. (Neither leaked semaphores nor shared memory segments will be automatically unlinked until the next reboot. This is problematic for both objects because the system allows only a limited number of named semaphores, and shared memory segments occupy some space in the main memory.)

官方文档：https://docs.python.org/3/library/multiprocessing.html

示例一：fork模式，“拷贝”几乎所有资源

```python
import multiprocessing
import time

"""
def task():
    print(name)
    name.append(123)


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # fork、spawn、forkserver
    name = []

    p1 = multiprocessing.Process(target=task)
    p1.start()

    time.sleep(2)
    print(name)  # []

# 设置进程为fork模式，子进程会拷贝主进程全部资源，他们之间的资源是相互隔离的，所以子进程append123后，主进程打印name还是空的列表
"""
"""
def task():
    print(name) # [123]


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # fork、spawn、forkserver
    name = []
    name.append(123)

    p1 = multiprocessing.Process(target=task)
    p1.start()
    
# 主进程先append123后，开了一个子进程，这时子进程name列表里存在了123
"""

"""
def task():
    print(name)  # []


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # fork、spawn、forkserver
    name = []
    
    p1 = multiprocessing.Process(target=task)
    p1.start()

    name.append(123)
   
# 主进程name是空的时候，开了一个子进程，这时子进程name列表是空
"""
```

示例二：spawn模式和forkserver模式，run参数传必备资源

```python
import multiprocessing
import time

"""
def task(data):
    print(data)
    data.append(999)


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")  # fork、spawn、forkserver
    name = []

    p1 = multiprocessing.Process(target=task, args=(name, ))
    p1.start()

    time.sleep(2)
    print(name) # []
"""

def task(data):
    print(data)
    data.append(999)


if __name__ == '__main__':
    multiprocessing.set_start_method("forkserver")  # fork、spawn、forkserver
    name = []

    p1 = multiprocessing.Process(target=task, args=(name, ))
    p1.start()

    time.sleep(2)
    print(name) # []
# 设置进程为spawn/forkserver模式，参数传必备的资源，子进程会拷贝参数传入的资源，他们之间的资源是相互隔离的，所以子进程append999后，主进程打印name还是空的列表
```

示例三：fork模式，支持文件对象/线程锁等传参

```python
import multiprocessing
import threading
import time

def task():
    print(file_object, lock)


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # fork、spawn、forkserver

    name = []
    file_object = open('x1.txt', mode='a+', encoding='utf-8')
    lock = threading.RLock()

    p1 = multiprocessing.Process(target=task)
    p1.start()
    
# 设置进程为for模式，支持文件对象/线程锁等传参，子进程会拷贝主进程全部资源，他们之间的资源是相互隔离的
```

示例四：spawn模式和forkserver模式，不支持文件对象/线程锁等传参

```python
import multiprocessing
import threading
import time

def task():
    print(file_object, lock)


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # fork、spawn、forkserver

    name = []
    file_object = open('x1.txt', mode='a+', encoding='utf-8')
    lock = threading.RLock()

    p1 = multiprocessing.Process(target=task, args=(file_object, lock,))
    p1.start()
# 会报错，不支持文件对象/线程锁传参，TypeError: cannot serialize '_io.TextIOWrapper' object

# 正确的做法：子进程中单独写入自己的文件对象/线程锁
def task():
    file_object = open('x1.txt', mode='a+', encoding='utf-8')
    lock = threading.RLock()


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")  # fork、spawn、forkserver

    name = []
    file_object = open('x1.txt', mode='a+', encoding='utf-8')
    lock = threading.RLock()

    p1 = multiprocessing.Process(target=task)
    p1.start()
```

案例：

```python
import multiprocessing


def task():
    print(name)  # 123 abc 123
    file_object.write("abc\n")
    file_object.flush()


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    
    name = []
    file_object = open('x1.txt', mode='a+', encoding='utf-8')
    file_object.write("123\n")  # 写入到内存，没有写入文件，开子进程时拷贝主进程写入内存的值

    p1 = multiprocessing.Process(target=task)
    p1.start()

# 主进程的写入内存后，开了子进程，子进程拷贝了主进程写入内存的值，然后子进程写入自己的内容，强制写入文件后，主进程也执行完成，主进程的内存中的值也写入文件，所以文件内容为123 abc 123
```

```python
import multiprocessing


def task():
    print(name)
    file_object.write("abc\n")
    file_object.flush()


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    
    name = []
    file_object = open('x1.txt', mode='a+', encoding='utf-8')
    file_object.write("123\n")
    file_object.flush()

    p1 = multiprocessing.Process(target=task)
    p1.start()
    
# 主进程的写入文件后，开了子进程，子进程拷贝了主进程写入文件的值，然后子进程写入自己的内容，强制写入文件后，主进程也执行完成，所以文件内容为123 abc
```

```python
import multiprocessing
import threading
import time

def func():
    print("来了")
    with lock:  # 获取锁
        print(666)
        time.sleep(1)

def task():
    # 拷贝的锁也是被申请走的状态
    # 被谁申请走了? 被子进程中的主线程申请走了
    print(lock)
    # 锁子进程中除了主线程，其他的线程
    for i in range(10):
        t = threading.Thread(target=func)
        t.start()
    time.sleep(2)
    lock.release()  # 释放了锁，func函数中锁的代码可以正常执行官


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    name = []
    lock = threading.RLock()
    lock.acquire()
    # print(lock)
    # lock.acquire() # 申请锁
    # print(lock)
    # lock.release()
    # print(lock)
    # lock.acquire()  # 申请锁
    # print(lock)

    p1 = multiprocessing.Process(target=task)
    p1.start()
```

- 主进程没结束：等待子进程结束
- 在pycharm中启动的所有py程序都是pycharm的子进程
- 主进程会等待所有的子进程结束以后才结束，目的是为了回收资源，如果子进程执行结束，主进程没有回收资源，那么这个子进程会变成一个僵尸进程。
#### 10.2.3 常见功能
进程常见方法：

- `p.start()`，当前进程准备就绪，等待被CPU调度（工作单元其实是进程中的线程）。
- `p.join()`，等待当前子进程任务执行完毕后再向下继续执行，执行join方法的效果就是阻塞，直到这个子进程执行结束就结束阻塞

```python
import time
from multiprocessing import Process


def task(arg):
    time.sleep(2)
    print("执行中...")


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    p = Process(target=task, args=('xxx',))
    p.start()
    p.join()

    print("继续执行...")
```

```python
def task():
    print('%s is running, parent is <%s>====%s' % (os.getpid(), os.getppid(), os.getppid()))
    time.sleep(3)
    print('%s is done, parent is <%s>=======%s' % (os.getpid(), os.getppid(), os.getppid()))


if __name__ == '__main__':
    p = Process(target=task,)
    p.start()  # 给操作系统发送一个信号

    p.join()  # 子进程先执行
    print('主流程', os.getpid(), os.getppid())
    print(p.pid)
```

多个子进程：

```python
def task(name, n):
    print('%s is running' % name)
    time.sleep(n)


if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=task, args=('子进程1', 5))
    p2 = Process(target=task, args=('子进程2', 3))
    p3 = Process(target=task, args=('子进程3', 2))
    p4 = Process(target=task, args=('子进程4', 1))

    p_l = [p1, p2, p3, p4]
    for p in p_l:
        p.start()
    for p in p_l:
        p.join()
    print('主进程', (time.time() - start))
```

- 进程名称的设置和获取

```python
import os
import time
import threading
import multiprocessing


def func():
    time.sleep(3)


def task(arg):
    for i in range(10):
        t = threading.Thread(target=func)
        t.start()
    print("子进程：{}".format(os.getpid()), "主进程{}".format(os.getppid()))
    print("线程个数:", len(threading.enumerate()))
    time.sleep(2)
    print("当前进程的名称：", multiprocessing.current_process().name)


if __name__ == '__main__':
    print("主进程{}".format(os.getpid()))
    multiprocessing.set_start_method("spawn")
    p = multiprocessing.Process(target=task, args=('xxx',))
    p.name = "哈哈哈哈"
    p.start()

    print("继续执行...")
```

- 自定义进程类，直接将线程需要做的事写到run方法中

```python
import multiprocessing


class MyProcess(multiprocessing.Process):
    def run(self):
        print('执行此进程', self._args)


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    p = MyProcess(args=('xxx',))
    p.start()
    print("继续执行...")

```

- CPU个数，程序一般创建多少个进程？（利用CPU多核优势）。

```python
import multiprocessing

if __name__ == '__main__':
    count = multiprocessing.cpu_count()
    for i in range(count - 1):
        p = multiprocessing.Process(target=xxxx)
        p.start()
```

#### 10.2.4 守护进程

daemon把进程设置为守护进程

守护进程会在主进程代码执行结束后就终止

- 需要强调的是：运行完毕并非终止运行
- 对主进程来说，运行完毕指的是主进程代码运行完毕
- 主进程在其代码结束后就已经算运行完毕了（守护进程在此时就被回收），然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束

`p.daemon = 布尔值`，守护进程（必须放在start之前）

- `p.daemon =True`，设置为守护进程，主进程执行完毕后，子进程也自动关闭。
- `p.daemon =False`，设置为非守护进程，主进程等待子进程执行完毕后，主进程才结束。

示例一：

```python
from multiprocessing import Process
import time


def task(name):
    print('%s is running' % name)
    time.sleep(2)


if __name__ == '__main__':
    p = Process(target=task, args=('子进程',))
    p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且主进程代码执行结束,p即终止运行
    p.start()

    p.join()  # 等待子进程结束后继续执行
    print('主')  # 只要终端打印出这一行内容，那么守护进程p也就跟着结束掉了
```

示例二：

```python
def Foo():
    print(123)
    time.sleep(1)
    print('end123')


def Bar():
    print(456)
    time.sleep(2)
    print('end456')


if __name__ == '__main__':
    p1 = Process(target=Foo)
    p2 = Process(target=Bar)

    p1.daemon = True
    p1.start()
    p2.start()
    print('main---------')
```

#### 10.2.5 进程之间数据共享

##### 10.2.5.1 共享

进程是资源分配最小单元，每个进程中都维护自己独立的数据，不共享，如果想让他们之间进行共享，可以借助一些特殊的东西来实现。

**Shared memory**

Data can be stored in a shared memory map using [`Value`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Value) or [`Array`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Array). For example, the following code

```
    'c': ctypes.c_char,  'u': ctypes.c_wchar,
    'b': ctypes.c_byte,  'B': ctypes.c_ubyte, 
    'h': ctypes.c_short, 'H': ctypes.c_ushort,
    'i': ctypes.c_int,   'I': ctypes.c_uint,  （其u表示无符号）
    'l': ctypes.c_long,  'L': ctypes.c_ulong, 
    'f': ctypes.c_float, 'd': ctypes.c_double
```

```python
from multiprocessing import Process, Value, Array


def func(n, m1, m2):
    n.value = 888
    m1.value = 'a'.encode('utf-8')
    m2.value = "武"


if __name__ == '__main__':
    num = Value('i', 666)
    v1 = Value('c')
    v2 = Value('u')

    p = Process(target=func, args=(num, v1, v2))
    p.start()
    p.join()

    print(num.value)  # 888
    print(v1.value)  # a
    print(v2.value)  # 武
```

```python
from multiprocessing import Process, Value, Array


def f(data_array):
    data_array[0] = 666


if __name__ == '__main__':
    arr = Array('i', [11, 22, 33, 44]) # 数组：元素类型必须是int; 只能是这么几个数据。

    p = Process(target=f, args=(arr,))
    p.start()
    p.join()

    print(arr[:])
```

**Server process**

A manager object returned by `Manager()` controls a server process which holds Python objects and allows other processes to manipulate them using proxies.

```python
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(666)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list()

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
```

##### 10.2.5.2 交换

进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的。

**创建队列的类（底层就是以管道和锁定的方式实现）**：

```powershell
Queue([maxsize]):创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
```

**参数介绍：**

```powershell
maxsize是队列中允许最大项数，省略则无大小限制。
但需要明确：
    1、队列内存放的是消息而非大数据
    2、队列占用的是内存空间，因而maxsize即便是无大小限制也受限于内存大小
```

**主要方法介绍：**

```powershell
q.put方法用以插入数据到队列中。
q.get方法可以从队列读取并且删除一个元素。
```

**队列的使用**：

```python
from multiprocessing import Process,Queue

q=Queue(3)

#put ,get ,put_nowait,get_nowait,full,empty
q.put(1)
q.put(2)
q.put(3)
print(q.full())  # 判断是否满了
# q.put(4)  # 再放就阻塞住了，卡死

print(q.get())
print(q.get())
print(q.get())
print(q.empty())  # 判断是否空了
# print(q.get())  # 再取就阻塞住了，卡死
```

```python
import multiprocessing


def task(q):
    for i in range(10):
        q.put(i)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    
    p = multiprocessing.Process(target=task, args=(queue,))
    p.start()
    p.join()

    print("主进程")
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
```

**管道的使用：**

```python
import time
import multiprocessing


def task(conn):
    time.sleep(1)
    conn.send([111, 22, 33, 44])
    data = conn.recv() # 阻塞
    print("子进程接收:", data)
    time.sleep(2)


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=task, args=(child_conn,))
    p.start()

    info = parent_conn.recv() # 阻塞
    print("主进程接收：", info)
    parent_conn.send(666)
```

上述都是Python内部提供的进程之间数据共享和交换的机制，作为了解即可，在项目开发中很少使用，后期项目中一般会借助第三方的来做资源的共享，例如：MySQL、redis等。

生产者与消费者模型

**为什么要使用生产者消费者模型**

生产者指的是生产数据的任务，消费者指的是处理数据的任务，在并发编程中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

**什么是生产者和消费者模式**

生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。

- 这个阻塞队列就是用来给生产者和消费者解耦的

```python
from multiprocessing import Process, Queue
import time


def producer(q):
    for i in range(3):
        res = '包子%s' % i
        time.sleep(0.5)
        print('生产者生产了%s' % res)

        q.put(res)


def consumer(q):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(1)
        print('消费者吃了%s' % res)


if __name__ == '__main__':
    # 容器
    q = Queue()

    # 生产者们
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=producer, args=(q,))
    p3 = Process(target=producer, args=(q,))

    # 消费者们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    q.put(None)
    q.put(None)
    print('主')
```

上述再有多个生产者和多个消费者时，我们则需要用一个很low的方式去解决，有几个消费者就需要发送几次结束信号：相当low！

#### 10.2.6 进程锁

如果多个进程抢占式去做某些操作时候，为了防止操作出问题，可以通过进程锁来避免。

互斥锁的原理，就是把并发改成串行，降低了效率，但保证了数据安全不错乱

```python
# 由并发变成了串行,牺牲了运行效率,但避免了竞争
import time
from multiprocessing import Process, Lock


def task(name, mentu):
    mentu.acquire()  # 加锁
    print('%s 1' % name)
    time.sleep(1)
    print('%s 2' % name)
    time.sleep(2)
    print('%s 3' % name)
    time.sleep(3)
    mentu.release()  # 解锁


if __name__ == '__main__':
    mentu = Lock()
    for i in range(3):
        p = Process(target=task, args=('进程%s' % i, mentu))
        p.start()

```

练习一：模拟抢票

```python
# 把文件db.json的内容重置为：{"count":1}

def search(name):
    time.sleep(1)
    dict = json.load(open('db.json', 'r', encoding='utf-8'))
    print('<%s>查看到剩余票数{%s}' % (name, dict['count']))


def get(name):
    time.sleep(1)
    dict = json.load(open('db.json', 'r', encoding='utf-8'))
    if dict['count'] > 0:
        dict['count'] -= 1
        json.dump(dict, open('db.json', 'w', encoding='utf-8'))
        print('<%s> 购票成功!' % name)
    else:
        print('没有足够的票!')


def task(name, mutex):
    search(name)
    with mutex:  # 相当于lock.acquire(),执行完自代码块自动执行lock.release()
        get(name)


if __name__ == '__main__':
    mutex = Lock()
    for i in range(10):  # 模拟10个人并发抢票
        p = Process(target=task, args=('路人%s' % i, mutex))
        p.start()
```

1. 在数据安全的基础上,才考虑效率问题
2. 同步存在的意义：数据的安全性
3. 在主进程中实例化 mutex = Lock()
4. 把这个锁传递给子进程
5. 在子进程中，对需要加锁的代码进行 with lock:with lock相当于lock.acquire()和lock.release
6. 在进程中需要加锁的场景:
    1. 共享的数据资源(文件，数据库)
    2. 对资源进行修改，删除操作
7. 加锁之后能保证数据的安全性，但是也降低了程序的执行效率

互斥锁与join的区别：

- 互斥锁和join都是把并发变成串行
- join是把所有的代码都变成串行，互斥锁是把部分的代码变成串行

练习二：模拟抢票

```python
import time
import multiprocessing


def task(lock):
    print("开始")
    lock.acquire()
    # 假设文件中保存的内容就是一个值：10
    with open('f1.txt', mode='r', encoding='utf-8') as f:
        current_num = int(f.read())

    print("排队抢票了")
    time.sleep(0.5)
    current_num -= 1

    with open('f1.txt', mode='w', encoding='utf-8') as f:
        f.write(str(current_num))
    lock.release()


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    
    lock = multiprocessing.RLock() # 进程锁
    
    for i in range(10):
        p = multiprocessing.Process(target=task, args=(lock,))
        p.start()

    # spawn模式，需要特殊处理。
    time.sleep(7)


```

```python
import time
import multiprocessing
import os


def task(lock):
    print("开始")
    lock.acquire()
    # 假设文件中保存的内容就是一个值：10
    with open('f1.txt', mode='r', encoding='utf-8') as f:
        current_num = int(f.read())

    print(os.getpid(), "排队抢票了")
    time.sleep(0.5)
    current_num -= 1

    with open('f1.txt', mode='w', encoding='utf-8') as f:
        f.write(str(current_num))
    lock.release()


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    lock = multiprocessing.RLock()

    process_list = []
    for i in range(10):
        p = multiprocessing.Process(target=task, args=(lock,))
        p.start()
        process_list.append(p)

    # spawn模式，需要特殊处理。
    for item in process_list:
        item.join()
```

```python
import time
import multiprocessing

def task(lock):
    print("开始")
    lock.acquire()
    # 假设文件中保存的内容就是一个值：10
    with open('f1.txt', mode='r', encoding='utf-8') as f:
        current_num = int(f.read())

    print("排队抢票了")
    time.sleep(1)
    current_num -= 1

    with open('f1.txt', mode='w', encoding='utf-8') as f:
        f.write(str(current_num))
    lock.release()


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')
    lock = multiprocessing.RLock()
    for i in range(10):
        p = multiprocessing.Process(target=task, args=(lock,))
        p.start()
```

#### 10.2.7 进程池

```python
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def task(num):
    print("执行", num)
    time.sleep(2)


if __name__ == '__main__':
    # 修改模式
    pool = ProcessPoolExecutor(4)
    for i in range(10):
        pool.submit(task, i)
	print(1)
	print(2)
```

```python
from concurrent.futures import ProcessPoolExecutor
import time


def task(num):
    print("执行", num)
    time.sleep(2)


if __name__ == '__main__':

    pool = ProcessPoolExecutor(4)
    for i in range(10):
        pool.submit(task, i)
    # 等待进程池中的任务都执行完毕后，再继续往后执行。
    pool.shutdown(True)
    print(1)
```

```python
import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing


def task(num):
    print("执行", num)
    time.sleep(2)
    return num


def done(res):
    print(multiprocessing.current_process())
    time.sleep(1)
    print(res.result())
    time.sleep(1)


if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    for i in range(50):
        fur = pool.submit(task, i)
        fur.add_done_callback(done)  # done的调用由主进程处理（与线程池不同）

    print(multiprocessing.current_process())
    pool.shutdown(True)

```

注意：如果在进程池中要使用进程锁，则需要基于Manager中的Lock和RLock来实现。

```python
import time
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor


def task(lock):
    print("开始")
    # lock.acquire()
    # lock.relase()
    with lock:
        # 假设文件中保存的内容就是一个值：10
        with open('f1.txt', mode='r', encoding='utf-8') as f:
            current_num = int(f.read())

        print("排队抢票了")
        time.sleep(1)
        current_num -= 1

        with open('f1.txt', mode='w', encoding='utf-8') as f:
            f.write(str(current_num))


if __name__ == '__main__':
    pool = ProcessPoolExecutor()
    # lock_object = multiprocessing.RLock() # 不能使用
    manager = multiprocessing.Manager()
    lock_object = manager.RLock() # Lock
    for i in range(10):
        pool.submit(task, lock_object)
```

**案例：计算每天用户访问情况。**

![image-20210326132114601](J:\homework\Python学习笔记\Python_notes.assets\image-20210326132114601.png)

示例一：

```python
import os
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager


def task(file_name, count_dict):
    ip_set = set()
    total_count = 0
    ip_count = 0
    file_path = os.path.join("files", file_name)
    file_object = open(file_path, mode='r', encoding='utf-8')
    for line in file_object:
        if not line.strip():
            continue
        user_ip = line.split(" - -", maxsplit=1)[0].split(",")[0]
        total_count += 1
        if user_ip in ip_set:
            continue
        ip_count += 1
        ip_set.add(user_ip)
    count_dict[file_name] = {"total": total_count, 'ip': ip_count}
    time.sleep(1)


def run():
    # 根据目录读取文件并初始化字典
    """
        1.读取目录下所有的文件，每个进程处理一个文件。
    """

    pool = ProcessPoolExecutor(4)
    with Manager() as manager:
        """
        count_dict={
        	"20210322.log":{"total":10000,'ip':800},
        }
        """
        count_dict = manager.dict()
        
        for file_name in os.listdir("files"):
            pool.submit(task, file_name, count_dict)
            
            
        pool.shutdown(True)
        for k, v in count_dict.items():
            print(k, v)


if __name__ == '__main__':
    run()
```

示例二：

```python
import os
import time
from concurrent.futures import ProcessPoolExecutor


def task(file_name):
    ip_set = set()
    total_count = 0
    ip_count = 0
    file_path = os.path.join("files", file_name)
    file_object = open(file_path, mode='r', encoding='utf-8')
    for line in file_object:
        if not line.strip():
            continue
        user_ip = line.split(" - -", maxsplit=1)[0].split(",")[0]
        total_count += 1
        if user_ip in ip_set:
            continue
        ip_count += 1
        ip_set.add(user_ip)
    time.sleep(1)
    return {"total": total_count, 'ip': ip_count}


def outer(info, file_name):
    def done(res, *args, **kwargs):
        info[file_name] = res.result()

    return done


def run():
    # 根据目录读取文件并初始化字典
    """
        1.读取目录下所有的文件，每个进程处理一个文件。
    """
    info = {}
    
    pool = ProcessPoolExecutor(4)

    for file_name in os.listdir("files"):
        fur = pool.submit(task, file_name)
        fur.add_done_callback(  outer(info, file_name)  ) # 回调函数：主进程

    pool.shutdown(True)
    for k, v in info.items():
        print(k, v)


if __name__ == '__main__':
    run()
```

### 10.3 线程

#### 10.3.1 线程概念

进程只是用来把资源集中到一起（进程只是一个资源单位，或者说资源集合），而线程才是cpu上的执行单位。

线程的特点：

> 线程，是计算机中可以被cpu调度的最小单元（真正在工作）。
> 进程，是计算机资源分配的最小单元（进程为线程提供资源）。
>
> 一个进程中可以有多个线程同一个进程中的线程可以共享此进程中的资源。

线程的开销：

- 线程的创建,也需要一些开销(一个存储局部变量的结构,记录状态)
    - 线程的创建、切换和销毁开销远远小于进程
    - 进程：数据隔离， 开销大，同时执行几段代码
    - 线程：数据共享，开销小，同时执行几段代码

类比：

- 一个**工厂**，至少有一个**车间**，一个车间中至少有一个**工人**，最终是工人在工作。

- 一个**程序**，至少有一个**进程**，一个进程中至少有一个**线程**，最终是线程在工作。

```powershell
上述串行的代码示例就是一个程序，在使用python xx.py 运行时，内部就创建一个进程（主进程），在进程中创建了一个线程（主线程），由线程逐行运行代码。
```

**1. 多线程：**

基于多线程对上述串行示例进行优化：

- 一个**工厂**，创建一个**车间**，这个车间中创建 **3个工人**，并行处理任务。
- 一个**程序**，创建一个**进程**，这个进程中创建 **3个线程**，并行处理任务。

```python
import time
import requests

url_list = [
    ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
    ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
    ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
]

for file_name, url in url_list:
    res = requests.get(url)
    with open(file_name, mode='wb') as f:
        f.write(res.content)
```

```python
import time
import requests
import threading
"""
def func(a1,a2,a3):
    pass

t = threaing.Thread(target=func,args=(11,22,33))
t.start()
"""

url_list = [
    ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
    ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
    ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
]


def task(file_name, video_url):
    res = requests.get(video_url)
    with open(file_name, mode='wb') as f:
        f.write(res.content)
    print(time.time())


for name, url in url_list:
    # 创建线程，让每个线程都去执行task函数（参数不同）
    t = threading.Thread(target=task, args=(name, url))
    t.start()
```

**2. 多进程：**

基于多进程对上述串行示例进行优化：

- 一个**工厂**，创建 **三个车间**，每个车间 **一个工人（共3人）**，并行处理任务。
- 一个**程序**，创建 **三个进程**，每个进程 **一个线程（共3人）**，并行处理任务。

```python
import time
import requests
import multiprocessing

# 进程创建之后，在进程中还会创建一个线程。
# t = multiprocessing.Process(target=函数名, args=(name, url))
# t.start()
    
    

url_list = [
    ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
    ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
    ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
]


def task(file_name, video_url):
    res = requests.get(video_url)
    with open(file_name, mode='wb') as f:
        f.write(res.content)
    print(time.time())


if __name__ == '__main__':
    print(time.time())
    for name, url in url_list:
        t = multiprocessing.Process(target=task, args=(name, url))
        t.start()
```

综上所述，大家会发现 **多进程** 的开销比 **多线程** 的开销大。那是不是使用多线程要比多进程更好呀？

接下来，给大家再来介绍一个Python内置的GIL锁的知识，然后再根据 进程 和 线程 各自的特点总结各自适合应用场景。

**开启线程的两种方式：**

方式一：

```python
import time
import random
from threading import Thread


def piao(name):
    print('%s piaoing' % name)
    time.sleep(random.randrange(1, 5))
    print('%s piao end' % name)


if __name__ == '__main__':
    t1 = Thread(target=piao, args=('ike',))
    t1.start()
    print('主线程')
```

方式二：面向对象

```python
import time
import random
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s piaoing' % self.name)
        time.sleep(random.randrange(1, 5))
        print('%s piao end' % self.name)


if __name__ == '__main__':
    t1 = MyThread('ike')
    t1.start()
    print('主') 
```

#### 10.3.2 进程与线程的区别

1. 同一个进程内的多个线程共享该进程内的地址空间
2. 创建线程的开销要远小于创建进程的开销（创建一个进程，就是创建一个车间，涉及到申请空间，而且在该空间内建至少一条流水线，但创建线程，就只是在一个车间内造一条流水线，无需申请空间，所以创建开销小）

**开进程的开销远大于开线程：**

1.主进程下开子进程：

```python
import time
from multiprocessing import Process


def piao(name):
    print('%s running' % name)
    time.sleep(2)
    print('%s running end' % name)


if __name__ == '__main__':
    p1=Process(target=piao,args=('ike',))
    p1.start()
    print('主进程')
    
'''执行结果：
主进程
ike running
ike running end
'''
```

备注：p.start ()将开启进程的信号发给操作系统后，操作系统要申请内存空间，然后拷贝父进程地址空间到子进程，开销远大于线程

2.主线程下开子线程：

```python
import time
from threading import Thread

def piao(name):
    print('%s running' % name)
    time.sleep(2)
    print('%s running end' % name)


if __name__ == '__main__':
    t1 = Thread(target=piao, args=('ike',))
    t1.start()
    print('主线程')
    
'''执行结果：
ike running
主线程
ike running end
'''
```

备注：几乎是t.start ()同时就将线程开启了，然后先打印出了ike running，证明线程的创建开销极小

示例：同一进程内的多个线程共享该进程的地址空间

**进程与线程的地址空间：**

1.进程之间的地址空间是隔离的：

```python
from multiprocessing import Process

n = 100

def task():
    global n
    n = 0
    print(n)

if __name__ == '__main__':
    p1=Process(target=task,)
    p1.start()
    p1.join()

    print('主进程', n)
```

备注：进程p已经将自己的全局的n改成了0，但改的仅仅是它自己的，查看父进程的n仍然为100

2.同一进程内开启的多个线程是共享该进程地址空间的：

```python
from threading import Thread

n = 100

def task():
    global n
    n = 0

    
if __name__ == '__main__':
    t1 = Thread(target=task, )
    t1.start()
    t1.join()

    print('主线程', n)

```

备注： 查看结果为0，因为同一进程内的线程之间共享进程内的数据

**进程与线程的PID：**

1.开启多个进程，每个进程的PID都不一样：

```python
from multiprocessing import Process, current_process
import os


def task():
    # print(current_process().pid)
    print('子进程PID:%s  父进程的PID:%s' % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    p1 = Process(target=task, )
    p1.start()

    # print('主线程',current_process().pid)
    print('主线程PID:', os.getpid())
    
    
'''
结果：
主线程PID: 9996
子进程PID: 8900  父进程的PID: 9996
'''
```

备注：主进程和子进程不属于同一个进程

2.在主进程下开启多个线程，每个线程都跟主进程的PID一样：

```python
from threading import Thread
import os


def task():
    print('子线程PID: %s' % (os.getpid()))


if __name__ == '__main__':
    t1 = Thread(target=task, )
    t1.start()

    print('主线程PID:', os.getpid())
    
    
'''
结果：
子线程PID: 9528
主线程PID: 9528
'''
```

备注：因为他们同属于一个进程

#### 10.3.3 Thread对象的其他属性

- getName()：获取线程名
- setName()：设置线程名
- is_alive()：查看线程是否存活
- active_count()：获取线程活跃数
- enumerate()：当前活跃的线程对象
- currentThread()：获取当前的线程变量

示例：

```python
from threading import Thread, currentThread, active_count, enumerate
import time


def task():
    print('%s is running ' % currentThread().getName())
    time.sleep(2)
    print('%s is done ' % currentThread().getName())


if __name__ == '__main__':
    t = Thread(target=task, name='子线程')
    t.start()

    # 设置子线程名字， 默认Thread-1
    t.setName('儿子线程')

    # 设置主线程名字，默认MainThread
    currentThread().setName('主线程1')

    # 查看线程是否存活
    t.join()  # 执行这行代码后，线程已运行完，返回就是False
    print(t.is_alive())

    # 线程活跃数
    print(active_count())

    # 当前活跃的线程对象
    print(enumerate())

    # 当前的线程变量
    print('主线程', currentThread())
    print('主线程', currentThread().getName())
```

#### 10.3.4 守护线程

守护线程会在主线程代码执行结束后就终止

- 需要强调的是：运行完毕并非终止运行
    - 对主进程来说，运行完毕指的是主进程代码运行完毕
    - 对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程全部运行完毕，主线程才算运行完毕
    - 主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束

- `t.setDaemon(布尔值)` ，守护线程（必须放在start之前）
  - `t.setDaemon(True)`，设置为守护线程，主线程执行完毕后，子线程也自动关闭。
  - `t.setDaemon(False)`，设置为非守护线程，主线程等待子线程，子线程执行完毕后，主线程才结束。（默认）

示例一：

```python
from threading import Thread
import time


def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)


if __name__ == '__main__':
    t = Thread(target=sayhi, args=('egon',))
    # 必须在t.start()之前设置  同等于 t.daemon = True
    t.setDaemon(True)
    t.start()

    print('主线程')
    print(t.is_alive())
```

示例二：

```python
from threading import Thread
import time


def Foo():
    print(123)
    time.sleep(1)
    print('end123')


def Bar():
    print(456)
    time.sleep(2)
    print('end456')


if __name__ == '__main__':
    p1 = Thread(target=Foo)
    p2 = Thread(target=Bar)

    p1.daemon = True
    p1.start()
    p2.start()
    print('main---------')
```

因为非守护线程没有运行完，所以打印了end123

#### 10.3.5 GIL解释器锁

##### 10.3.5.1 GIL锁介绍

GIL本质就是一把互斥锁，既然是互斥锁，所有互斥锁的本质都一样，都是将并发运行变成串行，以此来控制同一时间内共享数据只能被一个任务所修改，进而保证数据安全。

GIL全局解释器锁（Global Interpreter Lock），是CPython解释器特有一个玩意，让一个进程中同一个时刻只能有一个线程可以被CPU调用。

![1644832594283](J:\homework\Python学习笔记\Python_notes.assets\1644832594283.png)

如果程序想利用 计算机的多核优势，让CPU同时处理一些任务，适合用多进程开发（即使资源开销大）。

![1644832641686](J:\homework\Python学习笔记\Python_notes.assets\1644832641686.png)

如果程序不利用 计算机的多核优势，适合用多线程开发。

![1644832724915](J:\homework\Python学习笔记\Python_notes.assets\1644832724915.png)

常见的程序开发中，计算操作需要使用CPU多核优势，IO操作不需要利用CPU的多核优势，所以，就有这一句话：

- 计算密集型，用多进程，例如：大量的数据计算【累加计算示例】。
- IO密集型，用多线程，例如：文件读写、网络数据传输【下载抖音视频示例】。

累加计算示例（计算密集型）：

- 串行处理

  ```python
  import time
  
  start = time.time()
  
  result = 0
  for i in range(100000000):
      result += i
  print(result)
  
  end = time.time()
  
  print("耗时：", end - start) # 耗时： 9.522780179977417
  ```

- 多进程处理

  ```python
  import time
  import multiprocessing
  
  
  def task(start, end, queue):
      result = 0
      for i in range(start, end):
          result += i
      queue.put(result)
  
  
  if __name__ == '__main__':
      queue = multiprocessing.Queue()
  
      start_time = time.time()
  
      p1 = multiprocessing.Process(target=task, args=(0, 50000000, queue))
      p1.start()
  
      p2 = multiprocessing.Process(target=task, args=(50000000, 100000000, queue))
      p2.start()
  
      v1 = queue.get(block=True) #阻塞
      v2 = queue.get(block=True) #阻塞
      print(v1 + v2)
  
      end_time = time.time()
  
      print("耗时:", end_time - start_time) # 耗时: 2.6232550144195557
  ```


当然，在程序开发中 多线程 和 多进程 是可以结合使用，例如：创建2个进程（建议与CPU个数相同），每个进程中创建3个线程。

```python
import multiprocessing
import threading


def thread_task():
    pass


def task(start, end):
    t1 = threading.Thread(target=thread_task)
    t1.start()

    t2 = threading.Thread(target=thread_task)
    t2.start()

    t3 = threading.Thread(target=thread_task)
    t3.start()


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task, args=(0, 50000000))
    p1.start()

    p2 = multiprocessing.Process(target=task, args=(50000000, 100000000))
    p2.start()
```

##### 10.3.5.2 多线程开发

```python
import threading

def task(arg):
	pass


# 创建一个Thread对象（线程），并封装线程被CPU调度时应该执行的任务和相关参数。
t = threading.Thread(target=task,args=('xxx',))
# 线程准备就绪（等待CPU调度），代码继续向下执行。
t.start()

print("继续执行...") # 主线程执行完所有代码，不结束（等待子线程）
```

线程的常见方法：

- `t.start()`，当前线程准备就绪（等待CPU调度，具体时间是由CPU来决定）。

  ```python
  import threading
  
  loop = 10000000
  number = 0
  
  def _add(count):
      global number
      for i in range(count):
          number += 1
  
  t = threading.Thread(target=_add,args=(loop,))
  t.start()
  
  print(number)
  ```

- `t.join()`，等待当前线程的任务执行完毕后再向下继续执行。

  ```python
  import threading
  
  number = 0
  
  def _add():
      global number
      for i in range(10000000):
          number += 1
  
  t = threading.Thread(target=_add)
  t.start()
  
  t.join() # 主线程等待中...
  
  print(number)
  ```

  ```python
  import threading
  
  number = 0
  
  
  def _add():
      global number
      for i in range(10000000):
          number += 1
  
  
  def _sub():
      global number
      for i in range(10000000):
          number -= 1
  
  
  t1 = threading.Thread(target=_add)
  t2 = threading.Thread(target=_sub)
  t1.start()
  t1.join()  # t1线程执行完毕,才继续往后走
  t2.start()
  t2.join()  # t2线程执行完毕,才继续往后走
  
  print(number)
  
  ```

  ```python
  import threading
  
  loop = 10000000
  number = 0
  
  
  def _add(count):
      global number
      for i in range(count):
          number += 1
  
  
  def _sub(count):
      global number
      for i in range(count):
          number -= 1
  
  
  t1 = threading.Thread(target=_add, args=(loop,))
  t2 = threading.Thread(target=_sub, args=(loop,))
  t1.start()
  t2.start()
  
  t1.join()  # t1线程执行完毕,才继续往后走
  t2.join()  # t2线程执行完毕,才继续往后走
  
  print(number)
  ```

- `t.setDaemon(布尔值)` ，守护线程（必须放在start之前）

  - `t.setDaemon(True)`，设置为守护线程，主线程执行完毕后，子线程也自动关闭。
  - `t.setDaemon(False)`，设置为非守护线程，主线程等待子线程，子线程执行完毕后，主线程才结束。（默认）

  ```python
  import threading
  import time
  
  def task(arg):
      time.sleep(5)
      print('任务')
  
  t = threading.Thread(target=task, args=(11,))
  t.setDaemon(True) # True/False
  t.start()
  
  print('END')
  ```

- 线程名称的设置和获取

  ```python
  import threading
  
  
  def task(arg):
      # 获取当前执行此代码的线程
      name = threading.current_thread().getName()
      print(name)
  
  
  for i in range(10):
      t = threading.Thread(target=task, args=(11,))
      t.setName('日魔-{}'.format(i))
      t.start()
  ```

- 自定义线程类，直接将线程需要做的事写到run方法中。

  ```python
  import threading
  
  
  class MyThread(threading.Thread):
      def run(self):
          print('执行此线程', self._args)
  
  
  t = MyThread(args=(100,))
  t.start()
  ```

  ```python
  import requests
  import threading
  
  
  class DouYinThread(threading.Thread):
      def run(self):
          file_name, video_url = self._args
          res = requests.get(video_url)
          with open(file_name, mode='wb') as f:
              f.write(res.content)
  
  
  url_list = [
      ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
      ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
      ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
  ]
  for item in url_list:
      t = DouYinThread(args=(item[0], item[1]))
      t.start()
  
  ```

##### 10.3.5.3 线程安全

一个进程中可以有多个线程，且线程共享所有进程中的资源。

多个线程同时去操作一个"东西"，**可能**会存在数据混乱的情况，例如：

- 示例1

  ```python
  import threading
  
  loop = 10000000
  number = 0
  
  
  def _add(count):
      global number
      for i in range(count):
          number += 1
  
  
  def _sub(count):
      global number
      for i in range(count):
          number -= 1
  
  
  t1 = threading.Thread(target=_add, args=(loop,))
  t2 = threading.Thread(target=_sub, args=(loop,))
  t1.start()
  t2.start()
  
  t1.join()  # t1线程执行完毕,才继续往后走
  t2.join()  # t2线程执行完毕,才继续往后走
  
  print(number)
  ```

  ```python
  import threading
  
  lock_object = threading.RLock()
  
  loop = 10000000
  number = 0
  
  
  def _add(count):
      lock_object.acquire() # 加锁
      global number
      for i in range(count):
          number += 1
      lock_object.release() # 释放锁
  
  
  def _sub(count):
      lock_object.acquire() # 申请锁（等待）
      global number
      for i in range(count):
          number -= 1
      lock_object.release() # 释放锁
  
  
  t1 = threading.Thread(target=_add, args=(loop,))
  t2 = threading.Thread(target=_sub, args=(loop,))
  t1.start()
  t2.start()
  
  t1.join()  # t1线程执行完毕,才继续往后走
  t2.join()  # t2线程执行完毕,才继续往后走
  
  print(number)
  
  ```

- 示例2：

  ```python
  import threading
  
  num = 0
  
  def task():
      global num
      for i in range(1000000):
          num += 1
      print(num)
  
  
  for i in range(2):
      t = threading.Thread(target=task)
      t.start()
  ```

  ```python
  import threading
  
  num = 0
  lock_object = threading.RLock()
  
  
  def task():
      print("开始")
      lock_object.acquire()  # 第1个抵达的线程进入并上锁，其他线程就需要再此等待。
      global num
      for i in range(1000000):
          num += 1
      lock_object.release()  # 线程出去，并解开锁，其他线程就可以进入并执行了
      print(num)
  
  
  for i in range(2):
      t = threading.Thread(target=task)
      t.start()
  ```

  ```python
  import threading
  
  num = 0
  lock_object = threading.RLock()
  
  
  def task():
      print("开始")
      with lock_object: # 基于上下文管理，内部自动执行 acquire 和 release
          global num
          for i in range(1000000):
              num += 1
      print(num)
  
  
  for i in range(2):
      t = threading.Thread(target=task)
      t.start()
  ```


在开发的过程中要注意有些操作默认都是 线程安全的（内部集成了锁的机制），我们在使用的时无需再通过锁再处理，例如：

```python
import threading

data_list = []

lock_object = threading.RLock()


def task():
    print("开始")
    for i in range(1000000):
        data_list.append(i)
    print(len(data_list))


for i in range(2):
    t = threading.Thread(target=task)
    t.start()
```

![image-20210225102151570](J:\homework\Python学习笔记\Python_notes.assets\image-20210225102151570.png)

所以，要多注意看一些开发文档中是否标明线程安全。

每次执行python程序，都会产生一个独立的进程。例如python test.py，python aaa.py，python bbb.py会产生3个不同的python进程。

示例：

```python
# test.py内容
import os,time
print(os.getpid())
time.sleep(1000)

# 打开终端执行
python3 test.py

# 在windows下查看
tasklist |findstr python

# 在linux下下查看
ps aux |grep python
```

在一个python进程内，不仅有自己编写代码开启的主线程或由该线程开启的其他线程，另外还有解释器开启的垃圾回收等解释器级别的线程，总之，所有线程都是运行在这一个进程内。

- 所有数据都是共享的，这其中代码作为一种数据也是被所有线程共享的
    - 自己写的代码
    - Cpython解释器的代码
- 所有线程任务，都需要将代码当做参数传递给解释器的代码去执行，即所有的线程想要运行自己的任务，首先要解决的问题是能访问到解释器的代码

案例：

解释器的代码是所有线程共享的，所有Cpython垃圾回收线程也可能访问到解释器代码而去执行，这样就会导致一个问题：

- 相对于同一个数据，比如：100
- 开启多个线程：线程1执行x=100，而Cpython垃圾回收线程执行的回收的操作，这样就会冲突

解决这个问题就是加GIL锁处理，保证python解释器同一时间只能执行一个任务的代码，如图：

![1643078259276](J:\homework\Python学习笔记\Python_notes.assets\1643078259276.png)

##### 10.3.5.4 线程锁

共同点：将并发运行变成串行，锁的目的是为了保护共享的数据，同一时间只能有一个线程来修改共享的数据。

结论：保护不同的数据就应该加不同的锁。

总结：GIL 与Lock是两把锁Lock 和 RLock。，保护的数据不一样

- GIL是解释器级别的，保护的就是解释器级别的数据，比如垃圾回收的数据
- Lock保护自己开发的程序的数据，分工明确
- 所以GIL不负责自己开发的程序的数据，只能由自己去加锁处理

分析：

1. GIL锁相当于一个权限，比如有10个线程，自己写的程序有加了lock锁
2. 这10个线程都去抢GIL锁，肯定有一个1抢到，比如线程1，即拿到权限，然后去执行，执行就会拿到lock.acquire()
3. 很有可能由于各种因素，线程1还未执行完毕就被线程2抢到权限了，然后线程2执行，然后线程2发现lock锁还在线程1那，还没释放，所以就阻塞了，被迫线程2交出权限，即释放GIL
4. 线程1又夺回权限，开始上一次暂停的位置继续执行，直到lock锁被释放lock.release()
5. 其他的线程重复执行这一系列的步骤

- Lock，同步锁。

  ```python
  import threading
  
  num = 0
  lock_object = threading.Lock()
  
  
  def task():
      print("开始")
      lock_object.acquire()  # 第1个抵达的线程进入并上锁，其他线程就需要再此等待。
      global num
      for i in range(1000000):
          num += 1
      lock_object.release()  # 线程出去，并解开锁，其他线程就可以进入并执行了
      
      print(num)
  
  
  for i in range(2):
      t = threading.Thread(target=task)
      t.start()
  
  ```

- RLock，递归锁。

  ```python
  import threading
  
  num = 0
  lock_object = threading.RLock()
  
  
  def task():
      print("开始")
      lock_object.acquire()  # 第1个抵达的线程进入并上锁，其他线程就需要再此等待。
      global num
      for i in range(1000000):
          num += 1
      lock_object.release()  # 线程出去，并解开锁，其他线程就可以进入并执行了
      print(num)
  
  
  for i in range(2):
      t = threading.Thread(target=task)
      t.start()
  ```

#### 10.3.6 死锁与递归锁

##### 10.3.6.1 死锁

是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，这些永远在互相等待的进程称为死锁进程。

互斥锁只能acquire一次，只有释放了这次才能进行继续进行下去。

死锁示例：

```python
import threading

num = 0
lock_object = threading.Lock()


def task():
    print("开始")
    lock_object.acquire()  # 第1个抵达的线程进入并上锁，其他线程就需要再此等待。
    lock_object.acquire()  # 第1个抵达的线程进入并上锁，其他线程就需要再此等待。
    global num
    for i in range(1000000):
        num += 1
    lock_object.release()  # 线程出去，并解开锁，其他线程就可以进入并执行了
    lock_object.release()  # 线程出去，并解开锁，其他线程就可以进入并执行了
    
    print(num)


for i in range(2):
    t = threading.Thread(target=task)
    t.start()
```

```python
import threading
import time 

lock_1 = threading.Lock()
lock_2 = threading.Lock()


def task1():
    lock_1.acquire()
    time.sleep(1)
    lock_2.acquire()
    print(11)
    lock_2.release()
    print(111)
    lock_1.release()
    print(1111)


def task2():
    lock_2.acquire()
    time.sleep(1)
    lock_1.acquire()
    print(22)
    lock_1.release()
    print(222)
    lock_2.release()
    print(2222)


t1 = threading.Thread(target=task1)
t1.start()

t2 = threading.Thread(target=task2)
t2.start()
```

##### 10.3.6.2 递归锁

在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock。

RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require，直到一个线程所有的acquire都被release，其他的线程才能获得资源。

递归锁与互斥锁的区别：

- 递归锁可以连续acquire多次
- 互斥锁只能acquire一次

RLock支持多次申请锁和多次释放，Lock不支持。例如：

```python
import threading
import time

lock_object = threading.RLock()


def task():
    print("开始")
    lock_object.acquire()
    lock_object.acquire()
    print(123)
    lock_object.release()
    lock_object.release()


for i in range(3):
    t = threading.Thread(target=task)
    t.start()
```

```python
import threading
lock = threading.RLock()

# 程序员A开发了一个函数，函数可以被其他开发者调用，内部需要基于锁保证数据安全。
def func():
	with lock:
		pass
        
# 程序员B开发了一个函数，可以直接调用这个函数。
def run():
    print("其他功能")
    func() # 调用程序员A写的func函数，内部用到了锁。
    print("其他功能")
    
# 程序员C开发了一个函数，自己需要加锁，同时也需要调用func函数。
def process():
    with lock:
		print("其他功能")
        func() # ----------------> 此时就会出现多次锁的情况，只有RLock支持（Lock不支持）。
		print("其他功能")
```

#### 10.3.7 信号量

信号量也是一把锁，信号量可以指定一个数，比如：5

互斥锁与信号量对比：

- 互斥锁同一时间只能有一个任务去抢到锁执行
- 信号量是根据指定的数的任务去抢锁执行

示例：

```python
from threading import Thread, Semaphore, currentThread
import time, random

# 管理一个内置的计数器
sm = Semaphore(3)

# 计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()
def task():
    
    # 每当调用acquire()时内置计数器-1
    # sm.acquire()
    # print('%s in' %currentThread().getName())

    # 调用release() 时内置计数器+1
    # sm.release()
    with sm:
        print('%s in' % currentThread().getName())
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task)
        t.start()
```

#### 10.3.8 Even事件

Python提供了Event对象用于线程间通信，它是由线程设置的信号标志，在初始情况下，Event对象中的信号标志被设置为假，如果有线程等待一个Event对象, 而这个Event对象的标志为假，那么这个线程将会被一直阻塞直至该标志为真。一个线程如果将一个Event对象的信号标志设置为真,它将唤醒所有等待这个Event对象的线程。

```python
from threading import Event

event.isSet()：返回event的状态值；

event.wait()：如果 event.isSet()==False将阻塞线程；

event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；

event.clear()：恢复event的状态值为False。
```

示例一：学生上课

```python
from threading import Thread, Event
import time

event = Event()


# event.wait()
# event.set()


def student(name):
    print('学生%s 正在听课' % name)
    event.wait(0.5)
    print('学生%s 课间活动' % name)


def teacher(name):
    print('老师%s 正在授课' % name)
    time.sleep(3)
    event.set()


if __name__ == '__main__':
    stu1 = Thread(target=student, args=('Python',))
    stu2 = Thread(target=student, args=('PHP',))
    stu3 = Thread(target=student, args=('Java',))
    t1 = Thread(target=teacher, args=('Go',))

    stu1.start()

    stu2.start()
    stu3.start()
    t1.start()
```

示例二：数据库验证

```python
from threading import Thread, Event, currentThread
import time

event = Event()


def conn():
    n = 0
    while not event.is_set():
        if n == 3:
            print('%s try too many times' % currentThread().getName())
            return
        print('%s try %s' % (currentThread().getName(), n))
        event.wait(0.5)
        n += 1

    print('%s is connected' % currentThread().getName())


def check():
    print('%s is checking' % currentThread().getName())
    time.sleep(5)
    event.set()


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=conn)
        t.start()
    t = Thread(target=check)
    t.start()
```

#### 10.3.9 计时器

这个类实现了隔一段调用函数，在Timer调用的函数中，进行设置。Timer是Thread的一个派生类。

示例：验证码更新验证功能

```python
from threading import Timer
import random


class Code:
    def __init__(self):
        self.make_cache()

    def make_cache(self, interval=5):
        self.cache = self.make_code()
        print(self.cache)
        self.t = Timer(interval, self.make_cache)
        self.t.start()

    def make_code(self, n=4):
        res = ''
        for i in range(n):
            s1 = str(random.randint(0, 9))
            s2 = chr(random.randint(65, 90))
            res += random.choice([s1, s2])
        return res

    def check(self):
        while True:
            code = input('请输入你的验证码>>: ').strip()
            if code.upper() == self.cache:
                print('验证码输入正确')
                self.t.cancel()
                break


obj = Code()
obj.check()
```

#### 10.3.10 线程队列

三种不同的用法：

先进先出：queue.Queue

```python
import queue

q = queue.Queue(3)  # 先进先出->队列

q.put('first')
q.put(2)
q.put('third')
# q.put(4, block=False)  # 等同于q.put_nowait(4)
# q.put(4, block=True, timeout=3)  # block默认为True

print(q.get())
print(q.get())
print(q.get())
# print(q.get(block=False))  # 等同于q.get_nowait()

print(q.get(block=True, timeout=3))

```

堆栈--先进后出：queue.LifoQueue

```python
import queue
q = queue.LifoQueue(3)  # 后进先出->堆栈
q.put('first')
q.put(2)
q.put('third')

print(q.get())
print(q.get())
print(q.get())
```

优先级队列：queue.PriorityQueue

```python
import queue

q = queue.PriorityQueue(3)  # 优先级队列

q.put((10, 'one'))
q.put((40, 'two'))
q.put((30, 'three'))

print(q.get())
print(q.get())
print(q.get())
```

备注：存储数据时可设置优先级的队列

#### 10.3.11 进程池与线程池

基于多进程或多线程实现并发的套接字通信，这种实现方式的致命缺陷是：服务的开启的进程数或线程数都会随着并发的客户端数目地增多而增多，这会对服务端主机带来巨大的压力，甚至于不堪重负而瘫痪。于是我们必须对服务端开启的进程数或线程数加以控制，让机器在一个自己可以承受的范围内运行，这就是进程池或线程池的用途。例如进程池，就是用来存放进程的池子，本质还是基于多进程，只不过是对开启进程的数目加上了限制。

```powershell
ThreadPoolExecutor：线程池，提供异步调用
ProcessPoolExecutor: 进程池，提供异步调用
```

基本方法：

```powershell
1、submit(fn, *args, **kwargs)
异步提交任务

2、map(func, *iterables, timeout=None, chunksize=1) 
取代for循环submit的操作

3、shutdown(wait=True) 
相当于进程池的pool.close()+pool.join()操作
wait=True，等待池内所有任务执行完毕回收完资源后才继续
wait=False，立即返回，并不会等待池内的任务执行完毕
但不管wait参数为何值，整个程序都会等到所有任务执行完毕
submit和map必须在shutdown之前

4、result(timeout=None)
取得结果

5、add_done_callback(fn)
回调函数
```

示例一：进程池

```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os, time, random


def task(name):
    print('name:%s pid:%s run' % (name, os.getpid()))
    time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    pool=ProcessPoolExecutor(4)

    for i in range(10):
        pool.submit(task, 'egon%s' % i)
    # 相当于进程池的pool.close()+pool.join()操作
    pool.shutdown(wait=True)

    print('主')
```

Python3中官方才正式提供线程池。

线程不是开的越多越好，开的多了可能会导致系统的性能更低了，例如：如下的代码是不推荐在项目开发中编写。

**不建议**：无限制的创建线程。

```python
import threading


def task(video_url):
    pass

url_list = ["www.xxxx-{}.com".format(i) for i in range(30000)]

for url in url_list:
    t = threading.Thread(target=task, args=(url,))
    t.start()

# 这种每次都创建一个线程去操作，创建任务的太多，线程就会特别多，可能效率反倒降低了。
```

**建议**：使用线程池

示例1：

```python
import time
from concurrent.futures import ThreadPoolExecutor

# pool = ThreadPoolExecutor(100)
# pool.submit(函数名,参数1，参数2，参数...)


def task(video_url,num):
    print("开始执行任务", video_url)
    time.sleep(5)

# 创建线程池，最多维护10个线程。
pool = ThreadPoolExecutor(10)

url_list = ["www.xxxx-{}.com".format(i) for i in range(300)]

for url in url_list:
    # 在线程池中提交一个任务，线程池中如果有空闲线程，则分配一个线程去执行，执行完毕后再将线程交还给线程池；如果没有空闲线程，则等待。
    pool.submit(task, url,2)
    
print("END")
```

示例2：等待线程池的任务执行完毕。

```python
import time
from concurrent.futures import ThreadPoolExecutor


def task(video_url):
    print("开始执行任务", video_url)
    time.sleep(5)


# 创建线程池，最多维护10个线程。
pool = ThreadPoolExecutor(10)

url_list = ["www.xxxx-{}.com".format(i) for i in range(300)]
for url in url_list:
    # 在线程池中提交一个任务，线程池中如果有空闲线程，则分配一个线程去执行，执行完毕后再将线程交还给线程池；如果没有空闲线程，则等待。
    pool.submit(task, url)

print("执行中...")
pool.shutdown(True)  # 等待线程池中的任务执行完毕后，在继续执行
print('继续往下走')
```

示例3：任务执行完任务，再干点其他事。

```python
import time
import random
from concurrent.futures import ThreadPoolExecutor, Future


def task(video_url):
    print("开始执行任务", video_url)
    time.sleep(2)
    return random.randint(0, 10)


def done(response):
    print("任务执行后的返回值", response.result())


# 创建线程池，最多维护10个线程。
pool = ThreadPoolExecutor(10)

url_list = ["www.xxxx-{}.com".format(i) for i in range(15)]

for url in url_list:
    # 在线程池中提交一个任务，线程池中如果有空闲线程，则分配一个线程去执行，执行完毕后再将线程交还给线程池；如果没有空闲线程，则等待。
    future = pool.submit(task, url)
    future.add_done_callback(done) # 是子主线程执行
    
# 可以做分工，例如：task专门下载，done专门将下载的数据写入本地文件。
```

示例4：最终统一获取结果。

```python
import time
import random
from concurrent.futures import ThreadPoolExecutor,Future


def task(video_url):
    print("开始执行任务", video_url)
    time.sleep(2)
    return random.randint(0, 10)


# 创建线程池，最多维护10个线程。
pool = ThreadPoolExecutor(10)

future_list = []

url_list = ["www.xxxx-{}.com".format(i) for i in range(15)]
for url in url_list:
    # 在线程池中提交一个任务，线程池中如果有空闲线程，则分配一个线程去执行，执行完毕后再将线程交还给线程池；如果没有空闲线程，则等待。
    future = pool.submit(task, url)
    future_list.append(future)
    
pool.shutdown(True)
for fu in future_list:
    print(fu.result())
```

案例：基于线程池下载豆瓣图片。

```csv
26044585,Hush,https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb88cacc46869954f478-aP4Q3V
19318369,柒十一,https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO
15529690,Law344,https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzoQd
18311394,Jennah·,https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz
18009711,可洛爱画画,https://hbimg.huabanimg.com/03331ef39b5c7687f5cc47dbcbafd974403c962ae88ce-Co8AUI
30574436,花姑凉~,https://hbimg.huabanimg.com/2f5b657edb9497ff8c41132e18000edb082d158c2404-8rYHbw
17740339,小巫師,https://hbimg.huabanimg.com/dbc6fd49f1915545cc42c1a1492a418dbaebd2c21bb9-9aDqgl
18741964,桐末tonmo,https://hbimg.huabanimg.com/b60cee303f62aaa592292f45a1ed8d5be9873b2ed5c-gAJehO
30535005,TANGZHIQI,https://hbimg.huabanimg.com/bbd08ee168d54665bf9b07899a5c4a4d6bc1eb8af77a4-8Gz3K1
31078743,你的老杨,https://hbimg.huabanimg.com/c46fbc3c9a01db37b8e786cbd7174bbd475e4cda220f4-F1u7MX
25519376,尺尺寸,https://hbimg.huabanimg.com/ee29ee198efb98f970e3dc2b24c40d89bfb6f911126b6-KGvKes
21113978,C-CLong,https://hbimg.huabanimg.com/7fa6b2a0d570e67246b34840a87d57c16a875dba9100-SXsSeY
24674102,szaa,https://hbimg.huabanimg.com/0716687b0df93e8c3a8e0925b6d2e4135449cd27597c4-gWdv24
30508507,爱起床的小灰灰,https://hbimg.huabanimg.com/4eafdbfa21b2f300a7becd8863f948e5e92ef789b5a5-1ozTKq
12593664,yokozen,https://hbimg.huabanimg.com/cd07bbaf052b752ed5c287602404ea719d7dd8161321b-cJtHss
16899164,一阵疯,https://hbimg.huabanimg.com/0940b557b28892658c3bcaf52f5ba8dc8402100e130b2-G966Uz
847937,卩丬My㊊伴er彎,https://hbimg.huabanimg.com/e2d6bb5bc8498c6f607492a8f96164aa2366b104e7a-kWaH68
31010628,慢慢即漫漫,https://hbimg.huabanimg.com/c4fb6718907a22f202e8dd14d52f0c369685e59cfea7-82FdsK
13438168,海贼玩跑跑,https://hbimg.huabanimg.com/1edae3ce6fe0f6e95b67b4f8b57c4cebf19c501b397e-BXwiW6
28593155,源稚生,https://hbimg.huabanimg.com/626cfd89ca4c10e6f875f3dfe1005331e4c0fd7fd429-9SeJeQ
28201821,合伙哼哼,https://hbimg.huabanimg.com/f59d4780531aa1892b80e0ec94d4ec78dcba08ff18c416-769X6a
28255146,漫步AAA,https://hbimg.huabanimg.com/3c034c520594e38353a039d7e7a5fd5e74fb53eb1086-KnpLaL
30537613,配䦹,https://hbimg.huabanimg.com/efd81d22c1b1a2de77a0e0d8e853282b83b6bbc590fd-y3d4GJ
22665880,日后必火,https://hbimg.huabanimg.com/69f0f959979a4fada9e9e55f565989544be88164d2b-INWbaF
16748980,keer521521,https://hbimg.huabanimg.com/654953460733026a7ef6e101404055627ad51784a95c-B6OFs4
30536510,“西辞”,https://hbimg.huabanimg.com/61cfffca6b2507bf51a507e8319d68a8b8c3a96968f-6IvMSk
30986577,艺成背锅王,https://hbimg.huabanimg.com/c381ecc43d6c69758a86a30ebf72976906ae6c53291f9-9zroHF
26409800,CsysADk7,https://hbimg.huabanimg.com/bf1d22092c2070d68ade012c588f2e410caaab1f58051-ahlgLm
30469116,18啊全阿,https://hbimg.huabanimg.com/654953460733026a7ef6e101404055627ad51784a95c-B6OFs4
17473505,椿の花,https://hbimg.huabanimg.com/0e38d810e5a24f91ebb251fd3aaaed8bb37655b14844c-pgNJBP
19165177,っ思忆゜♪,https://hbimg.huabanimg.com/4815ea0e4905d0f3bb82a654b481811dadbfe5ce2673-vMVr0B
16059616,格林熊丶,https://hbimg.huabanimg.com/8760a2b08d87e6ed4b7a9715b1a668176dbf84fec5b-jx14tZ
30734152,sCWVkJDG,https://hbimg.huabanimg.com/f31a5305d1b8717bbfb897723f267d316e58e7b7dc40-GD3e22
24019677,虚无本心,https://hbimg.huabanimg.com/6fdfa9834abe362e978b517275b06e7f0d5926aa650-N1xCXE
16670283,Y-雨后天空,https://hbimg.huabanimg.com/a3bbb0045b536fc27a6d2effa64a0d43f9f5193c177f-I2vHaI
21512483,汤姆2,https://hbimg.huabanimg.com/98cc50a61a7cc9b49a8af754ffb26bd15764a82f1133-AkiU7D
16441049,笑潇啸逍小鱼,https://hbimg.huabanimg.com/ae8a70cd85aff3a8587ff6578d5cf7620f3691df13e46-lmrIi9
24795603,⁢⁢⁢⁢⁢v,https://hbimg.huabanimg.com/a7183cc3a933aa129d7b3230bf1378fd8f5857846cc5-3tDtx3
29819152,妮玛士珍多,https://hbimg.huabanimg.com/ca4ecb573bf1ff0415c7a873d64470dedc465ea1213c6-RAkArS
19101282,陈勇敢❤,https://hbimg.huabanimg.com/ab6d04ebaff3176e3570139a65155856871241b58bc6-Qklj2E
28337572,爱意随风散,https://hbimg.huabanimg.com/117ad8b6eeda57a562ac6ab2861111a793ca3d1d5543-SjWlk2
17342758,幸运instant,https://hbimg.huabanimg.com/72b5f9042ec297ae57b83431123bc1c066cca90fa23-3MoJNj
18483372,Beau染,https://hbimg.huabanimg.com/077115cb622b1ff3907ec6932e1b575393d5aae720487-d1cdT9
22127102,栽花的小蜻蜓,https://hbimg.huabanimg.com/6c3cbf9f27e17898083186fc51985e43269018cc1e1df-QfOIBG
13802024,LoveHsu,https://hbimg.huabanimg.com/f720a15f8b49b86a7c1ee4951263a8dbecfe3e43d2d-GPEauV
22558931,白驹过隙丶梨花泪う,https://hbimg.huabanimg.com/e49e1341dfe5144da5c71bd15f1052ef07ba7a0e1296b-jfyfDJ
11762339,cojoy,https://hbimg.huabanimg.com/5b27f876d5d391e7c4889bc5e8ba214419eb72b56822-83gYmB
30711623,雪碧学长呀,https://hbimg.huabanimg.com/2c288a1535048b05537ba523b3fc9eacc1e81273212d1-nr8M4t
18906718,西霸王,https://hbimg.huabanimg.com/7b02ad5e01bd8c0a29817e362814666a7800831c154a6-AvBDaG
31037856,邵阳的小哥哥,https://hbimg.huabanimg.com/654953460733026a7ef6e101404055627ad51784a95c-B6OFs4
26830711,稳健谭,https://hbimg.huabanimg.com/51547ade3f0aef134e8d268cfd4ad61110925aefec8a-NKPEYX
```

```python
import os
import requests
from concurrent.futures import ThreadPoolExecutor


def download(file_name, image_url):
    res = requests.get(
        url=image_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
    )
    # 检查images目录是否存在？不存在，则创建images目录
    if not os.path.exists("images"):
        # 创建images目录
        os.makedirs("images")
    file_path = os.path.join("images", file_name)
    # 2.将图片的内容写入到文件
    with open(file_path, mode='wb') as img_object:
        img_object.write(res.content)


# 创建线程池，最多维护10个线程。
pool = ThreadPoolExecutor(10)

with open("mv.csv", mode='r', encoding='utf-8') as file_object:
    for line in file_object:
        nid, name, url = line.split(",")
        file_name = "{}.png".format(name)
        pool.submit(download, file_name, url)
```

```python
import os
import requests
from concurrent.futures import ThreadPoolExecutor


def download(image_url):
    res = requests.get(
        url=image_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
    )
    return res


def outer(file_name):
    def save(response):
        res = response.result()
        # 写入本地
        # # 检查images目录是否存在？不存在，则创建images目录
        if not os.path.exists("images"):
            # 创建images目录
            os.makedirs("images")

        file_path = os.path.join("images", file_name)

        # # 2.将图片的内容写入到文件
        with open(file_path, mode='wb') as img_object:
            img_object.write(res.content)

    return save


# 创建线程池，最多维护10个线程。
pool = ThreadPoolExecutor(10)

with open("mv.csv", mode='r', encoding='utf-8') as file_object:
    for line in file_object:
        nid, name, url = line.split(",")
        file_name = "{}.png".format(name)
        fur = pool.submit(download, url)
        fur.add_done_callback(outer(file_name))
```

#### 10.3.12 map方法

map取代了for循环+submit

示例：

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import os, time, random


def task(n):
    print('%s is runing' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n ** 2


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=3)

    # for i in range(11):
    #     future=executor.submit(task,i)

    executor.map(task, range(1, 3))  # map取代了for+submit
```

#### 10.3.13 调用的两种方式

同步调用：提交完任务后，就在原地等待任务执行完毕，拿到结果，再执行下一行代码，导致程序是串行执行

示例：

```python
from concurrent.futures import ThreadPoolExecutor
import time
import random


def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(3, 5))
    res = random.randint(7, 13) * '#'
    return {'name': name, 'res': res}


def weigh(shit):
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了 《%s》kg' % (name, size))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)

    shit1 = pool.submit(la, 'aaa').result()
    weigh(shit1)

    shit2 = pool.submit(la, 'bbb').result()
    weigh(shit2)

    shit3 = pool.submit(la, 'ccc').result()
    weigh(shit3)
```

回调机制：可以为进程池或线程池内的每个进程或线程绑定一个函数，该函数在进程或线程的任务执行完毕后自动触发，并接收任务的返回值当作参数，该函数称为回调函数。

示例：

```python
from concurrent.futures import ThreadPoolExecutor
import time
import random


def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(3, 5))
    res = random.randint(7, 13) * '#'
    return {'name': name, 'res': res}


def weigh(shit):
    # 拿到结果
    shit = shit.result()
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了 《%s》kg' % (name, size))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)

    pool.submit(la, 'aaa').add_done_callback(weigh)

    pool.submit(la, 'bbb').add_done_callback(weigh)

    pool.submit(la, 'ccc').add_done_callback(weigh)
# la拿到的是一个返回对象obj，需要用obj.result()拿到结果
```

#### 10.3.14 面试题

1. 简述进程和线程的区别以及应用场景。

2. 什么是GIL锁

3. 手写单例模式

4. 程序从flag a执行到falg b的时间大致是多少秒？

   ```python
   import threading
   import time
   def _wait():
   	time.sleep(60)
   # flag a
   t = threading.Thread(target=_wait)
   t.setDaemon(False)
   t.start()
   # flag b
   ```

5. 程序从flag a执行到falg b的时间大致是多少秒？

   ```python
   import threading
   import time
   def _wait():
   	time.sleep(60)
   # flag a
   t = threading.Thread(target=_wait)
   t.setDaemon(True)
   t.start()
   # flag b
   ```

6. 程序从flag a执行到falg b的时间大致是多少秒？

   ```python
   import threading
   import time
   def _wait():
   	time.sleep(60)
   # flag a
   t = threading.Thread(target=_wait)
   t.start()
   t.join()
   # flag b
   ```

7. 读程序，请确认执行到最后number是否一定为0

   ```python
   import threading
   loop = int(1E7)
   def _add(loop = 1):
   	global number
   	for _ in range(loop):
   		number += 1
   def _sub(loop = 1):
   	global number
   	for _ in range(loop):
   		number -= 1
   number = 0
   ta = threading.Thread(target=_add,args=(loop,))
   ts = threading.Thread(target=_sub,args=(loop,))
   ta.start()
   ta.join()
   ts.start()
   ts.join()
   ```

8. 读程序，请确认执行到最后number是否一定为0

   ```python
   import threading
   loop = int(1E7)
   number = 0
   
   def _add(loop = 1):
   	global number
   	for _ in range(loop):
   		number += 1
   def _sub(loop = 1):
   	global number
   	for _ in range(loop):
   		number -= 1
   
   ta = threading.Thread(target=_add,args=(loop,))
   ts = threading.Thread(target=_sub,args=(loop,))
   ta.start()
   ts.start()
   ta.join()
   ts.join()
   ```

9. data.txt 文件中共有 10000 条数据，请为每 100行 数据创建一个线程，并在线程中把当前100条数据的num列相加并打印。

   ```
   subscription_id,erotic,num
   ASDFOKASDJF423KASDFJASDF,5,1
   FSD23R23SFSDF4DFGDFGDFGDF,5,99
   ASDDSFGWERTCERT44GFGDSFG,5,2
   FFFFFFSDSVFG5RTFGDDFFFFA,5,11
   ASDFASDF3234XCVWEGDFGSAF,5,1
   ...
   ```


### 10.4 协程

计算机中提供了：线程、进程 用于实现并发编程（真实存在）。

协程（Coroutine），是程序员通过代码搞出来的一个东西（非真实存在）。

协程是单线程下的并发，又称微线程，纤程。英文名Coroutine。一句话说明什么是协程：**协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的。**

> 协程也可以被称为微线程，是一种用户态内的上下文切换技术。
> 简而言之，其实就是通过一个线程实现代码块相互切换执行（来回跳着执行）。

强调：

- python的线程属于内核级别的，即由操作系统控制调度，线程遇到IO就会被迫切换到其他线程运行
- 单线程内开启协程，一旦遇到io，就会从应用程序级别（也就是自己写的程序）控制切换，以此来提升效率

对比操作系统控制线程的切换，用户在单线程内控制协程的切换

优点：

- 协程的切换开销更小，属于程序级别的切换，操作系统完全感知不到，因而更加轻量级
- 单线程内就可以实现并发的效果，最大限度地利用cpu

缺点：

- 协程的本质是单线程下，无法利用多核，可以是一个程序开启多个进程，每个进程内开启多个线程，每个线程内开启协程
- 协程指的是单个线程，因而一旦协程出现阻塞，将会阻塞整个线程

总结：

1. 必须在只有单线程里实现协程
2. 修改共享数据不需要加锁
3. 用户程序里自己保存多个控制流的上下文栈

附加：一个协程遇到IO操作自动切换到其它协程（如何实现检测IO，yield、greenlet都无法实现，就用到了gevent模块（select机制）

#### 10.4.1 greenlet模块

如果我们想要实现在多个线程任务之间切换，使用yield生成器之间切换很麻烦，而使用greenlet模块可以很简单的实现。

示例：pip install greenlet

```python
from greenlet import greenlet


def eat(name):
    print('%s eat 1' % name)
    g2.switch('egon')
    print('%s eat 2' % name)
    g2.switch()


def play(name):
    print('%s play 1' % name)
    g1.switch()
    print('%s play 2' % name)


g1 = greenlet(eat)
g2 = greenlet(play)

# 可以在第一次switch时传入参数，以后都不需要
g1.switch('egon')
```

greenlet只是提供了一种比generator更加便捷的切换方式，当切到一个任务执行时如果遇到io，那就原地阻塞，仍然是没有解决遇到IO自动切换来提升效率的问题。

示例：

```python
import time
from greenlet import greenlet


def eat(name):
    print('%s eat 1' % name)
    time.sleep(10)
    g2.switch('aaa')
    print('%s eat 2' % name)
    g2.switch()


def play(name):
    print('%s play 1' % name)
    g1.switch()
    print('%s play 2' % name)


g1 = greenlet(eat)
g2 = greenlet(play)

# 可以在第一次switch时传入参数，以后都不需要
g1.switch('aaa')
```

#### 10.4.2 gevent模块

Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是**Greenlet**，它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。

用法：

- g1=gevent.spawn(func,1,,2,3,x=4,y=5)创建一个协程对象g1，spawn括号内第一个参数是函数名，如eat，后面可以有多个参数，可以是位置实参或关键字实参，都是传给函数eat的
- g2=gevent.spawn(func2)
- g1.join()  # 等待g1结束
- g2.join()  # 等待g2结束
- 或者上述两步合作一步：gevent.joinall([g1,g2])
- g1.value # 拿到func1的返回值

**遇到IO阻塞时会自动切换任务**：

示例：

```python
# pip3 install gevent
from gevent import monkey;
import gevent
import time
monkey.patch_all()


def eat(name):
    print('%s eat 1' % name)
    # gevent.sleep(3)
    time.sleep(3)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    # # gevent.sleep(4)
    time.sleep(4)
    print('%s play 2' % name)


start_time = time.time()
g1 = gevent.spawn(eat, 'aaa')
g2 = gevent.spawn(play, 'bbb')

g1.join()
g2.join()
stop_time = time.time()
print(stop_time - start_time)
```

示例中：

- gevent.sleep(3)模拟的是gevent识别IO阻塞

- time.sleep(3)或其他的阻塞，gevent是不能直接识别的，需要打补丁后就可以识别了

    ```python
    from gevent import monkey
    monkey.patch_all()
    ```

- monkey.patch_all()必须放到被打补丁者的前面

或者我们直接写成：**要用gevent，需要将from gevent import monkey;monkey.patch_all()放到文件的开头**

```python
from gevent import monkey;monkey.patch_all()
import gevent
import time

def eat(name):
    print('%s eat 1' % name)
    time.sleep(3)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    time.sleep(4)
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'aaa')
g2 = gevent.spawn(play, 'bbb')

gevent.joinall([g1, g2])
print('zhu')
```

通过gevent实现单线程下的socket并发:

示例：

服务端：

```python
# 基于gevent实现
from gevent import monkey, spawn; monkey.patch_all()
from socket import *


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()


def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        spawn(communicate, conn)

    server.close()


if __name__ == '__main__':
    g = spawn(server, '127.0.0.1', 8090)
    g.join()

```

客户端：多线程并发多个客户端

```python
from threading import Thread
from socket import *
import threading

def client(server_ip,port):
    c=socket(AF_INET,SOCK_STREAM)  # 套接字对象一定要加到函数内，即局部名称空间内，放在函数外则被所有线程共享，则大家公用一个套接字对象，那么客户端端口永远一样了
    c.connect((server_ip,port))

    count=0
    while True:
        c.send(('%s say hello %s' %(threading.current_thread().getName(),count)).encode('utf-8'))
        msg=c.recv(1024)
        print(msg.decode('utf-8'))
        count+=1
if __name__ == '__main__':
    for i in range(500):
        t=Thread(target=client,args=('127.0.0.1',8090))
        t.start()
```

#### 10.4.3 asynic

协程（Coroutine），也可以被称为微线程，是一种用户态内的上下文切换技术，简而言之，其实就是通过一个线程实现代码块相互切换执行。例如：

```python
def func1():
    print(1)
    ...
    print(2)

def func2():
    print(3)
    ...
    print(4)
    
func1()
func2()
```

实现协程的几种方式：

- greenlet，早期模块
- yield关键字
- asyncio装饰器（python3.4）
- async、await关键字（python3.5）【推荐】

##### 10.4.3.1 greenlet

```python
from greenlet import greenlet

def func1():
    print(1)     # 第2步：输出1
    g2.switch()  # 第3步：切换到func2
    print(2)	 # 第6步：输出2
    g2.switch()  # 第7步：切换到func2，从上一次执行的位置继续向后执行


def func2():
    print(3)	 # 第4步：输入3
    g1.switch()  # 第5步：切换到func1，从上一次执行的位置继续向后执行
    print(4)     # 第8步：输出4


g1 = greenlet(func1)
g2 = greenlet(func2)

# 可以在第一次switch时传入参数，以后都不需要
g1.switch() # 第1步：去执行func1函数
```

##### 10.4.3.2 yield关键字

```python
def func1():
    yield 1
    yield from func2()
    yield 2
    
def func2():
    yield 3
    yield 4

f1 = func1()
for item in f1:
    print(item)  # 1 3 4 2
```

##### 10.4.3.3 asyncio

在python3.4及之后的版本。

```python
import asyncio

@asynico.coroutine
def func1():
    print(1)
    # 网络io请求：下载一张图片
    yield from asyncio.sleep(2)  # 遇到io耗时操作，自动化切换到tasks中的其他任务
    print(2)

@asynico.coroutine
def func2():
    print(3)
    # 网络io请求：下载一张图片
    yield from asyncio.sleep(2)  # 遇到io耗时操作，自动化切换到tasks中的其他任务
    print(4)
    
tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2()),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
```

注意：遇到io阻塞自动切换

##### 10.4.3.4 async & await 关键字

在python3.5及以后的版本

```python
import asyncio

async def func1():
    print(1)
    # 网络io请求：下载一张图片
    await asyncio.sleep(2)  # 遇到io耗时操作，自动化切换到tasks中的其他任务
    print(2)

async def func2():
    print(3)
    # 网络io请求：下载一张图片
    await asyncio.sleep(2)  # 遇到io耗时操作，自动化切换到tasks中的其他任务
    print(4)
    
tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2()),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
```

**协程的意义：**

> 在一个线程中如果遇到IO等待时间，线程不会等待，利用空闲时间再去干其他的事。
>
> 不要让用户手动去切换，而是遇到IO操作时能自动切换。
>
> Python在3.4之后推出了asyncio模块 + Python3.5推出async、async语法 ，内部基于协程并且遇到IO请求自动化切换。

示例：下载三张图片（网络IO）

普通编程：

```python
import requests


def download_img(url):
    print("开始下载", url)
    response = requests.get(url=url).content
    print("下载完成")
    file_name = "./5.异步操作/img/" + url.split("-")[1]
    with open(file_name, "wb") as f:
        f.write(response)

urls = [
    "http://pic.netbian.com/uploads/allimg/210508/152327-16204586078720.jpg",
    "http://pic.netbian.com/uploads/allimg/210617/193149-16239295098fb3.jpg",
    "http://pic.netbian.com/uploads/allimg/210617/192555-1623929155c29b.jpg"
]

for url in urls:
    download_img(url)
```

异步编程：

```python
# pip install aiohttp
import aiohttp
import asyncio


async def download_img(session, url):
    print("开始下载", url)
    async with session.get(url=url, verify_ssl=False) as response:
        content = await response.read()
        file_name = "./5.异步操作/img/" + url.split("-")[1]
        with open(file_name, "wb") as f:
            f.write(content)
        print("下载完成", url)


async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            "http://pic.netbian.com/uploads/allimg/210508/152327-16204586078720.jpg",
            "http://pic.netbian.com/uploads/allimg/210617/193149-16239295098fb3.jpg",
            "http://pic.netbian.com/uploads/allimg/210617/192555-1623929155c29b.jpg"
        ]
        tasks = [
            asyncio.create_task(download_img(session, url)) for url in urls
        ]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

<font color="red">**协程、线程、进程的区别：**</font>  

> 参考文章：https://pythonav.com/wiki/detail/6/91/
>
> 参考视频： https://www.bilibili.com/video/BV1NA411g7yf

> - 线程，是计算机中可以被cpu调度的最小单元。
> - 进程，是计算机资源分配的最小单元（进程为线程提供资源）。
> - 一个进程中可以有多个线程，同一个进程中的线程可以共享此进程中的资源。
>
> 由于CPython中GIL的存在：
>  - 线程，适用于IO密集型操作。
>
> - 进程，适用于计算密集型操作。
>
> 协程，协程也可以被称为微线程，是一种用户态内的上下文切换技术，在开发中结合遇到IO自动切换，就可以通过一个线程实现并发操作。
>
>
> 所以，在处理IO操作时，协程比线程更加节省开销（协程的开发难度大一些）。

##### 10.4.3.5 快速上手

协程函数，定义函数时候，`async def` 函数名。

协程对象，执行协程函数()得到的协程对象。

```python
async def func():
    pass
result = func()
```

注意：执行协程函数创建协程对象，函数内部代码不会执行。

运行协程函数内部代码，必须将协程对象交给事件循环来处理。

```python
import asyncio
async def func():
    print("快来看看吧！")
    
result = func()
loop = asyncio.get_event_loop()
loop.run_untile_complete(result)

# python3.7
asyncio.run(result)
```

##### 10.4.3.6 await

await + 可等待的对象（协程对象，future、task对象--》IO等待）

示例一：

```python
import asyncio

async def func():
    print("执行呀")
    response = await asyncio.sleep(2)
    print("结束", response)
    
loop = asyncio.get_event_loop()
loop.run_untile_complete(func())
```

示例二：

```python
import asyncio


async def others():
    print("start")
    response = await asyncio.sleep(2)
    print("end")
    return "返回值"


async def func():
    print("执行协程函数内部代码")
    # 遇到IO操作挂起当前协程，等IO操作完成之后再继续往下执行，当前协程挂起时，事件循环可以去执行其他协程
    response = await others()
    print("IO请求结束， 结果为：", response)

asyncio.run(func())
```

示例三：

```python
import asyncio


async def others():
    print("start")
    response = await asyncio.sleep(2)
    print("end")
    return "返回值"


async def func():
    print("执行协程函数内部代码")
    # 遇到IO操作挂起当前协程，等IO操作完成之后再继续往下执行，当前协程挂起时，事件循环可以去执行其他协程
    response1 = await others()
    print("IO请求结束， 结果为：", response1)

    response2 = await others()
    print("IO请求结束， 结果为：", response2)

asyncio.run(func())
```

await就是等待协程函数返回结果之后再继续往下走。

##### 10.4.3.7 task

> Tasks are used to schedule coroutines concurrently.
>
> When a coroutine is warapped into a Task with functions like `asyncio.create-task()`the coroutine is automatically scheduled to run soon.

白话：在事件循环中添加多个任务

Tasks用于并发调度协程，通过`asyncio.create-task()`（协程对象）的方式创建Task对象，这样可以让协程加入事件循环中等待被调度执行。除了使用`asyncio.create-task()`函数以外，还可以用低层级的`loop.create-task()`或`ensure_future()`函数。不建议手动实例化Task对象。

示例一：

```python
import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main():
    print("main开始")

    # 创建Task对象，将当前执行func函数任务添加到事件循环
    task1 = asyncio.create_task(func())
    # 创建Task对象，将当前执行func函数任务添加到事件循环
    task2 = asyncio.create_task(func())

    print("main结束")

    # 当执行某协程遇到IO操作时，会自动切换执行其他任务
    # 此处的await是等待对应的协程全部执行完毕并获取结果
    ret1 = await task1
    ret2 = await task2
    print(ret1, ret2)
```

示例二：

```python
import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main():
    print("main开始")

    task_list = [
        asyncio.create_task(func(), name="n1"),
        asyncio.create_task(func(), name="n2")
    ]

    print("main结束")

    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done)

asyncio.run(main())
```

事件三：

```python
import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"

task_list = [func(), func()]

# task_list写到协程函数外边，asyncio.run会自动创建task，将task任务加到事件循环中
done, pending = asyncio.run(asyncio.wait(task_list))
print(done)
```

##### 10.4.3.8 asyncio.future对象

> A Future a special **low-level** awaltable object represents an eventual result of an asynchronous operation.

Task继承Future，Task对象内部await结果的处理基于Future对象来的。

示例一：

```python
import asyncio


async def main():

    # 获取当前事件循环
    loop = asyncio.get_running_loop()

    # 创建一个任务（Future对象），这个任务什么都不干
    ret = loop.create_future()

    # 等待任务最终结果（Future对象），没有结果则会一直等下去
    await ret


asyncio.run(main())
```

示例二：

```python
import asyncio


async def func(ret):
    await asyncio.sleep(2)
    ret.set_result("666")


async def main():

    # 获取当前事件循环
    loop = asyncio.get_running_loop()

    # 创建一个任务（Future对象），这个任务什么都不干
    ret = loop.create_future()

    # 创建一个任务（task对象），绑定了func函数，函数内部在2s之后执行，会给ret赋值
    # 即手动设置future任务的最终结果，那么ret就可以结束了
    await loop.create_task(func(ret))

    # 等待Future对象获取最终结果，否则一直等下去
    data = await ret
    print(data)


asyncio.run(main())
```

##### 10.4.3.9 concurrent.futures.Future对象

使用线程池、进程池实现异步操作时用到的对象。

```python
import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def func(value):
    time.sleep(1)
    print(value)
    return 123


# 创建线程池
pool = ThreadPoolExecutor(max_workers=5)

# 创建进程池
# pool = ProcessPoolExecutor(max_workers=5)

for i in range(5):
    fut = pool.submit(func, i)
    print(fut)
```

以后写代码可能会存在交叉使用，例如：crm项目80%基于协程异步编程 + MySQL（不支持），使用【线程、进程做异步编程】。

```python
import time
import asyncio
import concurrent.futures


def func1():
    # 某个耗时操作
    time.sleep(2)
    return 123


async def main():

    loop = asyncio.get_running_loop()
    # 1.Run in the default loop's executor（默认ThreadPoolExecutor）
    """
    第一步：内部先调用ThreadPoolExecutor的 submit 方法，
           去线程池申请一个线程去执行func1函数，并返回一个concurrent.futures.Future对象
    第二步：调用asyncio.wrap_future将concurrent.futures.Future对象包装为asyncio.Future对象，
           因为concurrent.futures.Future对象不支持await语法，所以需要包装为asyncio.Future对象才能使用。
    """
    fut = loop.run_in_executor(None, func1)
    result = await fut
    print("defult thread pool", result)

    # 2.Run in a custom thread pool:
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     result = await loop.run_in_executor(pool, func1)
    #     print("custom thread pool", result)

    # 3.Run in a custom process pool；
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     result = await loop.run_in_executor(pool, func1)
    #     print("custom process pool", result)


asyncio.run(main())
```

案例：asyncio + 不支持异步的模块

```python
import asyncio
import requests
import time


async def download_img(url):
    # 发送网络请求，下载图片（遇到网络下载图片的IP请求，自动切换到其他任务）
    print("开始下载", url)

    loop = asyncio.get_event_loop()

    # requests模块默认不支持异步操作，所以就使用线程池来配置实现
    future = loop.run_in_executor(None, requests.get, url)

    response = await future

    print("下载完成", url)
    

    file_name = "./5.异步操作/img/" + url.split("-")[1]
    with open(file_name, "wb") as f:
        f.write(response.content)
    

urls = [
    "http://pic.netbian.com/uploads/allimg/210508/152327-16204586078720.jpg",
    "http://pic.netbian.com/uploads/allimg/210617/193149-16239295098fb3.jpg",
    "http://pic.netbian.com/uploads/allimg/210617/192555-1623929155c29b.jpg"
]
tasks = [download_img(url) for url in urls]

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
```

##### 10.4.3.10 异步迭代器

什么是异步迭代器：

> 实现了`__aiter()__` 和 `__anext__()` 方法的对象，`__anext__` 必须返回一个 `awaitable` 对象，`async_for`会处理异步迭代器 `__anext__()` 方法所返回的可迭代对象，直到其引发一个 `StopAsyncIteration` 异常。

什么是异步可迭代对象：

> 可在 `async_for` 语句中被使用的对象。必须通过它的 `__aiter__()` 方法返回一个 `asynchronous_iterator` 。

```python
import asyncio


class Reader():
    """ 自定义异步迭代器（同时也是异步可迭代对象） """
    def __init__(self):
        self.count = 0

    async def readline(self):
        # await asyncio.sleep(1)
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self  # 可迭代对象返回自己

    async def __anext__(self):
        val = await self.readline()
        if val == None:
            raise StopAsyncIteration
        return val


async def func():
    obj = Reader()
    async for item in obj:
        print(item)


asyncio.run(func())
```

##### 10.4.3.11 异步上下文管理器

此种对象通过 `__aenter__()` 和 `__aexit__()` 方法来对 `async_with` 语句的环境进行控制。

示例：demo

```python
import asyncio


class AsyncContextManger:
    def __init__(self):
        self.conn = "数据库链接"

    async def do_something(self):
        # 异步操作数据库
        return 666

    async def __aenter__(self):
        # 异步链接数据库
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        # 异步关闭数据库链接
        await asyncio.sleep(1)


async def func():
    async with AsyncContextManger() as f:
        result = await f.do_something()
        print(result)


asyncio.run(func())
```

##### 10.4.3.12 uvloop

是asyncio的事件循环的替代方案。事件循环>默认asyncio的事件循环。

> 安装 ： pip install uvloop

```python
import asyncio
import uvloop
# 将asyncio替换成uvloop性能提示一个等级
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())  

# 编写asyncio的代码，与之前写的代码一致。

# 内部的事件循环自动变为uvloop
asyncio.run(...)
```

注意：一个asgi-> `uvicorn` 内部使用的就是uvloop

- 什么是`WSGI`
- 什么是`ASGI`
- `WSGI`和`ASGI`的区别在哪

**什么是 WSGI**

先说一下`CGI`，（通用网关接口， Common Gateway Interface/CGI），定义客户端与Web服务器的交流方式的一个程序。例如正常情况下客户端发来一个请求，根据`HTTP`协议Web服务器将请求内容解析出来，进过计算后，再将加us安出来的内容封装好，例如服务器返回一个`HTML`页面，并且根据`HTTP`协议构建返回内容的响应格式。涉及到`TCP`连接、`HTTP`原始请求和相应格式的这些，都由一个软件来完成，这时，以上的工作需要一个程序来完成，而这个程序便是`CGI`。

那什么是`WSGI`呢？[维基](https://link.jianshu.com?t=https://zh.wikipedia.org/wiki/Web服务器网关接口)上的解释为，**Web服务器网关接口(Python Web Server Gateway Interface，WSGI)**，是为`Python`语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。从语义上理解，貌似`WSGI`就是`Python`为了解决**Web服务器端与客户端**之间的通信问题而产生的，并且`WSGI`是基于现存的`CGI`标准而设计的，同样是一种程序（或者`Web`组件的接口规范？）。

[WSGI](https://link.jianshu.com?t=https://zh.wikipedia.org/wiki/Web服务器网关接口)区分为两部分：一种为“服务器”或“网关”，另一种为“应用程序”或“应用框架”。
 所谓的`WSGI`中间件同时实现了`API`的两方，即在`WSGI`服务器和`WSGI`应用之间起调解作用：从`WSGI`服务器的角度来说，中间件扮演应用程序，而从应用程序的角度来说，中间件扮演服务器。中间件具有的功能：

- 重写环境变量后，根据目标URL，将请求消息路由到不同的应用对象。
- 允许在一个进程中同时运行多个应用程序或应用框架
- 负载均衡和远程处理，通过在网络上转发请求和相应消息。
- 进行内容后处理，例如应用`XSLT`样式表。（以上 from 维基）

看了这么多，总结一下，其实可以说`WSGI`就是基于`Python`的以`CGI`为标准做一些扩展。

**什么是[ASGI](https://link.jianshu.com?t=https://blog.ernest.me/post/asgi-draft-spec-zh)**

异步网关协议接口，一个介于网络协议服务和`Python`应用之间的标准接口，能够处理多种通用的协议类型，包括`HTTP`，`HTTP2`和`WebSocket`。
 然而目前的常用的`WSGI`主要是针对`HTTP`风格的请求响应模型做的设计，并且越来越多的不遵循这种模式的协议逐渐成为`Web`变成的标准之一，例如`WebSocket`。
 `ASGI`尝试保持在一个简单的应用接口的前提下，提供允许数据能够在任意的时候、被任意应用进程发送和接受的抽象。并且同样描述了一个新的，兼容`HTTP`请求响应以及`WebSocket`数据帧的序列格式。允许这些协议能通过网络或本地`socket`进行传输，以及让不同的协议被分配到不同的进程中。

**WSGI和ASGI的区别在哪**

以上，`WSGI`是基于`HTTP`协议模式的，不支持`WebSocket`，而`ASGI`的诞生则是为了解决`Python`常用的`WSGI`不支持当前`Web`开发中的一些新的协议标准。同时，`ASGI`对于`WSGI`原有的模式的支持和`WebSocket`的扩展，即`ASGI`是`WSGI`的扩展。

#### 10.4.4 实战案例

##### 10.4.4.1 异步redis

> pip install aioredis

示例一：

```python
import asyncio
import aioredis


async def execute(address, passowrd):
    print("开始执行", address)
    # 网络IO操作：创建redis链接
    await aioredis.create_redis(address, passowrd=passowrd)

    # 网络IO操作：在redis中设置哈希值car，内部再设三个键值对，
    await redis.hmset_dict("car", key1=1, key2=2, key3=3)

    # 网络IO操作：去redis中获取值
    result = await redis.hgetall("car", encoding="utf-8")
    print(result)

    redis.close()
    # 网络IO操作：关闭redis链接
    await redis.wait_closed()

    print("结束", address)

asyncio.run(execute("redis://43.9.4.198:6379", "root:123456"))
```

示例二：

```python
import asyncio
import aioredis


async def execute(address, passowrd):
    print("开始执行", address)
    # 网络IO操作：创建redis链接
    await aioredis.create_redis(address, passowrd=passowrd)

    # 网络IO操作：在redis中设置哈希值car，内部再设三个键值对，
    await redis.hmset_dict("car", key1=1, key2=2, key3=3)

    # 网络IO操作：去redis中获取值
    result = await redis.hgetall("car", encoding="utf-8")
    print(result)

    redis.close()
    # 网络IO操作：关闭redis链接
    await redis.wait_closed()

    print("结束", address)

    task_list = [
        execute("redis://43.9.4.198:6379", "root:123456"),
        execute("redis://43.9.4.199:6379", "root:123456")
    ]


asyncio.run(asyncio.wait(task_list))
```

##### 10.4.4.2 异步MySQL

示例一：

```python
import asyncio
import aiomysql


async def execute():
    # 网络IO操作：链接Mysql
    conn = await aiomysql.connect(host="127.0.0.1",
                                  port=3306,
                                  user="root",
                                  password="123",
                                  db="mysql")

    # 网络IO操作：创建USERROOT
    cur = await conn.cursor()
    # 网络IO操作：执行SQL
    await cur.excute("select host,user from user")

    # 网络IO操作：获取SQL结果
    result = await cur.fetchall()
    print(result)

    # 网络IO操作：关闭链接
    await cur.close()
    conn.close()


asyncio.run(execute())
```

示例二：

```python
import asyncio
import aiomysql


async def execute(host, user):
    # 网络IO操作：链接Mysql
    conn = await aiomysql.connect(host=host,
                                  port=3306,
                                  user=user,
                                  password="123",
                                  db="mysql")

    # 网络IO操作：创建USERROOT
    cur = await conn.cursor()
    # 网络IO操作：执行SQL
    await cur.excute("select host,user from user")

    # 网络IO操作：获取SQL结果
    result = await cur.fetchall()
    print(result)

    # 网络IO操作：关闭链接
    await cur.close()
    conn.close()
    print("结束", host)


task_list = [
    execute("17.62.136.197", "root"),
    execute("17.62.136.198", "root")
]

asyncio.run(asyncio.wait(task_list))
```

##### 10.4.4.3 FastAPI框架

> 安装框架：pip install fastapi
>
> pip install uvicorn（asgi内部基于uvloop）

示例一：

```python
import asyncio
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    """普通操作接口"""
    # 某个IO操作10s
    return{"messsage": "hello world!"}


if __name__=='__main__':
	uvicorn.run("fastapi:app", host="127.0.0.1", port=8001, log_level="info")
```

示例二：

```python
import asyncio
import uvicorn
import aioredis
from aioredis import Redis
from fastapi import FastAPI

app = FastAPI()

# 创建一个redis连接池
REDIS_POOL = aioredis.ConnectionsPool("redis://47.193.14.198:6379",
                                      password="123456",
                                      minsize=1,
                                      maxsize=10)


@app.get("/")
def index():
    """普通操作接口"""
    return {"message": "hello world!"}


async def red():
    """异步操作接口"""
    print("请求来了！")

    await asyncio.sleep(2)

    # 连接池获取一个连接
    conn = await REDIS_POOL.acquire()
    redis = Redis(conn)

    # 设置值
    await redis.hmset_dict("car", key1=1, key2=2, key3=3)

    # 读取值
    result = await redis.hgetall("car", encoding="utf-8")
    print(result)

    # 连接归还连接池
    REDIS_POOL.release(conn)

    return result


if __name__ == '__main__':
    uvicorn.run("fastapi:app", host="127.0.0.1", port=8001, log_level="info")
```

##### 10.4.4.4 异步爬虫

> pip3.8 install aiohttp

```python
import aiohttp
import asyncio


async def fetch(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        text = await response.text()
        print("返回结果：", url, len(text))
        return text


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            "https://python.org",
            "https://baidu.com",
            "https://www.hao123.com/",
        ]

        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]

        done, pending = await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

```

**总结：最大的意义:通过一个线程利用其IO等待时间去做一些其他事情。**

### 10.5 IO模型

#### 10.5.1 阻塞IO

socket默认情况下都是blocking，一个典型的读操作流程是这样的：

![1643078596539](J:\homework\Python学习笔记\Python_notes.assets\1643078596539.png)

当用户进程调用了recvfrom这个系统调用，kernel就开始了IO的第一个阶段：准备数据。对于network io来说，很多时候数据在一开始还没有到达，这个时候kernel就要等待足够的数据到来。

用户这边整个进程会被阻塞，当kernel一直等到数据准备好了，它就会将数据从kernel中拷贝到用户内存，然后kernel返回结果，用户进程才能解除blokck状态，重新运作起来。

**所以，blocking IO的特点就是IO执行的两个阶段（等待数据和拷贝数据两个阶段），都被block了。**

```
几乎所有的程序员第一次接触到的网络编程都是从listen\(\)、send\(\)、recv\(\) 等接口开始的，
使用这些接口可以很方便的构建服务器/客户机的模型。然而大部分的socket接口都是阻塞型的
ps：
所谓阻塞型接口是指系统调用（一般是IO接口）不返回调用结果并让当前线程一直阻塞
只有当该系统调用获得结果或者超时出错时才返回。
```

示例：

服务端：

```python
from socket import *
from threading import Thread


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()


server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)

while True:
    print('starting...')
    conn, addr = server.accept()

    t = Thread(target=communicate, args=(conn,))
    t.start()

server.close()
```

客户端：

```python
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

while True:
    msg = input('>>: ').strip()
    if not msg: continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()
```

实际上，除非特别指定，几乎所有的IO接口 ( 包括socket接口 ) 都是阻塞型的。这给网络编程带来了一个很大的问题，如在调用recv(1024)的同时，线程将被阻塞，在此期间，线程将无法执行任何运算或响应任何的网络请求。

一个简单的解决方案：

```
在服务器端使用多线程（或多进程）。多线程（或多进程）的目的是让每个连接都拥有独立的线程（或进程），
这样任何一个连接的阻塞都不会影响其他的连接。
```

该方案的问题是：

```
开启多进程或都线程的方式，在遇到要同时响应成百上千路的连接请求，则无论多线程还是多进程都会严重占据系统资源，
降低系统对外界响应效率，而且线程与进程本身也更容易进入假死状态。
```

改进方案：

```
很多程序员可能会考虑使用“线程池”或“连接池”。“线程池”旨在减少创建和销毁线程的频率，
其维持一定合理数量的线程，并让空闲的线程重新承担新的执行任务。“连接池”维持连接的缓存池，尽量重用已有的连接、
减少创建和关闭连接的频率。这两种技术都可以很好的降低系统开销，都被广泛应用很多大型系统，如websphere、tomcat和各种数据库等。
```

改进后方案其实也存在着问题：

```
“线程池”和“连接池”技术也只是在一定程度上缓解了频繁调用IO接口带来的资源占用。而且，所谓“池”始终有其上限，
当请求大大超过上限时，“池”构成的系统对外界的响应并不比没有池的时候效果好多少。所以使用“池”必须考虑其面临的响应规模，
并根据响应规模调整“池”的大小。
```

**对应上例中的所面临的可能同时出现的上千甚至上万次的客户端请求，“线程池”或“连接池”或许可以缓解部分压力，但是不能解决所有问题。总之，多线程模型可以方便高效的解决小规模的服务请求，但面对大规模的服务请求，多线程模型也会遇到瓶颈，可以用非阻塞接口来尝试解决这个问题。**

#### 10.5.2 非阻塞IO

通过设置socket使其变为non-blocking。当对一个non-blocking socket执行读操作时，流程是这个样子：

![1643078400826](J:\homework\Python学习笔记\Python_notes.assets\1643078400826.png)

非阻塞的recvform系统调用调用之后，进程并没有被阻塞，内核马上返回给进程，如果数据还没准备好，此时会返回一个error。进程在返回之后，可以干点别的事情，然后再发起recvform系统调用。重复上面的过程，循环往复的进行recvform系统调用。这个过程通常被称之为轮询。

轮询检查内核数据，直到数据准备好，再拷贝数据到进程，进行数据处理。需要注意，拷贝数据整个过程，进程仍然是属于阻塞的状态。

**所以，在非阻塞式IO中，用户进程其实是需要不断的主动询问kernel数据准备好了没有。**

示例：

服务端：

```python
from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8083))
server.listen(5)
server.setblocking(False)
print('starting...')

rlist = []
wlist = []
while True:

    try:
        conn, addr = server.accept()
        rlist.append(conn)
        print(rlist)
    except BlockingIOError:
        # print('干其他的活')

        # 收消息
        del_rlist = []
        for conn in rlist:
            try:
                data = conn.recv(1024)
                if not data:
                    del_rlist.append(conn)
                    continue
                wlist.append((conn, data.upper()))
            except BlockingIOError:
                continue
            except Exception:
                conn.close()
                del_rlist.append(conn)

        # 发消息
        del_wlist = []
        for item in wlist:
            try:
                conn = item[0]
                data = item[1]
                conn.send(data)
                del_wlist.append(item)
            except BlockingIOError:
                pass

        for item in del_wlist:
            wlist.remove(item)

        for conn in del_rlist:
            rlist.remove(conn)

server.close()
```

客户端：

```python
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8083))

while True:
    msg = input('>>: ').strip()
    if not msg: continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()
```

**非阻塞IO模型绝不被推荐！**

优点：

- 能够在等待任务完成的时间里干其他活了（包括提交其他任务，也就是 “后台” 可以有多个任务在”同时“执行）。

缺点：

- 循环调用recv()将大幅度推高CPU占用率。
- 任务完成的响应延迟增大了，因为每过一段时间才去轮询一次read操作，而任务可能在两次轮询之间的任意时间完成。这会导致整体数据吞吐量的降低。

**此外，在这个方案中recv()更多的是起到检测“操作是否完成”的作用，实际操作系统提供了更为高效的检测“操作是否完成“作用的接口，例如select()多路复用模式，可以一次检测多个连接是否活跃。**

#### 10.5.3 多路复用IO

IO multiplexing这个词可能有点陌生，但是如果我说select/epoll，大概就都能明白了。有些地方也称这种IO方式为**事件驱动IO**(event driven IO)。

select/epoll的好处就在于单个process就可以同时处理多个网络连接的IO。它的基本原理就是select/epoll这个function会不断的轮询所负责的所有socket，当某个socket有数据到达了，就通知用户进程。

![1643078336325](J:\homework\Python学习笔记\Python_notes.assets\1643078336325.png)

当用户进程调用了select，那么整个进程会被block，而同时，kernel会“监视”所有select负责的socket，当任何一个socket中的数据准备好了，select就会返回。这个时候用户进程再调用read操作，将数据从kernel拷贝到用户进程。这个图和blocking IO的图其实并没有太大的不同，事实上还更差一些。因为这里需要使用两个系统调用\(select和recvfrom\)，而blocking IO只调用了一个系统调用\(recvfrom\)。但是，用select的优势在于它可以同时处理多个connection。

**注意：**

- **如果处理的连接数不是很高的话，使用select/epoll的web server不一定比使用multi-threading + blocking IO的web server性能更好，可能延迟还更大。select/epoll的优势并不是对于单个连接能处理得更快，而是在于能处理更多的连接。**

- **在多路复用模型中，对于每一个socket，一般都设置成为non-blocking，但是，如上图所示，整个用户的process其实是一直被block的。只不过process是被select这个函数block，而不是被socket IO给block。**

**结论: select的优势在于可以处理多个连接，不适用于单个连接**

示例：

服务端：

```python
from socket import *
import select

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8083))
server.listen(5)
server.setblocking(False)
print('starting...')

rlist = [server, ]
wlist = []
wdata = {}

while True:
    rl, wl, xl = select.select(rlist, wlist, [], 0.5)
    print('rl', rl)
    print('wl', wl)

    for sock in rl:
        if sock == server:
            conn, addr = sock.accept()
            rlist.append(conn)
        else:
            try:
                data = sock.recv(1024)
                if not data:
                    sock.close()
                    rlist.remove(sock)
                    continue
                wlist.append(sock)
                wdata[sock] = data.upper()
            except Exception:
                sock.close()
                rlist.remove(sock)

    for sock in wl:
        data = wdata[sock]
        sock.send(data)
        wlist.remove(sock)
        wdata.pop(sock)

server.close()
```

客户端：

```python
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8083))

while True:
    msg = input('>>: ').strip()
    if not msg: continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()
```

**select监听fd变化的过程分析：**

```
用户进程创建socket对象，拷贝监听的fd到内核空间，每一个fd会对应一张系统文件表，内核空间的fd响应到数据后，就会发送信号给用户进程数据已到；
用户进程再发送系统调用，比如（accept）将内核空间的数据copy到用户空间，同时作为接受数据端内核空间的数据清除，这样重新监听时fd再有新的数据又可以响应到了（发送端因为基于TCP协议所以需要收到应答后才会清除）。
```

**该模型的优点：**

```
相比其他模型，使用select() 的事件驱动模型只用单线程（进程）执行，占用资源少，不消耗太多 CPU，同时能够为多客户端提供服务。
如果试图建立一个简单的事件驱动的服务器程序，这个模型有一定的参考价值。
```

**该模型的缺点：**

```
首先select()接口并不是实现“事件驱动”的最好选择。因为当需要探测的句柄值较大时，select()接口本身需要消耗大量时间去轮询各个句柄。
很多操作系统提供了更为高效的接口，如linux提供了epoll，BSD提供了kqueue，Solaris提供了/dev/poll，…。
如果需要实现更高效的服务器程序，类似epoll这样的接口更被推荐。遗憾的是不同的操作系统特供的epoll接口有很大差异，所以使用类似于epoll的接口实现具有较好跨平台能力的服务器会比较困难。
其次，该模型将事件探测和事件响应夹杂在一起，一旦事件响应的执行体庞大，则对整个模型是灾难性的。
```

**selectors模块**：

除了Select可以实现IO多路复用，还有poll和epoll模块可以实现，它们的不同点是：

Select最多可以监听1024个连接，且管理多个描述符也是进行轮询，根据描述符的状态进行处理，但select在linux,windows,mac上都有

poll解决select的监听个数限制，但是依旧是轮询方式。

epoll解决了轮询问题，可以直接拿到就绪的套接字，但是Windows不支持。

好在我们有selectors模块，帮我们默认选择当前平台下最合适的。

示例：

服务端：

```python
from socket import *
import selectors

sel = selectors.DefaultSelector()  # 设置不同平台默认的selectoer
server_fileobj = socket(AF_INET, SOCK_STREAM)
server_fileobj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_fileobj.bind(('127.0.0.1', 8088))
server_fileobj.listen(5)


def accept(server_fileobj, mask):
    conn, addr = server_fileobj.accept()
    sel.register(conn, selectors.EVENT_READ, read)  # 将套接字放入监听列表，并绑定read函数


def read(conn, mask):
    try:
        data = conn.recv(1024)
        if not data:
            print('closing', conn)
            sel.unregister(conn)  # 将套接字从监听列表中移除，不再监听
            conn.close()
            return
        conn.send(data.upper() + b'_SB')
    except Exception:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


server_fileobj.setblocking(False)  # 设置socket的接口为非阻塞
# 相当于网select的读列表里append了一个文件句柄server_fileobj,并且绑定了一个回调函数accept
sel.register(server_fileobj, selectors.EVENT_READ, accept)

while True:
    events = sel.select()  # 检测所有的fileobj，是否有完成wait data的，开始监听
    for sel_obj, mask in events:
        callback = sel_obj.data  # 获得套接字绑定的函数，如果是server_fileobj，callback=accpet 
        # 执行绑定的函数，sel_obj.fileobj就是拿到的套接字，如果是server_fileobj，相当于accpet(server_fileobj，mask)
        callback(sel_obj.fileobj, mask)
```

客户端：

```python
from socket import *

c = socket(AF_INET, SOCK_STREAM)
c.connect(('127.0.0.1', 8088))

while True:
    msg = input('>>: ')
    if not msg: continue
    c.send(msg.encode('utf-8'))
    data = c.recv(1024)
    print(data.decode('utf-8'))
```

#### 10.5.4 异步IO

asynchronous IO其实用得不多，从内核2.6版本才开始引入。先看一下它的流程：

![1643078454115](J:\homework\Python学习笔记\Python_notes.assets\1643078454115.png)

用户进程发起read操作之后，立刻就可以开始去做其它的事。而另一方面，从kernel的角度，当它受到一个asynchronous read之后，首先它会立刻返回，所以不会对用户进程产生任何block。然后，kernel会等待数据准备完成，然后将数据拷贝到用户内存，当这一切都完成之后，kernel会给用户进程发送一个signal，告诉它read操作完成了。

#### 10.5.5 模型比较分析

四个IO Model的区别：

- blocking和non-blocking的区别
    - 前面的介绍中其实已经很明确的说明了这两者的区别。调用blocking IO会一直block住对应的进程直到操作完成，而non-blocking IO在kernel还准备数据的情况下会立刻返回。
- synchronous IO和asynchronous IO的区别
    - 同步I/O操作导致请求进程被阻塞，直到I/O操作完成；异步I/O操作不会阻塞请求进程。

按照这个定义，四个IO模型可以分为两大类（同步阻塞，异步不阻塞）：

定义：

```
A synchronous I/O operation causes the requesting process to be blocked until that I/O operationcompletes;  
An asynchronous I/O operation does not cause the requesting process to be blocked;
```

- blocking IO，non-blocking IO，IO multiplexing都属于synchronous IO这一类，阻塞
- asynchronous I/O后一类，不阻塞

```
有人可能会说，non-blocking IO并没有被block啊。这里有个非常“狡猾”的地方，定义中所指的”IO operation”是指真实的IO操作，
就是例子中的recvfrom这个system call。non-blocking IO在执行recvfrom这个system call的时候，如果kernel的数据没有准备好，
这时候不会block进程。但是，当kernel中数据准备好的时候，recvfrom会将数据从kernel拷贝到用户内存中，这个时候进程是被block了，
在这段时间内，进程是被block的。而asynchronous IO则不一样，当进程发起IO 操作之后，就直接返回再也不理睬了，直到kernel发送一个信号，
告诉进程说IO完成。在这整个过程中，进程完全没有被block。
```

#### 10.5.6 socket_server模块

示例：

服务端实现并发：

```python
import socketserver


class MySocket(socketserver.BaseRequestHandler):
    def handle(self):
        """
        并发业务逻辑
        :return:
        """
        while True:
            client_data = self.request.recv(1024)
            if client_data.decode('utf-8') == 'exit':
                print('客户端断开连接，等待新的客户端连接')
                break
            print('接收数据>>:', client_data.decode('utf-8'))
            response = input('响应数据>>:').strip()
            self.request.sendall((response).encode('utf-8'))
        self.request.close()


# 封装了这三步：1.self.socket  2.self.socket.bind  3.self.socket.listen(5)
server = socketserver.ThreadingTCPServer(('127.0.0.1', 8081), MySocket)

server.serve_forever()
```

客户端：

```PYTHON
import socket
ip_port = ('127.0.0.1', 8081)
sock = socket.socket()
sock.connect(ip_port)
print('客户端启动：')


while True:
    inp = input('发送数据>>:')
    sock.sendall(inp.encode('utf-8'))
    if inp == 'exit':
        break
    server_response = sock.recv(1024)
    print('服务端响应数据>>:', server_response.decode('utf-8'))

sock.close()
```

## 第十一章 数据库

### 11.1 数据库概念

**什么是数据库（Data）**

描述事物的符号记录称为数据，描述事物的符号既可以是数字、文字、图片，图像、声音、语言等，数据由多种表现形式，它们都可以经过数字化后存入计算机。

示例：我的个人信息

序号：1，姓名：ike，性别：male，年龄：25，出生年月：1994，籍贯：张家口，专业：计算机，爱好：健身

```
id,name,sex,age,birth,born_addr,major,hobby
1,ike,male,25,1994,张家口,计算机,健身
```

我们可以通过这样的一条数据了解到我的基本资料。

**什么是数据库（DataBase 简称DB）**

数据库即存放数据的仓库，只不过这个仓库是在计算机存储设备上，而且数据是按一定的格式存放的。

过去人们将数据存放在文件柜里，随着时间的推移数据量庞大，已经不再适用数据库是长期存放，在计算机内、有组织、可共享的数据即可。

数据库中的数据按一定的数据模型组织、描述和储存，具有较小的冗余度、较高的数据独立性和易扩展性，并可为各种用户共享。

**什么是数据库管理系统（DataBase Management System 简称DBMS）**

在了解了Data与DB的概念后，如何科学地组织和存储数据，如何高效获取和维护数据成了关键，这就用到了一个系统软件---数据库管理系统。

如MySQL、Oracle、SQLite、Access、MS SQL Server等等。

mysql主要用于大型门户，例如搜狗、新浪等，它主要的优势就是开放源代码，因为开放源代码这个数据库是免费的，他现在是甲骨文公司的产品。
oracle主要用于银行、铁路、飞机场等。该数据库功能强大，软件费用高。也是甲骨文公司的产品。
sql server是微软公司的产品，主要应用于大中型企业，如联想、方正等。

**数据库服务器、数据管理系统、数据库、表、记录之间的关系**

- 记录：1,ike,male,25,1994,张家口,计算机,健身（多个字段信息组成的一条记录，即文件中的一行内容）
- 表：class，student（可以理解一个文件，如一个excel）
- 数据库：school_info（可以理解为一个文件夹，存放文件的）
- 数据库管理系统：如MySQL等（是一个软件）
- 数据库服务器：一台计算机（对内存要求比较高）

总结：

- 数据库服务器：用来运行数据库管理系统
- 数据库管理系统：用来管理数据库
- 数据库：即文件夹，用来组织和存放文件
- 表：即文件，用来存放多行内容

### 11.2 MySQL简介

MySQL是一个关系型数据库管理系统，由瑞典MySQL AB 公司开发，目前属于 Oracle旗下产品。MySQL 是最流行的关系型数据库管理系统之一，在 WEB 应用方面，MySQL是最好的 RDBMS(Relational Database Management System，关系数据库管理系统) 应用软件之一。

**MySQL就是一个基于socket编写的C/S架构的软件：**

客户端软件：

- MySQL自带：如mysql命令
- python模块：如pymysql

**数据库管理软件分为两类：**

- 关系型：如sqllite，db2，oracle，access，sql server，MySQL。**注意：sql语句通用**
    - 关系型数据库需要有表结构
- 非关系型：mongodb，redis，memcache
    - 非关系型数据库是key-value存储的，没有表结构

### 11.3 MySQL下载安装

以Windows系统为例：

- 官网下载：MySQL Community Server 5.7.16
- 解压下载包：如果想要让MySQL安装在指定目录，那么就将解压后的文件夹移动到指定目录，如：C:\mysql-5.7.16-winx64
- 添加环境变量步骤：右键计算机-->属性-->高级系统设置-->环境变量-->系统变量中找到path-->将MySQL的安装目录下的bin目录路径放到path中，用分号分割   *Rd3;Yz5kwEx
- 以管理员的身份打开cmd，初始化，制作系统服务：mysqld --initialize --user=mysql --console
- 启动MySQL服务：以管理员身份打开cmd，输入 net start mysql
- 关闭MySQL服务：以管理员身份打开cmd，输入 net stop mysql

### 11.4 设置登陆密码

```mysql
# 初始状态下，管理员root，密码为空，默认只允许从本机登录localhost
mysqladmin -uroot -p password "123"  # 设置初始密码 由于原密码为空，因此-p可以不用
mysqladmin -uroot -p "123" password "456"  # 修改mysql密码,因为已经有密码了，所以必须输入原密码才能设置新密码

# 提示：You must reset your password using ALTER USER statement before executing this statement.修改密码
alter user user() identified by "123456";
```

### 11.5 破解密码

**Windows系统下，破解密码的方式**：

示例： 

```mysql
#1 关闭mysql管理员身份:net stop mysql
#2 在cmd中执行，跳过授权表：mysqld --skip-grant-tables
#3 在cmd中执行：mysql
#4 执行如下sql：update mysql.user set apassword=password('') where user = 'root';
#5 刷新权限表：flush privileges;

#5 tskill mysqld #或taskkill -f /PID 7832
#6 重新启动mysql:net start mysql
```

**Mac系统下，破解密码的方式**：

示例：

```mysql
#1 关闭服务：server.stop mysql
#2 跳过授权表：mysql_safe --skip-grant-tables
#3 打开另外一个终端输入：mysql -uroot -p
#4 执行如下sql：update mysql.user set apassword=password('') where user = 'root';
#5 刷新权限表：flush privileges;
#6 找到mysql的进程：ps aux |grep mysql
#7 杀死进程：kill -9 6246
#8 重启服务：net start mysql
```

### 11.6 统一字符编码

**强调：配置文件中的注释可以有中文，但是配置项中不能出现中文**

**统一字符编码**：

```mysql
#在mysql的解压目录下，新建my.ini,然后配置
#1. mysql5.5以下，修改配置文件
[mysqld]
default-character-set=utf8 
[client]
default-character-set=utf8 
[mysql]
default-character-set=utf8

#mysql5.5以上：修改方式有所改动
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8

#2. 重启服务
#3. 查看修改结果：\s
```

### 11.7 初识数据库

SQL语言主要用于存取数据、查询数据、更新数据和管理关系数据库系统,SQL语言由IBM开发。

SQL语言分为3种类型：

- DDL语言：
    - 数据库定义语言： 数据库、表、视图、索引、存储过程，例如CREATE DROP ALTER
- DML语言：
    - 数据库操纵语言： 插入数据INSERT、删除数据DELETE、更新数据UPDATE、查询数据SELECT
- DCL语句：
    - 数据库控制语言： 例如控制用户的访问权限GRANT、REVOKE

SQL语句：

```mysql
操作文件夹（库）
	增：
		create database db1 charset utf8;
    查：
    	show create database db1;
    	show databases;
	改：
		alter database db1 charset gbk;
	删：
		drop database db1;
	
操作文件（表）
	切换文件夹：
		use db1;
	查看当前所在文件夹：
		select database();
	
	增：
		create table t1(id int,name char);
	查：
		show create table t1;
		show tables;
		desc t1;
	改：
		alter table t1 modify name char(6);
		alter table t1 change name NAME char(7);
	删：drop table t1;
		

操作文件内容（记录）
	增：
		insert t1(id,name) values(1,'egon1'),(2,'egon2'),(3,'egon3');
	查：
		select id,name from db1.t1;
		select * from db1.t1;
	改：
		update db1.t1 set name='SB';
		update db1.t1 set name='ALEX' where id=2;
	删：
		delete from t1;
		delete from t1 where id=2;
```

### 11.8 库操作

#### 11.8.1 创建数据库

语法：

```mysql
CREATE DATABASE 数据库名 charset utf8;
```

数据库命名规则：

- 可以由字母、数字、下划线、＠、＃、＄
- 区分大小写
- 唯一性
- 不能使用关键字，如：create select
- 不能单独使用数据
- 最长128位

#### 11.8.2 数据库相关操作

查看数据库：

```mysql
show databases;
show create databases db1;
select dtabases();
```

选择数据库:

```mysql
# use 数据库名字
use db1;
```

删除数据库:

```mysql
DROP DATABASE 数据库名;
```

修改数据库:

```mysql
alter database db1 charset utf8;
```

### 11.9 表操作

#### 11.9.1 存储引擎

存储引擎就是表的类型。

**MySQL支持的存储引擎**

查看所有支持的存储引擎：

```mysql
show engines\G;
```

查看正在使用的存储引擎:

```mysql
show variables like 'storage_engine%';
```

**1、InnoDB 存储引擎**

```
支持事务,其设计目标主要面向联机事务处理(OLTP)的应用。其

特点是行锁设计、支持外键,并支持类似 Oracle 的非锁定读,即默认读取操作不会产生锁。 从 MySQL 5.5.8 版本开始是默认的存储引擎。

InnoDB 存储引擎将数据放在一个逻辑的表空间中,这个表空间就像黑盒一样由 InnoDB 存储引擎自身来管理。从 MySQL 4.1(包括 4.1)版本开始,可以将每个 InnoDB 存储引擎的 表单独存放到一个独立的 ibd 文件中。此外,InnoDB 存储引擎支持将裸设备(row disk)用 于建立其表空间。

InnoDB 通过使用多版本并发控制(MVCC)来获得高并发性,并且实现了 SQL 标准 的 4 种隔离级别,默认为 REPEATABLE 级别,同时使用一种称为 netx-key locking 的策略来 避免幻读(phantom)现象的产生。除此之外,InnoDB 存储引擎还提供了插入缓冲(insert buffer)、二次写(double write)、自适应哈希索引(adaptive hash index)、预读(read ahead) 等高性能和高可用的功能。

对于表中数据的存储,InnoDB 存储引擎采用了聚集(clustered)的方式,每张表都是按 主键的顺序进行存储的,如果没有显式地在表定义时指定主键,InnoDB 存储引擎会为每一 行生成一个 6 字节的 ROWID,并以此作为主键。

InnoDB 存储引擎是 MySQL 数据库最为常用的一种引擎,Facebook、Google、Yahoo 等 公司的成功应用已经证明了 InnoDB 存储引擎具备高可用性、高性能以及高可扩展性。对其 底层实现的掌握和理解也需要时间和技术的积累。如果想深入了解 InnoDB 存储引擎的工作 原理、实现和应用,可以参考《MySQL 技术内幕:InnoDB 存储引擎》一书。
```

**2、MyISAM 存储引擎**

```mysql
不支持事务、表锁设计、支持全文索引,主要面向一些 OLAP 数 据库应用,在 MySQL 5.5.8 版本之前是默认的存储引擎(除 Windows 版本外)。数据库系统 与文件系统一个很大的不同在于对事务的支持,MyISAM 存储引擎是不支持事务的。究其根 本,这也并不难理解。用户在所有的应用中是否都需要事务呢?在数据仓库中,如果没有 ETL 这些操作,只是简单地通过报表查询还需要事务的支持吗?此外,MyISAM 存储引擎的 另一个与众不同的地方是,它的缓冲池只缓存(cache)索引文件,而不缓存数据文件,这与 大多数的数据库都不相同。
```

**3、NDB 存储引擎**

```
MySQL AB 公司从 Sony Ericsson 公司收购了 NDB 存储引擎。 NDB 存储引擎是一个集群存储引擎,类似于 Oracle 的 RAC 集群,不过与 Oracle RAC 的 share everything 结构不同的是,其结构是 share nothing 的集群架构,因此能提供更高级别的 高可用性。NDB 存储引擎的特点是数据全部放在内存中(从 5.1 版本开始,可以将非索引数 据放在磁盘上),因此主键查找(primary key lookups)的速度极快,并且能够在线添加 NDB 数据存储节点(data node)以便线性地提高数据库性能。由此可见,NDB 存储引擎是高可用、 高性能、高可扩展性的数据库集群系统,其面向的也是 OLTP 的数据库应用类型。
```

**4、Memory 存储引擎**

```
正如其名,Memory 存储引擎中的数据都存放在内存中,数据库重 启或发生崩溃,表中的数据都将消失。它非常适合于存储 OLTP 数据库应用中临时数据的临时表,也可以作为 OLAP 数据库应用中数据仓库的维度表。Memory 存储引擎默认使用哈希 索引,而不是通常熟悉的 B+ 树索引。
```

**5、Infobright 存储引擎**

```
第三方的存储引擎。其特点是存储是按照列而非行的,因此非常 适合 OLAP 的数据库应用。其官方网站是 http://www.infobright.org/,上面有不少成功的数据 仓库案例可供分析。
```

**6、NTSE 存储引擎**

```
网易公司开发的面向其内部使用的存储引擎。目前的版本不支持事务, 但提供压缩、行级缓存等特性,不久的将来会实现面向内存的事务支持。
```

**7、BLACKHOLE**

```
黑洞存储引擎，可以应用于主备复制中的分发主库。

MySQL 数据库还有很多其他存储引擎,上述只是列举了最为常用的一些引擎。如果 你喜欢,完全可以编写专属于自己的引擎,这就是开源赋予我们的能力,也是开源的魅力所在。
```

**使用存储引擎**

**建表时指定:**

```mysql
create table t1(id int)engine=innodb;
create table t4(id int)engine=myisam;
create table t2(id int)engine=memory;
create table t3(id int)engine=blackhole;

# memory、blackhole这两种存储引擎只有表结构，无数据
# memory，在重启mysql或者重启机器后，表内数据清空
# blackhole，往表内插入任何数据，都相当于丢入黑洞，表内永远不存记录

# 插入数据
insert into t1 values(1);
insert into t2 values(1);
insert into t3 values(1);
insert into t4 values(1);
```

#### 11.9.2 表的增删改查

表相当于文件，表中的一条记录就相当于文件的一行内容，不同的是，表中的一条记录有对应的标题，称为表的字段。

**1.创建表**

语法：

```mysql
create table 表名(
字段名1 类型[(宽度) 约束条件],
字段名2 类型[(宽度) 约束条件],
字段名3 类型[(宽度) 约束条件]
);

#注意：
1. 在同一张表中，字段名是不能相同
2. 宽度和约束条件可选
3. 字段名和类型是必须的
```

示例：

```mysql
create database db1 charset utf8;
use db1;
create table t1(  
    id int, 
    name varchar(50),
    sex enum('male','female'),
    age int(3)
    );
show tables;  # 查看db1库下所有表名
```

插入数据：

```mysql
insert into t1 values(1,'aaa',18,'male'),(2,'bbb',81,'female');
```

**注意：表的最后一个字段不加逗号！**

**2.删除表**

语法：

```mysql
DROP TABLE 表名;
```

**3.修改表**

语法：

```mysql
1. 修改表名
      ALTER TABLE 表名 
                          RENAME 新表名;

2. 增加字段
      ALTER TABLE 表名
                          ADD 字段名  数据类型 [完整性约束条件…],
                          ADD 字段名  数据类型 [完整性约束条件…];
      ALTER TABLE 表名
                          ADD 字段名  数据类型 [完整性约束条件…]  FIRST;
      ALTER TABLE 表名
                          ADD 字段名  数据类型 [完整性约束条件…]  AFTER 字段名;

3. 删除字段
      ALTER TABLE 表名 
                          DROP 字段名;

4. 修改字段
      ALTER TABLE 表名 
                          MODIFY  字段名 数据类型 [完整性约束条件…];
      ALTER TABLE 表名 
                          CHANGE 旧字段名 新字段名 旧数据类型 [完整性约束条件…];
      ALTER TABLE 表名 
                          CHANGE 旧字段名 新字段名 新数据类型 [完整性约束条件…];
```

示例：

```mysql
1. 修改存储引擎
mysql> alter table service 
    -> engine=innodb;

2. 添加字段
mysql> alter table student10
    -> add name varchar(20) not null,
    -> add age int(3) not null default 22;

mysql> alter table student10
    -> add stu_num varchar(10) not null after name;                //添加name字段之后

mysql> alter table student10                        
    -> add sex enum('male','female') default 'male' first;          //添加到最前面

3. 删除字段
mysql> alter table student10
    -> drop sex;

mysql> alter table service
    -> drop mac;

4. 修改字段类型modify
mysql> alter table student10
    -> modify age int(3);
mysql> alter table student10
    -> modify id int(11) not null primary key auto_increment;    //修改为主键

5. 增加约束（针对已有的主键增加auto_increment）
mysql> alter table student10 modify id int(11) not null primary key auto_increment;
ERROR 1068 (42000): Multiple primary key defined

mysql> alter table student10 modify id int(11) not null auto_increment;
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

6. 对已经存在的表增加复合主键
mysql> alter table service2
    -> add primary key(host_ip,port);        

7. 增加主键
mysql> alter table student1
    -> modify name varchar(10) not null primary key;

8. 增加主键和自动增长
mysql> alter table student1
    -> modify id int not null primary key auto_increment;

9. 删除主键
a. 删除自增约束
mysql> alter table student10 modify id int(11) not null; 

b. 删除主键
mysql> alter table student10                                 
    -> drop primary key;
```

**4.查询表**

```mysql
describe t1;  # 查看表结构，可简写为desc 表名
+-------+-----------------------+------+-----+---------+-------+
| Field | Type                  | Null | Key | Default | Extra |
+-------+-----------------------+------+-----+---------+-------+
| id    | int(11)               | YES  |     | NULL    |       |
| name  | varchar(50)           | YES  |     | NULL    |       |
| sex   | enum('male','female') | YES  |     | NULL    |       |
| age   | int(3)                | YES  |     | NULL    |       |
+-------+-----------------------+------+-----+---------+-------+

MariaDB [db1]> show create table t1\G;  # 查看表详细结构，可加\G
```

**5.复制表**

```mysql
# 复制表结构＋记录 （key不会复制: 主键、外键和索引）
mysql> create table new_service select * from t1;

# 只复制表结构
mysql> select * from t1 where 1=2;  # 条件为假，查不到任何记录
Empty set (0.00 sec)
mysql> create table new1_service select * from t1 where 1=2;  
Query OK, 0 rows affected (0.00 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> create table t4 like t1;
```

#### 11.9.3 数据类型

MySQL中定义数据字段的类型对你数据库的优化是非常重要的。

MySQL支持多种类型，大致可以分为三类：数值、日期/时间和字符串(字符)类型。

##### 11.9.3.1 数值类型

**1.整数类型**

表示整数类型：TINYINT SMALLINT MEDIUMINT INT BIGINT

作用：存储年龄，等级，id，各种号码等

```mysql
=============tinyint=====================
tinyint[(m)] [unsigned] [zerofill]

小整数，数据类型用于保存一些范围的整数数值范围：
有符号：
-128 ～ 127
无符号：
0 ～ 255

PS： MySQL中无布尔值，使用tinyint(1)构造。

==============int=======================
int[(m)][unsigned][zerofill]

整数，数据类型用于保存一些范围的整数数值范围：
有符号：
-2147483648 ～ 2147483647
无符号：
0 ～ 4294967295


=============bigint=======================
bigint[(m)][unsigned][zerofill]
大整数，数据类型用于保存一些范围的整数数值范围：
有符号：
-9223372036854775808～9223372036854775807
无符号：
0～18446744073709551615
```

验证：

有符号tinyint：

```mysql
MariaDB [db1]> create table t1(x tinyint); #默认为有符号，即数字前有正负号
MariaDB [db1]> desc t1;
MariaDB [db1]> insert into t1 values
    -> (-129),
    -> (-128),
    -> (127),
    -> (128);
MariaDB [db1]> select * from t1;
+------+
| x    |
+------+
| -128 | #-129存成了-128
| -128 | #有符号，最小值为-128
|  127 | #有符号，最大值127
|  127 | #128存成了127
+------+
```

设置无符号tinyint：

```mysql
MariaDB [db1]> create table t2(x tinyint unsigned);
MariaDB [db1]> insert into t2 values
    -> (-1),
    -> (0),
    -> (255),
    -> (256);
MariaDB [db1]> select * from t2;
+------+
| x    |
+------+
|    0 | -1存成了0
|    0 | #无符号，最小值为0
|  255 | #无符号，最大值为255
|  255 | #256存成了255
+------+
```

有符号int：

```mysql
MariaDB [db1]> create table t3(x int); #默认为有符号整数
MariaDB [db1]> insert into t3 values
    -> (-2147483649),
    -> (-2147483648),
    -> (2147483647),
    -> (2147483648);
MariaDB [db1]> select * from t3;
+-------------+
| x           |
+-------------+
| -2147483648 | #-2147483649存成了-2147483648
| -2147483648 | #有符号，最小值为-2147483648
|  2147483647 | #有符号，最大值为2147483647
|  2147483647 | #2147483648存成了2147483647
+-------------+
```

无符号int：

```mysql
MariaDB [db1]> create table t4(x int unsigned);
MariaDB [db1]> insert into t4 values
    -> (-1),
    -> (0),
    -> (4294967295),
    -> (4294967296);
MariaDB [db1]> select * from t4;
+------------+
| x          |
+------------+
|          0 | #-1存成了0
|          0 | #无符号，最小值为0
| 4294967295 | #无符号，最大值为4294967295
| 4294967295 | #4294967296存成了4294967295
+------------+
```

有符号bigint：

```mysql
MariaDB [db1]> create table t6(x bigint);
MariaDB [db1]> insert into t5 values  
    -> (-9223372036854775809),
    -> (-9223372036854775808),
    -> (9223372036854775807),
    -> (9223372036854775808);

MariaDB [db1]> select * from t5;
+----------------------+
| x                    |
+----------------------+
| -9223372036854775808 |
| -9223372036854775808 |
|  9223372036854775807 |
|  9223372036854775807 |
+----------------------+
```

无符号bigint：

```mysql
MariaDB [db1]> create table t6(x bigint unsigned);
MariaDB [db1]> insert into t6 values  
    -> (-1),
    -> (0),
    -> (18446744073709551615),
    -> (18446744073709551616);

MariaDB [db1]> select * from t6;
+----------------------+
| x                    |
+----------------------+
|                    0 |
|                    0 |
| 18446744073709551615 |
| 18446744073709551615 |
+----------------------+
```

zerofill测试整数类型的显示宽度：

```mysql
MariaDB [db1]> create table t7(x int(3) zerofill);
MariaDB [db1]> insert into t7 values
    -> (1),
    -> (11),
    -> (111),
    -> (1111);
MariaDB [db1]> select * from t7;
+------+
| x    |
+------+
|  001 |
|  011 |
|  111 |
| 1111 | #超过宽度限制仍然可以存
+------+
```

注意：为该类型指定宽度时，仅仅只是指定查询结果的显示宽度，与存储范围无关，存储范围如下。

其实我们完全没必要为整数类型指定显示宽度，使用默认的就可以了。

默认的显示宽度，都是在最大值的基础上加1。

| 类型         | 大小                                     | 范围（有符号）                                               | 范围（无符号）                                               | 用途            |
| :----------- | :--------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :-------------- |
| TINYINT      | 1 字节                                   | (-128，127)                                                  | (0，255)                                                     | 小整数值        |
| SMALLINT     | 2 字节                                   | (-32 768，32 767)                                            | (0，65 535)                                                  | 大整数值        |
| MEDIUMINT    | 3 字节                                   | (-8 388 608，8 388 607)                                      | (0，16 777 215)                                              | 大整数值        |
| INT或INTEGER | 4 字节                                   | (-2 147 483 648，2 147 483 647)                              | (0，4 294 967 295)                                           | 大整数值        |
| BIGINT       | 8 字节                                   | (-9,223,372,036,854,775,808，9 223 372 036 854 775 807)      | (0，18 446 744 073 709 551 615)                              | 极大整数值      |
| FLOAT        | 4 字节                                   | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | 单精度 浮点数值 |
| DOUBLE       | 8 字节                                   | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |
| DECIMAL      | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 依赖于M和D的值                                               | 依赖于M和D的值                                               | 小数值          |

- int的存储宽度是4个Bytes，即32个bit，即2**32
- 无符号最大值为：4294967296-1
- 有符号最大值：2147483648-1
- 有符号和无符号的最大数字需要的显示宽度均为10，而针对有符号的最小值则需要11位才能显示完全，所以int类型默认的显示宽度为11是非常合理的
- 最后：整形类型，其实没有必要指定显示宽度，使用默认的就ok

**2.浮点类型**

定点数类型 DEC等同于DECIMAL

浮点类型：FLOAT DOUBLE

作用：存储薪资、身高、体重、体质参数等

```mysql
======================================
#FLOAT[(M,D)] [UNSIGNED] [ZEROFILL]

定义：
        单精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。m最大值为255，d最大值为30

有符号：
           -3.402823466E+38 to -1.175494351E-38,
           1.175494351E-38 to 3.402823466E+38
无符号：
           1.175494351E-38 to 3.402823466E+38


精确度： 
           **** 随着小数的增多，精度变得不准确 ****


======================================
#DOUBLE[(M,D)] [UNSIGNED] [ZEROFILL]

定义：
           双精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。m最大值为255，d最大值为30

有符号：
           -1.7976931348623157E+308 to -2.2250738585072014E-308
           2.2250738585072014E-308 to 1.7976931348623157E+308

无符号：
           2.2250738585072014E-308 to 1.7976931348623157E+308

精确度：
           ****随着小数的增多，精度比float要高，但也会变得不准确 ****

======================================
decimal[(m[,d])] [unsigned] [zerofill]

定义：
          准确的小数值，m是数字总个数（负号不算），d是小数点后个数。 m最大值为65，d最大值为30。


精确度：
           **** 随着小数的增多，精度始终准确 ****
           对于精确数值计算时需要用此类型
           decaimal能够存储精确值的原因在于其内部按照字符串存储。
```

验证

```mysql
mysql> create table t1(x float(256,31));
ERROR 1425 (42000): Too big scale 31 specified for column 'x'. Maximum is 30.
mysql> create table t1(x float(256,30));
ERROR 1439 (42000): Display width out of range for column 'x' (max = 255)
mysql> create table t1(x float(255,30)); #建表成功
Query OK, 0 rows affected (0.02 sec)

mysql> create table t2(x double(255,30)); #建表成功
Query OK, 0 rows affected (0.02 sec)

mysql> create table t3(x decimal(66,31));
ERROR 1425 (42000): Too big scale 31 specified for column 'x'. Maximum is 30.
mysql> create table t3(x decimal(66,30));
ERROR 1426 (42000): Too-big precision 66 specified for 'x'. Maximum is 65.
mysql> create table t3(x decimal(65,30)); #建表成功
Query OK, 0 rows affected (0.02 sec)

mysql> show tables;
+---------------+
| Tables_in_db1 |
+---------------+
| t1            |
| t2            |
| t3            |
+---------------+
rows in set (0.00 sec)



mysql> insert into t1 values(1.1111111111111111111111111111111); #小数点后31个1
Query OK, 1 row affected (0.01 sec)

mysql> insert into t2 values(1.1111111111111111111111111111111);
Query OK, 1 row affected (0.00 sec)

mysql> insert into t3 values(1.1111111111111111111111111111111);
Query OK, 1 row affected, 1 warning (0.01 sec)

mysql> select * from t1; #随着小数的增多，精度开始不准确
+----------------------------------+
| x                                |
+----------------------------------+
| 1.111111164093017600000000000000 |
+----------------------------------+
row in set (0.00 sec)

mysql> select * from t2; #精度比float要准确点，但随着小数的增多，同样变得不准确
+----------------------------------+
| x                                |
+----------------------------------+
| 1.111111111111111200000000000000 |
+----------------------------------+
row in set (0.00 sec)

mysql> select * from t3; #精度始终准确,d为30，于是只留了30位小数
+----------------------------------+
| x                                |
+----------------------------------+
| 1.111111111111111111111111111111 |
+----------------------------------+
row in set (0.00 sec)
```

##### 11.9.3.2 日期类型

表示时间值的日期和时间类型为DATETIME、DATE、TIMESTAMP、TIME和YEAR。

每个时间类型有一个有效值范围和一个"零"值，当指定不合法的MySQL不能表示的值时使用"零"值。

TIMESTAMP类型有专有的自动更新特性，将在后面描述。

作用：存储用户注册时间，文章发布时间，员工入职时间，出生时间，过期时间等

类型格式：

```mysql
        YEAR
            YYYY（1901/2155）

        DATE
            YYYY-MM-DD（1000-01-01/9999-12-31）

        TIME
            HH:MM:SS（'-838:59:59'/'838:59:59'）

        DATETIME

            YYYY-MM-DD HH:MM:SS（1000-01-01 00:00:00/9999-12-31 23:59:59    Y）

        TIMESTAMP

            YYYYMMDD HHMMSS（1970-01-01 00:00:00/2037 年某时）
```

示例：

```mysql
MariaDB [db1]> create table student(
    -> id int,
    -> name varchar(20),
    -> born_year year,
    -> birth date,
    -> class_time time,
    -> reg_time datetime);

MariaDB [db1]> insert into student values
    -> (1,'alex',"1995","1995-11-11","11:11:11","2017-11-11 11:11:11"),
    -> (2,'egon',"1997","1997-12-12","12:12:12","2017-12-12 12:12:12"),
    -> (3,'wsb',"1998","1998-01-01","13:13:13","2017-01-01 13:13:13");

MariaDB [db1]> select * from student;
+------+------+-----------+------------+------------+---------------------+
| id   | name | born_year | birth      | class_time | reg_time            |
+------+------+-----------+------------+------------+---------------------+
|    1 | alex |      1995 | 1995-11-11 | 11:11:11   | 2017-11-11 11:11:11 |
|    2 | egon |      1997 | 1997-12-12 | 12:12:12   | 2017-12-12 12:12:12 |
|    3 | wsb  |      1998 | 1998-01-01 | 13:13:13   | 2017-01-01 13:13:13 |
+------+------+-----------+------------+------------+---------------------+
```

注意：

```mysql
1. 单独插入时间时，需要以字符串的形式，按照对应的格式插入
2. 插入年份时，尽量使用4位值
3. 插入两位年份时，<=69，以20开头，比如50,  结果2050      
                >=70，以19开头，比如71，结果1971
MariaDB [db1]> create table t12(y year);
MariaDB [db1]> insert into t12 values  
    -> (50),
    -> (71);
MariaDB [db1]> select * from t12;
+------+
| y    |
+------+
| 2050 |
| 1971 |
+------+
```

| 类型      | 大小 (字节) | 范围                                                         | 格式                | 用途                     |
| :-------- | :---------- | :----------------------------------------------------------- | :------------------ | :----------------------- |
| DATE      | 3           | 1000-01-01/9999-12-31                                        | YYYY-MM-DD          | 日期值                   |
| TIME      | 3           | '-838:59:59'/'838:59:59'                                     | HH:MM:SS            | 时间值或持续时间         |
| YEAR      | 1           | 1901/2155                                                    | YYYY                | 年份值                   |
| DATETIME  | 8           | 1000-01-01 00:00:00/9999-12-31 23:59:59                      | YYYY-MM-DD HH:MM:SS | 混合日期和时间值         |
| TIMESTAMP | 4           | 1970-01-01 00:00:00/2038结束时间是第 **2147483647** 秒，北京时间 **2038-1-19 11:14:07**，格林尼治时间 2038年1月19日 凌晨 03:14:07 | YYYYMMDD HHMMSS     | 混合日期和时间值，时间戳 |

##### 11.9.3.3 字符串类型

字符串类型指CHAR、VARCHAR、BINARY、VARBINARY、BLOB、TEXT、ENUM和SET。该节描述了这些类型如何工作以及如何在查询中使用这些类型。

| 类型       | 大小                | 用途                            |
| :--------- | :------------------ | :------------------------------ |
| CHAR       | 0-255字节           | 定长字符串                      |
| VARCHAR    | 0-65535 字节        | 变长字符串                      |
| TINYBLOB   | 0-255字节           | 不超过 255 个字符的二进制字符串 |
| TINYTEXT   | 0-255字节           | 短文本字符串                    |
| BLOB       | 0-65 535字节        | 二进制形式的长文本数据          |
| TEXT       | 0-65 535字节        | 长文本数据                      |
| MEDIUMBLOB | 0-16 777 215字节    | 二进制形式的中等长度文本数据    |
| MEDIUMTEXT | 0-16 777 215字节    | 中等长度文本数据                |
| LONGBLOB   | 0-4 294 967 295字节 | 二进制形式的极大文本数据        |
| LONGTEXT   | 0-4 294 967 295字节 | 极大文本数据                    |

注意：char和varchar括号内的参数指的都是字符的长度。

```mysql
# char类型：定长，简单粗暴，浪费空间，存取速度快
    字符长度范围：0-255（一个中文是一个字符，是utf8编码的3个字节）
    存储：
        存储char类型的值时，会往右填充空格来满足长度
        例如：指定长度为10，存>10个字符则报错，存<10个字符则用空格填充直到凑够10个字符存储

    检索：
        在检索或者说查询时，查出的结果会自动删除尾部的空格，除非我们打开pad_char_to_full_length SQL模式（SET sql_mode = 'PAD_CHAR_TO_FULL_LENGTH';）

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# varchar类型：变长，精准，节省空间，存取速度慢
    字符长度范围：0-65535（如果大于21845会提示用其他类型 。mysql行最大限制为65535字节，字符编码为utf-8：https://dev.mysql.com/doc/refman/5.7/en/column-count-limit.html）
    存储：
        varchar类型存储数据的真实内容，不会用空格填充，如果'ab  ',尾部的空格也会被存起来
    强调：varchar类型会在真实数据前加1-2Bytes的前缀，该前缀用来表示真实数据的bytes字节数（1-2Bytes最大表示65535个数字，正好符合mysql对row的最大字节限制，即已经足够使用）
        如果真实的数据<255bytes则需要1Bytes的前缀（1Bytes=8bit 2**8最大表示的数字为255）
        如果真实的数据>255bytes则需要2Bytes的前缀（2Bytes=16bit 2**16最大表示的数字为65535）

    检索：
        尾部有空格会保存下来，在检索或者说查询时，也会正常显示包含空格在内的内容
```

备注：

```mysql
length： 查看字节数
char_length: 查看字符数
```

**char填充空格来满足固定长度，在检索或者说查询时，查出的结果会自动删除尾部的空格，然后修改sql_mode让其现出原形**

示例：

```mysql
mysql> create table t1(x char(5),y varchar(5));
Query OK, 0 rows affected (0.26 sec)

# char存5个字符，而varchar存4个字符
mysql> insert into t1 values('我是五 ','我是四 ');
Query OK, 1 row affected (0.05 sec)

mysql> SET sql_mode='';
Query OK, 0 rows affected, 1 warning (0.00 sec)

# 检索时，char查出的结果会自动删除尾部的空格，而varchar，存了多少，就显示多少
mysql> select x,char_length(x),y,char_length(y) from t1; 
+-----------+----------------+------------+----------------+
| x         | char_length(x) | y          | char_length(y) |
+-----------+----------------+------------+----------------+
| 我是五    |              3 | 我是四     |              4 |
+-----------+----------------+------------+----------------+
row in set (0.00 sec)

# 让char现出原形
mysql> SET sql_mode = 'PAD_CHAR_TO_FULL_LENGTH';
Query OK, 0 rows affected (0.00 sec)

# 这下子char原形毕露了......
mysql> select x,char_length(x),y,char_length(y) from t1;
+-------------+----------------+------------+----------------+
| x           | char_length(x) | y          | char_length(y) |
+-------------+----------------+------------+----------------+
| 我是五      |              5 | 我是四     |              4 |
+-------------+----------------+------------+----------------+
row in set (0.00 sec)


# char类型：3个中文字符+2个空格=11Bytes
# varchar类型:3个中文字符+1个空格=10Bytes
mysql> select x,length(x),y,length(y) from t1;
+-------------+-----------+------------+-----------+
| x           | length(x) | y          | length(y) |
+-------------+-----------+------------+-----------+
| 我是五      |        11 | 我是四     |        10 |
+-------------+-----------+------------+-----------+
row in set (0.00 sec)
```

**虽然 CHAR 和 VARCHAR 的存储方式不太相同,但是对于两个字符串的比较,都只比较其值,忽略 CHAR 值存在的右填充,即使将 SQL _MODE 设置为 PAD_CHAR_TO_FULL_ LENGTH 也一样,但这不适用于like.**

```mysql
mysql> CREATE TABLE names (myname CHAR(10));
Query OK, 0 rows affected (0.03 sec)

mysql> INSERT INTO names VALUES ('ike  ');
Query OK, 1 row affected (0.00 sec)

mysql> select * from names where myname='ike';
+------------+
| myname     |
+------------+
| ike        |
+------------+
1 row in set (0.00 sec)

mysql> select * from names where myname like 'ike';
+---------------------+-----------------------+
| myname LIKE 'Monty' | myname LIKE 'Monty  ' |
+---------------------+-----------------------+
|                   1 |                     0 |
+---------------------+-----------------------+
Empty set (0.00 sec)
```

总结：

![img](http://book.luffycity.com/python-book/assets/chapter8/%E5%AD%97%E7%AC%A6%E7%B1%BB%E5%9E%8B.png)

总结：

```
#常用字符串系列：char与varchar
规定长度后，char存取速度快，有几个存取几个，varchar每次存都需要先加1byte，增加了存取速度。
注：虽然varchar使用起来较为灵活，但是从整个系统的性能角度来说，char数据类型的处理速度更快，有时甚至可以超出varchar处理速度的50%。因此，用户在设计数据库时应当综合考虑各方面的因素，以求达到最佳的平衡

#其他字符串系列（效率：char>varchar>text）
TEXT系列 TINYTEXT TEXT MEDIUMTEXT LONGTEXT
BLOB 系列    TINYBLOB BLOB MEDIUMBLOB LONGBLOB 
BINARY系列 BINARY VARBINARY

text：text数据类型用于保存变长的大字符串，可以组多到65535 (2**16 − 1)个字符。
mediumtext：A TEXT column with a maximum length of 16,777,215 (2**24 − 1) characters.
longtext：A TEXT column with a maximum length of 4,294,967,295 or 4GB (2**32 − 1) characters.
```

##### 11.9.3.4 枚举类型与集合类型

字段的值只能在给定范围中选择，如单选框，多选框。

enum，单选：只能在给定的范围内选一个值，如：性别 sex 男male/女female

set，多选：在给定的范围内可以选择一个或一个以上的值（爱好1,爱好2,爱好3...）

示例：

```python
mysql> create table consumer(
    ->  id int,
    ->  name char(16),
    ->  sex enum('male','female','other'),  # 在指定范围内选一个
    ->  level enum('vip1','vip2','vip3'),  # 在指定范围内选一个
    ->  hobbies set('play','music','read','run')  # 在指定范围内选多个
    -> );
mysql> insert into consumer values
    -> (1,'java','male','vip2','music,read');
Query OK, 1 row affected (0.12 sec)

mysql> select * from consumer;
+------+------+------+-------+------------+
| id   | name | sex  | level | hobbies    |
+------+------+------+-------+------------+
|    1 | java | male | vip2  | music,read |
+------+------+------+-------+------------+
1 row in set (0.00 sec)

mysql> insert into consumer values
    -> (1,'python','xxxxx','vip2','music,read');
Query OK, 1 row affected, 1 warning (0.14 sec)

mysql> select * from consumer;
+------+--------+------+-------+------------+
| id   | name   | sex  | level | hobbies    |
+------+--------+------+-------+------------+
|    1 | java   | male | vip2  | music,read |
|    1 | python |      | vip2  | music,read |
+------+--------+------+-------+------------+
```

##### 11.9.3.5 约束

约束条件与数据类型的宽度一样，都是可选参数。

作用：用于保证数据的完整性和一致性

分为：

- PRIMARY KEY (PK) ，标识该字段为该表的主键，可以唯一的标识记录。
- FOREIGN KEY (FK)， 标识该字段为该表的外键。
- NOT NULL ，标识该字段不能为空。
- UNIQUE KEY (UK)，标识该字段的值是唯一的。
- AUTO_INCREMENT，标识该字段的值自动增长（整数类型，而且为主键）。
- DEFAULT，为该字段设置默认值。
- UNSIGNED，无符号。
- ZEROFILL，使用0填充。

说明：

```mysql
1. 是否允许为空，默认NULL，可设置NOT NULL，字段不允许为空，必须赋值
2. 字段是否有默认值，缺省的默认值是NULL，如果插入记录时不给字段赋值，此字段使用默认值
sex enum('male','female') not null default 'male'
age int unsigned NOT NULL default 20 必须为正值（无符号） 不允许为空 默认是20
3. 是否是key
主键 primary key
外键 foreign key
索引 (index,unique...)
```

**not null与default**：

是否可空，not null - 不可空，null - 可空。

默认值，创建列时可以指定默认值，当插入数据时如果未主动设置，则自动添加默认值。

示例：

not null：

```mysql
mysql> create table t2(id int not null);  # 设置字段id不为空
mysql> desc t2;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| id    | int(11) | NO   |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
mysql> insert into t2 values(); #不能插入空
ERROR 1364 (HY000): Field 'id' doesn't have a default value
```

null：

```mysql
mysql> create table t1(id int);  # id字段默认可以插入空
mysql> desc t1;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| id    | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
mysql> insert into t1 values(); # 可以插入空
```

default：

```mysql
# 设置id字段有默认值后，则无论id字段是null还是not null，都可以插入空，插入空默认填入default指定的默认值
mysql> create table t3(id int default 1);
mysql> alter table t3 modify id int not null default 1;
```

综合：

```mysql
mysql> create table student(
    -> name varchar(20) not null,
    -> age int(3) unsigned not null default 18,
    -> sex enum('male','female') default 'male',
    -> hobby set('play','study','read','music') default 'play,music'
    -> );
mysql> desc student;
+-------+------------------------------------+------+-----+------------+-------+
| Field | Type                               | Null | Key | Default    | Extra |
+-------+------------------------------------+------+-----+------------+-------+
| name  | varchar(20)                        | NO   |     | NULL       |       |
| age   | int(3) unsigned                    | NO   |     | 18         |       |
| sex   | enum('male','female')              | YES  |     | male       |       |
| hobby | set('play','study','read','music') | YES  |     | play,music |       |
+-------+------------------------------------+------+-----+------------+-------+
```

**unique**：

设置唯一约束，不能重复。

示例：

```mysql
# 单列唯一
# 方式一：
create table department(
	id int unique,
	name char(10) unique
);
#方式二：
create table department(
	id int,
	name char(10),
	unique(id),
	unique(name)
);
mysql> insert into department values(1,'IT');
Query OK, 1 row affected (0.00 sec)
mysql> insert into department values(1,'IT');
ERROR 1062 (23000): Duplicate entry '1' for key 'id'

# 联合唯一
create table services(
	id int,
	ip char(15),
	port int,
	unique(id),
	unique(ip,port)
);

mysql> insert into services values
    -> (1,'192.168.11.10',80),
    -> (2,'192.168.11.10',81),
    -> (3,'192.168.11.13',80);
Query OK, 3 rows affected (0.12 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> insert into services values
    -> (4,'192.168.11.10',80);
ERROR 1062 (23000): Duplicate entry '192.168.11.10-80' for key 'ip'
```

**primary key**：

primary key字段的值不为空且唯一，存储引擎（innodb）:对于innodb存储引擎来说，一张表内必须有一个主键。

一张表中可以：

- 单列做主键
- 多列做主键（复合主键）
- 一张表中只能有一个主键

示例：

```mysql
mysql> # 单列主键
mysql> create table t17(
    ->  id int primary key,
    ->  name char(16)
    -> );
Query OK, 0 rows affected (0.85 sec)

mysql> insert into t17 values
    -> (1,'egon'),
    -> (2,'alex');
Query OK, 2 rows affected (0.06 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> insert into t17 values
    -> (2,'wxx');
ERROR 1062 (23000): Duplicate entry '2' for key 'PRIMARY'

mysql> desc t17;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| id    | int(11)  | NO   | PRI | NULL    |       |
| name  | char(16) | YES  |     | NULL    |       |
+-------+----------+------+-----+---------+-------+
2 rows in set (0.01 sec)
mysql> create table t18(
    ->  id int not null unique,
    ->  name char(16)
    -> );
Query OK, 0 rows affected (0.40 sec)

mysql> desc t18;  # not null + unique 等同于 primary key
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| id    | int(11)  | NO   | PRI | NULL    |       |
| name  | char(16) | YES  |     | NULL    |       |
+-------+----------+------+-----+---------+-------+
2 rows in set (0.01 sec)

mysql> # 复合主键
mysql> create table t19(
    ->  ip char(15),
    ->  port int,
    ->  primary key(ip,port)
    -> );
Query OK, 0 rows affected (0.95 sec)

mysql> insert into t19 values
    -> ('1.1.1.1',80),
    -> ('1.1.1.1',81);
Query OK, 2 rows affected (0.04 sec)
Records: 2  Duplicates: 0  Warnings: 0
mysql> insert into t19 values
    -> ('1.1.1.1',82);
ERROR 1062 (23000): Duplicate entry '1.1.1.1-82' for key 'PRIMARY'
mysql> desc t19;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| ip    | char(15) | NO   | PRI |         |       |
| port  | int(11)  | NO   | PRI | 0       |       |
+-------+----------+------+-----+---------+-------+
2 rows in set (0.01 sec)
```

**auto_increment**：

约束字段为自动增长，被约束的字段必须同时被key约束。

示例：

```python
# id为自增长
mysql> create table t20(
    ->  id int primary key auto_increme
    ->  name char(16)
    -> );
Query OK, 0 rows affected (0.38 sec)
mysql> desc t20;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(11)  | NO   | PRI | NULL    | auto_increment |
| name  | char(16) | YES  |     | NULL    |                |
+-------+----------+------+-----+---------+----------------+
2 rows in set (0.01 sec)

mysql> insert into t20(name) values
    -> ('egon'),
    -> ('alex'),
    -> ('wxx');
Query OK, 3 rows affected (0.12 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> insert into t20(id,name) values
    -> (7,'yuanhao');
Query OK, 1 row affected (0.12 sec)

# 指定id后，在指定的基础上自增长
mysql> insert into t20(name) values
    -> ('egon1'),
    -> ('egon2'),
    -> ('egon3');
Query OK, 3 rows affected (0.06 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from t20;
+----+---------+
| id | name    |
+----+---------+
|  1 | egon    |
|  2 | alex    |
|  3 | wxx     |
|  7 | yuanhao |
|  8 | egon1   |
|  9 | egon2   |
| 10 | egon3   |
+----+---------+
7 rows in set (0.00 sec)
```

修改步长及偏移量：

强调：起始偏移量<=步长

```mysql
show variables like 'auto_inc%';

#步长：
auto_increment_increment默认为1
#起始偏移量
auto_increment_offset默认1

#设置步长
set session auto_increment_increment=5;
set global auto_increment_increment=5;

#设置起始偏移量
set global auto_increment_offset=3;
强调：起始偏移量<=步长

mysql> show variables like 'auto_inc%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| auto_increment_increment | 5     |
| auto_increment_offset    | 3     |
+--------------------------+-------+
2 rows in set (0.00 sec)

create table t21(
	id int primary key auto_increment,
	name char(16)
);

insert into t21(name) values
('egon'),
('alex'),
('wxx'),
('yxx');
mysql> select * from t21;
+----+------+
| id | name |
+----+------+
|  3 | egon |
|  8 | alex |
| 13 | wxx  |
| 18 | yxx  |
+----+------+
```

清空表：

```mysql
# 如果有自增id，新增的数据，仍然是以删除前的最后一样作为起始。
mysql> delete from t20;
Query OK, 1 row affected (0.10 sec)

mysql> show create table t20 \G;
*************************** 1. row ***************************
       Table: t20
Create Table: CREATE TABLE `t20` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(16) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8
1 row in set (0.00 sec)

ERROR:
No query specified

mysql> select * from t20;
Empty set (0.00 sec)

mysql>  insert into t20(name) values
    ->  ('xxx');
Query OK, 1 row affected (0.21 sec)

mysql> select * from t20;
+----+------+
| id | name |
+----+------+
|  2 | xxx  |
+----+------+

# 数据量大，删除速度比上一条快，且直接从零开始，
mysql> truncate t20;
Query OK, 0 rows affected (0.46 sec)

mysql> insert into t20(name) values
    ->  ('xxx');
Query OK, 1 row affected (0.14 sec)

mysql> select * from t20;
+----+------+
| id | name |
+----+------+
|  1 | xxx  |
+----+------+
1 row in set (0.00 sec)
```

**foreign key**：

建立表之间的关系。

```mysql
# 建立表关系
# 先建被关联的表,并且保证被关联的字段唯一
create table dep(
	id int primary key,
	name char(16),
	comment char(50)
);

#再建立关联的表
create table emp(
	id int primary key,
	name char(10),
	sex enum('male','female'),
	dep_id int,
	foreign key(dep_id) references dep(id) 
	on delete cascade  # 同步删除
	on update cascade  # 同步更新
);
# 插入数据
# 先往被关联表插入记录
insert into dep values
(1,"IT","技术能力有限部门"),
(2,"销售","销售能力不足部门"),
(3,"财务","花钱特别多部门");

# 再往关联表插入记录
insert into emp values
(1,'egon','male',1),
(2,'alex','male',1),
(3,'wupeiqi','female',2),
(4,'yuanhao','male',3),
(5,'jinximn','male',2);

# 删除数据
delete from emp where dep_id=1;
delete from dep where id=1;
# 没有同步操作的情况下，先删/更新除关联的数据，再删除/更新被关联的数据，删除/更新表也是。
# 同步的情况下，删除/更新关联的数据，被关联的表也跟着删除/更新数据，删除/更新表也是。
```

**建表之间的关系**：

- 多对一
    - 左表的多条记录对应右表的一条记录，右表的多条记录对应左表的一条记录
    - 关联方式：foreign key
- 多对多
    - 左表的多条记录对应右表的多条记录，右表的多条记录对应左表的多条记录
    - 关联方式：foreign key + 一张新的表
- 一对一
    - 左表的一条记录对应右表的一条记录，右表的一条记录对应左表的一条记录
    - 关联方式：foreign key + unique

示例：多对一

```mysql
# 建表
create table press(
id int primary key auto_increment,
name varchar(20)
);

create table book(
id int primary key auto_increment,
name varchar(20),
press_id int not null,
foreign key(press_id) references press(id)
on delete cascade
on update cascade
);
# 建数据
insert into press(name) values
('北京工业地雷出版社'),
('人民音乐不好听出版社'),
('知识产权没有用出版社')
;

insert into book(name,press_id) values
('九阳神功',1),
('九阴真经',2),
('九阴白骨爪',2),
('独孤九剑',3),
('降龙十巴掌',2),
('葵花宝典',3)
;
```

示例：多对多

```mysql
# 建表
create table author(
id int primary key auto_increment,
name varchar(20)
);
# 这张表就存放作者表与书表的关系，即查询二者的关系查这表就可以了
create table author2book(
id int not null unique auto_increment,
author_id int not null,
book_id int not null,
constraint fk_author foreign key(author_id) references author(id)
on delete cascade
on update cascade,
constraint fk_book foreign key(book_id) references book(id)
on delete cascade
on update cascade,
primary key(author_id,book_id)
);

# 建数据
# 插入四个作者，id依次排开
insert into author(name) values('aa'),('bb'),('cc'),('dd');
# 每个作者与自己的代表作如下
aa: 
九阳神功
九阴真经
九阴白骨爪
独孤九剑
降龙十巴掌
葵花宝典
bb: 
九阳神功
葵花宝典
cc:
独孤九剑
降龙十巴掌
葵花宝典
dd:
九阳神功

insert into author2book(author_id,book_id) values
(1,1),
(1,2),
(1,3),
(1,4),
(1,5),
(1,6),
(2,1),
(2,6),
(3,4),
(3,5),
(3,6),
(4,1)
;
```

示例：一对一

```mysql
# 建表
create table customer(
id int primary key auto_increment,
name varchar(20) not null,
qq varchar(10) not null,
phone char(16) not null
);
create table student(
id int primary key auto_increment,
class_name varchar(20) not null,
customer_id int unique,  # 该字段一定要是唯一的
foreign key(customer_id) references customer(id)  # 外键的字段一定要保证unique
on delete cascade
on update cascade
);

# 建数据
#增加客户
insert into customer(name,qq,phone) values
('李飞机','31811231',13811341220),
('王大炮','123123123',15213146809),
('守榴弹','283818181',1867141331),
('吴坦克','283818181',1851143312),
('赢火箭','888818181',1861243314),
('战地雷','112312312',18811431230)
;
#增加学生
insert into student(class_name,customer_id) values
('脱产3班',3),
('周末19期',4),
('周末19期',5)
;
```

#### 11.9.4 数据库操作

##### 11.9.4.1 数据的增删改

在MySQL管理软件中，可以通过SQL语句中的DML语言来实现数据的操作，包括：

- 使用INSERT实现数据的插入
- UPDATE实现数据的更新
- 使用DELETE实现数据的删除
- 使用SELECT查询数据以及。

**插入数据INSERT**：

语法：

```mysql
1. 插入完整数据（顺序插入）
    语法一：
    INSERT INTO 表名(字段1,字段2,字段3…字段n) VALUES(值1,值2,值3…值n);

    语法二：
    INSERT INTO 表名 VALUES (值1,值2,值3…值n);

2. 指定字段插入数据
    语法：
    INSERT INTO 表名(字段1,字段2,字段3…) VALUES (值1,值2,值3…);

3. 插入多条记录
    语法：
    INSERT INTO 表名 VALUES
        (值1,值2,值3…值n),
        (值1,值2,值3…值n),
        (值1,值2,值3…值n);

4. 插入查询结果
    语法：
    INSERT INTO 表名(字段1,字段2,字段3…字段n) 
                    SELECT (字段1,字段2,字段3…字段n) FROM 表2
                    WHERE …;
```

**更新数据UPDATE**：

语法：

```mysql
语法：
    UPDATE 表名 SET
        字段1=值1,
        字段2=值2,
        WHERE CONDITION;

示例：
    update student set class_name='全栈开发' where id=1;
```

**删除数据DELETE**：

语法：

```mysql
语法：
    DELETE FROM 表名 
        WHERE CONITION;

示例：
    DELETE FROM sutdent 
        WHERE id=1;
```

##### 11.9.4.2 单表查询

语法：

```mysql
SELECT 字段1,字段2. FROM 表名
                   WHERE 条件
                   GROUP BY 分组条件
                   HAVING 筛选
                   ORDER BY 排序字段
                   LIMIT 限制条数
```

**关键字执行的优先级：**

```mysql
重点中的重点：关键字的执行优先级
1.from  # 找到表:from
2.where  # 拿着where指定的约束条件，去表中过滤出数据
3.group by  # 将过滤出的数据进行分组group by，如果没有group by，则整体作为一组
4.having  # 将分组的结果进行having过滤
5.select  # 执行select
6.distinct # 去重
7.order by # 将结果按条件排序：order by
8.limit # 限制结果的显示条数
```

建表：

```mysql
# 建表
create table employee(
id int not null unique auto_increment,
name varchar(20) not null,
sex enum('male','female') not null default 'male', #大部分是男的
age int(3) unsigned not null default 28,
hire_date date not null,
post varchar(50),
post_comment varchar(100),
salary double(15,2),
office int, #一个部门一个屋子
depart_id int
);
# 建数据
#三个部门：教学，销售，运营
insert into employee(name,sex,age,hire_date,post,salary,office,depart_id) values
('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33,401,1), #以下是教学部
('alex','male',78,'20150302','teacher',1000000.31,401,1),
('wupeiqi','male',81,'20130305','teacher',8300,401,1),
('yuanhao','male',73,'20140701','teacher',3500,401,1),
('liwenzhou','male',28,'20121101','teacher',2100,401,1),
('jingliyang','female',18,'20110211','teacher',9000,401,1),
('jinxin','male',18,'19000301','teacher',30000,401,1),
('成龙','male',48,'20101111','teacher',10000,401,1),

('歪歪','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
('丫丫','female',38,'20101101','sale',2000.35,402,2),
('丁丁','female',18,'20110312','sale',1000.37,402,2),
('星星','female',18,'20160513','sale',3000.29,402,2),
('格格','female',28,'20170127','sale',4000.33,402,2),

('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
('程咬金','male',18,'19970312','operation',20000,403,3),
('程咬银','female',18,'20130311','operation',19000,403,3),
('程咬铜','male',18,'20150411','operation',18000,403,3),
('程咬铁','female',18,'20140512','operation',17000,403,3)
;
```

**简单查询**：

```mysql
#简单查询
    SELECT id,name,sex,age,hire_date,post,post_comment,salary,office,depart_id 
    FROM employee;

    SELECT * FROM employee;

    SELECT name,salary FROM employee;

#避免重复DISTINCT
    SELECT DISTINCT post FROM employee;    

#通过四则运算查询
    SELECT name, salary*12 FROM employee;
    SELECT name, salary*12 AS Annual_salary FROM employee;
    SELECT name, salary*12 Annual_salary FROM employee;

#定义显示格式
   CONCAT() 函数用于连接字符串
   SELECT CONCAT('姓名: ',name,'  年薪: ', salary*12)  AS Annual_salary 
   FROM employee;

   CONCAT_WS() 第一个参数为分隔符
   SELECT CONCAT_WS(':',name,salary*12)  AS Annual_salary 
   FROM employee;
```

**WHERE约束**：

where字句中可以使用：

- 比较运算符：><>= <= <> !=
- between 80 and 100 值在80到100之间
- in(80,90,100) 值是80或90或100
- ike 'egon%'
    pattern可以是%或_，
    %表示任意多字符
    _表示一个字符
- 逻辑运算符：在多个条件直接可以使用逻辑运算符 and or not

```mysql
# 1:单条件查询：查询岗位为sale的员工
    SELECT name FROM employee
        WHERE post='sale';

# 2:多条件查询：查询岗位为老师以及工资大于10000的员工
    SELECT name,salary FROM employee
        WHERE post='teacher' AND salary>10000;

# 3:关键字BETWEEN AND：查询工资在10000到20000之间的员工
    SELECT name,salary FROM employee 
        WHERE salary BETWEEN 10000 AND 20000;

    SELECT name,salary FROM employee 
        WHERE salary NOT BETWEEN 10000 AND 20000;

# 4:关键字IS NULL(判断某个字段是否为NULL不能用等号，需要用IS)
# 查询岗位描述为空的员工
    SELECT name,post_comment FROM employee 
        WHERE post_comment IS NULL;
# 查询岗位描述不为空的员工
    SELECT name,post_comment FROM employee 
        WHERE post_comment IS NOT NULL;

    SELECT name,post_comment FROM employee 
        WHERE post_comment=''; 注意''是空字符串，不是null
    ps：
        执行
        update employee set post_comment='' where id=2;
        再用上条查看，就会有结果了

# 5:关键字IN集合查询：查询工资是3000或4000或9000的员工
    SELECT name,salary FROM employee 
        WHERE salary=3000 OR salary=4000 OR salary=9000 ;
# 查询工资是3000或4000或9000的员工
    SELECT name,salary FROM employee 
        WHERE salary IN (3000,3500,9000) ;
# 查询工资是3000或4000或9000之外的员工
    SELECT name,salary FROM employee 
        WHERE salary NOT IN (3000,3500,4000,9000) ;

# 6:关键字LIKE模糊查询
    通配符’%’：查询名字包括eg的员工信息
    SELECT * FROM employee 
            WHERE name LIKE 'eg%';

    通配符’_’：查询名字开头是al的四个字的员工信息
    SELECT * FROM employee 
            WHERE name LIKE 'al__';
```

**分组查询**：

什么是分组，为什么进行分组？

- 分组发生在where之后，即分组是基于where之后得到的记录而进行的

- 分组指的是：将所有记录按照某个相同字段进行归类，比如针对员工信息表的职位分组，或者按照性别进行分组等。

- 为何要分组呢？
        以组为单位进行统计

    ​	‘每’这个字后面的字段就是我们分组的依据

```mysql
# 分组之后，只能取分组的字段，以及每个组聚合结果
set global sql_mode="ONLY_FULL_GROUP_BY"; 
```

```mysql
单独使用GROUP BY关键字分组
    SELECT post FROM employee GROUP BY post;
    注意：我们按照post字段分组，那么select查询的字段只能是post，想要获取组内的其他相关信息，需要借助函数

GROUP BY关键字和GROUP_CONCAT()函数一起使用
    SELECT post,GROUP_CONCAT(name) FROM employee GROUP BY post;#按照岗位分组，并查看组内成员名
    SELECT post,GROUP_CONCAT(name) as emp_members FROM employee GROUP BY post;

GROUP BY与聚合函数一起使用
    select post,count(id) as count from employee group by post;#按照岗位分组，并查看每个组有多少人
```

示例：

```mysql
mysql> select * from emp group by post; 
+----+------+--------+-----+------------+----------------------------+--------------+------------+--------+-----------+
| id | name | sex    | age | hire_date  | post                       | post_comment | salary     | office | depart_id |
+----+------+--------+-----+------------+----------------------------+--------------+------------+--------+-----------+
| 14 | 张野 | male   |  28 | 2016-03-11 | operation                  | NULL         |   10000.13 |    403 |         3 |
|  9 | 歪歪 | female |  48 | 2015-03-11 | sale                       | NULL         |    3000.13 |    402 |         2 |
|  2 | alex | male   |  78 | 2015-03-02 | teacher                    | NULL         | 1000000.31 |    401 |         1 |
|  1 | egon | male   |  18 | 2017-03-01 | 老男孩驻沙河办事处外交大使 | NULL         |    7300.33 |    401 |         1 |
+----+------+--------+-----+------------+----------------------------+--------------+------------+--------+-----------+
rows in set (0.00 sec)


#由于没有设置ONLY_FULL_GROUP_BY,于是也可以有结果，默认都是组内的第一条记录，但其实这是没有意义的

mysql> set global sql_mode='ONLY_FULL_GROUP_BY';
Query OK, 0 rows affected (0.00 sec)

mysql> quit #设置成功后，一定要退出，然后重新登录方可生效
Bye

mysql> use db1;
Database changed
mysql> select * from emp group by post; #报错
ERROR 1055 (42000): 'db1.emp.id' isn't in GROUP BY
mysql> select post,count(id) from emp group by post; #只能查看分组依据和使用聚合函数
+----------------------------+-----------+
| post                       | count(id) |
+----------------------------+-----------+
| operation                  |         5 |
| sale                       |         5 |
| teacher                    |         7 |
| 老男孩驻沙河办事处外交大使 |         1 |
+----------------------------+-----------+
rows in set (0.00 sec)
```

强调：

```mysql
如果我们用unique的字段作为分组的依据，则每一条记录自成一组，这种分组没有意义
多条记录之间的某个字段值相同，该字段通常用来作为分组的依据
```

**聚合函数**：

- max
- min
- avg
- sum
- count

强调：没有group by则默认整体算作一组

示例：

```mysql
# 1.查询岗位名以及岗位包含的所有员工名字
select post,group_concat(name) from employee group by post;
# 2.查询岗位名以及各岗位内包含的员工个数
select post,count(id) from employee group by post;
# 3.查询公司内男员工和女员工的个数
select sex,count(id) from employee group by sex;
# 4.查询岗位名以及各岗位的平均薪资
select post,avg(salary) from employee group by post;
5.查询岗位名以及各岗位的最高薪资
# select post,max(salary) from employee group by post;
6.查询岗位名以及各岗位的最低薪资
# select post,min(salary) from employee group by post;
7.查询男员工与男员工的平均薪资，女员工与女员工的平均薪资
# select sex,avg(salary) from employee group by sex;
```

**HAVING过滤**：

having和where的区别：

- 执行优先级：where > group by > having
- Where 发生在分组group by之前，因而Where中可以有任意字段，但是绝对不能使用聚合函数。
- Having发生在分组group by之后，因而Having中可以使用分组的字段，无法直接取到其他字段,可以使用聚合函数。

```mysql
# 1.查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
select post,group_concat(name),count(id) from employee group by post having count(id) < 2;
# 2.查询各岗位平均薪资大于10000的岗位名、平均工资
select post,avg(salary) from employee group by post having avg(salary) > 10000;
# 3.查询各岗位平均薪资大于10000且小于20000的岗位名、平均工资
# select post,avg(salary) from employee group by post having avg(salary) > 10000 and avg(salary) <20000;
```

**排序查询**：

```mysql
按单列排序：
    SELECT * FROM employee ORDER BY salary;
    SELECT * FROM employee ORDER BY salary ASC;  # 升序
    SELECT * FROM employee ORDER BY salary DESC;  # 降序

按多列排序:先按照age排序，如果年纪相同，则按照薪资排序
    SELECT * from employee
        ORDER BY age,
        salary DESC;
```

示例：

```mysql
# 1.查询所有员工信息，先按照age升序排序，如果age相同则按照hire_date降序排序
select * from employee ORDER BY age asc,hire_date desc;
# 2.查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资升序排列
select post,avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) asc;
# 3.查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资降序排列
select post,avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) desc;
```

**限制查询的记录数:LIMIT**：

```mysql
示例：
    SELECT * FROM employee ORDER BY salary DESC 
        LIMIT 3;                    #默认初始位置为0 

    SELECT * FROM employee ORDER BY salary DESC
        LIMIT 0,5; #从第0开始，即先查询出第一条，然后包含这一条在内往后查5条

    SELECT * FROM employee ORDER BY salary DESC
        LIMIT 5,5; #从第5开始，即先查询出第6条，然后包含这一条在内往后查5条
```

示例：

```mysql
# 显示第1-5条数据
mysql> select * from  employee limit 0,5;
# 显示第6-10条数据
mysql> select * from  employee limit 5,5;
# 显示第11-15条数据
mysql> select * from  employee limit 10,5;

```

**正则表达式查询**：

```mysql
SELECT * FROM employee WHERE name REGEXP '^ale';

SELECT * FROM employee WHERE name REGEXP 'on$';
```

##### 11.9.4.3 多表查询

**语法**：

```mysql
SELECT 字段列表
    FROM 表1 INNER|LEFT|RIGHT JOIN 表2
    ON 表1.字段 = 表2.字段;
```

**建表**：

```mysql
# 建表
create table department(
id int,
name varchar(20) 
);

create table employee(
id int primary key auto_increment,
name varchar(20),
sex enum('male','female') not null default 'male',
age int,
dep_id int
);

# 插入数据
insert into department values
(200,'技术'),
(201,'人力资源'),
(202,'销售'),
(203,'运营');

insert into employee(name,sex,age,dep_id) values
('egon','male',18,200),
('alex','female',48,201),
('wupeiqi','male',38,201),
('yuanhao','female',28,202),
('liwenzhou','male',18,200),
('jingliyang','female',18,204)
;

# 查看表结构和数据
mysql> desc department;
+-------+-------------+------+-----+---------+-------+
| Field | Type | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id | int(11) | YES | | NULL | |
| name | varchar(20) | YES | | NULL | |
+-------+-------------+------+-----+---------+-------+

mysql> desc employee;
+--------+-----------------------+------+-----+---------+----------------+
| Field | Type | Null | Key | Default | Extra |
+--------+-----------------------+------+-----+---------+----------------+
| id | int(11) | NO | PRI | NULL | auto_increment |
| name | varchar(20) | YES | | NULL | |
| sex | enum('male','female') | NO | | male | |
| age | int(11) | YES | | NULL | |
| dep_id | int(11) | YES | | NULL | |
+--------+-----------------------+------+-----+---------+----------------+
```

**1.内连接**：只连接匹配的行，找两张表共有的部分

```mysql
mysql> select employee.id,employee.name,employee.age,employee.sex,department.name from employee inner join department on employee.dep_id=department.id; 
+----+-----------+------+--------+--------------+
| id | name      | age  | sex    | name         |
+----+-----------+------+--------+--------------+
|  1 | egon      |   18 | male   | 技术         |
|  2 | alex      |   48 | female | 人力资源     |
|  3 | wupeiqi   |   38 | male   | 人力资源     |
|  4 | yuanhao   |   28 | female | 销售         |
|  5 | liwenzhou |   18 | male   | 技术         |
+----+-----------+------+--------+--------------+
```

**2.左外连接**：优先显示左表全部记录，在内连接的基础上增加左边有右边没有的结果

```mysql
mysql> select employee.id,employee.name,department.name as depart_name from employee left join department on employee.dep_id=department.id;
+----+------------+--------------+
| id | name       | depart_name  |
+----+------------+--------------+
|  1 | egon       | 技术         |
|  5 | liwenzhou  | 技术         |
|  2 | alex       | 人力资源     |
|  3 | wupeiqi    | 人力资源     |
|  4 | yuanhao    | 销售         |
|  6 | jingliyang | NULL         |
+----+------------+--------------+
```

**3.右外连接**：优先显示右表全部记录，在内连接的基础上增加右边有左边没有的结果

```mysql
mysql> select employee.id,employee.name,department.name as depart_name from employee right join department on employee.dep_id=department.id;
+------+-----------+--------------+
| id   | name      | depart_name  |
+------+-----------+--------------+
|    1 | egon      | 技术         |
|    2 | alex      | 人力资源     |
|    3 | wupeiqi   | 人力资源     |
|    4 | yuanhao   | 销售         |
|    5 | liwenzhou | 技术         |
| NULL | NULL      | 运营         |
+------+-----------+--------------+
```

**4.全外连接**：显示左右两个表全部记录，在内连接的基础上增加左边有右边没有的和右边有左边没有的结果

```mysql
select * from employee left join department on employee.dep_id = department.id
union
select * from employee right join department on employee.dep_id = department.id
;
#查看结果
+------+------------+--------+------+--------+------+--------------+
| id   | name       | sex    | age  | dep_id | id   | name         |
+------+------------+--------+------+--------+------+--------------+
|    1 | egon       | male   |   18 |    200 |  200 | 技术         |
|    5 | liwenzhou  | male   |   18 |    200 |  200 | 技术         |
|    2 | alex       | female |   48 |    201 |  201 | 人力资源     |
|    3 | wupeiqi    | male   |   38 |    201 |  201 | 人力资源     |
|    4 | yuanhao    | female |   28 |    202 |  202 | 销售         |
|    6 | jingliyang | female |   18 |    204 | NULL | NULL         |
| NULL | NULL       | NULL   | NULL |   NULL |  203 | 运营         |
+------+------------+--------+------+--------+------+--------------+

#注意 union与union all的区别：union会去掉相同的纪录
```

##### 11.9.4.4 子查询

- 子查询是将一个查询语句嵌套在另一个查询语句中。
- 内层查询语句的查询结果，可以为外层查询语句提供查询条件。
- 子查询中可以包含：IN、NOT IN、ANY、ALL、EXISTS 和 NOT EXISTS等关键字。
- 还可以包含比较运算符：= 、 !=、> 、<等。

**1.带IN关键字的子查询**：

```mysql
#查询平均年龄在25岁以上的部门名
select id,name from department
    where id in 
        (select dep_id from employee group by dep_id having avg(age) > 25);

#查看技术部员工姓名
select name from employee
    where dep_id in 
        (select id from department where name='技术');

#查看不足1人的部门名
select name from department
    where id in 
        (select dep_id from employee group by dep_id having count(id) <=1);
```

**2.带比较运算符的子查询**：比较运算符：=、!=、>、>=、<、<=、<>

```mysql
#查询大于所有人平均年龄的员工名与年龄
mysql> select name,age from emp where age > (select avg(age) from emp);

#查询大于部门内平均年龄的员工名、年龄
select t1.name,t1.age from emp t1
inner join 
(select dep_id,avg(age) avg_age from emp group by dep_id) t2
on t1.dep_id = t2.dep_id
where t1.age > t2.avg_age;
```

**3.带EXISTS关键字的子查询**：

EXISTS关字键字表示存在。在使用EXISTS关键字时，内层查询语句不返回查询的记录。

而是返回一个真假值。True或False

当返回True时，外层查询语句将进行查询；当返回值为False时，外层查询语句不进行查询

```mysql
# department表中存在dept_id=200，Ture
mysql> select * from employee
    ->     where exists
    ->         (select id from department where id=200);
+----+------------+--------+------+--------+
| id | name       | sex    | age  | dep_id |
+----+------------+--------+------+--------+
|  1 | egon       | male   |   18 |    200 |
|  2 | alex       | female |   48 |    201 |
|  3 | wupeiqi    | male   |   38 |    201 |
|  4 | yuanhao    | female |   28 |    202 |
|  5 | liwenzhou  | male   |   18 |    200 |
|  6 | jingliyang | female |   18 |    204 |
+----+------------+--------+------+--------+

# department表中不存在dept_id=205，False
mysql> select * from employee
    ->     where exists
    ->         (select id from department where id=205);
Empty set (0.00 sec)
```

##### 11.9.4.5 权限管理

```mysql
# 授权表
user  # 该表放行的权限，针对：所有数据，所有库下所有表，以及表下的所有字段
db  # 该表放行的权限，针对：某一数据库，该数据库下的所有表，以及表下的所有字段
tables_priv  # 该表放行的权限。针对：某一张表，以及该表下的所有字段
columns_priv  # 该表放行的权限，针对：某一个字段

创建账号
# 本地账号
create user 'egon1'@'localhost' identified by '123'; # mysql -uegon1 -p123
# 远程帐号
create user 'egon2'@'192.168.31.10' identified by '123'; # mysql -uegon2 -p123 -h 服务端ip
create user 'egon3'@'192.168.31.%' identified by '123'; # mysql -uegon3 -p123 -h 服务端ip
create user 'egon3'@'%' identified by '123'; # mysql -uegon3 -p123 -h 服务端ip
```

示例：

```mysql
常用权限有：select,update,alter,delete
all可以代表除了grant之外的所有权限

# 针对所有库的授权:*.*
grant all on *.* to 'egon1'@'localhost';  # 在user表中可以查到egon1用户的所有权限
grant select on *.* to 'egon1'@'localhost';  # 只在user表中可以查到egon1用户的select权限
revoke select on *.* from 'egon1'@'localhost';  # 删除egon1表中的select权限

# 针对某一数据库：db1.*
grant select on db1.* to 'egon1'@'localhost';  # 只在db1表中可以查到egon1用户的select权限
revoke select on db1.* from 'egon1'@'localhost';  # 删除db1表中egon1用户的select权限

# 针对某一个表：db1.t2
grant select on db1.t2 to 'egon1'@'localhost';  # 只在tables_priv表中可以查到egon1用户的select权限
revoke select on db1.t2 from 'egon1'@'localhost';# 删除tables_priv表中的egon1用户的权限

# 针对某一个字段
grant select(id,name),update(age) on db1.t2 to 'egon1'@'localhost';  # 只在columns_priv表中可以查到egon1用户的id，name字段的查看权限，age的修改权限
```

### 11.10 pymysql模块

#### 11.10.1 pymsql基本使用方法

示例：

```python
# pip3 install pymysql
import pymysql

user = input('user>>: ').strip()
pwd = input('password>>: ').strip()

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='390252',
    db='db9',
    charset='utf8'
)

# 拿到游标，执行完默认以元组形式返回
cursor = conn.cursor()

# 执行sql语句，注意%s需要加引号
sql = 'select * from userinfo where user = "%s" and pwd="%s"' % (user, pwd)
# 受影响的行数
rows = cursor.execute(sql)

cursor.close()
conn.close()

# 进行判断
if rows:
    print('登录成功')
else:
    print('登录失败')
```

#### 11.10.2 sql注入

注意：符号--会注释掉它之后的sql

原理：就根据程序的字符串拼接name='%s'，我们输入一个***xxx' -- haha***,用我们输入的xxx加'在程序中拼接成一个判断条件name='***xxx' -- haha***'

示例：sql注入两种方式

```python
# 方式一：
# 1.sql注入之：用户存在，绕过密码
egon' -- 任意字符

# 方式二：
# 2.sql注入之：用户不存在，绕过用户与密码
xxx' or 1=1 -- 任意字符
```

以这两种方式登录都可以登录成功，第二种方式并且可以同时绕过用户名和密码。

解决方法：

```python
import pymysql

user = input('user>>: ').strip()
pwd = input('password>>: ').strip()

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='390252',
    db='db9',
    charset='utf8'
)

# 拿到游标
cursor = conn.cursor()

# 执行sql语句
# 注意%s需要去掉引号，因为pymysql会自动为我们加上
sql = 'select * from userinfo where user = %s and pwd=%s'  
# pymysql模块自动帮我们解决sql注入的问题，只要我们按照pymysql的规矩来
rows = cursor.execute(sql, (user, pwd))

cursor.close()
conn.close()

# 进行判断
if rows:
    print('登录成功')
else:
    print('登录失败')
```

#### 11.10.3 增、删、改

示例：插入一条数据

```python
import pymysql

user = input('user>>: ').strip()
pwd = input('password>>: ').strip()

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='390252',
    db='db9',
    charset='utf8'
)
# 拿游标
cursor = conn.cursor()

# 执行sql
# 增、删、改对应的sql语句
sql = 'insert into userinfo(user,pwd) values(%s, %s)'
rows = cursor.execute(sql, (user, pwd))
print(rows)

# 显示最后一条自增id的位置
print(cursor.lastrowid)

# 提交后才发现表中插入记录成功
conn.commit()

cursor.close()
conn.close()
```

示例：插入 多条记录

```python
import pymysql

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='390252',
    db='db9',
    charset='utf8'
)
# 拿游标
cursor = conn.cursor()

# 执行sql
# 增、删、改对应的sql语句
sql = 'insert into userinfo(user,pwd) values(%s, %s)'

# 插入多条记录
rows = cursor.executemany(sql, [('ike', '111'), ('egon', '222'), ('alex', '333')])

# 显示最后一条自增id的位置
print(cursor.lastrowid)

# 提交后才发现表中插入记录成功
conn.commit()

cursor.close()
conn.close()
```

#### 11.10.4 查

示例：

```python
import pymysql

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='390252',
    db='db9',
    charset='utf8'
)

cursor = conn.cursor(pymysql.cursors.DictCursor)

# 执行sql
# 执行sql语句，返回sql影响成功的行数rows,将结果放入一个集合，等待被查询
rows = cursor.execute('select * from userinfo;')

# 一行一行查
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

# 查指定行数的数据
print(cursor.fetchmany(2))

# 查询全部
print(cursor.fetchall())


cursor.scroll(2, mode='absolute')  # 相对绝对位置移动
print(cursor.fetchone())
cursor.scroll(1, mode='relative')  # 相对当前位置移动
print(cursor.fetchone())

cursor.close()
conn.close()
```

### 11.11 视图

视图是一个虚拟表（非真实存在），其本质是【根据SQL语句获取动态的数据集，并为其命名】，用户使用时只需使用【名称】即可获取结果集，可以将该结果集当做表来使用。

使用视图我们可以把查询过程中的临时表拿出来，用视图去实现，这样以后再想操作该临时表的数据时就无需重写复杂的sql了，直接去视图中查找即可，但视图有明显的效率问题，并且视图是存放在数据库中的，如果我们程序中使用的sql过分依赖数据库中的视图，即强耦合，那就意味着扩展sql极为不便，因此并不推荐使用！

示例：普通查询

```mysql
# 两张有关系的表
mysql> select * from course;
+-----+--------+------------+
| cid | cname  | teacher_id |
+-----+--------+------------+
|   1 | 生物   |          1 |
|   2 | 物理   |          2 |
|   3 | 体育   |          3 |
|   4 | 美术   |          2 |
+-----+--------+------------+
rows in set (0.00 sec)

mysql> select * from teacher;
+-----+-----------------+
| tid | tname           |
+-----+-----------------+
|   1 | 张磊老师        |
|   2 | 李平老师        |
|   3 | 刘海燕老师      |
|   4 | 朱云海老师      |
|   5 | 李杰老师        |
+-----+-----------------+
rows in set (0.00 sec)

# 查询李平老师教授的课程名
mysql> select cname from course where teacher_id = (select tid from teacher where tname='李平老师');
+--------+
| cname  |
+--------+
| 物理   |
| 美术   |
+--------+
rows in set (0.00 sec)

# 子查询出临时表，作为teacher_id等判断依据
select tid from teacher where tname='李平老师'
```

**1.创建视图**

示例：

```mysql
# 语法：CREATE VIEW 视图名称 AS  SQL语句
create view teacher_view as select tid from teacher where tname='李平老师';

# 查询李平老师教授的课程名的sql可以改写为
mysql> select cname from course where teacher_id = (select tid from teacher_view);
+--------+
| cname  |
+--------+
| 物理   |
| 美术   |
+--------+
rows in set (0.00 sec)

# 注意的问题：
# 1. 使用视图以后就无需每次都重写子查询的sql，但是这么效率并不高，还不如我们写子查询的效率高
# 2. 而且有一个致命的问题：视图是存放到数据库里的，如果我们程序中的sql过分依赖于数据库中存放的视图，那么意味着，一旦sql需要修改且涉及到视图的部分，则必须去数据库中进行修改，而通常在公司中数据库有专门的DBA负责，你要想完成修改，必须付出大量的沟通成本DBA可能才会帮你完成修改，极其地不方便！
```

**2.使用视图**

示例：

```mysql
# 修改视图，原始表也跟着改
mysql> select * from course;
+-----+--------+------------+
| cid | cname  | teacher_id |
+-----+--------+------------+
|   1 | 生物   |          1 |
|   2 | 物理   |          2 |
|   3 | 体育   |          3 |
|   4 | 美术   |          2 |
+-----+--------+------------+
rows in set (0.00 sec)

# 创建表course的视图
mysql> create view course_view as select * from course;
Query OK, 0 rows affected (0.52 sec)

mysql> select * from course_view;
+-----+--------+------------+
| cid | cname  | teacher_id |
+-----+--------+------------+
|   1 | 生物   |          1 |
|   2 | 物理   |          2 |
|   3 | 体育   |          3 |
|   4 | 美术   |          2 |
+-----+--------+------------+
rows in set (0.00 sec)

# 更新视图中的数据
mysql> update course_view set cname='xxx'; 
Query OK, 4 rows affected (0.04 sec)
Rows matched: 4  Changed: 4  Warnings: 0

# 往视图中插入数据
mysql> insert into course_view values(5,'yyy',2); 
Query OK, 1 row affected (0.03 sec)

# 发现原始表的记录也跟着修改了
mysql> select * from course;  
+-----+-------+------------+
| cid | cname | teacher_id |
+-----+-------+------------+
|   1 | xxx   |          1 |
|   2 | xxx   |          2 |
|   3 | xxx   |          3 |
|   4 | xxx   |          2 |
|   5 | yyy   |          2 |
+-----+-------+------------+
rows in set (0.00 sec)

# 我们不应该修改视图中的记录，而且在涉及多个表的情况下是根本无法修改视图中的记录的。
```

**3.修改视图**

示例：

```mysql
# 语法：ALTER VIEW 视图名称 AS SQL语句
mysql> alter view teacher_view as select * from course where cid>3;
Query OK, 0 rows affected (0.04 sec)

mysql> select * from teacher_view;
+-----+-------+------------+
| cid | cname | teacher_id |
+-----+-------+------------+
|   4 | xxx   |          2 |
|   5 | yyy   |          2 |
+-----+-------+------------+
rows in set (0.00 sec)
```

**4.删除视图**

示例：

```mysql
# 语法：DROP VIEW 视图名称

DROP VIEW teacher_view
```

### 11.12 触发器

使用触发器可以定制用户对表进行【增、删、改】操作时前后的行为，注意：没有查询！

**1.创建触发器**

语法：

```mysql
# 插入前
CREATE TRIGGER tri_before_insert_tb1 BEFORE INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 插入后
CREATE TRIGGER tri_after_insert_tb1 AFTER INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除前
CREATE TRIGGER tri_before_delete_tb1 BEFORE DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除后
CREATE TRIGGER tri_after_delete_tb1 AFTER DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新前
CREATE TRIGGER tri_before_update_tb1 BEFORE UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新后
CREATE TRIGGER tri_after_update_tb1 AFTER UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END
```

示例：

```mysql
# 准备表
CREATE TABLE cmd (
    id INT PRIMARY KEY auto_increment,
    USER CHAR (32),
    priv CHAR (10),
    cmd CHAR (64),
    sub_time datetime,  # 提交时间
    success enum ('yes', 'no')  # 0代表执行失败
);

CREATE TABLE errlog (
    id INT PRIMARY KEY auto_increment,
    err_cmd CHAR (64),
    err_time datetime
);

# 创建触发器
delimiter //
CREATE TRIGGER tri_after_insert_cmd AFTER INSERT ON cmd FOR EACH ROW
BEGIN
    IF NEW.success = 'no' THEN  # 等值判断只有一个等号
            INSERT INTO errlog(err_cmd, err_time) VALUES(NEW.cmd, NEW.sub_time) ;  # 必须加分号
      END IF ;  # 必须加分号
END//
delimiter ;


# 往表cmd中插入记录，触发触发器，根据IF的条件决定是否插入错误日志
INSERT INTO cmd (
    USER,
    priv,
    cmd,
    sub_time,
    success
)
VALUES
    ('egon','0755','ls -l /etc',NOW(),'yes'),
    ('egon','0755','cat /etc/passwd',NOW(),'no'),
    ('egon','0755','useradd xxx',NOW(),'no'),
    ('egon','0755','ps aux',NOW(),'yes');
    
# 插入后触发触发器！
# 查询错误日志，发现有两条
mysql> select * from errlog;
+----+-----------------+---------------------+
| id | err_cmd         | err_time            |
+----+-----------------+---------------------+
|  1 | cat /etc/passwd | 2017-09-14 22:18:48 |
|  2 | useradd xxx     | 2017-09-14 22:18:48 |
+----+-----------------+---------------------+
rows in set (0.00 sec)
```

**备注：特别的：NEW表示即将插入的数据行，OLD表示即将删除的数据行。**

**2.使用触发器**

触发器无法由用户直接调用，只针对于对表的【增/删/改】操作被动引发的。

**3.删除触发器**

```mysql
drop trigger tri_after_insert_cmd;
```

### 11.13 事务

事务用于将某些操作的多个SQL作为原子性操作，一旦有某一个出现错误，即可回滚到原来的状态，从而保证数据库数据完整性。

事务一般用于交易中，双方同时增减！

```mysql
# 准备表
create table user(
id int primary key auto_increment,
name char(32),
balance int
);

insert into user(name,balance)
values
('wsb',1000),
('egon',1000),
('ysb',1000);

# 原子操作，模仿一个买卖的场景
start transaction;
update user set balance=900 where name='wsb';  # 买东西支付100元
update user set balance=1010 where name='egon';  # 中介拿走10元
update user set balance=1090 where name='ysb';  # 卖家拿到90元
commit;

# 出现异常，回滚到初始状态
start transaction;
update user set balance=900 where name='wsb'; #买支付100元
update user set balance=1010 where name='egon'; #中介拿走10元
uppdate user set balance=1090 where name='ysb'; #卖家拿到90元,出现异常没有拿到
rollback;
commit;
mysql> select * from user;
+----+------+---------+
| id | name | balance |
+----+------+---------+
|  1 | wsb  |    1000 |
|  2 | egon |    1000 |
|  3 | ysb  |    1000 |
+----+------+---------+
rows in set (0.00 sec)
```

语法：

```
delimiter //
create procedure p4(
	out status int
)
BEGIN
	1. 声明如果出现异常则执行{
    set status = 1;
    rollback;
    }

开始事务
-- 由秦兵账户减去100
-- 方少伟账户加90
-- 张根账户加10
commit;
结束

set status = 2;


END //
delimiter ;
```

示例：

```mysql
delimiter //
create PROCEDURE p5(
    OUT p_return_code tinyint
)
BEGIN 
    DECLARE exit handler for sqlexception 
    BEGIN 
        -- ERROR 
        set p_return_code = 1; 
        rollback; 
    END; 

    DECLARE exit handler for sqlwarning 
    BEGIN 
        -- WARNING 
        set p_return_code = 2; 
        rollback; 
    END; 

    START TRANSACTION; 
        DELETE from tb1; #执行失败
        insert into blog(name,sub_time) values('yyy',now());
    COMMIT; 

    -- SUCCESS 
    set p_return_code = 0; #0代表执行成功

END //
delimiter ;
```

**在mysql中调用存储过程：**

```mysql
set @res=123;
call p5(@res);
select @res;
```

**在python中基于pymysql调用存储过程：**

```python
import pymysql

# 建立链接
conn = pymysql.connect(
    host='192.168.10.15',
    port=3306,
    user='root',
    password='123',
    db='db7',
    charset='utf8'
)

# 拿游标
cursor = conn.cursor()

# 执行sql
# cursor.callproc('p1')
# print(cursor.fetchall())

cursor.callproc('p2', (2, 4, 0))
# print(cursor.fetchall())

cursor.execute('select @_p2_2')
print(cursor.fetchone())

# 关闭
cursor.close()
conn.close()
```

### 11.14 存储过程

存储过程包含了一系列可执行的sql语句，存储过程存放于MySQL中，通过调用它的名字可以执行其内部的一堆sql。

优点：

- 用于替代程序写的SQL语句，实现程序与sql解耦
- 基于网络传输，传别名的数据量小，而直接传sql数据量大

缺点：

- 程序员扩展功能不方便

**程序与数据库结合使用的三种方式**

```python
# 方式一：
    MySQL：存储过程
    程序：调用存储过程

# 方式二：
    MySQL：
    程序：纯SQL语句

# 方式三：
    MySQL:
    程序：类和对象，即ORM（本质还是纯SQL语句）
```

**1.创建无参存储过程**

```mysql
delimiter //
create procedure p1()
BEGIN
	select * from db7.teacher;
END //
delimiter ;
```

```mysql
# MySQL中调用
call p1();
```

```python
# Python中调用
cursor.callproc('p1')
```

**2.创建有参存储过程**

```python
# 对于存储过程，可以接收参数，其参数有三类：

#in          仅用于传入参数用
#out        仅用于返回值用
#inout     既可以传入又可以当作返回值
```

```mysql
delimiter //
create procedure p2(in n1 int,in n2 int,out res int)
BEGIN
	select * from db7.teacher where tid > n1 and tid < n2;
	set res = 1;
END //
delimiter ;
```

```mysql
# MySQL中调用
set @x=0  # 0代表假（执行失败），1代表真（执行成功）
call p2(2,4,@x);
select @x;
```

```python
# Python中调用
cursor.callproc('p2',(2,4,0))# @_p2_0=2,@_p2_1=4,@_p2_2=0
cursor.execute('select @_p3_2')
cursor.fetchone()
```

**3.执行存储过程**

MySQL中执行：

```mysql
-- 无参数
call proc_name()

-- 有参数，全in
call proc_name(1,2)

-- 有参数，有in，out，inout
set @t1=0;
set @t2=3;
call proc_name(1,2,@t1,@t2)

执行存储过程

在MySQL中执行存储过程-- 无参数
call proc_name()

-- 有参数，全in
call proc_name(1,2)

-- 有参数，有in，out，inout
set @t1=0;
set @t2=3;
call proc_name(1,2,@t1,@t2)
```

Python中执行：

```python
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 执行存储过程
cursor.callproc('p1', args=(1, 22, 3, 4))
# 获取执行完存储的参数
cursor.execute("select @_p1_0,@_p1_1,@_p1_2,@_p1_3")
result = cursor.fetchall()

conn.commit()
cursor.close()
conn.close()

print(result)
```

**4.删除存储过程**

```mysql
drop procedure proc_name;
```

### 11.15 函数

MySQL中提供了许多内置函数例如：

**1.数学函数**：

```mysql
ROUND(x,y)
	返回参数x的四舍五入的有y位小数的值

RAND()
	返回０到１内的随机值,可以通过提供一个参数(种子)使RAND()随机数生成器生成一个指定的值。
```

**2.聚合函数**：

```mysql
AVG(col)返回指定列的平均值
COUNT(col)返回指定列中非NULL值的个数
MIN(col)返回指定列的最小值
MAX(col)返回指定列的最大值
SUM(col)返回指定列的所有值之和
GROUP_CONCAT(col) 返回由属于一组的列值连接组合而成的结果    
```

**3.字符串函数**：

```mysql
CHAR_LENGTH(str)
	# 返回值为字符串str 的长度，长度的单位为字符。一个多字节字符算作一个单字符。
CONCAT(str1,str2,...)
	# 字符串拼接，如有任何一个参数为NULL ，则返回值为 NULL。
CONCAT_WS(separator,str1,str2,...)
	# 字符串拼接（自定义连接符）
CONCAT_WS()不会忽略任何空字符串。 (然而会忽略所有的 NULL）。

CONV(N,from_base,to_base)
	# 进制转换
	# 例如：
		SELECT CONV('a',16,2); 表示将 a 由16进制转换为2进制字符串表示

FORMAT(X,D)
	# 将数字X 的格式写为'#,###,###.##',以四舍五入的方式保留小数点后 D 位， 并将结果以字符串的形式返回。若D为0, 则返回结果不带有小数点，或不含小数部分。
	# 例如：
		SELECT FORMAT(12332.1,4); 
		# 结果为： '12,332.1000' INSERT(str,pos,len,newstr)
            # 在str的指定位置插入字符串
            # pos：要替换位置其实位置
            #len：替换的长度
            # newstr：新字符串
            # 特别的：
            # 如果pos超过原字符串长度，则返回原字符串
            # 如果len超过原字符串长度，则由新字符串完全替换
INSTR(str,substr)
	# 返回字符串 str 中子字符串的第一个出现位置。

LEFT(str,len)
	#返回字符串str 从开始的len位置的子序列字符。

LOWER(str)
	# 变小写

UPPER(str)
	# 变大写

REVERSE(str)
	# 返回字符串 str ，顺序和字符顺序相反。

SUBSTRING(str,pos) , SUBSTRING(str FROM pos) SUBSTRING(str,pos,len) , SUBSTRING(str FROM pos FOR len)
# 不带有len参数的格式从字符串str返回一个子字符串，起始于位置 pos。带有len参数的格式从字符串str返	回一个长度同len字符相同的子字符串，起始于位置 pos。使用 FROM的格式为标准 SQL 语法。也可能对pos使用一个负值。假若这样，则子字符串的位置起始于字符串结尾的pos字符，而不是字符串的开头位置。在以下格式的函数中可以对pos使用一个负值。

# 示例：
mysql> SELECT SUBSTRING('Quadratically',5);
-> 'ratically'

mysql> SELECT SUBSTRING('foobarbar' FROM 4);
-> 'barbar'

mysql> SELECT SUBSTRING('Quadratically',5,6);
-> 'ratica'

mysql> SELECT SUBSTRING('Sakila', -3);
-> 'ila'

mysql> SELECT SUBSTRING('Sakila', -5, 3);
-> 'aki'

mysql> SELECT SUBSTRING('Sakila' FROM -4 FOR 2);
-> 'ki'
```

**4.日期和时间函数**：

```mysql
CURDATE()或CURRENT_DATE()  # 返回当前的日期
CURTIME()或CURRENT_TIME()  # 返回当前的时间
DAYOFWEEK(date)   # 返回date所代表的一星期中的第几天(1~7)
DAYOFMONTH(date)  # 返回date是一个月的第几天(1~31)
DAYOFYEAR(date)   # 返回date是一年的第几天(1~366)
DAYNAME(date)   # 返回date的星期名，如：SELECT DAYNAME(CURRENT_DATE);
FROM_UNIXTIME(ts,fmt)  # 根据指定的fmt格式，格式化UNIX时间戳ts
HOUR(time)   # 返回time的小时值(0~23)
MINUTE(time)   # 返回time的分钟值(0~59)
MONTH(date)   # 返回date的月份值(1~12)
MONTHNAME(date)   # 返回date的月份名，如：SELECT MONTHNAME(CURRENT_DATE);
NOW()    # 返回当前的日期和时间
QUARTER(date)   # 返回date在一年中的季度(1~4)，如SELECT QUARTER(CURRENT_DATE);
WEEK(date)   # 返回日期date为一年中第几周(0~53)
YEAR(date)   # 返回日期date的年份(1000~9999)

示例：重点
DATE_FORMAT(date,format) 根据format字符串格式化date值

mysql> SELECT DATE_FORMAT('2009-10-04 22:23:00', '%W %M %Y');
-> 'Sunday October 2009'
mysql> SELECT DATE_FORMAT('2007-10-04 22:23:00', '%H:%i:%s');
-> '22:23:00'
mysql> SELECT DATE_FORMAT('1900-10-04 22:23:00',
->                 '%D %y %a %d %m %b %j');
-> '4th 00 Thu 04 10 Oct 277'
mysql> SELECT DATE_FORMAT('1997-10-04 22:23:00',
->                 '%H %k %I %r %T %S %w');
-> '22 22 10 10:23:00 PM 22:23:00 00 6'
mysql> SELECT DATE_FORMAT('1999-01-01', '%X %V');
-> '1998 52'
mysql> SELECT DATE_FORMAT('2006-06-00', '%d');
-> '00'
```

**5.加密函数**：

```mysql
MD5()  # 计算字符串str的MD5校验和
PASSWORD(str)  # 返回字符串str的加密版本，这个加密过程是不可逆转的，和UNIX密码加密过程使用不同的算法。
```

**6.控制流函数**：

```mysql
CASE WHEN[test1] THEN [result1]...ELSE [default] END
 # 如果test1是真，则返回resultN1，否则返回default
CASE [test] WHEN[val1] THEN [result]...ELSE [default]END  
# 如果test和valN相等，则返回resultN，否则返回default

IF(test,t,f)   
# 如果test是真，返回t；否则返回f

IFNULL(arg1,arg2) 
# 如果arg1不是空，返回arg1，否则返回arg2

NULLIF(arg1,arg2) 
# 如果arg1=arg2返回NULL；否则返回arg1  
```

**7.自定义函数**：

函数中不要写sql语句（否则会报错），函数仅仅只是一个功能，是一个在sql中被应用的功能，若要想在begin...end...中写sql，用存储过程。

示例：

```mysql
delimiter //
create function f1(
    i1 int,
    i2 int)
returns int
BEGIN
    declare num int;
    set num = i1 + i2;
    return(num);
END //
delimiter ;
```

```mysql
elimiter //
create function f5(
    i int
)
returns int
begin
    declare res int default 0;
    if i = 10 then
        set res=100;
    elseif i = 20 then
        set res=200;
    elseif i = 30 then
        set res=300;
    else
        set res=400;
    end if;
    return res;
end //
delimiter ;
```

**8.删除函数**：

```mysql
drop function func_name;
```

**9.执行函数**：

```mysql
# 获取返回值
select UPPER('egon') into @res;
SELECT @res;

# 在查询中使用
select f1(11,nid) ,name from tb2;
```

### 11.16 流程控制

示例：

```mysql
delimiter //
CREATE PROCEDURE proc_if ()
BEGIN

    declare i int default 0;
    if i = 1 THEN
        SELECT 1;
    ELSEIF i = 2 THEN
        SELECT 2;
    ELSE
        SELECT 7;
    END IF;

END //
delimiter ;

if条件语句
```

**1.while循环**：

```mysql
delimiter //
CREATE PROCEDURE proc_while ()
BEGIN

    DECLARE num INT ;
    SET num = 0 ;
    WHILE num < 10 DO
        SELECT
            num ;
        SET num = num + 1 ;
    END WHILE ;

END //
delimiter ;
```

**2.repeat循环**：

```mysql
delimiter //
CREATE PROCEDURE proc_repeat ()
BEGIN

    DECLARE i INT ;
    SET i = 0 ;
    repeat
        select i;
        set i = i + 1;
        until i >= 5
    end repeat;

END //
delimiter ;
```

**3.loop循环**：

```mysql
BEGIN

    declare i int default 0;
    loop_label: loop

        set i=i+1;
        if i<8 then
            iterate loop_label;
        end if;
        if i>=10 then
            leave loop_label;
        end if;
        select i;
    end loop loop_label;

END
```

## 第十二章 前端开发

### 12.1 HTML

#### 12.1.1 HTML简介

超文本标记语言（英语：HyperText Markup Language，简称：HTML）是一种用于创建网页的标准标记语言。标记语言是一种将文本（Text）以及文本相关的其他信息结合起来，展现出关于文档结构和数据处理细节的计算机文字编码。与文本相关的其他信息（包括例如文本的结构和表示信息等）与原来的文本结合在一起，但是使用标记（markup）进行标识。可以使用 HTML 来建立自己的 WEB 站点，HTML 运行在浏览器上，由浏览器来解析。

#### 12.1.2 HTML文档的后缀名

- .html
- .htm

以上两种后缀名没有区别，都是静态网页后缀名，都可以使用。

#### 12.1.3 什么是HTML?

HTML 是用来描述网页的一种语言。

- HTML 指的是超文本标记语言: **H**yper**T**ext **M**arkup **L**anguage
- HTML 不是一种编程语言，而是一种**标记**语言
- 标记语言是一套**标记标签** (markup tag)
- HTML 使用标记标签来**描述**网页
- HTML 文档包含了HTML **标签**及**文本**内容
- HTML文档也叫做 **web 页面**

HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

- HTML 标签是由*尖括号*包围的关键词，比如` <html>`
- HTML 标签通常是*成对出现*的，结束标签比开始标签多了一个`/`，比如 `<b>` 和`</b>`
- 标签对中的第一个标签是*开始标签*，第二个标签是结束标签，也称为开放，闭合标签
- 标签之间是可以嵌套的。例如：`div`标签里面嵌套`p`标签的话，那么`</p>`必须放在`</div>`的前面。
- HTML标签不区分大小写，`<h1>`和`<H1>`是一样的，但是我们通常建议使用小写，因为大部分程序员都以小写为准

HTML 是用来描述网页的一种语言。

- HTML 指的是超文本标记语言: **H**yper**T**ext **M**arkup **L**anguage
- HTML 不是一种编程语言，而是一种**标记**语言
- 标记语言是一套**标记标签** (markup tag)
- HTML 使用标记标签来**描述**网页
- HTML 文档包含了HTML **标签**及**文本**内容
- HTML文档也叫做 **web 页面**

#### 12.1.4 HTML 标签特点

HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

- HTML 标签是由*尖括号*包围的关键词，比如` <html>`
- HTML 标签通常是*成对出现*的，结束标签比开始标签多了一个`/`，比如 `<b>` 和`</b>`
- 标签对中的第一个标签是*开始标签*，第二个标签是结束标签，也称为开放，闭合标签
- 标签之间是可以嵌套的。例如：`div`标签里面嵌套`p`标签的话，那么`</p>`必须放在`</div>`的前面。
- HTML标签不区分大小写，`<h1>`和`<H1>`是一样的，但是我们通常建议使用小写，因为大部分程序员都以小写为准

#### 12.1.5 HTML文档结构

​	下面是一个可视化的HTML页面结构：![前端HTML](j:/homework/%E5%89%8D%E7%AB%AF/Users/zhangzhiqiang/Desktop/web%E5%89%8D%E7%AB%AF/img/%E5%89%8D%E7%AB%AFHTML.png)

##### 12.1.5.1 HTML实例

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
	<title>HTML实例</title>
</head>
<body>
	<h1>标题1</h1>
	<p>段落1</p>

</body>
</html>
```

实例解析

- `<!DOCTYPE html>` 声明为 HTML5 文档
- `<html></html>`元素是 HTML 页面的根元素
- `<head> </head>`标签用于定义文档的头部，它是所有头部元素的容器。常见的头部元素有`<title>`、`<script>`、`<style>`、`<link>`和`<meta>`等标签，头部标签在下一节中会有详细介绍。
- `<title>` 元素描述了文档的标题
- `<body></body>`标签之间的内容是网页的主要内容，如`<h1>`、`<p>`、`<a>`、`<img>`等网页内容标签，在`<body>`标签中的内容（图中淡绿色部分内容）最终会在浏览器中显示出来。

#### 12.1.6 HTML注释

无论我们学习什么编程语言，一定要重视的就是注释。

HTML中注释的格式:

```html
<!--这里是注释的内容-->
```

注意： 注释中可以直接使用回车换行。

并且我们习惯用注释的标签把HTML代码包裹起来。如：

```html
<!-- xx部分 开始 -->
    这里放你xx部分的HTML代码
<!-- xx部分 结束 -->
```

HTML注释的注意事项：

1. HTML注释不支持嵌套。
2. HTML注释不能写在HTML标签中。

#### 12.1.7 head标签

`head`标签申明了文档的头部的信息，描述了文档的各种属性和信息，包括文档的标题、编码方式及URL等信息,这些信息大部分是用于提供索引,辩认或其他方面的应用（移动端）的等。 以下标签是可以用在`head`标签中的：

```html
<!DOCTYPE html>
<html>
<head>
	<title>HTML实例</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="">
	<style type="text/css"></style>
</head>
```

##### 12.1.7.1 title标签

`<title>`标签：在`<title>`和`</title`>标签之间的文字内容是网页的标题信息，它会显示在浏览器标签页的标题栏中。可以把它看成是一个网页的标题。主要用来告诉用户和搜索引擎这个网页的主要内容是什么，搜索引擎可以通过网页标题，迅速的判断出当前网页的主题。示例：

```html
<!DOCTYPE html>
<html>
	<head>
		<title>段落／语气／换行／无序／有序／定义／表格</title>
	</head>
</html>
```

![title图片](j:/homework/%E5%89%8D%E7%AB%AF/Users/zhangzhiqiang/Desktop/web%E5%89%8D%E7%AB%AF/img/title%E5%9B%BE%E7%89%87.png)

##### 12.1.7.2 meta标签

Meta标签介绍：

元素可提供有关页面的原信息（mata-information）,针对搜索引擎和更新频度的描述和关键词。

标签位于文档的头部，不包含任何内容。

提供的信息是用户不可见的。 meta标签的组成：meta标签共有两个属性，它们分别是http-equiv属性和name属性，不同的属性又有不同的参数值，这些不同的参数值就实现了不同的网页功能。

常用的meta标签：

- http-equiv属性

它用来向浏览器传达一些有用的信息，帮助浏览器正确地显示网页内容，与之对应的属性值为content，content中的内容其实就是各个参数的变量值。

```html
<!--重定向 2秒后跳转到对应的网址，注意分号-->
<meta http-equiv="refresh" content="2;URL=http://www.luffycity.com">
<!--指定文档的内容类型和编码类型 -->
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<!--告诉IE浏览器以最高级模式渲染当前网页-->
<meta http-equiv="x-ua-compatible" content="IE=edge">
```

- name属性

主要用于页面的关键字和描述，是写给搜索引擎看的，关键字可以有多个用 ‘,’号隔开，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的。

```html
<meta name="keywords" content="meta总结,html meta,meta属性,meta跳转">
<meta name="description" content="meta标签">
```

#### 12.1.8 其他标签

```html
<!--标题-->
<title>标题标签</title>
<!--icon图标（网站的图标）-->
<link rel="icon" href="fav.ico">
<!--定义内部样式表-->
<style></style>
<!--引入外部样式表文件-->
<link rel="stylesheet" href="mystyle.css">
<!--定义JavaScript代码或引入JavaScript文件-->
<script src="myscript.js"></script>
```

#### 12.1.9 body标签

想要在网页上展示出来的内容一定要放在`body`标签中。

`<h1>` - `<h6>` 标签可定义标题。`<h1>` 定义最大的标题。`<h6>` 定义最小的标题。 由于 h 元素拥有确切的语义，因此慎重地选择恰当的标签层级来构建文档的结构。不要利用标题标签来改变同一行中的字体大小。我们应当使用css来定义来达到漂亮的显示效果。 标题标签通常用来制作文章或网站的标题。

##### 12.1.9.1 标题标签`h1～h6`

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<h1>一级标题</h1>
  <h2>二级标题</h2>
	<h3>三级标题</h3>
	<h4>四级标题</h4>
	<h5>五级标题</h5>
	<h6>六级标题</h6>	
</body>
</html>
```

文本样式标签：主要对HTML页面中的文本进行修饰

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<h1>一级 <b>标题</b></h1>
	<h2>二级 <i>标题</i></h2>
	<h3>三级 <u>标题</u></h3>
	<h4>四级 <s>标题</s></h4>
	<h5>五级 <sup>标题</sup></h5>
	<h5>五级 <sub>标题</sub></h5>
	<h6> <em>六级</em> <strong>标题</strong></h6>	
</body>
</html>
```

总结：

```html
1. <b>加粗</b>
2. <i>斜体</i>
3. <u>下划线</u>
4. <s>删除线</s>
5. <sup>上标</sup>
6. <sub>下标</sub>
7. <strong>强调：斜体</strong>
8. <em>强调：粗体</em>
一般强调我们习惯用strong标签来强调
```

##### 12.1.9.2 段落标签`p`

`<p></p>`paragraph的简写。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<h2>段落标签</h2>
	<p>售后政策</p>
	<p>小米服务</p>
	<p>自主服务</p>
	<p>我不知道</p>
</body>
</html>
```

`<br>`标签用来将内容换行，其在HTML网页上的效果相当于我们平时使用word编辑文档时使用回车换行。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<h2>换行标签</h2>
	作为子民我愿以此身终生报效国家， <br>大丈夫建功立业何须活着返回家园。
</body>
</html>
```

##### 12.1.9.3 列表标签`ul`

`<ul>`：unordered lists的缩写 无序列表。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
   <!-- 无序列表 type可以定义无序列表的样式-->
    <ul type="circle">
        <li>我的账户</li>
        <li>我的订单</li>
        <li>我的优惠券</li>
        <li>我的收藏</li>
        <li>退出</li>
    </ul>
</body>
</html>
```

ul标签的属性：列表标识类型

- disc：实心圆(默认值)
- circle：空心圆
- square：实心矩形
- none：不显示标识

##### 12.1.9.4 列表标签`ol`

`<ol>`：ordered listsde的缩写 有序列表。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<!-- 有序列表 type可以定义有序列表的样式 -->
    <ol type="a">
        <li>我的账户</li>
        <li>我的订单</li>
        <li>我的优惠券</li>
        <li>我的收藏</li>
        <li>退出</li>
    </ol>
</body>
</html>
```

ol标签的属性：列表标识类型

- 1：数字
- a：小写字母
- A：大写字母
- i：小写罗马字符
- I：大写罗马字符

列表表示的起始编号默认为1

##### 12.1.9.5 列表标签`dl`

html `<dl> <dt> <dd>`是一组合标签，使用了dt dd最外层就必须使用dl包裹，此组合标签我们也又叫表格标签，与table表格类似组合标签，故名我们也叫dl表格。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<!-- <dl> 标签用于定义列表类型标签 -->
	<dl>
		<dt>帮助中心</dt>
		<dd>账户管理</dd>
		<dd>购物指南</dd>
		<dd>订单操作</dd>
	</dl>
</body>
</html>
```

##### 12.1.9.6 表格标签`table`

表格由`<table>` 标签来定义。每个表格均有若干行（由 `<tr>` 标签定义），每行被分割为若干单元格（由`<td>`标签定义）。字母 td 指表格数据（table data），即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<table border="1" cellspacing="0">
		<!-- 标题 -->
		<caption>商品清单</caption>
		<!-- 表格头 -->
		<thead>
			<!-- 表格行 -->
			<tr>
				<!-- 表格头里的列：［th］ -->
				<th>产品名称</th>
				<th>品牌</th>
				<!-- 横向合并：合并列数 -->
				<th colspan="2">数量和入库时间</th>
			</tr>
		</thead>
		<!-- 表格主体 -->
		<tbody>
			<!-- 表格行 -->
			<tr>
				<!-- 表格体里列：［td］ -->
				<td>电视机</td>
				<td>小米</td>
				<td>200</td>
				<td>2018-09</td>
			</tr>
			<tr>
				<td>电冰箱</td>
				<!-- 纵向合并：合并行数 -->
				<td rowspan="2">海尔</td>
				<td>900</td>
				<td>2018-06</td>
			</tr>
				<tr>
				<td>电冰箱</td>
				<td>900</td>
				<td>2018-06</td>
			</tr>
		</tbody>
		<!-- 表格底部 -->
		<tfoot>
			<tr>
				<td colspan="4">备注</td>
			</tr>
		</tfoot>
	</table>
</body>
</html>
```

表格架构：

- table：表格
    - caption：标题
    - thead：表格头
        - tr：表格头中的行
            - th：表格头中的单元格
    - tbody：表格体
        - tr：表格体中的行
            - td：表格体中的单元格
    - tfoot：表格底部

合并：

- rowspan：合并行（竖着合并）
- colspan：合并列（横着合并）

##### 12.1.9.7 超链接标签`a`

超级链接`<a>`标记代表一个链接点，是英文anchor（锚点）的简写。它的作用是把当前位置的文本或图片连接到其他的页面、文本或图像。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<!-- href：超链接地址 -->
	<!-- title：鼠标悬停时的提示语 -->
	<!-- target=_self：为在当前窗口打开
		 target=_blank：为在新的窗口打开
		-->
		<p id="top"></p>
    <a href="http://www.baidu.com" target="_blank" title="点击一下，了解更多">百度一下</a>
    <a href="a.zip">下载包</a>
    <a href="13870492666@163.com">联系我们</a>
    <!-- 返回页面顶部的内容 -->
    <a href="#">跳转到顶部</a>

    <!-- 返回某个id -->
    <a href="#p1">跳转到p1</a>
    <!-- javascript:alert(1)是表示在触发<a>默认动作时，执行一段JavaScript代码;
	而 javascript:表示什么都不执行，这样点击<a>时就没有任何反应。 -->
    <a href="javascript:alert(1)">内容</a>
    <a href="javascript:;">内容</a>
    <p>向下滚动</p>
    <p>向下滚动</p<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<!-- href：超链接地址 -->
	<!-- title：鼠标悬停时的提示语 -->
	<!-- target=_self：为在当前窗口打开
		 target=_blank：为在新的窗口打开
		-->
		<p id="top"></p>
    <a href="http://www.baidu.com" target="_blank" title="点击一下，了解更多">百度一下</a>
    <a href="a.zip">下载包</a>
    <a href="13870492666@163.com">联系我们</a>
    <!-- 返回页面顶部的内容 -->
    <a href="#">跳转到顶部</a>

    <!-- 返回某个id -->
    <a href="#p1">跳转到p1</a>
    <!-- javascript:alert(1)是表示在触发<a>默认动作时，执行一段JavaScript代码;
	而 javascript:;表示什么都不执行，这样点击<a>时就没有任何反应。 -->
    <a href="javascript:alert(1)">内容</a>
    <a href="javascript:;">内容</a>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
		<a href="#top">回到顶部</a>
</body>
</html>	
```

备注：

- href：超链接地址
- title：鼠标悬停时的提示语
- target=**_self**：为在当前窗口打开
- target=**_blank**：为在新的窗口打开

链接其他表现形式：

- 目标文档为下载资源：
    - 例如：href属性值，指定的文件名.rar/zip，就是下载操作(rar、zip等)
- 电子邮件链接:
    - 前提：计算机中必须安装邮件客户端，并且配置好了邮件相关信息。 例如：`<a href="13870492666@163.com">联系我们</a>`
- 返回页面顶部的空链接或具体id值的标签:
    - 例如：`<a href="#">内容</a>`或`<a href="#id值">内容</a>`
- javascript:是表示在触发`<a>`默认动作时，执行一段JavaScript代码:
    - 例如：`<a href="javascript:alert()">内容</a>`
- javascript:;表示什么都不执行，这样点击`<a>`时就没有任何反应:
    - 例如：`<a href="javascrip:;">`内容</a

##### 12.1.9.8 图片标签`img`

使用`<img/>`标签在网页中插入图片；

语法：`<img src="图片地址" alt="图片加载失败时显示的内容" title = "提示信息" />`

```html
<!DOCTYPE html>
<html>
<head>
	<title>img标签</title>
</head>
<body>
	<!-- 相对路径：
		.／1.png
		..／1.png
		...／1.png
	 -->
	<!-- 绝对路径：
		/Users/zhangzhiqiang/Desktop/web前端/img/1.png
	 -->
	 <p>
 	描述该图片内容的信息,
	<span>与行内元素展示的标签,<span>
    <span>与行内元素展示的标签<span>
	</p>
	<img src="./1.png" width="600" height="500" alt="加载失败显示字符" title="鼠标悬浮显示标题">
</body>
</html>

```

⚠️注意：

- src设置的图片地址可以是本地的地址也可以是一个网络地址
- 图片的格式可以是png、jpg和gif
- alt属性的值会在图片加载失败时显示在网页上
- 还可以为图片设置宽度(width)和高度(height)，不设置就显示图片默认的宽度和高度
- 与行内元素在一行内显示
- 可以设置宽度和高度
- span标签可以单独摘出某块内容，结合css设置相应的样式

##### 12.1.9.9 表单标签`form`

表单是一个包含表单元素的区域，允许用户在表单中输入内容；

语法：

```html
<form>允许出现表单控件</form>
```

示例：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
	<title>form标签</title>
</head>
<body>
	<form action="https://www.baidu.com/" method="post" enctype="multipart/form-data ">
		<!-- 文本框 -->
		<p>
			用户名:
			<input type="text" name="username" placeholder="请输入用户名" readonly >
		</p>
		<p>
			密码：
			<input type="password" name="pwd" placeholder="请输入密码">
		</p>
		<p>
			确认密码：
			<input type="re_password" name="re_pwd" placeholder="确认密码" disabled>
		</p>
		<p>
			<label for="yzm">验证码：</label>
			<input type="text" name="yzm" id="yzm" placeholder="输入验证码">
		</p>
		<!-- 单选框 -->
		<p>
			性别：
			<!-- checked默认选中 -->
			<!-- radio单选框 -->
			男：<input type="radio" name="sex" checked="">
			女：<input type="radio" name="sex">
		</p>
		<p>
			提交:
			<input type="submit" name="sub">
		</p>
		<hr>
		<!-- 多选框 -->
		<p>
			课程多选：
			<!-- checkbox复选框 -->
			web前端<input name="pd" type="checkbox" checked="">
			python开发<input name="kf" type="checkbox" name="">
			linux编程<input name="bc" type="checkbox" name="">
		</p>
		<hr>
		<!-- 下拉单选 -->
		<p>
			下拉框实现单选：
			<select>
				<!-- selected 默认选中项 -->
				<option>html</option>
				<option>css</option>
				<option selected="python">python</option>
				<option>vue</option>
			</select>
		</p>
		<hr>
		<!-- 下拉多选 -->
		<p>
			<!--滚动列表 multiple设置以后实现多选效果，ctrl+鼠标左键进行多选-->
			下拉框实现多选：
			<select multiple="multiple">
				<option>html</option>
				<option>css</option>
				<option selected="python">python</option>
				<option>vue</option>
				<option>linux</option>
				<option>c</option>
				<option>java</option>
				<option>ruby</option>
				<option>go</option>
			</select>
		</p>
		<hr>
		<!-- textarea -->
		<p>
			个人描述：
			<!-- 超出文本框可以滚动列表 -->
			<textarea rows="10" cols="30">
			</textarea>
		</p>
		<!-- 上传文件 -->
		<p>
			上传文件：
			<input type="file" name="textfile">
		</p>
		<!-- 按钮 -->
		<p>
			<input type="submit" name="zc" value="立即注册">
			<input type="reset" name="cz" value="重置">
			<input type="button" name="an" value="普通按钮">
			<input type="hidden" name="hi" value="隐藏按钮">
			<input type="image" src="./1.png" name="submit" title="百度一下">
		</p>
	</form>
</body>
</html>

```

示例解释：

- form表单标签

    - action：表单提交时的动作，提交给服务器处理程序的地址
    - accept—charset：提交表单中使用的字符集
    - name：识别表单的名称
    - method：定义表单提交时的方式
        - get：明文提交，数据显示在地址上，安全性低，提交最大为2KB
        - post：隐式提交，数据显示在Form Data里，安全性高，无大小限制
    - enctype：
        - `application/x-www-form-urlencoded`所有字符都可以提交给服务器，不允许上传文件，默认
        - `multipart/form-data`将文件以二进制提交给服务器
        - `text/plain `只允许提交普通字符，特殊字符和文件都无法提交，在发邮件时要设置这种类型
    - target：action属性中地址的mubiao，默认：_self

    ⚠️注意：如果有文件需要提交给服务器，methdo必须为post请求方式，enctype必须为multipart/form-data。

- 表单控件

    - input组传统属性：

        - type：
            - button：可点击按钮
            - text：明文显示输入的数据
            - password：密文显示用户输入的数据，一般用在密码输入
            - radio：单选按钮
            - checkbox：复选框
            - submit：功能固定化，负责将表中的表单提交给服务器
            - file：上传文件
            - hidden：隐藏输入字段，用户看不到
            - image：图像形式的提交按钮
            - reset：重置按钮，会清除表单中的所有数据
        - value：input元素设定值，checkbox或radio必须设置value属性
        - name：规定input的名称，提交到服务器后的表单进行标识
        - readonly：输入字段为只读，与text或password元素配合使用
        - disabled：输入字段为禁用，无法与hidden一起使用
        - size：输入字段大小，统计字符，与text或password元素配合使用
        - maxlength：输入字段的长度
        - accept：规定文件上传的类型
        - alt：图片无法显示时，提供备选信息，只能与type="image"元素配合使用
        - src：提交按钮显示的图像URL，与text或password元素配合使用
        - checked：页面加载时/后预选的input元素，通过javascript进行设置

    - input组新增属性：

        - autocomplete：浏览器应该自动完成表单，默认开启
        - autofocus：页面加载时，域自动获得焦点
        - novalidate：提交表单时不验证form或input域
        - height：规定image类型的input标签的图像高度，用于image类型的input标签
        - width：规定image类型的input标签的图像宽度，用于image类型的input标签
        - list：在表单控件输入数据时可用的一个选项列表
        - min：规定输入域所允许的最大值
        - max：规定输入域所允许的最小值
        - step：规定合法的数字间隔
        - multiple：规定按住ctrl按键，输入字段可以选择多个值，用于type="email"和"file"的input元素
        - pattern：用于验证input域的模式。模型pattern是正则表达式
        - placeholder：提供占位符文字，描述输入域所期待的值。占位符会在输入域为空时显示出现，在输入域获得焦点时消失
        - required：规定必须在提交之前填写输入域
        - form：规定输入域所属的一个或多个表单，form属性必须和所属表单的id
        - formaction：重写表单的action属性
        - formenctype：重写表单的enctype属性
        - formmethod：重写表单的method属性
        - formnovalidate：重写表单的novalidate属性
        - formtarget：重写表单的target属性

    - select和option选项框：

        - select属性

            - size：取值大于1位滚动列表，否则为下拉框
            - multiple：设置多选

        - option属性

            - value：选项的值
            - selected：预选中

            ⚠️注意：如果不设置selected属性的话，那么选项框中的第一个值默认被选中

    - textarea文本域：允许用户在表单中录入多行数据的控件

        - cols：指定文本区域的列数，变相设置当前元素的宽度
        - rows：指定文本区域的行数，变相设置当前元素的高度

    - lable：关联文本与表达的元素，点击文本时，如同点击表单元素一样

##### 12.1.9.10 其它标签

**1.换行标签`br`**

`<br>`标签用来将内容换行，其在HTML网页上的效果相当于我们平时使用word编辑文档时使用回车换行。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<h2>换行标签</h2>
	作为子民我愿以此身终生报效国家， <br>大丈夫建功立业何须活着返回家园。
</body>
</html>

```

**2.分割线`hr`**

`<hr>`标签用来在HTML页面中创建水平分隔线，通常用来分隔内容。

```html
<!DOCTYPE html>
<html>
<head>
	<title>段落／语气／换行／无序／有序／定义／表格</title>
</head>
<body>
	<h2>段落标签</h2>
	<p>售后政策</p>
	<p>小米服务</p>
	<p>自主服务</p>
	<p>我不知道</p>
	<hr>

	<h2>定义列表－definition list</h2>
		<dl>
			<dt>帮助中心</dt>
			<dd>账户管理</dd>
			<dd>购物指南</dd>
			<dd>订单操作</dd>
		</dl>
	<hr>
</body>
</html>

```

**3.特殊符号**

浏览器在显示的时候会移除源代码中多余的空格和空行。 所有连续的空格或空行都会被算作一个空格。需要注意的是，HTML代码中的所有连续的空行（换行）也被显示为一个空格。

```html
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>路飞符号</title>
    </head>
    <body>

        <p>帮助有志向的年轻人


            通过努力学习获得
            体面的   	工作  和    生活！
            &hearts;A &clubs;A &spades;A &diams;A
        </p>
    </body>
</html>

```

[特殊符号对照表](http://tool.chinaz.com/Tools/HtmlChar.aspx)

#### 12.1.10 标签分类

HTML中标签元素三种不同类型：

- 块状元素
- 行内 
- 行内块元素

常用的块状元素：

```html
<div> <p> <h1>~<h6> <ol> <ul> <table><form> <li>
```

常用的行内元素

```html
<a> <span> <br> <i> <em> <strong> <label>
```

常用的行内块状元素：

```html
<img> <input>
```

**块级元素特点**：display:block;

1. 每个块级元素都从新的一行开始，并且其后的元素也另起一行。**独占一行**

2. 元素的高度、宽度、行高以及顶和底边距都**可设置**。

3. 元素宽度在不设置的情况下，是它本身父容器的100%（和父元素的宽度一致），除非设定一个宽度。

**行内元素特点**：display:inline;

1. 和其他元素都**在一行上**；

2. 元素的高度、宽度及顶部和底部边距**不可设置**；

3. 元素的宽度就是它包含的文字或图片的宽度，**不可改变。**

**行内块状元素的特点**：display:inline-block;

1. 和其他元素都**在一行上**；

2. 元素的高度、宽度、行高以及顶和底边距都**可设置**

#### 12.1.11 嵌套规则

- 块元素可以包含行内元素或某些块元素

    - ```html
        <div><div></div><h1></h1><p><p></div>
        ```

- 行内元素不能包含块元素，它只能包含其它的行内元素
    - ```html
        <a href=”#”><span></span></a>
        ```

- 块级元素不能放在p标签里面

    - ```html
        <p><div></div></p>
        ```

- 有几个特殊的块级元素只能包含行内元素，不能再包含块元素

    - ```html
        h1、h2、h3、h4、h5、h6、p
        ```

- li元素可以嵌入ul，ol，div等标签

    - ```html
        <ul>
            <li>
                <ul>
                    <li>
                        <div>
        
                        </div>
                    </li>
                    <li>
                        <ol>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ol>
                    </li>
                </ul>
            </li>
        </ul>
        ```

### 12.2 CSS

#### 12.2.1 CSS简介

CSS是指层叠样式表(Cascading Style Sheets)，样式定义如何显示HTML元素，样式通常又会存在于样式表中。也就是说把HTML元素的样式都统一收集起来写在一个地方或一个CSS文件里。

优势：

- 内容与表现分离
- 网页的变现统计，容易修改
- 丰富的样式，使页面布局更加灵活
- 减少网页代码量，增加网页浏览器速度，节省网络宽带
- 运用独立页面的CSS，有利于网页被搜索引擎收录

#### 12.2.2 CSS基础语法

css语法可以分为两部分：

- 1.选择器
- 2.声明

声明由属性和值组成，多个声明之间用分号进行分隔。

语法：

```css
选择器{
	样式1;
	样式2;
	......
}
```

例子：

```html
<!DOCTYPE html>
<html>
<head>
	<title>css样式声明</title>
	<!-- css样式：选择符和声明构成
	声明：属性名(color)和属性值(orange)
		  -->
	<style type="text/css">
		span{
			color: orange;
			font-size: 30px;
		}
	</style>
</head>
<body>
	<p>
		<span>好好学Pyhton</span>
		请你 <span>吃炸鸡</span>
	</p>
</body>
</html>
```

**CSS注释：**

- 注释是代码之母

- 注释快捷键：alt＋／

```css
/*这是注释*/
```

**CSS中引用样式：**

- 内联式
- 嵌入式
- 外部式
    - 链接式
    - 导入式

1.内联式

```html
<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<!-- 1.内联试 -->
	<p style="color: red">
		文本是什么颜色？
	</p>
</body>
</html>
```

2.嵌入式

```html
<!DOCTYPE html>
<html>
<head>
	<style type="text/css">
		h3{
			color: green;
		}
	</style>
</head>
<body>
	<h3>
		小猪佩琦🐷
	</h3>
</body>
</html>
```

3.外部式

html文件

```html
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="css/css_嵌入式.css">
</head>
<body>
	<p style="color: red">
		文本是什么颜色？
	</p>
	<h4>
		中华人民共和国
	</h4>
</body>
</html>
```

css文件

```css
h4{
	color:blue;
}

p{
	color: red;
	font-size: 20px;
	font-weight: bold;
}
```

#### 12.2.3 基本选择器

在一个HTML页面中会有很多的元素，不同的元素可能有不同的样式，某些元素又需要设置相同的样式，选择器就是用来从HTML页面中查找特定的元素，找到元素之后就可以为它们设置样式了，选择器为样式规则指定一个作用范围。

**基本选择器包括：**

- 标签(元素)选择器
- 类(class)选择器
- id(身份证号)选择器

##### 12.2.3.1 标签选择器

解释：通过标签名来选择元素;

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
    <title>css的基础选择器-标签选择器</title>
    <link rel="stylesheet" type="text/css" href="css/demo4.css">
</head>
<body>
<div id="container">
    <h3 class="active title">永恒课题</h3>
    <p>
        7月16日出版的第14期《求是》 <span class="active">杂志发表习近平总书记的重要文章</span>《增强推进党的政治建设的自觉性和坚定性》。 <span id="pq">文章强调：“党的政治建设是一个永恒课题，来不得半点松懈。</span>
    </p>
    <p>
        ”并对抓好、落实党的政治建设提出了明确要求，具有很强的政治性、思想性和指导性。新华社 <span id="jj">《学习进行时》</span>以摘要形式梳理其中要点，和您一起学习。
    </p>
</div>
</body>
</html>
```

css文件：

```css
p{
	color:red;
}
```

将所有p标签的字体设置为红色。

##### 12.2.3.2 id选择器

解释：通过标签的id值选择元素;

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>css的基础选择器-标签选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo4.css">
</head>
<body>
	<div id="container">
		<h3 class="active title">永恒课题</h3>
		<p>
			7月16日出版的第14期《求是》 <span class="active">杂志发表习近平总书记的重要文章</span>《增强推进党的政治建设的自觉性和坚定性》。 <span id="pq">文章强调：“党的政治建设是一个永恒课题，来不得半点松懈。</span>
		</p>
		<p>
			”并对抓好、落实党的政治建设提出了明确要求，具有很强的政治性、思想性和指导性。新华社 <span id="jj">《学习进行时》</span>以摘要形式梳理其中要点，和您一起学习。
		</p>
	</div>
</body>
</html>
```

css文件

```css
#pq{
	color: blue;
}
#jj{
	color: orange;
}
```

将所有id值pq标签的字体设置为蓝色，将所有id值jj标签的字体设置为橘色

注意⚠️：id的值是唯一的

##### 12.2.3.3 类选择器

解释：通过标签的类选择元素：

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>css的基础选择器-标签选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo4.css">
</head>
<body>
	<div id="container">
		<h3 class="active title">永恒课题</h3>
		<p>
			7月16日出版的第14期《求是》 <span class="active">杂志发表习近平总书记的重要文章</span>《增强推进党的政治建设的自觉性和坚定性》。 <span id="pq">文章强调：“党的政治建设是一个永恒课题，来不得半点松懈。</span>
		</p>
		<p>
			”并对抓好、落实党的政治建设提出了明确要求，具有很强的政治性、思想性和指导性。新华社 <span id="jj">《学习进行时》</span>以摘要形式梳理其中要点，和您一起学习。
		</p>
	</div>
</body>
</html>
```

css文件

```css
.active{
	color: red;
}
.title{
	font-size: 30px;
}
```

把所有类为active的值的字体颜色设置为黑色，把所有类为title的值的字体大小设置为30px

**类选择器去重使用：**

一个html文件设置的属性可能有很多重复的样式，如果把所有相同的样式都设置，会产生很多冗余的代码，所以我们可以把重复样式类的值写到一个类里边，以逗号分隔，这样就会减少css的代码量。

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>类选择器去重使用</title>
	<link rel="stylesheet" type="text/css" href="css/demo5.css">
</head>
<body>
	<!-- 绿色 20px -->
	<p class="lv big">欢迎</p>
	<!-- 绿色 粗 -->
	<p class="lv strong">欢迎</p>
	<!-- 粗 20px -->
	<p class="strong big">欢迎</p>
</body>
</html>
```

css文件

```css
.lv{
	color: green;
}
.big{
	font-size: 20px;
}
.strong{
	font-weight: bold;
}
```

把类为lv的值的颜色设置为绿色，类为big的值的字体大小设置成20px，类为strong的字体设置为粗体。

#### 12.2.4 高级选择器

高级选择器：

- 后代选择器
- 子代选择器
- 组合选择器
- 交集选择器
- 伪类选择器

##### 12.2.4.1 后代选择器

解释：后代选择器从根元素一直往后查找并设置

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>高级选择器－后代／子代／交集选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo6.css">
</head>
<body>
	<h3>我在人民广场吃着炸鸡</h3>
	<div class="wrap">
		<p>
			<a href="#">小圆圈</a>
		</p>
		<a href="#">world</a>
	</div>
	<div>
		<a href="＃">hello world</a>
	</div>
	<a href="＃">OK</a>
	<span>在干嘛呢？</span>
	<span>工作忙吗？</span>
	<h2 class="met">web</h2>
</body>
</html>
```

css文件

```css
.wrap a{
	color: red;
}
```

把类的值为wrap的所有后代中a标签的字体颜色设置为红色

##### 12.2.4.2 子代选择器

解释：从div的字元素中找到p标签设置

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>高级选择器－后代／子代／交集选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo6.css">
</head>
<body>
	<h3>我在人民广场吃着炸鸡</h3>
	<div class="wrap">
		<p>
			<a href="#">小圆圈</a>
		</p>
		<a href="#">world</a>
	</div>
	<div>
		<a href="＃">hello world</a>
	</div>
	<a href="＃">OK</a>
	<span>在干嘛呢？</span>
	<span>工作忙吗？</span>

	<h2 class="met">web</h2>
</body>
</html>
```

css文件

```css
.wrap >a{
	color: yellow;
}
```

把类的值为wrap的直接子元素中找到a标签，设置字体为黄色

##### 12.2.4.3 组合选择器

解释：把设置相同的选择器用逗号隔开设置

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>高级选择器－后代／子代／交集选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo6.css">
</head>
<body>
	<h3>我在人民广场吃着炸鸡</h3>
	<div class="wrap">
		<p>
			<a href="#">小圆圈</a>
		</p>
		<a href="#">world</a>
	</div>
	<div>
		<a href="＃">hello world</a>
	</div>
	<a href="＃">OK</a>
	<span>在干嘛呢？</span>
	<span>工作忙吗？</span>

	<h2 class="met">web</h2>
</body>
</html>
```

css文件

```css
h3, span{
	color: gray;
	font-size: 14px;
}
```

把所有类的值为h3和span的标签的字体颜色设置为灰色，字体大小设置为14px

##### 12.2.4.4 交集选择器

解释：提取两个选择器共同的部分进行设置

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>高级选择器－后代／子代／交集选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo6.css">
</head>
<body>
	<h3>我在人民广场吃着炸鸡</h3>
	<div class="wrap">
		<p>
			<a href="#">小圆圈</a>
		</p>
		<a href="#">world</a>
	</div>
	<div>
		<a href="＃">hello world</a>
	</div>
	<a href="＃">OK</a>
	<span>在干嘛呢？</span>
	<span>工作忙吗？</span>

	<h2 class="met">web</h2>
</body>
</html>
```

css文件

```css
h2{
	color: red;
}
.met{
	font-weight: lighter;
}
h2.met{
	font-size: 14px;
}
```

说明：如果类的值为h2和met的标签设置字体大小为14px，我们就可以提取两个标签共同的部分进行设置

语法：

```css
选择器1.选择器2{
	共同的样式;
}
```

##### 12.2.4.5 伪类选择器

常见的几种伪类选择器。

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>伪类选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo7.css">
</head>
<body>
	<a href="#">小圆圈</a>
	<span>小米商城</span>
	<div>
		<span>小米手机</span>
	</div>
</body>
</html>
```

css文件

```css
/*没有被访问过a的状态*/
a:link{
	color: orange;
}
/*访问过后的状态*/
a:visited{
	color: green;
}
/*鼠标悬浮的状态,可以应用所有标签*/
a:hover{
	color: black;
}
/*鼠标摁住时的状态*/
a:active{
	color: yellow;
}
/*鼠标悬浮的状态,可以应用所有标签*/
span:hover{
	color: red;
}
/*鼠标悬浮的状态,可以应用所有标签*/
div:hover{
	background-color: green;
}
/*鼠标悬浮的状态,可以应用所有标签*/
div:hover span{
	color: white;
}
```

##### 12.2.4.6 伪元素

常用的几种伪元素：

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>伪类选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo7.css">
</head>
<body>
	<a href="#">小圆圈</a>
	<span>小米商城</span>
	<div>
		<span>小米手机</span>
	</div>
	<p>我不知道</p>
</body>
</html>
```

css文件

```css
/*文本的首字符设置特殊样式*/
p:first-letter{
	font-size: 48px;
}
/*在标签的前面插入新的内容*/
span:before {
  content: "*";
  color: red;
}
/*在标签的后面插入新的内容*/
p:after {
  content: "?";
  color: red;
}
```

- p标签的首字符设置字体大小为48px
- 在span标签的前面插入新的内容，样式为‘＊’，字体颜色为红色
- 在p标签的最后插入新的内容，样式为‘？’，字体颜色为红色

##### 12.2.4.7 继承性

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>继承性</title>
	<link rel="stylesheet" type="text/css" href="css/demo8.css">
</head>
<body>
	<div>
		<ul>
			<li>
				<p>这是继承了吗？</p>
			</li>
		</ul>
	</div>
</body>
</html>
```

css文件

```css
body{
	color: red;
	font-size: 30px;
	border: 1px solid red;
}
```

css给根元素设置字体颜色为红色，字体大小为30px，并设置一个宽度为1px，实线，颜色为红色的方框线，在body下的元素都继承了body的样式；

#### 12.2.5 选择器的优先级

我们现在已经学过了很多的选择器，也就是说我们从HTML中找一个元素的方法有很多种，既然有很多种，就会产生优先级。

例如：如果通过不同的选择器找到了相同的元素，并设置不同的样式，浏览器会怎么渲染呢？

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>选择器权重</title>
	<style type="text/css">
		/*001*/
		div{
			color: red;
		}
		/*010*/
		.b{
			color: purple;
		}
		/*100*/
		#b{
			color: orange;
		}
		/*003 3个标签相加*/
		html body div{
			color: blue;
		}
    /*数选择器的数量：
			内联选择器1000－id选择器100－类选择器10－元素选择器1
			*/
	</style>
</head>
<body>
	<div>a</div>
	<div class="b" id="b" style="color: green;">we</div>
</body>
</html>
```

选择器的权重规则：

- 内联选择器的权重为1000
- id选择器的权重为100
- 类选择器的权重为10
- 元素(标签)选择器的权重为1

**选择器权重深入：**

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>css选择器权重深入</title>
	<style type="text/css">
		/*001*/
		p{
			color: gray;
		}
		/*003*/
		div div p{
			color: yellow;
		}
		/*010*/
		.wrap3{
			color: purple;
		}
		/*011*/
		div .wrap3{
			color: black;
		}
		/*012*/
		div div .wrap3{
			color:  blue;
		}
		/*120*/
		.wrap1 #box2 .wrap3{
			color: green;
		}
		/*继承来的属性，权重非常低，几乎为0*/
		#box1 #box2{
			color: red;
		}
		/*继承来的属性低于选中标签的效果*/
		.container{
			color: red;
			font-size: 14px;
		}
		.container ul li{
			color: #000;
			font-size: 16px;
		}
	</style>
</head>
<body>
	<div class="wrap1" id="box1">
		<div class="wrap2" id="box2">
			<p class="wrap3" id="box3">
				到底是什么颜色？
			</p>
		</div>
	</div>
	<div class="container">
		<ul>
			<li>
				小米手机
			</li>
		</ul>
	</div>
</body>
</html>
```

注意⚠️：还有一种不讲道理的`!import`方式来强制让样式生效，这样不推荐使用，因为这样是破坏自然规律的一种写法，大量使用这中写法无法进行维护的，破坏自然规律！

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>!important讲解</title>
	<style type="text/css">
		div{
			color: purple !important;
		}
		#a{
			color: green !important;
		}
		/*都有!import，看权重*/
	</style>
</head>
<body>
	<div class="a" id="a">颜色</div>
</body>
</html>
```

如果div样式不加`!important`显示颜色为绿色，如果加了则显示紫色，如果都加了，则看权重，此时例子中显示的是绿色；

#### 12.2.6 字体属性

- font-family

`font-family`可以把多个字体名称作为一个‘回退’系统来保存。意思就是如果浏览器不支持第一种字体，则会自动去尝试下一个字体，以此类推。

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>字体属性</title>
	<style type="text/css">
		/*字体备选方案顺序依次*/
		body{
			font-family: "Hoefler Text","Arial";
		}
	</style>
</head>
<body>
    Python编程
</body>
</html>
```

如果设置成`inherit`，则表示继承父元素的字体。

- font-size

设置字体大小

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>字体属性</title>
	<style type="text/css">
		body{
			font-size: 30px;
		}
	</style>
</head>
<body>
	python 课程
</body>
</html>
```

- color

设置字体颜色

**支持三种颜色值：**

- 颜色的名称，比如：red
- 设置rgb值，比如：rgb(255,255,255)
- 十六进制值，比如：#FF6700
- rgba中的a表示透明度，值在0-1之间，比如：rgba(255,0,0,.5)

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>字体属性</title>
	<style type="text/css">
		body{
			/*red，green，blue设置颜色*/
			color: rgb(255,255,0);
			/*a：表示透明度0-1之间的数*/
			color: rgba(255,0,0,.5);
			/*十六进制表示法*/
			color: #FF6700;
			/*颜色名称*/
			color: red;
		}
	</style>
</head>
<body>
	python 课程
</body>
</html>
```

- font-weight

设置字体粗细

|   值    |                      描述                      |
| :-----: | :--------------------------------------------: |
| normal  |                默认值，标准粗细                |
|  bold   |                      粗体                      |
| bolder  |                      更粗                      |
| lighter |                      更细                      |
| 100~900 | 设置具体粗细，400等同于normal，而700等同于bold |
| inherit |             继承父元素字体的粗细值             |

示例：html

```html
<!DOCTYPE html>
<html>
<head>
	<title>字体属性</title>
	<style type="text/css">
		body{
			/*字体粗细取100-900之间的数*/
			font-weight: 900;
			/*粗体*/
			font-weight: bold;
			/*更粗*/
			font-weight: bolder;
			/*默认粗细，标准*/
			font-weight: normal;
			/*更细*/
			font-weight: lighter;
		}
	</style>
</head>
<body>
	python 课程
</body>
</html>
```

- font-style

设置字体样式

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>字体属性</title>
	<style type="text/css">
		body{
			/*字体样式*/
			font-style: italic;
		}
	</style>
</head>
<body>
	python课程
</body>
</html>
```

#### 12.2.7 文本属性

- line-height

设置行高

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性和字体属性示例</title>
	<style type="text/css">
		div{
			line-height: 70px;
		}
	</style>
</head>
<body>
	<div class="box">
		<a href="https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.11.4b1311d9qvNbqS&q=%E6%97%B6%E5%B0%9A%E5%A5%97%E8%A3%85&cat=16&style=grid&seller_type=taobao">
			休闲运动套装女夏2019新款时尚撞色宽松T恤束脚裤休闲显瘦两件套
		</a>
		<p>$ <span>655.00</span></p>
	</div>
</body>
</html>
```

注意：行高一定要大于字体大小，否则字体会大于行高页面显示不美观

示例：html文件

```css
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－缩进</title>
	<style type="text/css">
		div{
			/*注意⚠️：行高一定要大于字体大小*/
			line-height: 40px;
			font-size: 30px;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

- text-decoration

设置文本的修饰，下划线／上划线／删除线

|      值      |                 描述                  |
| :----------: | :-----------------------------------: |
|     none     |        默认。定义标准的文本。         |
|  underline   |         定义文本下的一条线。          |
|   overline   |         定义文本上的一条线。          |
| line-through |       定义穿过文本下的一条线。        |
|   inherit    | 继承父元素的text-decoration属性的值。 |

示例：html

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性和字体属性示例</title>
	<style type="text/css">
		.box span{
			/*删除线*/
			text-decoration: line-through;
			/*下划线*/
			text-decoration: underline;
			/*上划线*/
			text-decoration: overline;
			/*默认为标准文本*/
			text-decoration: none;
			/*继承父类元素的值*/
			text-decoration: inherit;
		}
	</style>
</head>
<body>
	<div class="box">
		<a href="https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.11.4b1311d9qvNbqS&q=%E6%97%B6%E5%B0%9A%E5%A5%97%E8%A3%85&cat=16&style=grid&seller_type=taobao">
			休闲运动套装女夏2019新款时尚撞色宽松T恤束脚裤休闲显瘦两件套
		</a>
		<p>$ <span>655.00</span></p>
	</div>
</body>
</html>
```

- text-align

设置文本对齐

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－文本对齐</title>
	<style type="text/css">
		div{
			/*设置文本对齐center／right／left默认left*/
			text-align: center;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

对齐样式：

|   值    |      描述       |
| :-----: | :-------------: |
|  left   | 左边对齐 默认值 |
|  right  |     右对齐      |
| center  |    居中对齐     |
| justify |    两端对齐     |

- text-indent

设置文本缩进

示例：html

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－缩进</title>
	<!-- 文本缩进：px是一个绝对单位，你设置多少像素就会显示多少像素
		em是一个相对单位，相对当前字体大小进行缩进 -->
	<style type="text/css">
		p{
			text-indent: 2em;
			text-indent: 32px;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

- font

设置综合属性

示例：html

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－综合</title>
	<style type="text/css">
		p{
			/*字体大小／行高/字体综合属性*/
    		font: 20px/2 "Helvetica Neue",Helvetica,Arial,"Microsoft Yahei","Hiragino Sans GB","Heiti SC","WenQuanYi Micro Hei",sans-serif;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

- letter-spacing

设置文字之间的距离

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－文字距离</title>
	<style type="text/css">
		p{
      		/*调整文字之间的距离*/
			letter-spacing: 5px;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

- word-spacing

设置英文单词之间的距离

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－单词距离</title>
	<style type="text/css">
		p{
      		/*调整英文单词之间的距离*/
			word-spacing: 10px;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

#### 12.2.8 背景属性

设置背景样式

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－缩进</title>
	<style type="text/css">
		p{
			/*设置背景颜色*/
			background-color: red;
			/*设置背景图像*/
			background-image: url('img/1.png');
			/*设置背景图片尺寸*/
			background-size: 380px 860px;
			/*如何重复背景图像*/
			background-repeat: no-repeat;
			/*设置背景图像是否固定或者随着页面的其余部分滚动*/
			background-attachment: fixed;
			/*设置图像位置*/
			background-position: center;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

常用背景相关属性：

|         属性          |                       描述                       |
| :-------------------: | :----------------------------------------------: |
|   background-color    |              规定要使用的背景颜色。              |
|   background-image    |              规定要使用的背景图像。              |
|    background-size    |               规定背景图片的尺寸。               |
|   background-repeat   |              规定如何重复背景图像。              |
| background-attachment | 规定背景图像是否固定或者随着页面的其余部分滚动。 |
|  background-position  |               规定背景图像的位置。               |
|        inherit        |    规定应该从父元素继承background属性的设置。    |

`background-repeat`取值范围：

|    值     |                       描述                        |
| :-------: | :-----------------------------------------------: |
|  repeat   |    默认。背景图像将在垂直方向和水平方向重复。     |
| repeat-x  |            背景图像将在水平方向重复。             |
| repeat-y  |            背景图像将在垂直方向重复。             |
| no-repeat |              背景图像将仅显示一次。               |
|  inherit  | 规定应该从父元素继承background-repeat属性的设置。 |

`background-attachment`取值范围：

|   值    |                         描述                          |
| :-----: | :---------------------------------------------------: |
| scroll  |   默认值。背景图像会随着页面其余部分的滚动而移动。    |
|  fixed  |      当页面的其余部分滚动时，背景图像不会移动。       |
| inherit | 规定应该从父元素继承background-attachment属性的设置。 |

`background-position`取值范围：

|                              值                              |                             描述                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| top left  top center  top right  center left  center center  center right  bottom left  bottom center  bottom right | 如果只设置了一个关键词，那么第二个值就是"center"。 默认值：0% 0%。 |
|                            x% y%                             | 第一个值是水平位置，第二个值是垂直位置。 左上角是 0% 0%。右下角是 100% 100%。 如果只设置了一个值，另一个值就是50%。 |
|                          xpos ypos                           | 第一个值是水平位置，第二个值是垂直位置。 左上角是 0 0。单位是像素 (0px 0px) 或任何其他的 CSS 单位。 如果只设置了一个值，另一个值就是50%。 可以混合使用`%`和`position`值。 |

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>背景属性</title>
	<style type="text/css">
		.bg{
			width: 1200px;
			height: 1300px;
			border: 3px solid green;
			background-color: red;
			background-image: url('images/scholl_flower.jpeg');
			/*默认repeat*/  
      		/*平铺方式:*/
			background-repeat:no-repeat; 
			/*背景定位: 综合写法*/
			/*background-position: 50px 100px;*/
			/*具体值：单个写法*/
			/*background-position-x: 100px;*/
			/*background-position-y: 200px; */

			/*关键字：top right center bottom left*/
			/*background-position: top center;*/

			/*百分比：0% 50% 100%*/
			/*计算规则：水平百分比的值＝容器宽度的百分比－背景图片宽度的百分比*/
			background-position: 50% 50%;
		}
	</style>
</head>
<body>
	<div class="bg">
		<p style="color: #fff;">这是一个八十年代的美女</p>
	</div>
</body>
</html>
```

小米案例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>小米背景定位案例</title>
	<meta charset="utf-8">
	<style type="text/css" charset="utf-8">
		.bgi{
			width: 100%;
			height: 658px;
			/*综合写法*/
			background: url('img/mibg.png') no-repeat center top;

			/*单个写*/
			/*background-image: url('img/mibg.png');*/
			/*平铺方式*/
			/*background-repeat: no-repeat;*/
			/*图片定位*/
			/*background-position: center top;*/
		}
	</style>
</head>
<body>
	<div class="bgi"></div>
</body>
</html>
```

#### 12.2.9 display属性

**一、块级元素和行内元素的分类：**

在HTML中，将标签分为文本级和容器级两类标签。

从HTML看标签分为：

- 文本级标签：a，span，p，br，i，u，em，strong，label
- 容器级标签：div，h系列，ol，ul，table，form，li，dt，dd

```python
# 备注：为什么说p文本级标签呢？因为p里面只能放文字，图片，表单元素，p里面不能放h和ul，p里面也不能放p标签。
```

从CSS看标签分类：

- 行内元素：除了p之外，所有的文本级标签，都是行内元素。p是个文本级，但是是个块级元素。
- 块级元素：所有的容器级标签都是块级元素，还有p标签。

**二、行内元素/块级元素/行内块元素的区别：**

**1.行内元素：**

- 与其他行内元素在一行显示

- 不能设置宽高。默认的宽高，就是文字的宽高

    ```html
    <!DOCTYPE html>
    <html>
    <head>
    	<title></title>
    	<style type="text/css">
    		a,span{
    			background-color: purple;
    			font-size: 30px;
    			width: 300px;
    			height: 300px;
    		}
    	</style>
    </head>
    <body>
     	<a href="#">百度一下</a>
    	<span>小圆圈</span>
    	<strong>粗的</strong>
    	<em>斜体</em>		
    </body>
    </html>
    ```

**2.块级元素：**

- 独占一行，不能与其它任何元素在一行显示

- 可以设置宽高。如果不设置宽，那么宽度默认为父亲的宽

    ```html
    <!DOCTYPE html>
    <html>
    <head>
    	<title></title>
    	<style type="text/css">
    		div{
    			background-color: green;
    			width: 200px;
    			height: 200px;
    		}
    		p{
    			background-color: red;
    		}
    	</style>
    </head>
    <body>
     	<div>MJJ</div>
    	<p>我是一个段落</p>
    	<h1>段落</h1>
    	<ul>
    		<li>小米商城</li>
    	</ul>	
    </body>
    </html>
    ```

**3.行内块元素：**

- 在一行内显示

- 可以设置宽高

    ```html
    <!DOCTYPE html>
    <html>
    <head>
    	<title></title>
    	<style type="text/css">
    		input{
    			width: 200px;
    			height: 200px;
    		}
    		img{
    			width: 200px;
    		}
    	</style>
    </head>
    <body>
     	<input type="" name="username">
    	<input type="" name="pswd">
    	<img src="./img/1.png">
    	<img src="./img/1.png">
    </body>
    </html>
    ```

**三、块级元素和行内元素的互相转换：**

我们可以通过`display`属性将块级元素和行内元素进行相互转换。display即“显示模式”。

**1.行内元素转换为块级元素：**

```html
<!DOCTYPE html>
<html>
<head>
	<title>display属性</title>
	<style type="text/css">
		span,a{
			display: block;
			background-color: green;
			width: 100px;
			/*height: 40px;*/
			/*text-align: center;水平居中
			line-height:控制文本垂直居中*/
			text-align: center;
			line-height: 40px;
		}
	</style>
</head>
<body>
	<span>我是行内元素</span>
	<a href="#">点我一下试试</a>
</body>
</html>
```

一旦给一个行内元素设置`display:block`那么这个标签立即成为块级标签，此时它和一个div没有区别，block是“块”的意思，也就是说：

- 此时这个span，a标签能够设置宽度、高度
- 此时这个span独占一行，别人无法和他一排显示
- 如果不设置宽度，默认为父亲的宽

**2.块级元素可以转换为行内元素：**

```html
<!DOCTYPE html>
<html>
<head>
	<title>display属性</title>
	<style type="text/css">
		div{
			background-color: red;
			width: 200px;
			height: 200px;
			/*块级转行内 none为隐藏*/
			display: inline;
		}
	</style>
</head>
<body>
	<div>我是一个块元素</div>
</body>
</html>
```

一旦给一个块级元素设置`display:inline`那么这个标签立即成为行内标签，此时它和一个span标签没有区别，inline是“行内”的意思，也就是说：

- 此时这个div不能设置宽度、高度
- 此时这个div可以和其它标签在一行显示

#### 12.2.10 盒模型

在CSS中，"box model"这一术语是用来设计和布局时使用，然后在网页中基本上都会显示一些方方正正的盒子。我们称为这种盒子叫盒模型。

##### 12.2.10.1 盒模型的属性

width：内容的宽度

height: 内容的高度

padding：内边距，边框到内容的距离

border: 边框，就是指的盒子的宽度

margin：外边距，盒子边框到附近最近盒子的距离

**一、padding**

padding：就是内边距的意思，它是边框到内容之间的距离。

注意：padding的区域是有背景颜色的。并且背景颜色和内容的颜色一样。也就是说background-color这个属性填充所有的border以内的区域。

**1. padding的设置**

padding有四个方向，分别描述四个方向的padding。

1.写小属性，分别设置不同方向的padding

```html
<!DOCTYPE html>
<html>
<head>
	<title>padding的讲解</title>
	<style type="text/css">
		div{
			width: 180px;
			height: 180px;
			background-color: green;

			/*分别设置*/
			padding-top: 20px;
			padding-left: 20px;
			padding-bottom: 20px;
			padding-right: 50px;
		}
	</style>
</head>
<body>
	<!-- 内边距：盒子边框到内容的距离 -->
	<div>mjj</div>
</body>
</html>
```

2.写综合属性，用空格隔开

```html
<!DOCTYPE html>
<html>
<head>
	<title>padding的讲解</title>
	<style type="text/css">
		div{
			width: 180px;
			height: 180px;
			background-color: green;

			/*综合设置*/
			/*四个值：上 右 下 左*/
			padding: 10px 20px 30px 40px;
			/*三个值：上 右左 下*/
			padding: 20px 30px 40px;
			/*两个值：上下 左 右*/
			padding: 20px 30px;
			/*一个值：上 下 左 右*/
			padding: 20px;
		}
	</style>
</head>
<body>
	<!-- 内边距：盒子边框到内容的距离 -->
	<div>mjj</div>
</body>
</html>
```

**清除 html默认样式：**

一些标签默认有padding，比如ul标签，有默认的padding－left值。

那么我们一般在做栈的时候，是要清除页面标签中默认的padding和margin。以便于我们更好的去调整元素的位置。

例如：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>清除html变迁元素的默认样式</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
</head>
<body>
	<p>我是一个段落</p>	
	<p>我是一个段落</p>
	<ul>
		<li>pop</li>
	</ul>
	<input type="text" name="">
</body>
</html>
```

CSS文件

```css
body,p,ul,ol,dl,dt{
	margin: 0;
	padding: 0;
}
ul,ol{
	list-style: none;
}
input{
	border: none;
	outline: none;
}
a{
	text-decoration: none;
}
```

我们要使用并集选择器来选中页面中应有的标签

```css
https://meyerweb.com/eric/tools/css/reset/
```

**二、border：**

border:边框的意思，描述盒子的边框

border有三个要素：粗细、线性样式、颜色

```css
border: 3px solid red;
```

- 如果颜色不写，默认是黑色
- 如果粗细不写，不显示边框
- 如果只写线性样式，默认的有上下左右3px的宽度，样式为实体

**1. border的设置：**

1.按照三要素来写border

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框border</title>
	<style type="text/css">
		.border{
      		width: 200px;
			height: 200px;
			/*按照三要素来编写border*/
			border-width: 4px;
			border-style: solid dotted double dashed;
			border-color: green red purple yellow;			
		}
	</style>
</head>
<body>
	<!-- 三要素：粗细width／样式style／颜色color -->
	<div class="border"></div>
	<input type="text" name="" class="username">
</body>
</html>
```

2.按照方向来写border

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框border</title>
	<style type="text/css">
		.border{
      		width: 200px;
			height: 200px;
			/*按照方向来编写border*/
			border-top-width: 10px;
			border-top-color: red;
			border-top-style: solid;

			border-right-width: 10px;
			border-right-color: yellow;
			border-right-style: dotted;

			border-bottom-width: 10px;
			border-bottom-color: purple;
			border-bottom-style: double;

			border-left-width: 10px;
			border-left-color: green;
			border-left-style:dashed;			
		}
	</style>
</head>
<body>
	<!-- 三要素：粗细width／样式style／颜色color -->
	<div class="border"></div>
	<input type="text" name="" class="username">
</body>
</html>
```

按照方向的另一种方法：

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框border</title>
	<style type="text/css">
		.border{
      		width: 200px;
			height: 200px;
			/*按照方向来编写border*/
			border-top: 10px solid red;
			border-right: 10px dotted yellow;
			border-bottom: 10px double purple;
			border-left: 10px dashed green;			
		}
	</style>
</head>
<body>
	<!-- 三要素：粗细width／样式style／颜色color -->
	<div class="border"></div>
	<input type="text" name="" class="username">
</body>
</html>
```

3.清除边框的默认样式

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
	<title>边框border</title>
	<style type="text/css">
		input{
			/*清除默认样式*/
			border: none;
			/*或者*/
			/*border: 0;*/

			/*清除外线*/
			outline: none;
		}
		.username{
			width: 180px;
			height: 40px;
			font-size: 20px;
			padding-left: 20px;
			border: 1px solid red;
		}
		.username:hover{
			border: 1px solid orange;
		}
	</style>
</head>
<body>
	<!-- 三要素：粗细width／样式style／颜色color -->
	<div class="border"></div>
	<input type="text" name="" class="username">
</body>
</html>
```

**三、margin：**

margin：外边距的意思。表示边框到最近盒子的距离

```html
<!DOCTYPE html>
<html>
<head>
	<title>外边距 margin</title>
	<style type="text/css">
		span{
			background-color: red;
		}
		.xiongda{
			/*盒子右边移动20px*/
			margin-right: 20px;
		}
		.xionger{
			/*盒子左边移动100px*/
			margin-left: 100px;
		}
		div{
			width: 200px;
			height: 200px;
		}

		/*margin垂直方向会出现外边距合并 外边距塌陷 大的吞并小的*/
		.box1{
			background-color: red;
			/*盒子下边移动30px*/
			margin-bottom: 30px;
		}
		.box2{
			background-color: green;
			/*盒子上边移动100px*/
			margin-top: 100px;
		}
	</style>
</head>
<body>
	<!-- 外边距：一个盒子到另一个盒子的距离 -->
	<span class="xiongda">熊大</span>
	<span class="xionger">熊二</span>

	<div class="box1"></div>
	<div class="box2"></div>
</body>
</html>
```

注意：垂直方向会出现外边距塌陷。

比如：box1设置盒子向下移动30px，box2设置盒子向上移动100px，这两个盒子之间的距离是100px，覆盖了小的30px。

##### 12.2.10.2 盒模型的计算

如果一个盒子设置了padding，border，width，height，margin。

盒子的真实宽度=width+2＊padding+2＊border

盒子的真实高度=height+2＊padding+2＊border

注意：标准盒模型，width不等于盒子真实的宽度，如果要保持盒子真实的宽度，那么加padding就要剪去width，相反减padding就一定要加width，真实高度一样设置。

#### 12.2.11 浮动与清除浮动

##### 12.2.11.1 标准流文档

文档元素在排版布局中，元素默认从左往右，从上往下，流式的排版布局，称这种布局为标准文档流。

**标准流文档下的围观现象**

- 空白折叠现象
    - 多个空格会被合并成一个空格显示到浏览器页面中。img／盒子标签换行写，会发现每张图片／盒子之间有间隙，如果在一行内写img／盒子标签，就解决了这个问题，但是我们不会这样去写我们的html结构。这种现象称为空白折叠现象。
- 高矮不齐，底边对齐
    - 文字还有图片大小不一，都会让我们页面的元素出现高矮不齐的现象，但是在浏览器查看我们的页面总会发现底边对齐
- 自动换行，一行写不满，换行写
    - 如果在一行内写文字，文字过多，那么浏览器会自动换行去显示我们的文字

##### 12.2.11.2 浮动

浮动是css里面布局最多的一个属性，也是很重要的一个属性。

float：表示浮动的意思。它有四个值：

- none: 表示不浮动，默认
- left: 表示左浮动
- right：表示右浮动
- inherit：继承父元素的浮动属性

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文字环绕</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		.box1{
			width: 300px;
			height: 300px;
			background-color: red;
			float: left;
		}
		.box2{
			width: 300px;
			height: 300px;
			background-color: green;
			float: right;
		}
		span{
			width: 100px;
			height: 200px;
			float: left;
			background-color: purple;
		}
	</style>	
</head>
<body>
	<div class="box1"></div>
	<div class="box2"></div>
	<span>浮动</span>
</body>
</html>
```

我们会发现，三个元素并排显示，.box1和span因为是左浮动，紧挨在一起，这种现象贴边。.box2盒子因为右浮动，所以紧靠着右边。

浮动元素的四大特性：

- 文字环绕

```html
<!DOCTYPE html>
<html>
<head>
	<title>文字环绕</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		/*文字环绕，把图片设为浮动即可*/
		.box img{
			float: left;
		}
	</style>	
</head>
<body>
	<div class="box">
		<img src="img/title图片.png">
		<p>
			浙江人中出了一个经济学家，很了不起，他总结了浙江人的工作哲学：“宁做创业狼，不做打工狗”，当然这话说的很极端，很多打工的朋友都不乐意听，但是我们仔细想想，这位老兄的话还真有点道理呢。
			狼为了寻求自由，宁愿独立人格，自由思想，天天奔跑在大草原上，肆意的猎杀牛羊，尽可能的享受大自然提供的一切美味，吃饱后就躺在草地上，什么都不想，享受阳光和自由的空气，他们是草原的主宰，他们有的是尊严。不过当严寒来临时，他们必须学会抗拒暴风雪的寒冷，学会在厚厚的雪堆下面寻找猎物，时常忍受饥饿的痛苦，随时担心自己冻饿而死。狼的生活可谓一半是海水，一半是火焰。
			浙江人中出了一个经济学家，很了不起，他总结了浙江人的工作哲学：“宁做创业狼，不做打工狗”，当然这话说的很极端，很多打工的朋友都不乐意听，但是我们仔细想想，这位老兄的话还真有点道理呢。
			狼为了寻求自由，宁愿独立人格，自由思想，天天奔跑在大草原上，肆意的猎杀牛羊，尽可能的享受大自然提供的一切美味，吃饱后就躺在草地上，什么都不想，享受阳光和自由的空气，他们是草原的主宰，他们有的是尊严。不过当严寒来临时，他们必须学会抗拒暴风雪的寒冷，学会在厚厚的雪堆下面寻找猎物，时常忍受饥饿的痛苦，随时担心自己冻饿而死。狼的生活可谓一半是海水，一半是火焰。
			浙江人中出了一个经济学家，很了不起，他总结了浙江人的工作哲学：“宁做创业狼，不做打工狗”，当然这话说的很极端，很多打工的朋友都不乐意听，但是我们仔细想想，这位老兄的话还真有点道理呢。
			狼为了寻求自由，宁愿独立人格，自由思想，天天奔跑在大草原上，肆意的猎杀牛羊，尽可能的享受大自然提供的一切美味，吃饱后就躺在草地上，什么都不想，享受阳光和自由的空气，他们是草原的主宰，他们有的是尊严。不过当严寒来临时，他们必须学会抗拒暴风雪的寒冷，学会在厚厚的雪堆下面寻找猎物，时常忍受饥饿的痛苦，随时担心自己冻饿而死。狼的生活可谓一半是海水，一半是火焰。
		</p>
	</div>
</body>
</html>
```

现象：所谓字围效果，当div浮动，p不浮动，div遮盖住了p，div的层级提高，但是p中的文字不会被遮盖，此时就形成了字围效果。

- 脱离了标准文档流

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动的现象</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		div{
			width: 200px;
			height: 200px;
			color: #fff;
		}
		div.left{
			background-color: red;
			float: left;
		}
		div.right{
			width: 300px;
			background-color: green; 
		}
	</style>
</head>
<body>
  <body>
	<!-- 浮动的现象：
			1.文字环绕
			2.脱离了标准文档流
			3.浮动元素互相贴靠
			4.浮动元素收缩现象 -->
	 <div class="left">左边的盒子</div>
	<div class="right">右边的盒子</div>
	<div class="center">最优的盒子</div>
</body>
</html>
```

现象：红色盒子压盖住了绿色的盒子，就是红色的盒子脱离的标准流，飘到了绿色盒子的上边

总结：所有的标签一旦设置浮动，就能够并排，并且都不区分行内、块状元素，都能够设置宽高

- 浮动元素互相贴靠

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动的现象</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		div{
			width: 200px;
			height: 200px;
			color: #fff;
		}
		div.left{
			background-color: red;
			float: left;
		}
		div.right{
			background-color: green; 
			float: left;
		}
		div.center{
			background-color: orange;
			float: left;
		}
	</style>
</head>
<body>
  <body>
	<!-- 浮动的现象：
			1.文字环绕
			2.脱离了标准文档流
			3.浮动元素互相贴靠
			4.浮动元素收缩现象 -->
	 <div class="left">左边的盒子</div>
	<div class="right">右边的盒子</div>
	<div class="center">最优的盒子</div>
</body>
</html>
```

现象：如果都设置了向一个方向浮动，就会产生互相贴靠

- 浮动元素收缩现象

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动的现象</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		div{
			height: 200px;
			color: #fff;
		}
		div.left{
			background-color: red;
			float: left;
		}
		div.right{
			background-color: green; 
		}
		div.center{
			background-color: orange;
		}
	</style>
</head>
<body>
  <body>
	<!-- 浮动的现象：
			1.文字环绕
			2.脱离了标准文档流
			3.浮动元素互相贴靠
			4.浮动元素收缩现象 -->
	<div class="left">左边的盒子</div>
	<div class="right">右边的盒子</div>
	<div class="center">最优的盒子</div>
</body>
</html>
```

收缩：一个浮动元素。如果没有设置width，那么就自动收缩为文字的宽度（这点跟行内元素很像）

注意：关于浮动，我们一定要遵循一个原则，永远不是一个盒子单独浮动，要浮动就要一起浮动。另外，有浮动，一定要清除浮动。

##### 12.2.11.3 浮动元素的破坏性

在页面布局的时候，每个结构中父元素的高度，我们一般不会设置。

在网页开发中，我们写完页面后，根据需求我们肯定会在之前写好的页面中增加或修改页面，比如：修改图片的高度，增加一点内容，如果我们每一个地方去增加或修改必定会影响我们的开发效率。

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动元素的破坏性与清除</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		.father{
			/*子元素浮动 父盒子一般不设置高度*/
      		/*出现这种问题，我们要清除浮动带来影响*/
			border: 1px solid red;
		}
		.child1{
			width: 200px;
			height: 100px;
			background-color: green;
			float: left;
		}
		.child2{
			width: 200px;
			height: 100px;
			background-color: orange;
			float: right;
		}
		.header{
			width: 100%;
			height: 100px;
			background-color: purple;
		}
	</style>
</head>
<body>
	<div class="father clearfix">
		<div class="child1">儿子</div>
		<div class="child2">二儿子</div>
	</div>
	<div class="header"></div>
</body>
</html>
```

现象：如果不给父盒子设置一个高度，那么浮动子元素是不会填充父盒子的高度，那么`header`的盒子会覆盖到第一个盒子的位置上，影响页面布局。

浮动元素确实能实现页面元素并排的效果，这是它的好处，同时它还带来了页面布局极大的错乱，要清除浮动。

常用的清除浮动的三种方法：

- 1.给父盒子设置高度

    - 缺点：使用不灵活，后期不易维护
    - 应用：网页中盒子固定高度区域，比如固定导航栏

    示例：html文件

    ```html
    <!DOCTYPE html>
    <html>
    <head>
    	<title>浮动元素的破坏性与清除</title>
    	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
    	<style type="text/css">
    		.father{
          		/*给第一个父盒子设置一个高度*/
       			height: 100px;
    			border: 1px solid red;
    		}
    		.child1{
    			width: 200px;
    			height: 100px;
    			background-color: green;
    			float: left;
    		}
    		.child2{
    			width: 200px;
    			height: 100px;
    			background-color: orange;
    			float: right;
    		}
    		.header{
    			width: 100%;
    			height: 100px;
    			background-color: purple;
    		}
    	</style>
    </head>
    <body>
    	<div class="father clearfix">
    		<div class="child1">儿子</div>
    		<div class="child2">二儿子</div>
    	</div>
    	<div class="header"></div>
    </body>
    </html>
    ```

- 2.内墙法

    - 有三个值：
        - left：当前元素左边不允许有浮动元素
        - right：当前元素右边不允许有浮动元素
        - both：当前元素左右两边不允许有浮动元素
    - 规则：在最后一个浮动元素的后面加一个空的块级元素，并且设置该属性clear：both
    - 缺点：结果冗余，网页中有很多这种情况，每个地方都加一遍代码就会冗余。

    示例：html文件

    ```html
    <!DOCTYPE html>
    <html>
    <head>
    	<title>浮动元素的破坏性与清除</title>
    	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
    	<style type="text/css">
    		.father{
    			border: 1px solid red;
    		}
    		.child1{
    			width: 200px;
    			height: 100px;
    			background-color: green;
    			float: left;
    		}
    		.child2{
    			width: 200px;
    			height: 100px;
    			background-color: orange;
    			float: right;
    		}
    		.header{
    			width: 100%;
    			height: 100px;
    			background-color: purple;
    		}
        /*给浮动元素的后面加一个空的div，
        并且该元素不浮动，然后设置clear：both*/
        .clear{
    			clear: both;
    		}
    	</style>
    </head>
    <body>
    	<div class="father clearfix">
    		<div class="child1">儿子</div>
    		<div class="child2">二儿子</div>
    		<!-- 第二种方法 clear:both -->
    		<div class="clear"></div>
    	</div>
    	<div class="header"></div>
    </body>
    </html>
    ```

- 3.伪元素清除法(常用)

    - 示例：html文件

    ```html
    <!DOCTYPE html>
    <html>
    <head>
    	<title>浮动元素的破坏性与清除</title>
    	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
    	<style type="text/css">
    		.father{
    			border: 1px solid red;
    		}
    		.child1{
    			width: 200px;
    			height: 100px;
    			background-color: green;
    			float: left;
    		}
    		.child2{
    			width: 200px;
    			height: 100px;
    			background-color: orange;
    			float: right;
    		}
    		.header{
    			width: 100%;
    			height: 100px;
    			background-color: purple;
    		}
        /*给浮动子元素的父盒子，
        也就是不浮动元素，添加一个clearfix的类，然后设置*/
        .clearfix::after{
          /*必须要写这三句话*/
    			content: ' ';
    			display: block;
    			clear: both;
    		}
    	</style>
    </head>
    <body>
    	<div class="father clearfix">
    		<div class="child1">儿子</div>
    		<div class="child2">二儿子</div>
    	</div>
    	<div class="header"></div>
    </body>
    </html>
    ```

- 4.overflow:hidden清除(常用)

其实它是一个BFC区域：BFC (Block Formtting Context) 

 https://blog.csdn.net/riddle1981/article/details/52126522

规则：计算BFC(块级盒子)高度时，浮动元素(两边的盒子)也参与计算

形成BFC的条件：除了overflow:visitable的属性值

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动元素的破坏性与清除</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		.father{
      /*BFC (Block Formtting Context) 区域 
      一条规则：计算BFC(块级盒子)高度时，浮动元素(两边的盒子)也参与计算
			形成BFC的条件：除了overflow:visitable的属性值*/
   			overflow: hidden;
			border: 1px solid red;
		}
		.child1{
			width: 200px;
			height: 100px;
			background-color: green;
			float: left;
		}
		.child2{
			width: 200px;
			height: 100px;
			background-color: orange;
			float: right;
		}
		.header{
			width: 100%;
			height: 100px;
			background-color: purple;
		}
	</style>
</head>
<body>
	<div class="father clearfix">
		<div class="child1">儿子</div>
		<div class="child2">二儿子</div>
	</div>
	<div class="header"></div>
</body>
</html>
```

overflow属性规定当内容溢出元素框时发生的事情。

说明：这个属性定义溢出元素内容区的内容会如何处理。如果值为 scroll，不论是否需要，用户代理都会提供一种滚动机制。因此，有可能即使元素框中可以放下所有内容也会出现滚动条。

overflow的5个值：

| 值      | 描述                                                     |
| :------ | :------------------------------------------------------- |
| visible | 默认值。内容不会被修剪，会呈现在元素框之外。             |
| hidden  | 内容会被修剪，并且其余内容是不可见的。                   |
| scroll  | 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。 |
| auto    | 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。 |
| inherit | 规定应该从父元素继承 overflow 属性的值。                 |

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>overflow</title>
	<style type="text/css">
		body{
			overflow: scroll;
		}
		.box{
			width: 300px;
			height: 300px;
			border: 1px solid red;
			overflow: hidden;
		}
	</style>
</head>
<body>
	<div class="box">
		中华民族创造了灿烂的中华文明，为人类作出了卓越贡献，成为世界上伟大的民族。鸦片战争后，由于西方列强的入侵和封建统治的腐败，中国逐渐陷入半殖民地半封建社会的黑暗深渊，中国人民经历了战乱频仍、山河破碎、民不聊生的深重苦难。自强不息的中华民族从未放弃对美好梦想的向往和追求。习近平总书记指出：“实现中华民族伟大复兴，就是中华民族近代以来最伟大的梦想。”为了实现这个伟大梦想，中国人民和无数仁人志士进行了千辛万苦的探索和不屈不挠的斗争。可是，从太平天国运动、戊戌变法到义和团运动，一次次奋起抗争都失败了。孙中山先生领导的辛亥革命，虽然结束了统治中国几千年的君主专制制度，对推动中国社会进步具有重大意义，但也未能改变旧中国半殖民地半封建的社会性质和中国人民的悲惨命运。近代中国历史表明，旧式农民战争和软弱的资产阶级革命都不可能完成中华民族救亡图存和反帝反封建的历史任务，更不可能承担起实现民族复兴的历史使命。
	</div>
</body>
</html>
```

规则：计算BFC(块级盒子)高度时，浮动元素(两边的盒子)也参与计算

形成BFC的条件：除了overflow:visitable的属性值

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动元素的破坏性与清除</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		.father{
   			overflow: hidden;
			border: 1px solid red;
		}
		.child1{
			width: 200px;
			height: 100px;
			background-color: green;
			float: left;
		}
		.child2{
			width: 200px;
			height: 100px;
			background-color: orange;
			float: right;
		}
		.header{
			width: 100%;
			height: 100px;
			background-color: purple;
		}
	</style>
</head>
<body>
	<div class="father clearfix">
		<div class="child1">儿子</div>
		<div class="child2">二儿子</div>
	</div>
	<div class="header"></div>
</body>
</html>
```

#### 12.2.12 定位

定位分为三种：

- 相对定位：relative
- 绝对定位：absolute
- 固定定位：fixed

##### 12.2.12.1 相对定位

相对定位：不脱离标准文档流，可以调整元素

现象和使用：

- 如果对当前元素仅仅设置了相对定位，那么它和其它标准流的盒子没什么区别
- 设置相对定位后，才可以使用四个方向的属性： top、bottom、left、right

所以说相对定位 在页面中没有什么太大的作用，影响我们页面的布局。我们不要使用相对定位来做压盖效果。

用途：

1.微调元素位置

2.做绝对定位的参考（父相子绝）绝对定位会说到此内容。

参考点：

以原来的位置作为参考点，进行移动

```html
<!DOCTYPE html>
<html>
<head>
	<title>相对定位</title>
	<style type="text/css">
		div{
			width: 200px;
			height: 200px;
			color: #fff;
		}
		div.one{
			background-color: red;
			position: relative;
			top: 30px;
			left: 100px;
		}
		div.two{
			background-color: green;
			left: 40px;
			bottom: 50px;
		}
		div.three{
			background-color: blue;
		}
	</style>
</head>
<body>
	<!-- 相对定位：
			不脱离标准文档流，可以调整元素
		 参考点：
			以原来的位置为参考点 -->
	<div class="one">one</div>
	<div class="two">two</div>
	<div class="three">three</div>
</body>
</html>
```

##### 12.2.12.2 绝对定位

特性：

- 脱标，不在页面上占位置
- 压盖现象，层级提高，意思相当于飘起来
- 不区分行内，块级元素，都能设置宽高

参考点：

相对于最近非static(默认静态)祖先元素定位，如果没有非static祖先元素，那么以页面根元素左上角进行定位。

网站中做站，经常用到的是父相子绝，但是不仅仅是父相子绝，父绝子绝 ，父固子绝,都是以父辈元素为参考点，也就是上面所说的非static元素。

注意⚠️：父绝子绝，没有实战意义，做站的时候不会出现父绝子绝。因为绝对定位脱离标准流，影响页面的布局。相反‘父相子绝’在我们页面布局中，是常用的布局方案。因为父亲设置相对定位，不脱离标准流，子元素设置绝对定位，仅仅的是在当前父辈元素内调整该元素的位置。

绝对定位的盒子无视父辈的padding！

```html
<!DOCTYPE html>
<html>
<head>
	<title>绝对定位</title>
	<style type="text/css">
		body{
			border: 1px solid orange;
		}
		.grandfather{
			border: 1px solid purple;
			position: relative;
			top: 20px;
			left: 30px;
		}
		.father{
			border: 1px solid black;
			margin-left: 40px;
			margin-top: 20px;
			position: relative;
			top: 30px;
			left: 60px;
		}
		.one,.two,.three{
			width: 200px;
			height: 200px;
			color: #fff;
		}
		div.one{
			background-color: red;
			position: absolute;
			top: 200px;
			left: 200px;
		}
		div.two{
			background-color: green;
			width: 400px;
			/*position: absolute;*/
		}
		div.three{
			background-color: blue;
		}
	</style>
</head>
<body>
	<!-- 特点：
			1.脱离标准文档流，不在页面上占位置
			2.压盖现象，层级提高 
		 参考点：
			相对于最近非static祖先元素定位，如果没有非static祖先元素，那么以页面根元素左上角进行定位
		 网站中的：子绝父相-->
	<div class="grandfather">
		<div class="father">
			<div class="one">one</div>
			<div class="two">two</div>
			<div class="three">three</div>
		</div>
	</div>
</body>
</html>
```

##### 12.2.12.3 固定定位

固定定位：固定当前的元素不会随着页面滚动而滚动

特性：

- 脱标
- 压盖现象，层级提高
- 一旦设置固定定位，在页面中滚动网页，固定不变

参考点：

以浏览器的边角作为参考点

作用：

- 返回顶部栏
- 固定导航栏
- 页面小广告

```html
<!DOCTYPE html>
<html>
<head>
	<title>固定定位</title>
	<style type="text/css">
		.box{
			width: 100px;
			height: 100px;
			background-color: red;
			color: #fff;
		}
		#one{
			position: fixed;
			top: 80px;
			left: 20px;
		}
		.other{
			width: 300px;
			height: 200px;
			overflow: scroll;
			padding-left: 200px;
		}
	</style>
</head>
<body>
	<div class="other">
		<p>
			【环球时报-环球网报道 记者 张骜】香港激进示威者连日来制造事端，外媒关注到我国防部新闻发言人吴谦日前在被问及解放军应对香港目前形势发展的表态。26日，在外交部例行记者会上，有记者就美国国务卿蓬佩奥在接受媒体采访谈及中国解放军驻港部队等相关问题提问。对此，中国外交部发言人华春莹进行了驳斥
		</p>
		<p>
			华春莹说，我注意到了蓬佩奥担心驻港部队是否介入以及香港近期发生事态的一系列表态，我们之前一直强调中央政府支持特区政府依法履职，依法采取措施，维护香港的稳定、安全与繁荣。前几天我强调过，香港是中国的香港，中国绝不会允许任何外国势力插手和干预香港事务。对于现在有些外界人士对驻港部队的关切和言论，国防部新闻发言人已经就驻港部队依法履职尽职尽责做出了明确的表态。
		</p>
		<div class="box" id="one">one</div>
	</div>
</body>
</html>
```

##### 12.2.12.4 浮动和定位给行内元素带来的现象

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动和定位给行内元素带来的现象</title>
	<style type="text/css">
		span{
			/*float: left;*/
			position: fixed;
			background-color: red;
			width: 200px;
			height: 200px;
			/*
			总结：
				设置浮动、绝对定位、固定定位、都可以给行内标签设置宽高,相对定位不改变标签属性。
				不是只有通过display转换成block才能设置标签
			*/
		}
	</style>
</head>
<body>
	<span>我是行内元素</span>
</body>
</html>
```

总结：

- 设置浮动，绝对定位，固定定位，都可以给行内标签设置宽高，相对定位不改变标签属性
- 不是只有通过display转换成块级标签才能设置标签

##### 12.2.12.5 z-index

z-index非常简单，它有四大特性，每个特性你记住了，页面布局就不会出现找不到盒子的情况

- z-index 值表示层级高低，数值大的压盖住数值小的
- 只有定位了的元素，才能有z-index,也就是说，不管相对定位，绝对定位，固定定位，都可以使用z-index，而浮动元素不能使用z-index
- z-index值没有单位，就是一个正整数，默认的z-index值为0，如果都没有z-index值，或者z-index值一样，那么谁写在HTML后面，谁的层级高。定位了的元素，层级永远高于没有定位的元素
- 从父现象：父亲怂了，儿子再牛逼也没用

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>z-index的讲解</title>
	<style type="text/css">
		.a{
			position: relative;
			width: 200px;
			height: 40px;
			background-color: #C3FFFB;
			border: 3px solid #3962FE;
			z-index: 1;

		}
		.b{
			position: relative;
			width: 200px;
			height: 40px;
			background-color: #C3FFFB;
			border: 3px solid #3962FE;
			top: -30px;
			left: 50px;
			z-index: 10000;

		}
		.c{
			position: relative;
			width: 200px;
			height: 40px;
			background-color: #C3FFFB;
			border: 3px solid #3962FE;
			top: -50px;
			left: 100px;
			/*默认值为auto*/
			/*z-index: auto;*/
			z-index:10;
		}
	</style>
</head>
<body>
	<div style="position: relative;z-index: 15;">
		<div class="a">A</div>
	</div>
	
	<div style="position: relative;z-index: 10;">
		<div class="b">B</div>
	</div>
	<div class="c">C</div>
</body>
</html>
```

#### 12.2.13 雪碧图技术

雪碧图的场景

- 静态图片，不随用户信息变化而变化
- 小图片，图片比较小(2-3kb)
- 加载量比较大
    - 一些大图不建议使用雪碧图

优点：

- 有效的减少了HTTP请求数量
- 加速内容显示

优点解释：

每请求一次，就会和服务器链接一次，建立链接需要额外的时间开销，采用雪碧图技术，减少了HTTP请求次数。

原理：

通过css的背景属性的background-position来控制雪碧图的显示。

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>css sprite雪碧图技术</title>
	<style type="text/css">
		div{
			width: 25px;
			height: 25px;
			display: inline-block;
			/*35 ＊ 895*/
			background: url('img/xbt.png') no-repeat 0 0;
			/*控制背景图大小*/
			background-size: 17.5px 447.5px;
		}
		.sprite1{
			background-position: 0 0;
		}
		.sprite2{
			background-position: 0 -33px;
		}
		.sprite3{
			background-position: 0 -66px;
		}
		.sprite4{
			background-position: 0 -99px;
	</style>
</head>
<body>
	<div class="sprite1"></div>
	<div class="sprite2"></div>
	<div class="sprite3"></div>
	<div class="sprite4"></div>
</body>
</html>
```

备注：测量好图片x，y轴的距离，通过background-position属性进行设置即可。

#### 12.2.14 其他练习

##### 12.2.14.1 制作圆/圆环/半圆

- border－radius：设置盒子模型圆角

示例：圆

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框属性</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
			/*切一个圆形*/
			border-radius: 50%;
		}
	</style>
</head>
<body>
	<div class="box"></div>
</body>
</html>
```

示例：圆环、半圆

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框属性</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 100px;
			/*切一个半圆*/
			border-top-left-radius: 100px;
			border-top-right-radius: 100px;
			border: 5px solid purple;
		}
	</style>
</head>
<body>
	<div class="box"></div>
</body>
</html>
```

##### 12.2.14.2 盒子阴影

- box－shadow：设置当前盒子模型阴影

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框阴影</title>
	<style type="text/css">
		.shandow{
			position: relative;
			width: 200px;
			height: 200px;
			margin: 50px auto;
			background-color: purple;
		}
		.shandow:hover{
			top: 3px;
			/*1.水平偏移方向
			  2.垂直偏移方向
			  3.阴影的模糊程度
			  4.阴影的颜色
			  5.默认outset外设，可以设置为inset内设
			*/
			box-shadow: 0 15px 20px red;
		}
	</style>
</head>
<body>
	<div class="shandow"></div>
</body>
</html>
```

##### 12.2.14.3 单列布局

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>网页常见布局方案－单列布局</title>
	<style type="text/css">
		*{
			margin: 0;
			height: 100%;
		}
		.header{
			width: 100%;
			height: 60px;
			line-height: 60px;
			text-align: center;
			background-color: #000;
		}
		.container{
			width: 1200px;
			margin: 0 auto;
		}
		.header .container{
			height: 60px;
			background-color: orange;
		}
		.wrap{
			width: 100%;
			height: 100%
		}
		.wrap .container{
			height: 100%;
			background-color: red;
		}
		.foot{
			width: 100%;
			height: 100%;
		}
		.foot .container{
			height: 100px;
			background-color: green;
		}
	</style>
</head>
<body>
	<!-- 头部 -->
	<div class="header">
		<div class="container">头部</div>
	</div>
	<!-- 主体内容 -->
	<div class="wrap">
		<div class="container">主体内容</div>
	</div>
	<!-- 脚部 -->
	<div class="foot">
		<div class="container">脚步</div>
	</div>
</body>
</html>
```

##### 12.2.14.4 多列布局

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>网页常见布局方案－多列布局</title>
	<style type="text/css">
		*{
			margin: 0;
			height: 100%;
		}
		.header{
			width: 100%;
			height: 60px;
			line-height: 60px;
			text-align: center;
			background-color: #000;
		}
		.container{
			width: 1200px;
			margin: 0 auto;
		}
		.header .container{
			height: 60px;
			background-color: orange;
		}
		.wrap{
			width: 100%;
			height: 100%
		}
		.wrap .container{
			height: 100%;
		}
		.wrap .left{
			width: 10%;
			height: 100%;
			float: left;
			background-color: yellowgreen;
		}
		.wrap .right{
			width: 10%;
			height: 100%;
			float: right;
			background-color: yellow;
		}
		.wrap .center{
			height: 100%;
			background-color: purple;
			margin: 0 130px;
		}
		.foot{
			width: 100%;
			height: 100%;
		}
		.foot .container{
			height: 100px;
			background-color: green;
		}
	</style>
</head>
<body>
	<!-- 头部 -->
	<div class="header">
		<div class="container">头部</div>
	</div>
	<!-- 主体内容 -->
	<div class="wrap">
		<div class="container">
			<div class="left"></div>
			<div class="right"></div>
			<div class="center">
				主体内容
			</div>
		</div>
	</div>
	<!-- 脚部 -->
	<div class="foot">
		<div class="container">脚步</div>
	</div>
</body>
</html>
```

##### 12.2.14.5 **元素水平垂直居中**

**1.行内元素水平垂直居中**

- display: table-cell：转换成单元格形式
- vertical-align: middle：垂直方向排列设置

```css
/*方式一：水平垂直居中*/
text-align: center;
/*等于盒子模型的高度*/
/*line-height: 200px;*/

/*方式二：水平垂直居中*/
text-align: center;
/*转换成单元格形式*/
display: table-cell;
/*垂直方向-排列方式：三个值：1.top 2.middle 3.bottom */
vertical-align: middle;
```

完整代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
	<title>行内元素水平垂直居中</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
			color: #fff;

			/*方式一：水平垂直居中*/
			text-align: center;
			/*等于盒子模型的高度*/
			/*line-height: 200px;*/

			/*方式二： 转换成单元格形式*/
			display: table-cell;
			/*垂直方向-排列方式：三个值：1.top 2.middle 3.bottom */
			vertical-align: middle;
		}
		td{
			width: 100px;
			height: 100px;
			background-color: green;
			text-align: center;
			vertical-align: middle;
		}
	</style>
</head>
<body>
	<div class="box">
		ike的博客
	</div>
	<table>
		<tr>
			<td>Mjj</td>
		</tr>
	</table>
</body>
</html>	
```

**2.块级元素水平垂直居中**

**1.行内元素水平垂直居中**

- display: table-cell：转换成单元格形式
- vertical-align: middle：垂直方向排列设置

```html
/*方式一：水平垂直居中*/
text-align: center;
/*等于盒子模型的高度*/
/*line-height: 200px;*/

/*方式二：水平垂直居中*/
text-align: center;
/*转换成单元格形式*/
display: table-cell;
/*垂直方向-排列方式：三个值：1.top 2.middle 3.bottom */
vertical-align: middle;
```

完整代码：

```html
<!DOCTYPE html>
<html>
<head>
	<title>行内元素水平垂直居中</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
			color: #fff;

			/*方式一：水平垂直居中*/
			text-align: center;
			/*等于盒子模型的高度*/
			/*line-height: 200px;*/

			/*方式二： 转换成单元格形式*/
			display: table-cell;
			/*垂直方向-排列方式：三个值：1.top 2.middle 3.bottom */
			vertical-align: middle;
		}
		td{
			width: 100px;
			height: 100px;
			background-color: green;
			text-align: center;
			vertical-align: middle;
		}
	</style>
</head>
<body>
	<div class="box">
		ike的博客
	</div>
	<table>
		<th>
			<td>Mjj</td>
		</th>
	</table>
</body>
</html>
```

**2.块级元素水平垂直居中**

方式一：position+margin

完整代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
	<title>块级元素水平垂直居中</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
			position: relative;
		}
		.child{
			width: 100px;
			height: 100px;
			background-color: green;
			position: absolute;
			margin: auto;
			left: 0;
			right: 0;
			top: 0;
			bottom: 0;
		}
		td{
			width: 100px;
			height: 100px;
			background-color: orange;
			vertical-align: middle;
			text-align: center;
		}
		span{
			display: inline-block;
			width: 50px;
			height: 50px;
			background-color: red;
			line-height: 50px;
		}
	</style>
</head>
<body>
	<!-- position+margin -->
	<div class="box">
		<div class="child"></div>
	</div>
	<table>
		<tr>
			<td>
				<span>ABC</span>
			</td>
		</tr>
	</table>
</body>
</html>
```

方式二：

示例：display：table-cell

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<title>块级元素水平垂直居中二</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
			display: table-cell;
			vertical-align: middle;
			text-align: center;
		}
		.child{
			width: 100px;
			height: 100px;
			background-color: green;
			display: inline-block;
			line-height: 100px;
		}
		td{
			width: 100px;
			height: 100px;
			background-color: orange;
			vertical-align: middle;
			text-align: center;
		}
		span{
			display: inline-block;
			width: 50px;
			height: 50px;
			background-color: red;
			line-height: 50px;
		}
	</style>
</head>
<body>
<!-- display：table-cell -->
	<div class="box">
		<div class="child">块垂直居中</div>
	</div>
	<table>
		<tr>
			<td>
				<span>
					ABC
				</span>
			</td>
		</tr>
	</table>
</body>
</html>
```

方式三：

示例：只通过定位实现

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<title>块级元素水平垂直居中三</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
			display: table-cell;
			vertical-align: middle;
			text-align: center;
		}
		.child{
			width: 100px;
			height: 100px;
			background-color: green;
			display: inline-block;
			line-height: 100px;
		}
		td{
			width: 100px;
			height: 100px;
			background-color: orange;
			vertical-align: middle;
			text-align: center;
		}
		span{
			display: inline-block;
			width: 50px;
			height: 50px;
			background-color: red;
			line-height: 50px;
		}
		.wrap{
			width: 200px;
			height: 200px;
			background-color: purple;
			position: relative;
		}
		.xiongda{
			width: 100px;
			height: 100px;
			background-color: yellow;
			position: absolute;
			top: 50%;
			left: 50%;
			margin-left: -50px;
			margin-top: -50px;
		}
	</style>
</head>
<body>	
	<div class="box">
		<div class="child">块垂直居中</div>
	</div>
	<table>
		<tr>
			<td>
				<span>
					ABC
				</span>
			</td>
		</tr>
	</table>
	<!-- 纯定位实现 -->
	<div class="wrap">
		<div class="xiongda"></div>
	</div>
</body>
</html>
```

### 12.3 JavaScript

#### 12.3.1 JavaScript简介

web前端有三层：

- HTML：从语义的角度，描述页面的结构（搭建框架）
- CSS：从审美的角度，描述样式（美化页面）
- JavaScript：从交互的角度，描述行为（提升用户体验）

**历史背景介绍**：

布兰登.艾奇 1995年在网景公司 发明的JavaScript

一开始的JavaScrip叫LiveScript

同一个时期 比如 VBScript,JScript等，但是后来被JavaScript打败了，**现在的浏览器只运行一种脚本语言叫JavaScript**

**JavaScrit的发展**：

**2003**年之前，JavaScript被认为“牛皮鲜”，用来制作页面上的广告，弹窗、漂浮的广告。什么东西让人烦，什么东西就是JavaScript开发的。所以浏览器就推出了屏蔽广告功能。

**2004**年，JavaScript命运开始改变，那一年，**谷歌公司开始带头使用Ajax技术**，Ajax技术就是JavaScript的一个应用。并且，那时候人们逐渐开始提升用户体验了。Ajax有一些应用场景。比如，当我们在百度搜索框搜文字时，输入框下方的智能提示，可以通过Ajax实现。比如，当我们注册网易邮箱时，能够及时发现用户名是否被占用，而不用调到另外一个页面。

**2007**年乔布斯发布了第一款iPhone，这一年开始，用户就多了上网的途径，就是用移动设备上网。**JavaScript在移动页面中，也是不可或缺的**。并且这一年，互联网开始标准化，按照W3C规则三层分离，JavaScript越来越被重视。

**2010**年，人们更加了解**HTML5技术**，**HTML5推出了一个东西叫做Canvas**（画布），工程师可以在Canvas上进行游戏制作，利用的就是JavaScript。

**2011**年，**Node.js诞生**，使JavaScript能够开发服务器程序了。

React-native inoic

如今，**WebApp**已经非常流行，就是用**网页技术开发手机应用**。手机系统有iOS、安卓。比如公司要开发一个“携程网”App，就需要招聘三队人马，比如iOS工程师10人，安卓工程师10人，前端工程师10人。共30人，开发成本大；而且如果要改版，要改3个版本。现在，假设公司都用web技术，用html+css+javascript技术就可以开发App。也易于迭代（网页一改变，所有的终端都变了）。

虽然目前WebApp在功能和性能上的体验远不如Native App，但是“WebApp慢慢取代Native App”很有可能是未来的趋势。

**JavaScrit的组成**：

- **ECMAScript 5.0**：定义了js的语法标准： 包含变量 、表达式、运算符、函数、if语句 for循环 while循环、内置的函数
- **DOM** ：操作网页上元素的API。比如让盒子显示隐藏、变色、动画 form表单验证
- **BOM**：操作浏览器部分功能的API。比如刷新页面、前进后退、让浏览器自动滚动

#### 12.3.2 JS基础（ECMAScript 5.0）

##### 12.3.2.1 JS的引入方式

内接式与外接式：

示例：

```js
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>js文件的引入</title>
	<!-- 内部式：js -->
	<script type="text/javascript">
		// 编写js代码
		alert('弹出框');
		console.log('控制台');
	</script>
	<!-- 外接式：引入js文本，代码写在引入的文本中 -->
	<script type="text/javascript" src="js_code/index.js"></script>
</head>
<body>
</body>
</html>
```

##### 12.3.2.2 调试方法

- alert为浏览器弹出框。
- console为浏览器F12控制台。

##### 12.3.2.3 代码注释

单行注释与多行注释：

示例：

```js
// 快捷键:Ctrl + /
// 单行注释：注释单行代码

/*
多行注释：注释多行代码
*/
```

##### 12.3.2.4 变量

- 变量定义：var就是一个**关键字**，用var来定义变量，关键字后面一定要有空格隔开。
- 变量赋值：等号表示赋值，将等号右边的值，赋值给左边的变量。
- 变量名：变量名要见名知意。

变量命名规范：

- 必须使用字母、下划线、$构成。
- 不能使用js中关键字和保留字来命名
- 严格区分大小写
- 长变量名尽量写成驼峰或以下划线连接

示例：

```js
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>变量</title>
	<script type="text/javascript">
		// 初始化变量：声明+赋值
		var x = 30;
		//声明变量
		var y;
		// 变量赋值
		y = 50;
		var name = 'ike';
		/*命名规则:
		1.必须使用字母、下划线、$开始
		2.多个英文字母：驼峰式
		3.不能使用js中关键字和保留字来命名
		4.严格区分大小写
		*/
		var _a = 40;
		var $ = 60;
		var z = 20;
		z = 30;
		alert(z)
	</script>
</head>
<body>
</body>
</html>
```

#### 12.3.3 数据类型

##### 12.3.3.1 基本数据类型

- 数值类型：number

    - 如果一个变量中，存放了数字，这个变量就是数值类型

    示例：

    ```js
    var a = 3;  //定义了一个变量a，并且赋值100
    var b = 1.23;
    var c = -1;
    var d = 6 / 0; 
    // typeof：检查当前变量的数据类型
    alert(typeof a);
    alert(typeof b);
    console.log(d); //Infinity 无限大
    alert(typeof d); //number 类型
    # 在javascript中，只要是数，都是数值类型，不区分整数、浮点数、正数、负数
    ```

- 字符串类型：string

    - 用单引号或双引号引起来的字符或数字等类型，称为字符串

    示例：

    ```js
    var name = 'asdf12';
    var en = '123';
    alert(typeof name);
    alert(typeof en);
    // 字符串 + 数值 相当于字符串的拼接
    console.log('我'+'哎'+1);
    // 小技巧  将数值类型转换成字符串类型
    var c = 10+'';
    console.log(typeof c);
    ```

- 布尔类型：boolean

    - 判断True或False

    示例：

    ```js
    var isShow = 1 > 1;
    console.log(isShow)
    console.log(typeof isShow);
    ```

- 未定义：undefined

    示例：

    ```js
    var  d1;
    console.log(d1); //值 是undefined
    console.log(typeof d1); //undefined 数据类型 
    ```

- 空对象：null

    示例：

    ```js
    var d = null; //空对象 object
    console.log(typeof d);
    ```

##### 12.3.3.2 引用数据类型

- 函数：Function

- 对象：Object

- 数组：Arrary

    - 示例：object类型

    ```js
    // 创建 
    var shopping = ['aaa','bbb','ccc']
    // alert(shopping);
    // alert(typeof shopping)
    
    var rand = ['android', 'apple',['1','2','3']]
    console.log(rand)
    // 访问
    var item = rand[2];
    console.log(item)
    // 修改
    rand[0] = '榴莲';
    console.log(rand);
    
    //访问数组的长度
    console.log('数组的长度是：' + rand.length);
    ```

- 字符串：String

- 日期：Date

##### 12.3.3.3 运算符

赋值运算符：

以var x = 12，y=5来演示示例：

![1643078679798](J:\homework\Python学习笔记\Python_notes.assets\1643078679798.png)

算数运算符：

var a = 5，b=2

![1643078694572](J:\homework\Python学习笔记\Python_notes.assets\1643078694572.png)

比较运算符：

var x = 5；

![1643078665588](J:\homework\Python学习笔记\Python_notes.assets\1643078665588.png)

注意：==比较的是值的相同，===比较的是值和数据类型（内存地址）

示例：

```js
var x = 5;
var y = '5';

// == 比较的是值的相同
// === 等同于  比较的是值和数据类型（内存地址）
console.log(x==y) //true
console.log(typeof x)//number
console.log(typeof y)//sting
console.log(x===y)//false
```

示例：a++与++a

```js
//  先将a的值赋值给b输出，然后再对a++ a此时是6
var a = 5;
var b = a++;
console.log(a); //6
console.log(b); //5
```

```js
// 先a++ 将a输出 在将输出的值赋值给b
var a = 5;
var b = ++a;
console.log(a); //6
console.log(b);//6
```

##### 12.3.3.4 数据类型的转换

**1.将number类型转换成string类型：**

隐式转换：

示例：

```js
// 隐式转换
var num = 1346.768;
console.log(''+num);
console.log(''.concat(num));
```

强制转换：

示例：

```js
// 强制类型转换
var num = 1346.768;
console.log(num.toString());
console.log(typeof num.toString());
console.log(String(num));
// 保留两位小数
console.log(num.toFixed(2));
```

**2.将string类型转换成number类型：**

示例：

```js
var str = '131313.9254136';
// 字符串转换整型
console.log(parseInt(str));
// 字符串转换浮点型
console.log(parseFloat(str));
console.log(typeof parseFloat(str));
```

示例：NaN

```js
// NaN
var str1 = '1313.stssgg985'
console.log(Number(str1));// NaN Not a Number 是一个number类型
console.log(isNaN(str1));// 判断是否NaN
```

**3.解析字符串，并且返回整数和浮点型：**

示例：

```js
// parseInt() parseFloat() 解析字符串，并且返回整数和浮点型
console.log(parseInt(stringNum2));//13
console.log(parseFloat(stringNum2));//13.1313
```

#### 12.3.4 流程控制

**if：**

示例：

```js
var age = 20;
if(age > 18){
    // {}作为当前的作用域
    console.log('打印的内容');
}
console.log(22222); //这行代码照样执行
```

**if..else：**

示例：

```js
var age = 16;
if(age > 18){
    // {}作为当前的作用域
    console.log('打印的内容');
}else{
    console.log('好好学前端');
}
console.log(22222); //代码照样执行
```

**if..else if..else：**

示例：

```js
var age = 1313;
if (age == 18) {
    //{}相当于作用域
    console.log('打印的内容');
} else if (age == 30) {
    console.log('好好学前端');
} else {
    console.log('随便你了')
}
console.log('alex'); //下面的代码照样执行
```

**逻辑&&与：**必须两个条件都成立才算成立

示例：

```js
var sum = 401;
var math = 90;
if(sum>400 && math>=90){
console.log('清华大学录入成功')
}else{
console.log('高考失利')
}
```

**逻辑||或：**有一个条件成立就算成立

示例：

```js
var sum = 400;
var math = 90;
if(sum>400 || math>=90){
    console.log('清华大学录入成功')
}else{
    alert('高考失利')
}
```

##### 12.3.4.1 三元运算

示例：

```js
var isres = 1 >2 ? '真的' : '假的';
alert(isres);
```

##### 12.3.4.2 for循环

示例：for循环遍历列表是最常用的对数据的操作

```js
//输出1~10之间的数
for(var i = 1;i<=10;i++){
     console.log(i)
 }
```

练习：输出1~100之间所有数之和

```js
var sum = 0;
for (var j = 1; j <= 100; j++) {
	sum += j
}
console.log(sum);
```

##### 12.3.4.3 break和continue

示例：

```js
var sum = 0;
for (var i = 1; i<=10;i++) {
    if (i === 8) {
        // break;//跳出当前循环
        continue;//跳过这次循环，进行下一次循环
    }
    sum +=1
}
console.log(sum)
```

##### 12.3.4.4 switch

示例：**语句用于基于不同条件执行不同动作**

```js
// switch语句 case表示一个条件，满足这个条件就会输出，直到遇到break跳出，如果你的break不写，那么程序会遇到下一个break停止。这个就是‘case穿透’
var gameScore = 'good';
switch (gameScore) {
    case 'good':
    	console.log('玩的很好');
    	break;
    case 'better':
    	console.log('玩的老牛逼');
    	break;
    case 'best':
    	console.log('恭喜你，吃鸡成功');
    	break;
    default:
    	console.log('很遗憾，被淘汰了');
    	break;
}
```

示例：getDay() 方法返回 0 至 6 之间的周名数字（weekday number）

```js
// 使用周名数字来计算周的名称
switch (new Date().getDay()) {
    case 0:
        day = "星期天";
        break;
    case 1:
        day = "星期一";
         break;
    case 2:
        day = "星期二";
         break;
    case 3:
        day = "星期三";
         break;
    case 4:
        day = "星期四";
         break;
    case 5:
        day = "星期五";
         break;
    case 6:
        day = "星期六";
} 
console.log(day)
```

##### 12.3.4.5 while循环

循环三部曲：

- 初始化循环变量
- 判断循环条件
- 更新循环变量

示例：

```js
// 例子：打印 1~9之间的数
var i = 1; //初始化循环变量

while(i<=9){ //判断循环条件
    console.log(i);
    i = i+1; //更新循环条件
}
```

##### 12.3.4.6 do..while循环

示例：先做一次，再循环

```js
// 不管有没有满足while中的条件do里面的代码都会走一次,然后再循环
var i = 3;//初始化循环变量
do{
    console.log(i);
    i++;//更新循环条件

}while (i<10); //判断循环条件
```

#### 12.3.5 函数

函数：就是将一些语句进行封装，然后通过调用的形式，执行这些语句。

函数的作用：

- 解决大量的重复性的语句
- 简化编程，让编程模块化

示例：

```js
//  声明
function 做饭(isBad){//形参
    if (isBad) {
        alert('点外卖')
    }else{
        alert('做饭了')
    }
}
var bad = true;	
//调用
做饭(bad);
做饭();
```

代码解释：

- function：是一个关键字。中文是“函数”、“功能”。
- 函数名字：命名规定和变量的命名规定一样。只能是字母、数字、下划线、美元符号，不能以数字开头。
- 参数：后面有一对小括号，里面是放参数用的。
- 大括号里面，是这个函数的语句。

**返回值:**

示例：

```js
// 函数表达式
var addition = function(a,b){
return a + b;
}
function subtraction(a,b){
return a - b;
}
function multiplication(a,b){
return a * b;
}
function division(a,b){
return a / b;
}

var r1 = addition(3,2);
var r2 = subtraction(3,2);
var r3 = multiplication(3,2);
var r4 = division(3,2);

console.log(r1);
console.log(r2);
console.log(r3);
console.log(r4);
```

##### 12.3.5.1 函数作用域

示例：

```js
<script type="text/javascript">
    var a = 1;//全局作用域
	console.log(a);
	function add(){
    	var b=3;//局部作用域
    	console.log(a);
	}	
	add();
</script>
```

##### 12.3.5.2 全局污染

示例：

```js
<script type="text/javascript" src="js_code/first.js"></script>
<script type="text/javascript" src="js_code/second.js"></script>
<script type="text/javascript">
    first();
second();
</script>
```

**first.js**

示例：

```js
(function(){
	var name = 'aaa';
	var hello = function(){
		alert('hello'+name);
	}
	window.first = hello;
})()
```

**second.js**

示例：

```js
(function(){
	var name = 'bbb';
	var hello = function(){
		alert('hello'+name);
	}
	window.second = hello;
})()
```

##### 12.3.5.3 对象object

示例：

```js
var person={
    name:'ike',
    age:18,
    sex:'male',
    fav:function(a){
        alert('睡觉');
        return '舒服'+a
    }
}
console.log(person);
console.log(person.name)
console.log(person.fav(88))
```

#### 12.3.6 常用内置函数

##### 12.3.6.1 数组的操作方法

示例：升序

```js
var values = [1,15,16,18,2,3]
function compare(a,b){
    // if (a < b) {
    // 	return -1;
    // }else if (a > b){
    // 	return 1;
    // }else{
    // 	return 0;
    // }
    return a - b;  //简写
}
values.sort(compare);//升序
console.log(values);
```

示例：降序

```js
var values = [1,15,16,18,2.3]
function compare1(a,b){
    // if (a < b) {
    // 	return 1;
    // }else if (a > b){
    // 	return -1;
    // }else{
    // 	return 0;
    // }

    return b - a;//简写
}
values.sort(compare1);//降序
console.log(values);
```

示例：concat()数组合并

```js
// 1.concat()数组合并
var colors = ['red','blue']
var newColors = colors.concat('green');
newColors = newColors.concat({name:'ike'});
console.log(newColors);

var newcolors = colors.concat({name:'yellow'},['black','pink'])
console.log(newcolors);
```

示例：slice()返回数组的一段记录，顾头不顾尾

```js
// 2.slice()切片
newcolors = newcolors.slice(1,4);
console.log(newcolors)
```

示例：splice()

```js
// 3.splice() 删除、插入、替换
var names = ['张三','李四','王五','赵柳'];
// 删除前两个数，从0开始，顾头不顾尾：删除前两个数
names.splice(1,2);
console.log(names);
// 插入:在一个不删任何元素下，进行插入
// names.splice(1,0,'aaa','bbb');
// console.log(names)
// 替换：替换李四
names.splice(1,1,'你哈o');
console.log(names)
```

示例：pop()移除数组的最后一个元素

```js
var arr = ['张三','李四','王文','赵六'];
arr.pop();
console.log(arr);//["张三", "李四"，"王文"]
```

示例：push() 向数组最后添加一个元素

```js
var arr = ['张三','李四','王文','赵六'];
arr.push('小马哥');
console.log(arr);//["张三", "李四"，"王文"，"赵六"，"小马哥"]
```

示例：shift()移除数组的第一个元素

```js
var arr = ['张三','李四','王文','赵六'];
var first = arr.shift()
console.log(arr)
```

示例：unshift()向数组第一个元素前添加

```js
var arr = ['张三','李四','王文','赵六'];
var first = arr.unshift()
console.log(arr)
```

示例：indexOf lastIndexOf查找索引

```js
// 位置查询：indexOf正序  lastIndexOf倒序
var names = ['张三','mjj','王五','mjj','赵丽'];
alert(names.indexOf('mjj'));//1
alert(names.lastIndexOf('mjj'));//3
alert(names.indexOf('mjj',2));//3
alert(names.lastIndexOf('mjj',2));//1
alert(names.lastIndexOf('mjjsss',2));//-1
```

示例：reverse() 翻转数组

```js
var names = ['alex','xiaoma','tanhuang','angle'];
//4.反转数组
names.reverse();
console.log(names);
```

示例：join() 将数组中元素使用指定的字符串连接起来，它会形成一个新的字符串

```js
var score = [98,78,76,100,0];
var str = score.join('|');
console.log(str);//"98|78|76|100|0"
```

示例：sort对数组排序

```js
var names = ['alex','xiaoma','tanhuang','abngel'];
names.sort();
console.log(names)；// ["alex", "angle", "tanhuang", "xiaoma"]
```

示例：判断是否为数组：isArray()

```js
 布尔类型值 = Array.isArray(被检测的值) ;
```

示例：filter()

```js
var number = [1,2,3,6,5,4,19,4,20];
var filterresult = number.filter(function(item,index,array){
    console.log('item:'+item);
    console.log('index:'+index);
    console.log('array'+array);
})
```

**返回由原数组中每个元素的平方组成的新数组：**

示例：map()

```js
var number = [1,2,3,6,5,4,19,4,20];
var mapresult = number.map(function(item,index,array){
    return item*2;
})
console.log(mapresult);
```

示例：map练习

```js
var oldArray=[
    {
        name:'aaa',
        age:17
    },
    {
        name:'bbb',
        age:18
    },
    {
        name:'ccc',
        age:27
    }
];
// 方式一：
// var newName=[];
// var newAge=[];
// for (var i=0;i<oldArray.length;i++) {
// 	var myname = oldArray[i].name;
// 	var myage = oldArray[i].age;
// 	newName.push(myname);
// 	newAge.push(myage);
// }
// console.log(newName);
// console.log(newAge)

// 方式二：
var newName = oldArray.map(function(item,index){
    return item.name
})

var newAge = oldArray.map(function(item,index){
    return item.age
})

console.log(newName);
console.log(newAge)
```

示例：for循环遍历

```js
var number = [1,2,3,6,5,4,19,4,20];
for (var i = 0; i < number.length; i++) {
    console.log(number[i]);
}
```

**forEach方法中的function回调有三个参数：**

* 第一个参数是遍历的数组内容
* 第二个参数是对应的数组索引
* 第三个参数是数组本身

示例：forEach循环遍历

```js
var number = [1,2,3,6,5,4,19,4,20];
number.forEach(function(item,index,array){
    console.log(item)
})
```

**forEach和map的区别：**

共同：forEach() 和 map() 里面每一次执行匿名函数都支持3个参数：前项item,索引index,原始数组arr

```js
var list = ['a', 'b', 'd', 'c', 'e'];

var num1 = list.forEach(function (value, index, array) {
    return value;
});

var num2 = list.map(function (value, index, array) {
    return value;
});

console.log(num1);  // undefined
console.log(num2);  // ["a", "b", "d", "c", "e"]
```

总结：

1. forEach()返回值是undefined
2. map()返回一个新数组，原数组不会改变

区别：

1. forEach()方法不会返回执行结果，而是undefined，forEach()会修改原来的数组。
2. map()方法会得到一个新的数组并返回，且他们两个执行速度：forEach() < map()。

使用场景：

1. foreach() 适合并不打算改变数据的时候使用，如：存入数据库，打印，深copy；
2. map() 改变数据值的时候。因为它更快，且返回一个新的数组； 

##### 12.3.6.2 Date日期对象

示例：

```js
// UTC 1970.1.1 到 285616年
// Date日期对象
var now = new Date();
console.log(now)
// 指定参数
var xmas = new Date('December 25,1995 13:00:30');
console.log(xmas)
var xmas = new Date(1995,11,25);
console.log(xmas)
var xmas = new Date(1995,11,25,14,25,0);
console.log(xmas)
```

示例：获取时间

```js
var now = new Date();
// 常用方法
console.log(now.getDate());// 获取月份的第几天
console.log(now.getMonth());// 获取当前月份要加1
console.log(now.getFullYear());// 获取年
console.log(now.getDay());// 获取天 0代表周日
console.log(now.getHours());// 获取小时
console.log(now.getMinutes());// 获取分钟
console.log(now.getSeconds());// 获取小时
```

示例：日期格式化

```js
var now = new Date();
console.log(now.toDateString());// 星期 月 日 年
console.log(now.toTimeString());//时 分 秒 时区
// 常用方法
console.log(now.toLocaleDateString());//2019/8/16
console.log(now.toLocaleTimeString());//上午9:51:29
console.log(now.toLocaleString());//2019/8/16 上午9:53:37
console.log(now.toUTCString());//Fri, 16 Aug 2019 01:52:34 GMT
```

示例：数字时钟格式的时间

```js
function nowNumTime(){
    var now = new Date();
    var hour = now.getHours();
    var minute = now.getMinutes();
    var second = now.getSeconds();

    var temp = '' + (hour > 12 ? hour - 12 : hour);
    if (hour === 0) {
        temp = '12';
    }
    temp = temp+(minute < 10 ? ':0':":")+ minute;
    temp = temp+(second < 10 ? ':0':":")+ second;
    temp = temp+(hour >= 12? ' P.M':" A.M");
    console.log(temp);
    return temp;
}
var nownum = nowNumTime();
console.log(nownum)
```

##### 12.3.6.3 Math对象

**对象属性：**

| 属性    | 描述                                              |
| :------ | :------------------------------------------------ |
| E       | 返回算术常量 e，即自然对数的底数（约等于2.718）。 |
| LN2     | 返回 2 的自然对数（约等于0.693）。                |
| LN10    | 返回 10 的自然对数（约等于2.302）。               |
| LOG2E   | 返回以 2 为底的 e 的对数（约等于 1.414）。        |
| LOG10E  | 返回以 10 为底的 e 的对数（约等于0.434）。        |
| PI      | 返回圆周率（约等于3.14159）。                     |
| SQRT1_2 | 返回返回 2 的平方根的倒数（约等于 0.707）。       |
| SQRT2   | 返回 2 的平方根（约等于 1.414）。                 |

**对象方法：**

| 方法       | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| abs(x)     | 返回数的绝对值。                                             |
| acos(x)    | 返回数的反余弦值。                                           |
| asin(x)    | 返回数的反正弦值。                                           |
| atan(x)    | 以介于 -PI/2 与 PI/2 弧度之间的数值来返回 x 的反正切值。     |
| atan2(y,x) | 返回从 x 轴到点 (x,y) 的角度（介于 -PI/2 与 PI/2 弧度之间）。 |
| ceil(x)    | 对数进行上舍入。                                             |
| cos(x)     | 返回数的余弦。                                               |
| exp(x)     | 返回 e 的指数。                                              |
| floor(x)   | 对数进行下舍入。                                             |
| log(x)     | 返回数的自然对数（底为e）。                                  |
| max(x,y)   | 返回 x 和 y 中的最高值。                                     |
| min(x,y)   | 返回 x 和 y 中的最低值。                                     |
| pow(x,y)   | 返回 x 的 y 次幂。                                           |
| random()   | 返回 0 ~ 1 之间的随机数。                                    |
| round(x)   | 把数四舍五入为最接近的整数。                                 |
| sin(x)     | 返回数的正弦。                                               |
| sqrt(x)    | 返回数的平方根。                                             |
| tan(x)     | 返回角的正切。                                               |
| toSource() | 返回该对象的源代码。                                         |
| valueOf()  | 返回 Math 对象的原始值。                                     |

示例：

```js
console.log(Math.E);// 2.718281828459045
console.log(Math.LN10);// 2.302585092994046
console.log(Math.LN2);// 0.6931471805599453
console.log(Math.PI);// 3.141592653589793
console.log(Math.SQRT2);// 1.4142135623730951
```

示例：max()、min()方法

```js
var arr = [1,2,3,6,52,41,89];
var max = Math.max.apply(null,arr);
var min = Math.min.apply(null,arr);
console.log(max);
console.log(min);
```

示例：关于小数位数的问题

```js
var num = 24.3;
console.log(Math.ceil(num));// 天花板函数，只要有余数进1
console.log(Math.floor(num));// 地板函数，只要有余数都省略
console.log(Math.round(num));// 标准的四舍五入函数
```

示例：随机数

```js
// 随机数 random()    0 <= random <1
console.log(Math.random());
```

练习：获取min到max之间的整数(1-100)

```js
// 1.获取min到max之间的整数(1-100)
function rand(max){
    return Math.floor(Math.random()* max);
}
var val = rand(100);
console.log(val);
```

练习：

```js
// 1.获取min到max之间的整数(1-100)
function rand(max,min){
    return Math.floor(Math.random()*(max-min)+min);
}
// 2.获取随机颜色 rgb(0~255,0~255,0~255)
function randomColor(){
    var r = rand(0,256),g = rand(0,256),b = rand(0,256);
    // 模板字符串  Tab键上边的按钮
    var result = `rgb(${r},${g},${b})`;
    return result;
}
var rc = randomColor();
console.log(rc);
document.body.style.backgroundColor = rc;
// 3.随机验证码 四位 数字+字母(大写)
function creatCode(){
    // 设置默认的空的字符串
    var code = '';
    var codeLength = 4;
    var randomCode = [0,1,2,3,4,5,6,7,8,9,'A','V','G','H','J','I','K','O','L','P']
    for (var i = 0; i < codeLength; i++) {
        // 设置随机范围0~20
        var index = rand(0,20);
        code += randomCode[index];
    }
    return code;
}
var rancode = creatCode();
console.log(rancode);
document.write(`<h1>${rancode}</h1>`);
```

##### 12.3.6.4 字符串的操作方法

示例：chartAt() 返回指定索引的位置的字符

```javascript
var str = 'hello world';
console.log(str.charAt(1));//获取指定的字符
```

示例：concat 返回字符串值，表示两个或多个字符串的拼接

```javascript
console.log(str.concat('你好','ike'));//拼接字符串
```

示例：replace(a,b) 将字符串a替换成字符串b

```javascript
var a = '1234567755';
var newStr = a.replace("4567","****");
console.log(newStr);//123****755
```

示例：indexof() lastIndexOf() 查找字符的下标，如果找到返回字符串的下标，找不到则返回-1

```javascript
var str = 'hello world';
console.log(str.indexOf('o'));//4
console.log(str.lastIndexOf('o'));//7
console.log(str.indexOf('o',6));//7
console.log(str.lastIndexOf('o',6));//4
```

示例：切片

```js
var str = 'hello world';
console.log(str.substring(2))
console.log(str.slice(2));
// 第一个参数是起始的
// 位置，第二个参数是结束的位置，顾头不顾尾
console.log(str.slice(2,4));
console.log(str.substring(2,6))
```

示例：split('a',1) 以字符串a分割字符串，并返回新的数组。如果第二个参数没写，表示返回整个数组，如果定义了个数，则返回数组的最大长度

```javascript
var  str =  '我的天呢,a是嘛,你在说什么呢?a哈哈哈';
console.log(str.split('a'));//["我的天呢,", "是嘛,你在说什么呢?", "哈哈哈"]
```

示例：substr(statr,end) 左闭右闭

```javascript
var str = 'hello world';
console.log(str.substr(2));
// 第二个参数是返回的字符数
console.log(str.substr(2,4));
```

示例：toLowerCase()转小写

```javascript
var str1 = 'HELLO WORLD';
console.log(str1.toLowerCase());
```

示例：toUpperCase()转大写

```javascript
var str = 'hEllo world';
console.log(str.toUpperCase());
```

示例：length获取字符串长度，拼接字符串

```js
str = 'hEllo world';
console.log(str.length);//获取字符串的长度
```

示例：trim()清空左右两边的空格

```js
var str = '     hello world   ';
console.log(str);
console.log(str.trim());//清楚前后空格
```

示例：字符串练习

```js
//查找当前字符e在字符串中的所有位置
var str = 'He unfolded the map and set it on the floor.';
var arr = [];
var pos = str.indexOf('e');
console.log(pos);
while(pos > -1){
    // 找到当前e字符对应的位置
    arr.push(pos);
    pos = str.indexOf('e', pos+1)
}
console.log(arr)
```

特别：

```javascript
//1.将number类型转换成字符串类型
var num = 132.32522;
var numStr = num.toString()
console.log(typeof numStr)
//四舍五入 保留小数位数
var newNum = num.toFixed(2)
console.log(newNum)
```

#### 12.3.7 globle对象的编码和解码

示例：编码

```js
// URI 通用资源标识符
var uri = 'http://www.baidu.cn/web index.html?name=ike';
// encodeURI只能识别空格，其他特殊字符不能识别
console.log(encodeURI(uri))
// encodeURIComponent编码使用最多的方法
console.log(encodeURIComponent(uri));
```

示例：解码

```js
var uri1 = 'http%3A%2F%2Fwww.baidu.cn%2Fweb%20index.html%3Fname%3Dike';
// 只能解析空格
console.log(decodeURI(uri1));// http%3A%2F%2Fwww.baidu.cn%2Fweb index.html%3Fname%3Dike
// 特殊符号都能解析
console.log(decodeURIComponent(uri1));// http://www.baidu.cn/web index.html?name=
```

#### 12.3.8 window对象

示例：

```js
// window对象相对于globle对象，全局的数据类型都挂载到window
var a = 3;
console.log(window.a);
function hello(){
    alert(window.a);
}
window.hello();
```

#### 12.3.9 BOM简介

Browser Object Model ，简称（BOM）浏览器内核主要指的是浏览器的渲染引擎，2013 年以前，代表有 Trident（IE），Gecko（firefox），Webkit（Safari chrome 等）以及 Presto（opera)。2013 年，谷歌开始研发 blink 引擎，chrome 28 以后开始使用，而 opera 则放弃了自主研发的 Presto 引擎，投入谷歌怀抱，和谷歌一起研发 blink 引擎，国内各种 chrome系的浏览器（360、UC、QQ、2345 等等）也纷纷放弃 webkit，投入 blink 的怀抱。

移动端的浏览器内核主要说的是系统内置浏览器的内核。

目前移动设备浏览器上常用的内核有 Webkit，Blink，Trident，Gecko 等，其中 iPhone 和 iPad 等苹果 iOS 平台主要是 WebKit，Android 4.4 之前的 Android 系统浏览器内核是 WebKit，Android4.4 系统浏览器切换到了Chromium，内核是 Webkit 的分支 Blink，Windows Phone 8 系统浏览器内核是 Trident。

BOM骨架图:

![1643078868914](J:\homework\Python学习笔记\Python_notes.assets\1643078868914.png)

- **window对象是BOM的顶层(核心)对象**，所有对象都是通过它延伸出来的，也可以称为window的子对象。
- document 对象，文档对象；
- location 对象，浏览器当前URL信息；
- navigator 对象，浏览器本身信息；
- screen 对象，客户端屏幕信息；
- history 对象，浏览器访问历史信息；
- DOM是BOM的一部分。

**window对象**

- window对象是JavaScript中的顶级对象
- 全局变量、自定义函数也是window对象的属性和方法
- window对象下的属性和方法调用时，可以省略window
- alert('提示信息')
- confirm("确认信息")
- prompt("弹出输入框")
- open("url地址"，“打开的方式（可以是-self或-black）”，“新窗口的大小”）

* close()  关闭当前的网页
* window.moveTo() - 移动当前窗口
* window.resizeTo() - 调整当前窗口的尺寸
* setTimeout(函数，时间) 只执行一次
* setInterval(函数，时间) 无限执行
* clearTimeout/clearInterval(定时器名称) 清除定时器

注：如果url为空，则默认打开一个空白页面，如果打开方式为空，则默认为新窗口方式打开页面。返回值为：返回新打开窗口的window对象

注：存在兼容性问题：

1. FF：禁止设置关闭浏览器的代码
2. Chrome：默认直接关闭
3.  IE：询问用户

**弹出系统对话框：**

```js
// 方式一
window.alert('Mjj');
// 方式二
var a = window.confirm('你确定要离开网站吗？')
console.log(a);
// 方式三
var b = window.prompt('请输入你早晨吃了什么？');
console.log(b);
```

**打开窗口、关闭窗口：**

```js
window.open('https://www.baidu.com/');
```

示例：

```js
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>

        <!--行间的js中的open() window不能省略-->
        <button onclick="window.open('https://www.baidu.com/')">百度一下</button>

        <button>打开百度</button>
        <button onclick="window.close()">关闭</button>
        <button>关闭</button>

    </body>
    <script type="text/javascript">

        var oBtn = document.getElementsByTagName('button')[1];
        var closeBtn = document.getElementsByTagName('button')[3];

        oBtn.onclick = function(){

            //打开空白页面
            open('https://www.baidu.com',"_self")
        }
        closeBtn.onclick = function(){
            if(confirm("是否关闭？")){
                close();
            }
        }
    </script>
</html>
```

**location对象：**

location相当于浏览器地址栏，可以将url解析成独立的片段，用于获得当前页面的地址 (URL)，并把浏览器重定向到新的页面。在编写时可不使用 window 这个前缀。

**location对象的属性：**

- href：跳转
- hash：返回url中#后面的内容，包含#
- host：主机名，包括端口
- hostname：主机名
- pathname：url中的路径部分
- protocol：协议 一般是http、https
- search：查询字符串

示例：

```js
<!DOCTYPE html>
<html>
<head>
	<title>location对象</title>
</head>
<body>
	<form>
		<span>luffy</span>
	</form>
	<script type="text/javascript">
    var oSpan = document.getElementsByTagName("span")[0];
	oSpan.onclick = function () {
        location.href = "http://www.luffycity.com";   //点击span时，跳转到指定链接
    }
	</script>
</body>
</html>
```

**location对象**

示例：

```js
// 1. 2秒之后跳转到百度首页
setTimeout(function(){
    setTimeout(function(){
        // location.href = 'https://www.baidu.com';
        location.replace('https://www.baidu.com');
        location.reload();
    },2000)
})
```

**navigator对象**

window.navigator 的一些属性可以获取客户端的一些信息，对象包含有关访问者浏览器的信息。在编写时可不使用 window 这个前缀。

- userAgent：浏览器设定的User-Agent字符串

- platform：浏览器支持的系统，win/mac/linux

- appName：浏览器名称

- appVersion：浏览器版本

- language：浏览器设置的语言

- userAgent是最常用的属性，用来完成浏览器判断

    ```js
    if(window.navigator.userAgent.indexOf('MSIE')!=-1){
            alert('我是IE');
        }else{
            alert('我不是IE');
        }
    ```

- ```js
  console.log(navigator.userAgent);
    console.log(navigator.platform);
  ```

**screen对象**

window.screen 对象包含有关用户屏幕的信息。

screen.availWidth 属性返回访问者屏幕的宽度，以像素计，减去界面特性，比如窗口任务栏。                                         

screen.availHeight 属性返回访问者屏幕的高度，以像素计，减去界面特性，比如窗口任务栏。

```js
document.write(screen.availHeight+screen.availWidth);//获取屏幕的宽度和高度之和
```

**history对象**

1、后退：

- history.back()：加载历史列表中的前一个 URL。返回上一页。
- history.go(-1)： go(“参数”) -1表示上一页，1表示下一页。

2、前进：

- history.forward()：加载历史列表中的下一个 URL。返回下一页。

- history.go(1)

  ```js
  1、window.location.href = '你所要跳转到的页面';
  2、window.open('你所要跳转到的页面’);
  3、window.history.back(-1):返回上一页
  4、window.history.go(-1/1):返回上一页或下一页五、
  5、history.go("baidu.com")；
  ```

用的不多。因为浏览器中已经自带了这些功能的按钮。

**窗口尺寸大小**

* 可视区尺寸：  
  * document.documentElement.clientWidth
  * document.documentElement.clientHeight

* 滚动条滚动距离： 
  * document.documentElement.clientScrollTop
  * document.documentElement.clientScrollLeft  

存在兼容性问题（Chrome与其它浏览器不同），解决办法如下：

```js
var scrollTop = document.documentElement.scrollTop||document.body.scrollTop;
var scrollLeft = document.documentElement.scrollTop||document.body.scrollLeft;
```

内容高/宽：元素，scrollHeight/scrollWidth

当一个时间发生时鼠标到页面可视区的距离：clientX/clientY

#### 12.3.10 DOM简介

**概念：**

所谓DOM,全称 Docuemnt Object Model 文档对象模型，毫无疑问，此时要操作对象，什么对象？文档对象

在文档中一切皆对象，比如html,body,div,p等等都看做对象，那么我们如何来点击某个盒子让它变色呢？

DOM 为文档提供了结构化表示，并定义了如何通过脚本来访问文档结构。目的其实就是为了能让js操作html元素而制定的一个规范。

**解析过程：**

HTML加载完毕，渲染引擎会在内存中把HTML文档，生成一个DOM树，getElementById是获取文档内DOM上的元素节点。然后操作的时候修改的是该元素的**属性**。

**DOM骨架树（一切皆是节点）**

![1643078838013](J:\homework\Python学习笔记\Python_notes.assets\1643078838013.png)

- **元素节点**：HMTL标签。
- **文本节点**：标签中的文字（比如标签之间的空格、换行）
- **属性节点**：：标签的属性

整个html文档就是一个文档节点。所有的节点都是Object。

**DOM的作用：**

- JavaScript 能改变页面中的所有 HTML 元素
- JavaScript 能改变页面中的所有 HTML 属性
- JavaScript 能改变页面中的所有 CSS 样式
- JavaScript 能删除已有的 HTML 元素和属性
- JavaScript 能添加新的 HTML 元素和属性
- JavaScript 能对页面中所有已有的 HTML 事件作出反应
- JavaScript 能在页面中创建新的 HTML 事件

获取其他DOM的三种方式：

示例：

```js
// 1.document.getElementById()
var doc = document.getElementById('class_list');
console.log(doc);
console.log(typeof doc);

// 2.docuemnt.getElementsByTagName()获取出来的是一个节点对象节点集合
var olis = document.getElementsByTagName('li');
console.log(olis);
for (var i = 0;i < olis.length;i++) {
    console.log(olis[i])
}
console.log(typeof olis);

// 3.document.getElementByClassNmae('item')
var ootem= document.getElementsByClassName('item');
console.log(ootem);
for (var i = 0;i < ootem.length;i++) {
    console.log(ootem[i])
}
```
示例：遍历对象节点集合

```js
// 1.document.getElementById()
var doc = document.getElementById('class_list');
console.log(doc);
console.log(typeof doc);

// 2.docuemnt.getElementsByTagName()获取出来的是一个节点对象节点集合
var olis = document.getElementsByTagName('li');
console.log(olis);
for (var i = 0;i < olis.length;i++) {
    console.log(olis[i])
}
console.log(typeof olis);

// 3.document.getElementByClassNmae('item')
var ootem= document.getElementsByClassName('item');
console.log(ootem);
for (var i = 0;i < ootem.length;i++) {
    console.log(ootem[i])
}
```

示例：设置属性值

```html
<!DOCTYPE html>
<html>
<head>
	<title>class_list2</title>
	<style type="text/css">
		#box{
			color: red;
		}
	</style>
</head>
<body>
    <h2>你要买什么课程</h2>
	<p title="轻选择购买的课程" id="box">本课程是web全栈课程</p>
	<ul id="class_list">
		<li class="item">javascript</li>
		<li class="item">css</li>
		<li>Dom</li>
	</ul>
	<script type="text/javascript">
		var op = document.getElementsByTagName('p')[0];
		// 设置属性值 有一个必须的参数，这个节点对象的名字
		var title = op.getAttribute('title');
		console.log(title);

		// 设置属性值：setAttribute(name,value)
		op.setAttribute('id','box');
	</script>
</body>
</html>
```

##### 12.3.10.1 节点属性

在文档对象模型中，每一个节点都是一个对象，DOM节点有三个重要的属性

1. nodeName：节点的名称
2. nodeValue：节点的值
3. nodeType：节点的类型

一.nadeName属性：节点的名称是只读

```python
1.元素节点的nodeName与标签名相同
2.属性节点的nodeName与属性的名称相同
3.文本节点的nodeName永远是  # text
4.注释节点的nodeName永远是  # comment
5.文档节点的nodeName永远是  # document
```

二.nodeValue属性：节点的值

```python
1.元素节点的nodeValue是undefinede或null
2.属性节点的nodeValue是属性的值
3.文本节点的nodeValue是文本自身
4.注释节点的nodeValue是文本自身
5.文档节点的nodeValue是null
```

三.nodeType属性：节点的类型，是只读的

```html
以下常用的集中节点类型：
元素类型		节点类型
元素            1
属性            2
文本            3
注释	          8
文档            9
```

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>节点属性</title>
</head>
<body>
	<div id="box" title="我是文档">我是一个文本节点<!-- 我是注释 --></div>
	<script type="text/javascript">
		// 1.元素节点
		var odiv = document.getElementById('box');
		// DIV|null|1
		console.log(odiv.nodeName + '|' + odiv.nodeValue + '|'+ odiv.nodeType);

		// 2.属性节点
		var attrNode = odiv.attributes[0];
		// id|box|2
		console.log(attrNode.nodeName + "|" + attrNode.nodeValue + "|" + attrNode.nodeType);

		// 3.文本节点
		var textNode = odiv.childNodes[0];
		// #text|我是一个文本节点|3
		console.log(textNode.nodeName + "|" + textNode.nodeValue + "|" + textNode.nodeType);

		// 4.注释节点
		var commentNode = odiv.childNodes[1];
		// #comment| 我是注释 |8
		console.log(commentNode.nodeName + "|" + commentNode.nodeValue + "|" + commentNode.nodeType);
		// 5.文档节点 9
		console.log(document.nodeType);
	</script>
</body>
</html>
```

节点对象常用属性：

示例：缺点--标签不能换行

```html
<div class="xiongdi1">我是上兄弟</div><div id="father"><p>iker</p><p>ikeer2</p></div><div class="xiongdi">我是兄弟</div>

<script type="text/javascript">
    var ofather = document.getElementById('father');
    console.log(ofather.childNodes);// 获得元素的集合
    console.log(ofather.childNodes[0]);// 获得集合的第一个
    console.log(ofather.firstChild);// 获得第一个元素
    console.log(ofather.lastChild);// 获得最后一个元素
    console.log(ofather.childNodes[ofather.childNodes.length-1]);// 获得最后一个元素
    console.log(ofather.parentNode);// 获得父元素

    console.log(ofather.nextSibling);// 获得后边挨着的元素
    console.log(ofather.previousSibling);//获得上一个元素
</script>
```

示例：解决标签不能换行

```html
<div class="xiongdi1">我是上兄弟</div>
	<div id="father">
		<p>iker</p>
		<p>ikeer2</p>
	</div>
	<div class="xiongdi">我是兄弟</div>
	<script type="text/javascript">
        var ofather = document.getElementById("father");
		 function get_childNodes(fatherNode){
		 	var nodes = fatherNode.childNodes;
			var arr = [];
			for (var i = 0; i < nodes.length; i++) {
				if (nodes[i].nodeType === 1) {
					arr.push(nodes[i]);
				}
			}
			return arr;
		}
		var childnodes = get_childNodes(ofather);
		console.log(childnodes);
	</script>
```

示例：获取下一个div

```html
<div class="xiongdi1">我是上兄弟</div>
	<div id="father">
		<p>iker</p>
		<p>ikeer2</p>
	</div>
	<div class="xiongdi">我是兄弟</div>
	<script type="text/javascript">
		function get_nextSibling(x) {
			var y = x.nextSibling;
			while (y && y.nodeType != 1){
				y = y.nextSibling;
			}
			return y;
		}
		console.log(get_nextSibling(ofather));
	</script>
```

##### 12.3.10.2 节点方法

```css
动态的操作节点：
1.创建节点 createElement()
2.插入节点 appendChild()	  insertBefore(newNode,node)
3.删除节点 removeChild()
4.替换节点 replaceChild(newNode,node)
5.创建文本节点 createTextNode()
```

插入节点有两种方式，它们的含义是不同的。

方式1：语法

```css
 父节点.appendChild(新的子节点);
```

解释：父节点的最后插入一个新的子节点。

方式2：语法

```
父节点.insertBefore(新的子节点,作为参考的子节点);
```

解释：

- 在参考节点前插入一个新的节点。
- 如果参考节点为null，那么他将在父节点最后插入一个子节点。

删除节点

格式如下：语法

```
父节点.removeChild(子节点);
```

解释：**用父节点删除子节点**。必须要指定是删除哪个子节点。

如果我想删除自己这个节点，可以这么做：

```
node1.parentNode.removeChild(node1);
```

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>节点方法</title>
	<style type="text/css">
		.active{
			color: red;
			font-size: 30px;
		}
	</style>
</head>
<body>
	<div id="box">
		<p id="active">ike</p>
	</div>
	<!-- 
	动态的操作节点：
	1.创建节点 createElement()
	2.插入节点 appendChild()	  insertBefore(newNode,node)
	3.删除节点 removeChild()
	4.替换节点 replaceChild(newNode,node)
	5.创建文本节点 createTextNode()
	 -->
	 <script type="text/javascript">
	 	var oDiv = document.getElementById('box');
	 	var oAtive = document.getElementById('active');

	 	var newNode = document.createElement('p');
	 	var newNode2 = document.createElement('p');
	 	var newNode3 = document.createElement('a');

	 	console.log(newNode === newNode2)


	 	newNode.setAttribute('class','active');
	 	oDiv.appendChild(newNode);
	 	// 第一个参数是新插入的节点，第二个参数是参考点
		oDiv.appendChild(newNode2, oAtive);
	 	// newNode = null; // 释放对象
	 	var textNode = document.createTextNode('alex');
	 	newNode.appendChild(textNode);

		// 仅仅设置文本内容
	 	newNode.innerHTML = '<a href="#">alex@163.com</a>';
	 	newNode2.innerHTML = '<a href="#">学前端</a>';
	 	newNode3.setAttribute('href', 'http://www.baidu.com')
	 	newNode3.innerHTML = '百度一下';
	 	// newNode.innerText = '<a href="#">alex@163.com</a>';

	 	// 删除操作
	 	// oDiv.removeChild(oAtive);

	 	// 替换操作
	 	oDiv.replaceChild(newNode3,oAtive)
	 </script>
</body>
</html>
```

##### 12.3.10.3 动态操作样式

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>动态操作样式</title>
	<style type="text/css">
		.highLight{
			background-color: blue;
			color: red;
			width: 250px;
			height: 250px;
			text-align: center;
			line-height: 250px;
		}
	</style>
</head>
<body>
	<p id="box" class="highLight">鹿鼎记</p>
	<script type="text/javascript">
		// nodeObj.style
		var op = document.getElementById('box');、
		// 直接操作样式属性
		// console.log(op.style);
		// op.style.color = 'blue';
		// op.style.backgroundColor = 'red';
		// op.style.width = '250px';
		// op.style.height = '250px';
		// op.style.textAlign = 'center';
		// op.style.lineHeight = '250px';

		// 通过控制属性的类名来控制样式
		op.setAttribute('class','highLight');
	</script>
</body>
</html>
```

##### 12.3.10.4 事件

事件三要素：

- 找到触发的事件对象
- 事件
- 事件处理程序

比如：我用手去按开关，灯亮了。

这件事情里，找到触发的事件对象是：手。事件是：按开关。事件处理程序是：灯的开和关。

总结：谁引发的后续事件，谁就是事件源。

**总结如下：**

- 事件源：引发后续事件的html标签。
- 事件：js已经定义好了
- 事件驱动程序：对样式和html的操作，也就是DOM

**代码书写步骤如下：**

- 获取事件源：`document.getElementById(“box”);`
- 绑定事件： 事件源box.事件onclick = function(){ 事件驱动程序 };
- 书写事件驱动程序：关于DOM的操作

**样式属性操作：**

所谓样式属性，就是对之前所讲解的style标签中的属性进行操作，并且通过js控制盒模型的属性（width,height等），控制盒子的显示隐藏（display:none|block）,控制盒子的颜色切换（background：red|green）等等。

操作文档对象，要遵循事件三步走：

- 获取事件源
- 事件
- 事件驱动程序

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>事件</title>
	<style type="text/css">
		#box{
			width: 100px;
			height: 100px;
			background-color: blue;
		}
	</style>
</head>
<body>
    <!--行内绑定-->
	<div id="box" onclick="add()"></div>
	<script type="text/javascript">
		var oDiv = document.getElementById('box');

		var isBlue = true;
        // 绑定事件的第一种方式
		oDiv.onclick = function(){
			// alert('事件被触发了');

			if (isBlue) {
				// this指向了当前的元素节点对象
				this.style.backgroundColor = 'red';
				isBlue = false;
			}else{
				this.style.backgroundColor = 'yellow';
				isBlue = true;
			}
		};

        //绑定事件的第二种方式
		// oDiv.onclick = add;
		// function add(){
		// 	alert('事件被触发了');
		// }
		
		// 一般使用这种方式（推荐使用这种）
		// var add = function(){
		// 	alert('事件被触发了');
		// }
	</script>
</body>
</html>
```

**鼠标事件：**

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>onmouseover()和onmouseout()事件</title>
	<style type="text/css">
		#box{
			width: 200px;
			height: 200px;
			background-color: red;
		}
	</style>
</head>
<body>
	<div id="box"></div>
	<script type="text/javascript">
		// 1.找开关	2.按一下	3.灯亮了

		// 1.找到触发的事件对象	2.事件	3.事件处理程序
        // 1.获取事件源
		var oDiv = document.getElementById('box');
		// 2.鼠标滑过事件
        // 2.绑定事件(悬停事件：鼠标进入到事件源中立即出发事件)
		oDiv.onmouseover = function(){
            // 3.书写事件驱动程序(修改src)
			this.style.backgroundColor = 'green';
		}
		// 3.鼠标移开事件
        // 2.绑定事件(悬停事件：鼠标进入到事件源中立即出发事件)
		oDiv.onmouseout = function(){
            // 3.书写事件驱动程序(修改src)
			this.style.backgroundColor = 'blue';
		}
	</script>
</body>
</html>
```

**表单控件上的事件：**

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>表单控件上的事件</title>
	<style type="text/css">
		.text{
			color: red;
			font-size: 10px;
		}
	</style>
</head>
<body>
	<form action="">
		<p class="name">
			<label for="username">用户名：</label>
			<input type="text" name="user" id="username">
			<span></span>
		</p>
		<p class="pwd">
			<label for="pwd">密码：</label>
			<input type="password" name="pwd" id="pwd">
		</p>
		<input type="submit" name="">
	</form>

	<script type="text/javascript">
        // 1.获取事件源(事件对象，在文档中一切的标签都是对象)
		var userName = document.getElementById('username');
        // 创建一个span标签
		var newNode = document.createElement('span');
        // 2.事件
		userName.onfocus = function(){
			console.log('请输入用户名');
             // 3.事件驱动程序  
			newNode.innerHTML = '请输入用户名';
            // 给span标签设置元素
			newNode.setAttribute('class','text');
			userName.parentNode.appendChild(newNode);
		}
		userName.onblur = function(){
			console.log('请输入正确的用户名');
			newNode.innerHTML = '请输入正确的用户名';
			newNode.setAttribute('class','text');
			userName.parentNode.appendChild(newNode);
		}
	</script>
</body>
</html>
```

**内容选中事件和改变事件：**

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>内容选中事件和内容改变事件</title>
</head>
<body>
	<textarea cols="30" rows="10">阿拉基分散发</textarea>
	<input type="text" name="" value="修改这里">
	<script type="text/javascript">
		var textArea = document.getElementsByTagName('textarea')[0];
		var inputObj = document.getElementsByTagName('input')[0];

		textArea.onselect = function(){
			console.log('内容被选中！');
		}
		inputObj.onchange = function(){
			console.log('内容被改变了！')
		}
		inputObj.oninput = function(){
			console.log('内容实时被改变了！');
			console.log(this.value);
		}

	</script>
</body>
</html>
```

**窗口事件：**

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>窗口加载事件</title>
	<script type="text/javascript">
		/*
	setTimeout(function(){
		var oDiv = document.getElementById('box');
		oDiv.onclick = function(){
		this.innerHTML = ('alex');
	}
},0)
*/
	// 等待文档元素加载完成之后才会调用onload()
	window.onload = function(){
		var oDiv = document.getElementById('box');
		oDiv.onclick = function(){
			this.innerHTML = 'alex';
		}
	}
	</script>
</head>
<body>
	<div id="box">夹杂史蒂夫</div>
</body>
</html>
```

### 12.4 jQuery

#### 12.4.1 jQuery介绍

jQuery是一个快速，小巧，功能丰富的JavaScript库。它通过易于使用的API在大量浏览器中运行，使得HTML文档遍历和操作，事件处理，动画和Ajax更加简单。通过多功能性和可扩展性的结合，jQuery改变了数百万人编写JavaScript的方式。另外它只是封装了js的dom的操作和ajax，其它的未封装。所以js是包含jquery的。由此可见，jquery的出现，使我们更加容易操作DOM。

**核心思想：write less,do more 写的少 做的多**

##### 12.4.1.1 jQuery的作用

用js写代码的时候，会遇到一些问题：

- window.onload事件有事件覆盖的问题，因此只能写一个事件
- 代码容错性差
- 浏览器兼容性问题
- 书写复杂，代码量多，看上去比较乱
- 动画效果实现复杂

jQuery完美的解决了以上问题。学习jQuery就是学习怎么用jQuety操作DOM，学习jQuery封装好的功能接口。

##### 12.4.1.2 jQuery的特点

- 链式编程：调用方法时可以连起来写，比如`.show()`和`.html()`可以连写成`.show().html()`。
- 隐式迭代：隐式对应的是显式。隐式迭代的意思是：在方法的内部进行循环遍历，而不用我们自己再进行循环，简化我们的操作，方便我们调用。

**jQuery符号：**

- jQuery 使用 `$` 符号原因：书写简洁、相对于其他字符与众不同、容易被记住
- `$` 代表的就是jQuery

示例：

```javascript
  <script src="jquery-3.3.1.js"></script>
    <script>
        console.log($);
        console.log(jQuery);
        console.log($===jQuery);// True
    </script>
```

**jQuery参数：**

- jQuery 里面的 `$` 函数，根据传入参数的不同，进行不同的调用，实现不同的功能。返回的是jQuery对象。
- jQuery这个js库，除了`$` 之外，还提供了另外一个函数：jQuery。jQuery函数跟 `$` 函数的关系：`jQuery === $`。

示例：

```js
$(); // 调用上面我们自定义的函数$

$(document）.ready(function(){}); // 调用入口函数

$(function(){}); // 调用入口函数，简单写法

$("#btn") // 获取id属性为btnShow的元素

$("div") // 获取所有的div标签元素
```

**jQuery的第一个demo**

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        div{
            width: 100px;
            height: 100px;
            background-color: green;
            margin-top: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <button>操作</button>
    <div></div>
    <div></div>
    <div></div>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            // 获取dom元素
            var oBtn = $('button'); // 根据标签名获取元素
            var oDiv = $('div'); // 根据标签名获取元素
            oBtn.click(function(){
                oDiv.show(3000);// 显示盒子
                oDiv.html('赵云'); // 设置内容
            });// 事件是通过方法绑定的
        })
    </script>
</body>
</html>
```

##### 12.4.1.3 入口函数对比

**jQuery入口函数与js入口函数的区别**：

区别一：书写个数不同：

- Js 的入口函数只能出现一次，出现多次会存在事件覆盖的问题。
- jQuery 的入口函数，可以出现任意多次，并不存在事件覆盖问题。

区别二：执行时机不同：

- Js的入口函数是在所有的文件资源加载完成后，才执行。
    - 这些文件资源包括：页面文档、外部的js文件、外部的css文件、图片等。
- jQuery的入口函数，是在文档加载完成后，就执行。
    - 文档加载完成指的是：DOM树加载完成后，就可以操作DOM了，不用等到所有的外部资源都加载完成。

**文档加载的顺序：从上往下，边解析边执行。**

示例：js入口函数

```js
// 原生js的入口函数。页面上所有内容(文本，图片)加载完毕，才执行。
window.onload = function () {
    alert(1);
}
```

示例：jQuery入口函数

方式一：

```js
// 等待文档资源加载完成之后调用此方法
$(document).ready(function(){
    alert(1);
});
```

方式二：

```js
// 2.jquery简便写法入口函数
$(function(){
    alert(2);
});
```

方式三：

```js
$(window).ready(function(){
    // 表示文档，图片资源加载完成之后调用
    console.log(3);
});
$(window).ready(function(){
    // 表示文档，图片资源加载完成之后调用，而且不会覆盖
    console.log(4);
});
```

##### 12.4.1.4  DOM对象和jQuery对象对比

通过 jQuery 获取的元素是一个**伪数组**，数组中包含着原生JS中的DOM对象

**区别：**

- 通过原生 js 获取这些元素节点的方式

示例：

```js
var myBox = document.getElementById("app");           //通过 id 获取单个元素
var boxArr = document.getElementsByClassName("box");  //通过 class 获取的是伪数组
var divArr = document.getElementsByTagName("div");    //通过标签获取的是伪数组
```

- 通过 jQuery 获取这些元素节点的方式

示例：

```js
//获取的是伪数组，里面包含着原生 JS 中的DOM对象
console.log($('#app'));// 通过 id 获取单个元素
console.log($('.box'));// 通过 class 获取的是伪数组
console.log($('div'));// 通过标签获取的是伪数组
```

**相互转换：**

- jQuery对象转为js DOM对象：

示例：

```js
$(function(){
    // 获取jquery对象
    console.log($('#box2'));

    // 获取js对象
    var oDiv2 = document.getElementById('box2');
    console.log(oDiv2);

    // jquery==>js对象
    console.log($('#box2')[0]);// 推荐使用这种
    console.log($('#box2').get(0));
});
```

- js DOM 对象 转为jQuery对象：

示例：

```js
$(function(){
    // 获取jquery对象
    console.log($('#box2'));

    // 获取js对象
    var oDiv2 = document.getElementById('box2');
    console.log(oDiv2);

    // js对象==>jquery对象 $(js对象)
    console.log($(oDiv2));
});
```

总结：

- 如果是jquery对象一定要调用jquery的属性和方法
- 如果是js对象一定要调用的是js的属性和方法

示例：

```js
// 入口函数
$(function(){
    // 事件三步走： 事件源  事件  事件驱动程序
    // jquery如何获取dom   
    // jquery的标签选择器
    console.log($('div'));
    // js对象
    // $('div')[0].onclick
    // jquery内部自己遍历 
    $('div').click(function(){
        // alert(1);
        // this指的是js对象
        console.log(this.innerText);
        console.log($(this).text())
        // $(this).hide(300);
    });
    // 2.类选择器
    console.log($('.box'))
    // 3.id选择器
    console.log($('#box'))
});
</script>
```

#### 12.4.2 jQuery选择器

##### 12.4.2.1 基本选择器

- id选择器
    - 选择id为指定值的第一个元素
- 类选择器
    - 选择指定类名的所有元素
- 标签选择器
    - 选择指定标签名的所有元素

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        div{
            width: 100px;
            height: 100px;
            background-color: green;
            margin-top: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <button id="btn">操作</button>
    <div></div>
    <div></div>
    <div class="content"></div>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            // 获取dom元素
            var oBtn = $('#btn'); // 根据标id获取元素
            var oDiv = $('div'); // 根据标签名获取元素
            var oCls = $('.content');// 根据类名获取元素
            oBtn.click(function(){
                oDiv.show(3000);// 显示盒子
                oDiv.html('赵云'); // 设置内容
                oCls.html('马云');
            });
        })
    </script>
</body>
</html>
```

##### 12.4.2.2 层级选择器

- 后代选择器
    - 选择指定元素的后代元素
    - 符号为：空格
- 子代选择器
    - 选择指定元素的直接子元素
    - 符号为：>
- 紧邻选择器
    - 选择紧挨着的下一个元素
    - 符号为：+
- 兄弟选择器
    - 选择后面所有的兄弟元素
    - 符号为：~

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<ul class="lists">
		<li>
			方圆
			<ol>
			    <li>童文杰</li>
			</ol>
		</li>
		<li class="item">
			<a href="#">乔卫东</a>
		</li>
		<li class="item2">宋倩</li>
		<li>方一凡</li>
		<li>林磊儿</li>
		<li>乔英子</li>
	</ul>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 后代选择器  修改样式属性
			$('.lists li').css('color','green');
			// 子代选择器 所有指定儿子级别的元素
			$('.item > a').css({
				'color':'yellow',
				'background-color':'red'
			});
			// 紧邻选择器  只选中挨着最近的兄弟
			$('.item + li').css('color','pink');

			// 兄弟选择器  类名后的所有兄弟
			$('.item2~li').css('color','blue');
		});
	</script>
</body>
</html>
```

##### 12.4.2.3 基本过滤器

- :eq(index);
    - 选择索引index的元素
- :gt(index);
    - 选择索引大于index的元素
- :lt(index);
    - 选择索引小于index的元素
- odd
    - 选择索引为奇数的元素
- even
    - 选择索引为偶数的元素
- first
    - 选择第一个匹配的元素
- last
    - 选择最后一个匹配的元素

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<ul>
	    <li>1</li>
	    <li>2</li>
	    <li>3</li>
	    <li>4</li>
	</ul>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 1.:eq(index) 选择索引为index的元素
			$('ul li:eq(0)').css('background','red');
			// 2.:gt(index) 选择索引大于index的元素
			$('ul li:gt(0)').css('color','green');
			// 3.:lt(index) 选择索引小于index的元素
			$('ul li:lt(3)').css('color','yellow');
			// 4.odd 选择索引为奇数的元素
			$('ul li:odd').css('background','black');
			// 5.even 选择索引为偶数的元素
			$('ul li:even').css('background','green');
			// 6.first 选取第一个元素
			$('ul li:first').css('background','red');
			// 7.last 选择最后一个元素
			$('ul li:last').css('background','red');
		});
	</script>
</body>
</html>
```

##### 12.4.2.4 属性选择器

- $('li[id]')
    - 选择id标签包含id属性的元素
- $('li[class=what]')
    - 选择li标签class属性值为what的元素
- $('li[class!=what]')
    - 选择li标签class属性值不为what的元素
- $('input[name^=user]')
    - 选择input标签name属性值为user开头的元素
- $('input[name$=222]')
    - 选择input标签name属性值为222结尾的元素
- $('button[class*=btn]')
    - 选择button标签class属性值包含btn的元素
- `$('input[name][name=lastname]')`
    - 选择input标签name属性并且属性值为lastname的元素

示例：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
         <div id="box">
            <h2 class="title">属性元素器</h2>
            <!--<p class="p1">我是一个段落</p>-->
            <ul>
                <li id="li1">第一个li标签</li>
                <li class="what" id="li2">第二个li标签</li>
                <li class="what">第三个li标签</li>
                <li class="heihei">第四个li标签</li>
            </ul>
            <form action="" method="post">
            	<span>
            		<input name="username" type='text' value="1" checked="checked" />
            	</span>
                
                <span>
                	<input name="username1111" type='text' value="2" />
                </span>
                <input name="username2222" type='text' value="3" />
                <input name="username3333" type='text' value="4" />
                <button class="btn-default">按钮1</button>
                <button class="btn-info">按钮2</button>
                <button class="btn-success">按钮3</button>
                <button class="btn-danger">按钮4</button>
                <input type="text" name="lastname">
            </form>
        </div>
    </body>
    <script src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(function(){
            //标签名[属性名] 查找所有含有id属性的该标签名的元素
            $('li[id]').css('color','red');
            //匹配给定的属性是what值得元素
            $('li[class=what]').css('font-size','30px');
            //[attr!=value] 匹配所有不含有指定的属性，或者属性不等于特定值的元素
            $('li[class!=what]').css('font-size','50px');
            //匹配给定的属性是以某些值开始的元素
            $('input[name^=username]').css('background','gray');
            //匹配给定的属性是以某些值结尾的元素
            $('input[name$=222]').css('background','greenyellow');
            //匹配给定的属性是以包含某些值的元素
            $('button[class*=btn]').css('background','red');
            // 匹配指定的属性都符合的元素
            $('input[name][name=lastname]').css('background','yellow');
        })
    </script>
</html>
```

##### 12.4.2.5 筛选选择器

- find
    - 查找指定元素的所有后代元素，相当于所有子孙后代
- children
    - 查找指定元素的直接子元素，相当于亲生儿子元素
- sibligs
    - 查找所有兄弟的元素，不包含自己
- parent
    - 查找父元素

示例：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <div id="box">
            <p class="p1">
                <span>我是第一个span标签</span>
                <span>我是第二个span标签</span>
                <span>我是第三个span标签</span>
            </p>
            <button>按钮</button>
        </div>
        <ul>
            <li class="list">2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
        </ul>
    </body>
    <script src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        //获取第n个元素 数值从0开始
        $('span').eq(1).css('color','blue');

        //获取第一个元素 :first :last    点语法  ：get方法 和set方法
        $('span').last().css('color','greenyellow');
        $('span').first().css('color','greenyellow');

        //查找span标签的父元素（亲的）
   $('span').parent('.p1').css({"width":'200px','height':'200px',"background":'red'});

        //选择所有的兄弟元素（不包括自己）
        $('.list').siblings('li').css('color','red');

        //查找所有的后代元素
        $('div').find('button').css('background','yellow');

        //不写参数代表获取所有子元素。
        $('ul').children().css("background", "green");
        $('ul').children("li").css("margin-top", 10);
    </script>
</html>
```

示例：siblings用法

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
	<style type="text/css">
		button{
			width: 100px;
			height: 40px;
		}
	</style>
</head>
<body>
	<button>按钮1</button>
	<button>按钮2</button>
	<button>按钮3</button>
	<button>按钮4</button>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		
		$(function(){
			// 内部遍历
			$('button').click(function() {
				// 选项卡
				$(this).css('background','red').siblings('button').css('background','transparent');
				console.log($(this).css('background','red'));
			});
		});
	</script>
</body>
</html>
```

#### 12.4.3 jQuery动画

jQuery提供的一组网页中常见的动画效果，这些动画是标准的、有规律的效果；同时还提供给我们了自定义动画的功能。

##### 12.4.3.1 显示和隐藏

**显示动画效果：**

显示动画用show方法实现。

方式一：无参数，默认是normal  400ms。其实这个方法的底层就是通过`display: block;`实现的。

```js
  $("div").show();
```

方式二：通过控制元素的宽高、透明度、display属性，逐渐显示，3秒后显示完毕。

```js
$('div').show(3000);
```

方式三：和方式二类似，也是通过控制元素的宽高、透明度、display属性，逐渐显示。

```js
 $("div").show("slow");
```

参数可以是：

- slow 慢：600ms
- normal 正常：400ms
- fast 快：200ms

方式四：

```js
 //show(毫秒值，回调函数;
    $("div").show(5000,function () {
        alert("动画执行完毕！");
    });
```

解释：动画执行完后，立即执行回调函数。

**总结：**

上面的四种方式几乎一致：参数可以有两个，第一个是动画的执行时长，第二个是动画结束后执行的回调函数。

**隐藏动画效果：**

隐藏动画用hide方法实现和show方法用法一样。

##### 12.4.3.2 显示隐藏动画

显示和隐藏的来回切换采用的是toggle()方法：就是先执行show()，再执行hide()。

```js
 $(selector).toggle(speed, callback);
```

示例：显示，隐藏，以及显示隐藏

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color:red;
			display: none;
		}
	</style>
</head>
<body>
	<button id="show">显示</button>
	<button id="hide">隐藏</button>
	<button id="toggle">开关式动画</button>
	<div class="box"></div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 显示动画
			$('#show').click(function(){
				// 如果是一个按钮控制盒子显示隐藏 那么得需要去控制isShow这个变量

				// show(动画的时间，fn)   
				// 默认是normal  400ms   slow  600ms  fast 200ms
				$('.box').show('slow',function(){
					$(this).text('alex');
				});
			});
			// 隐藏
			$('#hide').click(function(){

				$('.box').hide('slow');
			});
			// 开关式的显示隐藏动画
			$('#toggle').click(function(){
				// 玩动画 就跟玩定时器一样  先关动画 再开动画
				$('.box').stop().toggle(2000);
			})
		});
	</script>
</body>
</html>
```

##### 12.4.3.3 滑入和滑出

**滑入动画效果：**（类似于生活中的卷帘门）

```js
$(selector).slideDown(speed, 回调函数);
```

解释：下拉动画，显示元素。

注意：省略参数或者传入不合法的字符串，那么则使用默认值：400毫秒

**滑出动画效果：** 

```js
 $(selector).slideUp(speed, 回调函数);
```

解释：上拉动画，隐藏元素。

##### 12.4.3.4 滑入滑出动画

滑入和画出的来回切换采用的是slideToggle()方法：就是先执行show()，再执行slideUp()。

```js
 $(selector).slideToggle(speed, callback);
```

示例：滑入、滑出、以及滑入滑出

```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
    .box {
        width: 200px;
        height: 200px;
        background-color: red;
        display: none;
    }
    </style>
</head>

<body>
    <button id="slideDown">卷帘门下拉</button>
    <button id="slideUp">卷帘门上拉</button>
    <button id="toggleSlide">开关式动画</button>
    <div class="box"></div>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        // 滑入
        $('#slideDown').click(function() {
        		$('.box').slideDown(200);
        });
        // 滑出
        $('#slideUp').click(function() {
     		$('.box').slideUp(600);
        });
        // 开关式的显示隐藏动画
        $('#toggleSlide').click(function() {
          	$('.box').stop().slideToggle(1000);
        })
    });
    </script>
</body>
</html>
```

##### 12.4.3.5 淡入和淡出

**淡入动画效果：**让元素以淡淡的进入视线的方式展示出来

```
 $(selector).fadeIn(speed, callback);
```

**淡出动画效果：**让元素以渐渐消失的方式隐藏起来

```
$(selector).fadeOut(1000);
```

##### 12.4.3.6 淡入淡出动画

淡入淡出的来回切换采用的是fadeToggle()方法：就是先执行fadeIn()，再执行fadeOut()。

淡入淡出效果：通过改变透明度，切换匹配元素的显示或隐藏状态。

```
 $(selector).fadeToggle('fast', callback);
```

示例：淡入、淡出、以及淡入淡出

```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
    .box {
        width: 200px;
        height: 200px;
        background-color: red;
        display: none;
    }
    </style>
</head>

<body>
    <button id="fadeIn">淡入动画</button>
    <button id="fadeOut">淡出动画</button>
    <button id="fadeToggle">开关式动画</button>
    <div class="box"></div>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        // 淡入
        $('#fadeIn').click(function() {
        		$('.box').fadeIn(1000);
        });
        // 淡出
        $('#fadeOut').click(function() {
                // 第二个参数都是有回调函数
     		$('.box').fadeOut(1000);
        });
        // 开关式的淡入淡出
        $('#fadeToggle').click(function() {
          	$('.box').stop().fadeToggle(1000);
        })
    });
    </script>
</body>
</html>
```

##### 12.4.3.7 自定义动画

语法：

```
 $(selector).animate({params}, speed, callback);
```

作用：执行一组CSS属性的自定义动画。

- 第一个参数表示：要执行动画的CSS属性（必选）
- 第二个参数表示：执行动画时长（可选）
- 第三个参数表示：动画执行完后，立即执行的回调函数（可选）

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
	<style type="text/css">
		div{
			width: 100px;
			height: 100px;
			background-color: red;
			position: absolute;
			bottom: 0;
			left: 0;
		}
	</style>
</head>
<body>
	<div></div>
	<button>动画吧</button>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
				$('button').click(function(event) {
					/* Act on the event */
					// animate({队列的属性},时间,fn)
						var json = {
							width:200,
							height: 200,
							top: 200,
							left : 500,
							"border-radius":200,
						};
						var json2 = {
							width: 0,
							height: 0,
							top: 0,
							left: 2000,
						}
						$('div').stop().animate(json,2000,function(){
							$('div').stop().animate(json2,1000,function(){
								alert('已添加购物车')
							})
						});
				});
		});
	</script>
</body>
</html>
```

##### 12.4.3.8 停止动画

```
$(selector).stop(true, false);
```

**里面的两个参数，有不同的含义。**

第一个参数：

- true：后续动画不执行。
- false：后续动画会执行。

第二个参数：

- true：立即执行完成当前动画。
- false：立即停止当前动画。

PS：参数如果都不写，默认两个都是false。实际工作中，直接写stop()用的多。

**菜单下拉案例：**

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        * {
            margin: 0;
            padding: 0;
        }
        ul {
            list-style: none;
        }
        .wrap {
            width: 330px;
            height: 30px;
            margin: 100px auto 0;
            padding-left: 10px;
            background-color: pink;
        }
        .wrap li {
            background-color: green;
        }
        .wrap > ul > li {
            float: left;
            margin-right: 10px;
            position: relative;
        }
        .wrap a {
            display: block;
            height: 30px;
            width: 100px;
            text-decoration: none;
            color: #000;
            line-height: 30px;
            text-align: center;
        }
        .wrap li ul {
            position: absolute;
            top: 30px;
            display: none;
        }
    </style>
</head>
<body>
<div class="wrap">
    <ul>
        <li>
            <a href="javascript:void(0);">一级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">二级菜单2</a></li>
                <li><a href="javascript:void(0);">二级菜单3</a></li>
                <li><a href="javascript:void(0);">二级菜单4</a></li>
            </ul>
        </li>
        <li>
            <a href="javascript:void(0);">二级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">二级菜单2</a></li>
                <li><a href="javascript:void(0);">二级菜单3</a></li>
                <li><a href="javascript:void(0);">二级菜单4</a></li>
            </ul>
        </li>
        <li>
            <a href="javascript:void(0);">三级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">三级菜单2</a></li>
                <li><a href="javascript:void(0);">三级菜单3</a></li>
                <li><a href="javascript:void(0);">三级菜单4</a></li>
            </ul>
        </li>
    </ul>
</div>
  <script src="./jquery-3.3.1.js"></script>
    <script>
        //入口函数
        $(function () {
            //需求：鼠标放入一级li中，让他里面的ul显示。移开隐藏。
            var jqli = $(".wrap>ul>li");

            //绑定事件  mouseenter 鼠标进入 mouseleave  鼠标离开
            // js  onmouseover onmouseout  
            jqli.mouseenter(function () {
                $(this).children("ul").stop().slideDown(1000);
            });
            //绑定事件(移开隐藏)
            jqli.mouseleave(function () {
                $(this).children("ul").stop().slideUp(1000);
            });
        });
    </script>
</body>
</html>
```

#### 12.4.4 jQery属性操作

jQery的属性操作模块分为四个部分：HTML属性操作，DOM属性操作，类样式操作和值操作。

- HTML属性操作：是对HTML文档中的属性进行读取，设置和移除操作。比如attr()、removeAttr()
- DOM属性操作：对DOM元素的属性进行读取，设置和移除操作。比如prop()、removeProp()
- 类样式操作：是指对DOM属性className进行添加，移除操作。比如addClass()、removeClass()、toggleClass()
- 值操作：是对DOM属性value进行读取和设置操作。比如html()、text()、val()

##### 12.4.4.1 HTML属性操作

**1.attr()：**设置属性值或者返回被选元素的属性值

示例：获取值：attr()设置一个属性值的时候，只是获取值

```js
<div title = 'tit1' class="active"></div>
console.log($('div').attr('class'));// active
```

示例：设置值的两种方式

```js
// 方式一：
// 设置 属性的时候 不要使用此方式来设置类名  不建议
$('div').attr('class','box1 box2');
// 方式二：
$('a').attr({
    "href":"http://www.baidu.com",
    title:'哈哈哈哈'
});
```

**2.removeAttr()：**移除属性

示例：

```js
// 移除标签的属性
$('div').removeAttr('title id');
```

##### 12.4.4.2 DOM属性操作

**1.prop()：** 设置或返回被选元素的属性和值。

- 当该方法用于**返回**属性值时，则返回第一个匹配元素的值。
- 当该方法用于**设置**属性值时，则为匹配元素集合设置一个或多个属性/值对。

语法：

返回属性的值：

```js
$(selector).prop(property)
```

设置属性和值：

```javascript
$(selector).prop(property,value)
```

设置多个属性和值：

```javascript
$(selector).prop({property:value, property:value,...})
```

示例：

```js
// 返回属性值
console.log($('input[type=radio]').prop('checked'));

// 设置属性值
$('input[type=radio]').eq(0).prop('aaaaa','11121111');
console.log($('input[type=radio]').eq(0))
```

**2.removeProp()：**移除属性值

示例：

```js
// 移除属性值
$('input[type=radio]').eq(0).removeProp('aaaaa');
console.log($('input[type=radio]').eq(0))
```

attr()和prop()的使用：

1. 是有true,false两个属性使用prop();
2. 其他则使用attr();

##### 12.4.4.3 类样式操作

**1.addClass：**为每个匹配的元素添加指定的类名。

```javascript
$('div').addClass("box");// 追加一个类名到原有的类名
```

还可以为匹配的元素添加多个类名

```javascript
$('div').addClass("box box2");// 追加多个类名
```

**2.removeClass：**从所有匹配的元素中删除全部或者指定的类。

 移除指定的类（一个或多个）

```javascript
$('div').removeClass('box')；
```

移除全部的类

```javascript
$('div').removeClass();
```

**3.toggleClass：**如果存在（不存在）就删除（添加）一个类。

语法：toggleClass('box')

```javascript
$('span').click(function(){
    // 动态的切换class类名为addr
    $(this).toggleClass('addr')
})
```

可以通过添加删除类名，来实现元素的显示隐藏

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
		}
		.hidden{
			display: none;
		}
	</style>
</head>
<body>
	<button id="btn">隐藏</button>
	<div class="box"></div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			var isShow = true;
			$('#btn').click(function(){
				/*
				1.通过控制类样式属性对盒子显示隐藏
				if (isShow) {
					$('.box').css('display','none');
					isShow = false;
					$(this).text('显示');
				}else{
					$('.box').css('display','block');
					isShow = true;
					$(this).text('隐藏');
				}
				*/
                
				// 2.通过控制类名  addClass() removeClass()
				// 谨记：如果是操作类名  一定要使用addClass 和removeClass 不要使用attr()
				if (isShow) {
					// className +=' hidden'
					$('.box').addClass('hidden active yyy uuu ooo ppp');
					isShow = false;
					$(this).text('显示');
				}else{
					$('.box').removeClass('hidden yyy uuu ooo ppp');
					isShow = true;
					$(this).toggleClass('addr');
					$(this).text('隐藏');
				}
			})
		});
	</script>
</body>
</html>
```

##### 12.4.4.4 值操作

**html()：**html() 是获取选中标签元素中所有的内容

语法：

```javascript
$('#box').html();
```

设置值：设置该元素的所有内容，会替换掉，标签中原来的内容。

```javascript
$('#box').html('<a href="https://www.baidu.com">百度一下</a>');
```

**text()：**获取匹配元素包含的文本内容

语法：

```javascript
$('#box').text();
```

设置值：设置该所有的文本内容

```javascript
$('#box').text('<a href="https://www.baidu.com">百度一下</a>');
```

**注意：值为标签的时候，不会被渲染为标签元素，只会被当做值渲染到浏览器中。**

**val()：**用于表单控件中获取值，比如input textarea select等等

设置值：

```javascript
$('input').val('设置了表单控件中的值')；
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<p id="box">
		wuSir
	</p>
	<div class="box">
		外边
		<span>里边</span>
	</div>
	<input type="text" value="123">
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 只获取文本的内容  text() innerText
			// trim()清除前后的空格
			console.log($('#box').text().trim());

			// 设置文本的内容
			$('#box').text('<h2> 武sir  </h2>');

			// 获取标签和文本的内容 html() innerHTML
			console.log($('.box').html().trim());

			// 设置
			$('.box').html('<a href="https://www.baidu.com">百度一下</a>');

			// 获取表单input中的值
			console.log($('input').val());

			// 清空input输入框中的内容
			$('input').val('');
        
			// 设置input输入框中的内容
			$('input').val('哈哈哈哈');
		});
	</script>
</body>
</html>
```

#### 12.4.5 DOM文档的操作

##### 12.4.5.1 插入操作

###### 知识点1：父子之间

语法：追加某元素，在父元素中添加新的子元素。子元素可以为：stirng | element（js对象） | jquery元素

```js
父元素.append(子元素)
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div class="wuSir">wusir</div>
	<div class="box"></div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			var oP = document.createElement('p');
			oP.innerText = '基友';
			// 1.父子之间 父.append(子)  子.appendTo(父)
			// 子元素：可以是 一个string、jsDOM对象、jquery对象
			$('.box').append('alex');// 可以插入普通的文本
			$('.box').append('<h2>alex</h2>');// 可以插入标签+文本
			$('.box').append(oP); // 插入一个jsDom对象
			$('.box').append($('.wusir')); // 如果插入的是一个jquery对象 相当于是一个移动操作
		});
	</script>
</body>
</html>
```

###### 知识点2：父子之间

语法：追加到某元素，子元素添加到父元素，要添加的元素同样既可以是stirng 、element(js对象) 、 jquery元素

```
子元素.appendTo(父元素)
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div class="wuSir">wusir</div>
	<div class="box"></div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			$('<p>天霸</p>').appendTo('.box').click(function(event) {
				$(this).css({
					width:100,
					height:100,
					backgroundColor:'red'
				}).text('wuSir');

			});;
		});
	</script>
</body>
</html>
```

###### 知识点3：父子之间

语法：前置添加， 添加到父元素的第一个位置

```javascript
父元素.prepend(子元素)；
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<ul>
		<li>alex</li>
	</ul>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// prepend()   prependTo()
			//1. prepend() 插入 子级的第一个元素
			$('ul').prepend('<li>wusir</li>');
			});
		});
	</script>
</body>
</html>
```

###### 知识点4：父子之间

语法：前置添加， 添加到父元素的第一个位置

```javascript
子元素.prependTo(父元素)；
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<ul>
		<li>alex</li>
	</ul>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			$('<li>村长</li>').prependTo('ul').click(function() {
				alert(this.innerText);
			});
		});
	</script>
</body>
</html>
```

###### 知识点5：兄弟之间

语法：在匹配的元素之后插入内容 

```javascript
兄弟元素.after(要插入的兄弟元素)；
要插入的兄弟元素.inserAfter(兄弟元素)；
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <ul>
        <li class="item">alex</li>
    </ul>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        // es6的模板字符串   tab键上面那个符号  反引号 ``,使用${变量名}插入变量
        var title = "百度一下下";
        $('.item').after(`<li>
			<a href="#">${title}</a>
		</li>`);
        $('<li>wusir</li>').insertAfter('.item');
    </script>
</body>
</html>
```

###### 知识点6：兄弟之间

语法：在匹配的元素之前插入内容 

```javascript
兄弟元素.before(要插入的兄弟元素)；
要插入的兄弟元素.inserBefore(兄弟元素)；
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <ul>
        <li class="item">alex</li>
    </ul>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        var title = "百度一下下";
 	 	$('.item').before(`<li>
			<a href="#">${title}</a>
		</li>`);
		 $('<li>wusir</li>').insertBefore('.item');
    </script>
</body>
</html>
```

##### 12.4.5.2 替换操作

###### 知识点1：单个替换

语法：将所有匹配的元素替换成指定的string、js对象、jquery对象。

```
$(selector).replaceWith(content);
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div class="box">
		<h2>alexsb</h2>
		<h2>alexsb</h2>
		<h3>wusirddb</h3>
	</div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 页面中获取的DOM对象.replaceWith(替换的内容)
			$('h2').replaceWith('<span>圆圆</span>');
		});
	</script>
</body>
</html>
```

###### 知识点2：所有替换

语法：替换所有。将所有的h2标签替换成p标签。

```
$('<p>哈哈哈</p>').replaceAll('h2');
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div class="box">
		<h2>alexsb</h2>
		<h2>alexsb</h2>
		<h3>wusirddb</h3>
	</div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			$('<p style = "color:red;">黑girl</p>').replaceAll('span');
		});
	</script>
</body>
</html>
```

##### 12.4.5.3删除操作

###### 知识点1：节点事件都删除

语法：删除节点后，事件也会删除（简言之，删除了整个标签）

```js
$(selector).remove(); 
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div class="box">
        <p style="font-size: 20px;font-weight: 600;">alex</p>
    </div>
    <button>删除</button>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        $('button').click(function() {
        	  alert(1);
            // remove() 删除节点后 事件也会删除  删除了整个标签
            console.log($(this).remove());
            var jqBtn = $(this).remove();
            $('.box').prepend(jqBtn);
        })
    });
    </script>
</body>
</html>
```

###### 知识点2：删除节点保留事件

语法：删除节点后，事件会保留

```
$(selector).detach(); 
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div class="box">
        <p style="font-size: 20px;font-weight: 600;">alex</p>
    </div>
    <button>删除</button>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        $('button').click(function() {
        	  alert(1);
            // detach() 删除节点后 事件会保留
            var jqBtn = $(this).detach();
            $('.box').prepend(jqBtn);
        })
    });
    </script>
</body>
</html>
```

###### 知识点3：清空后代节点

语法：清空选中元素中的所有后代节点

```js
$(selector).empty(); 
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div class="box">
        <p style="font-size: 20px;font-weight: 600;">alex</p>
    </div>
    <button>删除</button>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        $('button').click(function() {
        	  alert(1);
        	  // 清空选中元素中的所有后代节点
			$('.box').empty();
        })
    });
    </script>
</body>
</html>
```

#### 12.4.6 jQuery位置信息

##### 12.4.6.1 宽度和高度

**获取宽度：**

```js
.width()
```

描述：为匹配的元素集合中获取第一个元素的当前计算宽度值。这个方法不接受任何参数。

`.css(width)` 和 `.width()`之间的区别是后者返回一个没有单位的数值（例如，`400`），前者是返回带有完整单位的字符串（例如，`400px`）。当一个元素的宽度需要数学计算的时候推荐使用`.width()` 方法 。

**设置宽度：**

```js
.width( value )
```

描述：给每个匹配的元素设置CSS宽度。

**获取高度：**

```js
.height()
```

描述：获取匹配元素集合中的第一个元素的当前计算高度值。

- 这个方法不接受任何参数。

**设置高度：**

```js
 .height( value )
```

描述：设置每一个匹配元素的高度值。

##### 12.4.6.2 内部宽和内部高

**获取内部宽：**

```
.innerWidth()
```

描述：为匹配的元素集合中获取第一个元素的当前计算宽度值,包括padding，但是不包括border。

ps:这个方法不适用于`window` 和 `document`对象，对于这些对象可以使用`.width()`代替。

**设置内部宽：**

```
.innerWidth(value);
```

描述： 为匹配集合中的每个元素设置CSS内部宽度。如果这个“value”参数提供一个数字，jQuery会自动加上像素单位（px）。

**获取内部高：**

```
.innerHeight();
```

描述：为匹配的元素集合中获取第一个元素的当前计算高度值,包括padding，但是不包括border。

ps:这个方法不适用于`window` 和 `document`对象，对于这些对象可以使用`.height()`代替。

**设置内部宽：**

```
.innerHeight(value);
```

描述： 为匹配集合中的每个元素设置CSS内部高度。如果这个“value”参数提供一个数字，jQuery会自动加上像素单位（px）。

##### 12.4.6.3 外部宽和外部高

**获取外部宽：**

```
 .outerWidth( [includeMargin ] )
```

描述：获取匹配元素集合中第一个元素的当前计算外部宽度（包括padding，border和可选的margin）

- includeMargin (默认: `false`)

    类型： `Boolean`

    一个布尔值，表明是否在计算时包含元素的margin值。

- 这个方法不适用于`window` 和 `document`对象，可以使用`.width()`代替

**设置外部宽：**

```
 .outerWidth( value )
```

描述： 为匹配集合中的每个元素设置CSS外部宽度。

**获取外部高：**

```
 .outerHeight( [includeMargin ] )
```

描述：获取匹配元素集合中第一个元素的当前计算外部高度（包括padding，border和可选的margin）

- includeMargin (默认: `false`)

    类型： `Boolean`

    一个布尔值，表明是否在计算时包含元素的margin值。

- 这个方法不适用于`window` 和 `document`对象，可以使用`.width()`代替

**设置外部高：**

```
 .outerHeight( value )
```

描述： 为匹配集合中的每个元素设置CSS外部高度。

##### 12.4.6.4 偏移

**获取**

```js
.offset()
```

返回值：[Object](http://www.shouce.ren/api/view/a/13081#articleHeader15) 。`.offset()`返回一个包含`top` 和 `left`属性的对象 。

描述：在匹配的元素集合中，获取的第一个元素的当前坐标，坐标相对于文档。

注意：jQuery不支持获取隐藏元素的偏移坐标。同样的，也无法取得隐藏元素的 border, margin, 或 padding 信息。若元素的属性设置的是 `visibility:hidden`，那么我们依然可以取得它的坐标

**设置**

```js
 .offset( coordinates )
```

描述： 设置匹配的元素集合中每一个元素的坐标， 坐标相对于文档。

- coordinates

  类型: [Object](http://www.shouce.ren/api/view/a/13081#articleHeader25)

  一个包含`top` 和 `left`属性的对象，用整数指明元素的新顶部和左边坐标。

例子：

```js
$("p").offset({ top: 10, left: 30 });
```

**水平方向获取：**

```js
.scrollLeft()
```

描述：获取匹配的元素集合中第一个元素的当前水平滚动条的位置（页面卷走的宽度）

**水平方向设置：**

```js
.scrollLeft( value )
```

描述：设置每个匹配元素的水平方向滚动条位置。

**垂直方向获取：**

```js
.scrollTop()
```

描述：获取匹配的元素集合中第一个元素的当前迟滞滚动条的位置（页面卷走的高度）

**垂直方向获取：**

```js
.scrollLeft( value )
```

描述：设置每个匹配元素的垂直方向滚动条位置。

#### 12.4.7 jQuery事件

HTML中与JavaScript交互是通过事件驱动来实现的，例如鼠标点击事件、页面的滚动事件onscroll等等，可以向文档或者文档中的元素添加事件监听器来预订事件。想要知道这些事件是在什么时候进行调用的，就需要了解一下“事件流”的概念。

##### 12.4.7.1 事件流的概念

事件流描述的是从页面中接收事件的顺序，以流的顺序执行。

**DOM事件流**

“ DOM2级事件”规定的事件流包括三个阶段：

1. 事件捕获阶段；

2. 处于目标阶段；

2. 事件冒泡阶段；

```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title></title>
</head>

<body>
    <button id='btn'>按钮</button>
    <script type="text/javascript">
    var oBtn = document.getElementById('btn')
    // oBtn.onclick = function(){
    // 	alert(1);
    // };
    // 如果是true 则表示有捕获
    oBtn.addEventListener('click', function() {
        console.log('按钮处于捕获阶段');
        alert(1);
    }, true)
    document.body.addEventListener('click', function() {
        console.log('body处于捕获阶段');
    }, true)
    document.documentElement.addEventListener('click', function() {
        console.log('html处于捕获阶段');
    }, true)
    document.addEventListener('click', function() {
        console.log('文档处于捕获阶段');
    }, true)
     oBtn.addEventListener('click', function() {
        console.log('按钮处于冒泡阶段');
    }, false)
    document.body.addEventListener('click', function() {
        console.log('body处于冒泡阶段');
    }, false)
    document.documentElement.addEventListener('click', function() {
        console.log('html处于冒泡阶段');
    }, false)
    document.addEventListener('click', function() {
        console.log('文档处于冒泡阶段');
    }, false)
    </script>
</body>
</html>

/*打印结果：
文档处于捕获阶段
27-原生js的事件流.html:25 html处于捕获阶段
27-原生js的事件流.html:22 body处于捕获阶段
27-原生js的事件流.html:18 按钮处于捕获阶段
27-原生js的事件流.html:31 按钮处于冒泡阶段
27-原生js的事件流.html:34 body处于冒泡阶段
27-原生js的事件流.html:37 html处于冒泡阶段
27-原生js的事件流.html:40 文档处于冒泡阶段
*/
```

解释：

1、addEventListener：

addEventListener 是DOM2 事件新增的指定事件处理程序的操作，这个方法接收3个参数：

- 要处理的事件名
- 作为事件处理程序的函数
- 一个布尔值
    - 最后这个布尔值参数如果是true，表示在捕获阶段调用事件处理程序；如果是false，表示在冒泡阶段调用事件处理程序。

2、document、documentElement和document.body三者之间的关系：

- document代表的是整个html页面；

- document.documentElement代表的是`<html>`标签；

- document.body代表的是`<body>`标签；

执行过程：

首先在事件捕获过程中，document对象首先接收到click事件，然后事件沿着DOM树依次向下，一层一层向下传播，直到找到事件的实际目标。也就是示例中的`btn`。

接着在事件冒泡过程中，事件开始时由最具体的元素（button标签）接收，然后逐级向上传播到较为不具体的节点鼻祖（document）。

需要注意的点：由于老版本的浏览器不支持事件捕获，因此在实际开发中需要使用事件冒泡，在由特殊需要时再使用事件捕获

补充知识了解即可：

1、IE中的事件流只支持“事件冒泡”，但是版本到了IE9+以后，实现了“DOM2级事件”，也就是说IE9+以后也可以在捕获阶段对元素进行相应的操作。

2、在DOM事件流中，实际的目标在“捕获阶段”不会接收到事件。而是在“处于目标阶段”被触发，并在事件处理中被看成“冒泡阶段”的一部分。然后，“冒泡阶段”发生，事件又传播回文档。

事件冒泡处理：event.stopPropagation();

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
	<style type="text/css">
		.father{
			width: 300px;
			height: 300px;
			background-color: red;
		}

	</style>
</head>
<body>
	<div class="father">
		<button>按钮</button>
		<a href="http://www.baidu.com">百度一下</a>
	</div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){

			// 给按钮绑定事件
			// 在所有的事件回调函数中 都会有默认的事件对象
			$('.father button').click(function(event){
				// 原生js的事件对象
				console.log(event);
				alert($(this).text());
				// 阻止事件冒泡
				event.stopPropagation();

			});

			$('a').click(function(e){
				// e.preventDefault();
				// e.stopPropagation();
				alert('a被点击了');
				// 相当于 e.preventDefault() 和 e.stopPropagation();
				return false;
			});

			$('.father').click(function(event){
				console.log(event);
				// alert('父亲被点击了');
				event.stopPropagation();
				// console.log('哈哈哈哈哈');

				// 既阻止了默认事件 又阻止了冒泡
				// return false;
			});
			
			$('body').click(function(e){
				console.log(e);
				e.stopPropagation();
				alert('body被点击了');
			})
		});
	</script>
</body>
</html>
```

**冒泡事件应用：**

```js
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        * {
            padding: 0;
            margin: 0;
        }

        a {
            text-decoration: none;
        }

        .change {
            width: 100%;
            height: 300px;
            background-color: #67b168;
            position: fixed;
            top: 0;
            left: 0;
            display: none;

        }

        .change ul li {
            display: inline-block;
            width: 100px;
            height: 40px;
            background-color: #666666;
            text-align: center;
            line-height: 40px;
        }

        .change ul li a {
            display: block;
            width: 100px;
            height: 40px;
            color: #cccccc;
        }
    </style>
</head>
<body>
<a href="#" class="fu">换肤</a>
<div class="change">
    <ul>
        <li><a href="#">热门</a></li>
        <li><a href="#">电脑</a></li>
        <li><a href="#">键盘</a></li>
    </ul>
</div>

<script src="../../static/jquery-3.5.1.js"></script>
<script>
    $(function () {
        $('.fu').click(function (even) {
            even.stopPropagation();
            even.preventDefault();
            $('.change').slideDown(500);
            $('.change ul li a').click(function (even) {
                // 阻止默认事件，阻止冒泡
                even.preventDefault();
                even.stopPropagation();
                $(this).css('color', 'red').parent().siblings().children().css('color', '#cccccc')
            });

        });

        $('.change,ul').click(function () {
            return false;
        });

        $(document).click(function () {
            $('.change').stop().slideUp(500);
        })
    })
</script>
</body>
</html>



```

##### 12.4.7.2 jQuery常用事件

鼠标事件：

- click()：鼠标单击触发事件
- dbclick()：鼠标双击触发事件
- mousedown()：鼠标按下触发事件
- mouseup()：鼠标弹起触发事件
- mousemove()：鼠标移动触发事件
- mouseover()：鼠标移入触发事件
- mouseout()：鼠标移出触发事件
    - 移入和移出是指被选元素或当前元素的子元素
- mouseenter()：鼠标进入触发事件
- nouseleave()：鼠标离开触发事件
    - 进入和离开是指被选元素，不包括子元素
- focus()：鼠标聚焦触发事件
- blur()：失去焦点触发事件
- keydown()：键盘按下触发事件
- keyup：键盘弹起触发事件

表单事件：

- change()：表单元素发生改变的时候触发事件
    - 此事件仅限于input、textarea、select元素
- select()：文本元素发生改变的时候触发事件
    - 此事件仅限于input、type类型为text和textarea表单元素
- submit()：表单元素发生改变的时候触发事件

示例：鼠标移入和进入事件

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
	<style type="text/css">
		.father{
			width: 200px;
			height: 200px;
			background-color:red;
		}
		.child{
			width: 50px;
			height: 50px;
			background-color: green;
		}
	</style>
</head>
<body>
	<div class="father">
		<p class="child">
			alex
		</p>
	</div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		
		$(function(){
			// 鼠标穿过被选元素和被选元素的子元素 会触发此事件
			// $('.father').mouseover(function(event) {
			// 	console.log('移入了');
			// });
			// $('.father').mouseout(function(event) {
			// 	console.log('移出了');
			// });
			// 鼠标只穿过被选元素会触发此事件
			$('.father').mouseenter(function(event) {
				console.log('进入了');
			});
			$('.father').mouseleave(function(event) {
				console.log('离开了');
			});
		});
	</script>
</body>
</html>
```

示例：鼠标单击双击事件

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<button>按钮</button>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 两次 单击中间的时间差是300毫秒 ，如果小于300毫秒 表示双击
			// 遇到的问题：是双击  调用了两次单击
			var timer = null;
			var count  = 0;
			// 解决这个单双击冲突问题
			$('button').click(function(event) {
				// console.log(1);
				console.log(timer);
				// 取消第一次延时未执行的 方法
				clearTimeout(timer);
				// 如果是双击事件 要阻止 两次单击事件的调用 
				timer = setTimeout(function(){
					count++;
					// console.log(count);
					// console.log('单击了');
				},300)
			});
			$('button').dblclick(function(event) {
				// 取消的是第二次延时未执行方法
				console.log(timer);
				clearTimeout(timer);
				console.log('双击了');
			});
		});
	</script>
</body>
</html>
```

示例：鼠标焦点与键盘按下事件

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<input type="text" name="user">
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		
		$(function(){
			// 加载页面时 让输入框 获得焦点
			$('input[type=text]').focus();

			setTimeout(function(){
				$('input[type=text]').blur();
			},2000)

			$('input[type=text]').focus(function(){
				console.log('获取焦点');
			});
			$('input[type=text]').blur(function(){
				console.log('失去焦点');
			});

			// 键盘按键事件 
			$('input').keyup(function(e){
				console.log(e.keyCode);
				// 键码
				switch (e.keyCode) {
					case 13:
						console.log('回车键调用了');
						console.log($(this).val());
						// 未来与后端进行交互
						break;
					case 27:
						console.log('回车键调用了');
						console.log($(this).val());
						// 未来与后端进行交互
						break;
					default:
						// statements_def
						break;
				}
			})
		});
	</script>
</body>
</html>
```

示例：表单事件

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<form action="http://www.baidu.com/s" method="get">
		<input type="text" name="wd">
		<input type="submit">
	</form>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		
		$(function(){
			// 文本选中的时候会调用
			$('input[type=text]').select(function(){
				console.log('内容选中了');
			});
			// 原生js的onsubmit事件
			$('form').submit(function(e){
				e.preventDefault();
				// 未来 自己去发请求  往百度发请求 ajax技术
				console.log('form被submit了');
			});
			$('input[type=text]').change(function(){
				console.log('内容被修改了');
			})
		});
	</script>
</body>
</html>
```

##### 12.4.7.3 事件委托

通俗的讲，事件就是onclick，onmouseover，onmouseout，等就是事件，委托就是让别人来做，这个事件本来是加在某些元素上的，然而你却加到别人身上来做，完成这个事件。

举例：比如卖房子会委托中介，客户只要把房子信息告诉中介就可了。

**原理：**

- 利用冒泡的原理，把事件加到父级上，触发执行效果。

 **作用：**

- 性能要好
- 针对新创建的元素，直接可以拥有事件

**事件源 :**

- 跟this作用一样(他不用看指向问题，谁操作的就是谁),event对象下的

**使用情景：**

- 为DOM中的很多元素绑定相同事件；
- 为DOM中尚不存在的元素绑定事件； 

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<ul>
	    <li>alex</li>
	    <li class="item">wusir</li>
	</ul>
	<button>添加</button>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			/*
			$('ul>li').click(function(){
				alert($(this).text());
			});
			*/	

			// 2.再执行这段代码
			// 事件委托  （看时机  如果是未来追加的元素 建议使用 事件委托来绑定事件）
			// 原理： 利用冒泡的原理，把事件加到父级上，触发执行效果。
			$('ul').on('click','li',function(e){
				alert($(this).text());
			});

			// 1.先执行这段代码：
			// 未来 动态的 往ul中追加了li标签
			// 未来追加的li标签 自己完成不了click事件，那么这个时候考虑“事件委托(代理)”
			$('button').click(function(event) {
				$('ul').append('<li>黑gril</li>')
			});

		});
	</script>
</body>
</html>
```

#### 12.4.8 jQuery的Ajax

AJAX = 异步的javascript和XML（Asynchronous Javascript and XML）

简言之，在不重载整个网页的情况下，AJAX通过后台加载数据，并在网页上进行显示。

通过 jQuery AJAX 方法，您能够使用 HTTP Get 和 HTTP Post 从远程服务器上请求文本、HTML、XML 或 JSON - 同时您能够把这些外部数据直接载入网页的被选元素中。

**jquery的$.ajax()方法**：

```js
/*
jquery的$.ajax()方法 是做ajax技术经常使用的一个方法。

它的参数很多，总会有一些初学者记不住，在这里，演示几个经常使用的参数。后面讲django会详细讲ajax技术的原理。大家先把每个参数做个笔记。
参数如下： 

1.url: 要求为String类型的参数，（默认为当前页地址）发送请求的地址。

2.type: 要求为String类型的参数，请求方式（post或get）默认为get。注意其他http请求方法，例如put和delete也可以使用，但仅部分浏览器支持。

3.timeout: 要求为Number类型的参数，设置请求超时时间（毫秒）。此设置将覆盖$.ajaxSetup()方法的全局设置。

4.async: 要求为Boolean类型的参数，默认设置为true，所有请求均为异步请求。如果需要发送同步请求，请将此选项设置为false。注意，同步请求将锁住浏览器，用户其他操作必须等待请求完成才可以执行。

5.cache: 要求为Boolean类型的参数，默认为true（当dataType为script时，默认为false），设置为false将不会从浏览器缓存中加载请求信息。

6.data: 要求为Object或String类型的参数，发送到服务器的数据。如果已经不是字符串，将自动转换为字符串格式。get请求中将附加在url后。防止这种自动转换，可以查看　　processData选项。对象必须为key/value格式，例如{foo1:"bar1",foo2:"bar2"}转换为&foo1=bar1&foo2=bar2。如果是数组，JQuery将自动为不同值对应同一个名称。例如{foo:["bar1","bar2"]}转换为&foo=bar1&foo=bar2。

7.dataType: 要求为String类型的参数，预期服务器返回的数据类型。如果不指定，JQuery将自动根据http包mime信息返回responseXML或responseText，并作为回调函数参数传递。可用的类型如下：

　　xml：返回XML文档，可用JQuery处理。

　　html：返回纯文本HTML信息；包含的script标签会在插入DOM时执行。

　　script：返回纯文本JavaScript代码。不会自动缓存结果。除非设置了cache参数。注意在远程请求时（不在同一个域下），所有post请求都将转为get请求。

　　json：返回JSON数据。

　   jsonp：JSONP格式。使用SONP形式调用函数时，例如myurl?callback=?，JQuery将自动替换后一个“?”为正确的函数名，以执行回调函数。

　　text：返回纯文本字符串。

8.beforeSend： 要求为Function类型的参数，发送请求前可以修改XMLHttpRequest对象的函数，例如添加自定义HTTP头。在beforeSend中如果返回false可以取消本次ajax请求。XMLHttpRequest对象是惟一的参数。 function(XMLHttpRequest){ this; //调用本次ajax请求时传递的options参数 }

9.complete：要求为Function类型的参数，请求完成后调用的回调函数（请求成功或失败时均调用）。参数：XMLHttpRequest对象和一个描述成功请求类型的字符串。 function(XMLHttpRequest, textStatus){ this; //调用本次ajax请求时传递的options参数 }

10.success：

　　要求为Function类型的参数，请求成功后调用的回调函数，有两个参数。

　　(1)由服务器返回，并根据dataType参数进行处理后的数据。

　　(2)描述状态的字符串。 function(data, textStatus){ //data可能是xmlDoc、jsonObj、html、text等等 

11.error: 要求为Function类型的参数，请求失败时被调用的函数。该函数有3个参数，即XMLHttpRequest对象、错误信息、捕获的错误对象(可选)。ajax事件函数如下： function(XMLHttpRequest, textStatus, errorThrown){ //通常情况下textStatus和errorThrown只有其中一个包含信息 this; //调用本次ajax请求时传递的options参数 }

12.contentType： 要求为String类型的参数，当发送信息至服务器时，内容编码类型默认为"application/x-www-form-urlencoded"。该默认值适合大多数应用场合。

13.dataFilter： 要求为Function类型的参数，给Ajax返回的原始数据进行预处理的函数。提供data和type两个参数。data是Ajax返回的原始数据，type是调用jQuery.ajax时提供的dataType参数。函数返回的值将由jQuery进一步处理。 function(data, type){ //返回处理后的数据 return data; }

14.global： 要求为Boolean类型的参数，默认为true。表示是否触发全局ajax事件。设置为false将不会触发全局ajax事件，ajaxStart或ajaxStop可用于控制各种ajax事件。

15.ifModified： 要求为Boolean类型的参数，默认为false。仅在服务器数据改变时获取新数据。服务器数据改变判断的依据是Last-Modified头信息。默认值是false，即忽略头信息。

16.jsonp： 要求为String类型的参数，在一个jsonp请求中重写回调函数的名字。该值用来替代在"callback=?"这种GET或POST请求中URL参数里的"callback"部分，例如{jsonp:'onJsonPLoad'}会导致将"onJsonPLoad=?"传给服务器。

17.username： 要求为String类型的参数，用于响应HTTP访问认证请求的用户名。

18.password： 要求为String类型的参数，用于响应HTTP访问认证请求的密码。

19.processData： 要求为Boolean类型的参数，默认为true。默认情况下，发送的数据将被转换为对象（从技术角度来讲并非字符串）以配合默认内容类型"application/x-www-form-urlencoded"。如果要发送DOM树信息或者其他不希望转换的信息，请设置为false。

20.scriptCharset： 要求为String类型的参数，只有当请求时dataType为"jsonp"或者"script"，并且type是GET时才会用于强制修改字符集(charset)。通常在本地和远程的内容编码不同时使用
*/
```

示例：这个是需要与后台交互的，后台必须启动才能有效果

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<form >
		<input type="text" name="user">
		<input type="submit" name="">
	</form>
	<!-- <div class="box"></div> -->
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){

			$('form').submit(function(e){
				// 阻止form表单的默认事件
				e.preventDefault();
				var userVal = $('input[name=user]').val();
				console.log(userVal);
				
				// 与你后端交互
				$.ajax({
					url:"http://localhost:8800/create",
					type:'post',
					data:{
						"name":userVal
					},
					success:function(data){
						console.log(data);
					},
					error:function(err){
						console.log(err);
					}
				})
			})
		})
	</script>
</body>
</html>
```

和风天气请求示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div class="tmp"></div>
	<div class="city"></div>
	<img src="" alt="">
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			$.ajax({
				url:'https://free-api.heweather.com/s6/weather/now?location=beijing&key=4693ff5ea653469f8bb0c29638035976',
				type:"get",
				success:function (data) {
					console.log(data.HeWeather6[0].now.tmp);
					// 温度
					var tmp = data.HeWeather6[0].now.tmp;
					// 城市
					var city = data.HeWeather6[0].basic.location;
					// 天气状况码
					var cond_code= data.HeWeather6[0].now.cond_code;

					// 后面方法的参数使用的是es6的模板字符串拼接的变量
					$('.tmp').text(`${tmp}℃`);
					$('.city').text(city);
					// 后面的地址是使用的和风天气的天气状况cdn资源。您也可以使用本地图片加载
					$('img').attr('src',`https://cdn.heweather.com/cond_icon/${cond_code}.png`);
				}
			})
		});
	</script>
</body>
</html>
```

### 12.5 Bootstrap

简洁、直观、强悍的前端开发框架，让web开发更迅速、简单。

**Bootstrap**官网就是很好的笔记资源：https://www.bootcss.com/

## 第十三章 Django框架

### 13.1 HTTP协议简介

- HTTP协议(请求和应答,应用层协议)

    - 状态码

        - 1xx 消息
        - 2xx 成功
        - 3xx 重定向
        - 4xx 请求错误
        - 5xx 服务端的错误

    - 请求方式8种(常用的2种)

        - get  获取一个页面,图片
        - post  提交数据

    - url 

        url包括(协议 域名和端口 HTTP（80） HTTPS(443) 路径 参数)


```python
    '''
    1.http	协议
    2.www.luffycity.com	域名
    3.80	端口
    4.news/index.html	路径
    5.?id=250&page=1	参数
	'''
```

- get与post请求

    - GET请求提交的数据会放在URL之后，以?分割URL和传输数据，参数之间以&相连， POST方法是把提交的数据放在HTTP包的Body中.

    - GET请求提交的数据大小有限制（因为浏览器对URL的长度有限制），而POST请求提交的数据没有限制.

    - GET与POST请求在服务端获取请求数据方式不同。

    - GET请求提交数据，会带来安全问题，比如一个登录页面，通过GET请求提交数据时，用户名和密码将出现在URL上，如果页面可以被缓存或者其他人可以访问这台机器，就可以从历史记录获得该用户的账号和密码.

    - Get方法会产生一个TCP数据包，浏览器会把Header和Data一并发送出去，服务器响应200（OK），并回传相应的数据。

        Post方法会产生两个TCP数据包，浏览器会先将Header发送出去，服务器响应100（Continue）后，浏览器再发送Data，

        服务器响应200（OK），并回传相应的数据

    **优缺点对比：**

    Get方法安全性低，效率高；Post方法安全性高，效率低（耗时稍长）

- 请求格式

     ![img](J:\homework\Python学习笔记\Python_notes.assets\Python学习笔记.md) 

    请求首行与请求头的部分用\r\n分隔,请求头与请求体以\r\n\r\n分隔

- 响应格式

      ![img](J:\homework\Python学习笔记\Python_notes.assets\yuan_6.png) 

django请求生命周期：

 <img src="J:\homework\Python学习笔记\Python_notes.assets\202011130830231.png" alt="202011130830231.png"  /> 

1. wsgi，他就是socket服务端，用于接收用户请求并将请求进行初次封装，然后将请求交给web框架
2. 中间件，帮助我们对请求进行校验或在请求对象中添加其他相关数据，例如：csrf
3. 路由匹配，进行分发，分发给对应的视图
4. 视图函数，在视图函数中进行业务逻辑处理，涉及到ORM取数据、tmplates渲染页面
5. 中间件，对相应的数据进行处理
6. wsgi，将响应的内容发送给浏览器

### 13.2 web框架

- C/S：是客户端/服务器端程序

- B/S：是浏览器端/服务器端应用程序,WEB应用程序一般是B/S模式

- 百度的服务器 socket服务端

    1. 创建socket服务端
    2. 绑定 IP 和端口
    3. 监听
    4. 等待链接
    5. 接收数据
    6. 返回数据
    7. 断开链接

- 浏览器socket客户端

    1. 创建socket服务端
    2. 绑定 IP 和端口
    3. 发送数据
    4. 接收数据
    5. 断开链接

- Web框架------>socket服务端

    Web框架（Web framework）是一种开发框架，用来支持动态网站、网络应用和网络服务的开发。这大多数的Web框架提供了一套开发和部署网站的方式，也为Web行为提供了一套通用的方法。Web框架已经实现了很多功能，开发人员使用框架提供的方法并且完成自己的业务逻辑，就能快速开发web应用了。浏览器和服务器的是基于HTTP协议进行通信的。也可以说Web框架就是在以上十几行代码基础张扩展出来的，有很多简单方便使用的方法，大大提高了开发的效率。

```python
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8901))
sock.listen(5)

while True:
    print('server waiting....')
    # conn客户端的套接字
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print('data', data)

    # 读取文件
    with open('login.html', 'r')as f:
        data = f.read()

    # http协议/版本/ 状态码/ 成功
    conn.send(("HTTP/1.1 200 OK\r\nContent-type:text\r\n\r\n%s" % data).encode('gbk'))
    conn.close()

```

- wagiref模块

    wagiref（Web Server Gateway Interface）的简称，封装了socket服务端与客户端的交互，我们可以直接调用其功能，省去了大量的时间。

    ```python
    from wsgiref.simple_server import make_server
    
    
    def application(eviron, start_response):
    
        # 按着http请求协议解析数据:eviron
        # 按着http响应协议组装数据:start_response
        print(eviron)
        print(type(eviron))
    
        # 专注与web业务开发
        # 获取当前路径
        path = eviron.get('PATH_INFO')
        start_response('200 OK', [('Content-Type', 'text/html')])
        if path == '/login':
            with open('login.html', 'r')as f:
                data = f.read()
            return [data.encode('gbk')]
        elif path == '/index.html':
            with open('index.html', 'r')as f:
                data = f.read()
            return [data.encode('gbk')]
    
    
    # 封装socket链接前三步
    httped = make_server("", 8061, application)
    
    # 等待用户链接 conn,addr = sock.accept()
    httped.serve_forever()
    ```

### 13.3 django的下载与基本命令

1. 下载django：

    ```python
    pip3 install django
    ```

2. 创建一个django project

    ```python
    django-admin.py startproject mysite
    ```

    会创建一个mysite的项目，目录结构如下：

    ```python
    |---manage.py  # django项目里的工具,可以通过它调用django shell和数据库等,管理django站点
    |---mysite  # 文件夹
    	|---_init__.py  # 初始化文件
    	|---settings.py  # 包含了项目的默认配置,包括数据库信息及其他的一些配置信息
    	|---urls.py  # 负责把url模式影协到应用程序,url根配置
    	|---wsgi.py  # 内置runserver命令的WSGI应用配置
    ```

3. 在mysite目录下创建应用

    ```python
    python manage.py startapp blog
    ```

    ```python
    blog
    |---_init__.py
    |---admin.py
    |---apps.py
    |---models.py
    |---tests.py
    |---views.py
    |---migrations
    	|---__init__.py
    ```

4. vscode环境配置

    ```python
    # 新建django工程
    django-admin startproject hello_django
    # 进入到django工程目录下
    cd hello_django  
    # 通过venv创建python虚拟环境, 后一个venv是虚拟环境的目录名
    python -m venv venv  
    ```

5. 启动django项目

    ```python
    python manage.py runserver 8080
    ```

    这样我们的django就启动起来了！我们可以访问:http://127.0.0.1:8080

6. django基础必备三件套:

    - HttpResponse内部传入一个字符串参数,返回给浏览器。

        ```python
        from django.shortcuts import HttpResponse
        def index(request):
            # 业务逻辑代码
            return HttpResponse("hello,world!")
        ```

    - render除request参数外还接收一个待渲染的模板文件一个保存具体数据的字典参数,将数据填充进模板文件,最后把结果返回给浏览器。

        ```python
        from django.shortcuts import render
        
        def timer(request):
        	# 业务逻辑
            return render(request,"timer.html",{"date":ctime})
        ```

    - redirect 接受一个URL参数，表示跳转到指定的URL。

        ```python
        from django.shortcuts import redirect
        def index(request):
            # 业务逻辑代码
            return redirect("/home/")
        ```

### 13.4 静态文件配置

- settings.py写入下列代码

    ```python
    STATIC_URL = '/static/'  # 别名
    
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]
    ```

    ```python
    <link rel="stylesheet" href="/static/css/login.css">  # 以别名开头
    ```

    按照STATICFILES_DIRS列表的进行查找

    - html文件引入时导入的link标签路径是项目中的/static/文件名称下的插件
    - 在项目根目录创建static文件夹，包含常见的css,js,img,plugins等插件
    - 项目根目录static/app01文件夹存放css，js文件，jquery文件存放在app01目录下

* 示例：

  项目根目录static/app01文件夹存放css，js文件

  ```css
  h4{
      color: red;
  }
  ```

  ```js
  $('h4').click(function(){
      $(this).css('color','green')
  })
  ```

  模板文件 timer.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>静态文件</title>
      <!-- 引入jquery文件 -->
      <script src="/static/jquery-3.5.1.js"></script>
      <!-- 引入css文件 -->
      <link rel="stylesheet" href="/static/app01/timer.css">
  </head>
  <body>
      <h4>{{ timer }}</h4>
      <!-- 引入js文件 -->
      <script src="/static/app01/timer.js"></script>
  </body>
  </html>
  ```

### 13.5 路由配置

#### 13.5.1 路由配置---位置参数

```python
from django.contrib import admin
from django.urls import path, re_path
from frist_demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^articles/2003/$', views.special_case_2003),  # 以什么开头以什么结尾
    re_path(r'^articles/([0-9]{4})/$', views.year_archive),  # 结尾0-9传入四位数(/2019),传入两个参数,多对一
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),  # 结尾0-9传入四位数和2位数(/2019/06),传入3个参数,多对一
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail)  # 传入4个参数参数
]
```

```python
/articles/2003/  # 匹配第一个模式
/articles/2019/  # 匹配第二个模式
/articles/2019/06/  # 匹配第三个模式
/articles/2019/06/26/  # 匹配第四个模式
/articles/2019/6/  # 不匹配任何模式
```

注意:

- 参数要与列表中的写的参数匹配--比如(/articles/2019/3/)不匹配列表中的任何模式
- 每个正则表达式前面的'r' 是可选的但是建议加上,它告诉Python 这个字符串是“原始的”,都不应该转义

#### 13.5.2 路由配置---有名分组(关键字参数)

```python
from django.contrib import admin
from django.urls import path, re_path
from frist_demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive), 
]
```

```python
/articles/2019/06/ 请求将调用views.month_archive(request, year='2019', month='06')函数，而不是views.month_archive(request, '2019', '06').
```

这个实现与前面的示例完全相同，只有一个细微的差别：捕获的值作为关键字参数而不是位置参数传递给视图函数.

#### 13.5.3 路由配置---分发

导入include包

frist_demo.urls.py

```python
from django.contrib import admin
from django.urls import path, re_path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"app01/", include("app01.urls")) # 第一种
]
```

app01.urls.py

```python
from django.urls import path, re_path, include
from frist_demo import views

urlpatterns = [
    re_path(r'^articles/2003/$', views.special_case_2003),
    re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive), 
    re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive), 
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail) 
]
```

步骤：

- 把frist_demo.urls.py文件里的内容复制到app01.urls.py 文件里

- 在frist_demo.urls.py里导入include函数,匹配到app01/路径,找到urls文件

- 这样就可以通过http://127.0.0.1:8080/app01/articles/...匹配app01.py文件中urlpatterns列表中的模式了

    但是url地址中每次都需要输入app01,我们可以通过正则匹配,用第二种方法就可以实现

    ```js
    re_path(r"^", include("frist_demo.urls")) # 第二种
    ```

#### 13.5.4 路由配置---反向解析

##### 13.5.4.1 在模板中反向解析

login.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

{#模板语法之一反向解析{%  %}#}
<form action="{% url 'Log' %}" method="post">
    用户名 <input type="text" name="user">
    密码 <input type="pswd" name="pwd">
    <input type="submit">
</form>

</body>
</html>
```

urls.py

```python
from django.urls import path, re_path, include
from frist_demo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='Log')
]
```

views.py

```python
from django.shortcuts import render, HttpResponse
def login(request):

    print(request.method)
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print(request.POST)

        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == 'ike' and pwd == '123':
            return HttpResponse('success!')
        else:
            return HttpResponse('username or password error!')
```

- html 文件中以{%  %}语法匹配路径,html中路径不需要修改，永远都是获取最新的。
- urls文件中login路径可以随便修改，在html文件中永远获取到最新路径这就是反向解析。

##### 13.5.4.2 在脚本中反向解析

frist_demo.urls.py

```python
from django.urls import path, re_path, include
urlpatterns = [
	re_path(r"^", include("app01.urls"))
]
```

app01.urls.py

```python
from django.urls import path, re_path, include
from app01 import views

urlpatterns = [
    re_path(r'^articles/2003/$', views.special_case_2003, name='sc_2003'),  # 起个别名 name = 'sc_2003'
    re_path(r'^articles/([0-9]{4})/$', views.year_archive, name='y_a'),  # 起个别名
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive, name='y_m_d'),  # 起个别名
    re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail)
]
```

views.py

```python
from django.url import reverse
def special_case_2003(request):

    url = reverse('sc_2003')  # 反向解析
    url = reverse("y_a")  # 反向解析
    url = reverse(("y_m_d"))  # 反向解析
    print(url)
    return HttpResponse('special_case_2003')
```

在frist_demo.urls.py中给列表中的模块起个别名,就可以实现在脚本中反向解析

注意:

- views文件中反向解析后,不走return代码,直接反给自己的函数,也就是列表中模块的函数.

#### 13.5.5 路由控制---名称空间

命名空间（英语：Namespace）是表示标识符的可见范围,我们在开发项目时，会经常使用name属性反解出URL，当不小心在不同的app的urls中定义相同的name时，可能会导致URL反解错误，为了避免这种事情发生，引入了命名空间。
pro的urls.py

```python
from django.urls import path, re_path, include
urlpatterns = [
	re_path(r"^app01/", include(("app01.urls", 'app01'))),  # 取一个名称空间的别名app01
    re_path(r"^app02/", include(("app02.urls", 'app02'))),  # 取一个名称空间的别名app02

]
```

app01.urls

```python
from django.urls import path, re_path, include
from app01 import views
urlpatterns = [
    re_path("index/", views.index, name='index') # app01中的路由
]
```

app02.urls

```python
rom django.urls import path, re_path, include
from app02 import views
urlpatterns = [
        re_path("index/", views.index, name='index')  # app02中的路由
]
```

app01.views

```python
from django.shortcuts import render, HttpResponse
def index(request):
	return HttpResponse(reverse("app01:index"))  # 反转找到pro中的名称空间别名
```

app02.views

```python
from django.shortcuts import reverse, HttpResponse
def index(request):
    return HttpResponse(reverse("app02:index"))  # 反转找到pro中的名称空间别名
```

### 13.6 Django2.0版的path

#### 13.6.1 Django自带转换器

```python
urlpatterns = [
re_path('articles/(?P<year>[0-9]{4})/', views.year_archive),
re_path('article/(?P<article_id>[a-zA-Z0-9]+)/detail/', views.detail_view),
re_path('articles/(?P<article_id>[a-zA-Z0-9]+)/edit/', views.edit_view),
re_path('articles/(?P<article_id>[a-zA-Z0-9]+)/delete/', views.delete_view),
]
```

问题:

- 函数 year_archive 中year参数是字符串类型的，因此需要先转化为整数类型的变量值,在视图函数逻辑中year=int(year)就可以转换。有没有一种方法，在url中Django自动完成.
- 三个路由中article_id都是同样的正则表达式，但是你需要写三遍，当之后article_id规则改变后，需要同时修改三处代码，那么有没有一种方法，只需修改一处即可。

示例:

```python
from django.urls import path  
from . import views  
urlpatterns = [  
    path('articles/2003/', views.special_case_2003),  
    path('articles/<int:year>/', views.year_archive),  
    path('articles/<int:year>/<int:month>/', views.month_archive),  
    path('articles/<int:year>/<int:month>/<slug>/', views.article_detail),  
]
```

```python
def article_detail(request, year):
    print(year)
    print((type(year)))

    return HttpResponse('ok...')
```
基本规则:

- 使用尖括号(<>)从url中捕获值
- 捕获值中可以包含一个转化器类型（converter type），比如使用捕获一个整数变量。如果没有转化器，将匹配任何字符串，当然也包括了 / 字符
- 无需添加前导斜杠。比如:  articles/   前边不需要添加斜杠

Django默认支持以下5个转化器:

- str,匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式，类型为<class 'str'>
- int,匹配正整数，包含0，类型为<class 'int'>
- slug,匹配字母、数字以及横杠、下划线组成的字符串，类型为<class 'str'>
- uuid,匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00，这个基本上很少用，类型为<class 'uuid.UUID'>
- path,匹配任何非空字符串，包含了路径分隔符，类型为<class 'str'>

#### 13.6.2 注册自定义转换器

对于一些复杂或者复用的需要，可以定义自己的转化器。转化器是一个类或接口，它的要求有三点：

- regex 类属性，字符串类型
- to_python(self, value) 方法，value是由类属性 regex 所匹配到的字符串，返回具体的Python变量值，以供Django传递到对应的视图函数中。
- to_url(self, value) 方法，和 to_python 相反，value是一个具体的Python变量值，返回其字符串，通常用于url反向引用。

url_convert.py

```python
class MonConvert:
    regex = "[0-9]{2}"

    def to_python(self, value):
        return int(value)  # 转换为int类型

    def to_url(self, value):  # 反向解析
        return '%04d' % value
```

使用register_converter 将其注册到URL配置中

```python
from django.urls import re_path, path, register_converter
from frist_demo.url_convert import MonConvert
# 注册自定义url转换器
register_converter(MonConvert, "mm")
urlpatterns = [
	path("articles/<mm:month>", views.path_month)
]
```

path_month.py

```python
def path_month(request, month):
    print(month, type(month))

    return HttpResponse("path month...")
```

### 13.7 模板语法

#### 13.7.1 模板语法之变量

在Django模板中遍历复杂数据结构的关键是句点字符,语法:

```js
{{var_name}}
```

views.py

```python
from django.shortcuts import render
import datetime

# Create your views here.


def index(request):
    """
    模板语法:
        变量:{{}}
    :param request:
    :return:
    """
    name = 'ike'
    i = 10
    l = [11, 22, 33, 44]  # 列表
    info = {"name": "ike", "age": "23"}  # 字典
    b = True

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    alex = Person("alex", 333)  # 自定义类对象
    pq = Person("peiqi", 222)
    person_list = [pq, alex]
    date = datetime.date(2019, 6, 29)
    person_lis = []
return render(request, "index.html", locals())
```

index.html

```html
<p>字符串:{{ name }}</p>
<p>整型:{{ i }}</p>
<p>列表:{{ l }}</p>
<p>字典:{{ info }}</p>
<p>布尔:{{ b }}</p>
<p>类对象{{ alex }}</p>
<p>列表{{ person_list }}</p>
<p>日期:{{ date }}</p>

<hr>
<h3>深度查询</h3>
<p>{{ name }}</p>
<p>{{ i }}</p>
<p>{{ alex.name }}</p>
<p>{{ info.name }}</p>
<p>{{ person_list.1.name }}</p>
<p>{{ date.year }}</p>
```

注意:句点可以用来引用对象的方法,语法:

```python
<h2>dic.name.upper</h2>
```

#### 13.7.2 模板之过滤器{{}}

##### 13.7.2.1 date:日期

语法:

```python
{{obj|filter__name:param}}
```

例子:

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
    now = datetime.datetime.now()
    return render(request, "index.html", locals())
```

template-index.html

```python
<p>{{ now|date:'Y-m-d' }}</p>
```

##### 13.7.2.2 default:输出

语法:

```python
{{ value|default:"nothing" }}
```

如果一个变量True使用变量的值,否则使用给定的值,例如：

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
    person_lis = []
    return render(request, "index.html", locals())
```

index.html

```python
<p>{{ person_lis|default:'是一个空列表' }}</p>
```

##### 13.7.2.3 length:长度

语法:

```python
{{ value|length }}
```

返回数据类型的长度,例如:

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
    len = {1, 2, 3, 6}
    return render(request, "index.html", locals())
```

index.html

```html
<p>长度:{{ len|length }}</p>
```

##### 13.7.2.4 slice:切片

语法:

```python
{{ value|slice:"2:-1" }}
```

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
    len = {[11, 22, 33, 44]
    return render(request, "index.html", locals())	
```

index.html

```html
<p>{{ len|slice:'::2' }}</p>
```

##### 13.7.2.5 truncatechars:截断

语法:

```html
{{ value|truncatechars:9 }}
```

如果字符串很长想要截断,就可以用truncatechars实现,截断的字符串将以可翻译的省略号序列（“...”）结尾.

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
    truncate_str = 'hello python world use it'
    return render(request, "index.html", locals())	
```

template-index.html

```html
{#截断字符#}
<p>{{ truncate_str|truncatechars:6 }}</p>
{#阶段单词#}
<p>{{ truncate_str|truncatewords:2 }}</p>
```

##### 13.7.2.6 filesizeformat:文件大小

语法:

```python
{{value|filesizeformat}}
```

获取文件大小,例如:
views.py

```python
from django.shortcuts import render
import datetime
def index(request):
    file_size = 123456
    return render(request, "index.html", locals())	
```

template-index.html

```python
<p>{{ file_size|filesizeformat }}</p>
```

##### 13.7.2.7 safe:关闭转义

语法:

```python
{{ value|safe}}
```

Django中关闭HTML的自动转义,例如:

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
    link = "<a href>click</a>"
    return render(request, "index.html", locals())	
```

template-index.html

```python
<p>{{ link|safe }}</p>
```

#### 13.7.3 模板之标签{% %}

##### 13.7.3.1 for标签

遍历每一个元素,例如：

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
    l = [11, 22, 33, 44]  # 列表
    info = {"name": "ike", "age": "23"}  # 字典
    return render(request, "index.html", locals())	
```

template-index.html

```python
<h3>for循环标签--列表</h3>
{% for i in l %}
    <p>{{ i }}</p>
{% endfor %}

<h3>for循环标签--字典</h3>
{% for k,v in info.items %}
    <p>{{ k }}:{{ v }}</p>
{% endfor %}
```

可以利用`{% for obj in list reversed %}`反向完成循环.

注：循环序号可以通过｛｛forloop｝｝显示

```python
forloop.counter            The current iteration of the loop (1-indexed)
forloop.counter0           The current iteration of the loop (0-indexed)
forloop.revcounter         The number of iterations from the end of the loop (1-indexed)
forloop.revcounter0        The number of iterations from the end of the loop (0-indexed)
forloop.first              True if this is the first time through the loop
forloop.last               True if this is the last time through the loop
```

例子:

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
    l = [11, 22, 33, 44]  # 列表
    info = {"name": "ike", "age": "23"}  # 字典
    return render(request, "index.html", locals())	
```

template-index.html

```html
<h3>for循环标签--列表</h3>
{% for i in l %}
    <p>{{ forloop.counter }} {{ i }}</p>
{% endfor %}

<h3>for循环标签--字典</h3>
{% for k,v in info.items %}
    <p>{{ forloop.counter0 }}{{ k }}:{{ v }}</p>
{% endfor %}
```

for ... empty:

for 标签带有一个可选的`{% empty %}` 从句，以便在给出的组是空的或者没有被找到时，可以有所操作.

```python
{% for person in null_list %}
    <p>{{ forloop.counter0 }} {{ person.name }},{{ person.age }}</p>
    {% empty %}
    <p>列表为空</p>
{% endfor %}
```

##### 13.7.3.2 if 标签

`{% if %}`会对一个变量求值，如果它的值是“True”（存在、不为空、且不是boolean类型的false值），对应的内容块会输出.

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
	num = 60
    return render(request, "index.html", locals())	
```

template-index.html

```html
{% if num > 100 or num < 0 %}
    <p>无效</p>
{% elif num > 80 and num < 100 %}
    <p>优秀</p>
{% else %}
    <p>凑活吧</p>
{% endif %}
```

##### 13.7.3.3 with标签

给复杂的变量起个别名

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
	num = 60
    return render(request, "index.html", locals())	
```

template-index.html

```html
{% with info.name as num %}
    {{ num }}

{% endwith %}
```

##### 13.7.3.4 csrf_token标签

Django中间件拦截,无法访问POST请求,用这个标签通过拦截

这个标签用于跨站请求伪造保护

views.py

```python
def login(request):
    if request.method == 'POST':
        return HttpResponse('OK')
    return render(request, 'login.html')
```

template-login.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<form action="" method="post">
    {% csrf_token %}
    用户名:<input type="text" name="user">
    密码: <input type="text" name="pwd">
    <input type="submit">
</form>
</body>
</html>
```

#### 13.7.4 自定义标签和过滤器

- 在settings中的INSTALLED_APPS配置当前app,不然Django无法找到自定义的simple_tag.
- 在app中创建templatetags模块(注:模块名只能是templatetags)
- 创建一个.py文件,比如:my_tag.py

settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01'
]
```

my_tag.py

```python
# 自定义一个标签

from django import template

# 必须是这个变量
register = template.Library()


# 自定义过滤器:
@register.filter
def multi_filter(x, y):
    return x * y


# 自定义标签
@register.simple_tag()
def multi_tag(x, y, z):
    return x * y * z
```

template-login.html

```js
<hr>
<h3>自定义过滤器调用</h3>
{#导包my_tag_filte.py#}
{% load my_tag %}

{#过滤器只能实现两个参数#}
<p>{{ i|multi_filter:20 }}</p>

<hr>
<h3>自定义标签调用</h3>
{#自定义标签可以是多个参数#}
{% multi_tag 7 9 8%}

<hr>
<h3>自定义过滤器可以用于if流程判断,自定义标签不可以</h3>
{% if i|multi_filter:20 > 100 %}
    <p>100</p>
{% else %}
    <p>{{ i }}</p>

{% endif %}
```

注意:自定义过滤器可以用于if流程判断,自定义标签不可以

#### 13.7.5 模板继承

Django模版引擎中最强大也是最复杂的部分就是模版继承了.模版继承可以让您创建一个基本的“骨架”模版,它包含您站点中的全部元素,并且可以定义能够被子模版覆盖的 blocks.

advertise.html---带标题的面板

```html
<div class="action">
    <div class="panel panel-danger">
        <div class="panel-heading">Panel heading without title</div>
        <div class="panel-body">
            Panel content
        </div>
    </div>
    <div class="panel panel-warning">
        <div class="panel-heading">Panel heading without title</div>
        <div class="panel-body">
            Panel content
        </div>
    </div>
    <div class="panel panel-success">
        <div class="panel-heading">Panel heading without title</div>
        <div class="panel-body">
            Panel content
        </div>
    </div>
</div>
```

base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {#在base中加的block越多越好#}
    {% block title %}

    {% endblock %}
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .header {
            width: 100%;
            height: 50px;
            background: #369;
        }
    </style>
</head>
<body>

<div class="header"></div>
<div class="container">
    <div class="row">
        <div class="col-md-3">
            {#导入advertise.html#}
            {% include 'advertise.html' %}
        </div>
        <div class="col-md-9">
            {% block con %}
                <h1>content</h1>
            {% endblock %}
        </div>
    </div>
</div>


</body>
</html>
```

这个模板,我们叫做base.html,它定义类一个简单的html骨架,这也是父模板,子模板可以通过block继承父模板的内容.

index.html

```js
{#extends必须是第一个标签#}
{% extends 'base.html' %}

{% block title %}
    <title>orders标签</title>
{% endblock %}

{% block con %}
    {#加载父类block内容#}
    {{ block.super }}
    <h1>订单</h1>
{% endblock con %}
```

extends 标签是这里的关键,它告诉模版引擎，这个模版“继承”了另一个模版,当模版系统处理这个模版时，

- 首先，它将定位父模版——在此例中，就是“base.html”
- 版引擎将注意到 base.html 中的两个 block 标签,并用子模版中的内容来替换这些block

使用继承的提示:

- 如果你在模版中使用 `{% extends %}` 标签，它必须是模版中的第一个标签.其他的任何情况下，模版继承都将无法工作.

- 在base模版中设置越多的 `{% block %}` 标签越好.如果子模板不填充block内容,就会继承父模板中block内容,所以在继承父模板中的block内容我们可以看情况填充.

- 如果在模板中存在很多重复性的内容,那就意味着我们可以把这些内容单独提取出来,父模板中的`{% block %}` 定义后,然后在子模版中去调用重复内容.

- 继承父模板block的内容,我们在写的时候不想把父模板内容覆盖掉,我们可以在子模板写入`{{ block.super }}`,继保留了父模板的内容,也写入了子模板的内容.

- 为了更好的可读性,你也可以给你的`{% endblock %}` 标签一个 名字 .例如：

    ```js
    {% block content %}
    ...
    {% endblock content %}
    ```

- 不能在一个模板中定义多个相同的block标签.

### 13.8 视图函数

一个视图函数,简称视图,是一个简单的Python函数,它接收web请求并返回web响应.响应有多种方式,可以是HTML文件,一个重定向,一张图片等等.

注意:

- 无论视图本身包含什么逻辑,都要返回响应
- 视图函数代码写到哪里没有要求,只要在Python目录下就可以
- 为了代码整洁性以及可读性,程序员约定将试图函数放到views.py文件中

urls.py

```python
from django.contrib import admin
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"index/", views.index),
    re_path(r'login/', views.login)
]
```

views.py

```python
from django.shortcuts import HttpResponse, render, redirect
def index(request):
    print('请求方法:', request.method)
    import time
    ctime = time.time()
    return render(request, 'index.html', {"timer": ctime})
```

代码解释:

- 我们从 django.shortcuts模块导入了HttpResponse类,以及Python的time库
- 定义了index函数,它就是一个视图函数,函数名与urls.py文件中导入的文件名要一致,两个文件要互相映射,函数名定义一定要见名知意
- 视图会返回一个HttpResponse对象,其中包含生成的响应

#### 13.8.1. HttpReques对象

request属性:

Django将请求报文中的请求头,请求行,以及请求体封装成request类中的属性.除了特殊说明的之外,其他均为只读的.

```python
'''
1.request.GET
　　获取到一个类似于字典的对象,包含HTTP GET的所有参数。
2.request.POST
　　获取到一个类似于字典的对象,包含HTTP POST的所有参数
　　POST请求可以带有空的POST字典,如果通过HTTP POST方法发送一个表单,但是表单中没有任何的数据,QueryDict对象依然会被创建。因此,不应该使用if request.POST来检查使用的是否是POST方法;应该使用if request.method == "POST"
另外:如果使用POST上传文件的话，文件信息将包含在 FILES 属性中。
    注意:键值对的值是多个的时候,比如checkbox类型的input标签,select标签,需要用:
request.POST.getlist("hobby")获取值
3.request.body
　　获取到一个字符串,代表请求报文的主体.在处理非HTTP形式的报文时非常有用，例如：二进制图片、XML,Json等。
　　但是，如果要处理表单数据的时候,推荐还是使用 request.POST .
4.request.path
　　获取到一个字符串,表示请求的路径组件（不含域名和get请求参数）.
　　例如："/music/bands/the_beatles/"
5.request.get_full_path
	获取到一个字符串,表示请求的路径组件,包含get请求参数.
6.request.method
　　获取到一个字符串，表示请求使用的HTTP方法.必须使用大写。
　　例如："GET"、"POST"
7.request.encoding
　　获取到一个字符串,表示提交的数据的编码方式（如果为 None 则表示使用 DEFAULT_CHARSET 的设置，默认为 'utf-8'）。
   这个属性是可写的，你可以修改它来修改访问表单数据使用的编码。
   接下来对属性的任何访问（例如从 GET 或 POST 中读取数据）将使用新的 encoding 值。
   如果你知道表单数据的编码不是 DEFAULT_CHARSET ，则使用它。
8.request.META
 　　获取到一个标准的Python字典,包含所有的HTTP头部.具体的头部信息取决于客户端和服务器，下面是一些示例：
    CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
    CONTENT_TYPE —— 请求的正文的MIME 类型。
    HTTP_ACCEPT —— 响应可接收的Content-Type。
    HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
    HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
    HTTP_HOST —— 客服端发送的HTTP Host 头部。
    HTTP_REFERER —— Referring 页面。
    HTTP_USER_AGENT —— 客户端的user-agent 字符串。
    QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。
    REMOTE_ADDR —— 客户端的IP 地址。
    REMOTE_HOST —— 客户端的主机名。
    REMOTE_USER —— 服务器认证后的用户。
    REQUEST_METHOD —— 一个字符串，例如"GET" 或"POST"。
    SERVER_NAME —— 服务器的主机名。
    SERVER_PORT —— 服务器的端口（是一个字符串）。
 　　从上面可以看到，除 CONTENT_LENGTH 和 CONTENT_TYPE 之外，请求中的任何 HTTP 首部转换为 META 的键时，
    都会将所有字母大写并将连接符替换为下划线最后加上 HTTP_  前缀。
    所以，一个叫做 X-Bender 的头部将转换成 META 中的 HTTP_X_BENDER 键。
9.request.FILES
　　获取到一个类似于字典的对象，包含所有的上传文件信息。
   FILES 中的每个键为<input type="file" name="" /> 中的name，值则为对应的数据。
　　注意，FILES 只有在请求的方法为POST 且提交的<form> 带有enctype="multipart/form-data" 的情况下才会
   包含数据。否则，FILES 将为一个空的类似于字典的对象。
10.request.COOKIES
　　获取到一个标准的Python 字典，包含所有的cookie。键和值都为字符串。
11.request.session
 　　一个既可读又可写的类似于字典的对象，表示当前的会话。只有当Django 启用会话的支持时才可用。
12.request.user(用户认证组件下使用)
　　一个 AUTH_USER_MODEL 类型的对象，表示当前登录的用户。
　　如果用户当前没有登录，user 将设置为 django.contrib.auth.models.AnonymousUser 的一个实例。你可以通过 is_authenticated() 区分它们。
    例如：
    if request.user.is_authenticated():
        # Do something for logged-in users.
    else:
        # Do something for anonymous users.
     　　user 只有当Django 启用 AuthenticationMiddleware 中间件时才可用。
     -------------------------------------------------------------------------------------
    匿名用户
    class models.AnonymousUser
    django.contrib.auth.models.AnonymousUser 类实现了django.contrib.auth.models.User 接口，但具有下面几个不同点：
    id 永远为None。
    username 永远为空字符串。
    get_username() 永远返回空字符串。
    is_staff 和 is_superuser 永远为False。
    is_active 永远为 False。
    groups 和 user_permissions 永远为空。
    is_anonymous() 返回True 而不是False。
    is_authenticated() 返回False 而不是True。
    set_password()、check_password()、save() 和delete() 引发 NotImplementedError。
    New in Django 1.8:
    新增 AnonymousUser.get_username() 以更好地模拟 django.contrib.auth.models.User。
'''
```

request常用方法:

```python
'''
1.request.get_full_path()
　　返回path,如果可以将加上查询字符串。
　　例如："/music/bands/the_beatles/?print=true"
2.request.is_ajax()
　　如果请求是通过XMLHttpRequest发起的，则返回True，方法是检查 HTTP_X_REQUESTED_WITH 相应的首部是否是字符串'XMLHttpRequest'。
　　大部分现代的 JavaScript 库都会发送这个头部。如果你编写自己的 XMLHttpRequest 调用（在浏览器端）,你必须手工设置这个值来让is_ajax()可以工作。
　　如果一个响应需要根据请求是否是通过AJAX 发起的，并且你正在使用某种形式的缓存例如Django 的 cache middleware，
   你应该使用 vary_on_headers('HTTP_X_REQUESTED_WITH') 装饰你的视图以让响应能够正确地缓存。
'''
```

#### 13.8.2 HttpResponse对象

响应对象主要有三种形式：

- HttpResponse() 

    - 括号内直接跟一个具体的字符串作为响应体，比较直接很简单.

- render() 

    - 就是将一个模板页面中的模板语法进行渲染，最终渲染成一个html页面作为响应体

    ```python
    return render(request, 'template_name', {"context": context})
    # 返回一个渲染后的HttpResponse对象和给定的模板和一个给定的上下文字典。
    ```

    参数:

    - request： 用于生成响应的请求对象。
    - template_name：要使用的模板的完整名称，可选的参数
    - context：添加到模板上下文的一个字典。默认是一个空字典。如果字典中的某个值是可调用的，视图将在渲染模板之前调用它。

- redirect()

    - 传递要重定向的一个硬编码的URL

        ```python
        def cs_login(request):
            render_url = reverse('render')
            print(render_url)
            if request.method == 'POST':
                if request.POST.get('user') == 'Joker' and request.POST.get('password') == '123':
                    # 重定向
                    return redirect(render_url)
                else:
                    return HttpResponse('username or password error!')
        return render(request, 'app03/login.html')
        ```

    补充:
    
    ```python
    '''
    1.301和302的区别。
    301和302状态码都表示重定向，就是说浏览器在拿到服务器返回的这个状态码后会自动跳转到一个新的URL地址，这个地址可以从响应的Location首部中获取.(用户看到的效果就是他输入的地址A瞬间变成了另一个地址B)——这是它们的共同点。他们的不同在于。
    301表示旧地址A的资源已经被永久地移除了（这个资源不可访问了），搜索引擎在抓取新内容的同时也将旧的网址交换为重定向之后的网址；
    302表示旧地址A的资源还在（仍然可以访问），这个重定向只是临时地从旧地址A跳转到地址B，搜索引擎会抓取新的内容而保存旧的网址。 
    所以302好于301
    2.重定向原因：
    （1）网站调整（如改变网页目录结构）；
    （2）网页被移到一个新地址；
    （3）网页扩展名改变(如应用需要把.php改成.Html或.shtml)。
    这种情况下，如果不做重定向，则用户收藏夹或搜索引擎数据库中旧地址只能让访问客户得到一个404页面错误信息，访问流量白白丧失；再者某些注册了多个域名的网站，也需要通过重定向让访问这些域名的用户自动跳转到主站点等。
    '''
    ```

### 13.9 ORM

#### 13.9.1 ORM简介

对象关系映射（Object Relational Mapping，简称ORM）模式是一种为了解决面向对象与关系数据库存在的互不匹配的现象的技术.

- ORM是通过使用描述对象和数据库之间映射的元数据，将程序中的对象自动持久化到关系数据库中
- 一种简单的方案是采用硬编码方式，为每一种可能的数据库访问操作提供单独的方法,ORM提供了对数据库的映射,不用直接编写SQL代码,只需操作对象就能对数据库操作数据

ORM的方法论基于三个核心原则： 

- 简单：以最基本的形式建模数据。
- 传达性：数据库结构被任何人都能理解的语言文档化
- 精确性：基于数据模型创建正确标准化了的结构。 

![1639297421284](J:\homework\Python学习笔记\Python_notes.assets\1639297421284.png)

```python
#sql中的表                                                      

#创建表:
CREATE TABLE employee(                                     
	d INT PRIMARY KEY auto_increment ,                    
	name VARCHAR (20),                                     
	gender BIT default 1,                                  
	birthday DATA ,                                         
	department VARCHAR (20),                               
	salary DECIMAL (8,2) unsigned,                         
	);
#sql中的表纪录                                                  
#添加一条表纪录:                                                         
INSERT employee (name,gender,birthday,salary,department)         
VALUES   ("alex",1,"1985-12-12",8000,"保洁部");               
#查询一条表纪录:                                                           
SELECT * FROM employee WHERE age=24;                               
#更新一条表纪录:                                                           
UPDATE employee SET birthday="1989-10-24" WHERE id=1;              
#删除一条表纪录:                                                          
DELETE FROM employee WHERE name="alex"                             
# python的类
class Employee(models.Model):
     id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=32)
     gender=models.BooleanField()
     birthday=models.DateField()
     department=models.CharField(max_length=32)
     salary=models.DecimalField(max_digits=8,decimal_places=2)
# python的类对象
#添加一条表纪录:
emp=Employee(name="alex",gender=True,birthday="1985-12-12",epartment="保洁部")
emp.save()
ret=Employee.objects.create(name="alex",gender=True,birthday="1985-12-12",epartment="保洁部")
print(ret.name)
print(ret.gender)
#查询一条表纪录:
Employee.objects.filter(age=24)
#更新一条表纪录:
Employee.objects.filter(id=1).update(birthday="1989-10-24")
#删除一条表纪录:
Employee.objects.filter(name="alex").delete()
```

#### 13.9.2 Django使用mysql数据库

1. 创建模型

在工程下新建app01项目,在项目下的models.py中创建模型:

```python
from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 自增,主键
    title = models.CharField(max_length=32, unique=True)  # varchar类型,唯一约束
    pub_date = models.DateField()  # 存日期
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 浮点型,最大八位保留两位小数
    publish = models.CharField(max_length=32)  # varchar类型

    def __str__(self):
        return self.title
```

2. 字段

    ```python
    '''
    <1> CharField
    	字符串字段, 用于较短的字符串.
        CharField 要求必须有一个参数 maxlength, 用于从数据库层和Django校验层限制该字段所允许的最大字符数.
    <2> IntegerField
    	#用于保存一个整数.
    <3> FloatField
    	一个浮点数. 必须 提供两个参数:
            [参数]             [描述]
            max_digits    总位数(不包括小数点和符号)
            decimal_places    小数位数
            举例来说, 要保存最大值为 999 (小数点后保存2位),你要这样定义字段:
                models.FloatField(..., max_digits=5, decimal_places=2)
                要保存最大值一百万(小数点后保存10位)的话,你要这样定义:
                    models.FloatField(..., max_digits=19, decimal_places=10)
                    admin 用一个文本框(<input type="text">)表示该字段保存的数据.
    <4> AutoField
    	一个 IntegerField, 添加记录时它会自动增长. 你通常不需要直接使用这个字段;
    	自定义一个主键：my_id=models.AutoField(primary_key=True)
    	如果你不指定主键的话,系统会自动添加一个主键字段到你的 model.
    <5> BooleanField
    	true/false field. admin 用 checkbox 来表示此类字段.
    <6> TextField
    	一个容量很大的文本字段.
        admin 用一个 <textarea> (文本区域)表示该字段数据.(一个多行编辑框).
    <7> EmailField
    	一个带有检查Email合法性的 CharField,不接受 maxlength 参数.
    <8> DateField
    	一个日期字段. 共有下列额外的可选参数:
            Argument    描述
            auto_now    当对象被保存时,自动将该字段的值设置为当前时间.通常用于表示 "last-modified" 时间戳.
            auto_now_add    当对象首次被创建时,自动将该字段的值设置为当前时间.通常用于表示对象创建时间.
            （仅仅在admin中有意义...)
    <9> DateTimeField
    	一个日期时间字段. 类似 DateField 支持同样的附加选项.
    <10> ImageField
    	类似 FileField, 不过要校验上传对象是否是一个合法图片.#它有两个可选参数:height_field和width_field,
        如果提供这两个参数,则图片将按提供的高度和宽度规格保存.    
    <11> FileField
        一个文件上传字段.
        要求一个必须有的参数: upload_to, 一个用于保存上载文件的本地文件系统路径. 这个路径必须包含 strftime #formatting,
        该格式将被上载文件的 date/time
        替换(so that uploaded files don't fill up the given directory).
        admin 用一个<input type="file">部件表示该字段保存的数据(一个文件上传部件) .
        注意：在一个 model 中使用 FileField 或 ImageField 需要以下步骤:
           （1）在你的 settings 文件中, 定义一个完整路径给 MEDIA_ROOT 以便让 Django在此处保存上传文件.
           (出于性能考虑,这些文件并不保存到数据库.) 定义MEDIA_URL 作为该目录的公共 URL. 要确保该目录对
           WEB服务器用户帐号是可写的.
           （2） 在你的 model 中添加 FileField 或 ImageField, 并确保定义了 upload_to 选项,以告诉 Django
           使用 MEDIA_ROOT 的哪个子目录保存上传文件.你的数据库中要保存的只是文件的路径(相对于 MEDIA_ROOT).
           出于习惯你一定很想使用 Django 提供的 get_<#fieldname>_url 函数.举例来说,如果你的 ImageField
           叫作 mug_shot, 你就可以在模板中以 {{ object.#get_mug_shot_url }} 这样的方式得到图像的绝对路径.
    <12> URLField
         用于保存 URL. 若 verify_exists 参数为 True (默认), 给定的 URL 会预先检查是否存在( 即URL是否被有效装入且没有返回404响应).
         admin 用一个 <input type="text"> 文本框表示该字段保存的数据(一个单行编辑框)
    <13> NullBooleanField
          类似 BooleanField, 不过允许 NULL 作为其中一个选项. 推荐使用这个字段而不要BooleanField 加 null=True 选项
          admin 用一个选择框 <select> (三个可选择的值: "Unknown", "Yes" 和 "No" ) 来表示这种字段数据.
    <14> SlugField
    	"Slug" 是一个报纸术语. slug 是某个东西的小小标记(短签), 只包含字母,数字,下划线和连字符.
    	#它们通常用于URLs若你使用 Django 开发版本,你可以指定 maxlength. 若 maxlength 未指定, Django 会使用默认长度: 50.  
    	#在以前的 Django 版本,没有任何办法改变50 这个长度.这暗示了 db_index=True.它接受一个额外的参数: prepopulate_from, which is a list of fields from which to auto-#populate the slug, via JavaScript,in the object's admin form: models.SlugField(prepopulate_from=("pre_name", "name"))prepopulate_from 不接受 DateTimeFields.
    <13> XMLField
    	一个校验值是否为合法XML的 TextField,必须提供参数: schema_path, 它是一个用来校验文本的 RelaxNG schema #的文件系统路径.
    <14> FilePathField
           可选项目为某个特定目录下的文件名. 支持三个特殊的参数, 其中第一个是必须提供的.
           参数    描述
           path    必需参数. 一个目录的绝对文件系统路径. FilePathField 据此得到可选项目.
           Example: "/home/images".
           match    可选参数. 一个正则表达式, 作为一个字符串, FilePathField 将使用它过滤文件名.
           注意这个正则表达式只会应用到 base filename 而不是
           路径全名. Example: "foo.*\.txt^", 将匹配文件 foo23.txt 却不匹配 bar.txt 或 foo23.gif.
           recursive可选参数.要么 True 要么 False. 默认值是 False. 是否包括 path 下面的全部子目录.
           这三个参数可以同时使用.
           match 仅应用于 base filename, 而不是路径全名. 那么,这个例子:
           FilePathField(path="/home/images", match="foo.*", recursive=True)
           ...会匹配 /home/images/foo.gif 而不匹配 /home/images/foo/bar.gif
    <15> IPAddressField
           一个字符串形式的 IP 地址, (i.e. "24.124.1.30").
    <16> CommaSeparatedIntegerField
           用于存放逗号分隔的整数值. 类似 CharField, 必须要有maxlength参数.
    '''
    ```

3. 参数

    ```python
    '''
    (1)null
    如果为True，Django 将用NULL 来在数据库中存储空值。 默认值是 False.
    (2)blank
    如果为True，该字段允许不填。默认为False。
    要注意，这与 null 不同。null纯粹是数据库范畴的，而 blank 是数据验证范畴的。
    如果一个字段的blank=True，表单的验证将允许该字段是空值。如果字段的blank=False，该字段就是必填的。
    (3)default
    字段的默认值。可以是一个值或者可调用对象。如果可调用 ，每有新对象被创建它都会被调用。
    (4)primary_key
    如果为True，那么这个字段就是模型的主键。如果你没有指定任何一个字段的primary_key=True，
    Django 就会自动添加一个IntegerField字段做为主键，所以除非你想覆盖默认的主键行为，
    否则没必要设置任何一个字段的primary_key=True。
    (5)unique
    如果该值设置为 True, 这个数据字段的值在整张表中必须是唯一的
    (6)choices
    由二元组组成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项。 如果设置了choices ，默认的表单将是一个选择框而不是标准的文本框，<br>而且这个选择框的选项就是choices 中的选项。
    '''
    ```

4. settings配置

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':'bms',     　　 　  # 要连接的数据库，连接前需要创建好
            'USER':'root',　　　　　　  # 连接数据库的用户名
            'PASSWORD':'',　　　　　　  # 连接数据库的密码
            'HOST':'127.0.0.1',       # 连接主机，默认本级
            'PORT'：3306    　　　     #  端口 默认3306
        }
    }
    ```

    注意1：

    NAME即数据库的名字，在mysql连接前该数据库必须已经创建，而上面的sqlite数据库下的db.sqlite3则是项目自动创建 USER和PASSWORD分别是数据库的用户名和密码。设置完后，再启动我们的Django项目前，我们需要激活我们的mysql。然后，启动项目，会报错：no module named MySQLdb 。这是因为django默认你导入的驱动是MySQLdb，可是MySQLdb 对于py3有很大问题，所以我们需要的驱动是PyMySQL 所以，我们只需要找到项目名文件下的**init**,在里面写入:

    ```python
    import pymysql
    pymysql.install_as_MySQLdb()
    ```

    最后通过两条数据库迁移命令即可在指定的数据库中创建表:

    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```

    注意2:

    确保配置文件中的INSTALLED_APPS中写入我们创建的app名称

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        "book"
    ]
    ```

    注意3:

    如果报错如下

    ```python
    django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.3 or newer is required; you have 0.7.11.None
    ```

    MySQLclient目前只支持到python3.4，因此如果使用的更高版本的python，需要修改如下：

    找到F:\program\python36\Lib\site-packages\django\db\backends\mysql路径注释掉下面代码

    ```python
    if version < (1, 3, 3):
         raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)
    ```

    注意4: 

    如果想打印orm转换过程中的sql，需要在settings中进行如下配置:

    ```python
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console':{
                'level':'DEBUG',
                'class':'logging.StreamHandler',
            },
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['console'],
                'propagate': True,
                'level':'DEBUG',
            },
        }
    }
    ```

#### 13.9.3 单表操作

新建数据:

```python
# =======================添加表记录=======================

# 方式一:
book_obj = Book(id=1, title='Python红宝书', price=100, pub_date='2019-06-29', publish='人民出版社')
book_obj.save()

# 方式二: create返回值就是当前生成的对象记录,也就是表添加的记录
book_obj = Book.objects.create(title='Linux黄宝书', price=200, pub_date='2019-06-30', publish='人民出版社')
print(book_obj.title, book_obj.price)
```

查询数据:

```python
# =======================查询表记录API====================
'''
1.方法的返回值
2.方法的调用者
:param request:
:return:
'''
# 1.all方法:返回值一个queryset对象
book_list = Book.objects.all()
print(book_list)  # <QuerySet [<Book: Python红宝书>, <Book: Linux蓝宝书>]>
for i in book_list:
    print(i.title, i.price)

    print(book_list[1].title)

# 2.first,last 调用者:queryset对象  返回值:model对象
book = Book.objects.all().first()  # book = Book.objects.all()[0]
book = Book.objects.all().last()  # # book = Book.objects.all()[-1]

# 3.filter  调用者:queryset对象  返回值:queryset对象
book_list = Book.objects.filter(price=100)  # all取到的全部的数据,filter取到的是筛选后的数据
book1 = Book.objects.filter(price=100).first()

# 4.get  有且只有一个查询结果时才有意义,否则会报错  返回值:model对象
book_obj = Book.objects.get(price=136)
print(book_obj)

# 5.exclude  排除满足条件的数据  调用者:queryset对象  返回值:queryset对象
book1 = Book.objects.exclude(price=136)
print(book1)

# 6.order_by排序  调用者:queryset对象  返回值:queryset对象
res = Book.objects.all().order_by('-price')  # order_by('-price')为降序排  默认为升序
print(res)

# 7.rereverse对查询结果反向排序  调用者:queryset对象  返回值:queryset对象
res = Book.objects.all().order_by('-price').reverse()
print(res)

# 8.count统计  调用者:queryset对象 返回值:int
res = Book.objects.all().count()
print(res)

# 9.exist判读是否包含  调用者:queryset对象 返回值:bool
res = Book.objects.all().exists()
print(res)
if res:
    print('OK~~~')

# 10.values  调用者:queryset对象  返回值:queryset对象
res = Book.objects.all().values('price', 'title')
print(res)  # <QuerySet [{'price': Decimal('100.00')}, {'price': Decimal('136.00')}, {'price': Decimal('100.00')}]>

"""
temp = []
for obj in Book.object.all()
	temp.append({
    "price": obj.price
    "title": obj.title
    })
    """

# 11.valuse_list  调用者:queryset对象  返回值:queryset对象
res = Book.objects.all().values_list('price')
print(res)  # <QuerySet [(Decimal('100.00'),), (Decimal('136.00'),), (Decimal('100.00'),)]>

"""
values:
   <QuerySet [{'price': Decimal('100.00')}, {'price': Decimal('136.00')}, {'price': Decimal('100.00')}]>
values_list:
   <QuerySet [(Decimal('100.00'),), (Decimal('136.00'),), (Decimal('100.00'),)]>
"""

# 12.distinct去重  调用者:queryset对象  返回值:queryset对象
res = Book.objects.all().values_list('price').distinct()
print(res)
```

模糊查询:

```python
# =======================查询表记录之模糊查询====================
res = Book.objects.filter(price__gt=100, price__lt=200)
print(res)
res = Book.objects.filter(title__endswith='书')  # 以什么结尾,title__startswith同理
print(res)
res = Book.objects.filter(title__contains='n')  # 包含，精确查询
print(res)
res = Book.objects.filter(title__icontains='l')  # 包含，不区分大小写
print(res)
res = Book.objects.filter(price__in=[100, 136])  # 满足这几个条件
print(res)
res = Book.objects.filter(pub_date__year=2019, pub_date__month=6)  # 日期查询
print(res)
```

删除数据:

```python
# =======================删除记录和修改记录=======================
# 1.delete 删除  调用者:queryset对象 model对象
res = Book.objects.filter(price=136).delete()
print(res)  # (1, {'app01.Book': 1})个数以及表的个数

Book.objects.filter(price=100).first().delete()

```

修改数据:

```python
# 1.update修改  调用者:queryset对象
Book.objects.filter(title='Go黄宝书').update(title='人生苦短!go')
```

#### 13.9.4 Django中mysql数据库使用步骤总结:

- 1.创建一个mysql数据库; 

    ```sqlite
    creat database 数据库名;
    ```

- 2.在setting中配置,Django 链接Mysql数据库,INSTALLED_APPS中写入我们创建的app名称;

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':'bms',     　　 　  # 要连接的数据库，连接前需要创建好
            'USER':'root',　　　　　　  # 连接数据库的用户名
            'PASSWORD':'',　　　　　　  # 连接数据库的密码
            'HOST':'127.0.0.1',       # 连接主机，默认本级
            'PORT'：3306    　　　     #  端口 默认3306
            'OPTIONS': {'isolation_level': None}
        }
    }
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        "book"
    ]
    ```

- 3.在项目的__init__文件夹中写入代码;

    ```python
    import pymysql
    pymysql.install_as_MySQLdb()
    ```

- 4.创建表(在app01下的models.py中写类,建表语句);

    ```python
    from django.db import models
    
    # Create your models here.
    
    
    class Book(models.Model):
        id = models.AutoField(primary_key=True)  # 自增,主键
        title = models.CharField(max_length=32, unique=True)  # varchar类型,唯一约束
        pub_date = models.DateField()  # 存日期
        price = models.DecimalField(max_digits=8, decimal_places=2)  # 浮点型,最大八位保留两位小数
        publish = models.CharField(max_length=32)  # varchar类型
        
        class Meta:
            # 设置表名
            db_table = 'tb_students'
            managed = True
            verbose_name = '书籍信息'
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return self.title
    ```

- 5.执行数据迁移两条命令;

    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```

- 6.urls.py文件中设计url;

    ```python
    from django.contrib import admin
    from django.urls import path, re_path
    from app01 import views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('addbook/', views.addbook),
        path('books/', views.books),
        re_path(r"books/(\d+)/delete", views.delbook),  # delbook(request,1)
        re_path(r"books/(\d+)/change", views.changebook),  # delbook(request,1)
    ]
    ```

- 7.views.py文件中写函数

    ```python
    def changebook(request, id):
        book_obj = Book.objects.filter(id=id).first()
        if request.method == 'POST':
            title = request.POST.get('title')
            price = request.POST.get('price')
            date = request.POST.get('date')
            publish = request.POST.get('publish')
            Book.objects.filter(id=id).update(title=title, price=price, pub_date=date, publish=publish)
            return redirect('/books/')
    
        return render(request, "changebook.html", {"book_obj": book_obj})
    ```

- 写模板

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    
        <link rel="stylesheet" href="/static/bs/css/bootstrap.css">
        <style>
            .container{
                margin-top: 100px;
            }
            .btn{
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
    
    <h3>编辑书籍</h3>
    
    <div class="container">
         <div class="row">
             <div class="col-md-6 col-md-offset-3">
                 <form action="" method="post">
                     {% csrf_token %}
                     <div>
                         <label for="">书籍名称</label>
                         <input type="text" class="form-control" name="title" value="{{ book_obj.title }}">
                     </div>
                     <div>
                         <label for="">价格</label>
                         <input type="text" class="form-control" name="price" value="{{ book_obj.price }}">
                     </div>
                     <div>
                         <label for="">出版日期</label>
                         <input type="date" class="form-control" name="date" value="{{ book_obj.pub_date|date:'Y-m-d' }}">
                     </div>
                     <div>
                         <label for="">出版社</label>
                         <input type="text" class="form-control" name="publish" value="{{ book_obj.publish }}">
                     </div>
    
                     <input type="submit" class="btn btn-success pull-right">
    
                 </form>
             </div>
         </div>
    </div>
    
    </body>
    </html>
    ```

#### 13.9.5 多表查询

##### 13.9.5.1.创建表

- 作者表：包含姓名和年龄字段
- 作者详情表：包含生日，手机号，地址字段
- 出版社表：包含出版社名称，城市，邮箱字段
- 书籍表：包含书籍名称，出版日期，价格字段

###### 13.9.5.1 ORM建表语句

```python
from django.db import models

# Create your models here.
'''
Publish＝＝＝Book  一对多
Author＝＝＝AuthorDetail 一对一
'''

# 作者表
class Author(models.Model):
    nid = models.AutoField(primary_key=True)  # 如果写了就用写的，没写自动添加
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    # 与AuthorDetail建立一对一的关系
    authorDetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


# 作者详情表
class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField(null=True)
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)


# 出版社表
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


# 书籍表
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    read_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)

    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish = models.ForeignKey(to="Publish", to_field="nid", on_delete=models.CASCADE)
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors = models.ManyToManyField(to='Author')

    '''
    多对多建立关系语句等同于以下语句：
    class Book2Author(models.Model):
        nid = models.AutoField(primary_key=True)
        book = models.ForeignKey(to="Book")
        author = models.ForeignKey(to=Author)
    '''

    def __str__(self):
        return self.title

```

###### 13.9.5.2 对应关系

- 一对一：作者表与作者详情表之间是一对一的关系，详情表补充作者的信息。
- 多对一：书籍表和出版社表是一对多的关系，出版社可以出版多本书，但是一本书职能有一个出版社。
- 多对多：书籍表和作者表是多对多的关系，一本书可能有多个作者，一个作者可能出版多本书。

###### 13.9.5.3 注意事项：

- 表的命名：app名称+表的名称，是根据表中的原数据自动生成的，如：app01_book
- id字段如果没有写会自动添加，写了就用写的id
- 外键字段，Django会在字段名上自动补充"_id"形成新的字段名
- 上例中的建表语句使用PostgreSQL语法格式，Django会根据settings中指定的数据库类型来使用相应的SQL语句
- 定义好建表语句后，告诉Django使用这些表，需要在settings中的INSTALLED_APPS添加app名称，Django会自动添加，例如：'app01.apps.App01Config'
- 外键字段ForeignKey有一个null=True的设置，设置好后，允许外键接受空值NULL，可以给它赋值None
- 表之间建立关系的时候，加上on_delete=models.CASCADE参数，否则会报错，意思是：主外关系键中，级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
- 多对多的关系语句：authors = models.ManyToManyField(to='Author')这条语句会生成第五张表多对多的关系表，这条语句可以写在多对多任意一张表中，生成的表名book会根据这条语句所在的表中进行变动，比如：app01_book_authors
- 一对一的关系语句可以写在对应的人意一张表中
- 一对多的关系语句必须写在多的表中

执行数据库迁移语句会生成五张表：

- python3 manage.py makemigrations
- python3 migrate

##### 13.9.5.2 添加表纪录

###### 13.9.5.1 一对多的关系

```python
# 普通添加表纪录
info = AuthorDetail.objects.create(birthday='2019-01-09', telephone='119', addr='南京')
pub = Publish.objects.create(name="人民出版社", email="123@qq.com", city="北京")
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝绑定一对多的关系添加＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
# 方式一
    # 为book表绑定Publish关系
    book_obj = Book.objects.create(title="雪山飞狐", price=300, publishDate="2019-01-02", publish_id=1)
    print(book_obj.title)

# 方式二
    pub_obj = Publish.objects.filter(nid=1).first()
    book_obj = Book.objects.create(title="水浒传", price=400, publishDate="2019-01-02", publish=pub_obj)
    
    print(book_obj.publish)  # 打印与这本书籍关联的出版社对象，在models对应的表中加__str__可以打印出来
    print(book_obj.publish.name)
    print(book_obj.publish.email)
    print(book_obj.title)
    print(book_obj.price)
    print(book_obj.publishDate)

    # 查询西游记这本书的出版社对应的邮箱
    book_obj = Book.objects.filter(title="西游记")[0]  # 也可以first()取值
    print(book_obj.publish.email)
```

###### 13.9.5.2 多对多的关系

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝绑定多对多的关系＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
# 新建一本书
    book_obj = Book.objects.create(title="金瓶梅", price=400, publishDate="2019-07-16", publish_id=1)
    # 新建两个作者
    alex = Author.objects.get(name="alex")
    egon = Author.objects.get(name="egon")
    # 绑定多对多关系的API，三种任选其一
    book_obj.authors.add(alex, egon)
    book_obj.authors.add(1, 2)
    book_obj.authors.add(*[1, 2])
		
    # 解除多对多的关系
    book = Book.objects.filter(nid=8).first()
    # book.authors.remove(2)
    # book.authors.remove(*[1, 2])
    # 全部解除
    # book.authors.clear()
    # 查询主键为8的所有作者的名字＝＝＝关键点
    print(book.authors.all().values("name"))  # queryset:与这本书关联的所有作者对象集合
```

##### 13.9.5.3 跨表查询

###### 13.9.5.3.1 基于对象的跨表查询(子查询)

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝基于对象的跨表查询(子查询)＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
'''
正向查询按字段，反向查询按表名
'''
	# 一对多正向查询：查询金瓶梅这本书的出版社的名字
    book_obj = Book.objects.filter(title="金瓶梅").first()
    print(book_obj.publish)  # 与这本书关联的出版社对象
    print(book_obj.publish.name)

    # 一对多反向查询：查询人民出版社出版过的书籍
    publish = Publish.objects.filter(name="人民出版社").first()
    ret = publish.book_set.all()  # [obj1, obj2, obj3, obj4...]
    print(ret)

    # 多对多正向查询：查询金瓶梅这本书所有的作者的名字
    book_obj = Book.objects.filter(nid=9).first()
    author_list = book_obj.authors.all()  # queryset对象
    for author in author_list:
        print(author)

    # 多对多反向查询：查询alex出版过的书籍
    alex = Author.objects.filter(name='alex').first()
    book_list = alex.book_set.all()
    for book in book_list:
        print(book)

    # 一对一正向查询：查询alex的手机号
    alex = Author.objects.filter(name="alex").first()
    print(alex.authorDetail.telephone)

    # 一对一反向查询：查询手机号为112的作者的名字和年龄
    tel = AuthorDetail.objects.filter(telephone='112').first()
    print(tel.author.name)
    print(tel.author.age)
```

###### 13.9.5.3.2 基于双下划线的跨表查询

Django 提供了一种直观而高效的方式在查询(lookups)中表示关联关系，它能自动确认 SQL JOIN 联系。要做跨关系查询，就使用两个下划线来链接模型(model)间关联字段的名称，直到最终链接到你想要的 model 为止。

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝基于双下划线的跨表查询(join查询)＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
'''
正向查询按字段，反向查询按表名小写用来告诉ORM引擎用哪张表
'''
	# 方式一：一对多正向查询：查询金瓶梅这本书的出版社名称
    book_obj = Book.objects.filter(title='金瓶梅').values('publish__name')
    print(book_obj)

    # 方式二：一对多反向查询：查询出版过金瓶梅的书籍名称
    ret = Publish.objects.filter(book__title='金瓶梅').values('name')
    print(ret)

    # 方式一：多对多正向查询：查询西游记这本书的所有作者的名字(join)
    # 需求：通过Book表join与其关联的Author表，按字段authors通过ORM引擎join book_authors 和 author表
    ret = Book.objects.filter(title='西游记').values('authors__name')
    print(ret)

    # 方式二：多对多反向查询：查询西游记这本书的所有作者(join)
    # 需求：通过Author表join与其关联的Book表，按表名小写book通过ORM引擎join book_authors 和 book表
    ret = Author.objects.filter(book__title='西游记').values('name')
    print(ret)

    # 方式一：一对一正向查询：查询egon的手机号
    # 需求：通过Author表join与其关联的AuthorDetail表，按字段authorDetail通过ORM引擎join AuthorDetail表
    ret = Author.objects.filter(name='egon').values('authorDetail__telephone')
    print(ret)

    # 方式二：一对一反向查询：查询egon的手机号
    # 需求：通过AuthorDetail表join与其关联的Author表，按表名小写author通过ORM引擎join Author表
    ret = AuthorDetail.objects.filter(author__name='egon').values('telephone')
    print(ret)

    # 方式一：
    # 进阶练习：查询手机号110开头的作者出版过的所有书籍名称以及书籍出版社名称
    # 需求：通过Book表join与其关联的AuthorDetail表，Book与AuthorDetail无关联，所以必须连续跨表
    ret = Book.objects.filter(authors__authorDetail__telephone__startswith='110').values('title', 'publish__name')
    print(ret)

    # 方式二：
    # 进阶练习：查询手机号110开头的作者出版过的所有书籍名称以及书籍出版社名称
    # 需求：通过Book表join与其关联的AuthorDetail表，Book与AuthorDetail无关联，所以必须连续跨表
    ret = Author.objects.filter(authorDetail__telephone__startswith='110').values('book__title', 'book__publish__name')
    print(ret)
```

总结：

```python
"""
＝＝＝＝＝＝＝＝＝＝＝＝＝基于对象的跨表查询(子查询)＝＝＝＝＝＝＝＝＝＝＝＝＝
正向查询：关联属性在A表中 A－－－>B
返向查询：关联属性在A表中 B－－－>A
一对多查询：
    正向查询：按字段
    反向查询：按表名小写_set.all()
    
                        book_obj.publish
    Book(关联属性：publish)<－－－－－－－－－>Publish
                        publish_obj.book_set.all()  # queryset
    
多对多查询：
    正向查询：按字段
    反向查询：按表名小写_set.all()    
                        book_obj.objects.all()                
    Book(关联属性：authors)<－－－－－－－－－>Author
                        author_obj.book_set.all()  # queryset
                        
一对一查询：
    正向查询：按字段
    反向查询：按表名小写
    
                              alex.authordetail                
    Author(关联属性：authorDetail)<－－－－－－－－－>AuthorDetail
                              authordetail.author  # queryset
                        
＝＝＝＝＝＝＝＝＝＝＝＝＝基于双下划线的跨表查询(join查询)＝＝＝＝＝＝＝＝＝＝＝＝＝
    正向查询：按字段
    反向查询：按表名小写

"""
```

###### 13.9.5.3.3 聚合查询

aggregate()是QuerySet 的一个终止子句，意思是说，它返回一个包含一些键值对的字典。键的名称是聚合值的标识符，值是计算出来的聚合值。键的名称是按照字段和聚合函数的名称自动生成出来的。如果你想要为聚合值指定一个名称。

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝聚合查询 aggregate＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
'''
聚合返回是一个字典，不再是queryset
'''
    from django.db.models import Avg, Max, Min, Count

    # 查询所有书籍的平均价格
    ret = Book.objects.all().aggregate(avg_price=Avg('price'),
                                       max_price=Max('price'),
                                       min_price=Min('price'),
                                       Count_price=Count('price'))
    print(ret)
```

###### 13.9.5.3.4 分组查询

annotate()为调用的QuerySet中每一个对象都生成一个独立的统计值（统计方法用聚合函数）。

在models.py中新建Emp表：

```python
class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
```

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝分组查询 annotate＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
'''
返回值是queryset
'''
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝单表分组查询：
    # 示例一：
    # 查询每一个部门的名称以及员工的平均薪水
    # SQL: select dep,Avg(salary) from emp group by dep
    # 单表分组查询的ORM语法：单表模型.objects.values('group by的字段').annotate(聚合函数('统计字段'))
    ret = Emp.objects.values('dep').annotate(avg_salary=Avg('salary'))
    print(ret)

    # 示例二：
    # 查询每一个省份的名称以及员工数
    ret = Emp.objects.values('province').annotate(c=Count('id'))
    print(ret)

    # 补充知识点：
    # 在单表分组下，按着主键进行group by是没有任何意义
    ret = Emp.objects.all()
    print(ret)  # select * from emp
    ret = Emp.objects.values('name')
    print(ret)  # select name from emp
    Emp.objects.values('id').annotate(avg_salary=Avg('salary'))
    Emp.objects.all().annotate(avg_salary=Avg('salary'))
    
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝多表分组查询：
    # 示例1:查询每一个出版社的名称及出版的书籍个数
    # 方式一：
    ret = Publish.objects.values('name').annotate(count_book=Count('book__title'))
    print(ret)
    # 方式二:(推荐)
    ret = Publish.objects.values('nid').annotate(count_book=Count('book__title')).values('name', 'count_book')
    print(ret)

    # 方式三：另一种玩法
    ret = Publish.objects.all().annotate(count_book=Count('book__title')).values('name', 'count_book', 'city')
    print(ret)
    ret = Publish.objects.annotate(count_book=Count('book__title')).values('name', 'count_book', 'city')
    print(ret)

    # 示例2:查询每一个作者的名字以及出版过的书籍的最高价格
    ret = Author.objects.values('pk').annotate(mac_p=Max('book__price')).values('name', 'mac_p')
    print(ret)

    # 示例3:查询每一个书籍的名称以及对应的作者个数
    ret = Book.objects.values('pk').annotate(c=Count('authors__name')).values('title', 'c')
    print(ret)
    
    """
    总结跨表分组的模型：
    每一个的表模型.objects.values("pk").annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")
    每一个的表模型.objects.annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")
    每一个的表模型.objects.all().annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")
    """
```

练习：

```python
# 练习1:统计每一本以雪山开头的书籍的作者个数：
    ret = Book.objects.filter(title__startswith='雪山').values('pk').annotate(c=Count('authors__nid')).values('title', 'c')
    print(ret)

    # 练习2:统计不止一个作者的书籍
    ret = Book.objects.values('pk').annotate(c=Count('authors__nid')).filter(c__gt=1).values('title', 'c')
    print(ret)

    # 练习3:根据一本图书作者数量的多少对查询集 QuerySet进行排序:
    ret = Book.objects.all().annotate(c=Count('authors__name')).order_by('c')
    print(ret)

    # 练习4:查询各个作者出的书的总价格:
    ret = Author.objects.values('pk').annotate(c=Sum('book__price')).values('name', 'c')
    print(ret)
```

###### 13.9.5.3.5 F查询与Q查询

F查询：Django支持F()对象之间以及F()对象和常数之间的加减乘除和取模以及修改的操作。

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝F查询＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
    from django.db.models import F, Q
    # 统计评论数大于阅读数的书籍
    ret = Book.objects.filter(comment_num__gt=F('read_num'))
    print(ret)

    # 每本书籍加10
    Book.objects.all().update(price=F('price')+10)
```

Q查询：filter()等方法中的关键字参数查询都是一起进行“AND”的。如果你需要执行更复杂的查询，你可以使用Q对象。

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝Q查询＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
    # Q对象可以使用&(and) 和|(or) 操作符组合起来使用也可以分开使用，~Q(取反)
    # 查询名字为西游记或价格等于430的书籍
    ret = Book.objects.filter(Q(title='西游记') | Q(price=430))
    print(ret)

    # 查询名字不等于水浒传价格等于430阅读量大于2000的书籍
    ret = Book.objects.filter(~Q(title='水浒传') & Q(price=230), read_num__gt=2000)
    print(ret)
```

#### 13.9.6 Meta类详解

Django 模型类的Meta是一个内部类，它用于定义一些Django模型类的行为特性。下面对此作一总结：

- **abstract**
  这个属性是定义当前的模型类是不是一个抽象类。所谓抽象类是不会相应数据库表的。一般我们用它来归纳一些公共属性字段，然后继承它的子类能够继承这些字段。

  比方以下的代码中Human是一个抽象类。Employee是一个继承了Human的子类，那么在执行syncdb命令时，不会生成Human表。可是会生成一个Employee表，它包括了Human中继承来的字段。以后假设再加入一个Customer模型类，它能够相同继承Human的公共属性：

  ```python
  class Human(models.Model):
      name=models.CharField(max_length=100)
      GENDER_CHOICE=((u'M',u'Male'),(u'F',u'Female'),)
      gender=models.CharField(max_length=2,choices=GENDER_CHOICE,null=True)
      class Meta:
          abstract=True
          
  class Employee(Human):
      joint_date=models.DateField()
      
  class Customer(Human):
      first_name=models.CharField(max_length=100)
      birth_day=models.DateField()
  ```

  ```python
  # 上面的代码，运行 python manage.py syncdb 后的输出结果入下。能够看出Human表并没有被创建:
  
  $ python manage.py syncdb
  Creating tables ...
  Creating table myapp_employee
  Creating table myapp_customer
  Installing custom SQL ...
  Installing indexes ...
  No fixtures found.
  ```

  **models choices添加选项：**

  > 一个二元元组的元组或者列表，如果执行 choices ， Django 的 admin 就会使用 选择框 而不是标准的 text 框填写这个 field。
  >
  > 二元元组的第一个元素是要存入 database 的数据，第二个元素是 admin 的界面显示的数据。

  ```python
  YEAR_IN_SCHOOL_CHOICES = (
      (u'FR', u'Freshman'),
      (u'SO', u'Sophomore'),
      (u'JR', u'Junior'),
      (u'SR', u'Senior'),
      (u'GR', u'Graduate'),
  )
  ```

  使用了 `choices` 参数的 `field` 再其model示例里，可以用 `get_field的名字_display` 的方法，显示 `choices` 的字符串（就是二元元组的第二个数据）

  ```python
  from django.db import models
  
  class Person(models.Model):
      GENDER_CHOICES = (
          (u'M', u'Male'),
          (u'F', u'Female'),
      )
      name = models.CharField(max_length=60)
      gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
  ```

  ```python
  >>> p = Person(name="Fred Flinstone", gender="M")
  >>> p.save()
  >>> p.gender
  u'M'
  >>> p.get_gender_display()
  u'Male'
  ```

- **app_label**

  app_label这个选项仅仅在一种情况下使用，就是你的模型类不在默认的应用程序包下的models.py文件里。这时候你须要指定你这个模型类是那个应用程序的。比如你在其它地方写了一个模型类，而这个模型类是属于myapp的，那么你这是须要指定为：app_label='myapp'

- **db_table**

  db_table是用于指定自己定义数据库表名的。Django有一套默认的依照一定规则生成数据模型相应的数据库表名。假设你想使用自己定义的表名。就通过这个属性指定，比如：table_name='my_owner_table'

- **db_tablespace**

  有些数据库有数据库表空间，比方Oracle。你能够通过db_tablespace来指定这个模型相应的数据库表放在哪个数据库表空间。

- **get_latest_by**

  因为Django的管理方法中有个lastest()方法，就是得到近期一行记录。假设你的数据模型中有 DateField 或 DateTimeField 类型的字段。你能够通过这个选项来指定lastest()是依照哪个字段进行选取的。

- **managed**

  因为Django会自己主动依据模型类生成映射的数据库表。假设你不希望Django这么做。能够把managed的值设置为False。

- **order_with_respect_to**

  这个选项一般用于多对多的关系中，它指向一个关联对象。就是说关联对象找到这个对象后它是经过排序的。指定这个属性后你会得到一个get_XXX_order()和set_XXX_order（）的方法,通过它们你能够设置或者回去排序的对象。

- **ordering**

  这个字段是告诉Django模型对象返回的记录结果集是依照哪个字段排序的。比如以下的代码：

  ```python
  ordering=['order_date'] # 按订单升序排列
  ordering=['-order_date'] # 按订单降序排列，-表示降序
  ordering=['?order_date'] # 随机排序。？表示随机
  ```

- **permissions**

  permissions主要是为了在Django Admin管理模块下使用的。假设你设置了这个属性能够让指定的方法权限描写叙述更清晰可读。

- **proxy**

  这是为了实现代理模型使用的。

- **unique_together**

  unique_together这个选项用于：当你须要通过两个字段保持唯一性时使用。

  比如：如果你希望，一个Person的FirstName和LastName两者的组合必须是唯一的，那么须要这样设置：

  ```python
  unique_together = (("first_name", "last_name"),)
  ```

- **verbose_name**

  verbose_name的意思非常easy。就是给你的模型类起一个更可读的名字：

  ```python
  verbose_name = "pizza"
  ```

- **verbose_name_plural**

  这个选项是指定。模型的复数形式是什么。比如：

  ```python
  class BookInfo(models.Model):
      name = models.CharField(max_length=10, unique=True, verbose_name='名字')
      pub_date = models.DateField(null=True)
      readcount=models.IntegerField(default=0)
      commentcount=models.IntegerField(default=0)
      is_delete=models.BooleanField(default=False)
      class Meta:
          db_table = 'bookinfo'
          verbose_name_plural = 'hello'
      def __str__(self):
          return self.name
  ```

  如果verbose_name 后面没有_plural选项，则会在网站上类名后面自动拼接一个‘s'，效果如下：

  ![image-20210930143230212](j:\homework\Python学习笔记\Python_notes.assets\image-20210930143230212.png)

  将verbose_name = 'hello'改为verbose_name_plural = 'hello'，效果如下：

  ![image-20210930143338661](j:\homework\Python学习笔记\Python_notes.assets\image-20210930143338661.png)







### 13.10 Djanjo与Ajax

Ajax（Asynchronous Javascript And XML）翻译成中文就是“异步Javascript和XML”。即使用Javascript语言与服务器进行异步交互，传输的数据为XML（当然，传输的数据不只是XML,现在更多使用json数据）。

- 同步交互：客户端发出一个请求后，需要等待服务器响应结束后，才能发出第二个请求；
- 异步交互：客户端发出一个请求后，无需等待服务器响应结束，就可以发出第二个请求。

AJAX除了**异步**的特点外，还有一个就是：浏览器页面**局部刷新**；（这一特点给用户的感受是在不知不觉中完成请求和响应过程）

**优点：**

- AJAX使用Javascript技术向服务器发送异步请求
- AJAX无须刷新整个页面

**基于jquery的Ajax：**

index.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="http://ajax.aspnetcdn.com/ajax/jquery/jquery-2.1.4.min.js"></script>
</head>
<body>
<h2>this is index!</h2>
<button class="Ajax">Ajax</button>
<p class="content"></p>
<script>
    $(".Ajax").click(function () {
        // 发送Ajax请求
        $.ajax({
            url:"/test_ajax/",  // 请求url
            type:"get",  // 请求方式post
            success:function (data) {  //回调函数：某个动作执行结束再回来执行的函数
                console.log(data)

                $(".content").html(data)  // 显示到页面
            }
        })
    })
</script>
</body>
</html>
```

url.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('test_ajax/', views.test_ajax)
]
```

views.py

```python
from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):

    return render(request, 'index.html')


def test_ajax(request):
    return HttpResponse("hello world!")
```

示例一：计算器和登录验证

views.py

```python
def cs_cal(request):
    print(request.POST)
    n1 = int(request.POST.get('n1'))
    n2 = int(request.POST.get('n2'))
    ret = n1 + n2
    return HttpResponse(ret)
    
import json


def cs_login_plus(request):
    print(request.POST)

    username = request.POST.get("username")
    password = request.POST.get("password")

    userinfo = Usernfo.objects.filter(name=username, pwd=password).first()
    ret = {"username": None, "msg": None}
    if userinfo:
        ret["username"] = userinfo.name
    else:
        ret["msg"] = "username or password error!"

    return HttpResponse(json.dumps(ret))
```

 模板：

```js
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <title>Document</title>
  </head>
  <body>
    <h3>this is ajax</h3>
    <button class="ajax">提交</button>
    <p class="butoon"></p>
    <hr />

    <input type="text" id="num1" />
    +
    <input type="text" id="num2" />
    =
    <input type="text" id="ret" />
    <button class="cal">计算</button>
    <hr />
    <form>
      用户名
      <input type="text" id="user" />
      密码
      <input type="text" id="password" />
      <input type="button" value="提交" class="submit" />
      <span class="error"></span>
    </form>
    

    <script>
      $('.ajax').click(function name(params) {
        $.ajax({
          url: '/test_ajax/',
          type: 'get',
          data: { a: 1, b: 2 },
          success: function (data) {
            $('.butoon').html(data)
          },
        })
      })
    </script>

    <!-- 计算求值 -->
    <script>
      $('.cal').click(function name(params) {
        $.ajax({
          url: '/cal/',
          type: 'post',
          data: { n1: $('#num1').val(), n2: $('#num2').val() },
          success: function name(params) {
            $('#ret').val(params)
          },
        })
      })
    </script>

    <!-- 登录验证 -->

    <script>
      $('.submit').click(function () {
        $.ajax({
          url: '/login/',
          type: 'post',
          data: { username: $('#user').val(), password: $('#password').val() },
          success: function (data) {
            var data = JSON.parse(data)
            console.log(data)
            console.log(typeof data)
            if (data.username){
                location.href="http://book.luffycity.com/linux-book/index.html"
            }
            else{
                $(".error").html(data.msg).css({"color":"red", "margin-left": "10px"})
            }
          },
        })
      })
    </script>
  </body>
</html>

```

**文件上传**：

**一、请求头ContentType**

ContentType指的是请求体的编码类型，常见的类型共有3种：

- application/x-www-form-urlencoded

    - 这应该是最常见的 POST 提交数据的方式了。浏览器的原生表单，如果不设置 enctype 属性，那么最终就会以 application/x-www-form-urlencoded 方式提交数据。类似于下面这样（无关的请求头在本文中都省略掉了）：

    ```js
    POST http://www.example.com HTTP/1.1
    Content-Type: application/x-www-form-urlencoded;charset=utf-8
    
    user=yuan&age=22
    ```

- multipart/form-data

    - 这又是一个常见的 POST 数据提交的方式。我们使用表单上传文件时，必须让表单的 enctype 等于 multipart/form-data。示例：

        ```js
        POST http://www.example.com HTTP/1.1
        Content-Type:multipart/form-data;
        ```

- application/json

    - application/json 这个 Content-Type 作为响应头大家肯定不陌生。实际上，现在越来越多的人把它作为请求头，用来告诉服务端消息主体是序列化后的 JSON 字符串。由于 JSON 规范的流行，除了低版本 IE 之外的各大浏览器都原生支持 JSON.stringify，服务端语言也都有处理 JSON 的函数，使用 JSON 不会遇上什么麻烦。
        JSON 格式支持比键值对复杂得多的结构化数据，这一点也很有用。记得我几年前做一个项目时，需要提交的数据层次非常深，我就是把数据 JSON 序列化之后来提交的。不过当时我是把 JSON 字符串作为 val，仍然放在键值对里，以 x-www-form-urlencoded 方式提交。

上面提到的这两种 POST 数据的方式，都是浏览器原生支持的，而且现阶段标准中原生表单也只支持这两种方式（通过 元素的 enctype 属性指定，默认为 application/x-www-form-urlencoded。其实 enctype 还支持 text/plain，不过用得非常少）。
随着越来越多的 Web 站点，尤其是 WebApp，全部使用 Ajax 进行数据交互之后，我们完全可以定义新的数据提交方式，给开发带来更多便利。

**二、基于form表单和Ajax的文件上传**

示例：视图

```python
def file_put(request):
    if request.method == 'POST':
        # print("body", request.body)  # 请求报文中的请求体
        print("post", request.POST)  # if contentType == urlencode的时候,request.POST才有数据

        print(request.FILES)

        file_obj = request.FILES.get('avatar')
        with open(file_obj.name, 'wb')as f:
            for line in file_obj:
                f.write(line)
        return HttpResponse("OK")

    return render(request, 'file_put.html')
```

模板：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="http://ajax.aspnetcdn.com/ajax/jquery/jquery-2.1.4.min.js"></script>
</head>
<body>
<h3>简单的form</h3>
<form action="" method="post">
    用户名<input type="text" name="user">
    密码 <input type="password" name="pwd">
    <input type="submit">
</form>
<hr>

<h3>基于form表单的文件上传</h3>
<form action="" method="post" enctype="multipart/form-data">
    用户名 <input type="text" name="user">
    头像 <input type="file" name="avatar">
    <input type="submit">
</form>
<hr>

<h3>基于Ajax文件上传</h3>
<form action="" method="post">
    用户名<input type="text" id="user">
    头像 <input type="file" id="avatar">
    <input type="button" class="btn" value="ajax">
</form>

<script>
    // json序列化
    $(".btn").click(function () {
        $.ajax({
            url:"",
            type:"post",
            contentType:"application/json",
            data:JSON.stringify({  //json序列化
                a:1,
                b:2
            }),
            success:function (data) {
                console.log(data)
            }
        })
    })

    $(".btn").click(function () {
        $.ajax({
            url:"",
            type:"post",
            data:{
                a:1,
                b:2
            },
            success:function (data) {
                console.log(data)
            }
        })
    })

    // ajax上传文件
    $(".btn").click(function () {
        var formata = new FormData();
        formata.append("user", $("#user").val());
        formata.append("avatar", $("#avatar")[0].files[0]);
        $.ajax({
            url:"",
            type:"post",
            contentType:false,  //
            processData:false,  //
            data:formata,
            success:function (data) {
                console.log(data)
            }
        })
    })
</script>
</body>
</html>
```

### 13.11 组件-分页器

```python
print(page2.has_next())            #是否有下一页
print(page2.next_page_number())    #下一页的页码
print(page2.has_previous())        #是否有上一页
print(page2.previous_page_number()) #上一页的页码

# 抛错
page=paginator.page(12)   # error:EmptyPage

page=paginator.page("z")   # error:PageNotAnInteger
```

模板：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>

<ul>
    {% for foo in curr_page %}
        <li>{{ foo.title }}:{{ foo.price }}</li>
    {% endfor %}
</ul>

<nav aria-label="Page navigation">
  <ul class="pagination">
    {#判断是否有上一页#}
    {% if curr_page.has_previous %}
        <li>
            <a href="?page={{ curr_page.previous_page_number }}" aria-label="Previous">
                <span aria-hidden="true">上一页</span>
            </a>
        </li>
    {% else %}
        <li class="disabled">
        <a href="" aria-label="Previous">
            <span aria-hidden="true">上一页</span>
        </a>
        </li>
    {% endif %}

    {#  加页码  #}
    {% for item in page_range %}
    {% if current_page == item%}
        <li class="active"><a href="?page={{ item }}">{{ item }}</a></li>
    {% else %}
        <li><a href="?page={{ item }}">{{ item }}</a></li>
    {% endif %}
    {% endfor %}

    {#判断是否有下一页#}
    {% if curr_page.has_next %}
        <li>
          <a href="?page={{ curr_page.next_page_number }}" aria-label="Next">
            <span aria-hidden="true">下一页</span>
          </a>
        </li>
    {% else %}
        <li class="disabled">
          <a href="" aria-label="Next">
            <span aria-hidden="true">下一页</span>
          </a>
        </li>
    {% endif %}
  </ul>
</nav>
</body>
</html>
```

视图：

```python
from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator, EmptyPage


# Create your views here.


def index(request):
    """
    批量导入：
    book_list = []
    for i in range(100):
        book = Book(title='book_%s' % i, price=i * i)
        book_list.append(book)
    Book.objects.bulk_create(book_list)  # 批量插入
    """
    book_list = Book.objects.all()

    # 分页器
    paginator = Paginator(book_list, 3)  # 每页显示10条数据
    print('count:', paginator.count)  # 数据总数
    print('num_pages:', paginator.num_pages)  # 总页数
    print('page_range:', paginator.page_range)  # 页码列表
    current_page = int(request.GET.get('page', 1))

    if paginator.num_pages > 11:
        if current_page - 5 < 1:
            page_range = range(1, 12)
        elif current_page + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages-10, paginator.num_pages + 1)
        else:
            page_range = range(current_page - 5, current_page + 6)
    else:
        page_range = range(current_page - 5, current_page + 6)
    try:

        curr_page = paginator.page(current_page)  # 第几页的page对象
        print(curr_page.object_list)  # 显示某一页的所有数据

        for i in curr_page:  # 遍历当前页的所有数据对象
            print(i)
    except EmptyPage as e:
        curr_page = paginator.page(1)
    return render(request, 'index.html', locals())
```

### 13.12 组件-forms

针对字段进行校验

示例：models.py

```python
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.EmailField()
    tel = models.CharField(max_length=32)
```

模板：渲染标签

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>
<div class="container">
    <div class="row">
        <div class="cal-md-6 col-lg-offset-3">

            <form action="" method="post">
                {% csrf_token %}
                <p>用户名：<input type="text" name="name"></p>
                <p>密码：<input type="text" name="pwd"></p>
                <p>确认密码：<input type="text" name="re_pwd"></p>
                <p>邮箱：<input type="text" name="email"></p>
                <p>电话：<input type="text" name="tel"></p>
                <input type="submit">
            </form>

            <hr>
            <h3>form组件渲染方式1</h3>
            <form action="" method="post" novalidate>
                {% csrf_token %}
                {# lable渲染字段名字，和input标签#}
                <p>{{ form.name.label }}{{ form.name }}</p>
                    <span class="pull-right error">{{ form.name.errors.0 }}</span>
                <p>{{ form.pwd.label }}{{ form.pwd }}</p>
                    <span class="pull-right error">{{ form.pwd.errors.0 }}</span>
                <p>{{ form.re_pwd.label }}{{ form.re_pwd }}</p>
                    <span class="pull-right error">{{ form.re_pwd.errors.0 }}</span>
                <p>{{ form.email.label }}{{ form.email }}</p>
                <span class="pull-right error">{{ form.email.errors.0 }}</span>
                    <p>{{ form.tel.label }}{{ form.tel }}</p>
                <span class="pull-right error">{{ form.tel.errors.0 }}</span>
                <input type="submit">
            </form>

            <hr>
            <h3>forms组件渲染方式2</h3>
            <form action="" method="post">
                {% csrf_token %}
                {% for field in form %}
                    <p>
                        <lable for="">{{ field.label }}</lable>
                        {{ field }}
                    </p>
                {% endfor %}
            </form>
            <hr>
                
            <h3>forms组件渲染方式3</h3>
            <form action="" method="post">
                {% csrf_token %}
{#             缺点不灵活：默认p标签，无法切换标签#}
                {{ form.as_p }}
                <input type="submit">
            </form>

        </div>
    </div>
</div>
</body>
</html>
```

视图：

```js
from django.shortcuts import render, HttpResponse

# Create your views here.
from app01.my_forms import *


def reg(request):
    """
    显示错误与重置输入信息功能
    :param request:
    :return:
    """
    if request.method == "POST":

        # form = UserForm({"name":"iker", "email": "123@163.com", "xxx": "alex"})

        form = UserForm(request.POST)  # form表单的name属性对应的值，应该与forms组件的字段名称一致

        print(form.is_valid())  # 返回一个布尔值，所有的值都校验通过
        if form.is_valid():  # 校验返回布尔值
            print(form.cleaned_data)  # 只打印校验成功的键值
        else:
            print(form.cleaned_data)  # 如果校验正确的都会打印出来
            # print(form.errors)  # 如果校验失败，会打印键值和错误信息
            # print(type(form.errors))
            #
            # print(form.errors.get("name"))
            # print(type(form.errors.get("name")))
            #
            # print(form.errors.get("name")[0])

            # 全局钩子错误
            # print(form.errors.get("__all__")[0])
            errors = form.errors.get("__all__")

            return render(request, "reg.html", locals())
        '''
        如果所有字段校验成功：
            则form.cleaned_data:{"name":"ike", "email":"123@163.com"}
            form.errors 如果校验失败，会打印键值和错误信息
        如果校验的字段不包含：
            forms组件与form表单所有字段的校验都成功，多出的字段不会去校验
            键值必须和字段一致
        '''
        # print(request.POST)

    form = UserForm()  # 未绑定数据
    return render(request, "reg.html", locals())
```

form文件：

```python
from django import forms
from django.forms import widgets
from app01.models import UserInfo
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


class UserForm(forms.Form):
    name = forms.CharField(min_length=4, label="用户名",
                           error_messages={"required": "该字段不能为空"},
                           widget=widgets.TextInput(attrs={"class": "form-control"}))
    pwd = forms.CharField(min_length=4, label="密码",
                          widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                          error_messages={"required": "该字段不能为空", "invalid": "格式错误"}
                          )
    re_pwd = forms.CharField(min_length=4, label="确认密码",
                             widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                             error_messages={"required": "该字段不能为空", "invalid": "格式错误"})
    email = forms.EmailField(label="邮箱",
                             error_messages={"required": "该字段不能为空", "invalid": "格式错误"},
                             widget=widgets.TextInput(attrs={"class": "form-control"}))
    tel = forms.CharField(label="手机号",
                          widget=widgets.TextInput(attrs={"class": "form-control"}),
                          error_messages={"required": "手机号不能为空"})

    # 局部钩子
    def clean_name(self):
        val = self.cleaned_data.get("name")
        ret = UserInfo.objects.filter(name=val)

        if not ret:
            return val
        else:
            raise ValidationError("该用户已注册！")

    def clean_tel(self):
        val = self.cleaned_data.get("tel")
        if len(val) == 11:
            return val
        else:
            raise ValidationError("手机号格式错误")

    # 全局钩子
    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")

        if pwd and re_pwd:
            if pwd == re_pwd:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致！")
        else:
            return self.cleaned_data
```

### 13.13 组件-cookie与session

生活中我们登陆一些网站经常都是以登录状态才可以访问，但是每个功能都是独立的，cookie与session简单的来说就是帮助我们保持登录状态，在登录的状态下访问更多的网页。

总结：

我们知道HTTP协议是无状态协议，也就是说每个请求都是独立的！无法记录前一次请求的状态。但HTTP协议中可以使用Cookie来完成会话跟踪！在Web开发中，使用session来完成会话跟踪，session底层依赖Cookie技术。

##### 13.13.1 Cookie概述

Cookie翻译成中文是小甜点，小饼干的意思。在HTTP中它表示服务器送给客户端浏览器的小甜点。其实Cookie是key-value结构，类似于一个python中的字典。随着服务器端的响应发送给客户端浏览器。然后客户端浏览器会把Cookie保存起来，当下一次再访问服务器时把Cookie再发送给服务器。 Cookie是由服务器创建，然后通过响应发送给客户端的一个键值对。客户端会保存Cookie，并会标注出Cookie的来源（哪个服务器的Cookie）。当客户端向服务器发出请求时会把所有这个服务器Cookie包含在请求中发送给服务器，这样服务器就可以识别客户端了！

**Cookie规范**

- Cookie大小上限为4KB；
- 一个服务器最多在客户端浏览器上保存20个Cookie；
- 一个浏览器最多保存300个Cookie；
    上面的数据只是HTTP的Cookie规范，但在浏览器大战的今天，一些浏览器为了打败对手，为了展现自己的能力起见，可能对Cookie规范“扩展”了一些，例如每个Cookie的大小为8KB，最多可保存500个Cookie等！但也不会出现把你硬盘占满的可能！

注意，不同浏览器之间是不共享Cookie的。也就是说在你使用IE访问服务器时，服务器会把Cookie发给IE，然后由IE保存起来，当你在使用FireFox访问服务器时，不可能把IE保存的Cookie发送给服务器。一个Cookie对应一个浏览器。

**Cookie与HTTP头**
Cookie是通过HTTP请求和响应头在客户端和服务器端传递的：

- Cookie：请求头，客户端发送给服务器端；
- 格式：Cookie: a=A; b=B; c=C。即多个Cookie用分号离开； Set-Cookie：响应头，服务器端发送给客户端；
- 一个Cookie对象一个Set-Cookie： 
    - Set-Cookie: a=A Set-Cookie: b=B Set-Cookie: c=C

**Cookie的覆盖**
如果服务器端发送重复的Cookie那么会覆盖原有的Cookie，例如客户端的第一个请求服务器端发送的Cookie是：Set-Cookie: a=A；第二请求服务器端发送的是：Set-Cookie: a=AA，那么客户端只留下一个Cookie，即：a=AA。

**django中的cookie语法：**

设置cookie：

```python
rep = HttpResponse(...) 或 rep ＝ render(request, ...) 或 rep ＝ redirect()  
rep.set_cookie(key,value,...)
rep.set_signed_cookie(key,value,salt='加密盐',...)
```

获取cookie：

```python
request.COOKIES
```

删除cookie：

```python
response.delete_cookie("cookie_key",path="/",domain=name)
```

示例：视图

```python
from django.shortcuts import render, HttpResponse, redirect
from app01.models import UserInfo
import datetime

# Create your views here.


def login(request):
    # ret = UserInfo.objects.create(user='joker', pwd=123)
    # print(ret)
    if request.method == 'POST':
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        username = UserInfo.objects.filter(user=user, pwd=pwd).first()
        if username:
            response = HttpResponse('登录成功')
            # 设置有效时间，单位秒
            # response.set_cookie('is_login', True, max_age=30)
            response.set_cookie('is_login', True)
            # 设置COOKIE有效路径
            response.set_cookie('username', username.user, path='/index/')
            # 设置失效时间
            date = datetime.datetime(year=2021, month=1, day=30, hour=9, minute=3)
            response.set_cookie('username', username.user, expires=date)
            # 设置上次登录时间
            now = datetime.datetime.now().strftime("%Y-%m-%d %X")
            response.set_cookie("last_visit_time", now)
            return response

    return render(request, 'login.html')


def index(request):
    print(request.COOKIES)
    is_login = request.COOKIES.get('is_login')
    if is_login:
        username = request.COOKIES.get("username")
        last_now = request.COOKIES.get("last_visit_time")
        response = render(request, 'index.html', {"username":username, "last_now":last_now})
        
        return response
    else:
        return redirect('/login/')


def test(request):

    print(request.COOKIES)

    return HttpResponse('ok!')
```

##### 13.13.2 Session概述

Session是服务器端技术，利用这个技术，服务器在运行时可以 为每一个用户的浏览器创建一个其独享的session对象，由于 session为用户浏览器独享，所以用户在访问服务器的web资源时 ，可以把各自的数据放在各自的session中，当用户再去访问该服务器中的其它web资源时，其它web资源再从用户各自的session中 取出数据为用户服务。

**django中session语法：**

```python
1、设置Sessions值
		request.session['session_name'] ="admin"
2、获取Sessions值
		session_name = request.session["session_name"]
		session_name = request.session,get("session_name")
3、删除Sessions值
		del request.session["session_name"]
4、flush()
     删除当前的会话数据并删除会话的Cookie。
     这用于确保前面的会话数据不可以再次被用户的浏览器访问
5、get(key, default=None)
  fav_color = request.session.get('fav_color', 'red')  
6、pop(key)
  fav_color = request.session.pop('fav_color')  
7、keys()
8、items()  
9、setdefault()  
10 用户session的随机字符串
        request.session.session_key

        # 将所有Session失效日期小于当前日期的数据删除
        request.session.clear_expired()

        # 检查 用户session的随机字符串 在数据库中是否
        request.session.exists("session_key")

        # 删除当前用户的所有Session数据
        request.session.delete("session_key")

        request.session.set_expiry(value)
            * 如果value是个整数，session会在些秒数后失效。
            * 如果value是个datatime或timedelta，session就会在这个时间后失效。
            * 如果value是0,用户关闭浏览器session就会失效。
            * 如果value是None,session会依赖全局session失效策略。
```

session配置：

```python
# Django默认支持Session，并且默认是将Session数据存储在数据库中，即：django_session 表中。

# 配置 settings.py

    SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）

    SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
    SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
    SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
    SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
    SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
    SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
    SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
```

示例：视图

```python
def login_session(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user = UserInfo.objects.filter(user=user, pwd=pwd).first()

        if user:
            import datetime
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.session["is_login"] = True
            request.session["username"] = user.user

            request.session["last_visit_time"] = now

            # TODO：今天看到cookie 和 session 设置和获取值
            # 1. 显示登录人的姓名，登录时间
            # 2. 一个浏览器对应一个服务器
            # 3.重复在一个浏览器登录只做更新操作，更新session－data

            '''
            if request.COOKIE.get("sessionid"):
                更新:下边操作
                在django－sessoin表中创建一条记录
                    session－key         session－data
                    12asda               更新数据：｛"is_login":True, "username":"ike"｝
            else:
                三步骤：
                    1.生成一个随机字符串：12asda
                    2.response.set_cookies("sessionid",12asda)
                    3.在django－sessoin表中创建一条记录
                        session－key     session－data
                        12asda          ｛"is_login":True, "username":"ike"｝
            '''
            return HttpResponse("登录成功")

    return render(request, "login.html")


def index_session(request):
    print("验证", request.session.get("is_login"))

    '''
    
    django获取session三步骤：
        1.12asda = request.COOKIE.get("session")
        2.django-session表中过滤数据：
	        obj = django-session.objects.filter(session-key=12asda).first()
            在django－session表中添加数据：
            session－key             session－data
            12asda          ｛"is_login":True, "username":"ike"｝
        3.取出session字典
            ret ＝ obj.session-data.get("is_login")
    '''
    is_login = request.session.get("is_login")
    if not is_login:
        return redirect("/login_session/")

    username = request.session.get("username")
    last_visit_time = request.session.get("last_visit_time")

    return render(request, "index.html", {"username": username, "last_visit_time": last_visit_time})


def logout(request):
    # del request.session["is_login"]
    # 删除session数据
    request.session.flush()
    '''
    randon_str = request.COOKIE.get("sessionid")
    django_session.objects.filter(session_key=randon_str).delete()
    response.delete_cookie("sessionid", randon_str)
    '''

    return redirect("/login_session/")
```

模板：index.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h3>hi {{ username }}</h3>
<p>上次登录时间：{{ last_visit_time }}</p>
<a href="/logout/">注销</a>
</body>
</html>
```

login.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<form action="" method="post">
    {% csrf_token %}
    用户名：<input type="text" name="user">
    密码：<input type="text" name="pwd">
    <input type="submit">
</form>
</body>
</html>
```

### 13.14 组件-用户认证

#### 13.14.1 auth模块

```python
from django.contrib import auth
```

django.contrib.auth中提供了许多方法，这里主要介绍常用的三个：

- authenticate()

    提供了用户认证，即验证用户名以及密码是否正确,一般需要username password两个关键字参数
    如果认证信息有效，会返回一个 User 对象。authenticate()会在User 对象上设置一个属性标识那种认证后端认证了该用户，且该信息在后面的登录过程中是需要的。当我们试图登陆一个从数据库中直接取出来不经过authenticate()的User对象会报错的！！

```PYTHON
user = authenticate(username='someone',password='somepassword')
```

- login(HttpRequest, user)　　

    该函数接受一个HttpRequest对象，以及一个认证了的User对象
    此函数使用django的session框架给某个已认证的用户附加上session id等信息。

```PYTHON
from django.contrib.auth import authenticate, login

def my_view(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  if user is not None:
    login(request, user)
    # Redirect to a success page.
    ...
  else:
    # Return an 'invalid login' error message.
    ...
```

- logout(request) 注销用户

    该函数接受一个HttpRequest对象，无返回值。当调用该函数时，当前请求的session信息会全部清除。该用户即使没有登录，使用该函数也不会报错。

```python
from django.contrib.auth import logout

def logout_view(request):
  logout(request)
  # Redirect to a success page.
```

#### 13.14.2 User对象

User 对象属性：username， password（必填项）password用哈希算法保存到数据库。

**2.1 user对象的 is_authenticated()**

如果是真正的 User 对象，返回值恒为 True 。 用于检查用户是否已经通过了认证。
通过认证并不意味着用户拥有任何权限，甚至也不检查该用户是否处于激活状态，这只是表明用户成功的通过了认证。 这个方法很重要, 在后台用request.user.is_authenticated()判断用户是否已经登录，如果true则可以向前台展示request.user.name

要求：

- 用户登陆后才能访问某些页面
- 如果用户没有登录就访问该页面的话直接跳到登录页面
- 用户在跳转的登陆界面中完成登陆后，自动访问跳转到之前访问的地址

方法1:

```python
def my_view(request):
  if not request.user.is_authenticated():
    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
```

方法2:
django已经为我们设计好了一个用于此种情况的装饰器：login_requierd()

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
  ...
```

若用户没有登录，则会跳转到django默认的 登录URL '/accounts/login/ ' (这个值可以在settings文件中通过LOGIN_URL进行修改)。并传递 当前访问url的绝对路径 (登陆成功后，会重定向到该路径)。

**2.2 创建用户：**

使用 create_user 辅助函数创建用户:

```python
from django.contrib.auth.models import User
user = User.objects.create_user（username='',password='',email=''）
```

**2.3 check_password(passwd)：**
用户需要修改密码的时候 首先要让他输入原来的密码 ，如果给定的字符串通过了密码检查，返回 True

**2.4 修改密码：**
使用 set_password() 来修改密码

```python
user = User.objects.get(username='')
user.set_password(password='')
user.save
```

**2.5 auth.authenticate它接受两个参数，用户名 username 和 密码 password ，并在密码对给出的用户名合法的情况下返回一个 User 对象。 如果密码不合法，authenticate()返回None**

```python
user = auth.authenticate(username=user, password=pwd)
```

**2.6 auth.login该函数接受一个 HttpRequest 对象和一个 User 对象作为参数并使用Django的会话（ session ）框架把用户的ID保存在该会话中**

```python
auth.login(request, user)
```

**2.7 它接受一个HttpRequest对象并且没有返回值,所以，因为没有返回值，需要返回一个页面**

```python
auth.logout(request)
```

需要注意的是：**即使用户没有登录， logout() 也不会抛出任何异常**

示例：视图

```python
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        # 如果验证成果返回user对象，否则返回None
        user = auth.authenticate(username=user, password=pwd)
        if user:
            # 该函数接受一个 HttpRequest 对象和一个 User 对象作为参数并使用Django的会话（ session ）框架把用户的ID保存在该会话中
            auth.login(request, user)

            # 获取next的值路径，如果有则跳转到对应的路径，如果没有则跳转到index路径
            next_url = request.GET.get("next", "/index/")
            return redirect(next_url)

    return render(request, "login.html")


@login_required  # 在settings中配置好登录路径(LOGIN_URL = "/login/")，登录前在该路径进行登录验证
def index(request):
    # print("request:user", request.user)
    # print("id", request.user.id)
    # print("anon", request.user.is_anonymous)
    #
    # # if request.user.is_anonymous:
    # if not request.user.is_authenticated:  # 是否通过验证
    #     return redirect("/login/")
    # # username = request.user.username
    # # return render(request, "index.html", {"username": username})

    # request.user.username 直接在模版中写
    return render(request, "index.html")


@login_required
def order(request):
    # if not request.user.is_authenticated:
    #     return redirect("/login/")
    return render(request, "order.html")


def logout(request):
    auth.logout(request)

    return redirect("/login/")


def reg(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user = User.objects.create_user(username=user, password=pwd)
        return redirect("/login/")

    return render(request, "reg.html")
```

模板：

1.index.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h3>Hi~, {{ request.user.username }}</h3>
<a href="/logout/">注销</a>
</body>
</html>
```

2.login.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h3>登录</h3>
<form action="" method="post">
    {% csrf_token %}
    用户名：<input type="text" name="user">
    密码：<input type="text" name="pwd">
    <input type="submit" value="submit">
</form>

</body>
</html>
```

3.order.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h3>order</h3>

</body>
</html>
```

4.reg.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h3>注册</h3>
<form action="" method="post">
    {% csrf_token %}
    用户名：<input type="text" name="user">
    密码：<input type="text" name="pwd">
    <input type="submit" value="submit">
</form>

</body>
</html>
```

### 13.15 组件-中间件

##### 13.15.1 中间件的概念

中间件顾名思义，是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出。因为改变的是全局，所以需要谨慎实用，用不好会影响到性能。
如果你想修改请求，例如被传送到view中的HttpRequest对象。 或者你想修改view返回的HttpResponse对象，这些都可以通过中间件来实现。
可能你还想在view执行之前做一些操作，这种情况就可以用 middleware来实现。
Django默认的Middleware：每一个中间件都有具体的功能。

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

##### 13.15.2 自定义中间件

中间件中一共有四个方法：

- process_request
- process_view
- process_exception
- process_response

当用户发起请求的时候会依次经过所有的的中间件，这个时候请求先到达process_request,然后到达views的函数中，views函数处理后，再依次穿过中间件，这个时候是process_response,最后返回给请求者。

我们也可以自己定义一个中间件，我们可以自己写一个类。

示例：视图

```python
def index(request):

    print("index")

    return HttpResponse("hello")
```

自定义中间件1：process_request和process_response

```python
from django.middleware.security import SecurityMiddleware
from django.utils.deprecation import MiddlewareMixin


class CustomerMiddleware(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware1 process_request")

    def process_response(self, request, response):
        print("CustomerMiddleware1 process_response")
        return response


class CustomerMiddleware2(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware2 process_request..")

    def process_response(self, request, response):
        print("CustomerMiddleware2 process_response")

        return response
```

注意：如果当请求到达请求2的时候直接不符合条件返回，即return HttpResponse("Md2中断")，程序将把请求直接发给中间件2返回，然后依次返回到请求者。

流程图：

![1643078499115](J:\homework\Python学习笔记\Python_notes.assets\1643078499115.png)

自定义中间件2：process_view

```python
from django.middleware.security import SecurityMiddleware


class CustomerMiddleware(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware1 process_request")

    def process_response(self, request, response):
        print("CustomerMiddleware1 process_response")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('CustomerMiddleware1 process_view')


class CustomerMiddleware2(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware2 process_request..")

    def process_response(self, request, response):
        print("CustomerMiddleware2 process_response")

        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
		
        print('======>', callback)
        print('======>', request)
        print('CustomerMiddleware2 process_view')
        # response=callback(request,*callback_args,**callback_kwargs)
        # return response
```

当最后一个中间的process_request到达路由关系映射之后，返回到中间件1的process_view，然后依次往下，到达views函数，最后通过process_response依次返回到达用户。

注意：process_view如果有返回值，会越过其他的process_view以及视图函数，但是所有的process_response都还会执行。

流程图：

![1643078536810](J:\homework\Python学习笔记\Python_notes.assets\1643078536810.png)

之定义中间件3：process_exception

```python
from django.middleware.security import SecurityMiddleware


class CustomerMiddleware(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware1 process_request")

    def process_response(self, request, response):
        print("CustomerMiddleware1 process_response")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('CustomerMiddleware1 process_view')

    def process_exception(self):
        print("CustomerMiddleware1 process_exception...")


class CustomerMiddleware2(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware2 process_request..")

    def process_response(self, request, response):
        print("CustomerMiddleware2 process_response")

        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):

        print('======>', callback)
        print('======>', request)
        print('CustomerMiddleware2 process_view')

    def process_exception(self):
        print("CustomerMiddleware2 process_exception...")
```

当views出现错误时：

流程图：

![1643078563298](J:\homework\Python学习笔记\Python_notes.assets\1643078563298.png)



## 第十四章 爬虫

### 14.1 爬虫基础简介

爬虫：通过编写程序，模拟浏览器上网，然后让其去互联网上抓取数据的过程。

爬虫究竟是合法还是违法的？爬虫在法律中是不被禁止的，但是爬虫具有一定的法律风险，爬虫技术被一些不法分子利用，就会走上一条不归路，恶意的爬虫是违法的。爬虫带来的风险可以体现在如下两个方面：1.爬虫干扰了被访问网站的正常运营，2.爬虫抓取了收到法律保护的特定类型的数据或信息。

如何在使用编写爬虫的过程中避免涉及违法的行为？1.时常的优化自己的程序，避免干扰被访问网站的正常运行，2.使用，传播爬取到的数据时，审查抓取到的内容，如果发现了涉及到用户隐私，商业机密等敏感内容需要及时停止爬取或传播。

爬虫在使用过程中分为三类：

- 通用爬虫：抓取系统重要组成的部分，抓取的是一整张页面数据。
- 聚焦爬虫：是建立在通用爬虫的基础上，抓取的是页面中特定的局部内容。

- 增量式爬虫：检测网站中数据更新的情况，只会抓取网站中最新更新出的数据。

反爬机制：门户网站，可以通过定制相应的策略或技术手段，防止爬虫程序进行网站数据的爬取。

反反爬机制：爬虫程序可以通过定制相关的策略或技术手段，破解门户网站中具备的反爬机制，从而可以获取门户网站中相关的数据。

君子协议：robots.txt协议规定了网站中那些数据可以被爬虫爬取，那些数据不可以被爬取。

![image-20210620152318684](j:\homework\Python学习笔记\Python_notes.assets\image-20210620152318684.png)

http协议：就是服务器和客户端进行数据交互的一种形式。

https协议：安全的超文本传输协议。

常用的请求头信息：

-  User-Agent：请求载体的身份标识
- Connection：请求完毕后，是断开连接还是保持连接

常用的响应头信息：

- ontent-Type：服务器响应回客户端的数据类型

加密方式：

- 对称密钥加密
- 非对称密钥加密
- 证书密钥加密

### 14.2 request模块

爬虫模块分为：urllib模块、requests模块
requests模块：Python中原生的一款基于网络请求的模块，功能非常强大，简单便捷，效率极高。

requests模块作用：模拟记录器发请求。

requests模块编码流程：

- 指定url
  - User-Agent伪装
  - 请求参数的处理

- 发起请求
- 获取响应数据
  - requests中text方法获取的是文本信息，字符串类型
  - requests中content方法获取的是图片等二进制数据类型
  - requests中json()方法获取的是json对象数据类型
- 持久化存储

环境安装：

> pip install reuqests

示例一：爬取搜狗首页的页面数据

```python
import requests

# 指定url
url = "https://www.sogou.com/"

# 发起请求，获取响应数据
response = requests.get(url=url).text

# 持久化存储
with open("./爬虫一血.html", "w", encoding="utf-8") as f:
    f.write(response)

print("爬取数据成功")
```

示例二：爬取搜狗指定词条对应的搜索结果页面（简易网页采集器）

```python
import requests

# UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求载体身份标识为某一款浏览器，说明该请求是一个正常的请求。但是，如果检测到请求的载体身份标识不是基于某一款浏览器的，则表示该请求为不正常的请求（爬虫/自动化），则服务端就有可能拒绝该次的请求。
# UA伪装：让爬虫对应的请求载体身份标识伪装成某一跨浏览器
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

url = "https://www.sogou.com/web"
kw = input("enter a word:").strip()
param = {"query": kw}

response = requests.get(url=url, params=param, headers=headers).text
file_name = "1.爬虫基础/" + kw + '.html'
with open(file_name, "w", encoding="utf-8") as f:
    f.write(response)
print(file_name, "爬取数据成功！")
```

示例三：破解百度翻译--post请求、请求携带参数

```python
import requests
import json

url = "https://fanyi.baidu.com/sug"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}
word = input("enter a word:").strip()
data = {"kw": word}

response = requests.post(url=url, data=data, headers=headers)
# 获取响应数据：json()方法返回的是obj(如果确认响应数据是json类型，才可以时间json()方法)
dic_obj = response.json()
file_name = "1.爬虫基础/" + word + ".json"
with open(file_name, "w", encoding="utf-8") as f:
    json.dump(dic_obj, fp=f, ensure_ascii=False)
    print(word, "爬取成功!")
```

示例四：爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据

```python
import requests
import json

url = "https://movie.douban.com/j/chart/top_list?"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

param = {
    "type": 24,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}

response = requests.get(url=url, params=param, headers=headers).json()
file_name = "1.爬虫基础/豆瓣.json"
with open(file_name, "w", encoding="utf-8") as f:
    json.dump(response, fp=f, ensure_ascii=False)
    print("爬取成功！")
```

示例五：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数据

```python
import requests
import json

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

city = input("input city name:").strip()

data = {
    "cname": "",
    "pid": "",
    "keyword": city,
    "pageIndex": 1,
    "pageSize": 10
}

response_text = requests.post(url=url, data=data, headers=headers).text
file_name = "1.爬虫基础/({})肯德基餐厅.text".format(city)
with open(file_name, "w", encoding="utf-8") as f:
    f.write(response_text)
    print("爬取成功！")
```

### 14.3 数据解析

数据解析原理概述：解析局部的文本内容都会在标签之间或者标签对应的属性中进行存储。

1. 进行指定标签的定位

2. 标签或者标签对应的属性中存储的数据值进行提取（解析）

数据解析分类：正则、bs4、xpath

数据解析原理：1.标签定位    2.提取标签、标签属性中存储的数据值

#### 14.3.1 正则解析

```html
<div class="item-content">
	<h4><a href="http://www.fLdqp.com/zaoanxinyu/97.html" data-type="mip" data-title="个性宣言" title="个性宣言">个性宣言</a></h4>
	<p class="description">每个人都应该有自己的个性宣言，那么大家都知道哪些个性宣言呢？以下就是小编整理的【个性宣言就是这么特别】那些个性宣言精选，喜欢记得收藏。欢迎持续关注我们的后续更新。本文来自语录大</p>
	<p>
		<span>2020-11-07</span>
	</p>
</div>
```

```python
# 正则解析
ex = '<div class="item-content">.*?<p class="description">(.*?)</p>.*?<span>(.*?)</span>.*?</div>'
```

示例：

```python
import requests
import re

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

url = "http://www.fldqp.com/zaoanxinyu/"

page_text = requests.get(url=url, headers=headers).text

ex = '<div class="item-content">.*?<p class="description">(.*?)</p>.*?<span>(.*?)</span>.*?</div>'

text_list = re.findall(ex, page_text, re.S)
with open("./qiushi.text", "w", encoding="utf-8") as f:
    for text in text_list:
        f.write("{}--{}\n".format(text[1], text[0]))
        print("爬取成功！")
```

#### 14.3.2 bs4数据解析

原理：

1. 实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
2. 通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取

环境安装：

> pip install bs4
>
> pip install lxml

实例化BeautifulSoup对象：

- 将文本的html文档终中的数据加载到该对象中

```python
from bs4 import BeautifulSoup

with open("./test.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")
```

- 将互联网获取的页面源码加载到该对象中

```python
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

url = "http://www.fldqp.com/zaoanxinyu/"
page_text = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(page_text, "lxml")
```

数据解析的方法和属性：

```python
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

url = "http://www.fldqp.com/zaoanxinyu/"
page_text = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(page_text, "lxml")
```

- soup.tagName：返回文档中第一次出现tagName对应的标签

```python
print(soup.a)

# <a data-title="励志文章网" data-type="mip" href="http://www.fLdqp.com">励志文章网</a>
```

- soup.find(tagName)：返回文档中第一次出现tagNa么对应的标签

```python
print(soup.find("div")) 等同于 print(soup.div)

# <div class="d-none"></div>
```

- soup.find(tagName,  属性).text/string：通过属性定位

```python
# 获取指定标签的文本
print(soup.find("span", class_="page-link").text)
```

- soup.find_all(tagName)：返回符合要求的指定的标签

```python
# 获取页面中所有的a标签
print(soup.find_all("a"))
```

层级选择器通过属性或标签进行筛选，返回的是一个列表。

- soup.select(标签层级) > 表示一个层级

```python
# 获取第一个a标签href属性的值
print(soup.select(".mipmb-menu > li a")[0]["href"])
```

soup.select(标签层级) 空格 表示多个层级

```python
soup_list = soup.select(".mipmb-menu > li a")
for li in soup_list:
    print(li)
```

- 获取标签之间的文本数据

```python
print(soup.a.text)
print(soup.a.string)
```

- 获取section标签class属性的值

```python
print(soup.section["class"])
```

案例：爬取三国演义书籍

```python
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
}
base_url = "https://www.shicimingju.com"
url = base_url + "/book/sanguoyanyi.html"
page_text = requests.get(url=url, headers=headers).content
# 实例化BeautifulSoup对象，将页面源码加载到该对象中
soup = BeautifulSoup(page_text, "lxml")
# 解析章节标题
li_list = soup.select(".book-mulu > ul> li")
with open("./sanguo.text", "w", encoding="utf-8") as f:
    for li in li_list:
        title = li.a.text
        # 拼接详情页url
        detail_url = base_url + li.a["href"]
        detail_page_text = requests.get(url=detail_url, headers=headers).content
        # 实例化BeautifulSoup对象，将页面源码加载到该对象中
        detail_soup = BeautifulSoup(detail_page_text, "lxml")
        # 解析详情页内容
        div_tag = detail_soup.find("div", class_="chapter_content")
        content = div_tag.text
        f.write("{}:\n{}\n".format(title, content))
        print(title, "爬取成功!")
```

#### 14.3.3 xpath解析

xpath是最常用且最便捷高效的一种解析方式。xpath兼容性强，bs4只支持python语言，xpath可以兼容多种语言。

xpath解析原理：

1. 实例化一个etree对象，且需要将被解析的页面源码数据加载到该对象中
2. 调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获

实例化一个etree对象：

- 将本地的html文档中的源码加载到etree对象中

```python
from lxml import etree
tree = etree.parse("./test.html")
```

- 将页面获取的源码加载到该对象中

```python
from lxml import etree
url = "https://www.shicimingju.com/book/sanguoyanyi.html"
pate_text = requests.get(url=url, headers=headers).content
tree = etree.HTML(page_text)
```

xpath表达式：

> /：表示从根节点开始定位，表示的是一个层级
>
> //：表示多个层级，可以表示从任意位置开始定位
>
> 属性定位：//div[@class="book-mulu"]
>
> 索引定位：//div[@class="book-mulu"]//ul/li[1]/a/text()
>
> 获取标签中直系的文本内容：/text()  
>
> 获取标签中所有文本内容：//text()
>
> 获取属性结尾@属性：//div[@class="book-mulu"]//ul/li[1]/a/@href

- 示例：获取body下的div标签

```python
print(tree.xpath('/html/body/div'))  
```

- 示例：获取html下的所有div标签

```python
print(tree.xpath('/html//div'))  # 等同于tree.xpath("//div")
```

- 示例：获取属性为book-mulu的div标签

```python
print(tree.xpath('//div[@class="book-mulu"]'))
```

- 示例：获取属性为book-mulu的div下的ul标签下的第5个li标签下的a标签的文本内容

```python
print(tree.xpath('//div[@class="book-mulu"]//ul/li[5]/a/text()'))
```

- 示例：获取页面源码中所有第7个li标签的内容

```python
print(tree.xpath('//li[7]//text()'))
```

- 示例：获取属性为book-mulu的div标签下的所有文本内容

```python
tree.xpath('//div[@class="book-mulu"]//text()')
```

- 示例：获取属性为top_left_menu的div标下的ul下的第3个li下的a标签href属性的值

```python
print(tree.xpath('//div[@id="top_left_menu"]//ul/li[3]/a/@href'))
```

案例一：xpath解析58同城二手房

```python
import requests
import os
from lxml import etree

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
}

url = "https://bj.58.com/ershoufang/"

page_text = requests.get(url=url, headers=headers).text
# 将页面文档加载到etree对象中
tree = etree.HTML(page_text)

title_list = tree.xpath('//div[@class="property-content-title"]//h3/text()')
img_list = tree.xpath('//div[@class="property-image"]//img/@src')

if not os.path.exists("./58img"):
    os.mkdir("./58img")

for title in title_list:
    title_path = "./58img/" + title + ".png"
    for img in img_list:
        img_data = requests.get(url=img, headers=headers).content
        with open(title_path, "wb") as f:
            f.write(img_data)
    print(title, "爬取成功!")
```

案例二：xpath解析4k图片

```python
import requests
from lxml import etree
import os

base_url = "http://pic.netbian.com"

headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

response = requests.get(url=base_url + "/4kmeinv/", headers=headers).text

tree = etree.HTML(response)

li_list = tree.xpath('//div[@class="slist"]//ul/li')

if not os.path.exists("./picLibs"):
    os.mkdir("./picLibs")

for li in li_list:
    img_name = li.xpath("./a/img/@alt")[0] + ".jpg"
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    img_src = base_url + li.xpath('./a/img/@src')[0]

    img_data = requests.get(url=img_src, headers=headers).content
    with open("./picLibs/" + img_name, "wb") as f:
        f.write(img_data)
    print(img_name, "爬取成功！")
```

案例三：xpath解析全国城市名称

方式一：

```python
import requests
import os
from lxml import etree

url = "https://www.aqistudy.cn/historydata/"

headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)

li_list = tree.xpath('//div[@class="bottom"]/ul/li')
all_city_name = []
# 热门城市名称
for li in li_list:
    hot_city_name = li.xpath('./a/text()')[0]
    all_city_name.append(hot_city_name)

# 全部城市名称
city_name_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
for li in city_name_list:
    city_name = li.xpath('./a/text()')[0]
    all_city_name.append(city_name)

print(all_city_name)
```

方式二：

```python
import requests
import os
from lxml import etree

url = "https://www.aqistudy.cn/historydata/"

headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)

# 解析热门和全部的城市名称
li_list = tree.xpath(
    '//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
all_city_name = []
for li in li_list:
    city_name = li.xpath('./text()')[0]
    all_city_name.append(city_name)

print(all_city_name)
```

### 14.4 验证码识别

反爬机制：验证码，识别验证码图片中的数据，用于模拟登录操作。

识别验证码的操作：第三方自动识别，超级鹰：http://www.chaojiying.com/api-14.html

超级鹰的使用流程：

1. 用户中心 > 软件ID 生成一个用来接入接口的软件ID
2. 参考开发文档，下载示例代码

```python
import requests
from lxml import etree
from chaojiying import Chaojiying_Client

headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

base_url = "https://so.gushiwen.org"
url = base_url + "/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx"
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
# 获取验证码路径
src_img_code = base_url + tree.xpath('//*[@id="imgCode"]/@src')[0]
# 获取验证码
img_data = requests.get(url=src_img_code, headers=headers).content

chaoying = Chaojiying_Client("43815687", "43815687q0.", "918871")
print(chaoying.PostPic(img_data, 1004))  # {'err_no': 0, 'err_str': 'OK', 'pic_id': '9145317126580700002', 'pic_str': '1t2v', 'md5': '074f471aa30d1ef020633d5309905df6'}
```

示例：古诗文网模拟登录

```python
import requests
from lxml import etree
from chaojiying import Chaojiying_Client

session = requests.Session()

headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

base_url = "https://so.gushiwen.org"
url = base_url + "/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx"
page_text = session.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
# 获取验证码路径
src_img_code = base_url + tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = session.get(url=src_img_code, headers=headers).content
with open("./3.验证码识别/code.jpg", "wb") as f:
    f.write(img_data)

# 解析动态参数
__VIEWSTATE = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
__VIEWSTATEGENERATOR = tree.xpath(
    '//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]

chaoying = Chaojiying_Client("43815687", "43815687q0.", "918871")
code_text = chaoying.PostPic(
    img_data, 1004
)  # {'err_no': 0, 'err_str': 'OK', 'pic_id': '9145317126580700002', 'pic_str': '1t2v', 'md5': '074f471aa30d1ef020633d5309905df6'}
pic_str = code_text['pic_str']
print(pic_str)
print(type(pic_str))

post_url = "https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx"
data = {
    "__VIEWSTATE": __VIEWSTATE,
    "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
    "from": "http://so.gushiwen.org/user/collect.aspx",
    "email": "15010008824",
    "pwd": "43815687q0.",
    "code": pic_str,
    "denglu": "登录"
}

response = session.post(url=post_url, data=data, headers=headers)
page_text = response.text
print(response.status_code)
with open('./3.验证码识别/ghiwen.html', 'w', encoding='utf-8') as f:
    f.write(page_text)

```

### 14.5 requests高级操作

一般系统中很多的接口是基于登录后才可以操作的，在向服务端发送请求的时候，需要携带上登录时生成的cookie值。

session会话对象作用：如果请求过程中产生了cookie，则该cookie会被存储在session对象中，发送给服务端。

示例：

```python
# 创建一个session对象
session = requests.Session()
# 使用session对象进行登录
page_text = session.post(url=url, data=data, headers=headers).text
```

什么是代理：代理是服务器。作用：：破解IP这种反爬机制，突破自身IP访问的限制，隐藏自身真是的IP。

代理相关的网站：

1. http://www.kxdaili.com/dailiip/2/1.html
2. www.goubanjia.com

代理IP的匿名程度：

- 透明：服务器知道该次请求使用了代理，也知道请求对应的真实ip
- 匿名：知道使用了代理，不知道真实ip
- 高匿：不知道使用了代理，更不知道真实的ip

示例：

```python
import requests
url = "http://httpbin.org/ip"

headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}
proxy = {'http': '39.186.205.225:8118'}

response = requests.get(url=url, headers=headers, proxies=proxy)

print(response.text)  # {"origin": "39.186.205.225"}
```

### 14.6 高性能异步爬虫

目的：在爬虫中使用异步实现高性能的数据爬取操作。

异步爬虫的方式：

1. 多线程、多进程（不建议）：
   - 好处：可以为相关阻塞的操作单独开启线程或者进程，阻塞操作就可以异步执行。
   - 弊端：无法无限制的开启多线程和多进程。
2. 线程池、进程池（适当的使用）：
   - 好处：我们可以降低系统对进程或者线程创建和销毁的一个频率，从而很好的降低系统的开销。
   - 弊端：池中线程或进程的数量是有上限的。
3. 单线程+异步协程（推荐）：
   - get_event_loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足某些条件的时候，函数就会被循环执行。
   - coroutine：协程对象，我们可以将协程对象注册到事件循环中，它会被事件循环调用。我们可以使用 `async` 关键字来定义一个方法，这个方法在调用时不会被立即执行，二十返回一个协程对象。
   - task：任务，它是对协程对象的进一步封装，包含了任务的各个状态。
   - future：代表将来执行或还没有执行的任务，实际上和 `task` 没有本质的区别。
   - async：定义一个协程。
   - await：用来挂起阻塞方法的执行。

示例一：普通爬虫

```python
import requests

headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

urls = [
    "http://pic.netbian.com/uploads/allimg/210508/152327-16204586078720.jpg",
    "http://pic.netbian.com/uploads/allimg/210617/193149-16239295098fb3.jpg",
    "http://pic.netbian.com/uploads/allimg/210617/192555-1623929155c29b.jpg"
]


def get_content(url):
    print("正在爬取", url)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content


def parse_content(content):
    print("响应数据的长度为：", len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)
```

**线程的基本使用：**

示例一：普通

```python
import time

# 使用单线程串行方式执行


def get_page(str):
    print("正在下载", str)
    time.sleep(2)
    print("下载成功", str)


val_list = ["iamge_a", "iamge_b", "iamge_c"]

start_time = time.time()
for i in range(len(val_list)):
    get_page(val_list[i])
end_time = time.time()

print("%d second" % (end_time - start_time))
```

示例二：线程

```python
import time

# 导入线程池模块对应的类
from multiprocessing.dummy import Pool

start_time = time.time()


def get_page(str):
    print("正在下载", str)
    time.sleep(2)
    print("下载成功", str)


val_list = ["iamge_a", "iamge_b", "iamge_c"]

# 实例化一个线程池对象
pool = Pool(4)
# 将列表中每一个元素传递给get_page进行处理
pool.map(get_page, val_list)
# 关闭pool，使其不在接受新的（主线程）任务
pool.close()
# 主线程阻塞后，让子进程继续运行完成，子进程运行完后，再把主进程全部关掉。
pool.join()
end_time = time.time()
print("用时：", end_time - start_time)
```

**协程回顾**

示例：async修饰的函数，调用之后返回一个协程对象

```python
import asyncio


async def func(url):
    print('正在请求的url是', url)
    print('请求成功,', url)


# async修饰的函数，调用之后返回一个协程对象
c = func("wwww.baidu.com")

# 创建一个事件循环对象
loop = asyncio.get_event_loop()
# 将协程对象注册到loop中，然后启动loop
loop.run_until_complete(c)
```

示例：task的使用

```python
import asyncio


async def func(url):
    print('正在请求的url是', url)
    print('请求成功,', url)


# async修饰的函数，调用之后返回一个协程对象
c = func("wwww.baidu.com")
# 创建一个循环对象
loop = asyncio.get_event_loop()
# 基于loop创建一个task对象
task = loop.create_task(c)
print(task) # <Task pending name='Task-1' coro=<func() running
# 将task任务注册到loop中，然后启动loop
loop.run_until_complete(task) # <Task finished name='Task-1' coro=<func() done
print(task)
```

示例：future的使用

```python
import asyncio


async def func(url):
    print('正在请求的url是', url)
    print('请求成功,', url)


# async修饰的函数，调用之后返回一个协程对象
c = func("wwww.baidu.com")
# 创建一个事件循环对象
loop = asyncio.get_event_loop()
# 创建一个future对象
future = asyncio.ensure_future(c)
print(future)
# 将future任务注册到loop中，然后启动loop
loop.run_until_complete(future)
print(future)
```

示例：绑定回调

```python
import asyncio


async def func(url):
    print('正在请求的url是', url)
    print('请求成功,', url)
    return "666"


# async修饰的函数，调用之后返回一个协程对象
c = func("wwww.baidu.com")

def callback_func(task):
    # result()返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result())


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(c)
# 将回调函数绑定到任务对象中
future.add_done_callback(callback_func)
loop.run_until_complete(future)
```

示例：多任务协程对象

```python
import asyncio
import time


async def func(url):
    print("正在下载", url)
    # 1.在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步。
    # time.sleep(2)

    # 当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print("下载完成", url)


urls = ['www.baidu.com', 'www.sogou.com', 'www.goubanjia.com']
start_time = time.time()
loop = asyncio.get_event_loop()
tasks = []
for url in urls:
    c = func(url)
    task = loop.create_task(c)
    tasks.append(task)

# 需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))

print(time.time() - start_time)
```

**基于flask服务多任务异步协程**

示例：flask服务

```python
from flask import Flask
import time

app = Flask(__name__)

@app.route("/index")
def cs_index():
    time.sleep(2)
    return "hello index..."

@app.route("/login")
def cs_login():
    time.sleep(2)
    return "hello login..."

@app.route("/logout")
def cs_logout():
    time.sleep(2)
    return "hello logout..."


if __name__ == '__main__':
    app.run(threaded=True)
```

示例一：基于flask服务多任务异步协程【requests.get】基于同步

```python
import requests
import asyncio
import time

start = time.time()
urls = [
    "http://127.0.0.1:5000/index", "http://127.0.0.1:5000/login",
    "http://127.0.0.1:5000/logout"
]


async def get_page(url):
    print("正在下载", url)
    # requests.get是基于同步，必须使用异步的网络请求模块进行指定url的请求发送
    # aiohttp：是基于异步网络请求的模块
    response = requests.get(url=url)
    print("下载完成，", response.text)


tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()

print("总耗时：", end - start)

"""
正在下载 http://127.0.0.1:5000/index
下载完成， hello index...
正在下载 http://127.0.0.1:5000/login
下载完成， hello login...
正在下载 http://127.0.0.1:5000/logout
下载完成， hello logout...
总耗时： 6.052320241928101
"""
```

示例：基于flask服务多任务异步协程【aiothhp】基于异步

```python
import aiohttp
import asyncio
import time

start_time = time.time()
urls = [
    "http://127.0.0.1:5000/index", "http://127.0.0.1:5000/login",
    "http://127.0.0.1:5000/logout"
]


async def get_page(url):
    print("正在下载", url)
    async with aiohttp.ClientSession() as session:
        # 异步get()发送请求对应的参数：headers,params,proxy
        # 异步post()发送请求对应的参数：herders,data,proxy
        # text()返回字符串形式的响应数据
        # read()返回二进制形式的响应数据
        # json()返回json对象
        # 注意：获取响应数据操作之前一定要使用awati进行手动挂起
        async with await session.get(url) as response:
            page_text = await response.text()
    print("下载完成", url)


tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end_time = time.time()

print("总耗时：", end_time - start_time)

```

### 14.7 动态加载数据

selenium是基于浏览器自动化的一个模块。

selenium与爬虫之间的关联关系：

- 便捷的获取网站中动态加载的数据
- 便捷实现模拟登录

selenium环境搭建：

1. 环境安装：pip install selenium
2. 下载浏览器驱动路径：http://chromedriver.storage.googleapis.com/index.html
3. 驱动程序和浏览器的映射关系：http://blog.csdn.net/huilan_same/article/details/51896672

基于浏览器编写自动化代码：

1. 发起请求：get(url)
2. 标签定位：find系列方法
3. 标签交互：send_keys('xxx')
4. 执行js程序：excute_script('jsCode')
5. 前进，后退：back(),forward()
6. 关闭浏览器：quit()

selenium处理iframe问题：

如果定位的标签存在于iframe标签之中，则必须使用driver.switch_to.frame(id)。

跳出iframe：driver.switch_to.default_content()

动作链（拖动）：from selenium.webdriver import ActionChains

实例化一个动作链对象：action = ActionChains(bro)

- 鼠标事件：
  1. 右键单击：context_click()
  2. 双击：double_click()
  3. 鼠标悬停：move_to_element()
  4. 按下左键不松手：click_and_hold()
  5. 坐标移动：move_by_offset(x,y)
  6. 动作链立即执行：perform()
  7. 释放动作链对象：action.release()

- 键盘事件：
  1. 删除键backspace：find_element_by_id().send_keys(Keys.BACK_SPACE)
  2. Ctrl+a：.send_keys(Keys.CONTROL, 'a')
  3. 回车：.send_keys(Keys.ENTER)

示例一：selenium 程序流程演示

```python
from selenium import webdriver
from time import sleep

# 去掉浏览器顶部自动化监控字样
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches",
                                       ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)
# 打开百度
driver.get("http://www.baidu.com")
# 窗口最大化
driver.maximize_window()
# 输入美女
driver.find_element_by_id("kw").send_keys("美女")
sleep(2)
# 点击搜索
driver.find_element_by_id("su").click()
sleep(2)
```

示例二：selenium的基础用法

```python
from selenium import webdriver
from lxml import etree
from time import sleep
import requests
import os

headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches",
                                       ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://pic.netbian.com/4kmeinv/")

# 获取页面源码数据
page_text = driver.page_source

tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]//ul/li')

if not os.path.exists("7.动态加载数据/img"):
    os.mkdir("7.动态加载数据/img")

for li in li_list:
    img_name = li.xpath("./a/img/@alt")[0] + ".jpg"
    img_src = "https://pic.netbian.com/" + li.xpath('./a/img/@src')[0]
    response = requests.get(url=img_src, headers=headers).content
    upload_img = "7.动态加载数据/img/" + img_name
    with open(upload_img, "wb") as f:
        f.write(response)
    print(img_name, "爬取成功！")

```

示例三：selenium其他操作

```python
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.taobao.com/')
driver.maximize_window()

# 标签定位
search_input = driver.find_element_by_id('q').send_keys('Iphone')

# js操作，向下滚动
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
# 点击搜索按钮
btn = driver.find_element_by_css_selector('.btn-search')
btn.click()

driver.get('https://www.baidu.com')
sleep(2)
# 回退
driver.back()
sleep(2)
# 前进
driver.forward()

driver.quit()

```

示例四：动作链姐iframe的处理

```python
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches",
                                       ['enable-automation'])
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(
    'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 如果定位的标签是存在于iframe标签之中的则必须通过如下操作在进行标签定位
# 定位iframe作用域
driver.switch_to.frame('iframeResult')
div = driver.find_element_by_id('draggable')

# 实例化一个动作链
action = ActionChains(driver)
# 长按指定的标签
action.click_and_hold(div)

for i in range(5):
    # perform()立即执行动作
    # move_by_offset(x,y) 移动到指定的坐标位置
    action.move_by_offset(17, 0).perform()
    sleep(0.5)

sleep(2)

# 释放动作链
action.release()
# 关闭浏览器
driver.quit()


```

示例五：实现五可视化界面+规避检测

```python
from selenium import webdriver
from time import sleep
# 实现无可视化界面
from selenium.webdriver.chrome.options import Options
# 实现规避检测
from selenium.webdriver import ChromeOptions

# 实现无可视化界面
chrome_option = Options()
chrome_option.add_argument("--headless")
chrome_option.add_argument("--disable-gpu")

# 实现规避检测
options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 如何实现让selenium规避被检测到的风险
driver = webdriver.Chrome(chrome_options=chrome_option, options=options)

driver.get('https://www.baidu.com')

print(driver.page_source)

sleep(3)
driver.quit()

```

示例六：12306登录

```python
import time
from chaojiying import Chaojiying_Client
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from PIL import Image  # pip3.8 install Pillow

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches",
                                       ['enable-automation'])

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://kyfw.12306.cn/otn/resources/login.html)
driver.find_element_by_link_text("账号登录").click()
sleep(2)
driver.save_screenshot("7.动态加载数据/aa.png")

code_img_ele = driver.find_elements_by_xpath('//*[@id="J-loginImg"]')[0]

# 获取图片的坐标
code_location = code_img_ele.location
print(code_location)  # {'x': 1216, 'y': 292}
# 获取图片的长宽
code_size = code_img_ele.size
print(code_size)  # {'height': 188, 'width': 300}

rangle = (int(code_location["x"]), int(code_location["y"]),
          int(code_location["x"]) + int(code_size["width"]),
          int(code_location["y"]) + int(code_size["height"]))

code_img = Image.open("7.动态加载数据/aa.png")
code_img_name = "7.动态加载数据/code.png"

# 根据指定的区域进行裁剪，保存为code.png
frame = code_img.crop(rangle)
frame.save(code_img_name)

# 调用超级鹰方法，将验证码图片提交给超级鹰进行识别
chaojiying = Chaojiying_Client("43815687", "43815687q0.", "918871")

img = open(code_img_name, "rb").read()
# {'err_no': 0, 'err_str': 'OK', 'pic_id': '9147116046580700020', 'pic_str': '261,76|38,146', 'md5': '14f78c004ed4631a83f8b6a0d796d945'}
# print(chaojiying.PostPic(img, 9004))
# 258,68|59,142
# print(chaojiying.PostPic(img, 9004)["pic_str"])
result = chaojiying.PostPic(img, 9004)["pic_str"]
# 存储即将被点击的坐标
all_list = []
if "|" in result:
    lis = result.split("|")
    count = len(lis)
    for i in range(count):
        xy_list = []
        x = int(lis[i].split(",")[0])
        y = int(lis[i].split(",")[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(",")[0])
    y = int(result.split(",")[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
# [[271, 79], [51, 162]]
print(all_list)

# 便利列表，使用动作链对每一个列表元素对应的坐标进行点击操作
for index in all_list:
    x = index[0]
    y = index[1]
    ActionChains(driver).move_to_element_with_offset(code_img_ele, x,
                                                     y).click().perform()
    sleep(0.5)

# 登录操作
driver.find_element_by_id("J-userName").send_keys("zzq43815687")
driver.find_element_by_id("J-password").send_keys("zzq43815687")
driver.find_element_by_id("J-login").click()
sleep(2)

# 拖拽验证码
div = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
action = ActionChains(driver)
action.click_and_hold(div)
for i in range(10):
    action.move_by_offset(50, 0).perform()
action.release()
sleep(10)

```

### 14.8 scrapy框架

scrapy框架是一个继承了很多功能并且具有很想通用性的一个项目模板。具有高性能的持久化存储，异步的数据下载，高性能的数据解析，分布式等功能。

#### 14.8.1 框架的基本使用

环境的安装：

> Mac or Linux：pip install scrapy
>
> windows：
>
> - pip install wheel
> - 下载twisted，下载地址：http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
> - 安装twisted：pip install Twisted‑17.1.0‑cp36‑cp36m‑win_amd64.whl
> - pip install pywin32
> - pip install scrapy
>
> 验证环境：终端输入指令scrapy，没有报错表示安装成功！

创建及执行工程：

> - 创建一个工程：scrapy startproject xxxPro
> - cd xxxPro
> - 在spiders字母不创建一个爬虫文件
>   - scrapy genspider spiderName  www.xxx.com
> - 执行工程
>   - scrapy crawl spiderName

配置文件设置：

> - ROBOTSTXT_OBEY = False
> - LOG_LEVEL = "ERROR"

#### 14.8.2 持久化存储

基于终端命令：

- 要求：只可以将parse方法的返回值存储到本地的文本文件中
- 注意：持久化存储对应的文本文件的类型只可以为 `'json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle'`格式的文件
- 命令：scrapy crawl -o filePath
- 好处：简洁高效
- 缺点：局限性比较强（数据存储格式有限）

基于管道：

- 编码流程：
  - 解析数据
  - 在item类中定义相关的属性

  ```python
  # items.py
  class QiubaiproItem(scrapy.Item):
      # define the fields for your item here like:
      author = scrapy.Field()
      content = scrapy.Field()
  ```

  - 将解析的数据封装存储到item类型的对象
  - 将item类型的对象提交给管道进行持久化存储的操作

  ```python
  from qiubaiPro.items import QiubaiproItem
  class QiubaiSpider(scrapy.Spider):
      name = 'qiubai'
      # allowed_domains = ['www.xxx.com']
      start_urls = ['https://www.qiushibaike.com/text/']
      all_data = []
      def parse(self, response):
          div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
          for div in div_list:
              author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
              content = div.xpath('./a[1]/div/span//text()').extract()
              content = "".join(content)
  
              item = QiubaiproItem()
              item["author"] = author
              item["content"] = content
              yield item # 将item提交给了管道
  ```

  - 在管道类的process_item中要将其接收到的item对象中存储的数据进行持久化存储

  ```python
  class QiubaiproPipeline:
      f = None
  
      def open_spider(self, spider):
          print("开始爬虫")
          self.f = open("./qiubai.txt", "w", encoding="utf-8")
  
      def process_item(self, item, spider):
          author = item["author"]
          content = item["content"]
          self.f.write(author + ":" + content + "\n")
          return item
  
      def close_spider(self, spider):
          print("结束爬虫")
          self.f.close()
  ```

  - 在配置文件中开启管道，300表示优先级，数值越小，优先级越高

  ```python
  ITEM_PIPELINES = {
     'qiubaiPro.pipelines.QiubaiproPipeline': 300,
  }
  LOG_FILE = "log.txt"
  ```
  
- 好处：推荐使用（推荐）

练习一：将爬取到的数据一份存储到本地一份存储到数据库

1. 管道文件中一个管道类对应的是将数据存储到一种平台
2. 爬虫文件提交的item只会给管道文件中第一个被执行的管道类接收
3. process_item中的 `return item` 表示将item传递给下一个即将执行的管道类

4. 配置文件需要添加新增加的管道类

```python
ITEM_PIPELINES = {
    'qiubaiPro.pipelines.QiubaiproPipeline': 300,
    'qiubaiPro.pipelines.MySQLproPipleline': 301,
}
```

```python
from enum import IntEnum
from itemadapter import ItemAdapter
import pymysql


class QiubaiproPipeline:
    f = None

    def open_spider(self, spider):
        print("开始爬虫")
        self.f = open("./qiubai.txt", "w", encoding="utf-8")

    def process_item(self, item, spider):
        author = item["author"]
        content = item["content"]
        self.f.write(author + ":" + content + "\n")
        return item  # 会传递给下一个即将被执行的管道类

    def close_spider(self, spider):
        print("结束爬虫")
        self.f.close()


# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
class MySQLproPipleline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host="127.0.0.1",
                                    port=3306,
                                    user="root",
                                    password="123456",
                                    db="scrapy",
                                    charset="utf8")

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("insert into qiubai values('%s', '%s')" %
                                (item["author"], item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
```

练习二：基于Spider的全站数据爬取

- 手动发送请求：callback回调函数是专门用于数据解析

```python
import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/meinvxiaohua/']

    # 生成一个通用的url模板（不可变）
    url = "http://www.521609.com/meinvxiaohua/list12%d.html"
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//div[@class="index_img list_center"]/ul/li')
        for li in li_list:
            img_name = li.xpath(
                './a[2]/text() | ./a[2]/b/text()').extract_first()
            print(img_name)
        if self.page_num <= 11:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 手动发送请求：callback回调函数是专门用于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)
```

练习三：请求传参

使用场景：爬取解析的数据不在同一张页面中。（深度爬取）

```python
# news.py
import scrapy
from newsPro.items import NewsproItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.shicimingju.com/']

    def parse_detail(self, response):
        item = response.meta["item"]
        author = response.xpath(
            '//*[@id="item_div"]/div[2]/a/text()').extract_first()
        item["author"] = author
        # print(author)
        yield item

    def parse(self, response):
        div_list = response.xpath('//div[@id="main_left"]/div')
        for li in div_list:
            item = NewsproItem()
            title = li.xpath('./div[2]/h3/a/text()').extract_first()
            item["title"] = title
            detail_url = "https://www.shicimingju.com" + li.xpath(
                './div[2]/h3/a/@href').extract_first()
            # print(title, detail_url)
            yield scrapy.Request(url=detail_url,
                                 callback=self.parse_detail,
                                 meta={"item": item})

```

```python
ITEM_PIPELINES = {
    'newsPro.pipelines.NewsproPipeline': 300,
}
```

#### 14.8.3 图片爬取

基于scrapy爬取字符串类型的数据和爬取图片类型的数据之间的区别：

- 字符串：只需要基于xpath进行解析且提交管道进行持久化存储
- 图片：xpath解析出图片src的属性值，单独的对图片地址发起请求获取图片二进制类型的数据

ImgesPipleline：

> 只需要将img的src的属性值进行解析，提交到管道，管道就会对图片的src发送请求，获取图片的二进制类型的数据，且还会帮我们进行持久化存储。

使用流程：

- 数据解析
- 将存储图片地址的item提交到指定的管道类

```python
from imgPro.items import ImgproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['http://pic.netbian.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        
        div_list = response.xpath("//div[@id='container']/div")
        for div in div_list:
            item = ImgproItem()
            # 解析使用伪属性
            src = "https:" + div.xpath("./div/a/img/@src2").extract_first()
            item["src"] = src
            yield item
```

- 在管道文件中自定制一个基于ImagesPipeline的管道类

```python
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class ImgPipeline(ImagesPipeline):

    # 可以根据图片地址进行图片数据的请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["src"])

    # 指定图片的名称
    def file_path(self, request, response=None, info=None):
        img_name = request.url.split("/")[-1]
        return img_name

    # 返回给下一个即将被执行的管道类
    def item_completed(self, results, item, info):
        return item
```

- 修改配置文件：
  - 指定图片路径
  - 指定开启的管道类

```python
ITEM_PIPELINES = {
    'imgPro.pipelines.ImgPipeline': 300,
}
# 指定图片存储的目录
IMAGES_STORE = './8.scrapy/imgPro/imgs'
```

#### 18.8.4 五大核心组件

![image-20210721114046503](j:\homework\Python学习笔记\Python_notes.assets\image-20210721114046503.png)

爬虫（Spider）：爬虫是主要干活的，用于特定的网页中提取自己需要的信息，即所谓的实体（item），用户也可以从中提取出链接，让Scrapy继续抓取下一个页面。

引擎（Scheduler）：用来处理整个系统的数据流处理,，触发事务(框架核心)。

调度器（Scheduler）：用来接受引擎发过来的请求，压入队列中, 并在引擎再次请求的时候返回。可以想像成一个URL（抓取网页的网址或者说是链接）的优先队列,，由它来决定下一个要抓取的网址是什么,，同时去除重复的网址。

下载器（Downloader）：用于下载网页内容，并将网页内容返回给Spider（Scrapy下载器是建立在twisted这个高效的异步模型上的）。

项目管道（Pipleline）：负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体，验证实体的有效性，清楚不需要的信息，当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。

#### 14.8.5 中间件

位置：引擎和下载器之间

作用：批量拦截整个工程中所有的请求和响应

拦截请求：

- UA伪装：process_request
-  代理IP：process_exception  ： return request

拦截响应：

- 纂改响应数据，响应对象
- 需求：爬取网易新闻中的新闻数据（标题和内容）
  1. 通过网易新闻的首页解析出五大板块对应的详情页的url（没有动态加载）
  2. 每一个板块对应的新闻标题都是动态加载出来的（动态加载）
  3. 通过解析出每一条新闻详情页的url获取详情页的页面源码，解析出新闻内容

示例：拦截请求

```python
# spider
import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        content = response.text
        print(content)
```

```python
# middlewares
from itemadapter import is_item, ItemAdapter
from scrapy import signals
import random


class MiddleproDownloaderMiddleware:

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

    proxy_http = ["101.205.120.102", "139.196.122.123", "139.196.153.156"]
    proxy_https = ["183.195.106.118", "47.100.228.154", "218.2.214.107"]

    # 拦截请求
    def process_request(self, request, spider):
        # UA伪装
        request.headers["User-Agent"] = random.choice(self.user_agent_list)

        # 验证代理操作是否生效
        request.meta['proxy'] = 'http://101.205.120.102'
        return None

    # 拦截所有的响应
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    # 拦截发生异常的请求
    def process_exception(self, request, exception, spider):
        if request.url.split(":")[0] == "http":
            request.meta["proxy"] = "http://" + random.choice(self.proxy_http)
        else:
            request.meta["procy"] = "https://" + random.choice(
                self.proxy_https)
        # 异常修改后返回request继续发送请求
        return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

```

示例：拦截响应

```python
# spider
import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']

    models_urls = []

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def parse(self, response):
        li_list = response.xpath('//div[@class="ns_area list"]/ul/li')

        a_list = [2, 3, 5, 6]
        for index in a_list:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            print(model_url)
            self.models_urls.append(model_url)

        for url in self.models_urls:
            yield scrapy.Request(url=url, callback=self.parse_model)

    def parse_model(self, response):
        div_list = response.xpath('//div[@class="ndi_main"]/div')
        for div in div_list:
            item = WangyiproItem()
            title = div.xpath('./div/h3/a/text() | ./div/div[1]/h3/a/text()'
                              ).extract_first()
            
            new_detail_url = div.xpath(
                './div/h3/a/@href | ./div/div[1]/h3/a/@href').extract_first()
            item["title"] = title

            yield scrapy.Request(url=new_detail_url,
                                 callback=self.parse_detail,
                                 meta={"item": item})

    def parse_detail(self, response):
        content = response.xpath('//*[@id="content"]/div[2]/text()').extract()
        content = "".join(content)

        item = response.meta["item"]
        item["content"] = content
        yield item

    def closed(self, spider):
        self.driver.quit()
```

```python
# items
import scrapy


class WangyiproItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    content = scrapy.Field()
```

```python
# middlewares
# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from time import sleep
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse


class WangyiproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None
	# 拦截响应
    def process_response(self, request, response, spider):
        # spider获取爬虫类中的对象
        driver = spider.driver

        if request.url in spider.models_urls:
            driver.get(request.url)
            sleep(2)
            # 动态加载页面源码
            page_text = driver.page_source
            # 五大模块对应的响应对象,针对定位到的response进行纂改
            # 实例化一个新的响应对象，（符合需求：包含动态加载出的新闻数据）替代原来旧的响应对象
            # 基于selenium编辑获取动态加载数据
            new_response = HtmlResponse(url=request.url,
                                        body=page_text,
                                        encoding='utf-8',
                                        request=request)
            return new_response
        else:
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
```

```python
# settings
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
ROBOTSTXT_OBEY = False
LOG_LEVEL = "ERROR"
DOWNLOADER_MIDDLEWARES = {
   'wangyiPro.middlewares.WangyiproDownloaderMiddleware': 543,
}
ITEM_PIPELINES = {
   'wangyiPro.pipelines.WangyiproPipeline': 300,
}
```

#### 14.8.6 cookie操作

使用scrapy框架，登录成功后，框架会自动记录cookie，不用特意指定。

```python
import scrapy


class SessionSpider(scrapy.Spider):
    name = 'session'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'https://mail.263.net/wm2e/mail/login/show/loginShowAction_getEnterpriseBulletinUrl.do?'
    ]
    # 重写开始请求方法
    def start_requests(self):
        # 指定请求参数
        data = {"usr": "zhangzhiqiang96@camelotchina.com", "passWord": "P@ssw0rd1111"}

        for url in self.start_urls:
            yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)

    def parse(self, response):
       with open("./session.html", "w", encoding="utf-8")as f:
           f.write(response.text)
```

#### 14.8.7 CrawlSpider

CrawlSpider是Spider的一个子类，基于CrawlSpider可以实现全站数据的爬取。

全站数据爬取的方式：

- 基于spider：手动爬取
- 基于CrawlSpider爬取

CrawlSpider的使用：

1. 创建一个流程：scrapy startproject xxx

2. cd xxx

3. 创建爬虫文件（CrawlSpider）：

   - scrapy genspider -t crawl xxx www.xxx.com

   - 链接提取器：
     - 作用：根据指定的规则（allow）进行指定链接的提取
   - 规则解析器：
     - 作用：将链接提取器渠道的链接进行指定规则（callback）的解析

需求：爬取sun网站中的编号，新闻标题，新闻内容，编号

- 分析：爬取的数据没有在同一张页面中
- 可以使用链接提取器提取所有的页面链接
- 让链接提取器提取所有的新闻详情页的链接

```python
# spider
import scrapy
from scrapy import item
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem, DetailproItem


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = [https://wzzdg.sun0769.com/political/index/supervise?page=']
    start_urls = ['https://wzzdg.sun0769.com/political/index/supervise?page=']

    # 链接提取器，根据指定的规则(正则)进行指定链接的提取
    link = LinkExtractor(allow=r'page=\d+')
    detail_link = LinkExtractor(allow=r'/political/politics/index\?id=\d+')
    rules = (
        # 规则解析器：将链接提取器提取到的链接进行指定规则（callback）解析操作
        # follow=True：可以将链接提取器继续用作到链接提取器提取到的链接所对应的页面中
        Rule(link, callback='parse_item', follow=True),
        Rule(detail_link, callback='detail_parse_item'))

    # 解析新闻编号和新闻标题
    """
    1.如下两个解析方法中不可以实现请求传参（meta）
    2.无法实现封装到一个item中，需要依次存储到两个item
    """
    def parse_item(self, response):
        li_list = response.xpath('//div[@class="width-12"]/ul/li')
        for li in li_list:
            news_num = li.xpath("./span[1]/text()").extract_first()
            news_title = li.xpath("./span[3]/a/text()").extract_first()
            item = SunproItem()
            item["news_num"] = news_num
            item["news_title"] = news_title
            yield item

    def detail_parse_item(self, response):
        detail_num = response.xpath(
            '/html//div[3]/div[2]/div[2]/div[1]/span[4]/text() | /html//div[3]/div[2]/div[2]/div[1]/span[3]/text()'
        ).extract_first()
        detail_content = response.xpath(
            '/html//div[3]/div[2]/div[2]/div[2]/pre/text()').extract()
        detail_content = "".join(detail_content)
        detail_item = DetailproItem()
        detail_item["detail_num"] = detail_num.split("：")[1]
        detail_item["detail_content"] = detail_content
        yield detail_item
```

```python
# items
import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    news_num = scrapy.Field()
    news_title = scrapy.Field()

class DetailproItem(scrapy.Item):
    detail_num = scrapy.Field()
    detail_content = scrapy.Field()
```

```python
# piplines
from itemadapter import ItemAdapter


class SunproPipeline:
    def process_item(self, item, spider):
        if item.__class__.__name__ == "DetailproItem":
            print(item["detail_num"], item["detail_content"])
        else:
            print(item["news_num"], item["news_title"])
        return item
```

#### 14.8.8 分布式爬虫

一、分布式爬虫架构

在前面我们已经实现了Scrapy爬虫，虽然爬虫是异步加多线程的，但是我们只能在一台主机上运行，所以爬取效率还是有限的，分布式爬虫则是将多台主机组合起来，共同完成一个爬取任务，这将大大提高爬取的效率。

![20180525220702269](j:\homework\Python学习笔记\Python_notes.assets\20180525220702269.png)

Scrapy单机爬虫中有一个本地爬取队列Queue，这个队列是利用deque模块实现的。如果新的Request生成就会放到队列里面，随后Request被Scheduler调度。之后，Request交给Downloader执行爬取，简单的调度架构如下图所示。

![20180525220738869](j:\homework\Python学习笔记\Python_notes.assets\20180525220738869.png)

如果两个Scheduler同时从队列里面取Request，每个Scheduler都有其对应的Downloader，那么在带宽足够、正常爬取且不考虑队列存取压力的情况下，爬取效率会有什么变化？没错，爬取效率会翻倍。

这样，Scheduler可以扩展多个，Downloader也可以扩展多个。而爬取队列Queue必须始终为一个，也就是所谓的共享爬取队列。这样才能保证Scheduer从队列里调度某个Request之后，其他Scheduler不会重复调度此Request，就可以做到多个Schduler同步爬取。这就是分布式爬虫的基本雏形，简单调度架构如下图所示。

![20180525220747525](j:\homework\Python学习笔记\Python_notes.assets\20180525220747525.png)

我们需要做的就是在多台主机上同时运行爬虫任务协同爬取，而协同爬取的前提就是共享爬取队列。这样各台主机就不需要各自维护爬取队列，而是从共享爬取队列存取Request。但是各台主机还是有各自的Scheduler和Downloader，所以调度和下载功能分别完成。如果不考虑队列存取性能消耗，爬取效率还是会成倍提高。

二、维护爬取队列

那么这个队列用什么来维护？首先需要考虑的就是性能问题。我们自然想到的是基于内存存储的Redis，它支持多种数据结构，例如列表（List）、集合（Set）、有序集合（Sorted Set）等，存取的操作也非常简单。

Redis支持的这几种数据结构存储各有优点。

- 列表有`lpush()`、`lpop()`、`rpush()`、`rpop()`方法，我们可以用它来实现先进先出式爬取队列，也可以实现先进后出栈式爬取队列。
- 集合的元素是无序的且不重复的，这样我们可以非常方便地实现随机排序且不重复的爬取队列。
- 有序集合带有分数表示，而Scrapy的Request也有优先级的控制，我们可以用它来实现带优先级调度的队列。

我们需要根据具体爬虫的需求来灵活选择不同的队列。

三、如何去重

Scrapy有自动去重，它的去重使用了Python中的集合。这个集合记录了Scrapy中每个Request的指纹，这个指纹实际上就是Request的散列值。我们可以看看Scrapy的源代码，如下所示：

```python
import hashlib
def request_fingerprint(request, include_headers=None):
   if include_headers:
       include_headers = tuple(to_bytes(h.lower())
                                for h in sorted(include_headers))
   cache = _fingerprint_cache.setdefault(request, {})
   if include_headers not in cache:
       fp = hashlib.sha1()
       fp.update(to_bytes(request.method))
       fp.update(to_bytes(canonicalize_url(request.url)))
       fp.update(request.body or b'')
       if include_headers:
           for hdr in include_headers:
               if hdr in request.headers:
                   fp.update(hdr)
                   for v in request.headers.getlist(hdr):
                       fp.update(v)
       cache[include_headers] = fp.hexdigest()
   return cache[include_headers]
```

`request_fingerprint()`就是计算Request指纹的方法，其方法内部使用的是hashlib的`sha1()`方法。计算的字段包括Request的Method、URL、Body、Headers这几部分内容，这里只要有一点不同，那么计算的结果就不同。计算得到的结果是加密后的字符串，也就是指纹。每个Request都有独有的指纹，指纹就是一个字符串，判定字符串是否重复比判定Request对象是否重复容易得多，所以指纹可以作为判定Request是否重复的依据。

**那么我们如何判定重复呢？Scrapy是这样实现的，如下所示：**

```python
def __init__(self):
   self.fingerprints = set()

def request_seen(self, request):
   fp = self.request_fingerprint(request)
   if fp in self.fingerprints:
       return True
   self.fingerprints.add(fp)
```

在去重的类`RFPDupeFilter`中，有一个`request_seen()`方法，这个方法有一个参数`request`，它的作用就是检测该Request对象是否重复。这个方法调用`request_fingerprint()`获取该Request的指纹，检测这个指纹是否存在于`fingerprints`变量中，而`fingerprints`是一个集合，集合的元素都是不重复的。如果指纹存在，那么就返回`True`，说明该Request是重复的，否则这个指纹加入到集合中。如果下次还有相同的Request传递过来，指纹也是相同的，那么这时指纹就已经存在于集合中，Request对象就会直接判定为重复。这样去重的目的就实现了。

Scrapy的去重过程就是，利用集合元素的不重复特性来实现Request的去重。

对于分布式爬虫来说，我们肯定不能再用每个爬虫各自的集合来去重了。因为这样还是每个主机单独维护自己的集合，不能做到共享。多台主机如果生成了相同的Request，只能各自去重，各个主机之间就无法做到去重了。

那么要实现去重，这个指纹集合也需要是共享的，Redis正好有集合的存储数据结构，我们可以利用Redis的集合作为指纹集合，那么这样去重集合也是利用Redis共享的。每台主机新生成Request之后，把该Request的指纹与集合比对，如果指纹已经存在，说明该Request是重复的，否则将Request的指纹加入到这个集合中即可。利用同样的原理不同的存储结构我们也实现了分布式Reqeust的去重。

四、防止终端

在Scrapy中，爬虫运行时的Request队列放在内存中。爬虫运行中断后，这个队列的空间就被释放，此队列就被销毁了。所以一旦爬虫运行中断，爬虫再次运行就相当于全新的爬取过程。

要做到中断后继续爬取，我们可以将队列中的Request保存起来，下次爬取直接读取保存数据即可获取上次爬取的队列。我们在Scrapy中指定一个爬取队列的存储路径即可，这个路径使用`JOB_DIR`变量来标识，我们可以用如下命令来实现：

```python
scrapy crawl spider -s JOB_DIR=crawls/spider
```

更加详细的使用方法可以参见官方文档：

> https://doc.scrapy.org/en/latest/topics/jobs.html

在Scrapy中，我们实际是把爬取队列保存到本地，第二次爬取直接读取并恢复队列即可。那么在分布式架构中我们还用担心这个问题吗？不需要。因为爬取队列本身就是用数据库保存的，如果爬虫中断了，数据库中的Request依然是存在的，下次启动就会接着上次中断的地方继续爬取。

所以，当Redis的队列为空时，爬虫会重新爬取；当Redis的队列不为空时，爬虫便会接着上次中断之处继续爬取。

五、架构实现

我们接下来就需要在程序中实现这个架构了。首先实现一个共享的爬取队列，还要实现去重的功能。另外，重写一个Scheduer的实现，使之可以从共享的爬取队列存取Request。

幸运的是，已经有人实现了这些逻辑和架构，并发布成叫Scrapy-Redis的Python包。接下来，我们看看Scrapy-Redis的源码实现，以及它的详细工作原理。

**如何实现分布式？**

- 安装一个scrapy-redis的组件

  > pip install scrapy-redis

- 原生的scrapy是不可以实现分布式爬虫，必须要让scrapy结合scrapy-redis组件一起实现分布式爬虫
- 为什么原生的scrapy不可以实现分布式？
  1. 调度器不可以被分布式集群共享
  2. 管道不可以被分布式集群共享
- scrapy-redis组件作用：
  
  - 可以给原生的scrapy框架提供可以被共享的管道和调度器

**实现流程：**

- 创建一个流程

- 创建一个基于CrawlSpider的爬虫文件

  > scrapy genspider -t crawl xxx www.xxx.com

- 修改当前的爬虫文件

  - 导包：from scrapy_redis.spiders import RedisCrawlSpider
  - 将 `start_urls` 和 `allowed_domains` 进行注释
  - 添加一个新属性：redis_key = "sun"可以被共享的调度器队列的名称
  - 编写解析数据相关的代码
  - 将当前爬虫类的父类修改成RedisCrawlSpider

- 修改配置文件（settings）

  - 指定可以被共享的管道

  ```python
  ITEM_PIPELINES = {'scrapy_redis.pipelines.RedisPipeline': 400}
  ```

  - 指定可以被共享的调度器

  ```python
  # 增加了一个去重容器类的配置, 作用使用Redis的set集合来存储请求的指纹数据, 从而实现请求去重的持久化
  DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
  # 使用scrapy-redis组件自己的调度器
  SCHEDULER = "scrapy_redis.scheduler.Scheduler"
  # 配置调度器是否要持久化, 也就是当爬虫结束了, 要不要清空Redis中请求队列和去重指纹的set。如果是True, 就表示要持久化存储, 就不清空数据, 否则清空数据
  SCHEDULER_PERSIST = True
  ```

  - 指定redis服务器

  ```python
  # 指定redis
  REDIS_HOST = '127.0.0.1'  # redis远程服务器的ip
  REDIS_PORT = 6379
  REDIS_ENCODING = 'utf-8'
  REDIS_PARAMS = {'password':'xxxxxx'}
  ```

- redis相关操作配置

  - 配置redis的配置文件

    - linux或者mac修改：redis.conf
    - windows修改：windows.conf
    - 配置文件修改：

    ```python
    # 将bind 127.0.0.1 进行删除
    # 关闭保护模式：protected-mode yes改为no
    ```

  - 结合着配置文件开始redis服务

    > redis-server.exe  redis.windows.conf

  - 启动客户端

    > redis-cli
    >
    > auth 123456

- 执行工程

  > cd fbsPro/spiders
  >
  > scrapy runspider xxx.py

- 向调度去队列中房一个其实的url

  - 调度器的队列再redis的客户端中

    > lpush xxx www.xxx.com

- 爬取到的数据存储在了redis的proName:itms这个数据结构中

  > 查看数据结构：keys *
  >
  > 查看数据详情：lrange Name 0 - 1
  >
  > 查看数据统计：llen Name
  >
  > 清空数据：flushall

示例：

```python
# spider
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fbsPro.items import FbsproItem, FbsdetailItem


class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.sss.com']
    # start_urls = ['https://wzzdg.sun0769.com/political/index/supervise?page=']

    redis_key = 'sun'
    link = LinkExtractor(allow=r'page=\d+')
    detail_link = LinkExtractor(allow=r'/political/politics/index\?id=\d+')
    rules = (
        Rule(link, callback='parse_item', follow=True),
        Rule(detail_link, callback='fbs_parse_item'),
    )

    def parse_item(self, response):
        li_list = response.xpath('//div[@class="width-12"]/ul/li')
        for li in li_list:
            news_num = li.xpath("./span[1]/text()").extract_first()
            news_title = li.xpath("./span[3]/a/text()").extract_first()
            item = FbsproItem()
            item["news_num"] = news_num
            item["news_title"] = news_title
            yield item

    def fbs_parse_item(self, response):
        detail_num = response.xpath(
            '/html//div[3]/div[2]/div[2]/div[1]/span[4]/text() | /html//div[3]/div[2]/div[2]/div[1]/span[3]/text()'
        ).extract_first()
        detail_content = response.xpath(
            '/html//div[3]/div[2]/div[2]/div[2]/pre/text()').extract()
        detail_content = "".join(detail_content)
        detail_item = FbsdetailItem()
        detail_item["detail_num"] = detail_num.split("：")[1]
        detail_item["detail_content"] = detail_content
        yield detail_item
```

```python
# settings
# 指定可以被共享的管道
ITEM_PIPELINES = {'scrapy_redis.pipelines.RedisPipeline': 400}
"""指定可以被共享的调度器"""
# 增加了一个去重容器类的配置, 作用使用Redis的set集合来存储请求的指纹数据, 从而实现请求去重的持久化
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis组件自己的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 配置调度器是否要持久化, 也就是当爬虫结束了, 要不要清空Redis中请求队列和去重指纹的set。如果是True, 就表示要持久化存储, 就不清空数据, 否则清空数据
SCHEDULER_PERSIST = True

# 指定redis
REDIS_HOST = '127.0.0.1'  # redis远程服务器的ip
REDIS_PORT = 6379
REDIS_ENCODING = 'utf-8'
```

#### 14.8.9 增量式爬虫

检测网站数据更新的情况，只会爬取网站最新更新出来的数据。

分析：

- 指定一个起始的url
- 基于CrawlSpider获取其他页面的链接
- 基于Rule将其他的页面链接进行请求
- 从每一个页码对应的页面源码中解析出每一个详情页的url
- 对详情页的url发起请求，然后解析出标题和内容
- 进行持久化存储

核心：检测详情页的url之前没有请求过

- 将爬取过的详情页的url存储
- 存储到redis的set数据结构

```python
# spider
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from redis import Redis
from zls.items import ZlsItem


class MovieSpider(CrawlSpider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://dianying.2345.com/list/------.html']

    rules = (Rule(LinkExtractor(allow=r'/list/-------\d+\.html'),
                  callback='parse_item',
                  follow=True), )

    # 创建redis链接对象
    conn = Redis("127.0.0.1", port=6379)

    # 解析详情页的url
    def parse_item(self, response):
        li_list = response.xpath('//div[@id="contentList"]/ul/li')
        for li in li_list:
            detail_url = "https:" + li.xpath(
                './div[1]/a/@href').extract_first()
            # 将详情页的url存入到redis的set中
            ex = self.conn.sadd("urls", detail_url)
            if ex == 1:
                print('该url没有被爬取过，可以进行数据的爬取')
                yield scrapy.Request(url=detail_url,
                                     callback=self.parst_detail)
            else:
                print('数据还没有更新，暂无新数据可爬取！')

    # 解析详情页中的电影名称和类型，进行持久化存储
    def parst_detail(self, response):
        item = ZlsItem()
        title = response.xpath('//div[@class="tit"]/h1/text()').extract_first()
        content = response.xpath(
            '//li[@class="extend"]/p[1]/span/text()').extract_first()
        item["title"] = title
        item["content"] = content

        yield item
```

```python
# items
import scrapy


class ZlsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    content = scrapy.Field()
```

```python
# pipelines
class ZlsPipeline(object):
    conn = None

    def open_spider(self, spider):
        self.conn = spider.conn

    def process_item(self, item, spider):
        dic = {'title': item['title'], 'content': item['content']}
        # print(dic)
        self.conn.lpush('movie_data', dic)
        return item
```

## 第十五章 drf框架

### 15.1 Web应用模式

在开发Web应用中，有两种应用模式：

1. **前后端不分离**：客户端看到的内容和所有界面效果都是由服务端提供出来的，这种情况下，前端页面中会出现很多涉及到服务器端的模板语法。

![depended_frontend_backend](j:\homework\Python学习笔记\Python_notes.assets\depended_frontend_backend.png)

2. **前后端分离**：把前端的界面效果（html，css，js分离到另一个项目中，python服务端只需要返回数据即可。）前端形成一个独立的网站，服务端构成一个独立的网站。

![indepent_frontend_backend](j:\homework\Python学习笔记\Python_notes.assets\indepent_frontend_backend.png)

django，一般都是做Web网站，如果可以利用django实现前后端分离，则django就可以完成地铁站的运营调度系统，路由的终端系统，pos机的服务端系统，游戏的服务端后台，软件的服务端后台。

### 15.2 API接口

为了在团队内部形成共识，防止个人习惯差异引起的混乱我们需要找到一种大家都觉得很好的接口实现规范，而且这种规范能够让后端写的接口，用途一目了然，减少双方之间的合作成本。

目前市面上大部分公司开发任意使用的接口服务架构主要有：restful、rpc。soap

- restful：翻译成中文：资源状态转换

  把后端所有的数据/文件都看成资源。接口请求数据本质上来说就是对资源的操作了。Web项目中操作资源，无非就是增删改查，所以要求在地址栏中声明操作的资源是什么，然后通过http请求东磁来说明对资源进行哪一种操作。

  - 优点：维护开发简单，可以保证后期的开发不回出现太多重复接口
  - 缺点：
    1. 有部分接口不会有明确的增删改查这种区分，所以会出现一些不伦不类的接口。会因为这些语义不明，不伦不类的接口导致后期的维护成本上升。
    2. 因为restful把对于资源的操作都理解成了增删改查，建议使用htpp，所以restful接口天生局限于web开发。

- rpc：翻译成中文：远程服务调用

  - 优点：不需要管当前操作的是什么请求，也不需要操作url地址的编写，对接简单
  - 缺点：接口多了，对应函数名和参数就多了，前端在请求api接口时，就会比较难找，容易出现重复的接口

- soap：SOAP (Simple Object Access Protocol) 顾名思义，是一个严格定义的信息交换协议，用于在Web Service中把远程调用和返回封装成机器可读的格式化数据。事实上SOAP数据使用XML数据格式，定义了一整套复杂的标签，以描述调用的远程过程、参数、返回值和出错信息等等。而且随着需要的增长，又不得增加协议以支持安全性，这使SOAP变得异常庞大，背离了简单的初衷。另一方面，各个服务器都可以基于这个协议推出自己的API，即使它们提供的服务及其相似，定义的API也不尽相同，这又导致了WSDL的诞生。WSDL (Web Service Description Language) 也遵循XML格式，用来描述哪个服务器提供什么服务，怎样找到它，以及该服务使用怎样的接口规范，简言之，服务发现。现在，使用Web Service的过程变成，获得该服务的WSDL描述，根据WSDL构造一条格式化的SOAP请求发送给服务器，然后接收一条同样SOAP格式的应答，最后根据先前的WSDL解码数据。绝大多数情况下，请求和应答使用HTTP协议传输，那么发送请求就使用HTTP的POST方法。

  - 优点：定义严格，必须符合soap的格式，某些适合使用比较方便，开发工具支持比较多
  - 缺点：需要生成SDL文件

### 15.3 RESTful API规范

![restful](j:\homework\Python学习笔记\Python_notes.assets\restful.gif)

REST全称是Representational State Transfer，中文意思是表述（编者注：通常译为表征）性状态转移。 它首次出现在2000年Roy Fielding的博士论文中。  

RESTful是一种定义Web API接口的设计风格，尤其适用于前后端分离的应用模式中。

这种风格的理念认为后端开发任务就是提供数据的，对外提供的是数据资源的访问接口，所以在定义接口时，客户端访问的URL路径就表示这种要操作的数据资源。

而对于数据资源分别使用POST、DELETE、GET、UPDATE等请求动作来表达对数据的增删查改。

| 请求方法  | 后端操作 |
| --------- | -------- |
| GET       | 查询     |
| POST      | 新增     |
| PUT/PATCH | 修改     |
| DELETE    | 删除     |

事实上，我们可以使用任何一个框架都可以实现符合restful规范的API接口。

参考文档：http://www.runoob.com/w3cnote/restful-architecture.html

接口实施过程中，会存在幂等性。所谓幂等性是指代客户端发起多次请求是否对于服务端里面的资源产生不同结果。如果多次请求，服务端结果还是一样，则属于幂等接口，如果多次请求，服务端产生结果是不一样的，则属于非幂等接口。在http请求，get/put/patch/delete都属于幂等性接口，post属于非幂等接口。

为什么要考虑幂等性？主要就是接口操作的安全性问题。

#### 15.3.1 域名

应该尽量将API部署在专用域名之下。

```http
https://api.example.com
```

如果确定API很简单，不会有进一步扩展，可以考虑放在主域名下。

```http
https://www.example.org/api/
```

#### 15.3.2 版本（Version）

项目开发过程中都会对项目进行版本迭代，所以每一个版本的api接口肯定都有可能存在差异，因此应该将API的版本号放入URL。

另一种做法是，将版本号放在HTTP头信息中，但不如放入URL方便和直观。[Github](https://developer.github.com/v3/media/#request-specific-version)就采用了这种做法。

因为不同的版本，可以理解成同一种资源的不同表现形式，所以应该采用同一个URL。版本号可以在HTTP请求头信息的Accept字段中进行区分（参见[Versioning REST Services](http://www.informit.com/articles/article.aspx?p=1566460)）：

```http
Accept: vnd.example-com.foo+json; version=1.0

Accept: vnd.example-com.foo+json; version=1.1

Accept: vnd.example-com.foo+json; version=2.0
```

#### 15.3.3 路径

路径又称"终点"（endpoint），表示API的具体网址，每个网址代表一种资源（resource）

**(1) 资源作为网址，只能有名词，不能有动词，而且所用的名词往往与数据库的表名对应。**

举例来说，以下是不好的例子:

```http
/getProducts
/listOrders
/retreiveClientByOrder?orderId=1
```

对于一个简洁结构，你应该始终用名词。 此外，利用的HTTP方法可以分离网址中的资源名称的操作。

```http
GET   /products ：               将返回所有产品清单
POST  /products ：               将产品新建到集合
GET   /products/4 ：             将获取产品 4
PATCH（或）PUT      /products/4 ：将更新产品 4
```

**(2) API中的名词应该使用复数。无论子资源或者所有资源。**

举例来说，获取产品的API可以这样定义

```http
获取单个产品：http://127.0.0.1:8080/AppName/rest/products/1
获取所有产品: http://127.0.0.1:8080/AppName/rest/products
```

#### 15.3.4 HTTP动词

对于资源的具体操作类型，由HTTP动词表示。

常用的HTTP动词有下面四个（括号里是对应的SQL命令）。

- GET（SELECT）：从服务器取出资源（一项或多项）。
- POST（CREATE）：在服务器新建一个资源。
- PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
- DELETE（DELETE）：从服务器删除资源。

```http
CURD   Create、Update、Read、Delete 增删查改，这四个数据库的常用操作
```

还有三个不常用的HTTP动词。

- PATCH（UPDATE）：在服务器更新(更新)资源（客户端提供改变的属性）。
- HEAD：获取资源的元数据。
- OPTIONS：获取信息，关于资源的哪些属性是客户端可以改变的。

下面是一些例子。

```http
GET /zoos：列出所有动物园
POST /zoos：新建一个动物园（上传文件）
GET /zoos/ID：获取某个指定动物园的信息
PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）
PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）
DELETE /zoos/ID：删除某个动物园
GET /zoos/ID/animals：列出某个指定动物园的所有动物
DELETE /zoos/ID/animals/ID：删除某个指定动物园的指定动物
```

#### 15.3.5 过滤信息（Filtering）

如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。

下面是一些常见的参数。query_string 查询字符串,地址栏后面问号后面的数据,格式: name=xx&sss=xxx

```http
完整的URL地址格式：
协议://域名(IP):端口号/路径?查询字符串#锚点
```

```http
?limit=10：指定返回记录的数量
?offset=10：指定返回记录的开始位置。
?page=2&per_page=100：指定第几页，以及每页的记录数。
?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
?animal_type_id=1：指定筛选条件
```

参数的设计允许存在冗余，即允许API路径和URL参数偶尔有重复。比如，GET /zoos/ID/animals 与 GET /animals?zoo_id=ID 的含义是相同的。

#### 15.3.6 状态码（Status Code）

http所有请求，必有所回应的协议。

```http
1xx 表示当前本次请求还是持续，没结束
2xx 表示当前本次请求成功
3xx 表示当前本次请求成功，但是服务器进行代理操作/重定向
4xx 表示当前本次请求失败，主要是客户端发生了错误
5xx 表示当前本次请求失败，主要是服务器发生了错误
```

服务器向用户返回的状态码和提示信息，常见的有以下一些（方括号中是该状态码对应的HTTP动词）。

> - 200 OK - [GET]：服务器成功返回用户请求的数据
> - 201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
> - 202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
> - 204 NO CONTENT - [DELETE]：用户删除数据成功。
> - 400 INVALID REQUEST - [GET/POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作
> - 401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
> - 403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
> - 404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
> - 406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
> - 410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
> - 422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
> - 500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。
> - 507 数据存储出错，往往数据库操作错误出错，服务器就返回这

状态码的完全列表参见[这里](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)或[这里](https://zh.wikipedia.org/wiki/HTTP%E7%8A%B6%E6%80%81%E7%A0%81)。

#### 15.3.7 错误处理（Error handling）

如果状态码是4xx，服务器就应该向用户返回出错信息。一般来说，返回的信息中将error作为键名，出错信息作为键值即可。

```json
{
    error: "Invalid API key"
}
```

#### 15.3.8 返回结果

针对不同操作，服务器向用户返回的结果应该符合以下规范。

- GET /collection：返回资源对象的列表（数组）
- GET /collection/ID：返回单个资源对象(json)
- POST /collection：返回新生成的资源对象(json)
- PUT /collection/ID：返回完整的资源对象(json)
- DELETE /collection/ID：返回一个空文档(空字符串)

#### 15.3.9 超媒体（Hypermedia API）

RESTful API最好做到Hypermedia（即返回结果中提供链接，连向其他API方法），使得用户不查文档，也知道下一步应该做什么。

比如，Github的API就是这种设计，访问[api.github.com](https://api.github.com/)会得到一个所有可用API的网址列表。

```json
{
"current_user_url": "https://api.github.com/user",
"authorizations_url": "https://api.github.com/authorizations",
// ...
}
```

从上面可以看到，如果想获取当前用户的信息，应该去访问[api.github.com/user](https://api.github.com/user)，然后就得到了下面结果。

```json
{
  "message": "Requires authentication",
  "documentation_url": "https://developer.github.com/v3"
}
```

上面代码表示，服务器给出了提示信息，以及文档的网址。

#### 15.3.10 其他

服务器返回的数据格式，应该尽量使用JSON，避免使用XML。

XML是W3C为了替换HTML研发出来的，但是现在很明显失败了。

xml VS json

```xml
<xml version="1.0" charset="utf-8">
	<name>张三</name>
  <sex>男</sex>
  <age>18</age>
</xml>
```

```json
{
  “name”:"张三",
  "sex":"男",
  "age":18
}
```

菲尔丁博士提供的这些规范，就是他的个人总结，但是只是约定俗成，并非硬性规定，所以我们以后在公司里面，即便使用的就是restful但是也不会说每一条都遵守的。

### 15.4 序列化

API接口开发，最核心最常见的一个过程就是序列化，所谓序列化就是把数据转换格式，序列化可分为两个阶段：

**序列化**：把我们识别的数据转换成指定的格式提供给别人。

> 例如：我们在django中获取到的数据默认是模型对象，但是模型对象数据无法直接提供给前端或别的平台使用，所以我们需要把数据进行序列化，变成字符串或者json数据，提供给前端或者其他平台。

**反序列化**：把别人提供的数据转换/还原成我们需要的格式。

> 例如：前端js提供过来的json数据，对于python而言就是字符串，我们需要进行反序列化换成模型类对象，这样我们才能把数据保存到数据库中。

### 15.5 Django Rest_Framework

核心思想：缩减编写API接口的代码

Django REST framework是一个建立在Django基础之上的Web 应用开发框架,本质上就是一个内置在django里面的子应用，可以快速的开发REST API接口应用。

在REST framework中，提供了序列化器对象Serialzier的定义，可以帮助我们简化序列化与反序列化的过程，不仅如此，还提供丰富的类视图、扩展类、视图集来简化视图的编写工作。REST framework还提供了认证、权限、限流、过滤、分页、接口文档等功能支持。REST framework提供了一个用于测试API接口 的可视化Web界面【可以浏览器直接访问接口，drf的api接口测试页面非常美观】。

![drf_logo](j:\homework\Python学习笔记\Python_notes.assets\drf_logo.png)

中文文档：

> https://q1mi.github.io/Django-REST-framework-documentation/#django-rest-framework

github：

>  https://github.com/encode/django-rest-framework/tree/master

**特点**：

- 提供了定义序列化器Serializer的方法，可以快速根据 Django ORM 或者其它库自动序列化/反序列化；
- 提供了丰富的类视图、Mixin扩展类，简化视图的编写；

- 丰富的定制层级：函数视图、类视图、视图集合到自动生成 API，满足各种需要；
- 多种身份认证和权限认证方式的支持；[jwt   Json web token]
- 内置了限流系统；
- 直观的 API web 界面；【方便我们调试开发api接口】
- 可扩展性，插件丰富

### 15.6 环境安装

#### 15.6.1 虚拟环境（Virtualenv）

Virtualenv 是一个版本管理的虚拟环境

Virtualenvwrapper 是 Virtualenv 的增强版（因为Virtualenv 的操作太麻烦，所以不直接使用它）

**Virtualenv介绍：**

> 举例：
> 在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.7。所有第三方的包都会被pip安装到Python3的site-packages目录下。如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python3。如果应用A需要python2.7，而应用B需要python3.6怎么办？

这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

**1. 安装pip：**

由于安装virtualenv需要使用到Python包管理工具pip，因此需要提前安装好pip。

> \# 查看是否安装   pip3 list
>
> \# 安装命令      sudo apt-get install python3-pip
>
> \# 查看pip3版本号:   pip3 --version

**2. 安装virtualenv：**

> sudo pip3 install virtualenv

**3. 安装virtualenvwrapper：**

安装virtualenvwrapper的主要原因是为了后期使用方便，由于每次开启虚拟环境需要找到虚拟环境所在目录的bin下的使用source运行activate。

这就需要记住每个虚拟环境所在的目录，而且切换环境不够方便，因此我们需要安装virtualenvwrapper，这样能够省去每次开启虚拟环境切换目录的操作，从而更加方便快捷。

> sudo pip3 install virtualenvwrapper

**4. 配置virtualenvwrapper**

virtualenvwrapper安装完成后，需要配置一下才可以正常使用。

需要配置的文件是：/home/.bashrc

- 先创建一个目录放置虚拟环境

  > mkdir ~/.virtualenvs

- 配置环境变量

  > vim ~/.bashrc

  1. 打开文件后在文件最下方增加如下代码

  ```python
  export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
  export WORKON_HOME=$HOME/.virtualenvs
  source /usr/local/bin/virtualenvwrapper.sh
  ```

  2. 配置完成之后需要执行如下命令，才可以让编辑后的配置文件生效 

  > source ~/.bashrc 

  3. 查看virtualenvwrapper的安装路径

  > sudo find / -name virtualenvwrapper.sh

**5. 创建虚拟环境**

```python
# mkvirtualenv -p python3 创建的虚拟环境名称
mkvirtualenv -p python3 drfdemo
```

**6. 查看已创建的虚拟环境**

```python
lsvirtualenv
```

**7. 进入/切换虚拟环境**

```python
# workon 要进入/切换到的虚拟环境名称
workon drfdemo
```

**8.快捷进入虚拟环境目录**

```python
cdvirtualenv
```

**9.快捷进入虚拟环境包安装目录**

```python
cdsitepackages
```

**10. 退出当前虚拟环境**

```python
deactivate
```

**11. 删除虚拟环境**

```python
# rmvirtualenv 需要删除的虚拟环境名称
rmvirtualenv dailyfresh
```

需要注意的是不可删除当前所处的虚拟环境，如需删除需要退出或切换到其他虚拟环境

**12. 查看虚拟环境中已经安装的包**

```python
pip3 list
pip3 freeze
```

#### 15.6.2 安装DRF

drf需要以下依赖：

- Python (2.7, 3.2以上)
- Django (1.10, 1.11, 2.0以上)

drf是以Django扩展应用的方式提供的，所以我们可以直接利用已有的Django环境而无需从新创建。（若没有Django环境，需要先创建环境安装Django）

前提是已经安装了django，建议安装在虚拟环境

```python
# 创建虚拟环境
mkvirtualenv drfdemo -p python3
# 安装django
pip install django==2.2.0  -i https://pypi.douban.com/simple
# 安装drf
pip install djangorestframework -i https://pypi.douban.com/simple
# 因为我们接下来需要开发api接口肯定要操作数据，所以安装pymysql
pip install pymysql -i https://pypi.douban.com/simple
```

**1.创建django项目**

```python
cd ~/virtualenvs/
django-admin startproject drfdemo
```

**2.添加rest_framework应用**

在settings.py的INSTALLED_APPS中添加`rest_framework`

```python
NSTALLED_APPS = [
    'rest_framework',
]
```

接下来就可以使用drf提供的功能进行api接口开发了。在项目中如果使用rest_framework框架实现api接口，主要有以下三个步骤：

- 将请求的数据（如json格式）转换位模型类对象
- 通过模型对象进行数据库操作，完成客户端请求的增删查改
- 将模型类对象转换位响应的数据（如json）

#### 15.6.3 体验drf完全简写代码的过程

1.创建子应用

```python
# 项目根目录下创建子应用，用于展示当前例子。
python manage.py startapp app01
```

2.创建模型

```python
# models.py文件创建模型
from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(null=False, max_length=32, verbose_name="姓名")
    sex = models.BooleanField(default=True, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    class_num = models.CharField(max_length=5, verbose_name="班级")
    description = models.TextField(max_length=100, verbose_name="个性签名")
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")

    class Meta:
        # 设置表明
        db_table = 'tb_students'
        managed = True
        verbose_name = '学生表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
```

3.创建数据库

```python
create database student charset=utf8;
use student;
```

4.初始化数据库链接

```python
# 安装pymsql
pip3 install pymsql
```

5.主引用中`__init__.py`设置使用pymysql作为数据库驱动

```python
import pymysql

pymysql.install_as_MySQLdb()
```

6.配置mysql账号密码

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "student",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "",
    },
}
```

7.执行数据迁移

```python
python manage.py makemigrations
python manage.py migrate
```

8.创建序列化器

```python
"""
在app01目录下新建serializers.py文件，用于保存该应用的序列化器
创建一个StudentModelSerializer用于序列化与反序列化
"""
from django.db.models import fields
from rest_framework import serializers
from .models import Student

# 创建一个序列化器，在视图中被调用
class StudentModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

```

- **model：**指明该序列化器处理的数据字段从哪个模型类获取
- **fields：**指明该序列化器包含模型类中的哪些字段，all代表所有，取其中几个写在列表中

9.编写视图

```python
# 在app01应用的views.py中创建视图StudentViewSet，这是一个视图集
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentModelSerializers

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers
```

- **queryset：** 指明该视图集在查询数据时使用的查询集
- **serializer_class：** 指明该视图在进行序列化或反序列化时使用的序列化器

10.定义路由

```python
# 在student应用的urls.py中定义路由信息
from rest_framework import urlpatterns
from . import views
from rest_framework.routers import DefaultRouter

# 路由列表
urlpatterns = []
# 实例化一个路由器
router = DefaultRouter()
# 将视图集注册到路由中
router.register('student', views.StudentViewSet)
# 将路由器中的所有路由加到主项目的路由列表中
urlpatterns += router.urls
```

把app01子应用中的路由文件加载到总路由文件中

```python
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/', include("app01.urls"))
]
```

11.运行测试

```python
python manage.py run server
```

1）在浏览器中输入`http://127.0.0.1:8000/app01/`，可以看到drf提供的api web浏览页面

![image-20210817223350583](j:\homework\Python学习笔记\Python_notes.assets\image-20210817223350583.png)

2）输入 `http://127.0.0.1:8000/app01/student/`，获取所有数据接口

![image-20210817223521767](j:\homework\Python学习笔记\Python_notes.assets\image-20210817223521767.png)

3）在页面底部可以访问添加学生的接口，

![image-20210817223610516](j:\homework\Python学习笔记\Python_notes.assets\image-20210817223610516.png)

4）添加学生后输入`http://127.0.0.1:8000/app01/student/3/`，可以访问获取单个学生信息的接口

![image-20210817223729027](j:\homework\Python学习笔记\Python_notes.assets\image-20210817223729027.png)



5）获取单个学生信息后，可以修改访问修改学生的接口

![image-20210817223916174](j:\homework\Python学习笔记\Python_notes.assets\image-20210817223916174.png)

6）点delete按钮，可以访问删除学生的接口

![image-20210817223949348](j:\homework\Python学习笔记\Python_notes.assets\image-20210817223949348.png)

### 15.7 序列化器-Serializer

Serializer作用：

> 1.序列化：序列化器会把模型对象转换成字典，经过response转换成json字符串返回。
>
> 2.反序列化：把客户端发送过来的数据，经过request以后变成字典，序列化器可以把字段转换成模型。
>
> 3.反序列化：完成数据校验功能

#### 15.7.1 定义序列化器

Django REST framework中的Serializer使用类来定义，须继承自rest_framework.serializers.Serializer。

接下来，为了方便演示序列化器的使用，我们先创建一个新的子应用sers

```python
python manage.py startapp sers
```

我们已经有了一个数据库模型类Student，我们为这个模型类提供一个序列化器

```python
from rest_framework import serializers
""" 
声明序列化器，所有的序列化器要直接或者间接继承于Serializer
其中，ModelSerializer是Serializer的子类，
ModelSerializer在Serializer的基础上进行了代码简化 
"""


class StudentSerializer(serializers.Serializer):
    """ 学生信息序列化器 """
    # 1.需要进行数据转换的字段
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    sex = serializers.BooleanField()
    description = serializers.CharField()
```

**注意：serializer不是只能为数据库模型类定义，也可以为非数据库模型类的数据定义。** serializer是独立于数据库之外的存在。

常用的字段类型：

| 字段                    | 字段构造方式                                                 |
| ----------------------- | ------------------------------------------------------------ |
| **BooleanField**        | BooleanField()                                               |
| **NullBooleanField**    | NullBooleanField()                                           |
| **CharField**           | CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True) |
| **EmailField**          | EmailField(max_length=None, min_length=None, allow_blank=False) |
| **RegexField**          | RegexField(regex, max_length=None, min_length=None, allow_blank=False) |
| **SlugField**           | SlugField(max*length=50, min_length=None, allow_blank=False) 正则字段，验证正则模式 [a-zA-Z0-9*-]+ |
| **URLField**            | URLField(max_length=200, min_length=None, allow_blank=False) |
| **UUIDField**           | UUIDField(format='hex_verbose')  format:  1) `'hex_verbose'` 如`"5ce0e9a5-5ffa-654b-cee0-1238041fb31a"`  2） `'hex'` 如 `"5ce0e9a55ffa654bcee01238041fb31a"`  3）`'int'` - 如: `"123456789012312313134124512351145145114"`  4）`'urn'` 如: `"urn:uuid:5ce0e9a5-5ffa-654b-cee0-1238041fb31a"` |
| **IPAddressField**      | IPAddressField(protocol='both', unpack_ipv4=False, **options) |
| **IntegerField**        | IntegerField(max_value=None, min_value=None)                 |
| **FloatField**          | FloatField(max_value=None, min_value=None)                   |
| **DecimalField**        | DecimalField(max_digits, decimal_places, coerce_to_string=None, max_value=None, min_value=None) max_digits: 最多位数 decimal_palces: 小数点位置 |
| **DateTimeField**       | DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None) |
| **DateField**           | DateField(format=api_settings.DATE_FORMAT, input_formats=None) |
| **TimeField**           | TimeField(format=api_settings.TIME_FORMAT, input_formats=None) |
| **DurationField**       | DurationField()                                              |
| **ChoiceField**         | ChoiceField(choices) choices与Django的用法相同               |
| **MultipleChoiceField** | MultipleChoiceField(choices)                                 |
| **FileField**           | FileField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
| **ImageField**          | ImageField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
| **ListField**           | ListField(child=, min_length=None, max_length=None)          |
| **DictField**           | DictField(child=)                                            |

选项参数：

| 参数名称            | 作用             |
| ------------------- | ---------------- |
| **max_length**      | 最大长度         |
| **min_lenght**      | 最小长度         |
| **allow_blank**     | 是否允许为空     |
| **trim_whitespace** | 是否截断空白字符 |
| **max_value**       | 最小值           |
| **min_value**       | 最大值           |

通用参数：

| 参数名称           | 说明                                          |
| ------------------ | --------------------------------------------- |
| **read_only**      | 表明该字段仅用于序列化输出，默认False         |
| **write_only**     | 表明该字段仅用于反序列化输入，默认False       |
| **required**       | 表明该字段在反序列化时必须输入，默认True      |
| **default**        | 反序列化时使用的默认值                        |
| **allow_null**     | 表明该字段是否允许传入None，默认False         |
| **validators**     | 该字段使用的验证器                            |
| **error_messages** | 包含错误编号与错误信息的字典                  |
| **label**          | 用于HTML展示API页面时，显示的字段名称         |
| **help_text**      | 用于HTML展示API页面时，显示的字段帮助提示信息 |

#### 15.7.2 创建Serializer对象

定义好Serializer类后，就可以创建Serializer对象了。

Serializer的构造方法：

```python
Serializer(instance=None, data=empty, **kwarg)
```

说明：

1. 用于序列化时，将模型对象或模型列表传入 `instance` 参数，当 `instance` 参数为模型列表时， `many` 必须为True
2. 用于反序列化时，将要被反序列化的数据传入 `data` 参数
3. 除了 `instance` 和 `data` 参数外，在构造Serializer对象时，还可以通过 `context` 参数额外添加数据，如：

```python
serializer = AccountSerializer(account, context={"request": request})
```

**通过context参数附加的数据，可以通过Serializer对象的context属性获取。**

1. 使用序列化器的时候一定要注意，序列化器声明了以后，不会自动执行，需要我们在视图中进行调用才可以。
2. 序列化器无法直接接收数据，需要我们在视图中实例化序列化器对象时把使用的数据传递过来。
3. 序列化器的字段声明类似于模型。
4. 开发restful api时，序列化器会帮我们把模型数据转换成字典。
5. drf提供的视图会帮我们把字典转换成json，或者把客户端发过来的数据转换成字典。

#### 15.7.3 序列化器的使用

序列化器的使用分两个阶段：

1. 在客户端请求时，使用序列化器可以完成对数据的反序列化。
2. 在服务端响应时，使用序列化器可以完成对数据的序列化。

##### 15.7.3.1 序列化

基本使用：

1. 查询出一个学生对象

```python
from app01.models import Student
student = Student.objects.get(id=3)
```

2. 构造序列化器对象

```python
from .serializers import StudentSerializer
serializer = StudentSerializer(instance=student)
```

3. 获取序列化数据

```python
# 通过data属性可以获取序列化后的数据
serializer.data
```

视图代码：获取单个数据

```python
from django.views import View
from app01.models import Student
from .serializers import StudentSerializer
from django.http.response import JsonResponse

from sers import serializers

# Create your views here.


class StudentView(View):
    """ 使用序列化器序列化转换单个模型数据 """
    def get(self, request):
        # 获取数据
        student = Student.objects.get(pk=3)
        # 数据转换
        serializer = StudentSerializer(instance=student)
        print(serializer)
        # 响应数据
        return JsonResponse(serializer.data)
    	# {"id": 3, "name": "\u738b\u4e8c\u7259", "age": 15, "sex": false, "description": "\u6211\u662f\u738b\u4e8c\u7259"}
```

视图代码：如果被序列化的是包含多条数据的查询及QuserySet，可以通过添加 `many=True` 参数补充说明

```python
class Student2View(View):
    def get(self, request):
        student_obj = Student.objects.all()
        serializer = StudentSerializer(instance=student_obj, many=True)
        print(serializer)

        return JsonResponse(serializer.data, safe=False)
    # [{"id": 1, "name": "\u5f20\u4e00", "age": 18, "sex": true, "description": "\u6211\u662f\u5f20\u4e00"}, {"id": 3, "name": "\u738b\u4e8c\u7259", "age": 15, "sex": false, "description": "\u6211\u662f\u738b\u4e8c\u7259"}]
```

##### 15.7.3.2 反序列化

数据验证：

使用序列化器进行反序列化时，需要对数据进行验证后，才能获取验证成功的数据或保存成模型对象。

在获取反序列化的数据前，必须调用 `is_valid()` 方法进行验证，验证成功返回True，否则返回False。

验证失败，可以通过序列化器对象的 `errors` 属性获取错误信息，返回字典，包含了字段和字段的错误。如果是非字段错误，可以通过修改 `REST framework` 配置中的 `NON_FIELD_ERRORS_KEY` 来控制错误字典中的键名。

验证成功，可以通过序列化器对象的 `validated_data` 属性获取数据。

在定义序列化时，指明每个字段的序列化类型和选项参数，本身就是一种验证行为。

示例：BookSerializer

钩子验证：

- validate_字段名称：针对单个字段进行验证

- validate：针对多个字段进行验证
- validators：单独定义一个函数验证字段，在序列化器对应的字段种添加该字段方法的验证

保存数据：

- 数据验证成功后，序列化器完成了将数据反序列化的的过程，通过create()和update()两个方法来实现
- 如果将修改的数据保存到数据库，则需调用save()方法

```python
# serializers.py
from rest_framework import serializers
from .models import Book


def check_comment(data):
    if data == 1003:
        raise serializers.ValidationError("评论量已被占用！")
    return data


class BookSerializer(serializers.Serializer):
    name = serializers.CharField(label="书名", max_length=20)
    pub_date = serializers.DateField(label="发布日期", required=False)
    bread = serializers.IntegerField(label="阅读量", required=False)
    comment = serializers.IntegerField(label="评论量", required=False, validators=[check_comment])
    """ 验证字段方法 
    1. validate()        # 验证所有字段
    2. validate_字段名()  # 验证单个字段
    """
    def validate(self, attrs):
        if attrs.get("bread") == 10 and attrs.get("comment") == 11:
            raise serializers.ValidationError("重新输入阅读量")
        # 注意,每次验证完成以后必须有结果返回!否则数据就会丢失
        return attrs

    def validate_name(self, attrs):
        if attrs == "joker":
            raise serializers.ValidationError("{}已经被占用".format(attrs))
        return attrs

    def create(self, validated_data):
        """ 添加数据 """
        ret = Book.objects.create(**validated_data)
        print(ret)
        return ret

    def update(self, instance, validated_data):
        """ 修改数据 """
        print("instance打印", instance)
        print("validated_data打印", validated_data)
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance

```

1.通过构造序列化器对象，将要反序列化的数据传递给data参数，进行验证：

- is_valid()：判断验证是否通过，返回值为True or False，加入参数 `is_valid(raise_exception=True)`，验证失败后不会继续执行，直接抛出异常

2.将数据保存到数据库中，执行数据库操作：

- `serializer.save()` ：调用序列化器内的 create or update方法

如果实例化序列化器的时候，没有传入 `instance`参数，调用 save()方法时，creat()被调用，相反则调用update()。

```python
# views.py
from django.views import View
from django.http.response import HttpResponse, JsonResponse
from .serializers import BookSerializer
from .models import Book
import json
# Create your views here.


class BookView(View):

    def get(self, request):
        student = Book.objects.get(pk=1)
        serializer = BookSerializer(instance=student)
        return JsonResponse(serializer.data)

    def post(self, request):
        data = json.loads(request.body)
        # 1.实例化序列化器对象
        serializer = BookSerializer(data=data)
        print(serializer)
        # 2.调用验证方法:true验证通过，反则失败
        # ret = serializer.is_valid(raise_exception=True)
        ret = serializer.is_valid()
        print(ret)

        # 验证通过，则会返回验证后的数据到validated_data属性方法
        print("成功", serializer.validated_data)

        # 验证失败，则抛出异常
        print("失败", serializer.errors)

        # 执行数据库操作
        serializer.save() # 这里会自动调用序列化器内的create或者update方法

        return HttpResponse("ok")

    def put(self, request):
        data = json.loads(request.body)
        id = data.get("id")
        book = Book.objects.filter(pk=id).first()
        # 创建序列化器对象
        # partial=True：更新部分字段
        serializer = BookSerializer(instance=book, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        # 执行数据库操作
        serializer.save()  # 调动序列化器内的create或update方法
        """
        serializer.save()之所以会自动判断什么时候执行create和update,
        原因是save内部中根据实例化序列化器时是否传递模型对象参数进来而判断的.
        """
        return HttpResponse("更新成功！")
```

**附加说明：**

1. 在对序列化器进行save()时，可以额外传递数据，这些数据可以在create() and update()的validated_data参数获取到

```python
# request.user 是django中记录当前登录用户的模型对象
serializer.save(owner=request.user)
```

2. 默认序列化器必须传递所有的require的字段，否则会抛出验证异常。但是我们可以使用partial参数来允许部分字段更新

```python
# partial=True：更新部分字段	
serializer = BookSerializer(instance=book, data=data, partial=True)
```

##### 15.7.3.3 模型类序列化器

如果我们想要使用序列化器对应的是Django的模型类，DRF为我们提供了ModelSerializer模型类序列化器来帮助我们快速创建一个Serializer类。

ModelSerializer与常规的Serializer相同，但提供了：

- 基于模型类自动生成一系列字段
- 基于模型类自动为Serializer生成validators，比如：unique_together
- 包含默认的create() 和 update() 的实现

###### 15.7.3.3.1 定义

```python
class BookModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
```

- model：指明哪个模型类
- fields：指明生成模型类的哪些字段

###### 15.7.3.3.2 指明字段

1. 使用 **fields** 来明确字段， `__all__` 代表包含所有的字段，也可以单独取字段

```python
class BookModelSerializer(serializers.ModelSerializer):
	"""图书序列化器"""
    class Meta:
        model = Book
        fields = ["id", "name","pub_date"]
```

2. 使用 **exclude** 明确排除哪些字段

```python
class BookModelSerializer(serializers.ModelSerializer):
	"""图书序列化器"""
    class Meta:
        model = Book
		exclude = ["id", "name","pub_date"]
```

3. 指明自定义字段

```python
class BookModelSerializer(serializers.ModelSerializer):
	"""图书序列化器"""
    
    content = serializers.CharField(read_only=True, default='this is content!')
    class Meta:
        model = Book
		fields = ["id", "name","pub_date", "content"]
```

4. 指明只读字段

   可以通过 **read_only_fields** 指明只读字段，即仅使用于序列化输出的字段

```python
class BookModelSerializer(serializers.ModelSerializer):
	"""图书序列化器"""
    content = serializers.CharField(default='this is content!')
    class Meta:
        model = Book
        fields = ["id", "name","pub_date", "content"]
        read_only_fields = ["content",]
```

###### 15.7.3.3.3 添加额外参数

我们可以使用 **extra_kwargs** 参数为ModelSerializer添加或修改原有的选项参数

```python
class BookModelSerializer(serializers.ModelSerializer):
	"""图书序列化器"""
    content = serializers.CharField(default='this is content!')

    class Meta:
        model = Book
        fields = "__all__"
        # fields = ["name", "pub_date", "content", "bread"]
        # read_only_fields = ["content"]
        extra_kwargs = {
            "content":{"read_only":True},
            "comment": {"max_value": 200,},
        }
```

##### 15.7.3.4 序列化器使用时机

什么时候声明的序列化器需要继承序列化器基类Serializer，什么时候继承模型序列化器类ModelSerializer？

```python
# 继承序列化器类 Serializer
	1.字段声明
    2.验证
    3.添加/保存数据功能
# 继承模型序列化器类 ModelSerializer
	1.通过函数字段声明[可选，看需求]
    2.Meta声明字段
    3.验证
    4.添加/保存数据功能
```

### 15.8 http请求与响应

drf除了在数据序列化部分简写代码外，还在视图中提供了简写操作。所以在django.views.View类基础上，drf封装了多个视图子类，提供给我们使用。

Django REST framework 提供的视图的主要作用：

- 控制序列化器的执行（验证、保存、转化数据）
- 控制数据库查询的执行
- 调用请求类和响应类

#### 15.8.1 Request

REST framewor传入视图的request对象不再是Django默认的HttpRequest对象，而是REST framework提供的扩展了HttpRequest类的Request类的对象，在drf中，原生的django的http请求对象，通过 `request._request` 来调用。

REST framework提供了Parser解析器，在接受到请求后会自动根据Content-Type指明的请求数据类型（如JSON/表单等）将请求数据进行Parse解析，解析为类字典[QueryDict]对象保存在Request对象中。

**Request对象的数据是自动根据前端发送数据的格式进行解析之后的结果。**

无论前端发送的哪种格式的数据，我们都可以以一种统一的方式读取数据。

##### 15.8.1.1 常用属性

1. **data**

`request.data` 返回解析只有的请求体数据。类似于Django中标准的 `request.POST` 和 `request.FILES` 属性，但提供如下特性：

- 包含了解析之后的文件和非文件数据
- 包含了对POST、PUT、PATCH请求方式解析后的数据
- 利用了REST framework的parsers解析器，不仅支持表单类型数据，也支持JSON类型的数据

**相当于drf的 `request.data` 替代了 django 的 `request.POST/FILES/body` 方法。** 

```python
print(request.data)
# <QueryDict: {'name': ['joker0821'], 'pub_date': ['2021-08-21'], 'bread': ['222'], 'comment': ['222']}>
```

2. **query_params**

`request.query_params` 返回解析之后的查询字符串的数据。

`request.query_params` 与Django原生的 `request.GET` 相同，只是更换了request调用的方法。

```python
print(request.query_params)  # <QueryDict: {'user': ['joker'], 'age': ['18']}>
print(request.query_params.get("user"))  # joker
print(request.query_params.getlist("user"))  # ['joker', 'alex']
```

#### 15.8.2 Response

```python
from rest_framework.response import Response
```

REST framework提供了一个相应类 `Response` ，使用该类构造响应对象时，响应的具体数据内容会被转换（renderer渲染器）成符合前端需求的类型。

REST framework提供了 `Renderer` 渲染器，用来根据请求头中的 `Accept`（接收数据类型声明）来自动转换响应数据到对应格式。如果前端请求中未进行Accept声明，则会采用默认方式处理响应数据，我们可以通过配置来修改默认响应格式。

总之，就是Renderer能通过请求到的Accept查询出客户端支持和希望的数据类型，把视图的结果以客户端能识别的格式进行返回。

可以在 **rest_framework.settings.py** 查找所有的drf默认配置项

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
        'rest_framework.renderers.JSONRenderer',  # json渲染器
        'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览器API渲染器
    )
}
```

##### 15.8.2.1 构造方式

```python
Response(data, status=None, template_name=None, headers=None, content_type=None)
```

data数据不是renderer处理之后的数据，只需传递python的内置类型的数据即可，REST framework会使用 renderer 渲染器去处理 data。

data不能是复杂结构的数据，如Django的模型类数据，对于这样的数据我们可以使用 Serializer 序列化器序列化处理后再传递给data参数。

参数说明：

- data：为响应准备的序列化处理后的数据
- template_name：模板名称，如果使用HTMLRenderer 时需指明
- status：状态码，默认200
- headers：用于存放响应头信息的字典
- content_type：响应数据的Content_Type，通常此此参数无需传递，REST framework会根据前端所需类型的数据来设置该参数

##### 15.8.2.2 常用属性

- **data：**传给response对象的序列化后，但尚未render处理的数据

- **status_code：**状态码

- **content：**经过renderer处理后的响应数据

状态码：为了方便设置状态码，REST framework在 `rest_framework.status`  模块中提供了常用状态码常量。

1. **信息告知 - 1xx**

```python
HTTP_100_CONTINUE
HTTP_101_SWITCHING_PROTOCOLS
```

2. **成功 - 2xx**

```python
HTTP_200_OK
HTTP_201_CREATED
HTTP_202_ACCEPTED
HTTP_203_NON_AUTHORITATIVE_INFORMATION
HTTP_204_NO_CONTENT
HTTP_205_RESET_CONTENT
HTTP_206_PARTIAL_CONTENT
HTTP_207_MULTI_STATUS
```

3. **重定向 - 3xx**

```python
HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT
```

4. **客户端操作 - 4xx**

```python
HTTP_400_BAD_REQUEST
HTTP_401_UNAUTHORIZED
HTTP_402_PAYMENT_REQUIRED
HTTP_403_FORBIDDEN
HTTP_404_NOT_FOUND
HTTP_405_METHOD_NOT_ALLOWED
HTTP_406_NOT_ACCEPTABLE
HTTP_407_PROXY_AUTHENTICATION_REQUIRED
HTTP_408_REQUEST_TIMEOUT
HTTP_409_CONFLICT
HTTP_410_GONE
HTTP_411_LENGTH_REQUIRED
HTTP_412_PRECONDITION_FAILED
HTTP_413_REQUEST_ENTITY_TOO_LARGE
HTTP_414_REQUEST_URI_TOO_LONG
HTTP_415_UNSUPPORTED_MEDIA_TYPE
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
HTTP_417_EXPECTATION_FAILED
HTTP_422_UNPROCESSABLE_ENTITY
HTTP_423_LOCKED
HTTP_424_FAILED_DEPENDENCY
HTTP_428_PRECONDITION_REQUIRED
HTTP_429_TOO_MANY_REQUESTS
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
```

5. **服务端错误 - 5xx**

```python
HTTP_500_INTERNAL_SERVER_ERROR
HTTP_501_NOT_IMPLEMENTED
HTTP_502_BAD_GATEWAY
HTTP_503_SERVICE_UNAVAILABLE
HTTP_504_GATEWAY_TIMEOUT
HTTP_505_HTTP_VERSION_NOT_SUPPORTED
HTTP_507_INSUFFICIENT_STORAGE
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED
```

示例：

```python
response = Response("ok",status=status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED)
response.set_cookie("username","abc")
response["company"] = "testing"
return response
```

![image-20210831152058256](j:\homework\Python学习笔记\Python_notes.assets\image-20210831152058256.png)

![image-20210831152144117](j:\homework\Python学习笔记\Python_notes.assets\image-20210831152144117.png)

### 15.9 视图

REST framework 提供了众多的通用视图基类与扩展类，以简化视图的编写；

Django REST framework 提供的视图的主要作用：

- 控制序列化器的执行（验证、保存、转换数据）
- 控制数据库查询的执行
- 调用请求类和响应类

#### 15.9.1 两个通用视图基类

##### 15.9.1.1 APIView

```python
rest_framework.view.APIView
```

APIView 是 REST framework 提供的所有视图的基类，继承自Django的 View 父类。

```python
from rest_framework.views import APIView
from rest_framework.views import View
from django.views import View
""" print(request)
django 和 rest_framework 的 views ：
	<WSGIRequest: GET '/book3/book3/'>
rest_reamework 的 APIView：
	<rest_framework.request.Request: GET '/book3/book3/'>
"""

class Book3APIView(APIView):
    def get(self, request):
        print(request) 
        return HttpResponse("ok")
```

drf的 APIView在继承 Django View的基础上，新增了以下内容：

- 传入到视图方法中的是 REST framework 的 Request 对象，而不是 Django 的 HttpRequest 对象；
- 视图方法可以返回 REST framework 的 Response 对象，视图会为响应数据设置（renderer）符合前端要求的格式；
- 任何 APIException 异常都会被捕捉到，并且处理成合适的响应信息；
- 重写了 as_view()，在进行 dispatch() 路由分发前，会对http请求进行身份认证、权限检查、访问流量控制；

支持定义的类属性：

- **authentication_classes** 列表或元组，身份认证类
- **permissoin_classes** 列表或元组，权限检查类
- **throttle_classes** 列表或元祖，流量控制类

在 `APIView` 中仍以常规得类视图定义方法来实现ge()、post()或者其他请求方式的方法。

示例：

```python
# urls.py
from django.urls import path, re_path
from book3 import views

urlpatterns = [
    path("book3/", views.Book3APIView.as_view()),
    path("books3/", views.Book3APIviews.as_view()),
    re_path("^books32/(?P<pk>\d+)/$", views.Book32APIViews.as_view()),
]
```

```python
# views.py
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import View
from django.views import View
from book1.models import Book
from book1.serializers import BookModelSerializer
# Create your views here.


class Book3APIView(APIView):
    def get(self, request):
        print(request)
        """类继承View，都是继承自django的View
        # <WSGIRequest: GET '/book3/book3/'>

        rest_framework的APIView，继承自View
        # <rest_framework.request.Request: GET '/book3/book3/'>
        
        """
        return HttpResponse("book3 APIView ok")


class Book3APIviews(APIView):
    def get(self, request):
        """ 获取所有书籍信息 """

        # 1.获取书籍的数据
        book_list = Book.objects.all()

        # 2.调用序列化器
        serializer = BookModelSerializer(instance=book_list, many=True)

        # 3.返回数据
        return Response(serializer.data)

    def post(self, request):
        """ 添加一个学生信息 """
        # 1.调用序列化器对用户提交的数据进行验证
        serializer = BookModelSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # 2.调用序列化器进行数据库操作
        serializer.save()

        # 3.返回新增数据
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Book32APIViews(APIView):
    def get(self, request, pk):
        """ 获取一个学生的信息 """
        # 1.根据id获取学生模型
        student = Book.objects.get(pk=pk)

        # 2.调用序列化器转换数据
        serializer = BookModelSerializer(instance=student)

        # 3.响应数据
        return Response(serializer.data)

    def put(self, request, pk):
        """ 修改一个学生的信息 """

        # 1.根据id查询学生信息
        student = Book.objects.get(pk=pk)

        # 2.调用序列化器，对前端发的请求进行验证
        serializer = BookModelSerializer(instance=student,
                                         data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        # 3.保存数据
        serializer.save()
        # 4.响应数据
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        """ 删除一个学生的信息 """
        Book.objects.get(pk=pk).delete()
        return Response({"message": "ok!"}, status=status.HTTP_204_NO_CONTENT)
```

##### 15.9.1.2 GenericAPIView

通用视图类主要作用就是把视图中的独特的代码抽取查出来，让视图方法中的代码更加通用，方便把通用代码进行简写。

```python
rest_framework.generics.GenericAPIView
```

继承自 `APIView` ，主要增加了操作序列化器和数据库查询的方法，作用是为下面Mixin扩展类的之心那个提供方法支持。通常在使用时，可搭配一个或多个Mixin扩展类。

1.提供的关于序列化器使用的属性与方法

- 属性

  - **serializer_class** 指明视图使用的序列化器

  ```python
  # 用于指定当前视图类中使用的默认序列化器
  serializer_class = BookModelSerializer
  ```

- 方法

  - **get_serializer_class(self)** 当出现一个视图类中调用多个序列化器时，那么可以通过条件判断在 get_serializer_class 方法中通过返回不同的序列化器类名就可以让视图方法执行不同的序列化器对象了。

    返回序列化器类，默认返回 `serializer_class` ，可以重写，例如：

    ```python
    def get_serializer_class(self):
        """ 重写获取序列化器类的方法 """
        if self.requset and self.request.method.lower() == "get":
            return BookModel2Serializer
        else:
            return BookModelSerializer
    ```

  - **get_serializer(self, args, `**`kwargs)** 返回序列化器对象，主要用来提供给Mixin扩展类使用，如果我们在视图中想要获取序列化器对象，也可以直接调用此方法。

    **注意，该方法在提供序列化器对象的时候，会向序列化器对象的context属性补充三个数据：request、format、view，这三个数据对象可以在定义序列化器时使用。**
  
    - **request** 当前视图的请求对象
    - **view** 当前请求的类视图对象
    - **format** 当前请求期望返回的数据格式
    
    ```python
    def get_serializer_context(self):
        """
            Extra context provided to the serializer class.
            """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }
    ```
    
    ```python
    # get_serializer封装了serializer_class方法并且返回
    # serializer = self.serializer_class(instance=self.queryset.get(pk=pk))
    serializer = self.get_serializer(instance=self.get_object(), context={"request":"", "format":"", "view":""})
        
    # 在序列化器中进行获取
    def create(self):
        self.context["request"]
        self.context["format"]
        self.context["view"]
    ```

2.提供的关于数据库查询的属性与方法

- 属性

  - **queryset** 指明使用的数据查询集

  ```python
  queryset = Book.objects
  ```

- 方法

  - **get_queryset(self)** 返回视图使用的查询集，主要用来提供给Mixin扩展类使用，是列表视图与详情视图获取数据的基础，默认返回 `queryser` 属性，可以重写，例如：

    ```python
    def get_queryset(self):
        user = self.request.user
        return user.accounts.all()
    ```

  - **get_object(self)** 返回单个视图模型类对象，主要用来提供给Mixin扩展类使用。在视图中可以调用该方法获取详情信息的模型类对象。**若详情访问的模型类对象不存在，会返回404。**该方法会默认使用APIView提供的checck_object_permissions方法检查当前对象是否有权限被访问。例如：

    ```python
    class Book32APIViews(GenericAPIView):
    
        serializer_class = BookModelSerializer
        queryset = Book.objects  # get_query封装时加了all，使用时直接调用queryset
    
        def get(self, request, pk):
            """ 获取一个学生的信息 """
    
            # 1.调用序列化器转换数据
            #   get_object 获取学生信息
            #   get_serializer 指定当前视图类中使用的默认序列化器
            # serializer = self.serializer_class(instance=self.queryset.get(pk=pk))
            serializer = self.get_serializer(instance=self.get_object())
    
            # 2.响应数据
            return Response(serializer.data)
    ```

3.其他可以设置的属性

- **pagination_class** 指明分页控制类
- **filter_backends** 指明过滤控制后端

为了方便学习上面的GenericcAPIView通用视图类，我们新建一个子应用。

```python
python manage.py startapp gen
```

示例：

```python
# views.py
import requests
from book1 import views
from django.core.serializers import get_serializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from book1.serializers import BookModelSerializer, BookModel2Serializer
from book1.models import Book

class Book3APIviews(GenericAPIView):
    """
    1.serializer_class 用于指定当前视图类中使用的默认序列化器
    2.queryset 用于指定当前视图类中使用的数据集
    """
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()

    def get_serializer_class(self):
        """ 重写获取序列化器类的方法 """
        if self.request.method.lower() == "get":
            return BookModel2Serializer
        else:
            return BookModelSerializer

    def get(self, request):
        """ 获取所有书籍信息 """
        # 2.调用序列化器
        # serializer = self.serializer_class(instance=self.get_queryset(), many=True)
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        # 3.返回数据
        return Response(serializer.data)

    def post(self, request):
        """ 添加一个学生信息 """
        # 1.调用序列化器对用户提交的数据进行验证
        # serializer = self.serializer_class(data=request.data, partial=True)
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        # 2.调用序列化器进行数据库操作
        serializer.save()
        # 3.返回新增数据
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Book32APIViews(GenericAPIView):

    serializer_class = BookModelSerializer
    queryset = Book.objects
    def get(self, request, pk):
        """ 获取一个学生的信息 """
        # 1.调用序列化器转换数据
        #   get_object 获取学生信息
        #   get_serializer 指定当前视图类中使用的默认序列化器
        # serializer = self.serializer_class(instance=self.queryset.get(pk=pk))
        serializer = self.get_serializer(instance=self.get_object())
        # 2.响应数据
        return Response(serializer.data)

    def put(self, request, pk):
        """ 修改一个学生的信息 """
        # 1.调用序列化器，对前端发的请求进行验证
        #   get_object 获取学生信息
        serializer = self.get_serializer(instance=self.get_object(),
                                         data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        # 2.保存数据
        serializer.save()
        # 3.响应数据
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        """ 删除一个学生的信息 """
        self.get_object().delete()
        return Response({"message": "ok!"}, status=status.HTTP_204_NO_CONTENT)
```

```python
# serializers.py
class BookModelSerializer(serializers.ModelSerializer):

    content = serializers.CharField(default='this is content!')

    class Meta:
        model = Book
        fields = "__all__"
        # fields = ["name", "pub_date", "content", "bread"]
        # read_only_fields = ["content"]
        extra_kwargs = {
            "content":{"write_only":True},
            "comment": {"max_value": 200,},
        }
```

#### 15.9.2 五个视图扩展类

作用：

提供了几种后端视图（对数据资源进行曾删改查）处理流程的实现，如果需要编写的视图属于这五种，则视图可以通过继承相应的扩展类来复用代码，减少自己编写的代码量。

这五个扩展类需要搭配GenericAPIView父类，因为五个扩展类的实现需要调用GenericAPIView提供的序列化器与数据库查询的方法，针对基本的API接口代码进行了封装提供了5个常用的视图扩展类。

```pyton
from rest_framework.mixins import ListModelMixin
```

- **ListModdelMixin**

  列表视图扩展类，提供list(request, *args, **kwargs)方法快速实现列表视图。

  该Mixin的list方法会对数据进行过滤和分页。

源码：

```python
class ListModelMixin:
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        # 过滤
        queryset = self.filter_queryset(self.get_queryset())
		# 分页
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
		# 序列化
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
```

- **CreateModelMixin**

  创建视图扩展类，提供 `create(request, *args, **kwargs)` 方法快速实现创建资源的视图，。

  如果序列化器对前端发送的数据验证失败，返回400错误。

源码：

```python
class CreateModelMixin:
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        # 获取序列化器
        serializer = self.get_serializer(data=request.data)
        # 验证
        serializer.is_valid(raise_exception=True)
        # 保存
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
```

示例：ListModdelMixin、CreateModelMixin

```python
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from book1.serializers import BookModelSerializer
from book1.models import Book


class BookListCreateView(GenericAPIView,ListModelMixin,CreateModelMixin):
    serializer_class = BookModelSerializer
    queryset = Book.objects

    def get(self, request):
        """ 获取全部数据 """
        return self.list(request)

    def post(self, request):
        """ 添加数据 """
        return self.create(request)
```

- **RetrieveModelMixin**

  查询一条数据，详情视图扩展类，提供  `retrieve(request, *args, **kwargs)` 方法，可以快速实现返回一个存在的数据对象。如果存在，返回200， 否则返回404。

源码：

```python
class RetrieveModelMixin:
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        # 获取对象，会检查对象的权限
        instance = self.get_object()
        # 获取序列化器
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
```

- **UpdateModelMixin**

  更新视图扩展类，提供 `update(request, *args, **kwargs)` 方法，可以快速实现更新一个存在的数据对象。

  同时也提供 `partial_update(request, *args, **kwargs)` 方法，可以实现局部更新。

  成功返回200，序列化器校验数据失败时，返回400错误。

源码：

```python
class UpdateModelMixin:
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
```

- **DestroyModelMixin**

  删除视图扩展类，提供 `destroy(request, *args, **kwargs)` 方法，可以快速实现删除一个存在的数据对象。

  成功返回204，不存在返回404。

源码：

```python
class DestroyModelMixin:
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
```

示例：RetrieveModelMixin、UpdateModelMixin、DestroyModelMixin

```python
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from book1.serializers import BookModelSerializer
from book1.models import Book

class BookRetUpDeView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = BookModelSerializer
    queryset = Book.objects

    def get(self, request, pk):
        """ 获取一条数据 """
        return self.retrieve(request, pk)

    def put(self, request, pk):
        """ 修改数据 """
        return self.update(request, pk)

    def delete(self, request, pk):
        """ 删除数据 """
        return self.destroy(request, pk)
```

#### 15.9.3 通用结合扩展视图

- **CreateAPIView**

  方法：post

  继承自：GenericAPIView、CreateModelMixin

源码：

```python
class CreateAPIView(mixins.CreateModelMixin,
                    GenericAPIView):
    """
    Concrete view for creating a model instance.
    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

- **ListAPIView**

  方法：get

  继承自：GenericAPIView、ListModelMixin

源码：

```python
class ListAPIView(mixins.ListModelMixin,
                  GenericAPIView):
    """
    Concrete view for listing a queryset.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
```

- **RetrieveAPIView**

  方法：get

  继承自：GenericAPIView、RetrieveModelMixin

源码：

```python
class RetrieveAPIView(mixins.RetrieveModelMixin,
                      GenericAPIView):
    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
```

- **DestoryAPIView**

  方法：delete

  继承自：GenericAPIView、DestoryModelMixin

源码：

```python
class DestroyAPIView(mixins.DestroyModelMixin,
                     GenericAPIView):
    """
    Concrete view for deleting a model instance.
    """
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

- **UpdateAPIView**

  方法：put、patch

  继承自：GenericAPIView、UpdateModelMixin

源码：

```python
class UpdateAPIView(mixins.UpdateModelMixin,
                    GenericAPIView):
    """
    Concrete view for updating a model instance.
    """
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
```

- **ListCreateAPIView**

  方法：get、post

  继承自：GenericAPIView、ListModelMixin、CreateModelMixin

源码：

```python
class ListCreateAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

- **RetrieveUpdateAPIView**

  方法：get、put、patch

  继承自： GenericAPIView、RetrieveModelMixin、UpdateModelMixin

源码：

```python
class RetrieveUpdateAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            GenericAPIView):
    """
    Concrete view for retrieving, updating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
```

- **RetrieveDestroyAPIView**

  方法：get、delete

  继承自：GenericAPIView、RetrieveModelMixin、DestroyModelMixin

源码：

```python
class RetrieveDestroyAPIView(mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             GenericAPIView):
    """
    Concrete view for retrieving or deleting a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

```

- **RetrieveUpdateDestoryAPIView**

  方法：get、put、patch、delete

  继承自：GenericAPIView、RetrieveModelMixin、UpdateModelMixin、DestoryModelMixin

源码：

```python
class RetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

示例：

```python
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from book1.serializers import BookModelSerializer
from book1.models import Book


class BookGenList(ListAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()

class BookGenCre(CreateAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()

class BookGenLiCre(ListCreateAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()

class BookGenRet(RetrieveAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()

class BookGenDes(DestroyAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()

class BookGenUp(UpdateAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()

class BookGenReUp(RetrieveUpdateAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()

class BookGenReDe(RetrieveDestroyAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()

class BookGenReUpDe(RetrieveUpdateDestroyAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()
```

```python
# urls.py
from django.urls import re_path,path
from set import views

urlpatterns = [
    # 通用结合他拓展视图路由
    path("li/", views.BookGenList.as_view()),
    path("cre/", views.BookGenCre.as_view()),
    path("li_cre/", views.BookGenLiCre.as_view()),
    re_path("re/(?P<pk>\d+)/$", views.BookGenRet.as_view()),
    # re_path("de/(?P<pk>\d+)/$", views.BookGenDes.as_view()),
    # re_path("up/(?P<pk>\d+)/$", views.BookGenUp.as_view()),
    re_path("re_up/(?P<pk>\d+)/$", views.BookGenReUp.as_view()),
    re_path("re_de/(?P<pk>\d+)/$", views.BookGenReDe.as_view()),
    re_path("re_up_de/(?P<pk>\d+)/$", views.BookGenReUpDe.as_view()),
]
```

**注意：删除和修改的路由不与下边包含这两个的路由同时开启，否则会冲突。**

### 16.0 视图集

为了让视图代码变得更加简短，drf提供了视图集【viewsets】，视图集允许开发者自定义视图方法名，还允许一个类分配多个不同的路由，从而让操作同一个模型的视图方法写在一个视图类中。

使用视图集ViewSet，可以将一系列逻辑相关的动作放到一个类中：

- list() 提供一组数据
- retrieve() 提供单个数据
- create() 创建数据
- update() 保存数据
- destory() 删除数据

ViewSet视图集类不再固定实现get()、post()等方法，而是使用 **action** 动作，灵活实现将路由和视图进行绑定。

视图集只在使用as_view()方法的时候，才会将 **action** 动作与具体请求方式对应上。

#### 16.0.1 常用的视图集父类

- **ViewSet**

  继承自 `APIView`与`ViewSetMixin` ，作用也与APIView基本类似，提供了身份认证、权限校验、流量管理等。

  **ViewSet主要通过继承ViewSetMixin来实现在调用as_view()时传入字典（如{'get':'list'}）的映射处理工作。**

  在ViewSet中，没有提供任何动作action方法，需要我们自己实现action方法。

示例：

```python
# urls.py
from django.urls import path, re_path
from viewset import views


urlpatterns = [
    path("viewset/", views.BookViewSet.as_view({"get":"get_all", "post":"post"})),
    re_path("viewset/(?P<pk>\d+)/$", views.BookViewSet.as_view({"get":"get_one", "put":"put", "delete":"delete"}))
]
```

```python
# views.py
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from book1.models import Book
from book1.serializers import BookModelSerializer



class BookViewSet(ViewSet):
    """ 通用视图集：继承ViewSet """
    def get_all(self, request):
        """ 获取所有书籍信息 """
        book_list = Book.objects.all()
        serializer = BookModelSerializer(instance=book_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ 添加一本书的信息 """
        serializer = BookModelSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_one(self, request, pk):
        """ 获取一本书的信息 """
        student = Book.objects.get(pk=pk)
        serializer = BookModelSerializer(instance=student)
        return Response(serializer.data)

    def put(self, request, pk):
        """ 修改一本书的信息 """
        student = Book.objects.get(pk=pk)
        serializer = BookModelSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        """ 删除一本书的信息 """
        Book.objects.get(pk=pk).delete()
        return Response({"message": "ok!"}, status=status.HTTP_204_NO_CONTENT)

```

- **GenericViewSet**

  使用ViewSet通常并不方便，因为list、retrieve、create、update、destory等方法都需要自己编写，而这些方法与前面讲过的Mixin扩展类提供的方法同名，所以我们可以通过继承Mixin扩展类来复用这些方法而无需自己编写。但是Mixin扩展类依赖与 `GenericAPIView` ，所以还需要继承 `GenericAPIView` 。

  **GenericViewSet** 就帮助我们完成了这样的继承工作，继承自 `GenericAPIView` 与 `ViewSetMixin` ，在实现了调用as_view()时传入字典（如 `{'get':'list'}` ）的映射处理工作的同时，还提供了 `GenericAPIView` 提供的基础方法，可以直接搭配Mixin扩展类使用。

示例一：继承通用视图集GenericViewSet

```python
# urls.py
urlpatterns = [
    path("viewset_gen/", views.BookGenViewSet.as_view({"get":"get_all", "post":"post"})),
    re_path("viewset_gen/(?P<pk>\d+)/$", views.BookGenViewSet.as_view({"get":"get_one", "put":"put", "delete":"delete"})),
]
```

```python
# views.py
from rest_framework.viewsets import GenericViewSet

class BookGenViewSet(GenericViewSet):
    """ 继承GenericViewSet """
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()

    def get_all(self, request):
        """ 获取所有书籍信息 """
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        """ 添加一本书的信息 """
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_one(self, request, pk):
        """ 获取一本书的信息 """
        serializer = self.get_serializer(instance=self.get_object())
        # 2.响应数据
        return Response(serializer.data)

    def put(self, request, pk):
        """ 修改一本书的信息 """
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        """ 删除一本书的信息 """
        self.get_object().delete()
        return Response({"message": "ok!"}, status=status.HTTP_204_NO_CONTENT)
```

示例二：通用视图集和扩展类

```python
# views.py
urlpatterns = [
    path("viewset_gen_mixin/", views.BookMixinViewSet.as_view({"get":"list", "post":"create"})),
    re_path("viewset_gen_mixin/(?P<pk>\d+)/$", views.BookMixinViewSet.as_view({"get":"retrieve", "put":"update", "delete":"destroy"}))
]
```

```python
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

class BookMixinViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    """ 通用视图集加扩展类 """
    serializer_class = BookModelSerializer
    queryset = Book.objects
```

- **ModelViewSet**

  继承自 `GenericViewSet` ，同时包括了ListModelMixin、RetrieveModelMixin、CreateModelMixin、UpdateModelMixin、DestoryModelMixin。

源码：

```python
class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass
```

示例：继承ModelViewSet后，就可以简写示例二的代码

```python
from rest_framework.viewsets import GenericViewSet, ModelViewSet

class BookMixinViewSet(ModelViewSet):
    """ Model集合了5个扩展类"""
    serializer_class = BookModelSerializer
    queryset = Book.objects
```

- **ReadOnlyModelViewSet**

  继承自 `GenericViewSet` ，同时包括了ListModelMixin、RetrieveModelMixin。

源码：

```python
class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    """
    A viewset that provides default `list()` and `retrieve()` actions.
    """
    pass
```

示例：

```python
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
class BookMixinViewSet(ReadOnlyModelViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = BookModelSerializer
    queryset = Book.objects
```

#### 16.0.2 视图集中定义action动作

在视图集中，除了上述默认的方法动作外，还可以添加自定义动作。

示例：

```python
# urls.py
urlpatterns = [
        path("stu/", views.BookMixinViewSet.as_view({"get":"login"})),
]
```

```python
# views.py
from rest_framework.viewsets import ModelViewSet,
class BookMixinViewSet(ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects
    
    def login(self, request):
        return Response("登陆成功！")
```

在视图集中，我们可以通过action对象属性来获取当前请求视图集时的action动作是哪个。

示例：

```python
class BookMixinViewSet(ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects

    def get_serializer_class(self):
        print(self.action)  # 本次请求的视图方法名称
        if self.action.lower() == 'list':
            return BookModelSerializer
        else:
            return BookModel2Serializer
# 打印：list create
# 共通过旅游访问，可以看到本次请求的方法名
```

### 16.1 路由Routers

对于视图集ViewSet，我们除了可以手动指明请求方式与动作action之间的对应关系外，还可以使用Routers来帮助我们快速实现路由信息。

REST framework提供了两个router：

- **SimpleRouter**
- **DefaultRouter**

#### 16.1.1 使用方法

1. **创建router对象，并注册视图集**

   示例：

   ```python
   from rest_framework.routers import SimpleRouter, DefaultRouter
   from django.urls import path, re_path
   from viewset import views
   
   urlpatterns = [
       
   ]
   
   # 实例化路由类
   router = DefaultRouter()
   # 注册视图集
   router.register(prefix="viewset_gen_mixin", viewset=views.BookMixinViewSet, basename='20210906')
   print(router.urls)
   # 把生成的路由列表追加到urlpatterns中
   urlpatterns += router.urls
   ```

2. **注册视图集参数：register(prefix, viewset, base_name)**

   - prefix：该视图集路由的前缀
   - viewset：指定视图集
   - base_name：路由别名的前缀

3. **SimpleRouter 与 DefaultRouter 的区别**

   - SimpleRouter ：无图形化页面提示路由
   - DefaultRouter ：图形化页面提示路由

上面的代码成功生成了路由地址[增、删、改、查一条、查多条]，但是不会自动生成我们自定义的的视图。所以我们如果也要给自定义方法生成路由，则需要用action进行声明。

#### 16.1.2 视图集附加action

在视图集中，如果想要让Router自动帮我们为自定义的视图生成路由信息，需要使用 `rest_framework.decorators.action` 装饰器进行装饰。

以action装饰器装饰的方法名会作为action动作名，与list、retrieve等同。

action装饰器可以接收两个参数：

- methods：声明该action对应的请求方式，列表传递
- detail：声明该action的路径是否与单一资源对应
  - True：表示路径格式是 `xxx/<pk>/action方法名/` 
  - False：表示路径格式是 `xxx/action方法名`
- url_path：设置访问视图的子路由，默认为方法名

示例：

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class BookMixinViewSet(ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects

    def get_serializer_class(self):
        # print(self.action)  # 本次请求的视图方法名称  list create
        if self.action.lower() == 'list':
            return BookModelSerializer
        else:
            return BookModel2Serializer
    
    # <URLPattern '^viewset_gen_mixin/(?P<pk>[^/.]+)/test/$' [name='20210906-login']>
    @action(methods=['get', 'post'], detail=True, url_path='test')
    def login(self, request, pk ):
        print(pk)
        return Response("登陆成功！")


    # <URLPattern '^viewset_gen_mixin/logout/$' [name='20210906-logout']>
    @action(methods=['get', 'post'], detail=False)
    def logout(self, request):
        return Response("等了！")
```

**路由router形成url的方式**

1. SimpleRouter

![SimpleRouter](j:\homework\Python学习笔记\Python_notes.assets\SimpleRouter.png)

2. DefaultRouter

![DefaultRouter](j:\homework\Python学习笔记\Python_notes.assets\DefaultRouter.png)

DefaultRouter与SimpleRouter的区别是，DefaultRouter会多附带一个默认的API根视图，返回一个包含所有列表视图的超链接响应数据。

### 16.2 常用组件

提前配置：

1. 创建子应用

```python
python manage.py startapp opt
```

2. 创建管理员

```python
python manage.py createsuperuser
```

3. settings.py配置

```python
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```

4. 在settings.py中注册子应用

```python
INSTALLED_APPS = [
	'opt',  # drf的常用组件
]

# 总路由分发
pth("opt", include("opt.urls"))
```

#### 16.2.1 认证Authentication

1. 在配置文件中配置全局默认的认证方案

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',  # session认证
        'rest_framework.authentication.BasicAuthentication',  # 基本认证
    )
}
```

2. 在每个视图中通过设置authentication_classes类属性来设置

```python
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView


class ExampleView(APIView):
    # 类属性
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    def get(self, request):
        pass
```

认证时会有两种可能的返回值，这个需要我们配置权限组件类使用：

- 401 Unauthorized 未认证
- 403 Permission Denied 权限被禁用

#### 16.2.2 权限Permissions

权限控制可以限制用户对于视图的访问和对于具体数据对象的访问。

- 在执行视图的as_view()方法的dispatch()的方法前，会先进行视图访问权限的判断。
- 在通过get_object()获取具体模型对象时，会进行模型对象访问权限的判断。

**提供的权限：**

- AllowAny：允许所有用户
- IsAuthenticated：仅允许通用过登录的用户
- IsAdminUser：仅允许管理员用户
- IsAuthenticatedOrReadOnly：已经登录认证的用户可以对数据进行增删改操作，没有登录认证的用户只能查看数据

**配置使用：**

chrome浏览器进入无痕模式的快捷键 `Ctrl+Shift+N` 

在配置文件settings.py中全局设置默认的权限管理类，如： 

```python
# drf的配置信息，需要卸载django的配置文件，而且必须写在REST_FRAMEWORK的字典中，才能被drf识别
# 权限全局配置
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',  # 已经登录认证的用户才能访问
    'rest_framework.permissions.IsAdminUser',  # 管理员用户才可以登录
    'rest_framework.permissions.IsAuthenticatedOrReadOnly',  # 登录的用户可以操作数据，没有登录的只可查看数据
    ),
}
```

如果未指明，则采用如下默认配置

```python
'DEFAULT_PERMISSION_CLASSES': (
   'rest_framework.permissions.AllowAny',
)
```

也可以在具体的视图中通过premission_classess属性来单独设置，如

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = (IsAuthenticated,)
```

示例：

```python
from inspect import FrameInfo
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from app01.models import Student
from baseview.serializers import StudentModelSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action

class PermissionAPIView(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = Student.objects

    @action(methods=["get"], detail=False)
    def auth(self, request):
        return Response("ok")

    @action(methods=["get"], detail=False)
    def login(self, request):
        return Response("登录成功！")
```

**自定义权限：**

如需自定义权限，需继承 `rest_framework.permissions.BasePermission` 父类，并实现以下两个任何一个方法或全部

- `.has_permission(self, request, view)` 
  - 是否可以访问视图，view 表示当前视图对象
- `.has_object_permission(self, request, view, obj)` 
  - 是否可以访问数据对象，view表示当前视图，obj模型数据对象

示例：

在当前子应用下，创建一个权限文件permissions.py中声明自定义权限类：

```python
class ConstomPermission(BasePermission):
    """ 自定义权限 """
    def has_permission(self, request, view):
        if request.user and request.user.username == "xiaoming":
            return True
```

```python
class PermissionAPIView(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = Student.objects

    # 自定义权限
    permission_classes = [ConstomPermission, ]

    @action(methods=["get"], detail=False)
    def auth(self, request):
        return Response("ok")

    @action(methods=["get"], detail=False)
    def login(self, request):
        return Response("登录成功！")
```

#### 16.2.3 限流Throttling

可以对接口访问的频率进行限制，以减轻服务器压力，或者实现特定的业务。

一般用于付费购买次数，投票等场景使用。

**可选限流类：**

1. AnonRateThrottle

   限制所有匿名未认证用户，使用ip区分用户

   使用 `DEFAULT_THROTTLE_RATES['anon']` 来设置频率

2. UserRateThrottle
   限制认证用户，使用UserId来区分
   使用 `DEFAULT_THROTTLE_RATES['USER']` 来设置频率

3. ScopedRateThrottle

   限制用户对于每个视图的访问频次，使用ip或UserId来设置频率

示例：

```python
class ContactListView(APIView):
    throttle_scope = 'contacts'
   	return Response("ok!")

class UploadView(APIView):
    throttle_scope = 'uploads'
    return Response("ok!")
    
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'contacts': '1000/day',
        'uploads': '20/day'
    }
}
```

**使用方法：**

可以在配置文件中，使用 `DEFAULT_THROTTLE_CLASSES` 和 `DEFAULT_THROTTLE_RATES` 进行全局配置。

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': ( # 启用的限制类
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {   # 限制频率
        'anon': '100/day',
        'user': '1000/day'
    }
}
```

`DEFAULT_THROTTLE_RATES` 可以使用 `second`, `minute`, `hour` 或`day`来指明周期。

也可以在具体视图中通过 `throttle_classess` 属性来配置，如：

```python
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

class ExampleView(APIView):
    throttle_classes = [UserRateThrottle,]
```

示例：

全局配置中设置访问频率

```python
# settings.py

REST_FRAMEWORK = {

    # 配置认证方式
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',  # session认证
        'rest_framework.authentication.BasicAuthentication',  # 基本认证
    ),
    # 权限全局配置
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',  # 已经登录认证的用户才能访问
    'rest_framework.permissions.IsAdminUser',  # 管理员用户才可以登录
    'rest_framework.permissions.IsAuthenticatedOrReadOnly',  # 登录的用户可以操作数据，没有登录的只可查看数据
    ),

    # 限流全局配置
    # 'DEFAULT_THROTTLE_CLASSES': (  # 启用的限制类
    #     'rest_framework.throttling.AnonRateThrottle',  # 匿名用户
    #     'rest_framework.throttling.UserRateThrottle'),  # 登录用户
    'DEFAULT_THROTTLE_RATES': {  # 限制频率
        'anon': '5/day',
        'user': '10/day',
        'access': '15/minute',
    }
}
```

路由配置：

```python
from django.urls import re_path, path
from rest_framework.routers import DefaultRouter
from opt import views

urlpatterns = []

router = DefaultRouter()
router.register(prefix="opt1", viewset=views.PermissionAPIView, basename="20210928-1")
router.register(prefix="opt2", viewset=views.ThrottlingAPIView, basename="20210928-2")
urlpatterns += router.urls
```

视图代码：

```python
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from app01.models import Student
from baseview.serializers import StudentModelSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from rest_framework.decorators import action
class ThrottlingAPIView(ModelViewSet):
    """局部配置限流"""
    serializer_class = StudentModelSerializer
    queryset = Student.objects
    # 限流配置
    throttle_classes = [UserRateThrottle,AnonRateThrottle]
    # 自定义限流
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "access"
    @action(methods = ["get"], detail=False)
    def login(self, request):
        return Response("ok")
```

#### 16.2.4 过滤Filtering

对于列表数据可能需要根据字段进行过滤，我们可以通过添加django-fitlter扩展来增强支持。

```python
pip install django-filter
```

在配置文件settings.py中增加过滤组件

```python
INSTALLED_APPS = [
    ...
    'django_filters',  # 需要注册子应用，
]

REST_FRAMEWORK = {
    ...
    # 全局配置，也可以使用局部配置
    'DEFAULT_FILTER_BACKENDS':('django_filters.rest_framework.DjangoFilterBackend',),
}
```

在视图类中添加类属性filter_fields，指定可以过滤的字段

```python
class FilterAPIView(ModelViewSet):
    """ 过滤配置 """
    serializer_class = StudentModelSerializer
    queryset = Student.objects

    filter_fields = ["sex", "age"]

# 127.0.0.1:8000/opt/opt3/?sex=true  # 单个过滤条件
# 127.0.0.1:8000/opt/opt3/?sex=false&age=27  # 多个并列的过滤条件
```

#### 16.2.5 排序Ordering

对于列表数据，REST framework提供了  **OrderingFilter** 过滤器来帮助我们快速指明数据按照指定字段进行排序

**使用方法：**

在类视图中设置 filter_backends，使用 `rest_framework.filters.OrderingFilter` 过滤器，REST framework会在请求的查询字符串参数中检查是否包含了ordering参数，如果包含了ordering参数，则按照ordering参数指明的排序字段对数据集进行排序。

前端可以传递的ordering参数的可选字段值需要在ordering_fields中指明。

示例：

```python
from rest_framework.filters import OrderingFilter
class OrderingAPIView(ModelViewSet):
    """ 排序配置 """
    serializer_class = StudentModelSerializer
    queryset = Student.objects

    filter_backends = [OrderingFilter,]
    ordering_fields = ["id", "age"]

# http://127.0.0.1:8000/opt/opt4/?ordering=age
# -id 表示针对id字段进行倒序排序
# id  表示针对id字段进行升序排序
```

如果需要在过滤以后再次进行排序，则需要两者同步。因为排序配置和过滤配置使用同一个类属性，所以当视图中需要使用排序和过滤时，要么一起写在全部配置中，要么一起写在视图类中。

示例：

```python
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
class OrderingAPIView(ModelViewSet):
    """ 排序配置 """
    serializer_class = StudentModelSerializer
    queryset = Student.objects

    filter_backends = [OrderingFilter, DjangoFilterBackend] 
    ordering_fields = ["id", "age"]
    filter_fields = ["sex", "age"]
    
# http://127.0.0.1:8000/opt/opt4/?sex=0&ordering=-age
```

配置文件：

```python
    # 过滤组件[全局引入]
    # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend','rest_framework.filters.OrderingFilter')
```

#### 16.2.6 分页Pagination

REST framework提供了分页的功能。

我们可以在配置文件中设置全局的分页方式，如：

```python
# 分页配置
'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
'PAGE_SIZE': 3  # 每页数目
```

如果在全局配置 settings.py 文件中配置了全局分页，那么在drf中凡是调用了ListModelMixin的list()，才会自动分页。如果项目中出现大量需要分页的数据，只有部分不需要分页，则可以在部分的视图类中关闭分页功能。

```python
class 视图类(ListAPIView):
	pagination_class = None
```

示例：

```python
class PaginationAPIView(ModelViewSet):
    """ 分页配置 """
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()
```

也可以通过自定义Pagination类，来为视图添加不同分页行为。在视图中通过 `pagination_class` 属性来指明。

```python
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000
class BookDetailView(RetrieveAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    pagination_class = LargeResultsSetPagination
```

**可选分页器：**

1. **页码分页器：PageNumberPagination**

   前端访问形式：

   ```python
   GET  http://127.0.0.1:8000/students/?page=4
   
   # www.xxx.com?size=10&page=1
   # www.xxx.com?size=10&page=2
   # www.xxx.com?size=10&page=3
   # www.xxx.com?size=10&page=4
   # www.xxx.com?size=10&page=5
   ```

   可以在子类中定义的属性：

   - page_size：每页显示数量
   - page_query_param：前端发送的页数关键字名，默认为 "page"
   - page_size_query_param：前端发送的每页数目关键字名，默认为None
   - max_page_size：前端最多能设置每页显示数量

   ```python
   """ 页码分页器：PageNumberPagination """
   from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
   class PageNumberView(PageNumberPagination):
       # 默认每一页显示的数据量
       page_size = 2
       # 允许客户端通过get参数来控制每一页的数据量
       page_size_query_param = "size"
       # 每页最大显示条数
       max_page_size = 5
       # 自定义页码的参数名
       page_query_param = "p"
   
   class PaginationAPIView(ModelViewSet):
       """ 分页配置 """
       serializer_class = StudentModelSerializer
       queryset = Student.objects
       pagination_class = PageNumberView
   
   # 127.0.0.1/four/students/?p=1&size=5
   ```

2. **偏移量分页器：LimitOffsetPagination**

   前端访问形式：

   ```python
   GET http://127.0.0.1/four/students/?limit=100&offset=100
       
   # www.xxx.com?limit=10&offset=0
   # www.xxx.com?limit=10&offset=10
   # www.xxx.com?limit=10&offset=20
   # www.xxx.com?limit=10&offset=30
   # www.xxx.com?limit=10&offset=40
   ```
   
   可以在子类中定义的属性：
   
   - default_limit：默认限制，默认值与 page_size 设置的一致
   - limit_query_param：limit参数名，默认 limit
   - offset_query_param：offset参数名，默认 offset
   - max_limit：最大limit限制，默认 None
   
   ```python
   from rest_framework.pagination import LimitOffsetPagination
   class StandardLimitOffsetPagination(LimitOffsetPagination):
       # 默认每一页查询的数据量,类似上面的page_size
       default_limit = 2
       # 允许客户端通过get参数来控制每一页的数据量,默认limit
       limit_query_param = "limit"
       # 每页最大显示条数
       max_limit = 5
       # 偏移参数名
       offset_query_param = "offset"
   
   class PaginationAPIView(ModelViewSet):
       """ 分页配置 """
       serializer_class = StudentModelSerializer
       queryset = Student.objects
       pagination_class = LimitOffsetView
   # http://127.0.0.1:8000/opt/opt5/?limit=2&offset=4
   ```

#### 12.2.7 异常处理Exceptions

REST framework提供了自定义异常处理，我们可以自定义的方式来编写异常处理函数。

例如：我们想创建一个自定义异常函数，这个函数，我们保存到当前主应用中

> 实际工作中，我们可以设置一个独立的目录来保存这种公共的函数/工具/类库

示例：

```python
# exceptions.py
from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    """
    自定义异常处理函数
    :param exc: 异常对象，本次发生的异常对象
    :param context: 字典，异常出现时的执行上下文环境
    :ret
    """

    # 先调用drf封装的异常处理机制进行判断
    response = exception_handler(exc, context)

    # 判断异常是否drf存在
    if response is None:
        """ 出现drf不能处理的异常 """
        if isinstance(exc, DatabaseError):
            view = context["view"]
            print("数据库错误, {%s: %s}" % (view, exc))
            return Response({"detail": "服务器错误"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        
        if isinstance(exc, ZeroDivisionError):
            view = context.get("view")
            print()
            return Response("0不能作为除数,{%s: %s}" %(view, exc), status=status.HTTP_507_INSUFFICIENT_STORAGE)
        
    return response
```

```python
# views.py
class ExceptionAPIView(ModelViewSet):
    """ 异常处理 """
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

    @action(methods=["get"], detail=False)
    def get(self, request):
        10/0
        return Response("ok")
```

![image-20210930101648428](j:\homework\Python学习笔记\Python_notes.assets\image-20210930101648428.png)

在主应用的配置文件settings.py中声明自定义的异常处理

```python
REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER': 'drfdemo.exceptions.custom_exception_handler',
}
```

如果未声明，会采用默认的方式，如下：

```python
# rest_frame/settings.py
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
}
```

**REST framework定义的异常：**

APIException使用drf中所有异常的父类，他的子类有如下这些：

- ParseError：解析错误

- AuthenticationFailed：认证失败
- NotAuthenticated：尚未认证
- PermissionDenied：权限受限
- NotFound：未找到
- MethodNotAllowed：请求方式不支持
- NotAcceptable：要获取的数据格式不支持
- Throttled：超过限流次数
- ValidationError：校验失败

如上，很多异常没有在以上的这些中列出来，就需要我们在自定义异常中自己处理了。

#### 12.2.8 自动生成接口文档

> 官方文档：http://core-api.github.io/python-client/
>
> 接口文档：showdoc

REST framework可以自动帮助我们生成接口文档。

接口文档以网页的方式呈现。

自动接口文档能生成的是继承自`APIView`及其子类的视图。

1. 安装coreapi

   REST framewrok生成接口文档需要`coreapi`库的支持

   ```python
   pip install coreapi
   ```

2. 设置接口文档访问路径

   在settings.py中配置接口文档

   ```python
   REST_FRAMEWORK = {
       # 接口文档
       'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
   }
   ```

3. 在总路由中添加接口文档路径

   文档路由对应的视图配置为：
   `rest_framework.documentation.include_docs_urls`

   ```python
   from rest_framework.documentation import include_docs_urls
   
   urlpatterns = [
       ...
       path('docs/', include_docs_urls(title='站点标题-0930'))
   ]
   ```

   参数`title`为接口文档网站的标题

**文档描述说明定义的位置：**

- 单一方法的视图，可直接使用类视图的文档字符串，如：

  ```python
  class ExceptionAPIView(generics.ListAPIView):
      """
      数据异常机制.
      """
  ```

- 包含多个方法的视图，在类视图的文档字符串中，根据方法名定义，如：

  ```python
  class FilterAPIView(ModelViewSet):
      def get(self, request):
          """
          get:获取全部数据.
          """
      def post(self, request):
          """
          post:添加数据.
          """
      def get_one(self, request, pk):
          """
          get_one:获取一条数据.
          """
      def put(self, request, pk):
          """
          put:修改数据.
          """
  
      def delete(self, request, pk):
          """
          delete:删除数据.
  ```

- 对于视图集ViewSet，在类视图的文档字符串中分开定义，使用action名称区分，如：

  ```python
  class FilterAPIView(ModelViewSet):
      """
      list:
      返回数据列表.
  
      create:
      新建图书.
  
      read:
      查询一条信息.
  
      update:
      修改数据.
  
      partial_update:
      只更新部分数据.
  
      delete:
      删除一条数据.
      """
  ```

**访问接口文档网页：**

浏览器访问 `127.0.0.1:8000/docs/`，即可看到自动生成的接口文档。

![image-20210930113831669](j:\homework\Python学习笔记\Python_notes.assets\image-20210930113831669.png)

**两点说明：**

1. 视图集ViewSet中的retrieve名称，在接口文档网站中叫做read

2. 参数Description需要在模型类或序列化器类的字段中以help_text选项定义，如：

   ```python
   class Student(models.Model):
       """
       age = models.IntegerField(default=0, verbose_name='年龄', help_text='年龄')
   	"""
   ```

   或

   ```python
   class StudentSerializer(serializers.ModelSerializer):
       class Meta:
           model = Student
           fields = "__all__"
           extra_kwargs = {
               'age': {
                   'required': True,
                   'help_text': '年龄'
               }
           }
   ```

### 16.3 后台管理工具

django内置了一个强大的组件叫Admin，提供给网站管理员快速开发运营后台的管理站点。

> 站点文档： https://docs.djangoproject.com/zh-hans/2.2/ref/contrib/admin/
>
> 辅助文档：https://www.runoob.com/django/django-admin-manage-tool.html

**注意：要使用Admin，必须先创建超级管理员**

```python
python manage.py createsuperuser
```

访问地址：http://127.0.0.1:8000/admin，访问效果如下：

![image-20210930154641861](j:\homework\Python学习笔记\Python_notes.assets\image-20210930154641861.png)

admin站点默认并没有提供其他的操作给我们，所以一切功能都需要我们进行配置，在项目中，我们每次创建子应用的时候都会存在一个admin.py文件，这个文件就是用于配置admin站点功能的文件。

admin.py里面允许我们编写的代码一共可以分成2部分：列表页配置，详情页配置

#### 16.3.1 Admin列表页的配置

主要用于针对项目中各个子应用里面的models.py里面的模型，根据这些模型自动生成后台运营站点的管理功能。

```python
from django.contrib import admin
from app01.models import Student


class StudentModelAdmin(admin.ModelAdmin):
    pass


# admin.site.register(模型类, 模型管理类)
admin.site.register(Student, StudentModelAdmin)

```

模型：

```python
from datetime import datetime
from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(null=False, max_length=32, verbose_name="姓名", help_text="姓名")
    sex = models.BooleanField(default=True, verbose_name="性别", help_text="性别")
    age = models.IntegerField(verbose_name="年龄", help_text="年龄")
    class_num = models.CharField(max_length=5, verbose_name="班级", help_text="班级")
    description = models.TextField(max_length=100, verbose_name="个性签名", help_text="个人签名")
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间", help_text="创建时间")

    class Meta:
        # 设置表明
        db_table = 'tb_students'
        managed = True
        verbose_name = '学生表'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name

    from datetime import datetime
    # 模型中如果希望新增自定义字段方法
    @property
    def born(self):
        return datetime.now().year - self.age
```

列表配置：

```python
from django.contrib import admin
from app01.models import Student


class StudentModelAdmin(admin.ModelAdmin):
    """ 学生模型管理类 """

    # 设置列表显示的字段
    list_display = [
        "id", "name", "sex", "age", "class_num", "description", "create_time", "my_born"
    ]

    # 指定时间字段，根据不同值来进行选项排列
    # date_hierarchy = "create_time"

    # 设置默认排序字段,字段前面加-号表示倒叙排列
    ordering = ["id"]

    # 下方控制栏是否显示,默认False表示隐藏
    actions_on_bottom = True

    # 上方控制栏是否显示,默认False表示隐藏
    actions_on_top = True

    # 过滤器,按指定字段进行过滤
    list_filter = ["class_num", "age"]

    # 搜索内容
    search_fields = ["name", "class_num"]

    def my_born(self, obj):
        return str(obj.born)+"年"

    # 自定义字段点击时使用哪个字段作为排序条件
    my_born.admin_order_field = "age"

    # 自定义字段的描述信息
    my_born.short_description = "出生日期"


# admin.site.register(模型类, 模型管理类)
admin.site.register(Student, StudentModelAdmin)
```

#### 16.3.2 Admin详情页的配置

```python
from django.contrib import admin
from app01.models import Student


class StudentModelAdmin(admin.ModelAdmin):
    """ 学生模型管理类 """

    # 设置列表显示的字段
    list_display = [
        "id", "name", "sex", "age", "class_num", "description", "create_time", "my_born"
    ]

    # 指定时间字段，根据不同值来进行选项排列
    # date_hierarchy = "create_time"

    # 设置默认排序字段,字段前面加-号表示倒叙排列
    ordering = ["id"]

    # 下方控制栏是否显示,默认False表示隐藏
    actions_on_bottom = True

    # 上方控制栏是否显示,默认False表示隐藏
    actions_on_top = True

    # 过滤器,按指定字段进行过滤
    list_filter = ["class_num", "age"]

    # 搜索内容
    search_fields = ["name", "class_num"]

    def my_born(self, obj):
        return str(obj.born)+"年"

    # 自定义字段点击时使用哪个字段作为排序条件
    my_born.admin_order_field = "age"

    # 自定义字段的描述信息
    my_born.short_description = "出生日期"


    def delete_model(self, request, obj):
        """当站点删除当前模型时执行的钩子方法"""
        print("有人删除了模型信息[添加/修改]")

        # raise Exception("无法删除") # 阻止删除
        return super().delete_model(request, obj) # 继续删除

    def save_model(self, request, obj, form, change):
        """
        当站点保存当前模型时
        """
        print("有人修改了模型信息[添加/修改]")
        # 区分添加和修改? obj是否有id
        print(obj.id)
        return super().save_model(request, obj, form, change)

    # 显示哪些字段
    fields = ['name', 'age', 'class_num', "description"]

    # 除了设置的字段，其他都展示
    # exclude = ['age']

    # 设置只读字段
    # readonly_fields = ["name", "class_num"]   

    # 字段集,fieldsets和fields只能使用其中之一
    # fieldsets = [
    #     ["必填项",{
    #         'classes': ['collapse',],  # 折叠样式
    #         'fields': ['name', 'age', 'sex']
    #     }],
    #     ['可选项', {
    #         'classes': ['collapse',],  # 折叠样式
    #         'fields': ['class_num', 'description'],
    #     }],
    # ]


# admin.site.register(模型类, 模型管理类)
admin.site.register(Student, StudentModelAdmin)
```

#### 16.3.3 Xadmin站点全局配置

xadmin是Django的第三方扩展，是一个比Django的admin站点使用更方便的后台站点。构建于admin站点之上。

> 站点文档：http://sshwsfc.github.io/xadmin/
>
> 官方文档：https://xadmin.readthedocs.io/en/latest/index.html
>
> 默认只支持python2版本，使用python3需要配置

**安装：**

1. 安装最新版xadmin

   ```python
   pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2
   ```

2. 在配置文件settings.py中注册如下应用

   ```python
   INSTALLED_APPS = [
       ...
       # xamin主体模块
       'xadmin',
       # 渲染表格模块
       'crispy_forms',
       # 为模型通过版本控制，可以回滚数据
       'reversion',
       ...
   ]
   
   # 修改使用中文界面
   LANGUAGE_CODE = 'zh-Hans'
   
   # 修改时区
   TIME_ZONE = 'Asia/Shanghai'
   ```

3. xadmin有建立自己的数据库模型类，需要进行数据库迁移

   ```python
   python manage.py makemigrations
   python manage.py migrate
   ```

4. 在总路由中添加xadmin的路由信息

   ```python
   import xadmin
   xadmin.autodiscover()
   
   # version模块自动注册需要版本控制的 Model
   from xadmin.plugins import xversion
   xversion.register_models()
   
   urlpatterns = [
       path('xadmin/', xadmin.site.urls),
   ]
   ```

5. 创建超级用户

   ```python
   python manage.py createsuperuser
   ```

xadmin不再使用Django的admin.py进行功能配置了，而是需要编写代码在adminx.py文件中。

xadmin的配置文件需要我们在每个子应用中使用时先创建adminx.py

xadmin的站点管理类不用继承`admin.ModelAdmin`，而是直接继承`object`即可。

例如：在子应用app01中创建adminx.py文件。

**站点全局配置：**

```python
import xadmin
from xadmin import views

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "路飞学城"  # 设置站点标题
    site_footer = "路飞学城有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)
```

#### 16.3.4 Xadmin站点Model配置

xadmin可以使用的页面样式控制基本与Django原生的admin一致。

- **list_display** 控制列表展示的字段

  ```python
  list_display = ['id', 'name', 'sex', 'age']
  ```

- **search_fields** 控制可以通过搜索框搜索的字段名称，xadmin使用的是模糊查询

  ```python
  search_fields = ['id','name']
  ```

- **list_filter** 可以进行过滤操作的列，对于分类、性别、状态

  ```python
  list_filter = ['is_delete']
  ```

- **ordering** 默认排序的字段

- **readonly_fields** 在编辑页面的只读字段

- **exclude** 在编辑页面隐藏的字段

- **list_editable** 在列表页可以快速直接编辑的字段

- **show_detail_fields** 在列表页提供快速显示详情信息

- **refresh_times** 指定列表页的定时刷新

  ```python
  refresh_times = [5, 10,30,60]  # 定时刷新
  ```

- **list_export** 控制列表页导出数据的可选格式

  ```python
  list_export = ('xls', 'xml', 'json')   # list_export设置为None来禁用数据导出功能
  list_export_fields = ('id', 'title', 'pub_date') # 允许导出的字段
  ```

- **show_bookmarks** 控制是否显示书签功能

  ```python
  show_bookmarks = True
  ```

- **data_charts** 控制显示图表的样式

  ```python
  data_charts = {
          "order_amount": {
            'title': '图书发布日期表', 
            "x-field": "pub_date", 
            "y-field": ('title',),
            "order": ('id',)
          },
      #    支持生成多个不同的图表
      #    "order_amount": {
      #      'title': '图书发布日期表', 
      #      "x-field": "pub_date", 
      #      "y-field": ('title',),
      #      "order": ('id',)
      #    },
      }
  ```

  - title 控制图标名称
  - x-field 控制x轴字段
  - y-field 控制y轴字段，可以是多个值
  - order 控制默认排序

- **model_icon** 控制菜单的图标

  这里使用的图标是来自bootstrap3的图标。https://v3.bootcss.com/components/

  ```
  class BookInfoAdmin(object):
      model_icon = 'fa fa-gift'
  
  xadmin.site.register(models.BookInfo, BookInfodmin)
  ```

修改admin或者xadmin站点下的子应用成中文内容。

```python
# 在子应用的apps.py下面的配置中，新增一个属性verbose_name
from django.apps import AppConfig

class StudentsConfig(AppConfig):
    name = 'students'
    verbose_name = "学生管理"


# 然后在当前子应用的__init__.py里面新增一下代码：
default_app_config = "students.apps.StudentsConfig"
```

---

## 第十六章 工具使用

### 16.1 redis基础

Redis是业界主流的key-value nosql 数据库之一。和Memcached类似，它支持存储的value类型相对更多，包括string(字符串)、list(链表)、set(集合)、zset(sorted set --有序集合)和hash（哈希类型）。这些数据类型都支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。在此基础上，redis支持各种不同方式的排序。与memcached一样，为了保证效率，数据都是缓存在内存中。区别的是redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了master-slave(主从)同步。redis是一款基于CS架构的数据库，所以redis有客户端，也有服务端。其中，客户端可以使用python等编程语言，也可以终端命令行工具。

Redis 是一个高性能的key-value数据格式的内存缓存，NoSQL数据库(not only sql)，泛指非关系型数据库。

- 非关系型数据库：(redis，hadoop，mangoDB)
  1. 没有数据表的概念，不同的nosql数据库存放数据位置不同。
  2. nosql数据库没有通用的操作语言。
  3. 基本不支持事务。   redis支持简单事务

- 关系型数据库: (mysql, oracle, sql server, sqlite)
  1. 数据存放在表中，表之间有关系。
  2. 通用的SQL操作语言。
  3. 大部分支持事务。

**Redis特性：**

redis 是一个开源（BSD许可）的，内存中的数据结构存储系统，它可以用作数据库、缓存和消息中间件；redis是c语言编写的，支持数据持久化，是key-value类型数据库，应用在缓存、队列系统中，redis支持数据备份，也就是master-slave模式。

**Redis优势：**

- 异常快速 : Redis是非常快的，每秒可以执行大约110000设置操作，81000个/每秒的读取操作。

- 支持丰富的数据类型 : Redis支持最大多数开发人员已经知道如列表，集合，可排序集合，哈希等数据类型。

- 原子 – Redis的所有操作都是原子性的，意思就是要么成功执行，要么失败完全不执行。单个操作是原子性的。多个操作也支持事务，即原子性，通过MULTI和EXEC指令包起来。

- Redis是一个多功能实用工具，可以在很多场景使用。如：消息传递队列中使用（Redis原生支持发布/订阅）。
- 单线程特性，秒杀系统，基于redis是单线程特征，防止出现数据库“爆破”。

**Redis应用场景**

（一）性能

Redis 中缓存热点数据，能够保护数据库，提高查询效率。如下图所示，我们在碰到需要执行耗时特别久，且结果不频繁变动的SQL，就特别适合将运行结果放入缓存。这样，后面的请求就去缓存中读取，使得请求能够迅速响应。

![img](j:\homework\Python学习笔记\Python_notes.assets\20180531085918614.jpeg)

（二）并发

还是如上图所示，在大并发的情况下，所有的请求直接访问数据库，数据库会出现连接异常。这个时候，就需要使用redis做一个缓冲操作，让请求先访问到redis，而不是直接访问数据库。

#### 16.1.1  Redis安装

**Ubuntu安装：**

```shell
# 1.Ubuntu 上安装 Redis，打开终端，然后输入以下命令：
joker@joker:~$ sudo apt-get update
joker@joker:~$ sudo apt-get install redis-server

# 2.启动 Redis
$redis-server

# 3.查看 redis 是否还在运行
joker@joker:~$ redis-server

# 4.在上面的提示信息中：127.0.0.1 是本机的IP地址，6379是 Redis 服务器运行的端口。现在输入 PING 命令
joker@joker:~$ redis-cli
127.0.0.1:6379> 
127.0.0.1:6379> ping
PONG
```

**Linux安装：**

yum安装

```shell
# 1.查看是否有redis包
yum list redis

# 2.安装redis
yum install redis -y

# 3.安装好，启动redis
systemctl start redis

# 4.启动redis
redis-cli    # redis 客户端工具

# 5.进入交互式环境后，执行ping，返回pong表示安装成功
127.0.0.1:6379> ping
PONG
```

源码编译安装：

编译安装的优势是：

- 编译安装时可以指定扩展的module（模块），php、apache、nginx都是一样有很多第三方扩展模块，如mysql，编译安装时候，如果需要就定制存储引擎（innodb，还是MyIASM）
- 编译安装可以统一安装路径，linux软件约定安装目录在/opt/下面
- 软件仓库版本一般比较低，编译源码安装可以根据需求，安装最新的版本

```shell
# 1.下载redis源码
wget https://download.redis.io/releases/redis-5.0.10.tar.gz

# 2.解压缩
tar -zxvf redis-5.0.10.tar.gz

# 3.切换redis源码目录
cd redis-4.0.10

# 4.编译源文件
make 
# 5.编译好后，bin/目录下有编译好的redis指令
# 6.make install 安装到指定目录，默认在/usr/local/bin
make install

# 7.在/usr/local/目录下创建redis目录，cp文件
[root@localhost local]# pwd
/usr/local
[root@localhost local]# mkdir redis
[root@localhost local]# cp /usr/local/redis-server /usr/local/redis/
[root@localhost local]# cp /usr/local/redis-cli /usr/local/redis/

# 8.修改redis.conf 文件，将daemonize no 改为daemonize yes  放在后台运行
# 9.杀死redis进程
[root@localhost local]# pkill -9 redis

# 10.指定配置文件启动
[root@localhost redis]# redis-server redis.conf
4429:C 29 Oct 2021 20:07:49.168 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
4429:C 29 Oct 2021 20:07:49.168 # Redis version=5.0.10, bits=64, commit=00000000, modified=0, pid=4429, just started
4429:C 29 Oct 2021 20:07:49.168 # Configuration loaded

# 11.查看redis进程
[root@localhost redis]# ps -ef | grep redis

# 12.测试是否连接成功
[root@localhost redis]# redis-cli
127.0.0.1:6379> ping
PONG


# .文件解释
./redis-benchmark   # 用于进行redis性能测试的工具
./redis-check-dump  # 用于修复出问题的dump.rdb文件
./redis-cli 		# redis的客户端
./redis-server 		# redis的服务端
./redis-check-aof 	# 用于修复出问题的AOF文件
./redis-sentinel 	# 用于集群管理
```

#### 16.1.2 Redis数据类型

**1.操作模式**

redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py。

```shell
import redis

r = redis.Redis(host="192.168.243.1", port=6379)
r.set("name", "joker")
print(r.get("name"))  # b'joker'
```

**2.连接池**

redis-py使用connection_pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。

```shell
poll = redis.ConnectionPool(host="192.168.243.1", port=6379)
r = redis.Redis(connection_pool=poll)

r.set("foo", "Bar")
print(r.get("foo"))
```

**3.数据类型**

- string类型：字符串类型是 Redis 中最为基础的数据存储类型，它在 Redis 中是二进制安全的，也就是byte类型。
- hash类型： hash用于存储对象，对象的结构为属性、值，值的类型为string。key:{域:值[这里的值只能是字符串]}。
- list类型：列表的元素类型为string。key:[ 值1,值2,值3..... ]。
- set类型：无序集合，元素为string类型，元素唯一不重复，没有修改操作。{值1,值4,值3,值5}。
- zset类型：有序集合，元素为string类型，元素唯一不重复，没有修改操作。

##### 16.1.2.1 string类型

redis中的String在内存中按照一个name对应一个value来存储。

**使用场景：**

> 最常规的set/get操作，value可以是String也可以是数字。一般做一些复杂的计数功能的缓存，比如减少库存。

- set(name, value, ex=None, px=None, nx=False, xx=False)

  在Redis中设置值，默认，不存在则创建，存在则修改

  参数：

  ​	ex，过期时间（秒）

  ​	px，过期时间（毫秒）

  ​	nx，如果设置为True，则只有name不存在时，当前set操作才执行

  ​	xx，如果设置为True，则只有name存在时，当前set操作才执行

```python
# 新建
r.set("foo", "Bar")
print(r.get("foo"))

# ex:设置过期单位秒，超过3秒，取出None
r.set("foo", "Bar", ex=5)
print(r.get("foo"))

# px:设置过期单位毫秒，超过3秒，取出None
r.set("foo", "Bar", px=3000)
print(r.get("foo"))

# nx:如果设置为True，则只有name不存在时，当前set操作才执行 （新建）,存在则不新建
r.set("foo", "Bar", nx=True)
print(r.get("foo"))

# xx:如果设置为True，则只有name存在时，当前set操作才执行 （修改）
print(r.set("k5", "22", xx=True))
```

- setnx(name, value)  

```python
# 设置值，只有name不存在时，执行设置操作（添加）
r.setnx("foo1", "a1")  # redis中不存在foo1，才会执行添加
print(r.get("foo1"))
```

- setex(name, value, time)

```python
# 设置值
# 参数：time，过期时间（数字秒 或 timedelta对象）
r.setex("a1", "b1", 5)  # 5秒过期
print(r.get("a1"))  # 过了5秒后打印 None
```

- psetex(name, time_ms, value)

```shell
# 设置值
# 参数：time_ms，过期时间（数字毫秒 或 timedelta对象）
r.psetex("a1", 5000, "b1")
print(r.get("a1"))  # 过了5秒后打印 None
```

- mset(*args, **kwargs)

```python
# 批量设置值
r.mset({"k3":"v3", "k4":"v4"})  
或  
r.mset(k1="v1", k2="v2")
print(r.get("a3"))  # 取一个值
print(r.mget("k3", "k4"))  # 批量取值
```

- mget(*args, **kwargs)

```python
# 批量获取值
print(r.mget("k1", "k2", "k3"))
```

- getset(name, value)

```shell
# 获取原来的值并设置新值
print(r.getset("k4", "v44"))  # 设置的新值是v44，原来的值是v4
```

- getrange(key, start, end)

```python
# 获取子序列（根据字节获取，非字符）
# 参数：
    # name，Redis 的 name
    # start，起始位置（字节）
    # end，结束位置（字节）
    
r.set("for_name", "詹姆斯")
print(r.getrange("for_name", 0,2)) # 取前3个字节，一个汉字3个字节，取出的是詹
print(r.getrange("for_name", 0,-1)) # 取所有的

r.set("address", "abcde")
print(r.getrange("address", 0, 2))  # abc
print(r.getrange("address", 0, -1))  # abcde
```

- setrange(name, offset, value)

```python
# 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
# 参数：
    # offset，字符串的索引，字节（一个汉字三个字节）
    # value，要设置的值
    
r.setrange("address", 2, "jiatingzhuzhi")  # 从第二个位置开始替换
print(r.get("address"))  # b'abjiatingzhuzhi'
```

- strlen(name)

```python
# 返回name对应值的字节长度（一个汉字3个字节）
print(r.strlen("address"))  # 15
```

- incr(self, name, amount=1)

```python
# 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。
# 参数：
    # name,Redis的name
    # amount,自增数（必须是整数
    
r.set("k5", 1)
print(r.mget("k1", "k2", "k3", "k4", "k5"))  # [b'v1', b'v2', b'v3', b'v44', b'1']
r.incr("k5", amount=2)
print(r.mget("k1", "k2", "k3", "k4", "k5"))  # [b'v1', b'v2', b'v3', b'v44', b'3']
```

应用场景【点赞数】
例如抖音的每个视频都需要统计点赞数，而点赞次数比评论次数的多得多。如果使用关系数据库来存储点击，可能存在大量的行级锁争用。所以，点赞数的增加使用redis的INCR命令最好不过了。当redis服务器启动时，可以从关系数据库读入点击数的初始值。

- incrbu(self, name)

```python
# 与incr用法类似，区别：name对应的值，没有自增，需要自己指定一个值
```

- incrbyfloat(self, name, amount=1.0)

```python
# 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。
# 参数：
    # name,Redis的name
    # amount,自增数（浮点型）

r.set("k5", 1)
print(r.mget("k1", "k2", "k3", "k4", "k5"))  # [b'v1', b'v2', b'v3', b'v44', b'1']
r.incrbyfloat("k5", amount=1.1)
print(r.mget("k1", "k2", "k3", "k4", "k5"))  # [b'v1', b'v2', b'v3', b'v44', b'2.10000000000000009']
```

- decr(self, name, amount=1)

```python
# 自减 name对应的值，当name不存在时，则创建name＝amount，否则，则自减。
# 参数：
    # name,Redis的name
    # amount,自减数（整数）
r.set("k5", 10)
print(r.get("k5"))  # b'10'
r.decr("k5", amount=1)
print(r.get("k5"))  # b'9'
```

- append(key, value)

```python
# 在redis name对应的值后面追加内容
# 参数：
    # key, redis的name
    # value, 要追加的字符串
r.append("k5", 13)
print(r.get("k5"))  # b'913'
```

##### 16.1.2.2 hash类型

hash表现形式上有些像pyhton中的dict，可以存储一组关联性较强的数据 ， redis中Hash在内存中的存储格式。

使用场景：

> 这里value存放的是结构化的对象，比较方便的就是操作其中的某个字段。博主在做单点登录的时候，就是用这种数据结构存储用户信息，以cookieId作为key，设置30分钟为缓存过期时间，能很好的模拟出类似session的效果。

- hset(name, key, value)  **单个增加--修改(单个取出)--没有就新增，有的话就修改**

```python
# name对应的hash中设置一个键值对（不存在，则创建；否则，修改）
# 参数：
    # name，redis的name
    # key，name对应的hash中的key
    # value，name对应的hash中的value
    
r.hset("h1", "k1", "v2")
r.hset("h1", "k2", "v2")
print(r.hkeys("h1"))  # 取hash中所有的key
print(r.hget("h1", "k1"))  # 取单个key对应的值
print(r.hmget("h1", "k1", "k2"))  # 取多个key对应的值

r.hsetnx("h1", "k2", "v2")  # 如果hash中已经存在key，无法修改
print(r.hget("h2", "k2"))
```

- hmset(name, mapping)  **批量增加（取出）**

```python
# 在name对应的hash中批量设置键值对
# 参数：
	# name，redis的name
	# mapping，字典，如：{'k1':'v1', 'k2': 'v2'}
    
r.hmset("h3", {"k3":"v3", "k4":"v4"})
print(r.hkeys("h3"))
```

- hget(name,key)  **获取单个key的value**

```python
# 在name对应的hash中获取根据key获取value
print(r.hget("h1", "k1")) # 取出h1中的k1对应的值
```

- hmget(name, keys, *args)  **获取多个key的value**

```python
# 在name对应的hash中获取多个key的值
# 参数：
    # name，reids对应的name
    # keys，要获取key集合，如：['k1', 'k2', 'k3']
    # *args，要获取的key，如：k1,k2,k3
    
print(r.hmget("h1", "k1", "k2"))  # 取出h1中k2,k3对应的值
print(r.hmget("h1", ["k1", "k2"]))  # 取出h1中k2，k3对应的值
```

- hgetall(name)  **取出所有的键值对**

```python
# 获取name对应hash的所有键值
print(r.hgetall("h1"))
```

- hlen(name)　**得到所有键值对的格式 hash长度**

```python
# 获取name对应的hash中键值对的个数
print(r.hlen("h1"))
```

- hkeys(name)  **得到所有的keys（类似字典的取所有keys）**

```python
# 获取name对应的hash中所有的key的值
print(r.hkeys("h1"))
```

- hvals(name)  **得到所有的value（类似字典的取所有value）**

```python
# 获取name对应的hash中所有的value的值
print(r.hvals("h1"))
```

- hexists(name, key)  **判断成员是否存在（类似字典的in）**

```python
# 检查name对应的hash是否存在当前传入的key
print(r.hexists("h1", "k1"))
```

- hdel(name,*keys)  **删除键值对**

```python
# name对应的hash中指定key的键值对删除
print(r.hgetall("h1"))  # {b'k1': b'v2', b'k2': b'v2'}
r.hdel("h1", "k1")
print(r.hgetall("h1"))  # {b'k2': b'v2'}
```

- hincrby(name, key, amount=1)  **自增自减整数(将key对应的value--整数 自增1或者2，或者别的整数 负数就是自减)**

```python
# 自增name对应的hash中的指定key的值，不存在则创建key=amount
# 参数：
    # name，redis中的name
    # key， hash对应的key
    # amount，自增数（整数）

print(r.hgetall("h4"))  # {b'k1': b'124'}
r.hincrby("h4", "k1", amount=1)
print(r.hgetall("h4"))  # {b'k1': b'125'}

r.hincrby("h4", "k2", amount=2)
print(r.hgetall("h4"))  # {b'k1': b'126', b'k2': b'2'}  # 不存在的key，key的值就时amount
```

- hincrbyfloat(name, key, amount=1.0)  **自增自减浮点数(将key对应的value--浮点数 自增1.0或者2.0，或者别的浮点数 负数就是自减)**

```python
# 自增name对应的hash中的指定key的值，不存在则创建key=amount
  
# 参数：
    # name，redis中的name
    # key， hash对应的key
    # amount，自增数（浮点数）
# 自增name对应的hash中的指定key的值，不存在则创建key=amount

r.hset("h5", "k5", "1.0")
r.hincrbyfloat("h5", "k5", amount=-1.0)    # 已经存在，递减-1.0
print(r.hgetall("h5"))
r.hincrbyfloat("h5", "k6", amount=-1.0)    # 不存在，value初始值是-1.0 每次递减1.0
print(r.hgetall("h5"))
```

- hscan_iter(name, match=None, count=None)  

```python
# 利用yield封装hscan创建生成器，实现分批去redis中获取数据
   
# 参数：
    # match，匹配指定key，默认None 表示所有的key
    # count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数
   
for item in r.hgetall("h4"):
    print(item)

print(r.hscan_iter("h4"))  # 生成迭代器地址
```

- hscan(name, cursor=0, match=None, count=None)  **取值查看--分片读取**

```python
# 增量式迭代获取，对于数据大的数据非常有用，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而放置内存被撑爆
# 参数：
    # name，redis的name
    # cursor，游标（基于游标分批取获取数据）
    # match，匹配指定key，默认None 表示所有的key
    # count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数
如：
第一次：cursor1, data1 = r.hscan('xx', cursor=0, match=None, count=None)
第二次：cursor2, data1 = r.hscan('xx', cursor=cursor1, match=None, count=None)
...

print(r.hscan("h1"))
```

##### 16.1.2.3 list类型

List操作，redis中的List在在内存中按照一个name对应一个List来存储。

**使用场景：**

> 使用List的数据结构，可以做简单的消息队列的功能。另外还有一个就是，可以利用lrange命令，做基于redis的分页功能，性能极佳，用户体验好。本人还用一个场景，很合适---取行情信息。就也是个生产者和消费者的场景。LIST可以很好的完成排队，先进先出的原则。

- lpush(name,values)  **增加（类似于list的append，只是这里是从左边新增加）--没有就新建**

```python
# 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
r.lpush("list1", 11,22,33)
print(r.lrange("list1", 0, -1))  # [b'33', b'22', b'11']
# 保存顺序为: 33,22,11
```

扩展：

```python
r.rpush("list2", 22, 33, 44)  # 从右向左操作
print(r.lrange("list2", 0, -1))  # 切片取值
print(r.llen("list2"))  # 查看列表的长度
```

- lpushx(name,value)  **往已经有的name的列表的左边添加元素，没有的话无法创建**

```python
# 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边
r.lpushx("list3", 10)  # list3 不存在
print(r.llen("list3"))  # 0
print(r.lrange("list3", 0, -1))  # []
```

- rpushx(name,value)  **往已经有的name的列表的右边添加元素，没有的话无法创建**

```python
# 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最右边
r.rpushx("list4", 10)
print(r.llen("list4"))
print(r.lrange("list4", 0, -1))
```

- llen(name)  **查看元素的个数**

```python
# name对应的list元素的个数
print(r.llen("list4"))
```

- linsert(name, where, refvalue, value))  **新增（固定索引号位置插入元素）**

```python
# 在name对应的列表的某一个值前或后插入一个新值
# 参数：
    # name，redis的name
    # where，BEFORE或AFTER
    # refvalue，标杆值，即：在它前后插入数据
    # value，要插入的数据
    
r.linsert("list3", 'BEFORE', 10, 11)  # 在列表中第一个出现10的前面插入11
print(r.lrange("list3", 0,-1))  # 通过索引查看所有的值
```

- lset(name, index, value)  **修改（指定索引号进行修改）**

```python
# 对name对应的list中的某一个索引位置重新赋值
# 参数：
    # name，redis的name
    # index，list的索引位置
    # value，要设置的值
    
r.lset("list3", 0, 12)  # 把索引为0的元素改为11
print(r.lrange("list3", 0, -1))
```

- lrem(name, value, num)　**删除（指定值进行删除）**

```python
# 在name对应的list中删除指定的值
# 参数：
    # name，redis的name
    # value，要删除的值
    # num，  num=0，删除列表中所有的指定值；
           # num=2,从前到后，删除2个；
           # num=-2,从后向前，删除2个

r.lrem("list2", 33, 1)  # 将列表中左边第一次出现33的元素删除
print(r.lrange("list2", 0, -1))
r.lrem("list2", 22, -1)  # 将列表中右边第一次出现22的元素删除
print(r.lrange("list2", 0, -1))
r.lrem("list2", 44, 0)  # 将列表中所有44删除
print(r.lrange("list2", 0, -1))
```

- lpop(name)  **删除并返回**

```python
# 在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
  
# 更多：
    # rpop(name) 表示从右向左操作

print(r.lpop("list2"))  # 删除列表最左边的元素，并返回
print(r.rpop("list2"))  # 删除列表最右边的元素，并返回
```

- lindex(name, index)  **取值（根据索引号取值）**

```python
# 在name对应的列表中根据索引获取列表元素
print(r.lindex("list2", 0))
```

- lrange(name, start, end)  **切换获取**

```python
# 在name对应的列表分片获取数据
# 参数：
    # name，redis的name
    # start，索引的起始位置
    # end，索引结束位置
    
print(r.lrange("list2", 0, -1))
```

- ltrim(name, start, end)  **删除索引之外的值**

```python
# 在name对应的列表中移除没有在start-end索引之间的值
# 参数：
    # name，redis的name
    # start，索引的起始位置
    # end，索引结束位置
r.ltrim("list2", 0, 2)  # 删除索引0-2之外的元素
print(r.lrange("list2", 0, -1))
```

- brpoplpush(src, dst, timeout=0)  **移动 元素从一个列表移动到另外一个列表 可以设置超时**

```python
# 从一个列表的右侧移除一个元素并将其添加到另一个列表的左侧
# 参数：
    # src，取出并要移除元素的列表对应的name
    # dst，要插入元素的列表对应的name
    # timeout，当src对应的列表中没有数据时，阻塞等待其有数据的超时时间（秒），0 表示永远阻塞

r.brpoplpush("list2", "list1", timeout=2)
print(r.lrange("list1", 0, -1))
```

- rpoplpush(src, dst)  **移动 元素从一个列表移动到另外一个列表**

```python
# 从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
# 参数：
    # src，要取数据的列表的name
    # dst，要添加数据的列表的name
r.rpoplpush("list2", "list1")
print(r.lrange("list2", 0, -1))
```

- blpop(keys, timeout)  **一次移除多个列表**

```python
# 将多个列表排列，按照从左到右去pop对应列表的元素
    # 参数：
    # keys，redis的name的集合
    # timeout，超时时间，当元素所有列表的元素获取完之后，阻塞等待列表内有数据的时间（秒）, 0 表示永远阻塞
# 更多：r.brpop(keys, timeout) 同blpop，将多个列表排列,按照从右像左去移除各个列表内的元素
    
while True:
    r.blpop(["list1", "list2"], timeout=2)
    print(r.lrange("list1", 0, -1), r.lrange("list2", 0, -1))
```

- 自定义增量迭代

```python
# 由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要：
	# 获取name对应的所有列表
    # 循环列表
# 如果表非常大，那么就有可能在第一步时就将程序的内容撑爆，所有有必要自定义一个增量迭代的功能：

def list_iter(name):
    list_count = r.llen(name)
    for index in range(list_count):
        yield r.lindex(name, index)

# 循环遍历list2
for itme in list_iter("list2"):
    print(itme)
```

##### 16.1.2.4 set类型

Set操作，Set集合就是不允许重复的列表

**使用场景：**

> 因为set堆放的是一堆不重复值的集合。所以可以做全局去重的功能。
>
> 另外，就是利用交集、并集、差集等操作，可以计算共同喜好，全部的喜好，自己独有的喜好等功能。

- sadd(name,values)  **新增**

```python
# name对应的集合中添加元素
r.sadd("set1", 11, 22, 33, 44)
print(r.scard("set1"))  # 获取集合的长度
print(r.smembers("set1"))  # 获取集合中所有的成员
```

- scard(name)  **获取元素个数 类似于len**

```python
# 获取name对应的集合中元素个数, 类似于 len
print(r.scard("set1"))
```

- sdiff(keys, *args)   **差集**

```python
# 在第一个name对应的集合中且不在其他name对应的集合的元素集合
r.sadd("set2", 11,22)
print(r.smembers("set2"))
print(r.smembers("set1"))
print(r.sdiff("set2", "set1"))  # 打印set2中存在，set1中不存在的元素
```

- sdiffstore(dest, keys, *args)   **差集--差集存在一个新的集合中**

```python
# 获取第一个name对应的集合中且不在其他name对应的集合，再将其新加入到dest对应的集合中
r.sdiffstore("set3", "set2", "set1")  # 在set2集合中，但不在set1集合中，差集添加到set3集合中
print(r.smembers("set3"))
```

- sinter(keys, *args)  **交集**

```python
# 获取多一个name对应集合的交集
print(r.sinter("set1", "set2"))  # 取两个集合的交集
```

- sinterstore(dest, keys, *args)   **交集--交集存在一个新的集合中**

```python
# 获取多一个name对应集合的并集，再将其加入到dest对应的集合中
r.sinterstore("set4", "set1", "set2")  # set1和set2的交集，添加到set4集合中
print(r.smembers("set4"))
```

- sunion(keys, *args)  **并集**

```python
# 获取多个name对应的集合的并集
print(r.sunion("set1", "set2"))  # 获取两个集合的并集
```

- sunionstore(dest,keys, *args)  **并集--并集存在一个新的集合**

```python
# 获取多一个name对应的集合的并集，并将结果保存到dest对应的集合中
print(r.sunionstore("set3", "set1", "set2")) # 取2个集合的并集,添加到set3
print(r.smembers("set3"))
```

- sismember(name, value)  **判断是否是集合的成员 类似in**

```python
# 检查value是否是name对应的集合的成员
print(r.sismember("set1", 33))
```

- smembers(name)  **获取集合中所有的成员**

```python
# 获取name对应的集合的所有成员
print(r.smembers("set1"))  # 获取集合中所有的成员
```

- sscan(name, cursor=0, match=None, count=None)  **获取集合中所有的成员--元组形式**

```python
# 获取集合中所有的成员--元组形式
print(r.sscan("set1"))

for item in r.sscan("set1"):
    print(item)
```

- smove(src, dst, value)  **移动**

```python
# 将某个成员从一个集合中移动到另外一个集合
r.smove("set2", "set1", 88)  # 将set2中的88元素移动到set1中
print(r.smembers("set1"))
print(r.smembers("set2"))
```

- spop(name)  **删除--随机删除并且返回被删除值**

```python
# 从集合中随机移除一个成员，并将其返回,说明一下，集合是无序的，所有是随机删除的
r.spop("set2")  # 这个删除的值是随机删除的，集合是无序的
print(r.smembers("set2"))
```

- srandmember(name, numbers)

```python
# 从name对应的集合中随机获取 numbers 个元素
print(r.srandmember("set2", 3))
```

- srem(name, values)

```python
# 在name对应的集合中删除某些值
print(r.srem("set2", 11))   # 从集合中删除指定值 11
print(r.smembers("set2"))
```

- sscan_iter(name, match=None, count=None)  获取集合中所有的成员--迭代器的方式

```python
# 同字符串的操作，用于增量迭代分批获取元素，避免内存消耗太大
for i in r.sscan_iter("set1"):
    print(i)
```

##### 16.1.2.5 Sort set 类型

有序集合，在集合的基础上，为每个元素排序；元素的排序需要根据另外一个值来进行比较，所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。

**使用场景：**

> sorted set多了一个权重参数score,集合中的元素能够按score进行排列。可以做排行榜应用，取TOP N操作。

- zadd(name, *args, **kwargs)   新增

```python
# 在name对应的有序集合中添加元素
# 如：print(r.zadd("zz",{"n1":1,"n2":2,"n3":3,"n4":4}))<br><br># 查看：print(r.zscan("zz"))
r.zadd("zset1", n1=1, n2=2)
r.zadd("zset2", "m1", 11, "m2", 22)
print(r.zcard("zset1"))  # 集合长度
print(r.zcard("zset2"))  # 集合长度
print(r.zrange("zset1", 0, -1))  # 获取有序集合中所有的元素
print(r.zrange("zset2", 0, -1, withscores=True))  # 获取有序集合中所有的元素和分数
```

- zcard(name)  **获取有序集合元素个数 类似于len**

```python
# 获取name对应的有序集合元素的数量
print(r.zcard("zset1"))  # 集合长度
```

- r.zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)   **获取有序集合的所有元素**

```python
# 按照索引范围获取name对应的有序集合的元素
# 参数：
    # name，redis的name
    # start，有序集合索引起始位置（非分数）
    # end，有序集合索引结束位置（非分数）
    # desc，排序规则，默认按照分数从小到大排序
    # withscores，是否获取元素的分数，默认只获取元素的值
    # score_cast_func，对分数进行数据转换的函数
print(r.zrange("zset1", 0, -1))  # 获取有序集合中所有的元素
print(r.zrange("zset2", 0, -1, withscores=True))  # 获取有序集合中所有的元素和分数
```

- zrevrange(name, start, end, withscores=False, score_cast_func=float)  **从大到小排序(同zrange，集合是从大到小排序的)**

```python
print(r.zrevrange("zset1", 0, -1))  # 只获取元素，不显示分数
print(r.zrevrange("zset1", 0, -1, withscores=True))  # 获取有序集合中所有元素和分数,分数倒序
```

- zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)  **按照分数范围获取name对应的有序集合的元素**

```python
for i in range(1, 20):
    element = "n" + str(i)
    r.zadd("zset3", element, i)
print(r.zrangebyscore("zset3", 10, 15))  # 取10-15之间的元素，不显示分数
print(r.zrangebyscore("zset3", 5, 20, withscores=True))  # 取5-20之间的元素和分数
```

- zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)  **按照分数范围获取有序集合的元素并排序（默认从大到小排序）**

```python
print(r.zrevrangebyscore("zset3", 15, 10, withscores=True))  # 在分数15-10之间，取出符合条件的元素，安装分数倒叙进行排序
```

- zscan(name, cursor=0, match=None, count=None, score_cast_func=float)  **获取所有元素--默认按照分数顺序正序排序**

```python
print(r.zscan("zset3"))
```

- zscan_iter **获取所有元素--迭代器**

```python
for i in r.zscan_iter("zset3"):
    print(i)
```

- zcount(name, min, max)  **获取name对应的有序集合中分数 在 [min,max] 之间的个数**

```python
# 获取name对应的有序集合中分数 在 [min,max] 之间的个数
print(r.zrange("zset3", 0, -1, withscores=True))
print(r.zcount("zset3", 5, 20))
```

- zincrby(name, value, amount)  **自增**

```python
# 自增name对应的有序集合的 name 对应的分数
r.zincrby("zset3", "n2", amount=2)  # 每次将n2的分数自增2
print(r.zrange("zset3", 0, -1, withscores=True))
```

- zscore(name, value)   **获取值对应的分数**

```python
# 获取name对应有序集合中 value 对应的分数
print(r.zscore("zset3", "n18"))  # 获取元素n18对应的分数
```

- zrank(name, value)  **获取值的索引号**

```python
# 获取某个值在 name对应的有序集合中的排行（从 0 开始）
# 更多：zrevrank(name, value)，从大到小排序
print(r.zrank("zset3", "n1"))  # n1的索引是0，按照分数顺序   从小到达找
print(r.zrank("zset3", "n6"))
print(r.zrevrank("zset3", "n1"))  # 按照分数顺序   从大到小找
```

- zrem(name, values)  **删除--指定值删除**

```python
# 删除name对应的有序集合中值是values的成员
# 如：zrem('zz', ['s1', 's2'])
r.zrem("zset3", "n3")
print(r.zrange("zset3", 0, -1))
```

- zremrangebyrank(name, min, max)  **删除--根据排行范围删除，按照索引号来删除**

```python
# 根据排行范围删除
r.zremrangebyrank("zset3", 0, 2)  # 删除索引是0-2的元素
print(r.zrange("zset3", 0, -1))
```

- zremrangebyscore(name, min, max)

```python
# 根据分数范围删除
r.zremrangebyscore("zset3", 11, 12)  # 删除有序集合中的分数是11，12的元素
print(r.zrange("zset3", 0, -1))
```

- zinterstore(dest, keys, aggregate=None)

```python
# 获取两个有序集合的交集，如果遇到相同值不同分数，则按照aggregate进行操作
# aggregate的值为:  SUM  MIN  MAX

print(r.zrange("zset1", 0, -1, withscores=True))
print(r.zrange("zset3", 0, -1, withscores=True))
# 获取两个有序集合的交集并放入dest集合，如果遇到相同值不同分数，则按照aggregate进行操作
# aggregate的值为: SUM  MIN  MAX
print(r.zinterstore("zq", ("zset1", "zset3"), aggregate="MIN"))
print(r.zscan("zq"))
```

- zunionstore(dest, keys, aggregate=None)

```python
# 获取两个有序集合的并集，如果遇到相同值不同分数，则按照aggregate进行操作
# aggregate的值为:  SUM  MIN  MAX
r.zadd("zset1", "mm5", 55, "mm6", 66)
print(r.zrange("zset1", 0, -1, withscores=True))
print(r.zrange("zset3", 0, -1, withscores=True))
print(r.zunionstore("zq1", ("zset1", "zset3"), aggregate="MIN"))
print(r.zscan("zq1"))
```

##### 16.1.2.6 其他常用操作

- type(name)  **获取类型**

```python
# 查看数据类型
r.type("h1")  # b'hash'
```

- flushall()  **清空整个redis服务器数据**

```python
# 清空整个 Redis 服务器的数据(删除所有数据库的所有 key )
r.flushall()
```

- flushdb()  **清空当前数据库中的所有redis**

```python
# 清空当前数据库中的所有 key
r.flushdb()
```

- dbsize()  **返回挡墙数据库的key的数量**

```python
# 返回当前数据库的 key 的数量
print(r.dbsize())
```

- delete(*names)  **删除**

```python
# 根据删除redis中的任意数据类型（string、hash、list、set、有序set）
r.delete("zset2")  # 删除key为zset2的数据
```

- exists(name)  **检查名字是否存在**

```python
# 检测redis的name是否存在，存在就是True，False 不存在
print(r.exists("zset3"
```

- keys(pattern='')  **模糊匹配**

```python
# 根据模型获取redis的name
# 更多：
    # KEYS * 匹配数据库中所有 key 。
    # KEYS h?llo 匹配 hello ， hallo 和 hxllo 等。
    # KEYS hllo 匹配 hllo 和 heeeeello 等。
    # KEYS h[ae]llo 匹配 hello 和 hallo ，但不匹配 hillo
print(r.keys("z*"))
```

- expire(name ,time)   **设置超时时间**

```python
# 为某个redis的某个name设置超时时间
r.lpush("list5", 11, 22)
r.expire("list5", time=3)
print(r.lrange("list5", 0, -1))
```

-  rename(src, dst)  **重命名**

```python
# 对redis的name重命名
print(r.zrange("zset1", 0, -1))
print(r.rename("zset1", "zzset1"))
print(r.zrange("zzset1", 0, -1))
```

- randomkey()  **随机获取name**

```python
# 随机获取一个redis的name（不删除）
print(r.randomkey())
```

- scan(cursor=0, match=None, count=None)  **查看所有元素**

```python
print(r.hscan("hash2"))  # hash类型查看
print(r.sscan("set3"))  # set类型查看
print(r.zscan("zset2"))  # 有序set类型查看
print(r.getrange("foo1", 0, -1))  # 字符串类型查看
print(r.lrange("list2", 0, -1))  # list类型查看
print(r.smembers("set3"))  # set类型查看
print(r.zrange("zset3", 0, -1))  # 有序set类型查看
print(r.hgetall("hash1"))  # hash类型查看
```

- scan_iter(match=None, count=None)  **查看所有元素--迭代器**

```python
for i in r.hscan_iter("hash1"):
    print(i)

for i in r.sscan_iter("set3"):
    print(i)

for i in r.zscan_iter("zset3"):
    print(i)

```

- **other方法**

```python
print(r.get('name'))    # 查询key为name的值
r.delete("gender")  # 删除key为gender的键值对
print(r.keys()) # 查询所有的Key
print(r.dbsize())   # 当前redis包含多少条数据
r.save()    # 执行"检查点"操作，将数据写回磁盘。保存时阻塞
# r.flushdb()        # 清空r中的所有数据
```

#### 16.1.3 管道（pipline）

redis默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。

管道（pipeline）是redis在提供单个请求中缓冲多条服务器命令的基类的子类。它通过减少服务器-客户端之间反复的TCP数据库包，从而大大提高了执行批量命令的功能。

如果一个失败，则都不会创建。

```python
import redis

poll = redis.ConnectionPool(host="192.168.243.1", port=6379)
r = redis.Redis(connection_pool=poll)

pipe = r.pipeline()
pipe.set("name", "jack")
pipe.set("sex", "1")
pipe.set("from", "china")
pipe.incr('num')  # 如果num不存在则vaule为1，如果存在，则value自增1
pipe.execute()

print(r.get("name"))
print(r.get("sex"))
print(r.get("from"))
```

#### 16.1.4 发布订阅

订阅者：

```python
import redis
 
r=redis.Redis(host='127.0.0.1')
pub=r.pubsub()
 
pub.subscribe("fm104.5")
pub.parse_response()
 
while 1:
    msg = pub.parse_response()
    print(msg)
```

发布者：

```python
import redis
 
r=redis.Redis(host='127.0.0.1')
r.publish("fm104.5", "Hi,yuan!")
```

发布订阅的特性用来做一个简单的实时聊天系统再适合不过了，当然这样的东西开发中很少涉及到。再比如在分布式架构中，常常会遇到读写分离的场景，在写入的过程中，就可以使用redis发布订阅，使得写入值及时发布到各个读的程序中，就保证数据的完整一致性。再比如，在一个博客网站中，有100个粉丝订阅了你，当你发布新文章，就可以推送消息给粉丝们拉。

---

### 16.2 RabbitMQ

**什么是消息队列**

MQ全称为Message Queue 消息队列（MQ）是一种应用程序对应用程序的通信方法。MQ是消费-生产者模型的一个典型的代表，一端往消息队列中不断写入消息，而另一端则可以读取队列中的消息。这样发布者和使用者都不用知道对方的存在。

> ```shell
> 生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。
> ```

队列是一种先进先出的数据结构。

消息队列可以简单理解为：把要传输的数据放在队列中。

消息队列中间件是分布式系统中重要的组件，主要解决应用**解耦，异步消息，流量削锋**等问题，实现高性能，高可用，可伸缩和最终一致性架构。目前使用较多的消息队列有ActiveMQ，RabbitMQ，ZeroMQ，Kafka，MetaMQ，RocketMQ。

接下来利用一个外卖系统的消息推送给大家解释下MQ的意义。

![1639297222548](J:\homework\Python学习笔记\Python_notes.assets\1639297222548.png)

**RabbitMQ**

中文文档：https://www.rabbitmq.com/tutorials/tutorial-one-python.html

RabbitMQ 是一个由 Erlang 语言开发的 AMQP 的开源实现。

rabbitMQ是一款基于AMQP协议的消息中间件，它能够在应用之间提供可靠的消息传输。在易用性，扩展性，高可用性上表现优秀。使用消息中间件利于应用之间的解耦，生产者（客户端）无需知道消费者（服务端）的存在。而且两端可以使用不同的语言编写，大大提供了灵活性。

#### 16.2.1 rabbit安装

**windows**

> 查看博客安装流程：https://www.cnblogs.com/saryli/p/9729591.html
>
> 账号密码默认：guest

**linux**

> 查看博客安装流程：https://www.cnblogs.com/jimlau/p/12029985.html

开启服务：F:\Program Files\RabbitMQ Server\rabbitmq_server-3.7.4\sbin>rabbitmq-server.bat

#### 16.2.2 工作模型

```shell
# 安装pika模块
pip3 install -i https://pypi.douban.com/simple  pika
```

##### 16.2.2.1 简单模式

生产者

```python
import pika
from pika.spec import Exchange

# 1.链接rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

# 2.创建队列
channel.queue_declare(queue="hello")

# 3.向指定队列插入数据
channel.basic_publish(exchange='',
                      routing_key="hello",
                      body="hello rabbitmq2")

print("[x] sent 'hello rabbitmq' ")
```

消费者

```python
import pika
# 1.链接rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# 2.创建队列
channel.queue_declare(queue="hello")


# 3.确定回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 4.确定监听队列参数
channel.basic_consume(queue="hello",
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 5.正式监听
channel.start_consuming()
```

简单模式：没有任何异常的清空下，客户端写入，生产者写入数据，消费者同步收到数据。

##### 16.2.2.2 应答参数

no-ack ＝ False，如果消费者监听时，调回调函数时(代码出错)(its channel is closed, connection is closed, or TCP connection is lost)挂掉了，那么，RabbitMQ会重新将该任务添加到队列中。

- 回调函数中的 `ch.basic_ack(delivery_tag=method.delivery_tag)`
- basic_comsume中的 `no_ack=False`

生产者

```python
import pika

# 1.连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 2.创建队列
channel.queue_declare(queue="hello1")

# 3.向指定队列插入数据
channel.basic_publish(exchange="", routing_key="hello1", body="hello body11")

print(" [x] Sent 'Hello body!'")
```

消费者

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 1.创建队列
channel.queue_declare(queue="hello1")

# 2.确定回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # channel.close()
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
# no_ack=Fales:表示消费完以后不主动把状态通知rabbitmq

# 3.确定监听队列参数
channel.basic_consume(
    queue='hello1',
    auto_ack=False,  # 默认应答改为手动应答
    on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 正式监听
channel.start_consuming()
```

##### 16.2.2.3 持久化参数

消息生产者端发送消息时rabbitMQ服务挂掉了，消费者接消息时挂掉了，以下方法会让RabbitMQ重新将该消息添加到队列中：

- 回调函数中的 `ch.basic_ack(delivery_tag=method.delivery_tag)`， **消费端需要做的**
- 生产者和消费者添加 `durable=True`  **生产者消费端需要做的**
- 发布消息端的basic_publish添加参数 `properties=pika.BasicProperties(delivery_mode=2)`， **生产者端需要做的**

生产者

```python
import pika

# 1.连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 2.创建可持久化队列
channel.queue_declare(queue="hello4", durable=True)

# 3.向指定队列插入数据
channel.basic_publish(
    exchange="",  # 简单模式
    routing_key="hello4",  # 指定队列
    body="hello chijiuhua",
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent 消息持久化
    ))

print(" [x] Sent 'Hello body!'")
# connection.close()
```

消费者

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 1.创建队列
channel.queue_declare(queue="hello4", durable=True)


# 2.确定回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# no_ack=Fales:表示消费完以后不主动把状态通知rabbitmq

# 3.确定监听队列参数
channel.basic_consume(
    queue='hello4',
    auto_ack=False,  # 默认应答改为手动应答
	on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 正式监听
channel.start_consuming()
```

##### 16.2.2.4 分发参数

有两个消费者同时监听一个的队列。其中一个线程sleep2秒，另一个消费者线程sleep1秒，但是处理的消息是一样多。这种方式叫轮询分发（round-robin）不管谁忙，都不会多给消息，总是你一个我一个。想要做到公平分发（fair dispatch），必须关闭自动应答ack，改成手动应答。使用basicQos(perfetch=1)限制每次只发送不超过1条消息到同一个消费者，消费者必须手动反馈告知队列，才会发送下一个。

生产者

```python
import pika

# 1.连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 2.创建可持久化队列
channel.queue_declare(queue="ccc1")

# 3.向指定队列插入数据
channel.basic_publish(
    exchange="",  # 简单模式
    routing_key="ccc1",  # 指定队列
    body="b36",
  )

print(" [x] Sent 'Hello body!'")
# connection.close()
```

消费者

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 1.创建队列
channel.queue_declare(queue="ccc1")


# 2.确定回调函数
def callback(ch, method, properties, body):
    import time
    time.sleep(3)  # 先睡20秒启动，然后改成3秒，写入数据测试
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 公平分发
channel.basic_qos(prefetch_count=1)


# 3.确定监听队列参数
channel.basic_consume(
    queue='ccc1',
    auto_ack=False,  # 默认应答改为手动应答
    on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 正式监听
channel.start_consuming()
```

#### 16.2.3 交换机模式

##### 16.2.3.1 发布订阅

<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimage.mamicode.com%2Finfo%2F201803%2F20180330221803429111.png&refer=http%3A%2F%2Fimage.mamicode.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1639045942&t=85e5ffbd82b42ce2a2dde9a4ef9c81e7" alt="img" style="zoom:50%;" />

发布订阅和简单的消息队列区别在于，发布订阅会通过消费者队列绑定交换机的关系，将所有的消息发送给每一个的消费者；而消息队列中的数据被消费一次便消失。所以，RabbitMQ实现发布和订阅时，会为每一个消费者创建一个队列，而发布者发布消息时，会将消息通过与交换机绑定的队列，放置在所有相关队列中。

生产者

```python
import pika

# 1.连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 2.创建一个名为logs  类型为fanout的交换机
channel.exchange_declare(exchange="logs", exchange_type="fanout")

# 3.向logs交换机插入数据 "info:hello exchange"
messge = "info:hello exchange"
channel.basic_publish(
    exchange="logs",  # 交换机模式
    routing_key="",  # 指定队列
    body=messge,
)

print(" [x] Sent {}".format(messge))
connection.close()
```

消费者

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 1.创建一个名为logs  类型为fanout的交换机
channel.exchange_declare(exchange="logs", exchange_type="fanout")

# 2.创建队列
result = channel.queue_declare("", exclusive=True)
queue_name = result.method.queue
print(queue_name)

# 3.将指定队列绑定到交换机上
channel.queue_bind(exchange="logs", queue=queue_name)
print(' [*] Waiting for messages. To exit press CTRL+C')


# 4.确定回调函数
def callback(ch, method, properties, body):
    print("[x] {}".format(body))


# 5.确定监听队列参数
channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

# 正式监听
channel.start_consuming()
```

##### 16.2.3.2 交换机之关键字

<img src="https://images2015.cnblogs.com/blog/425762/201607/425762-20160717140748795-1181706200.png" alt="img" style="zoom:80%;" />

生产者在交换机中指定消息队列名，消费者创建的交换机绑定的队列与生产者一致，生产者在哪个队列中写入数据，消费者则在对应的队列中获取数据。

生产者

```python
import pika

# 1.连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 2.创建一个名为logs  类型为direct的交换机
channel.exchange_declare(exchange="logs2", exchange_type="direct")

# 3.向logs交换机插入数据 "error:hello exchange"
messge = "error:hello exchange"
channel.basic_publish(
    exchange="logs2",  # 交换机模式
    routing_key="error",  # 指定队列
    body=messge,
)

print(" [x] Sent {}".format(messge))
connection.close()
```

消费者

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 1.创建一个名为logs  类型为direct的交换机
channel.exchange_declare(exchange="logs2", exchange_type="direct")

# 2.创建队列
result = channel.queue_declare("", exclusive=True)
queue_name = result.method.queue
print(queue_name)

# 3.将指定队列绑定到交换机上
channel.queue_bind(exchange="logs2", queue=queue_name, routing_key="error")
print(' [*] Waiting for messages. To exit press CTRL+C')


# 4.确定回调函数
def callback(ch, method, properties, body):
    print("[x] {}".format(body))


# 5.确定监听队列参数
channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

# 正式监听
channel.start_consuming()
```

##### 16.2.3.3 通配符

通配符交换机”与之前的路由模式相比，它将信息的传输类型的key更加细化，以“key1.key2.keyN....”的模式来指定信息传输的key的大类型和大类型下面的小类型，让消费者可以更加精细的确认自己想要获取的信息类型。而在消费者一段，不用精确的指定具体到哪一个大类型下的小类型的key，而是可以使用类似正则表达式(但与正则表达式规则完全不同)的通配符在指定一定范围或符合某一个字符串匹配规则的key，来获取想要的信息。

“通配符交换机”（Topic Exchange）将路由键和某模式进行匹配。此时队列需要绑定在一个模式上。 **符号“#”匹配一个或多个词，符号“”仅匹配一个词** 。因此“audit.#”能够匹配到“audit.irs.corporate”，但是“audit.”只会匹配到“audit.irs”。（这里与我们一般的正则表达式的“*”和“#”刚好相反，这里我们需要注意一下。）
下面是一个解释通配符模式交换机工作的一个样例

<img src="https://img-blog.csdn.net/20180318124005972" alt="img" style="zoom: 80%;" />

生产者

```python
import pika

# 1.连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 2.创建一个名为logs  类型为topic的交换机
channel.exchange_declare(exchange="logs3", exchange_type="topic")

# 3.向logs交换机插入数据 "usa.weather..."
messge = "usa.weather...."
channel.basic_publish(
    exchange="logs3",  # 交换机模式
    routing_key="usa.weather",  # 指定队列
    body=messge,
)

print(" [x] Sent {}".format(messge))
connection.close()
```

消费者

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# 1.创建一个名为logs  类型为topic的交换机
channel.exchange_declare(exchange="logs3", exchange_type="topic")

# 2.创建队列
result = channel.queue_declare("", exclusive=True)
queue_name = result.method.queue
print(queue_name)

# 3.将指定队列绑定到交换机上
channel.queue_bind(exchange="logs3", queue=queue_name, routing_key="#.weather")  # 使用通配符进行匹配
print(' [*] Waiting for messages. To exit press CTRL+C')


# 4.确定回调函数
def callback(ch, method, properties, body):
    print("[x] {}".format(body))


# 5.确定监听队列参数
channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

# 正式监听
channel.start_consuming()
```

----

### 16.3 Git

#### 16.3.1 Git简介

同生活中的许多伟大事物一样，Git 诞生于一个极富纷争大举创新的年代。

Linux 内核开源项目有着为数众多的参与者。 绝大多数的 Linux 内核维护工作都花在了提交补丁和保存归档的繁琐事务上（1991－2002年间）。 到 2002 年，整个项目组开始启用一个专有的分布式版本控制系统 BitKeeper 来管理和维护代码。

到了 2005 年，开发 BitKeeper 的商业公司同 Linux 内核开源社区的合作关系结束，他们收回了 Linux 内核社区免费使用 BitKeeper 的权力。 这就迫使 Linux 开源社区（特别是 Linux 的缔造者 Linus Torvalds）基于使用 BitKeeper 时的经验教训，开发出自己的版本系统。 他们对新的系统制订了若干目标：

- 速度
- 简单的设计
- 对非线性开发模式的强力支持（允许成千上万个并行开发的分支）
- 完全分布式
- 有能力高效管理类似 Linux 内核一样的超大规模项目（速度和数据量）

自诞生于 2005 年以来，Git 日臻成熟完善，在高度易用的同时，仍然保留着初期设定的目标。 它的速度飞快，极其适合管理大项目，有着令人难以置信的非线性分支管理系统

**Git** 是一个开源的分布式版本控制软件,用以有效、高速的处理从很小到非常大的项目版本管理。 Git 最初是由*Linus Torvalds*设计开发的，用于管理Linux内核开发。Git 是根据GNU通用公共许可证版本2的条款分发的自由/免费软件，安装参见：https://git-scm.com/book/zh

**GitHub** 是一个基于Git的远程文件托管平台（同GitCafe、BitBucket和GitLab等）。

Git本身完全可以做到版本控制，但其所有内容以及版本记录只能保存在本机，如果想要将文件内容以及版本记录同时保存在远程，则需要结合GitHub来使用。使用场景：

- 无GitHub：在本地 .git 文件夹内维护历时文件
- 有GitHub：在本地 .git 文件夹内维护历时文件，同时也将历时文件托管在远程仓库

其他：

  集中式：远程服务器保存所有版本，用户客户端有某个版本
  分布式：远程服务器保存所有版本，用户客户端有所有版本

#### 16.3.2 "东北热"创业史

##### 16.3.2.1 第一阶段：单枪匹马撸

想要让git对一个目录进行版本控制需要以下步骤：

- 进入需要管理的文件夹

- 执行初始化命令，表示即将对当前文件夹进行版本控制

    ```shell
    git init
    ```

- 管理目录下的文件状态

    ```shell
    git status
    # 注：新增的文件和修改过后的文件都是红色的
    ```

- 管理指定文件

    ```shell
    git add 文件名  # 添加单个文件到版本库
    git add .	   # 添加当前目录下所有文件到版本库
    ```

- 个人信息配置：用户名、邮箱【输入一次即可】

    ```shell
    git config --global user.name "zzq" 
    git config --global user.email "zq15010008824@163.com"
    ```

- 生成版本

    ```shell
    git commit -m "描述信息"  # 提交到版本库，并填写版本说明，以便以后回滚。
    ```

    注意：执行git commit 命令时，可能会提示进行用户和邮箱的配置，该配置用于记录当前版本由那个用户提交

- 查看版本记录

    ```shell
    git log
    ```

<img src="j:\homework\Python学习笔记\Python_notes.assets\425762-20170811093733792-860907399.png" alt="img" style="zoom:67%;" />

**版本库**：工作区检测到有文件发生变化，那么意味着较上一个版本之后对程序进行了修改，修改完成之后，可以当做下一版本进行提交，那么就是执行 【git add .】 将所有文件提交到暂存区，然后再执行【git commit -m '又一个版本'】提交到版本库的分支即可，之后可以使用【git log】命令查看版本记录。

目前已使用Git的四个命令，这四个命令已经可以代替本地多个文件保存版本的方式：

```shell
git init					# 初始化，表示即将对当前文件夹进行版本控制。
git status					# 查看Git当前状态，如：那些文件被修改过、那些文件还未提交到版本库等。
git add 文件名	  			  # 将指定文件添加到版本库的暂存状态。
git rm --cached a			# 将文件从暂存区移到工作目录
git rm -f a					# 删除暂存区的文件，同时删除本地文件
git mv a  a.txt				# 改动暂存区和本地的文件名
git diff a					# 比对本地和暂存区的文件区别
git diff --cached a			# 比对暂存区和版本库文件区别
git commit -m '提交信息'	 # 将暂存区的文件提交到版本库的分支。
git log					  	# 查看提交记录，即：历史版本记录
git log --online			# 查看提交记录，简写形式
git log --online --decorate	# 查看提交记录，简写形式，包括分支
git log -p					# 查看提交记录，详细信息
```

##### 16.3.2.2 第二节点：拓展新功能

```shell
git add 文件名
git commit -m "短视频"
```

##### 16.3.2.3 第三阶段：约饭事件

已经开发好的功能，先下掉，回滚到之前的版本。等到上的时候再回滚到现在开发好的版本。

- 回滚到之前的版本

    ```shell
    git log  # 查看现有的版本
    git reset --hard 版本号
    ```

- 回滚到之后版本

    ```shell
    git reflog  # 查看所有的版本
    git 
    ```

    <img src="j:\homework\Python学习笔记\Python_notes.assets\425762-20170811110830683-181174888.png" alt="img" style="zoom:67%;" />

示例：

```shell
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ touch views-master.py		# 模拟新建一个项目

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ vim views-master.py		# 编写新的项目

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git status				# 查看git状态，是否被修改过
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        views-master.py

nothing added to commit but untracked files present (use "git add" to track)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git add .					# 将文件添加到版本库的暂存区
warning: LF will be replaced by CRLF in views-master.py.
The file will have its original line endings in your working directory

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git commit -m "第一版提交"	 # 将缓存区的文件提交到版本库的分支
[master (root-commit) 5a1a8f0] 第一版提交
 1 file changed, 1 insertion(+)
 create mode 100644 views-master.py

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git status				# 查看git状态
On branch master
nothing to commit, working tree clean

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ vim views-master.py		# 模拟提交第二版

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git status				# 查看git状态
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   views-master.py

no changes added to commit (use "git add" and/or "git commit -a")

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git add .					# 将文件添加到缓存区
warning: LF will be replaced by CRLF in views-master.py.
The file will have its original line endings in your working directory

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git commit -m "第二版提交"		# 将缓存区的文件提交到版本库的分支
[master 3def87c] 第二版提交
 1 file changed, 2 insertions(+), 1 deletion(-)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git status
On branch master
nothing to commit, working tree clean

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git log						# 查看提交记录
commit 3def87cc65afb2ab9919272e644e70a186d4f6f2 (HEAD -> master)
Author: zzq <zq15010008824@163.com>
Date:   Wed Nov 17 10:41:54 2021 +0800

    第二版提交

commit 5a1a8f040455e946497b85b51d9347953f8a3cf8
Author: zzq <zq15010008824@163.com>
Date:   Wed Nov 17 10:38:35 2021 +0800

    第一版提交

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ vim views-master.py		# 新增短视频功能

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git add .					# 提交到暂存区
warning: LF will be replaced by CRLF in views-master.py.
The file will have its original line endings in your working directory

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git commit -m "提交短视频功能"		# 提交到版本库分支
[master 8b82e98] 提交短视频功能
 1 file changed, 2 insertions(+), 1 deletion(-)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git status				# 查看git状态
On branch master
nothing to commit, working tree clean

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git log					# 查看提交记录
commit 8b82e9878fd9df05b030cad7e7106f0dc6be5887 (HEAD -> master)
Author: zzq <zq15010008824@163.com>
Date:   Wed Nov 17 10:43:39 2021 +0800

    提交短视频功能

commit 3def87cc65afb2ab9919272e644e70a186d4f6f2
Author: zzq <zq15010008824@163.com>
Date:   Wed Nov 17 10:41:54 2021 +0800

    第二版提交

commit 5a1a8f040455e946497b85b51d9347953f8a3cf8
Author: zzq <zq15010008824@163.com>
Date:   Wed Nov 17 10:38:35 2021 +0800

    第一版提交

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git reset --hard 3def87cc65afb2ab9919272e644e70a186d4f6f2		# 回到之前的版本
HEAD is now at 3def87c 第二版提交

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ cat views-master.py
print("开发新程序，完成")
print("提交新功能")

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git reflog					# 查看所有的提交记录
3def87c (HEAD -> master) HEAD@{0}: reset: moving to 3def87cc65afb2ab9919272e644e70a186d4f6f2
8b82e98 HEAD@{1}: commit: 提交短视频功能
3def87c (HEAD -> master) HEAD@{2}: commit: 第二版提交
5a1a8f0 HEAD@{3}: commit (initial): 第一版提交

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git reset --hard 8b82e98			# 回到之后的记录
HEAD is now at 8b82e98 提交短视频功能

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ cat views-master.py				# 成功返回到之后的记录
print("开发新程序，完成")
print("第二版提交")
print("提交短视频")

```

##### 16.3.2.4 第四阶段：紧急修复bug

###### 16.3.2.4.1 分支

分支可以给使用者提供多个环境，意味着你可以把你的工作从主线上分离出来，以免影响发开主线。

###### 16.3.2.4.2 紧急修复bug

分支学习：branch称为分支，默认仅有一个名为master的分支。一般开发新功能流程为：开发新功能时会在分支dev上进行，开发完毕后再合并到master分支。

![img](j:\homework\Python学习笔记\Python_notes.assets\425762-20170811152733617-1247689823.png)

**命令总结**：

- 查看分支

    ```shell
    git branch
    ```

- 创建分支

    ```shell
    git branch 分支名称
    ```

- 切换分支

    ```SHELL
    git checkout 分支名称
    ```

- 创建并切换到指定分支

    ```shell
    git branch -m 分支名称
    ```

- 分支合并（可能产生冲突）

    ```shell
    git merge 要合并的分支
    
    # 注意：切换分支再合并
    ```

- 删除分支

    ```shell
    git branch -d 分支名称
    ```

示例：

```shell
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (master)
$ git branch dev	# 创建新分支，即：拷贝一份当前所在分支代码到新分支

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (master)
$ git branch		# 查看分支
  dev
* master

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (master)
$ git checkout dev	# 切换到dev分支
Switched to branch 'dev'

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (dev)
$ git branch		# 查看分支
* dev
  master

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (dev)
$ vim views-master.py  # 修改bug

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (dev)
$ git status		# 查看状态，即：在dev分支修改了views-dev.py文件
On branch dev
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        views-dev.py

nothing added to commit but untracked files present (use "git add" to track)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (dev)
$ git add .			# 将修改文件添加到版本库的暂存区
warning: LF will be replaced by CRLF in views-dev.py.
The file will have its original line endings in your working directory

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (dev)
$ git commit -m "dev分支修改bug"	# 将暂存区的内容提交到当前所在分支，即：dev分支
[dev c4a0e18] dev分支修改bug
 1 file changed, 1 insertion(+)
 create mode 100644 views-dev.py

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (dev)
$ git checkout master	# 切换回master分支 
Switched to branch 'master'

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (master)
$ git branch		# 查看分支
  dev
* master

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (master)
$ git merge dev		# 将dev分支内容合并到master分支
Updating 8b38e05..c4a0e18
Fast-forward
 views-dev.py | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 views-dev.py
 
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (master)
$ git branch -d dev		# 删除分支
Deleted branch dev (was c4a0e18).

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/dbhot (master)
$ git branch
```

学习参考上图，小P也可以按照着这样的流程进行开发，如果遇到上文开发到一般需要临时修复Bug的情况，可以按照下图的流程进行：

![1639276593788](J:\homework\Python学习笔记\Python_notes.assets\1639276593788.png)

```shell
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git branch			# 当前在master分支
  dev
* master

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git checkout dev		# 切换到dev分支用来开发新功能
Switched to branch 'dev'

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ vim views-master.py		# 开发新功能

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git add .				# 提交到版本暂存区

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git commit -m "新开发到一半"	# 将暂存区的文件提交到版本分支
[dev 411b503] 新开发到一半
 1 file changed, 1 insertion(+)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git checkout master		# 切换到master分支
Switched to branch 'master'

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git branch			# 当前在master分支
  dev
* master

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git branch bug		# 新建bug分支，用来紧急修复bug

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git checkout bug		# 切换到bug分支
Switched to branch 'bug'

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (bug)
$ vim views-master.py	# 修复bug

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (bug)
$ git add .				# 提交到版本暂存区

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (bug)
$ git commit -m "新功能开发一半，紧急修复bug"	# 提交到版本库
[bug 2b30ea1] 新功能开发一半，紧急修复bug
 1 file changed, 2 insertions(+)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (bug)
$ git checkout master		# 切换到master分支
Switched to branch 'master'

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git merge bug				# 合并修复的bug
Updating 8713dfe..2b30ea1
Fast-forward
 views-master.py | 2 ++
 1 file changed, 2 insertions(+)
 
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master|MERGING)
$ git add .			# 将bug提交到暂存区

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master|MERGING)
$ git commit -m "紧急bug上线"		# 将暂存区的bug发到版本库分支
[master 2e6b428] 紧急bug上线


Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git checkout dev		# 切换到dev分支
Switched to branch 'dev'

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ vim views-master.py	# 继续开发新功能

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git add .				# 提交到版本暂存区

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git commit -m "继续开发"	# 提交到版本库分支
[dev 132bb26] 继续开发
 1 file changed, 1 insertion(+)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git checkout master		# 切换到master分支
Switched to branch 'master'

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git merge dev				# 将新功能合并到主分支
Auto-merging views-master.py
CONFLICT (content): Merge conflict in views-master.py
Automatic merge failed; fix conflicts and then commit the result.

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master|MERGING)
$ cat views-master.py		# 产生冲突
print("开发新程序，完成")
print("第二版提交")
print("提交短视频")
print("在dev环境紧急修复bug")
<<<<<<< HEAD
print("新功能开发到一半")
print("新功能紧急修复bug")
=======
print("模拟开发到一半，需要紧急修复bug")
print("修复完bug继续开发")
>>>>>>> dev

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master|MERGING)
$ vim views-master.py		# 解决冲突

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master|MERGING)
$ git status		# 查看分支状态
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   views-master.py

no changes added to commit (use "git add" and/or "git commit -a")

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master|MERGING)
$ git add .		# 将新功能提交到暂存区

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master|MERGING)
$ git commit -m "新功能上线"
```

注意：git merge 时也可能会出现冲突，解决冲突的方式上述stash相同，即：找到冲突文件，手动修改冲突并提交，此处不再敖述。

##### 16.3.2.5 第五阶段：进军三里屯

GitHub，一个基于Git实现的代码托管的平台，可以将内容以及版本记录在远程也保存一份，这样就不用U盘咯（类似于云盘）。PS: 类似GitHub的产品还有许多，如：GitLab、Bitbucket、码云等。

<img src="Python_notes.assets/425762-20170811191610632-470737695.png" alt="img" style="zoom: 50%;" />

基于GitHub实现代码托管：

- 注册一个GitHub账号
- 创建仓库
- 创建完后，会生成一个仓库地址
- git可以是用该URL进行向远程推送版本信息或获取版本信息

![1639276866245](J:\homework\Python学习笔记\Python_notes.assets\1639276866245.png)

![1639276940571](J:\homework\Python学习笔记\Python_notes.assets\1639276940571.png)

<img src="https://images2017.cnblogs.com/blog/425762/201708/425762-20170812194454960-1674213106.png" alt="img" style="zoom:50%;" />

命令总结：

- 给远程仓库起个别名

    ```shell
    git remote add origin 远程仓库地址
    ```

- 向远程推送代码

    ```shell
    git push -u origin 分支
    ```

**在把家**，里电脑的代码推送到GitHub

```shell
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git remote add pythonall git@github.com:zhangzhqiang/python-.git  # 给远程仓库起个别名

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git push pythonall master		# 将master分支推送到远程仓库
Enumerating objects: 36, done.
Counting objects: 100% (36/36), done.
Delta compression using up to 8 threads
Compressing objects: 100% (23/23), done.
Writing objects: 100% (36/36), 3.25 KiB | 554.00 KiB/s, done.
Total 36 (delta 9), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (9/9), done.
To https://github.com/zhangzhqiang/dbhot.git
 * [new branch]      master -> master

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (master)
$ git push pythonall dev		# 将dev分支推送到远程仓库
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'dev' on GitHub by visiting:
remote:      https://github.com/zhangzhqiang/dbhot/pull/new/dev
remote:
To https://github.com/zhangzhqiang/dbhot.git
 * [new branch]      dev -> dev

```

**在公司**，新电脑第一次使用，需要将代码从GitHub中获取并继续开发，开发完事下班就下班回家。

```shell
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot (master)
$ git clone https://github.com/zhangzhqiang/python-.git		# 克隆远程仓库代码
Cloning into 'dbhot'...
remote: Enumerating objects: 36, done.
remote: Counting objects: 100% (36/36), done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 36 (delta 9), reused 36 (delta 9), pack-reused 0
Receiving objects: 100% (36/36), done.
Resolving deltas: 100% (9/9), done.

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework (dev)
$ cd home-dbhot/

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot (master)
$ git checkout dev											# 切换分支
Switched to branch 'dev'
M       "Python\345\255\246\344\271\240\347\254\224\350\256\260/Python_notes.md"

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot (dev)
$ git merge master											# 把master分支合并到dev（仅合并一次）
Already up to date.

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git remote add db-hot https://github.com/zhangzhqiang/dbhot.git  # 给远程仓库起个别名

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git push db-hot dev												# 把代码推到dev分支
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 333 bytes | 333.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/zhangzhqiang/dbhot.git
   c1191cf..5b9e013  dev -> dev

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git checkout master											# 切换到master分支
Switched to branch 'master'
Your branch is up to date with 'origin/master'.

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (master)
$ git merge dev								# dev分支似乎最新的，将dev分支合到master
Updating b48e9ad..5b9e013
Fast-forward
 a1.py | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 a1.py

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (master)
$ git push db-hot master					# 将master分支的代码推到GitHub仓库的master分支
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/zhangzhqiang/dbhot.git
   b48e9ad..5b9e013  master -> master
```

**在家里**，由于白天在公司已经开发一部分功能并提交到GitHub，家里电脑的代码还是昨晚的版本，所以需要从GitHub拉去最新代码，然后继续开发。

```shell
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git checkout dev								# 切换到dev分支
Already on 'dev'

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git pull db-hot dev							# 从GitHub把代码拉下来
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 313 bytes | 1024 bytes/s, done.
From https://github.com/zhangzhqiang/dbhot
 * branch            dev        -> FETCH_HEAD
   c1191cf..5b9e013  dev        -> db-hot/dev
Updating c1191cf..5b9e013
Fast-forward
 a1.py | 1 +
 1 file changed, 1 insertion(+)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ vim a2.py										# 继续开发

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git add .										# 提交到版本暂存区
warning: LF will be replaced by CRLF in a2.py.
The file will have its original line endings in your working directory

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git commit -m "在家开发a2"					# 将暂存区的文件提交到版本库分支
[dev 870d772] 在家开发a2
 1 file changed, 1 insertion(+)
 create mode 100644 a2.py

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git push db-hot dev							# 将代码推送到GitHub的dev分支
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 339 bytes | 339.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/zhangzhqiang/dbhot.git
   5b9e013..870d772  dev -> dev
```

**在公司**，由于昨天晚上在家已经开发了一部分功能，在公司需要先把昨晚开发的功能从GitHub中拉取，并继续开发。

```shell
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (master)
$ git checkout dev					# 切换到dev分支
Switched to branch 'dev'
Your branch is ahead of 'origin/dev' by 1 commit.
  (use "git push" to publish your local commits)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git pull db-hot dev				# 把最新的代码拉下来
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 319 bytes | 1024 bytes/s, done.
From https://github.com/zhangzhqiang/dbhot
 * branch            dev        -> FETCH_HEAD
   5b9e013..870d772  dev        -> db-hot/dev
Updating 5b9e013..870d772
Fast-forward
 a2.py | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 a2.py

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ vim a2.py							# 开发新的功能

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git add .							# 把代码推到版本暂存区

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git commit -m "在公司继续开发a2"		# 把代码提交到版本库分支
[dev d721fb6] 在公司继续开发a2
 1 file changed, 1 insertion(+)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git push db-hot dev				# 把代码提交到GitHub的dev分支
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 364 bytes | 364.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/zhangzhqiang/dbhot.git
   870d772..d721fb6  dev -> dev
```

在公司开发完毕上线

```shell
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git checkout master		# 切换到master分支
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (master)
$ git merge dev				# 把dev分支合到master
Updating 5b9e013..d721fb6
Fast-forward
 a2.py | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 a2.py

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (master)
$ git push db-hot master	# 把master分支提交到GitHub的master分支
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/zhangzhqiang/dbhot.git
   5b9e013..d721fb6  master -> master
```

在公司开发，下班忘记push代码

```shell
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (master)
$ git checkout dev		# 切换到dev分支

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git pull db-hot dev		# 把GitHub的dev分支的代码拉下来
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 319 bytes | 1024 bytes/s, done.
From https://github.com/zhangzhqiang/dbhot
 * branch            dev        -> FETCH_HEAD
   5b9e013..870d772  dev        -> db-hot/dev
Updating 5b9e013..870d772
Fast-forward
 a2.py | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 a2.py

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ vim a2.py				# 继续编写代码

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git add .				# 把代码提交到版本暂存区

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git commit -m "在公司继续开发a2,忘记push"	# 把暂存区的代码提交的版本区分支，没有push到GitHub
[dev 884664d] 在公司继续开发a2,忘记push
 1 file changed, 1 insertion(+)
```

回家继续写代码

```shell
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (master)
$ git checkout dev			# 切换到dev分支

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git pull db-hot dev			# 把GitHub仓库的dev分支拉下来
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 344 bytes | 2.00 KiB/s, done.
From https://github.com/zhangzhqiang/dbhot
 * branch            dev        -> FETCH_HEAD
   870d772..d721fb6  dev        -> db-hot/dev
Updating 870d772..d721fb6
Fast-forward
 a2.py | 1 +
 1 file changed, 1 insertion(+)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ vim a2.py					# 继续编写代码

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git add .					# 提交到版本暂存区

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git commit -m "开发在家没有push的a2"		# 提交到版本库分支
[dev 01d86f7] 开发在家没有push的a2
 1 file changed, 1 insertion(+)

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/git-dbhot (dev)
$ git push db-hot dev			# 提交到GitHub
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 391 bytes | 391.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/zhangzhqiang/dbhot.git
   d721fb6..01d86f7  dev -> dev
```

到公司继续写代码

```shell
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (master)
$ git checkout dev			# 切换到dev分支

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git pull db-hot dev		# 从GitHub拉代码
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 371 bytes | 2.00 KiB/s, done.
From https://github.com/zhangzhqiang/dbhot
 * branch            dev        -> FETCH_HEAD
   d721fb6..01d86f7  dev        -> db-hot/dev
Auto-merging a2.py
CONFLICT (content): Merge conflict in a2.py		 # 发aa2冲突了，原因上次在公司写的时候没有push到远程仓库
Automatic merge failed; fix conflicts and then commit the result.

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev|MERGING)
$ vim a2.py						# 解决冲突并继续开发

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev|MERGING)
$ git add .					# 提交到版本暂存区

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev|MERGING)
$ git commit -m "解决拉代码的冲突后继续开发"			# 提交到版本库分支
[dev d6a7441] 解决拉代码的冲突后继续开发

Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/home-dbhot/dbhot (dev)
$ git push db-hot dev		# 提交到GitHub
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 798 bytes | 798.00 KiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/zhangzhqiang/dbhot.git
   01d86f7..d6a7441  dev -> dev
```

**其他**

```powershell
git pull db-hot dev 等于 git fetch db-hot dev 加 git merge db-hot dev
```

![1639278963127](J:\homework\Python学习笔记\Python_notes.assets\1639278963127.png)

###### 16.3.2.5.1 rebase的作用

rebase 可以保持提交记录简洁 **变基** ，不分叉。

方式一：

```shell
# 1.创建4个文件，并提交到版本库分支
touch a1.py  ..... a4.py
git add .
git commit -m "a1...a4"
git log

# 2.合并版本记录
git rebase 版本号   # 把版本号之间的的版本合并
#  或者
git rebase -i HEAD~3  # 当前版本的前三个版本合并
# 2.1把要合并的的分支pick该为s
pick 54e571f a2
s b7ef5da a3
s 8e11d41 a4
# 2.2以哪种描述信息链接分支记录
 a2 & a3 & a4
 
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/pro_rebase (master)
$ git log
commit ce51f797fb007e30abb6f3234851fefc5a76b4d5 (HEAD -> master)
Author: zzq <zq15010008824@163.com>
Date:   Wed Nov 17 21:28:56 2021 +0800

    a2 & a3 & a4

commit 7889b94d30ab7b5a5dcc6089625a8b04c608bdb6
Author: zzq <zq15010008824@163.com>
Date:   Wed Nov 17 21:28:34 2021 +0800

    a1
```

**注意：合同并记录时，建议不要合并已经push到GitHub仓库的记录**

方式二：

```shell
# 1.切换到dev分支创建dev1文件
git checkout dev
touch dev1.py
git add .
git commit -m "dev commit 1"

# 2.切换到master分支创建master1，提交到版本库
git checkout master
touch master1.py
git add .
git commit -m "master commit 1"

# 3.切换到dev分支，合并分支记录
git checkout dev
git rebase master

# 4.切换到master分支，合同dev分支
git checkout master
git merge dev
git log --graph
git log --graph --pretty=format:"%h %s"  # 查看格式化后的分支记录
```

方式三：

```shell
# 当拉代码的时候有冲突，我们叫做分叉
# 把 git pull db-hot dev 改为
git feach db-hot dev
git rebase db-hot/dev
```

示例：

```shell
# 1.切换到master分支，创建a1文件，提交到版本库分支
git checkout master
vim a1.py
git add .
git commit -m "master a1"

# 2.切换到devs分支，创建a1文件，提交到版本库分支
git checkout dev
vim a1.py
git add .
git commit -m "dev a1"

# 3.将master分支记录合并到dev分支
Administrator@74NTQEQTP61QRX3 MINGW64 /g/homework/pro_rebase (dev)
$ git rebase master
error: could not apply 8c85548... dev a1  # dev合master都修改了a1产生了冲突
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 8c85548... dev a1
Auto-merging a1.py
CONFLICT (content): Merge conflict in a1.py

# 4.解决冲突，提交文件到版本暂存区，继续合并master分支记录
vim a1.py
git status
git add a1.py
git rebase --continue
git log --graph --pretty=format:"%h %s"
```

###### 16.3.2.5.2 快速解决冲突

1. 安装beyond compare

2. 在git中配置beyond compare， --local 只对当前的项目生效

    ```shell
    git config --local merge.tool bc3			# 给合并工具起个别名
    git config --local mergetool.path "F:\Program Files\Beyond Compare 4\BCompare.exe"  # 指定安装目录
    git config --local mergetool.keepBackup false		# 在合并的时候是否进行备份
    ```

3. 应用beyond compare

    ```shell
    git mergetool
    ```

###### 16.3.2.5.3 命令总结

- 添加远程链接

    ```shell
    git remote add origin 链接地址
    ```

- 推送代码

    ```shell
    git push origin dev
    ```

- 下载代码

    ```shell
    git clone 链接地址
    ```

- 拉去代码

    ```shell
    git pull origin dev
    # 等价于
    git fectch origin dev
    git merge origin/dev 或 git rebase origin/dev
    ```

- 保持代码清洁（变基）

    ```shell
    git rebase 分支
    ```

- 记录图形展示

    ```shell
    git log --graph --pretty=format:"%h %s"
    ```

##### 16.3.2.6 第六阶段：多人协同开发

###### 16.3.2.6.1 创建项目 & 邀请成员

协同开发时，需要所有成员都可以对同一个项目进行操作，需要邀请成员并赋予权限，否则无法开发。github支持两种创建项目的方式（多人协同开发）

1. 合作者：将用户添加到仓库合作者中之后，该用户就可以向当前仓库提交代码。

    > https://docs.github.com/cn/account-and-profile/setting-up-and-managing-your-github-user-account/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository

![1639279335914](J:\homework\Python学习笔记\Python_notes.assets\1639279335914.png)

2. 组织：将成员邀请进入组织，组织下可以创建多个仓库，组织成员可以向组织下仓库提交代码。

![1639279591028](J:\homework\Python学习笔记\Python_notes.assets\1639279591028.png)

![1639279910643](J:\homework\Python学习笔记\Python_notes.assets\1639279910643.png)

![1639280079225](J:\homework\Python学习笔记\Python_notes.assets\1639280079225.png)

![1639280182089](J:\homework\Python学习笔记\Python_notes.assets\1639280182089.png)

![1639280256781](J:\homework\Python学习笔记\Python_notes.assets\1639280256781.png)

![1639280294887](J:\homework\Python学习笔记\Python_notes.assets\1639280294887.png)

```shell
git add .
git commit -m "conmmit org master"
git tag -a v1.0 -m "1.0的tag"	# 本地创建tag信息
git tag -d v1.0	# 删除tag
git push org --tags	# 将本地tag信息推送到远程仓库
git pull org --tags	# 更新本地tag版本信息
git checkout v2.0	# 切换tag
git clone -b v3.0 地址  # 指定tag下载代码
```

###### 16.3.2.6.2 协同开发

- 新人创建GitHub 或 GitLab账号
- 邀请同事进入组织（默认对项目的组织具有读权限）
- 接受后，就加进来了

**1. 邀请新人加入组织，组织默认只有读的权限，可以去看其他项目的代码，但不可以写**

![1639371179037](J:\homework\Python学习笔记\Python_notes.assets\1639371179037.png)

**2. 邀请加入项目，针对项目给写的权限**

![1639280471746](J:\homework\Python学习笔记\Python_notes.assets\1639280471746.png)

![1639280536295](J:\homework\Python学习笔记\Python_notes.assets\1639280536295.png)

邀请新成员成为项目的协作者，在项目中添加成员，并给予写的权限，在组织内只有查的权限，无法写其他的项目

![1639280570502](J:\homework\Python学习笔记\Python_notes.assets\1639280570502.png)

###### 16.3.2.6.3 新人下载代码开发

```powershell
# 1.组织者创建好项目
mkdir tongchengre
cd tongchengre
touch app.py
git init
git add .
git commit -m "tongchengre"
git remote add origin git@github.com:python-pra/tongchengre.git
git push -u origin master
git tag -a v1.0 -m "1.0版本"
git push origin --tags
git checkout -b dev
git push origin dev
```

1. 邀请新人加入组织，加入组织后默认只有读的权限
2. 邀请新人加入项目，对项目进行开发

```shell
# 2.模拟新人在自己的电脑上下载代码
mkdir brother
cd brother/
git clone https://github.com/python-pra/tongchengre.git
cd tongchengre/
git checkout dev
git checkout -b tongchengre	# 在dev分支基础上再创建分支
touch tongchengre.py
git add .
git commit -m "同城热50%"
git push origin tongchengre

vim 斗地主.py
git add .
git commit -m "同乘热项目开发完成"
git push origin tongchengre
```

###### 16.3.2.6.4 code review

1. 先配置代码review后，才能合并到dev分支

![1639375742980](J:\homework\Python学习笔记\Python_notes.assets\1639375742980.png)

![1639375841685](J:\homework\Python学习笔记\Python_notes.assets\1639375841685.png)

2. 小弟提交code review申请

![1639375945589](J:\homework\Python学习笔记\Python_notes.assets\1639375945589.png)

![1639379748254](J:\homework\Python学习笔记\Python_notes.assets\1639379748254.png)

3. 组长做code review后可以删除分支

![1639380027265](J:\homework\Python学习笔记\Python_notes.assets\1639380027265.png)

###### 16.2.6.5 提测上线（预发布）

测试部门完成测试，可以在github上pull request进行验证合并，后删除release分支，也可以通过merge进行合并

由测试部门或团队leader执行以下步骤：

1. 基于dev分支创建release分支

```shell
git branch
git checkout -b release
git push origin release
```

2. 测试部门拉release分支代码进行测试

```powershell
git pull origin release
```

3. 合并到dev

```shell
# 使用 pull request 或通过merge将 release 合并到 dev分支
git checkout dev
git merge release
git branch -d release
```

4. 在master分支打tag

```shell
git checkout master
git pull origin master
git tag -a v2.0 -m "第二版 开发完成"
git push origin --tags
```

5. 运维人员就可以下载代码做上线了

```shell
git clone -b v2.0 地址
```

##### 16.3.2.7 第七阶段：给开源软件贡献代码

1. fork源代码，将别人的源代码拷贝到自己的远程仓库

![1639380158307](J:\homework\Python学习笔记\Python_notes.assets\1639380158307.png)
2. 在自己的仓库进行修改代码

```shell
git checkout -d tornado
git clone https://github.com/zhangzhqiang/tornado.git
# 阅读源代码，找出bug提交
git add .
git commit -m "修改了一个源码bug"
git push origin tornado
```

3. 给源代码的作者提交修复bug申请（pull request）

#### 16.3.3 其他

##### 16.3.3.1 配置

- 项目配置文件：项目/.git/config

```shell
git config --local user.name "joker"
git config --local user.email "zq15010008824@163.com"
```

- 全局配置文件：~/.gitconfig 

```shell
git config --global user.name "joker"
git config --global user.email "zq15010008824@163.com"
```

- 系统配置文件：/etc/.gitconfig

```shell
git config --system user.name "joker"
git config --system user.email "zq15010008824@163.com"

# 注：需要由root权限
```

应用场景：

```shell
git config --local user.name "joker"
git config --local user.email "zq15010008824@163.com"

git config --local merge.tool bc3			# 给合并工具起个别名
git config --local mergetool.path "F:\Program Files\Beyond Compare 4\BCompare.exe"  # 指定安装目录
git config --local mergetool.keepBackup false		# 在合并的时候是否进行备份

git remote add origin 地址  # 默认添加在项目配置文件中
```

##### 16.3.3.2 免密登录

- URL中体现

```shell
原来的url：https://github.com/joker1-org/dbhot.git
修改的url：https://用户名:密码@github.com/joker1-org/dbhot.git

git remote add origin https://用户名:密码@github.com/joker1-org/dbhot.git
git push origin master
```

- SSH实现

```shell
# 1.生成公钥 和 私钥 （默认放在 ~/.ssh目录下，id_rsa私钥，id_rsa.pub公钥）
ssh-keygen.exe  # 生成公钥、私钥

# 2.拷贝公钥的内容，并设置到github中（头像--settings--SSH）
cat id_rsa.pub

# 3.项目中拷贝SSH链接
git remote add dbhot git@github.com:joker1-org/dbhot.git

# 4.以后使用
git push origin master
```

##### 16.3.3.3 忽略文件

让git不再管理当前目录下的某些文件，比如：用户名密码，数据库文件等

```shell
# 1.在当前目录下新建 .gitignore 文件
# 2.内容编辑参考：https://github.com/github/gitignore/blob/master/Python.gitignore
```

##### 16.3.3.4 项目管理

- issues：文档以及任务的管理
- wiki：项目文档管理

### 16.4 垃圾回收机制

引用计数器为主，标记清除和分代回收为辅 + 缓存机制

- 引用计数器
- 标记清除
- 分代回收
- 缓存机制
- Python的C源码（3.8.2版本）

#### 16.4.1 引用计数器

##### 16.4.1.1 环状双向链表 refchain

在python程序中创建的任何对象都会放在refchain链表中。

```python
name = "ike"
age = 18
hobby = ["篮球", "美女"]
```

```python
内部会创建一些数据【上一个对象、下一个对象、类型、引用个数】
name = "ike"
new = name

内部会创建一些数据【上一个对象、下一个对象、类型、引用个数、val = 18】
age = 18

内部会创建一些数据【上一个对象、下一个对象、类型、引用个数、item = 元素、元素个数】
hobby = ["篮球", "美女"]
```

![1645069079709](Python_notes.assets\1645069079709.png)

在C语言源码中如何体现每个对象中都有相同的值：PyObject结构体（封装了3个值）

有多个元素组成的对象：PyObject结构体（4个值） + ob_size

![1645070099424](J:\homework\Python学习笔记\Python_notes.assets\1645070099424.png)

##### 16.4.1.2 类型封装结构体

```python
data = 3.14

内部会创建：
	_ob_next = refchain中的上一个对象
    _ob_prev = refchain中的下以一个对象
    ob_refcnt = 1
    ob_type = float
    ob_fval = 3.14
```



![1645070191810](J:\homework\Python学习笔记\Python_notes.assets\1645070191810.png)

##### 16.4.1.3 引用计数器

```python
v1 = 3.14
v2 = 999
v3 = (1,2,3)
```

当python程序运行时，会根据数据类型的不同找到对应的结构体，根据结构体中的字段来进行创建相关的数据，然后将对象添加到refchain双向链表中。

在C源码中有两个关键的结构体：PyObject、PyVarObject

PyObject存放公共的上一个、下一个及类型和引用个数，每一个对象都有

PyVarObject存放多个元素组成的时候存在公共的值，比如int类型

每个对象中有ob_refcnt就是引用计数器，值默认为1，当有其他变量引用对象时，引用计数器就会发生变化。

- 引用

```python
a = 999
b = a
```

- 删除引用

```python
a = 999
b = a
del b  # b变量删除；b对应对象引用计数器-1
del a  # a变量删除；a对应对象引用计数器-1

# 当一个对象的引用计数器为0时，意味着没有人在使用这个对象了，这个对象就是垃圾，需要垃圾回收。
# 回收：1.对象从refchain链表移除； 2.将对象销毁，内存归还。
```

![1645074000461](J:\homework\Python学习笔记\Python_notes.assets\1645074000461.png)

##### 16.4.1.4 循环引用问题

在不重启的情况下，删除后，计数器为1，不会当成垃圾回收，那么这两个列表一直常驻在内存中，永远不会销毁，导致程序一直在运行，内存一直在消耗，时间长了内存就满了，就会产生爆栈，导致内存泄漏，如果重启，则程序终止运行，释放内存。

![1645073973255](J:\homework\Python学习笔记\Python_notes.assets\1645073973255.png)

#### 16.4.2 标记清除

目的：为了解决引用计数器循环引用的不足。

实现：在python的底层，再维护一个链表，这个链表中放可能存在循环引用的对象（列表/字典/集合/元组）。

![1645095066309](J:\homework\Python学习笔记\Python_notes.assets\1645095066309.png)

在Python内部，某种情况下触发，回去扫描 可能存在循环引用的链表中的每个元素，检查是否有循环引用，如果有则让双方的引用计数器各自减一，如果结果是0则垃圾回收。

问题：

- 某种情况：什么时候扫描？
- 可能存在循环引用的链表扫描代价大，每次扫描耗时久。

#### 16.4.3 分代回收

![1645180479470](J:\homework\Python学习笔记\Python_notes.assets\1645180479470.png)

将可能存在循环引用的对象维护成三个链表：

- 0代：0代对象个数达到700个扫描一次，扫描过程中如果是垃圾数据则回收，如果不是则上升到1代
- 1代：0代扫描10次，则1代扫描一次，1代扫描过程中如果是垃圾数据则回收，如果不是则上升到2代
- 2代：1代扫描10次，则2代扫描一次，2代扫描过程中如果是垃圾数据则回收，如果不是则上升到链表

分代回收解决了在什么时候扫描和扫描耗时久的问题。

#### 16.4.4 小结

在Python中维护了一个refchain的双向环状链表，这个链表中存储程序创建的所有对象，每种类型中对象中都有一个ob_refcnt引用计数器的值，引用个数 +1、-1，最后当引用计数器变为0时，则会进行垃圾回收（对象销毁、refchain中移除）。

但是，在Python对于那些可以有多个元素组成的对象，可能会存在循环引用的问题，为了解决这个问题python又引入了标记清除和分代回收。在其内部维护了4个链表，分别是：

- refchain：维护所有的对象
- 2代：1代扫10次，这三代专门为了解决由多个元素组成的对象
- 1代：0代扫10次
- 0代：700个

在源码的内部当达到各自的阈值时，就会触发扫描链表标记清除动作（由循环则各自 -1），因为扫描的对象比较多，通过加上0、1、2代，加上了优先级。

But，源码内部在上述的流程中提出了优化机制。

#### 16.4.5 Python缓存

##### 16.4.5.1. 池(int、字符串)

在Python中为了避免重复创建和销毁一些常见对象，会维护一个池。

```python
# 启动解释器时，python内部帮我们创建一个小数据池：-5、-4....257
v1 = 7	# 内部不会开辟内存，直接去池中获取
v2 = 9	# 内部不会开辟内存，直接去池中获取
v3 = 9	# 内部不会开辟内存，直接去池中获取
print(id(v2), id(v3))

# 超出范围则新开辟一块内存
v4 = 666
v5 = 999
```

##### 16.4.5.2 free_list机制

当一个对象的引用计数器为0时，按理说应该回收，在Python内部为了优化它，不会直接回收，而是将对象添加到free_list链表中当缓存，以后再去创建对象时，不再重新开辟内存，而是直接使用free_list。

```python
v1 = 3.14  # 开辟内存，内部存储结构体中定义那几个值，并皴法哦refchain中。
del v1  # refchain中移除，将对象添加到 free_list 中（80个），如果free_list中满了则销毁。

v9 = 99.9  # 不会重新开辟内存，去free_list中获取对象，对象内部数据初始化，再放到refchain中。
```



## 附录 注意事项

### 1.git使用

- 本地：git软件，常用的命令

  - git status
  - git add .
  - git commit -m '备注'
  - git push origin master
  - git init

- 远程：码云／github(程序员交友平台)

- 补充

  - 面试相关：

    - 1.写出你常用的git命令

    - 2.你们公司是怎么用git做开发的

      - 1.在码云或github等代码托管的网站创建自己仓库，创建完之后获取到一个仓库地址，如：https://gitee.com/python-ike/cn-ike.git

      - 2.自己写代码

      - 3.将代码提交到远程仓库

        - 初始化

          - 进入一个任意文件夹，如：j:\homework\
          - git init
          - git config 邮箱
          - git config 姓名
          - git remode add origin https://gitee.com/python-ike/cn-ike.git

          注意：至此git已经将j:\homework\管理起来了，此后本文件夹有任何的变动，git都会检测到(使用git status命令可以查看状态)

        - 代码收集并提交

          - git status
          - git add .
          - git commit -m '备注内容'
          - git push origin master 将本地j:\homework\目录同步到码云仓库

        - 修改代码或删除文件等对本地j:\homework\目录下的内容同步到码云仓库，执行－－代码收集并提交步骤

        - 如果远程有本地没有的代码，必须先执行：[可能会引发合并问题]

          - git pull origin master
          - git status
          - git add .
          - git commit -m '备注内容'
          - git push origin master

### 2.问题记录

#### 2.1 git经常遇到的问题

```python
# 大概意思是本地和远程之前的文件不一致,合并后才能上传本地新文件
F:\game_project\node_project>git push -u origin master
To https://gitee.com/cn_xxxxx/node.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://gitee.com/cn_xxxxx/node.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
# 解决办法
# 1、先拉下来，会自动合并的（不用操心）
git pull origin master
# 2、再上传
git push -u origin master
```

#### 2.2 数据迁移报错

```python
执行python manage.py makemigrations 操作报AttributeError: 'str' object has no attribute 'decode'

解决:
在python安装路径下 lib\site-packages\django\db\backends\mysql\operations.py这个脚本的第146行 在执行query = query.decode(errors=‘replace’) 这个语句时报错。

由于 python3.和Python2.在套接字返回值解码上的区别
python在bytes和str两种类型转换，所需要的函数依次是encode(),decode()
str通过encode()方法可以编码为指定的bytes。反过来，当从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法。反之，则使用encode()方法即可！

我们这边需要将decode替换成encode即可
query = query.encode(errors=‘replace’)
```

```python
D:\Luffycity\study\ORM>python manage.py makemigrations
(0.001) b'SELECT @@SQL_AUTO_IS_NULL'; args=None
(0.001) b'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED'; args=None
(0.001) b'SHOW FULL TABLES'; args=None
(0.002) b'SELECT `django_migrations`.`app`, `django_migrations`.`name` FROM `django_migrations`'; args=()
No changes detected

解决:
删除项目下的migrations文件夹下的文件,只留__init__.py文件
```

#### 2.3 pymsql字符转义报错

报错信息如下：

```python
pymysql.err.ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '%s'' at line 1")
```

解决办法：

使用pymysql.escape_string()方法

```python
search_sql = Element(SQL_PATH, 'trademark_sql')


class TrademarkSQL(TrademarkDatabase):
    """针对sql进行封装"""

    def select_data_one(self, txt='商标16047'):
        result = self.search_one(pymysql.escape_string(search_sql['查询商标授权名称'][1]), data=txt)
        print(result)
```

ymal文件：

```yaml
查询商标授权名称: "name==select count(trademark_name) from legal_trademark_test.trademark_apply_authorization where trademark_name=%s"
```

#### 2.4 配置DATABASES

报错如下：

```python
# TypeError: argument of type ‘WindowsPath’ is not iterable
# TypeError: argument 1 must be str, not WindowsPath
```

解决方法：

NAME值转换成str类型

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}
```

#### 2.5 没有添加注册APP

报错：django.template.exceptions.TemplateDoesNotExist

问题原因：

INSTALLED_APPS没有添加注册app名，所以找不到文件

解决方法：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
    'app02',
    'app03',
    'app04',
]
```

#### 2.6 django链接数据库报错

```python
django.db.utils.ProgrammingError: (1064, "You have an error in your SQL syntax;
check the manual that corresponds to your MySQL server version for the right syn
tax to use near 'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED' at line
1")
```

解决办法：

```python
# 在init文件中添加
import pymysql
pymysql.install_as_MySQLdb()

# 在配置文件中添加OPTIONS
settings.py中修改为如下内容:
DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'autotest',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'OPTIONS': {'isolation_level': None}
        }
}
```

#### 2.7 redis启动失败

报错：如下

```python
redis.exceptions.DataError: Invalid input of type: ‘dict‘. Convert to a byte, string or number first
```

对redis降版：

```python
# 将当前版本降级到2.10.6
pip3 install -U redis==2.10.6
```

成功写入数据。

而上面我之所以说是"血案",是因为我看了网上的教程说是Redis版本太高导致的之后,我就试图将Redis服务端的版本重新安装成低版本的2.10.6,但是发现并不能,最后才顿悟,应该将Python使用的Redis模块的版本降级为2.10.6(这里使用Redis模块,就类似于要在Python中操作MySQL而使用pymysql模块是一样的),而不是去动服务端的版本,无知啊,做个笔记,记录一下.

#### 2.8 ubuntu中可卸载的软件

```python
sudo apt-get -y --auto-remove purge unity unity-2d*
sudo apt-get -y purge empathy
sudo apt-get -y purge nautilus-sendto-empathy
sudo apt-get -y purge empathy-common #即时通讯
sudo apt-get -y purge thunderbird* #邮件
sudo apt-get -y purge gwibber* #微博
sudo apt-get autoremove gcalctool #计算器
sudo apt-get -y purge gnome-power-manager #电源统计
sudo apt-get -y purge ubuntuone* #Ubuntu One
sudo apt-get -y purge deja-dup #备份
sudo apt-get -y purge bluez* #卸载蓝牙
sudo apt-get -y purge simple-scan #扫描
sudo apt-get -y purge hplip* #打印
sudo apt-get -y purge printer-driver* #打印驱动
sudo apt-get -y purge rhythmbox* #音乐播放
sudo apt-get -y purge gedit* #文本编辑
sudo apt-get -y purge libreoffice* #办公套件
sudo apt-get -y purge gnome-orca #屏幕阅读
sudo apt-get -y purge onboard #屏幕键盘
sudo apt-get -y purge mahjongg #对对碰
sudo apt-get -y purge aisleriot #纸牌王
sudo apt-get -y purge gnome-sudoku #数独
sudo apt-get -y purge gnomine #扫雷
sudo apt-get -y purge wodim #命令刻碟
```

#### 2.9 Ubuntu连不上网

1. 检车VM服务是否开启
2. 虚拟机网络编辑器还原默认设置
3. 网络适配器选择桥接或NAT模式

4. 以上办法无法解决，检查ubuntu网络配置：突然没网的情况

   1. 查看ubuntu网络设置

   ```python
   cd /var/lib/NetworkManager
   vim NetworkManager.state
   ```

   2. 关闭网络总开关

   ```python
   sudo service network-manager stop
   ```

   3. 修改网络配置

   ```python
   [main]
   NetworkingEnabled=true
   WirelessEnabled=true
   WWANEnabled=true
   ```

   4. 开启网络开关

   ```python
   sudo service network-manager start
   ```

### 3. 面试记录

#### 3.1 可hash的数据类型

hash值得计算过程是依据这个值的一些特征计算的，这就要求hash值必须固定，因此hash的值必须是不可变的。 

| 不可变类型 | 可变类型 |
| ---------- | -------- |
| 数字       |          |
| 字符串     | 列表     |
| 元组       |          |
| 字典的key  |          |

#### 3.2 sort 与sorted的区别

sort()与sorted()的不同在于，sort是在原位重新排列列表，而sorted()是产生一个新的列表。

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

**list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作**。

示例一：

```python
>>> a=[1,2,5,3,9,4,6,8,7,0,12]
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
>>> a=[1,2,5,3,9,4,6,8,7,0,12]
>>> a
[1, 2, 5, 3, 9, 4, 6, 8, 7, 0, 12]
>>> sorted(a)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
>>> a
[1, 2, 5, 3, 9, 4, 6, 8, 7, 0, 12]

# 区别：
# 对于一个无序的列表a，调用a.sort()，对a进行排序后返回a，sort()函数修改待排序的列表内容。
# 而对于同样一个无序的列表a，调用sorted(a)，对a进行排序后返回一个新的列表，而对a不产生影响
```

示例二：

```python
>>> list1=[(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]
>>> list1.sort()
>>> list1
[(2, 'Mike', 22), (5, 'Lucy', 19), (8, 'Logan', 20)]

>>> list1=[(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]
>>> sorted(list1)
[(2, 'Mike', 22), (5, 'Lucy', 19), (8, 'Logan', 20)]
>>> list1
[(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]

# 小结：
# 由示例可以看出，当列表由list（或者tuple）组成时，默认情况下，sort和sorted都会根据list[0]（或者tuple[0]）作为排序的key，进行排序。
# 以上都是默认的排序方式，我们可以编写代码控制两个函数的排序行为。主要有三种方式：基于key函数；基于cmp函数和基于reverse函数
```

基于key函数排序

```python
>>> list1=[(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]
>>> list1.sort(key=lambda x:x[2])
>>> list1
[(5, 'Lucy', 19), (8, 'Logan', 20), (2, 'Mike', 22)]

>>> list1=[(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]
>>> sorted(list1, key=lambda x:x[2])
[(5, 'Lucy', 19), (8, 'Logan', 20), (2, 'Mike', 22)]
>>> list1
[(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]
```

 基于reverse函数

```python
>>> a=[1,2,5,3,9,4,6,8,7,0,12]
>>> a.sort(reverse=False)
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12]

>>> a=[1,2,5,3,9,4,6,8,7,0,12]
>>> a.sort(reverse=True)
>>> a
[12, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> a.sort(reverse=True)

# 小结：reverse=False为升序排序(默认)；reverse=True为降序排序
```

#### 3.3 类变量、成员变量、静态变量、局部变量概念

首先，Python语言并不支持静态变量。因为Python是动态语言，不存在完全静态的变量。 
Python中，静态成员变量称为类变量，非静态成员变量称为实例变量，成员变量。

**基本概念：**

<font color="red"> 类变量：</font> 类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。类变量在整个实例化的对象中是公用的。 

<font color="red">实例变量：</font>  定义在方法中的变量，用 self 绑定到实例上，只作用于当前实例的类。 

```python
class TestClass(object):
    val1 = 100

    def __init__(self):
        self.val2 = 200

    def func(self, val=400):
        val3 = 300
        self.val4 = val
        self.val5 = 500


if __name__ == '__main__':
    inst = TestClass()

    print(TestClass.val1)
    print(inst.val1)
    print(TestClass.val2)  # 会报错，类不能访问成员变量
    print(inst.val2)
    print(inst.val3)  # 会报错
    print(inst.val4)  # 会报错
    print(inst.val5)  # 会报错
```

```powershell

val1 是类变量，可以由类名直接调用，也可以由对象来调用；
val2 是成员变量，可以由类的对象来调用，这里可以看出成员变量一定是以self.的形式给出的，因为self的含义就是代表实例对象；如果__init__内的变量没有加self，那就变成一个__init__的局部变量；
val3 不是成员变量，它只是函数func内部的局部变量；
val4和val5 是成员变量，但并没有初始化，所以这里会报错
=======
#### 2.10 上传github报错如下

**报错1：**

​```powershell
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/python-pra/tongchengre.git/
```

解决方法

```powershell
# 1.执行如下命令
git config http.sslVerify "false"
有报错提示时执行  git init 再执行一遍命令

# 2.删除github凭证
# 3.创建个人访问令牌
# 4.清除缓存
git credential-manager uninstall

# 5.再执行clone命令，密码输入生成的tonken令牌登录
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

参考博客：https://blog.csdn.net/m0_46332820/article/details/119708248
```

![1639373585717](J:\homework\Python学习笔记\Python_notes.assets\1639373585717.png)

**报错2：**

![1639379354254](J:\homework\Python学习笔记\Python_notes.assets\1639379354254.png)

```powershell
# 1.检查是否设置review代码，如果设置删除
# 2.再执行以下命令，上传
git add .
git commit -m "提交的信息"

git remote add origin 远程仓库地址

git push -u origin 分支名
>>>>>>> dev
```

