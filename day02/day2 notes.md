# Day2 notes

## 1.今日概要

1.while循环

2.字符串格式化

3.运算符

4.编码

5.博客&git

## 2.内容回顾

1.计算机基础

2.安装解释器

- python2
- python3

3.语法

- print/input

- 整型/字符串/布尔值

- 条件语句

- and运算符

- 变量

- 练习

  ```python
  评分规则:
  	>=90 A
  	>=80 B
  	>=70 C
  	其他  D
  course = input('请输入成绩')
  course = int(course)
  if course >= 90:
  	print('A')
  elif course >= 80:
  	print('B')
  elif course >= 70:
  	print('C')
  else:
  	print('D')
  ```

- 补充

  ```python
  # 10086代码练习if嵌套
  message = """10086服务
  1.宽带服务;
  2.业务办理;
  3.人工服务;
  4.请挂机;"""
  print(message)
  
  number = input('请输入要选择的服务:').strip()
  number = int(number)
  if number == 1:
      print('宽带服务')
  elif number == 2:
      msg = """"
      1.话费查询
      2.流量查询
      3.增值业务
      """
      print(msg)
      course = input('请输入要办理的业务:').strip()
      course = int(course)
      if course == 1:
          print('话费查询')
      elif course == 2:
          print('流量查询')
      elif course == 3:
          print('增值业务')
      else:
          print('重新输入')
  elif number == 3:
      print('人工服务')
  elif number == 4:
      print('请挂机')
  else:
      print('输入错误')
  ```

## 3.今日内容

### ⑴.循环语句

1.循环打印"人生苦短,我用Python'"

```python
while True:
	print('人生苦短,我用Python!')
# 无限循环
```

2.通过循环,让count每次循环+1

```python
count = 1
while count < 11:
    print(count)
    count += 1
```

3.通过循环,打印1-10

```python
count = 1
while count < 11:
    if count != 7:
        print(count)
    count += 1
```

4.通过循环,打印1-10,但不打印7

```python
count = 1
while count <11:
	if count != 7:
		print(count)
	count += 1
```

5.break

```python
count = 1
while True:
    print(count)
    if count == 10:
        break  # break 终止当前循环
    count += 1
print('完了')
```

6.continue

```python
count = 1
while count <= 10:
    print(count)
    continue  # 本次循环遇到continue,则不再继续往下走,而是回到while条件位置;
count += 1
```

7.continue打印1-10,不打印7

```
count = 1
while count <= 10:
    if count == 7:  # 循环到7,不再往下走,回到while条件位置继续执行.
        count += 1
        continue
    print(count)
    count += 1
```

8.while else结构,while条件不满足,则执行else中的内容,break终止循环则不执行else

```python
count = 1
while count <= 10:
    print(count)
    count += 1
else:
    print('已结束')
```

### ⑵.字符串格式化

1.%s,占位符,指的是字符串

2.%d,占位符,指的是数字

3.%%,在需求中要求有%符号,在代码中要用2个%来转义

```python
name = 'alex'
print('%s的手机电量是100%%' % name)
```

###  ⑶.运算符

算数运算: +  -  *  /  %(取模)  //(整除)  **(次方)

```
# 取余数
value = 11 % 3
print(value)
# 取整数
value = 11 // 3
print(value)
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

比较运算:  == (比较)  !=(不等于)   >   <   >=  <=

赋值运算:  +=  -=  *=  /=  //=  %=  **  = 类比于算数预算的赋值,方便书写,减少工作量

```
count = 1
while count <= 100:
	print(count)
	count += 1 # count = count +1
```

逻辑运算: 

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
  # 注意:""在and中为假
  # 示例:
      v1 = 1 and 9
      v2 = 1 and 0
      v3 = 0 and 7
      v4 = 0 and ''
      v5 = 1 and 0 and 9
  ```

  - and和or结合

  ```python
  # 先看and后看or
  v1 = 1 and 9 or 0 and 6
  ```

  总结:优先级在没有()的情况下,not优先级最高,and优先级高于or,优先级的顺序为

  ```python
  # () not > and > or
  ```

### ⑷.编码

- 编码补充

  - ascii
  - unicode:万国码 可以统计世界上的所有语言,一般用于内存计算,最少2个字节,最多4个字节
    - ecs2    2**16
    - ecs4    2**32
  - utf-8,中文用3个字节.
  - utf-16
  - gbk,中文用2个字节.
  - gb2312,中文用2个字节.

- 单位换算

  ```python
   1byte = 8 bit 任何编码 ,1个字节等于8个数字,数字指基本的二进制数字
  
  ​ 1KB = 1024byte
  
  ​ 1MB = 1024KB
  
  ​ 1GB = 1024 MB
  
  ​ 1TB = 1024 GB
  
  ​ 1PB = 1024 TB
  ```

  

