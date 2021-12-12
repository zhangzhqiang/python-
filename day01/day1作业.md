## Day01作业:

1. 操作系统的作用?

   - 操作系统是管理,控制和监督,软,硬件资源协调运行的程序系统.

2. 列举你听过的操作系统及区别？

   - Windows系列--适合个人使用,用于办公,应用人群比较多,适合打游戏,资源库丰富
   - Linux系列--性能好,开源,适用于服务器
   - Mac--界面独特,交互好,装逼神本

3. 列举你了解的编码及他们之间的区别？

   - ascii--8位表示一个字节,范围是2**8
   - unicode--万国码,16-32位表示一个字节,最多是2**32
   - utf-8--压缩了unicode编码,用尽量少的位数表示一个字节,以8个位为单位

4. 列举你了解的Python2和Python3的区别？

   - 默认编码不同:
     - py2--ascii   
     - py3--utf-8
   - 输入不同:  
     - py2--raw_input('输入的内容')
     - py3-- input('输入的内容')
   - 打印不同:
     - py2-- print '你好'
     - py3-- print('你好')

5. 你了解的python都有那些数据类型？

   - 字符串
   - 整型
   - 布尔值

6. 补充代码，实现以下功能。

   ```python
   value =  'alex"烧饼'
   print(value)  # 要求输出  alex"烧饼
   ```

7. 用print打印出下面内容：

   ```python
   ⽂能提笔安天下,
   武能上⻢定乾坤.
   ⼼存谋略何⼈胜,
   古今英雄唯是君。
   msg = """
   ⽂能提笔安天下,
   武能上⻢定乾坤.
   ⼼存谋略何⼈胜,
   古今英雄唯是君。
   """
   print(msg)
   ```

8. 变量名的命名规范和建议？

   - 变量不能以数字开头
   - 不能使用python关键字
   - 见名知意
   - 不使用拼音命名
   - 以驼峰或下划线连接两个单词
   - 建议:以下划线连接两个变量单词

9. 如下那个变量名是正确的？

   ```
   name = '武沛齐'--正确
   _ = 'alex'  --正确
   _9 = "老男孩"--正确
   9name = "景女神"--错误
   oldboy(edu = 666--错误
   ```

10. 简述你了解if条件语句的基本结构。

- ```python
  if 条件:
  	结果
  elif 条件:
  	结果
  else:
  	结果
  ```

1. 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。

   ```python
   number = 66
   num = input('请输入数字:')
   num = int(num)
   if num > number:
       print('猜大了')
   elif num < number:
       print('猜小了')
   else:
       print('猜对了')
   ```

12.提示用户输入马花藤. 判断用户输入的对不对。如果对, 提示真聪明, 如果不对, 提示你 是傻逼么。

```python
msg = input('请输入内容:')
if msg == '麻花藤':
    print('郑聪明')
else:
    print('是傻逼么')
```

13.写程序，成绩有ABCDE5个等级，与分数的对应关系如下.

```python
'''
A    90-100
B    80-89
C    60-79
D    40-59
E    0-39
'''
while True:
    num = input('请输入成绩:')
    num = int(num)
    if num >100:
        print('请输入0-100数字')
    elif num > 89:
        print('A')
    elif num > 79:
        print('B')
    elif num > 59:
        print('C')
    elif num > 39:
        print('D')
    elif num >= 0:
        print('E')
    else:
        print('请输入正整数')
```

要求用户输入0-100的数字后，你能正确打印他的对应成绩.

1. 模拟10086客服电话（条件语句的嵌套）

2. ```python
   msg = """10086服务
   1.话费查询
   2.业务办理
   3.宽带业务"""
   
   conect = """
   1.办理停机
   2.话费充值"""
   
   print(msg)
   while True:
       num = input('请输入要办理的业务:')
       num = int(num)
       if num == 1:
           print('话费查询')
       elif num == 2:
           print(conect)
           inp = input('请输入序号:')
           inp = int(inp)
           if inp == 1:
               print('办理停机')
           elif inp == 2:
               print('话费充值')
           else:
               print('无此功能')
       else:
           print('请输入正确的序号')
   
   ```

   

