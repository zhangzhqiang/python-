# Day7 作业

1.第一题

```python
'''
看代码写结果

v1 = [1,2,3,4,5]
v2 = [v1,v1,v1]

v1.append(6)
print(v1)
print(v2)'''
# [1,2,3,4,5,6]
# [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
```

2.第二题

```python
'''看代码写结果

v1 = [1,2,3,4,5]
v2 = [v1,v1,v1]

v2[1][0] = 111
v2[2][0] = 222
print(v1)
print(v2)'''
# [222, 2, 3, 4, 5]
# [[222, 2, 3, 4, 5], [222, 2, 3, 4, 5], [222, 2, 3, 4, 5]]
```

3.第三题

```python
'''看代码写结果，并解释每一步的流程。

v1 = [1,2,3,4,5,6,7,8,9]
v2 = {}

for item in v1:  # 遍历k1中的元素
    if item < 6:  # 如果元素小于6
        continue  # 跳出本次循环,进入到下次循环
    if 'k1' in v2:  # 如果k1 在 v2中
        v2['k1'].append(item)  # k1键增加值
    else:  # 如果不存在
        v2['k1'] = [item]  # k1的值就等于元素
print(v2)'''
# {'k1': [6, 7, 8, 9]}
```

4.第四题

```python
'''简述深浅拷贝？'''
# 浅拷贝:只拷贝元素的第一层
# 深拷贝: 每一个可变的元素都会拷贝

```

5.第五题

```python
'''看代码写结果

import copy

v1 = "alex"
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)

print(v1 is v2)
print(v1 is v3)'''
# True  True
```

6.第六题

```python
'''看代码写结果

import copy

v1 = [1, 2, 3, 4, 5]
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)

print(v1 is v2)
print(v1 is v3)'''
# False  False
```

7.第七题

```python
'''看代码写结果

import copy

v1 = [1, 2, 3, 4, 5]

v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)

print(v1[0] is v2[0])
print(v1[0] is v3[0])
print(v2[0] is v3[0])'''
# True  True True

```

8.第八题

```python
'''看代码写结果

import copy

v1 = [1,2,3,4,5]

v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)

print(v1[0] is v2[0])
print(v1[0] is v3[0])
print(v2[0] is v3[0])'''
# True  True True
```

9.第九题

```python
'''看代码写结果

import copy

v1 = [1, 2, 3, {"name": '武沛齐', "numbers": [7, 77, 88]}, 4, 5]

v2 = copy.copy(v1)

print(v1 is v2)

print(v1[0] is v2[0])
print(v1[3] is v2[3])

print(v1[3]['name'] is v2[3]['name'])
print(v1[3]['numbers'] is v2[3]['numbers'])
print(v1[3]['numbers'][1] is v2[3]['numbers'][1])'''
# False True True True True True
```

10.第10题

```python
'''看代码写结果

import copy

v1 = [1, 2, 3, {"name": '武沛齐', "numbers": [7, 77, 88]}, 4, 5]

v2 = copy.deepcopy(v1)

print(v1 is v2)

print(v1[0] is v2[0])
print(v1[3] is v2[3])

print(v1[3]['name'] is v2[3]['name'])
print(v1[3]['numbers'] is v2[3]['numbers'])
print(v1[3]['numbers'][1] is v2[3]['numbers'][1])'''
# False True False True False True
```

11.第11题

```python
'''简述文件操作的打开模式'''
# r/r+/rb/w/w+/wb/a/a+/ab

```

12.第12题

```python
'''请将info中的值使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。

info = ['骗子，','不是','说'，'只有',"10",'个题吗？']'''
# info = ['骗子，', '不是', '说', '只有', "10", '个题吗？']
# with open('readme.txt', 'w', encoding='utf-8')as f:
#     f.write('_'.join(info))

```

13.第13题

```python
'''请将info中的值使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。

info = ['骗子，','不是','说','只有',10,'个题吗？']'''

# info = ['骗子，', '不是', '说', '只有', 10, '个题吗？']
# lis = []
# for i in info:
#     i = str(i)
#     lis.append(i)
# with open('readme.txt', 'w', encoding='utf-8')as f:
#     f.write('_'.join(lis))

```

14.第14题

```python
'''请将info中的所有键 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。

info = {'name':'骗子','age':18,'gender':'性别'} 

# 1. 请将info中的所有键 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
# 2. 请将info中的所有值 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
# 3. 请将info中的所有键和值按照 "键|值,键|值,键|值" 拼接起来并写入到文件 "readme.txt" 文件中。'''
# info = {'name': '骗子', 'age': 18, 'gender': '性别'}
# lis = []
# with open('readme.txt', 'w+', encoding='utf-8')as f:
#     for k in info.keys():
#         lis.append(k)
#     f.write('_'.join(lis))

# info = {'name': '骗子', 'age': 18, 'gender': '性别'}
# lis = []
# with open('readme.txt', 'w', encoding='utf-8')as f:
#     for v in info.values():
#         v = str(v)
#         lis.append(v)
#     f.write('_'.join(lis))

# info = {'name': '骗子', 'age': 18, 'gender': '性别'}
# lis = []
# with open('readme.txt', 'w', encoding='utf-8')as f:
#     for k, v in info.items():
#         item = '%s|%s' % (str(k), str(v))
#         lis.append(item)
#     f.write(','.join(lis))
```

15.第15题

```python
'''要求：
    如文件 data.txt 中有内容如下：

    wupeiqi|oldboy|wupeiqi@xx.com
    alex|oldboy|66s@xx.com
    xxxx|oldboy|yuy@xx.com

    请用代码实现读入文件的内容，并构造成如下格式：
    info = [
        {'name':'wupeiqi','pwd':'oldboy','email':'wupeiqi@xx.com'},
        {'name':'alex','pwd':'oldboy','email':'66s@xx.com'},
        {'name':'xxxx','pwd':'oldboy','email':'yuy@xx.com'},
    ]'''
# info = []
# with open('data.txt', 'r', encoding='utf-8')as f:
#     for line in f:
#         dic = {}
#         line = line.strip().split('|')
#         dic['name'] = line[0]
#         dic['pwd'] = line[1]
#         dic['email'] = line[2]
#         info.append(dic)
# print(info)
```

