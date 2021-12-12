# Day notes 34

## 今日内容

- 视图
- 触发器
- 事务
- 存储过程
- 函数
- 流程控制

### 1.视图

视图是一个虚拟表（非真实存在），其本质是【根据SQL语句获取动态的数据集，并为其命名】，用户使用时只需使用【名称】即可获取结果集，可以将该结果集当做表来使用。

使用视图我们可以把查询过程中的临时表拿出来，用视图去实现，这样以后再想操作该临时表的数据时就无需重写复杂的sql了，直接去视图中查找即可，但视图有明显的效率问题，并且视图是存放在数据库中的，如果我们程序中使用的sql过分依赖数据库中的视图，即强耦合，那就意味着扩展sql极为不便，因此并不推荐使用！

示例：普通查询

```mysql
# 两张有关系的表
mysql> select * from course;
+-----+--------+------------+
| cid | cname  | teacher_id |
+-----+--------+------------+
|   1 | 生物   |          1 |
|   2 | 物理   |          2 |
|   3 | 体育   |          3 |
|   4 | 美术   |          2 |
+-----+--------+------------+
rows in set (0.00 sec)

mysql> select * from teacher;
+-----+-----------------+
| tid | tname           |
+-----+-----------------+
|   1 | 张磊老师        |
|   2 | 李平老师        |
|   3 | 刘海燕老师      |
|   4 | 朱云海老师      |
|   5 | 李杰老师        |
+-----+-----------------+
rows in set (0.00 sec)

# 查询李平老师教授的课程名
mysql> select cname from course where teacher_id = (select tid from teacher where tname='李平老师');
+--------+
| cname  |
+--------+
| 物理   |
| 美术   |
+--------+
rows in set (0.00 sec)

# 子查询出临时表，作为teacher_id等判断依据
select tid from teacher where tname='李平老师'
```

**1.创建视图**

示例：

```mysql
# 语法：CREATE VIEW 视图名称 AS  SQL语句
create view teacher_view as select tid from teacher where tname='李平老师';

# 查询李平老师教授的课程名的sql可以改写为
mysql> select cname from course where teacher_id = (select tid from teacher_view);
+--------+
| cname  |
+--------+
| 物理   |
| 美术   |
+--------+
rows in set (0.00 sec)

# 注意的问题：
# 1. 使用视图以后就无需每次都重写子查询的sql，但是这么效率并不高，还不如我们写子查询的效率高
# 2. 而且有一个致命的问题：视图是存放到数据库里的，如果我们程序中的sql过分依赖于数据库中存放的视图，那么意味着，一旦sql需要修改且涉及到视图的部分，则必须去数据库中进行修改，而通常在公司中数据库有专门的DBA负责，你要想完成修改，必须付出大量的沟通成本DBA可能才会帮你完成修改，极其地不方便！
```

**2.使用视图**

示例：

```mysql
# 修改视图，原始表也跟着改
mysql> select * from course;
+-----+--------+------------+
| cid | cname  | teacher_id |
+-----+--------+------------+
|   1 | 生物   |          1 |
|   2 | 物理   |          2 |
|   3 | 体育   |          3 |
|   4 | 美术   |          2 |
+-----+--------+------------+
rows in set (0.00 sec)

# 创建表course的视图
mysql> create view course_view as select * from course;
Query OK, 0 rows affected (0.52 sec)

mysql> select * from course_view;
+-----+--------+------------+
| cid | cname  | teacher_id |
+-----+--------+------------+
|   1 | 生物   |          1 |
|   2 | 物理   |          2 |
|   3 | 体育   |          3 |
|   4 | 美术   |          2 |
+-----+--------+------------+
rows in set (0.00 sec)

# 更新视图中的数据
mysql> update course_view set cname='xxx'; 
Query OK, 4 rows affected (0.04 sec)
Rows matched: 4  Changed: 4  Warnings: 0

# 往视图中插入数据
mysql> insert into course_view values(5,'yyy',2); 
Query OK, 1 row affected (0.03 sec)

# 发现原始表的记录也跟着修改了
mysql> select * from course;  
+-----+-------+------------+
| cid | cname | teacher_id |
+-----+-------+------------+
|   1 | xxx   |          1 |
|   2 | xxx   |          2 |
|   3 | xxx   |          3 |
|   4 | xxx   |          2 |
|   5 | yyy   |          2 |
+-----+-------+------------+
rows in set (0.00 sec)

# 我们不应该修改视图中的记录，而且在涉及多个表的情况下是根本无法修改视图中的记录的。
```

