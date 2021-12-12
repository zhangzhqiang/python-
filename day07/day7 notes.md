# Day7 notes

## 1.今日概要

- 深浅拷贝(面试)
- 文件操作

## 2.内容回顾&补充

1.内容回顾

- 计算机基础
- 编码
- 语法
  - if  else
  - while
  - for
- 数据类型
- range/type/id
- 运算符

2.面试题

- 公司线上系统用的什么?

- py2 和 py3的区别?

  - 默认解释器编码
  - 输入输出
  - 整数的除法/int long

- 运算符

  ```python
  v = 1 or 0 and 8 or 9
  print(v)
  ```

- is 和 == 的区别?

- 列举python的数据类型中都有哪些方法?

## 3.今日内容

- 深浅拷贝

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
    print(v1 == v2)
    print(v1 is v2)
    print(v1[0] is v2[0])
    
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

- 文件操作

  ```python
  # ====================读取======================
  # 打开
  # f = open('log.txt', mode='r', encoding='utf-8')
  # 操作
  # f1 = f.read()
  # print(f1)
  # 关闭
  # f.close()
  
  # ====================写入=======================
  # f = open('log.txt', mode='w', encoding='utf-8')
  # f.write('我就是我')
  # f.close()
  
  # ====================追加=======================
  # f = open('log.txt', mode='a', encoding='utf-8')
  # f.write('kljl')
  # f.close()
  ```

  - 打开

    - r,只读

    - w,只写,写之前清空文件

    - a,只住家

    - r+

      ```python
      file_object = open('log.txt',mode='r+',encoding='utf-8')
      # file_object.seek(2) # 调整光标的位置
      
      content = file_object.read()
      file_object.write('浪')
      
      # 读取内容
      # content = file_object.read()
      # print(content)
      
      # file_object.write('666')
      
      # 关闭文件
      file_object.close()
      ```

      - 读:默认从0的光标开始读,可以通过seek调整光标的位置
      - 写:从光标所在的位置开始写,也可以通过seek调整光标的位置

    - w+

      ```python
      file_object = open('log.txt',mode='w+',encoding='utf-8')
      data = file_object.read()
      print(data)
      file_object.write('alex')
      file_object.seek(0)
      data = file_object.read()
      print(data)
      file_object.close()
      ```

      - 读:默认光标在写入的最后或0,可以通过seek调整光标的位置
      - 写:先清空文件

    - a+

      ```python
      file_object = open('log.txt',mode='a+',encoding='utf-8')
      
      # file_object.seek(0)
      # data = file_object.read()
      # print(data)
      
      file_object.seek(0)  # 写的时候永远在最后
      file_object.write('666')
      
      file_object.close()
      ```

      - 读:默认光标在最后,可以通过seek调整光标的位置,然后再去读
      - 写:永远在最后追加

  - 操作

    - 读

      ```python
      # file_object = open('log.txt',mode='r',encoding='utf-8')
      
      # 读取文件的所有内容到内存
      # data = file_object.read()
      
      # 从当前光标所在的位置向后读取文件两个字符
      # data = file_object.read(2)
      
      # 读取文件的所有内容到内存，并按照每一行进行分割到列表中。
      # data_list = file_object.readlines()
      # print(data_list)
      
      # 如果以后读取一个特别大的文件 (**********)
      # for line in file_object:
      #     line = line.strip()
      #     print(line)
      
      # file_object.close()
      ```

      - read()
      - read(2)  # 字符
      - readlines()  #每一行

    - 写

      ```python
      file_object = open('log.txt',mode='w',encoding='utf-8')
      file_object.write('asdfadsfasdf\n')
      file_object.write('asdfasdfasdfsadf')
      file_object.close()
      ```

  - 关闭

  练习题:

  ```python
  # 练习1：请将user中的元素根据 _ 链接，并写入 'a1.txt' 的文件
  """
  user = ['alex','eric']
  data = "_".join(user)
  file_object = open('a1.txt',mode='w',encoding='utf-8')
  file_object.write(data)
  file_object.close()
  """
  
  # 练习2：请将user中的元素根据 _ 链接，并写入 'a1.txt' 的文件
  """
  user = [
      {'name':'alex','pwd':'123'},    # alex|123
      {'name':'eric','pwd':'olbody'}, # eric|olbody
  ]
  file_object = open('a2.txt',mode='w',encoding='utf-8')
  for item in user:
      line = "%s|%s\n" %(item['name'],item['pwd'],)
      file_object.write(line)
  file_object.close()
  """
  
  # 练习3：请将a2.txt中的文件读取出来并添加到一个列表中 ['alex|123','eric|olbody']
  # 方式一
  """
  file_obj = open('a2.txt',mode='r',encoding='utf-8')
  content = file_obj.read()
  file_obj.close()
  content = content.strip()
  data_list = content.split('\n')
  print(data_list)
  """
  # 方式二
  """
  result = []
  file_obj = open('a2.txt',mode='r',encoding='utf-8')
  for line in file_obj:
      line = line.strip()
      result.append(line)
  file_obj.close()
  print(result)
  """
  ```

## 4.总结

- 深浅拷贝
- 文件操作
  - 打开
  - 读写
  - 关闭
- 文件操作和数据类型的结合使用