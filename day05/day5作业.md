# Day5作业

1.第1题

```python
'''
请将列表中的每个元素通过 "_" 链接起来。
'''
users = ['李少奇', '李启航', '渣渣辉']
print('_'.join(users))
```

2.第2题

```python
'''
请将列表中的每个元素通过 "_" 链接起来。
'''
users = ['李少奇', '李启航', 666, '渣渣辉']
for i in range(0, len(users)):
    users[i] = str(users[i])
print('_'.join(users))
```

3.第3题

```python
'''
请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。'''
v1 = (11, 22, 33)
v2 = [44, 55, 66]
v2.extend(v1)
print(v2)

```

4.第4题

```python
'''
请将元组 v1 = (11,22,33,44,55,66,77,88,99) 中的所有偶数索引位置的元素 追加到列表 v2 = [44,55,66] 中。
'''
v1 = (11, 22, 33, 44, 55, 66, 77, 88, 99)
v2 = [44, 55, 66]
for i in range(0, len(v1), 2):
    v2.append(v1[i])
print(v2)
```

5.第5题

```python
'''将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
'''
key_list = []
value_list = []
info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for k, v in info.items():
    key_list.append(k)
    value_list.append(v)
print(key_list, value_list)
```

6.第6题

```python
'''
字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}

a. 请循环输出所有的key
b. 请循环输出所有的value
c. 请循环输出所有的key和value
d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典'''

dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}

# a. 请循环输出所有的key
for k in dic.keys():
    print(k)

# b. 请循环输出所有的value
for v in dic.values():
    print(v)

# c. 请循环输出所有的key和value
for k, v in dic.items():
    print(k, v)

# d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic['k4'] = 'v4'
print(dic)

# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic['k1'] = 'alex'
print(dic)

# f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
dic['k3'].append(44)
print(dic)

# g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic['k3'].insert(0, 18)
print(dic)
```

7.第7题

```python
'''请循环打印k2对应的值中的每个元素。
'''
info = {
    'k1': 'v1',
    'k2': [('alex'), ('wupeiqi'), ('oldboy')],
}
for v in info['k2']:
    print(v)

```

8.第8题

```python
'''
有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}
'''
a = "k: 1|k1:2|k2:3 |k3 :4"
a1 = a.split('|')
dic = {}
for i in a1:
    k, v = i.split(':')
    k1 = k.strip()
    v1 = v.strip()
    dic[k1] = v1
print(dic)
```

9.第9题

```python
'''写代码

"""
有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。

result = {'k1':[],'k2':[]}'''
li= [11,22,33,44,55,66,77,88,99,90]
dic = {}
lis = []
lis1 = []
for i in range(0, len(li)):
    if li[i] > 66:
        lis.append(li[i])
    elif li[i] < 66 :
        lis1.append(li[i])
dic['k1'] = lis
dic['k2'] = lis1
print(dic)
```

10.第10题

```python
'''输出商品列表，用户输入序号，显示用户选中的商品

"""
商品列表：
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]
要求:
1：页面显示 序号 + 商品名称 + 商品价格，如：
    1 电脑 1999 
    2 鼠标 10
...
2：用户输入选择的商品序号，然后打印商品名称及商品价格
3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。
"""'''
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
count = 1
for i in goods:
    print('序号%d' % count, '商品名称:【%s】' % (i['name']), '商品价格:【%s】:' % (i['price']))
    count += 1
while True:
    choice = input('请选择商品序号,退出请输入[Q/q]:').strip()
    if choice.isdigit():
        choice = int(choice)
        if choice <= len(goods):
            print('您选择的商品是[%s],价格是[%d]' % (goods[choice-1]['name'], goods[choice-1]['price']))
    elif choice == 'Q' or choice == 'q':
        exit('欢迎下次光临')
    else:
        print('输入错误')
```

11.第11题

```python
'''看代码写结果
'''
v = {}
for index in range(10):
    v['users'] = index
print(v)

# 结果:{'users': 9}
```