**3.修改视图**

示例：

```mysql
# 语法：ALTER VIEW 视图名称 AS SQL语句
mysql> alter view teacher_view as select * from course where cid>3;
Query OK, 0 rows affected (0.04 sec)

mysql> select * from teacher_view;
+-----+-------+------------+
| cid | cname | teacher_id |
+-----+-------+------------+
|   4 | xxx   |          2 |
|   5 | yyy   |          2 |
+-----+-------+------------+
rows in set (0.00 sec)
```

**4.删除视图**

示例：

```mysql
# 语法：DROP VIEW 视图名称

DROP VIEW teacher_view
```

### 2.触发器

使用触发器可以定制用户对表进行【增、删、改】操作时前后的行为，注意：没有查询！

**1.创建触发器**

语法：

```mysql
# 插入前
CREATE TRIGGER tri_before_insert_tb1 BEFORE INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 插入后
CREATE TRIGGER tri_after_insert_tb1 AFTER INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除前
CREATE TRIGGER tri_before_delete_tb1 BEFORE DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除后
CREATE TRIGGER tri_after_delete_tb1 AFTER DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新前
CREATE TRIGGER tri_before_update_tb1 BEFORE UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新后
CREATE TRIGGER tri_after_update_tb1 AFTER UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END
```

示例：

```mysql
# 准备表
CREATE TABLE cmd (
    id INT PRIMARY KEY auto_increment,
    USER CHAR (32),
    priv CHAR (10),
    cmd CHAR (64),
    sub_time datetime,  # 提交时间
    success enum ('yes', 'no')  # 0代表执行失败
);

CREATE TABLE errlog (
    id INT PRIMARY KEY auto_increment,
    err_cmd CHAR (64),
    err_time datetime
);

# 创建触发器
delimiter //
CREATE TRIGGER tri_after_insert_cmd AFTER INSERT ON cmd FOR EACH ROW
BEGIN
    IF NEW.success = 'no' THEN  # 等值判断只有一个等号
            INSERT INTO errlog(err_cmd, err_time) VALUES(NEW.cmd, NEW.sub_time) ;  # 必须加分号
      END IF ;  # 必须加分号
END//
delimiter ;


# 往表cmd中插入记录，触发触发器，根据IF的条件决定是否插入错误日志
INSERT INTO cmd (
    USER,
    priv,
    cmd,
    sub_time,
    success
)
VALUES
    ('egon','0755','ls -l /etc',NOW(),'yes'),
    ('egon','0755','cat /etc/passwd',NOW(),'no'),
    ('egon','0755','useradd xxx',NOW(),'no'),
    ('egon','0755','ps aux',NOW(),'yes');
    
# 插入后触发触发器！
# 查询错误日志，发现有两条
mysql> select * from errlog;
+----+-----------------+---------------------+
| id | err_cmd         | err_time            |
+----+-----------------+---------------------+
|  1 | cat /etc/passwd | 2017-09-14 22:18:48 |
|  2 | useradd xxx     | 2017-09-14 22:18:48 |
+----+-----------------+---------------------+
rows in set (0.00 sec)
```

**备注：特别的：NEW表示即将插入的数据行，OLD表示即将删除的数据行。**

**2.使用触发器**

触发器无法由用户直接调用，只针对于对表的【增/删/改】操作被动引发的。

**3.删除触发器**

```mysql
drop trigger tri_after_insert_cmd;
```

### 3.事务

事务用于将某些操作的多个SQL作为原子性操作，一旦有某一个出现错误，即可回滚到原来的状态，从而保证数据库数据完整性。

事务一般用于交易中，双方同时增减！

```mysql
# 准备表
create table user(
id int primary key auto_increment,
name char(32),
balance int
);

insert into user(name,balance)
values
('wsb',1000),
('egon',1000),
('ysb',1000);

# 原子操作，模仿一个买卖的场景
start transaction;
update user set balance=900 where name='wsb';  # 买东西支付100元
update user set balance=1010 where name='egon';  # 中介拿走10元
update user set balance=1090 where name='ysb';  # 卖家拿到90元
commit;

# 出现异常，回滚到初始状态
start transaction;
update user set balance=900 where name='wsb'; #买支付100元
update user set balance=1010 where name='egon'; #中介拿走10元
uppdate user set balance=1090 where name='ysb'; #卖家拿到90元,出现异常没有拿到
rollback;
commit;
mysql> select * from user;
+----+------+---------+
| id | name | balance |
+----+------+---------+
|  1 | wsb  |    1000 |
|  2 | egon |    1000 |
|  3 | ysb  |    1000 |
+----+------+---------+
rows in set (0.00 sec)
```

