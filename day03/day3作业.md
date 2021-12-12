# Day3作业

1.第一题

```python
'''
有变量name = "aleX leNb " 完成如下操作：
'''
name = "aleX leNb "
# 1.移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip())
# 2.判断 name 变量是否以 "al" 开头,并输出结果（用切片）
if name[:2] in name:
    print(name[:2])
else:
    print('否')
# 3.将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
print(name.replace('l', 'p'))
# 4.将name变量对应的值中的第一个"l"替换成"p",并输出结果
print(name.replace('l', 'p', 1))
# 5.将 name 变量对应的值根据 所有的"l" 分割,并输出结果
print(name.split('l'))
# 6.将name变量对应的值根据第一个"l"分割,并输出结果
print(name.split('l', 1))
# 7.将 name 变量对应的值变大写,并输出结果
print(name.upper())
# 8.将 name 变量对应的值变小写,并输出结果
print(name.lower())
# 9.请输出 name 变量对应的值的第 2 个字符?
print(name[1])
# 10.请输出 name 变量对应的值的前 3 个字符?
print(name[:3])
# 11.请输出 name 变量对应的值的后 2 个字符?
print(name[-2:])
```

2.第二题

```python
'''
有字符串s = "123a4b5c"
'''
s = "123a4b5c"
# 1.通过对s切片形成新的字符串 "123"
print(s[:3])
# 2.通过对s切片形成新的字符串 "a4b"
print(s[3:6])
# 3.通过对s切片形成字符串s5,s5 = "c"
s5 = s[-1]
print(s5)
# 4.通过对s切片形成字符串s6,s6 = "ba2"
s6 = s[-3] + s[3] + s[1]
print(s6)
```

3.第三题

```python
# 使用while循环字符串 s="asdfer" 中每个元素。
s = "asdfer"
index = 0
while True:
    if index == len(s):
        break
    print(s[index])
    index += 1
```

4.第四题

```python
# 使用while循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
s = "321"
index = 0
while index < len(s):
    print('倒计时%s秒' % s[index])
    index += 1
else:
    print('出发')
```

5.第五题

```python
# 实现一个整数加法计算器(两个数相加)：
# 如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9（含空白），然后进行分割转换最终进行整数的计算得到结果。
while True:
    content = input('请输入数字:').strip()
    new_content = content.split('+')
    con1 = int(new_content[0])
    con2 = int(new_content[1])
    print(con1 + con2)
```

6.第六题

```python
# 计算用户输入的内容中有几个 h 字符？
# 如：content = input("请输入内容：") # 如fhdal234slfh98769fjdla
total = 0
index = 0
content = input('请输入内容:').strip()
while True:
    if content[index] == 'h':
        total += 1
    index += 1
    if index == len(content):
        break
print(total)
```

7.第七题

```python
# 计算用户输入的内容中有几个 h 或 H 字符？
# 如：content = input("请输入内容：") # 如fhdal234slfH9H769fjdla
index = 0
total = 0
content = input('请输入内容:').strip()
while True:
    if content[index] == 'h' or content[index] == 'H':
        total += 1
    index += 1
    if index == len(content):
        break
print(total)

```

8.第八题

```python
# 使用while循环分别正向和反向对字符串
# message = "伤情最是晚凉天，憔悴厮人不堪言。" 进行打印。
message = "伤情最是晚凉天，憔悴厮人不堪言。"
msg = len(message)
index = 0
total = ""
while True:
    total = total + message[index]
    index += 1
    if index == msg:
        index -= 1
        break
print(total)
total1 = ''
while True:
    total1 = total1 + message[index]
    index -= 1
    if index < 0:
        break
print(total1)

# print(message)
# print(message[::-1])
```

9.第九题

```python
# 获取用户输入的内容中 前4个字符中 有几个 A ？
# 如：content = input("请输入内容：") # 如fAdal234slfH9H769fjdla
content = input("请输入内容：").strip()
index = 0
total = 0
new_con = content[:4]
while True:
    if new_con[index] == 'A':
        total += 1
    index += 1
    if index == len(new_con):
        break
print(total)
```

10.第10题

```python
# 获取用户输入的内容，并计算前四位"l"出现几次,并输出结果。
content = input('请输入内容:').strip()
new_con = content[:4]
index = 0
total = 0
while True:
    if new_con[index] == 'l':
        total += 1
    index += 1
    if index == len(new_con):
        break
print(new_con)
print(total)

```

11.第11题

```python
# 获取用户两次输入的内容，并将所有的数据获取并进行相加
num1 = input("请输入：")  # asdfd123sf2312
num2 = input("请输入：")  # a12dfd183sf23
num11 = ''
num22 = ''
index = 0
while True:
    if num1[index].isdigit():
        num11 += num1[index]
    index += 1
    if index == len(num1):
        break

index = 0
while True:
    if num2[index].isdigit():
        num22 += num2[index]
    index += 1
    if index == len(num2):
        break
print(num11)
print(num22)
print(int(num11) + int(num22))
```

