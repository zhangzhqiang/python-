# Day4 notes

## 1.今日内容

- 列表
- 元祖

## 2.内容回顾和补充

### 1.计算机基础

- 硬件：cpu／硬盘／内存／主板／网卡／显卡。。。

- 操作系统：

  - linux(免费／开源)
    - centos
    - ubuntu
    - redhat
  - windows
  - mac

- 解释器／编译器

  - 补充：编译型语言和解释型语言。

    ```
    # 编译型：代码写完后，编译器将其变成另外一个文件，然后交到计算机执行。
    # 解释型：代码写完后，交到解释器，解释器会从上到下逐行执行,边解释边执行
    ```

- 软件(应用软件)

### 2.环境的安装

- python解释器
  - python2
  - python3
- 开发工具：pycharm(推荐)／文本编辑器

### 3.python语法

- 1.解释器路径:hello.py

  ```python
  #!/usr/bin/env/ python
  print('你好')
  ```

  linux系统应用：

  - 赋予文件可执行权限
  - ./hello.py

- 2.编码

  ```python
  #!/usr/bin/env/ python
  # -*- coding:utf-8 -*-
  print('你好')
  ```

  - 1.编码种类
    - acsii
    - unicode
    - utf-8/utf-16
    - gbk/gb2312
  - 2.中文表示
    - utf-8：3个字节
    - gbk：2个字节
  - 3.python默认解释器编码
    - python3:utf-8
    - python2:ascii

3.输入输出

- py2
  - 输入：raw_input
  - 输出：print ""
- py3
  - 输入：input
  - 输出：print("")

### 4.数据类型

- int

  - python2中有：int／long
  - python3中有int
  - 强制转换：int('678')
  - 除法：py2 和 py3(正常)

- bool

  - True/False(其他语言首字母小写)
  - 特殊为False的其它类型：0 和""

- str

  - 独有的功能

    - upper／lower

    - replace

    - strip／strip／rstrip

    - isdigit

    - split／rsplit

    - 补充：

      - startwith／endwith

      - ```python
        name = 'alex'
        # 判断是否以al开头
        flag = name.startswith('al')
        print(flag)
        ```

      - format

        ```python
        name = '我叫{0},年龄{1}'.format('老男孩', 88)
        print(name)
        ```

      - encode

        ```python
        name = '理解' # 解释器读取到内存后，按照unicode编码存储：8个字节
        v1 = name.encode('utf-8')
        print(v1)
        v2 = name.encode('gbk')
        print(v2)
        ```

      - join

        ```python
        name = 'alex'
        res = '——'.join(name) # 循环每个元素，并在元素之间加入链接符
        print(res)
        ```

  - 公共的功能

    - 索引，获取一个字符

    - 切片，获取一段字符串(子序列)

    - 步长

      ```python
      name = 'oldboyalex'
      # val = name[0:-1:2]
      # val = name[1:-1:2]
      # val = name[1::2]
      # val = name[::2]
      # val = name[-1:0:-2]  # 倒着隔步
      # 将字符串反转
      val = name[::-1]
      print(val)
      ```

    - 长度，获取字符长度

    - for循环

      ```python
      name = 'alex'
      for item in name:
          print(item)
      ```

      ```python
      name = 'alex'
      for item in name:
          print(item)
          break
          print(234)
      ```

      ```python
      name = 'alex'
      for item in name:
          print(item)
          continue
          print(234)
      ```

      ```python
      # 练习题
      # 请打印：1-10 跳过7
      for i in range(1, 11):
          if i == 7:
              pass
          else:
              print(i)
      ```

      注意：for和while的应用场景，有穷尽优先使用for，无穷尽用while

### 5.变量

### 6.注释

### 7.条件语句

- if elif else

### 8.循环语句

- while + for + break + continue

### 9.运算符

### 10.字符串格式化

- %s，字符串
- %d，整数
- %%，出现100％这样的需求

### 11.其它

- markdown笔记

