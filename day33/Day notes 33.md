# Day notes 33

## 今日内容

- pymysql模块

1.pymsql基本使用方法：

示例：

```python
# pip3 install pymysql
import pymysql

user = input('user>>: ').strip()
pwd = input('password>>: ').strip()

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='390252',
    db='db9',
    charset='utf8'
)

# 拿到游标，执行完默认以元组形式返回
cursor = conn.cursor()

# 执行sql语句，注意%s需要加引号
sql = 'select * from userinfo where user = "%s" and pwd="%s"' % (user, pwd)
# 受影响的行数
rows = cursor.execute(sql)

cursor.close()
conn.close()

# 进行判断
if rows:
    print('登录成功')
else:
    print('登录失败')
```

2.sql注入

注意：符号--会注释掉它之后的sql

原理：就根据程序的字符串拼接name='%s'，我们输入一个***xxx' -- haha***,用我们输入的xxx加'在程序中拼接成一个判断条件name='***xxx' -- haha***'

示例：sql注入两种方式

```python
# 方式一：
# 1.sql注入之：用户存在，绕过密码
egon' -- 任意字符

# 方式二：
# 2.sql注入之：用户不存在，绕过用户与密码
xxx' or 1=1 -- 任意字符
```

以这两种方式登录都可以登录成功，第二种方式并且可以同时绕过用户名和密码。

解决方法：

```python
import pymysql

user = input('user>>: ').strip()
pwd = input('password>>: ').strip()

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='390252',
    db='db9',
    charset='utf8'
)

# 拿到游标
cursor = conn.cursor()

# 执行sql语句
# 注意%s需要去掉引号，因为pymysql会自动为我们加上
sql = 'select * from userinfo where user = %s and pwd=%s'  
# pymysql模块自动帮我们解决sql注入的问题，只要我们按照pymysql的规矩来
rows = cursor.execute(sql, (user, pwd))

cursor.close()
conn.close()

# 进行判断
if rows:
    print('登录成功')
else:
    print('登录失败')
```

3.增、删、改

示例：插入一条数据

```python
import pymysql

user = input('user>>: ').strip()
pwd = input('password>>: ').strip()

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='390252',
    db='db9',
    charset='utf8'
)
# 拿游标
cursor = conn.cursor()

# 执行sql
# 增、删、改对应的sql语句
sql = 'insert into userinfo(user,pwd) values(%s, %s)'
rows = cursor.execute(sql, (user, pwd))
print(rows)

# 显示最后一条自增id的位置
print(cursor.lastrowid)

# 提交后才发现表中插入记录成功
conn.commit()

cursor.close()
conn.close()
```

示例：插入 多条记录

```python
import pymysql

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='390252',
    db='db9',
    charset='utf8'
)
# 拿游标
cursor = conn.cursor()

# 执行sql
# 增、删、改对应的sql语句
sql = 'insert into userinfo(user,pwd) values(%s, %s)'

# 插入多条记录
rows = cursor.executemany(sql, [('ike', '111'), ('egon', '222'), ('alex', '333')])

# 显示最后一条自增id的位置
print(cursor.lastrowid)

# 提交后才发现表中插入记录成功
conn.commit()

cursor.close()
conn.close()
```

4.查

示例：

```python
import pymysql

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='390252',
    db='db9',
    charset='utf8'
)

cursor = conn.cursor(pymysql.cursors.DictCursor)

# 执行sql
# 执行sql语句，返回sql影响成功的行数rows,将结果放入一个集合，等待被查询
rows = cursor.execute('select * from userinfo;')

# 一行一行查
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

# 查指定行数的数据
print(cursor.fetchmany(2))

# 查询全部
print(cursor.fetchall())


cursor.scroll(2, mode='absolute')  # 相对绝对位置移动
print(cursor.fetchone())
cursor.scroll(1, mode='relative')  # 相对当前位置移动
print(cursor.fetchone())

cursor.close()
conn.close()
```

