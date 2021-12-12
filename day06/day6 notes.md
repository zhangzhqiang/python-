# Day6 notes

## 1.今日内容

- 集合
- 内存相关
- 深浅拷贝

## 2.内容回顾&补充

- 内容回顾

- 补充

  - 列表

    - reverse,反转

      ```python
      v1 = [1, 2, 3, 4, 5]
      print(v1)
      v1.reverse()
      print(v1)
      ```

    - sort

      ```python
      1 = [1, 2, 3, 4988944, 5, 6565, 9999]
      print(v1)
      # v1.sort(reverse=False)  # 从小到大(默认)
      # v1.sort(reverse=True)  # 从大到小
      print(v1)
      ```

  - 字典

    - keys/values/items

    - get

      ```python
      # None数据类型,表示空(无任何功能,专门用于提供空值)
      info = {'k1': 'v1', 'k2': 'v2'}
      v2 = info.get('k33')  # None就是Python中的空
      v3 = info.get('k33', '没有')  # 空,打印没有
      print(v2)
      print(v3)
      ```

    - pop

      ```python
      # info = {'k1': 'v1', 'k2': 'v2'}
      #
      # res = info.pop('k2')
      # print(info, res)
      #
      # del info['k1']
      # print(info)
      ```

    - update

      ```python
      info = {'k1': 'v1', 'k2': 'v2'}
      
      # 键不存在,则添加,存在,则更新
      info.update({'k3': 'v3', 'k4': 'v4', 'k5': 'v5', 'k2': 999})
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

## 3.详细内容

### 1.集合set

- 无序
- 无重复

```python
v = {1, 2, 3, 4, 5}

# 疑问? v = {}
None
int
    v = 123
    v = int(123)
bool
    v2 = False/True
    v2 = bool() -->Flase
str
    v3 = ""
    v3 = str()
list
    v4 = []
    v4 = list()
tuple
    v5 = ()
    v5 = tuple()
dict
    v6 = {}
    v6 = dict()
set
    v7 = set()
```

2.集合的独有功能

- add

  ```python
  v = {1, 2}
  v.add('zhangsan')
  v.add('lisi')
  print(v)
  ```

- discard

  ```python
  v = {1, 2, 'zhangsan'}
  v.discard('zhangsan')
  print(v)
  ```

- update

  ```python
  v = {1, 2, 'zhangsan'}
  v.update({11, 22, 33})
  print(v)
  
  ```

- intersection

  ```python
  v = {1, 2, 'zhangsan'}
  v1 = v.intersection({1, 2, 3})
  print(v1)
  
  ```

- union

  ```python
  v = {1, 2, 'zhangsan'}
  v1 = v.union({1, 2, 3})
  print(v1)
  
  ```

- difference

  ```python
  v = {1, 2, 'zhangsan'}
  v1 = v.difference({1, 2, 3})
  print(v1)
  
  ```

- symmetric_difference

  ```python
  v = {1, 2, 'zhangsan'}
  v1 = v.symmetric_difference({1, 2, 3})
  print(v1)
  ```

3.公共功能

- len

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

- 索引【无】

- 步长【无】

- 删除【无】

- 修改【无】

4.嵌套问题

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

### 2.内存相关知识

- 示例一:

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

- 示例二:

  ```python
  v1 = [11, 22, 33, 44]
  v1 = [55, 66, 78]
  ```

- 示例三:

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

- 示例四:

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

- 示例五:

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

  -  == 用于比较直是否相等.
  - is用于比较内存地址是否相等.

### 3.今日总结

- 列表
  - reverse
  - sort
- 字典:
  - get()
  - update
- 集合
  - add
  - discard
  - update
  - intersection
  - union
  - difference
  - symmetric_difference
- 特殊:
  - 嵌套:集合/字典的key  hash
  - 空:None
  - 空集合:set()这一种表示方法
- id
- type
- 嵌套的应用:
  - 赋值
  - 修改内部元素:列表/字典/集合

