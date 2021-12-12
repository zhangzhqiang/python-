# Day9 作业

1.第一题

```python
'''写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回。'''

# 方式一:
lis = []
def count_number(data):
    for i in range(0, len(data)):
        if i % 2 == 1:
            lis.append(data[i])
    return lis
res = count_number([1, 2, 3, 6, 5, 89, 6])
print(res)

# 方式二:
def count_num(data):
    lis = []
    for i in range(1, len(data), 2):
        lis.append(data[i])
    return lis
res = count_num([1, 2, 3, 6, 5, 89, 6])
print(res)

# 方式三:
def count_num(data):
    val = data[1::2]
    return val
res = count_num((1, 2, 3, 4, 5, 6, 7))
print(res)
```

2.第二题

```python
'''写函数，判断用户传入的一个对象（字符串或列表或元组任意）长度是否大于5，并返回真假。'''


# 方式一:
def num(data):
    if len(data) > 5:
        return True
    return False
res = num([1, 2, 3, 4, ])
print(res)

# 方式二:
def num(data):
    return True if len(data) > 5 else False
print(num([1, 2, 3, 4, 5, 5]))
```

3.第三题

```python
'''写函数，接收两个数字参数，返回比较大的那个数字。'''
def numbeer(v1, v2):
    return v1 if v1 > v2 else v2
res = numbeer(8, 99)
print(res)
```

4.第四题

```python
'''写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，
然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容根据"*"拼接起来并追加到一个student_msg文件中。'''

def stu_info(data):
    with open('student_msg.txt', 'a', encoding='utf-8')as f:
        f.write(f1)

username = input('username:')
sex = input('sex:')
age = input('age:')
edu = input('education:')
lis = [username, sex, age, edu]
f1 = '*'.join(lis)
stu_info(f1)
```

5.第五题

```python
'''写函数，在函数内部生成如下规则的列表 [1,1,2,3,5,8,13,21,34,55…]（斐波那契数列），
并返回。 注意：函数可接收一个参数用于指定列表中元素最大不可以超过的范围。'''

def func(x):
    lis = []
    for i in range(x):
        if i == 0 or i == 1:
            lis.append(i)
        else:
            lis.append(lis[i - 2] + lis[i - 1])
    return lis

print(func(9))
```

6.第六题

```python
'''写函数，验证用户名在文件 data.txt 中是否存在，如果存在则返回True，否则返回False。（函数有一个参数，用于接收用户输入的用户名）

data.txt文件格式如下：

1|alex|123123
2|eric|rwerwe
3|wupeiqi|pppp'''


def name(data):
    with open('data.txt', 'r', encoding='utf-8')as f:
        for item in f:
            f1 = item.strip().split('|')
            return True if data in f1 else False


num = input('username:').strip()
print(name(num))
```

