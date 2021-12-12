# Day05 notes

## 1.今日内容

- 字典

## 2.内容回顾和补充

- int
  - py2/py3
  - 除法
  - 强制转换:int(要转换的内容)
    - int('字符串') 【重要】
    - int('布尔值')

- bool

  - 强制转换：

    - bool(字符串) --->bool(0)

      ```python
      v1 = bool(0)
      ```

    - bool(字符串)--->bool("")

      ```python
      v2 = bool('')
      ```

    - bool(列表)--->bool([])

      ```python
      v3 = bool([])
      ```

    - bool(元组)--->bool(())

      ```python
      v4 = bool(())
      ```

- str

  - 独有功能：upper、lower、split、strip、replace、isdigit、startwith、endswith、format、join、encode
  - 公共功能：len、索引、切片、步长、for循环、删除【无】、更新【无】
  - 强制转换：
    - str(999) # '999'
    - str(True) # 'True'
    - str(['张三','李四']) # "['张三','李四']"    
    - str(['张三','李四'] #  v1 = "".join(['张三','李四'])

- list

  - 独有功能：append、insert、pop、remove、clear、extend

  - 公共功能：len、索引、切片、步长、for循环、删除、更新

  - 强制转换：

    - list('sfasfafasfasfas')

      ```python
      v1 = list('sfasfafasfasfas')
      print(v1)
      ```

    - list((11,22,33))

      ```python
      v2 = list((11, 22, 33))
      print(v2)
      ```

- tuple

  - 独有功能：【无】

  - 公共功能：en、索引、切片、步长、for循环、删除【无】、更新【无】

  - 强制转换:

    - tuple('sfasfafasfasfas')

      ```python
      v3 = tuple('sfasfafasfasfas')
      print(v3)
      ```

    - tuple((11,22,33))

      ```python
      v4 = tuple((11,22,33))
      print(v4)
      ```

- 总结

  - 常见类型转换

    ```python
    # 字符串转数字
    # 数字转字符串
    # 列表转元组
    # 元组转里诶博爱
    # 其他转bool时,只有:0,"",[],()
    ```

  - 练习题

    ```python
    # "".join([元素必须是字符串,元素必须是字符串,元素必须是字符串,重要的事情说三遍])
    num = [11, 22, 33, 44]
    for item in range(0, len(num)):
        num[item] = str(num[item])
    print('_'.join(num))
    ```

## 3.内容详解

- 字典

帮助用户去表示一个事物的信息(事物是有多个属性)

```python
info = {"name": "WuSir", "age": 18, "gender": "男", "hobby": "同桌"} # 键值对
# 请输出:我的名字叫%s,几年%s岁,性别%s,喜欢%s
```

字典格式:

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

1.独有功能

```python
info = {"name": "WuSir", "age": 18, "gender": "男", "hobby": "同桌"}
```

- keys--->获取字典中所有的键  ["name","age","gender","hobby"]

  ```python
  for item in info.keys():
      print(item)
  ```

- values--->获取字典中所有的值  ["WuSir",18,男,同桌]

  ```python
for item in info.values():
      print(item)
  
  ```

- items--->获取字典中所有的键值对

  ```python
for v1, v2 in info.items():
      print(v1, v2)
  ```

2.公共功能

- len

  ```python
  info = {"name": "WuSir", "age": 18, "gender": "男", "hobby": "同桌"}
      print(len(info))
  ```

- 索引    取值

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

## 4.重点

- int
- bool
- str
- list
- tuple
- dict

