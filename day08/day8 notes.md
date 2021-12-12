# Day8 notes

## 1.今日内容

- 进制

- 文件操作

- 知识点梳理

## 2.内容详细

- 进制

  - 二进制
  - 八进制
  - 十进制
  - 十六进制

- 文件操作

  ```python
  # 方式一:
  # 打开文件
  f = open('文件存放的路径', mode = 'r\w\a', encoding = '文件原来写入时的编码')
  
  # 操作
  data = f.read() # 读取文件内容存放到内存
  f.write('要写入的内容')
  
  # 关闭
  f.close() # 关闭文件
  
  # 方式二:
  with open('a.txt',mode='a',encoding='utf-8') as v:
      data = v.read()
  	# 缩进中的代码执行完毕后，自动关闭文件
  ```

- 打开文件模式

  - r / w / a   只读只写
  - r+ / w+ / a+  可读可写
  - rb / wb / ab  只读只写(二进制)
  - r+b / w+b / a+b  可读可写(二进制)

  注意:rb/wb/ab:以二进制打开文件，不必指定编码（指定报错），用于读取/写入图片，音频，视频等文件;

- 文件操作

  - read()  把文件全部读到内存

  - read(2)

    - 2表示两个个字符

      ```python
      obj = open('a.txt',mode='r',encoding='utf-8')
      data = obj.read(2) # 2个字符
      obj.close()
      print(data)
      ```

    - 2表示两个字节

      ```python
      obj = open('a.txt',mode='rb')
      data = obj.read(2) # 2个字节
      obj.close()
      ```

  - write(字符串)

    ```python
    obj = open('a.txt',mode='w',encoding='utf-8')
    obj.write('中午你')
    obj.close()
    ```

  - write(二进制)

    ```python
    obj = open('a.txt',mode='wb')
    
    # obj.write('中午你'.encode('utf-8'))
    v = '中午你'.encode('utf-8')
    obj.write(v)
    
    obj.close()
    ```

  - seek(光标字节位置)，无论模式是否带b，都是按照字节进行处理;

    ```python
    obj = open('a.txt',mode='r',encoding='utf-8')  # 读模式打开
    obj.seek(3) # 跳转到指定字节位置
    data = obj.read()
    obj.close()
    print(data)
    
    
    obj = open('a.txt',mode='rb')  # 二进制读模式
    obj.seek(3) # 跳转到指定字节位置
    data = obj.read()
    obj.close()
    print(data)
    ```

  - tell(), 获取光标当前所在的字节位置

    ```python
    obj = open('a.txt',mode='rb')
    # obj.seek(3) # 跳转到指定字节位置
    obj.read()
    data = obj.tell()
    print(data)
    obj.close()
    ```

  - flush，强制将内存中的数据写入到硬盘

    ```python
    v = open('a.txt',mode='a',encoding='utf-8')
    while True:
        val = input('请输入：')
        v.write(val)
        v.flush()
    
    v.close()
    ```

- 文件内容修改

  - 若要修改文件内容,需要先将文件内容读到内存,在内存中修改后,再重新写入文件;

  - 若文件过大,可以打开两个文件,边修改边写入;

  ```python
  f1 = open("test1.txt",mode="r",encoding="utf-8")
  f2 = open("test2.txt",mode="w",encoding="utf-8")
  for line in f1:
      content = line.replace("123","456")
      f2.write(content)
      f1.close()
      f2.close()
  ```

  - with...as..自动释放文件句柄资源

  ```python
  with open("test1.txt",mode="r",encoding="utf-8") as f1,open("test2.txt",mode="w",encoding="utf-8") as f2:
  	for line in f1:
      	content = line.replace("123","456")
      	f2.write(content)
  ```

  