- git

  - 本地：git软件，常用的命令

    - git status
    - git add .
    - git commit -m '备注'
    - git push origin master
    - git init

  - 远程：码云／github(程序员交友平台)

  - 补充

    - 面试相关：

      - 1.写出你常用的git命令

      - 2.你们公司是怎么用git做开发的

        - 1.在码云或github等代码托管的网站创建自己仓库，创建完之后获取到一个仓库地址，如：https://gitee.com/python-ike/cn-ike.git

        - 2.自己写代码

        - 3.将代码提交到远程仓库

          - 初始化

            - 进入一个任意文件夹，如：G:\homework\
            - git init
            - git config 邮箱
            - git config 姓名
            - git remode add origin https://gitee.com/python-ike/cn-ike.git

            注意：至此git已经将G:\homework\管理起来了，此后本文件夹有任何的变动，git都会检测到(使用git status命令可以查看状态)

          - 代码收集并提交

            - git status
            - git add .
            - git commit -m '备注内容'
            - git push origin master 将本地G:\homework\目录同步到码云仓库

          - 修改代码或删除文件等对本地G:\homework\目录下的内容同步到码云仓库，执行－－代码收集并提交步骤

          - 如果远程有本地没有的代码，必须先执行：[可能会引发合并问题]

            - git pull origin master
            - git status
            - git add .
            - git commit -m '备注内容'
            - git push origin master
        
      - git经常遇到的问题
      
        ```python
        # 大概意思是本地和远程之前的文件不一致,合并后才能上传本地新文件
        F:\game_project\node_project>git push -u origin master
        To https://gitee.com/cn_xxxxx/node.git
         ! [rejected]        master -> master (fetch first)
        error: failed to push some refs to 'https://gitee.com/cn_xxxxx/node.git'
        hint: Updates were rejected because the remote contains work that you do
        hint: not have locally. This is usually caused by another repository pushing
        hint: to the same ref. You may want to first integrate the remote changes
        hint: (e.g., 'git pull ...') before pushing again.
        hint: See the 'Note about fast-forwards' in 'git push --help' for details.
        # 解决办法
        # 1、先拉下来，会自动合并的（不用操心）
        git pull origin master
        # 2、再上传
        git push -u origin master
        
        ```

### 12.总结

- 1.语法：变量if／while／运算符(辅助)
  - 必备：变量if／while
  - 重点：数据类型中的字符串
    - 独有的功能
    - 公共功能
    - for循环
- 2.解决实际问题：
  - 逻辑＋代码

## 3.内容详细

### 1.列表

- 如果想要表示两个同学 user = "张三","李四"

- 以后想要表示多个"事物"，可以使用列表。

  ```python
  user ＝ ["张三","李四",89]
  ```

- 公共功能

  - len

    ```python
    user ＝ ["张三","李四",89]
    val ＝ len(user)
    print(val) ＃3
    ```

  - 索引

    ```python
    user ＝ ["张三","李四",89]
    val ＝ user[0]
    print(val) # 张三
    ```

  - 切片

    ```python
    user ＝ ["张三","李四",89]
    val ＝ user[0:2]
    print(val) 
    ```

  - 删除（数字、布尔、字符串除外）

    ```python
    # 方式一
    users = ["张三", "李四", "王五", "王五"]
    users.pop(1)
    print(users)
    # 方式二
    users = ["张三", "李四", "王五", "王五"]
    del users[1]
    print(users)
    ```

    注意:

    - 字符串本身不能修改或删除(不可变类型)
    - 列表是可变类型

  - 修改（字符串、数字、布尔除外）

    ```python
    users = ["张三", "李四", "王五", "王五"]
    users[2] = 66
    
    users[0] = '中国'
    users[0][1]
    ```

  - 步长

    ```python
    user ＝ ["张三","李四",89]
    val ＝ user[0:2:2]
    print(val) 
    ```

  - 练习题

    ```python
    content = input('请输入：')
    content_len = len(content)
    index = 0
    total = 0
    while True:
        char = content[index]
        if char.isdigit():
            total += int(char)
        index += 1
        if index == content_len:
            break
    print(total)
    ```

  - for循环

    ```
    # 方式一：
    users = ["张三","李四","王五"]
    count = 0
    for i in users:
        print(count, i)
        count += 1
    
    # 方式二：
    users = ["张三","李四","王五"]
    for index in range(0, len(users)):
        print(index, users[index])
    ```

