# Day4作业

1.第一题

```
# 简述解释型语言和编译型语言的区别？
解释型语言:代码写完后,通过解释器从上到下逐行执行,边解释边执行.比如:Python/Ruby/PHP等
编译型语言:代码写完后,通过编译器会形成一个文件,然后交到计算机执行.比如:Java/C/C++/C#/GO等
```

2.第二题

```
# 列举你了解的Python的数据类型？
str/int/bool/list/tuple
```

3.第三题

```python
写代码，有如下列表，按照要求实现每一个功能。

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]

# 1.计算列表的长度并输出
print(len(li))

# 2.请通过步长获取索引为偶数的所有值，并打印出获取后的列表
print(li[::2])

# 3.列表中追加元素"seven",并输出添加后的列表
li.append("seven")
print(li)

# 4.请在列表的第1个位置插入元素"Tony",并输出添加后的列表
li.insert(0, "Tony")
print(li)

# 5.请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
li[2] = "Kelly"
print(li)

# 6.请将列表的第3个位置的值改成 "太白"，并输出修改后的列表
li[3] = "太白"
print(li)

# 7.请将列表 l2=[1,"a",3,4,"heart"] 的每一个元素追加到列表li中，并输出添加后的列表
方式一
l2 = [1, "a", 3, 4, "heart"]
li.extend(l2)
print(li)
方式二
for i in l2:
    li.append(i)
print(li)

# 8.请将字符串 s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
s = "qwert"
li.extend(s)
print(li)

# 9.请删除列表中的元素"ritian",并输出删除后的列表
li.remove('ritian')
print(li)

# 10.请删除列表中的第2个元素，并输出删除元素后的列表
li.pop(3)
print(li)

# 11.请删除列表中的第2至第4个元素，并输出删除元素后的列表
del li[2:]
print(li)
```

4.第四题

```python
# 请用三种方法实现字符串反转 name = "小黑半夜三点在被窝玩愤怒的小鸟"（步长、while、for）
name = "小黑半夜三点在被窝玩愤怒的小鸟"
# 方式一:
print(name[::-1])

# 方式二:
value = ""
index = len(name) - 1
while index >= 0:
    val = name[index]
    value += val
    index -= 1
print(value)

# 方式三:
value = ""
index = len(name)-1
for i in name:
    value += name[index]
    index -= 1
print(value)

# 方式四:
index = len(name) - 1
value = ""
for item in range(index, -1, -1):
    value += name[item]
print(value)
```

5.第五题

```python
'''
写代码，有如下列表，利用切片实现每一个功能
'''
li = [1, 3, 2, "a", 4, "b", 5,"c"]
# 1.通过对li列表的切片形成新的列表 [1,3,2]
print(li[0:3])

# 2.通过对li列表的切片形成新的列表 ["a",4,"b"]
print(li[3:-2])

# 3.通过对li列表的切片形成新的列表 [1,2,4,5]
print(li[::2])

# 4.通过对li列表的切片形成新的列表 [3,"a","b"]
print(li[1:-1:2])

# 通过对li列表的切片形成新的列表 [3,"a","b","c"]
print(li[1::2])

# 通过对li列表的切片形成新的列表 ["c"]
print(li[-1:])

# 通过对li列表的切片形成新的列表 ["b","a",3]
print(li[-3::-2])
```

6.第六题

```python
'''
请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
0 武沛齐
1 景女神
2 肖大侠
'''
users = ["武沛齐","景女神","肖大侠"]
for i in range(0, len(users)):
    print(i, users[i])
```

7.第七题

```python
'''
请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：

1 武沛齐
2 景女神
3 肖大侠
'''
users = ["武沛齐","景女神","肖大侠"]
count = 0
for i in users:
    count += 1
    print(count, i)
```

8.第八题

```python
'''
写代码，有如下列表，按照要求实现每一个功能。
'''
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]

# 1.将列表lis中的"k"变成大写，并打印列表。
lis[2].upper()
print(lis)

# 2.将列表中的数字3变成字符串"100"
lis[1] = '100'
print(lis)

# 3.将列表中的字符串"tt"变成数字 101
lis[3][2][1] = 101
print(lis)

# 4.在 "qwe"前面插入字符串："火车头"
lis[3].insert(0, '火车头')
print(lis)
```

9.第九题

```python
'''
写代码实现以下功能
如有变量 googs = ['汽车','飞机','火箭'] 提示用户可供选择的商品：
0,汽车
1,飞机
2,火箭
用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
'''
googs = ['汽车', '飞机', '火箭']
for i in range(0, len(googs)):
    print(i, googs[i])
chioce = input("请输入商品序号:")
chioce = int(chioce)
print("您选择的商品是 %s" % (googs[chioce],))

```

10.第10题

```python
'''
请用代码实现

li = "alex"
利用下划线将列表的每一个元素拼接成字符串"a_l_e_x"
'''
# li = 'alex'
# print('_'.join(li))
```

11.第11题

```python
# 利用for循环和range找出 0 ~ 100 以内所有的偶数，并追加到一个列表。
lis = []
for i in range(0, 101):
    if i % 2 == 0:
        lis.append(i)
print(lis)
```

12.第12题

```python
'''
利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
'''
lis = []
for i in range(0, 51):
    if i % 3 == 0:
        lis.append(i)
print(lis)
```

13.第13题

```python
'''
利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：

[48,45,42...]'''
lis = []
for i in range(0, 51):
    if i % 3 == 0:
        lis.insert(0, i)
print(lis)
```

14.第14题

```python
'''
查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。

li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]'''

li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
lis = []
for item in li:
    item.strip()
    if item.startswith('a'):
        lis.append(item)
print(lis)
```

15.第15题

```python
'''
判断是否可以实现，如果可以请写代码实现。
"'''
li = ["alex", [11, 22, (88, 99, 100,), 33], "WuSir", ("ritian", "barry",), "wenzhou"]
# 1.请将 "WuSir" 修改成 "武沛齐"
# li[2] = "武沛齐"
# print(li)

# 2.请将 ("ritian", "barry",) 修改为 ['日天','日地']
# li[3] = ['日天', '日地']
# print(li)

# 3.请将 88 修改为 87
# li[1][0] = 87
# print(li)

# 4.请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "文周
# val = li.pop(-1)
# li.insert(0, val)
# print(li)
```

16.第16题

```python
'''
写代码实现以下功能
如有变量 googs = ['汽车','飞机','火箭'] 提示用户可供选择的商品：
1,汽车
2,飞机
3,火箭
用户输入索引后，将指定商品的内容拼接打印，如：用户输入1，则打印 您选择的商品是汽车。
'''
googs = ['汽车','飞机','火箭']

for i in range(0, len(googs)):
    print(i+1, googs[i])
choice = input('请选择商品:')
choice = int(choice)-1
print('您选择的商品是%s' % googs[choice])
```

17.第17题

```python
# 17.字符串数字相加 content = "5 + 99+7+  2+ uu + 7y"
content = "5 + 99+7+  2+ uu + 7y"
total = 0
con = content.split('+')
for i in con:
    new_i = i.strip()
    if new_i.isdigit():
        new_i = int(new_i)
        total += new_i
print(total)
```