语法：

```
delimiter //
create procedure p4(
	out status int
)
BEGIN
	1. 声明如果出现异常则执行{
    set status = 1;
    rollback;
    }

开始事务
-- 由秦兵账户减去100
-- 方少伟账户加90
-- 张根账户加10
commit;
结束

set status = 2;


END //
delimiter ;
```

示例：

```mysql
delimiter //
create PROCEDURE p5(
    OUT p_return_code tinyint
)
BEGIN 
    DECLARE exit handler for sqlexception 
    BEGIN 
        -- ERROR 
        set p_return_code = 1; 
        rollback; 
    END; 

    DECLARE exit handler for sqlwarning 
    BEGIN 
        -- WARNING 
        set p_return_code = 2; 
        rollback; 
    END; 

    START TRANSACTION; 
        DELETE from tb1; #执行失败
        insert into blog(name,sub_time) values('yyy',now());
    COMMIT; 

    -- SUCCESS 
    set p_return_code = 0; #0代表执行成功

END //
delimiter ;
```

**在mysql中调用存储过程：**

```mysql
set @res=123;
call p5(@res);
select @res;
```

**在python中基于pymysql调用存储过程：**

```python
import pymysql

# 建立链接
conn = pymysql.connect(
    host='192.168.10.15',
    port=3306,
    user='root',
    password='123',
    db='db7',
    charset='utf8'
)

# 拿游标
cursor = conn.cursor()

# 执行sql
# cursor.callproc('p1')
# print(cursor.fetchall())

cursor.callproc('p2', (2, 4, 0))
# print(cursor.fetchall())

cursor.execute('select @_p2_2')
print(cursor.fetchone())

# 关闭
cursor.close()
conn.close()
```

### 4.存储过程

存储过程包含了一系列可执行的sql语句，存储过程存放于MySQL中，通过调用它的名字可以执行其内部的一堆sql。

优点：

- 用于替代程序写的SQL语句，实现程序与sql解耦
- 基于网络传输，传别名的数据量小，而直接传sql数据量大

缺点：

- 程序员扩展功能不方便

**程序与数据库结合使用的三种方式**

```python
# 方式一：
    MySQL：存储过程
    程序：调用存储过程

# 方式二：
    MySQL：
    程序：纯SQL语句

# 方式三：
    MySQL:
    程序：类和对象，即ORM（本质还是纯SQL语句）
```

**1.创建无参存储过程**

```mysql
delimiter //
create procedure p1()
BEGIN
	select * from db7.teacher;
END //
delimiter ;
```


```mysql
# MySQL中调用
call p1();
```


```python
# Python中调用
cursor.callproc('p1')
```
**2.创建有参存储过程**

```python
# 对于存储过程，可以接收参数，其参数有三类：

#in          仅用于传入参数用
#out        仅用于返回值用
#inout     既可以传入又可以当作返回值
```

```mysql
delimiter //
create procedure p2(in n1 int,in n2 int,out res int)
BEGIN
	select * from db7.teacher where tid > n1 and tid < n2;
	set res = 1;
END //
delimiter ;
```

```mysql
# MySQL中调用
set @x=0  # 0代表假（执行失败），1代表真（执行成功）
call p2(2,4,@x);
select @x;
```

```python
# Python中调用
cursor.callproc('p2',(2,4,0))# @_p2_0=2,@_p2_1=4,@_p2_2=0
cursor.execute('select @_p3_2')
cursor.fetchone()
```

**3.执行存储过程**

MySQL中执行：

```mysql
-- 无参数
call proc_name()

-- 有参数，全in
call proc_name(1,2)

-- 有参数，有in，out，inout
set @t1=0;
set @t2=3;
call proc_name(1,2,@t1,@t2)

执行存储过程

在MySQL中执行存储过程-- 无参数
call proc_name()

-- 有参数，全in
call proc_name(1,2)

-- 有参数，有in，out，inout
set @t1=0;
set @t2=3;
call proc_name(1,2,@t1,@t2)
```

Python中执行：

```python
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 执行存储过程
cursor.callproc('p1', args=(1, 22, 3, 4))
# 获取执行完存储的参数
cursor.execute("select @_p1_0,@_p1_1,@_p1_2,@_p1_3")
result = cursor.fetchall()

conn.commit()
cursor.close()
conn.close()

print(result)
```