- 独有功能

  - append,在列表的最后追加一个元素

    ```python
    user = []
    while True:
        name = input('username:').strip()
        user.append(name)  # 追加一个元素
        print(user)
    ```

  - 登录验证示例

    ```python
    # 录入用户名和密码
    users = []
    for i in range(0, 3):
        name = input('username and password:').strip()
        users.append(name)
    print(users)
    
    # 用户名和密码校验
    
    user = input('username:').strip()
    pwd = input('password:').strip()
    for item in users:
        res = item.split(',')
        print(res)
        username = res[0]
        password = res[1]
        if user == username and pwd == password:
            print('登录成功')
            break
    ```

  - insert

    ```python
    users = ["张三","李四","王五"]
    users.insert(1, '赵八')
    	print(users)
    # insert,在指定索引位置插入元素
    ```
    
  - remove
  
    ```python
    users = ["张三", "李四", "王五", "王五"]
    users.remove('王五')  # 如果有两个重名,只删除第一个
    print(users)
    ```
  
  - pop
  
    ```python
    users = ["张三", "李四", "王五", "王五"]
    users.pop(1)
    users.pop()  # 默认删除最后一个
    print(users)
    ```
  
  - clear
  
    ```python
    users = ["张三", "李四", "王五", "王五"]
    users.clear()
    print(users)
    ```
  
- 总结:

  - 增

    - append/insert

  - 删

    - pop/remove/del users[1]/clear

  - 改

    - users[3] = '新值'

  - 查

    - 索引/切片

  - 列表嵌套

    ```python
    users = ['alex',0,True,[11,22,33,'oldboy'],[1,['alex','ike'],2,3]]
    users[0]
    users[3]
    users[3][3]
    users[3][3][2]
    users[3] = 666
    ```

### 2.元组

1.元组的书写规范

```python
users = ["张三", "李四", "王五", "王五"] # 列表
users = ("张三", "李四", "王五", "王五") # 元组（不可变）
```

2.公共功能

- 索引（排除：int、bool）

  ```python
  users = ("张三", "李四", "王五", "王五")
  print(users[0])
  print(users[-1])
  ```

- 切片（排除：int、bool）

  ```python
  users = ("张三", "李四", "王五", "王五")
  print(users[0:3])
  ```

- 步长（排除：int、bool）

  ```python
  users = ("张三", "李四", "王五", "王五")
  print(users[0:3:2])
  ```

- 删除（排除：str、int、bool、tuple）

- 修改（排除：str、int、bool、tuple）

- for循环（排除：int、bool）

  ```python
  users = ("张三", "；李四", "王五", "王五")
  for item in users:
  	print(item)
  ```

- 长度（排除：int、bool）

  ```python
  users = ("张三", "李四", "王五", "王五")
  print(len(users))
  ```

3.独有功能(无)

4.特殊:元组中的元素不可被修改/删除

- ```python
  v1 = (11,22,33)
  v1[1] = 9 # 错误
  v1 = 999 # 正确
  
  # 可以嵌套
  v1 = (11,22,33,(44,55,66),(11,66,(99,88,(55,))))
  # 嵌套
  v1 = [11,22,33,(44,55,66)]
  v1[-1][1] = 887 # 错误
  v1[-1] = 123 # 正确
  # 嵌套
  v1 = (11,22,33,[44,55,66])
  v1[-1] = 666 # 错误
  v1[-1][2] = 777 # 正确
  ```

## 4.总结

- 解释型和编译型区别以及列举你了解的语言.

- 字符串补充功能

  - 独有
    - startswith/endswith
    - format
    - encode
    - join
  - 公共
    - 切片
    - 索引
    - len
    - 步长(面试题)
    - for循环
    - range(0,10) # 生成一个数字列表
  - 特性
    - 不可变,字符串元素不能删除和修改

- git本地和远程要同步,以后只能操作本地然后提交

- 列表(可变)

  - 公共
    - 索引
    - 切片
    - 步长
    - 修改
    - 删除
    - for循环
    - len
  - 独有
    - append
    - insert
    - pop
    - remove
    - clear
  - 列表嵌套

- 元组(不可变)

- 公共

  - 索引
  - 切片
  - 步长
  - for循环
  - len

- 独有功能(无)

- 元组嵌套

  ```python
  v1 = (11,22,33,[44,55,66])
  v1[-1] = 666 # 错误
  v1[-1][2] = 777 # 正确
  ```

- 