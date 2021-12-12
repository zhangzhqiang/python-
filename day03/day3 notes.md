# Day3 notes

## 1.今日概要

1.整型

2.字符串

3.布尔值

## 2.内容回顾和补充

### 1.任务

每周五写一个思维导图,罗列本周学习的的知识点.

- Mindjet MindManager Pro  软件
- processon 网站

### 2.补充

1.运算符补充

- in

```python
value = '我是中国人'
# 判断'中国'是否在value所代指的字符串中,'中国'是否是value所代指的字符串的子序列.
v1 = '中国' in value
# 示例
content = input('请输入内容:')
if '退钱' in content:
	print('包含敏感字符')
# 示例:
whilt True:
	content = input('请输入内容:')
	if '退钱' in content:
		print('包含敏感字符')
	else:
		print(content)
		break
```

- not in 与 in 相反

## 3.内容详解

### 1.整型(int)

```
age = 18
```

- python2

  - int

    - 32位电脑:-2147483648～2147483647
    - 64位电脑：-9223372036854775808～9223372036854775807

    - 超出范围后python自动将其转换成long（长整形）

  - 整型除法只能保留整数位

    ```python
    from __future__ import divisio
    v = 9 /2
    print(v)
    ```

- python3
  - 只有int
  - 整型除法只能保留所有

### 2.布尔值(bool/boolen)

- 只有两个值:True/False
- 转换
  - 数字转布尔：0是False，其他都是True
  - 字符串转布尔：“”是False，其他都是True

### 3.字符串(str/string)

- 字符串特有
  - .upper()  /  .lower()
  - .isdigit()
  - .strip()  / .lstrip()  / .rstrip()
  - .replace("被替换的字符/子序列","要替换为的内容")  /  .replace("被替换的字符/子序列","要替换为的内容", 1)
  - .split('根据什么东西进行分割')  /  .split('根据什么东西进行分割', 1 )  / rsplit 

- 公共

  - len() ，计算长度。 （字符串->计算字符串中的字符个数）

    - 索引取值（0作为开始）

      ```python
      v = "oldboy"
      v1 = v[0]  # 0 1 2 3 ... 从前向后
      v2 = v[-1] # -1 -2 -3 ...从后向前
      ```

  - 切片（0作为开始）

    ```python
    v = "oldboy"
    
    # v1 = v[2:4] # 取值规则为左闭右开
    # v2 = v[3:6]
    # v2 = v[3:-1]
    # v2 = v[3:]
    # v2 = v[:-1]
    # print(v2)
    
    # 示例: 取最后两个字符
    # data = input('请输入：')
    # 方式一
    # v = data[-2:]
    # print(v)
    # 方式二
    # total_len = len(data)
    # v = data[total_len-2:total_len]
    # print(v)
    ```

  - 练习

  - ```python
    """
    需求：让用户输入任意字符串，获取字符串之后并计算其中有多少个数字。
    """
    content = input('请输入内容:')
    index = 0
    total = 0
    while True:
        cont = content[index]
        print(cont)
        value = cont.isdigit()
        if value:
            total += 1
        if index == len(content)-1:
            break
        index += 1
    print('长度为 %s' % total)
    ```

### 4.码云的使用

1.git配置

- git init 初始化,让git把你的文件夹管理起来
- git config --global user.email "13870492666@163.com" 配置有奖
- git config --global user.name "ike"  配置用户名
- git remote add origin https://gitee.com/python-ike/cn-ike.git 配置码云地址

1.git命令

- git status 查看当前目录状态
- git add . 收集当前目录下所有文件
- git commit -m '第三题作业' 写入提交记录
- git push origin master 输入用户名和密码

2.其他情况

- 如果提交文件时少提交了
  - git add .
  - git commit - '忘记提交的文件'
  - git push orgin master

### 5.今日作业

```
1.思维导图
2.笔记
3.作业(py文件或文件夹)
```