**4.删除存储过程**

```mysql
drop procedure proc_name;
```

### 5.函数

MySQL中提供了许多内置函数例如：

**1.数学函数**：

```mysql
ROUND(x,y)
	返回参数x的四舍五入的有y位小数的值

RAND()
	返回０到１内的随机值,可以通过提供一个参数(种子)使RAND()随机数生成器生成一个指定的值。
```

**2.聚合函数**：

```mysql
AVG(col)返回指定列的平均值
COUNT(col)返回指定列中非NULL值的个数
MIN(col)返回指定列的最小值
MAX(col)返回指定列的最大值
SUM(col)返回指定列的所有值之和
GROUP_CONCAT(col) 返回由属于一组的列值连接组合而成的结果    
```

**3.字符串函数**：

```mysql
CHAR_LENGTH(str)
	# 返回值为字符串str 的长度，长度的单位为字符。一个多字节字符算作一个单字符。
CONCAT(str1,str2,...)
	# 字符串拼接，如有任何一个参数为NULL ，则返回值为 NULL。
CONCAT_WS(separator,str1,str2,...)
	# 字符串拼接（自定义连接符）
CONCAT_WS()不会忽略任何空字符串。 (然而会忽略所有的 NULL）。

CONV(N,from_base,to_base)
	# 进制转换
	# 例如：
		SELECT CONV('a',16,2); 表示将 a 由16进制转换为2进制字符串表示

FORMAT(X,D)
	# 将数字X 的格式写为'#,###,###.##',以四舍五入的方式保留小数点后 D 位， 并将结果以字符串的形式返回。若D为0, 则返回结果不带有小数点，或不含小数部分。
	# 例如：
		SELECT FORMAT(12332.1,4); 
		# 结果为： '12,332.1000' INSERT(str,pos,len,newstr)
            # 在str的指定位置插入字符串
            # pos：要替换位置其实位置
            #len：替换的长度
            # newstr：新字符串
            # 特别的：
            # 如果pos超过原字符串长度，则返回原字符串
            # 如果len超过原字符串长度，则由新字符串完全替换
INSTR(str,substr)
	# 返回字符串 str 中子字符串的第一个出现位置。

LEFT(str,len)
	#返回字符串str 从开始的len位置的子序列字符。

LOWER(str)
	# 变小写

UPPER(str)
	# 变大写

REVERSE(str)
	# 返回字符串 str ，顺序和字符顺序相反。

SUBSTRING(str,pos) , SUBSTRING(str FROM pos) SUBSTRING(str,pos,len) , SUBSTRING(str FROM pos FOR len)
# 不带有len参数的格式从字符串str返回一个子字符串，起始于位置 pos。带有len参数的格式从字符串str返	回一个长度同len字符相同的子字符串，起始于位置 pos。使用 FROM的格式为标准 SQL 语法。也可能对pos使用一个负值。假若这样，则子字符串的位置起始于字符串结尾的pos字符，而不是字符串的开头位置。在以下格式的函数中可以对pos使用一个负值。

# 示例：
mysql> SELECT SUBSTRING('Quadratically',5);
-> 'ratically'

mysql> SELECT SUBSTRING('foobarbar' FROM 4);
-> 'barbar'

mysql> SELECT SUBSTRING('Quadratically',5,6);
-> 'ratica'

mysql> SELECT SUBSTRING('Sakila', -3);
-> 'ila'

mysql> SELECT SUBSTRING('Sakila', -5, 3);
-> 'aki'

mysql> SELECT SUBSTRING('Sakila' FROM -4 FOR 2);
-> 'ki'
```

**4.日期和时间函数**：

