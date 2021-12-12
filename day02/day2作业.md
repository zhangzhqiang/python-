# Day2作业

1.第一题

```python
# 猜数字，设定一个理想数字比如：
# 66，让用户输入数字，如果比66大，则显示猜测的结果大了；
# 如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确，然后退出循环。

number = 66
while True:
    num = input('请输入数字:')
    num = int(num)
    if num > number:
        print('大了')
    elif num < number:
        print('小了')
    else:
        print('猜对了')
        break
```

2.第二题

```python
# 在上一题的基础，设置：给用户三次猜测机会，如果三次之内猜测对了，
# 则显示猜测正确，退出循环，如果三次之内没有猜测正确，
# 则自动退出循环，并显示‘大笨蛋’。

number = 66
count = 0
while count < 3:
    num = input('请输入数字:')
    num = int(num)
    if num > number:
        print('大了')
    elif num < number:
        print('小了')
    else:
        print('猜对了')
        break
    count += 1
else:
    print('大笨蛋')
```

3.第三题

```python
# 使用两种方法实现输出 1 2 3 4 5 6 8 9 10 。
# 第一种方法
count = 0
while count <= 10:
    if count != 7:
        print(count)
    count += 1
# 第二种方法
count = 0
while count <= 9:
    count += 1
    if count == 7:
        continue
    print(count)

# 第三种方法
count = 0
while count <= 10:
    if count == 7:
        count += 1
    print(count)
    count += 1
```

4.第四题

```python
# 求1-100的所有数的和
# 第一种方法
count = 0
total = 0
while count < 100:
    count += 1
    total += count
print(total)
# 第二种方法
print(sum(i for i in range(0, 101)))
```

5.第五题

```python
# 输出 1-100 内的所有奇数
# 第一种
count = 0
while count < 100:
    if count % 2 == 1:
        print(count)
    count += 1
# 第二种
count = 1
while count <100:
    print(count)
    count += 2
```

6.第六题

```python
# 输出 1-100 内的所有偶数
# 第一种
count = 0
while count < 100:
    if count % 2 == 0:
        print(count)
    count += 1
# 第二种
count = 0
while count < 100:
    print(count)
    count += 2
```

7.第七题

```python
# 求1-2+3-4+5 ... 99的所有数的和
count = 0
total = 0
while count < 100:
    if count % 2 == 0:
        total -= count
    else:
        total += count
    count += 1
print(total)
```

8.第八题

```python
# ⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数
# （提示：使⽤字符串格式化）⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）

count = 2
user = 'ike'
pwd = '123456'
while count > -1:
    username = input('输入账号:')
    password = input('输入密码:')
    if username == user and pwd == password:
        print('登录成功')
        break
    else:
        print('账号或密码错误,剩余 %s 机会' % count)
    count -= 1
```

9.第九题

```python
# 简述ASCII、Unicode、utf-8编码
ASCII:只支持英文,一个字符占1个字节,8位
Unicode:万国码.一个字符最少占2个字节,最多占4个字节,16-32位
UTF-8:unicode的压缩版,根据不同的数字编写成1-6个字节,一个最少占1个字节,汉字用3个字节

```

10.第10题

```python
3 简述位和字节的关系？
一个字节等于8位(bit)
```

11.第11题

```python
# 猜年龄游戏
sex = 18
while True:
    num = input('请输入年龄:')
    num = int(num)
    if num == sex:
        print('猜对了')
        break
    elif num < sex:
        print('猜小了')
    else:
        print('猜大了')

```

12.第12题

```python
# 猜年龄游戏升级版 要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，
# 就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，
# 如果回答N，就退出程序，如何猜对了，就直接退出。
count = 0
number = 18
while count < 3:
    num = input('请输入年龄:')
    num = int(num)
    if num == number:
        print('猜对了')
        break
    else:
        print('猜错了,还想继续玩(Y/N)?')
        chioce = input('输入(Y/N):')
        if chioce == 'Y':
            count = 0
        elif chioce == 'N':
            break
        else:
            print('结束')
    count += 1
```

13.第13题

```python
# 判断下列逻辑语句的True,False
1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6  True
not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6 False
```

14.第14题

```python
# 求出下列逻辑语句的值
8 or 3 and 4 or 2 and 0 or 9 and 7  8
0 or 2 and 3 and 4 or 6 and 0 or 3  4

```

15.掉15题

```python
# 下列结果是什么？
6 or 2 > 1 6
3 or 2 > 1 3
0 or 5 < 4 false
5 < 4 or 3 3
2 > 1 or 6 true
3 and 2 > 1 true
0 and 3 > 1 0
2 > 1 and 3 3
3 > 1 and 0 0
3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2 2
```