```mysql
CURDATE()或CURRENT_DATE()  # 返回当前的日期
CURTIME()或CURRENT_TIME()  # 返回当前的时间
DAYOFWEEK(date)   # 返回date所代表的一星期中的第几天(1~7)
DAYOFMONTH(date)  # 返回date是一个月的第几天(1~31)
DAYOFYEAR(date)   # 返回date是一年的第几天(1~366)
DAYNAME(date)   # 返回date的星期名，如：SELECT DAYNAME(CURRENT_DATE);
FROM_UNIXTIME(ts,fmt)  # 根据指定的fmt格式，格式化UNIX时间戳ts
HOUR(time)   # 返回time的小时值(0~23)
MINUTE(time)   # 返回time的分钟值(0~59)
MONTH(date)   # 返回date的月份值(1~12)
MONTHNAME(date)   # 返回date的月份名，如：SELECT MONTHNAME(CURRENT_DATE);
NOW()    # 返回当前的日期和时间
QUARTER(date)   # 返回date在一年中的季度(1~4)，如SELECT QUARTER(CURRENT_DATE);
WEEK(date)   # 返回日期date为一年中第几周(0~53)
YEAR(date)   # 返回日期date的年份(1000~9999)

示例：重点
DATE_FORMAT(date,format) 根据format字符串格式化date值

mysql> SELECT DATE_FORMAT('2009-10-04 22:23:00', '%W %M %Y');
-> 'Sunday October 2009'
mysql> SELECT DATE_FORMAT('2007-10-04 22:23:00', '%H:%i:%s');
-> '22:23:00'
mysql> SELECT DATE_FORMAT('1900-10-04 22:23:00',
->                 '%D %y %a %d %m %b %j');
-> '4th 00 Thu 04 10 Oct 277'
mysql> SELECT DATE_FORMAT('1997-10-04 22:23:00',
->                 '%H %k %I %r %T %S %w');
-> '22 22 10 10:23:00 PM 22:23:00 00 6'
mysql> SELECT DATE_FORMAT('1999-01-01', '%X %V');
-> '1998 52'
mysql> SELECT DATE_FORMAT('2006-06-00', '%d');
-> '00'
```

**5.加密函数**：

```mysql
MD5()  # 计算字符串str的MD5校验和
PASSWORD(str)  # 返回字符串str的加密版本，这个加密过程是不可逆转的，和UNIX密码加密过程使用不同的算法。
```

**6.控制流函数**：

```mysql
CASE WHEN[test1] THEN [result1]...ELSE [default] END
 # 如果test1是真，则返回resultN1，否则返回default
CASE [test] WHEN[val1] THEN [result]...ELSE [default]END  
# 如果test和valN相等，则返回resultN，否则返回default

IF(test,t,f)   
# 如果test是真，返回t；否则返回f

IFNULL(arg1,arg2) 
# 如果arg1不是空，返回arg1，否则返回arg2

NULLIF(arg1,arg2) 
# 如果arg1=arg2返回NULL；否则返回arg1  
```

**7.自定义函数**：

函数中不要写sql语句（否则会报错），函数仅仅只是一个功能，是一个在sql中被应用的功能，若要想在begin...end...中写sql，用存储过程。

示例：

```mysql
delimiter //
create function f1(
    i1 int,
    i2 int)
returns int
BEGIN
    declare num int;
    set num = i1 + i2;
    return(num);
END //
delimiter ;
```

```mysql
elimiter //
create function f5(
    i int
)
returns int
begin
    declare res int default 0;
    if i = 10 then
        set res=100;
    elseif i = 20 then
        set res=200;
    elseif i = 30 then
        set res=300;
    else
        set res=400;
    end if;
    return res;
end //
delimiter ;
```

**8.删除函数**：

```mysql
drop function func_name;
```

**9.执行函数**：

```mysql
# 获取返回值
select UPPER('egon') into @res;
SELECT @res;

# 在查询中使用
select f1(11,nid) ,name from tb2;
```

### 6.流程控制

示例：

```mysql
delimiter //
CREATE PROCEDURE proc_if ()
BEGIN

    declare i int default 0;
    if i = 1 THEN
        SELECT 1;
    ELSEIF i = 2 THEN
        SELECT 2;
    ELSE
        SELECT 7;
    END IF;

END //
delimiter ;

if条件语句
```

**1.while循环**：

```mysql
delimiter //
CREATE PROCEDURE proc_while ()
BEGIN

    DECLARE num INT ;
    SET num = 0 ;
    WHILE num < 10 DO
        SELECT
            num ;
        SET num = num + 1 ;
    END WHILE ;

END //
delimiter ;
```

**2.repeat循环**：

```mysql
delimiter //
CREATE PROCEDURE proc_repeat ()
BEGIN

    DECLARE i INT ;
    SET i = 0 ;
    repeat
        select i;
        set i = i + 1;
        until i >= 5
    end repeat;

END //
delimiter ;
```

**3.loop循环**：

```mysql
BEGIN

    declare i int default 0;
    loop_label: loop

        set i=i+1;
        if i<8 then
            iterate loop_label;
        end if;
        if i>=10 then
            leave loop_label;
        end if;
        select i;
    end loop loop_label;

END
```

