Day31 notes

## 今日内容

- 库操作
- 表操作

### 1. 库操作

#### 1.创建数据库

语法：

```mysql
CREATE DATABASE 数据库名 charset utf8;
```

数据库命名规则：

- 可以由字母、数字、下划线、＠、＃、＄
- 区分大小写
- 唯一性
- 不能使用关键字，如：create select
- 不能单独使用数据
- 最长128位

#### 2.数据库相关操作

查看数据库：

```mysql
show databases;
show create databases db1;
select dtabases();
```

选择数据库:

```mysql
# use 数据库名字
use db1;
```

删除数据库:

```mysql
DROP DATABASE 数据库名;
```

修改数据库:

```mysql
alter database db1 charset utf8;
```

### 2. 表操作

#### 1.存储引擎

存储引擎就是表的类型。

**MySQL支持的存储引擎**

查看所有支持的存储引擎：

```
show engines\G;
```

查看正在使用的存储引擎:

```
show variables like 'storage_engine%';
```

**1、InnoDB 存储引擎**

```
支持事务,其设计目标主要面向联机事务处理(OLTP)的应用。其

特点是行锁设计、支持外键,并支持类似 Oracle 的非锁定读,即默认读取操作不会产生锁。 从 MySQL 5.5.8 版本开始是默认的存储引擎。

InnoDB 存储引擎将数据放在一个逻辑的表空间中,这个表空间就像黑盒一样由 InnoDB 存储引擎自身来管理。从 MySQL 4.1(包括 4.1)版本开始,可以将每个 InnoDB 存储引擎的 表单独存放到一个独立的 ibd 文件中。此外,InnoDB 存储引擎支持将裸设备(row disk)用 于建立其表空间。

InnoDB 通过使用多版本并发控制(MVCC)来获得高并发性,并且实现了 SQL 标准 的 4 种隔离级别,默认为 REPEATABLE 级别,同时使用一种称为 netx-key locking 的策略来 避免幻读(phantom)现象的产生。除此之外,InnoDB 存储引擎还提供了插入缓冲(insert buffer)、二次写(double write)、自适应哈希索引(adaptive hash index)、预读(read ahead) 等高性能和高可用的功能。

对于表中数据的存储,InnoDB 存储引擎采用了聚集(clustered)的方式,每张表都是按 主键的顺序进行存储的,如果没有显式地在表定义时指定主键,InnoDB 存储引擎会为每一 行生成一个 6 字节的 ROWID,并以此作为主键。

InnoDB 存储引擎是 MySQL 数据库最为常用的一种引擎,Facebook、Google、Yahoo 等 公司的成功应用已经证明了 InnoDB 存储引擎具备高可用性、高性能以及高可扩展性。对其 底层实现的掌握和理解也需要时间和技术的积累。如果想深入了解 InnoDB 存储引擎的工作 原理、实现和应用,可以参考《MySQL 技术内幕:InnoDB 存储引擎》一书。
```

**2、MyISAM 存储引擎**

```
不支持事务、表锁设计、支持全文索引,主要面向一些 OLAP 数 据库应用,在 MySQL 5.5.8 版本之前是默认的存储引擎(除 Windows 版本外)。数据库系统 与文件系统一个很大的不同在于对事务的支持,MyISAM 存储引擎是不支持事务的。究其根 本,这也并不难理解。用户在所有的应用中是否都需要事务呢?在数据仓库中,如果没有 ETL 这些操作,只是简单地通过报表查询还需要事务的支持吗?此外,MyISAM 存储引擎的 另一个与众不同的地方是,它的缓冲池只缓存(cache)索引文件,而不缓存数据文件,这与 大多数的数据库都不相同。
```

**3、NDB 存储引擎**

```
MySQL AB 公司从 Sony Ericsson 公司收购了 NDB 存储引擎。 NDB 存储引擎是一个集群存储引擎,类似于 Oracle 的 RAC 集群,不过与 Oracle RAC 的 share everything 结构不同的是,其结构是 share nothing 的集群架构,因此能提供更高级别的 高可用性。NDB 存储引擎的特点是数据全部放在内存中(从 5.1 版本开始,可以将非索引数 据放在磁盘上),因此主键查找(primary key lookups)的速度极快,并且能够在线添加 NDB 数据存储节点(data node)以便线性地提高数据库性能。由此可见,NDB 存储引擎是高可用、 高性能、高可扩展性的数据库集群系统,其面向的也是 OLTP 的数据库应用类型。
```

**4、Memory 存储引擎**

```
正如其名,Memory 存储引擎中的数据都存放在内存中,数据库重 启或发生崩溃,表中的数据都将消失。它非常适合于存储 OLTP 数据库应用中临时数据的临时表,也可以作为 OLAP 数据库应用中数据仓库的维度表。Memory 存储引擎默认使用哈希 索引,而不是通常熟悉的 B+ 树索引。
```

**5、Infobright 存储引擎**

```
第三方的存储引擎。其特点是存储是按照列而非行的,因此非常 适合 OLAP 的数据库应用。其官方网站是 http://www.infobright.org/,上面有不少成功的数据 仓库案例可供分析。
```

**6、NTSE 存储引擎**

```
网易公司开发的面向其内部使用的存储引擎。目前的版本不支持事务, 但提供压缩、行级缓存等特性,不久的将来会实现面向内存的事务支持。
```

**7、BLACKHOLE**

```
黑洞存储引擎，可以应用于主备复制中的分发主库。

MySQL 数据库还有很多其他存储引擎,上述只是列举了最为常用的一些引擎。如果 你喜欢,完全可以编写专属于自己的引擎,这就是开源赋予我们的能力,也是开源的魅 力所在。
```

**使用存储引擎**

**建表时指定:**

```mysql
create table t1(id int)engine=innodb;
create table t4(id int)engine=myisam;
create table t2(id int)engine=memory;
create table t3(id int)engine=blackhole;

# memory、blackhole这两种存储引擎只有表结构，无数据
# memory，在重启mysql或者重启机器后，表内数据清空
# blackhole，往表内插入任何数据，都相当于丢入黑洞，表内永远不存记录

# 插入数据
insert into t1 values(1);
insert into t2 values(1);
insert into t3 values(1);
insert into t4 values(1);
```

#### 2.表的增删改查

表相当于文件，表中的一条记录就相当于文件的一行内容，不同的是，表中的一条记录有对应的标题，称为表的字段。

##### 1.创建表

语法：

```mysql
create table 表名(
字段名1 类型[(宽度) 约束条件],
字段名2 类型[(宽度) 约束条件],
字段名3 类型[(宽度) 约束条件]
);

#注意：
1. 在同一张表中，字段名是不能相同
2. 宽度和约束条件可选
3. 字段名和类型是必须的
```

示例：

```mysql
create database db1 charset utf8;
use db1;
create table t1(  
    id int, 
    name varchar(50),
    sex enum('male','female'),
    age int(3)
    );
show tables;  # 查看db1库下所有表名
```

插入数据：

```mysql
insert into t1 values(1,'aaa',18,'male'),(2,'bbb',81,'female');
```

**注意：表的最后一个字段不加逗号！**

##### 2.删除表

语法：

```mysql
DROP TABLE 表名;
```

##### 3.修改表

语法：

```mysql
1. 修改表名
      ALTER TABLE 表名 
                          RENAME 新表名;

2. 增加字段
      ALTER TABLE 表名
                          ADD 字段名  数据类型 [完整性约束条件…],
                          ADD 字段名  数据类型 [完整性约束条件…];
      ALTER TABLE 表名
                          ADD 字段名  数据类型 [完整性约束条件…]  FIRST;
      ALTER TABLE 表名
                          ADD 字段名  数据类型 [完整性约束条件…]  AFTER 字段名;

3. 删除字段
      ALTER TABLE 表名 
                          DROP 字段名;

4. 修改字段
      ALTER TABLE 表名 
                          MODIFY  字段名 数据类型 [完整性约束条件…];
      ALTER TABLE 表名 
                          CHANGE 旧字段名 新字段名 旧数据类型 [完整性约束条件…];
      ALTER TABLE 表名 
                          CHANGE 旧字段名 新字段名 新数据类型 [完整性约束条件…];
```

示例：

```mysql
1. 修改存储引擎
mysql> alter table service 
    -> engine=innodb;

2. 添加字段
mysql> alter table student10
    -> add name varchar(20) not null,
    -> add age int(3) not null default 22;

mysql> alter table student10
    -> add stu_num varchar(10) not null after name;                //添加name字段之后

mysql> alter table student10                        
    -> add sex enum('male','female') default 'male' first;          //添加到最前面

3. 删除字段
mysql> alter table student10
    -> drop sex;

mysql> alter table service
    -> drop mac;

4. 修改字段类型modify
mysql> alter table student10
    -> modify age int(3);
mysql> alter table student10
    -> modify id int(11) not null primary key auto_increment;    //修改为主键

5. 增加约束（针对已有的主键增加auto_increment）
mysql> alter table student10 modify id int(11) not null primary key auto_increment;
ERROR 1068 (42000): Multiple primary key defined

mysql> alter table student10 modify id int(11) not null auto_increment;
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

6. 对已经存在的表增加复合主键
mysql> alter table service2
    -> add primary key(host_ip,port);        

7. 增加主键
mysql> alter table student1
    -> modify name varchar(10) not null primary key;

8. 增加主键和自动增长
mysql> alter table student1
    -> modify id int not null primary key auto_increment;

9. 删除主键
a. 删除自增约束
mysql> alter table student10 modify id int(11) not null; 

b. 删除主键
mysql> alter table student10                                 
    -> drop primary key;
```

##### 4.查询表

```mysql
describe t1;  # 查看表结构，可简写为desc 表名
+-------+-----------------------+------+-----+---------+-------+
| Field | Type                  | Null | Key | Default | Extra |
+-------+-----------------------+------+-----+---------+-------+
| id    | int(11)               | YES  |     | NULL    |       |
| name  | varchar(50)           | YES  |     | NULL    |       |
| sex   | enum('male','female') | YES  |     | NULL    |       |
| age   | int(3)                | YES  |     | NULL    |       |
+-------+-----------------------+------+-----+---------+-------+

MariaDB [db1]> show create table t1\G;  # 查看表详细结构，可加\G
```

##### 5.复制表

```mysql
# 复制表结构＋记录 （key不会复制: 主键、外键和索引）
mysql> create table new_service select * from t1;

# 只复制表结构
mysql> select * from t1 where 1=2;  # 条件为假，查不到任何记录
Empty set (0.00 sec)
mysql> create table new1_service select * from t1 where 1=2;  
Query OK, 0 rows affected (0.00 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> create table t4 like t1;
```

#### 3.数据类型

MySQL中定义数据字段的类型对你数据库的优化是非常重要的。

MySQL支持多种类型，大致可以分为三类：数值、日期/时间和字符串(字符)类型。

##### 1.数值类型

**整数类型**

表示整数类型：TINYINT SMALLINT MEDIUMINT INT BIGINT

作用：存储年龄，等级，id，各种号码等

```mysql
=============tinyint=====================
tinyint[(m)] [unsigned] [zerofill]

小整数，数据类型用于保存一些范围的整数数值范围：
有符号：
-128 ～ 127
无符号：
0 ～ 255

PS： MySQL中无布尔值，使用tinyint(1)构造。

==============int=======================
int[(m)][unsigned][zerofill]

整数，数据类型用于保存一些范围的整数数值范围：
有符号：
-2147483648 ～ 2147483647
无符号：
0 ～ 4294967295


=============bigint=======================
bigint[(m)][unsigned][zerofill]
大整数，数据类型用于保存一些范围的整数数值范围：
有符号：
-9223372036854775808～9223372036854775807
无符号：
0～18446744073709551615
```

验证：

有符号tinyint：

```mysql
MariaDB [db1]> create table t1(x tinyint); #默认为有符号，即数字前有正负号
MariaDB [db1]> desc t1;
MariaDB [db1]> insert into t1 values
    -> (-129),
    -> (-128),
    -> (127),
    -> (128);
MariaDB [db1]> select * from t1;
+------+
| x    |
+------+
| -128 | #-129存成了-128
| -128 | #有符号，最小值为-128
|  127 | #有符号，最大值127
|  127 | #128存成了127
+------+
```

设置无符号tinyint：

```mysql
MariaDB [db1]> create table t2(x tinyint unsigned);
MariaDB [db1]> insert into t2 values
    -> (-1),
    -> (0),
    -> (255),
    -> (256);
MariaDB [db1]> select * from t2;
+------+
| x    |
+------+
|    0 | -1存成了0
|    0 | #无符号，最小值为0
|  255 | #无符号，最大值为255
|  255 | #256存成了255
+------+
```

有符号int：

```mysql
MariaDB [db1]> create table t3(x int); #默认为有符号整数
MariaDB [db1]> insert into t3 values
    -> (-2147483649),
    -> (-2147483648),
    -> (2147483647),
    -> (2147483648);
MariaDB [db1]> select * from t3;
+-------------+
| x           |
+-------------+
| -2147483648 | #-2147483649存成了-2147483648
| -2147483648 | #有符号，最小值为-2147483648
|  2147483647 | #有符号，最大值为2147483647
|  2147483647 | #2147483648存成了2147483647
+-------------+
```

无符号int：

```mysql
MariaDB [db1]> create table t4(x int unsigned);
MariaDB [db1]> insert into t4 values
    -> (-1),
    -> (0),
    -> (4294967295),
    -> (4294967296);
MariaDB [db1]> select * from t4;
+------------+
| x          |
+------------+
|          0 | #-1存成了0
|          0 | #无符号，最小值为0
| 4294967295 | #无符号，最大值为4294967295
| 4294967295 | #4294967296存成了4294967295
+------------+
```

有符号bigint：

```mysql
MariaDB [db1]> create table t6(x bigint);
MariaDB [db1]> insert into t5 values  
    -> (-9223372036854775809),
    -> (-9223372036854775808),
    -> (9223372036854775807),
    -> (9223372036854775808);

MariaDB [db1]> select * from t5;
+----------------------+
| x                    |
+----------------------+
| -9223372036854775808 |
| -9223372036854775808 |
|  9223372036854775807 |
|  9223372036854775807 |
+----------------------+
```

无符号bigint：

```mysql
MariaDB [db1]> create table t6(x bigint unsigned);
MariaDB [db1]> insert into t6 values  
    -> (-1),
    -> (0),
    -> (18446744073709551615),
    -> (18446744073709551616);

MariaDB [db1]> select * from t6;
+----------------------+
| x                    |
+----------------------+
|                    0 |
|                    0 |
| 18446744073709551615 |
| 18446744073709551615 |
+----------------------+
```

zerofill测试整数类型的显示宽度：

```mysql
MariaDB [db1]> create table t7(x int(3) zerofill);
MariaDB [db1]> insert into t7 values
    -> (1),
    -> (11),
    -> (111),
    -> (1111);
MariaDB [db1]> select * from t7;
+------+
| x    |
+------+
|  001 |
|  011 |
|  111 |
| 1111 | #超过宽度限制仍然可以存
+------+
```

注意：为该类型指定宽度时，仅仅只是指定查询结果的显示宽度，与存储范围无关，存储范围如下。

其实我们完全没必要为整数类型指定显示宽度，使用默认的就可以了。

默认的显示宽度，都是在最大值的基础上加1。

| 类型         | 大小                                     | 范围（有符号）                                               | 范围（无符号）                                               | 用途            |
| :----------- | :--------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :-------------- |
| TINYINT      | 1 字节                                   | (-128，127)                                                  | (0，255)                                                     | 小整数值        |
| SMALLINT     | 2 字节                                   | (-32 768，32 767)                                            | (0，65 535)                                                  | 大整数值        |
| MEDIUMINT    | 3 字节                                   | (-8 388 608，8 388 607)                                      | (0，16 777 215)                                              | 大整数值        |
| INT或INTEGER | 4 字节                                   | (-2 147 483 648，2 147 483 647)                              | (0，4 294 967 295)                                           | 大整数值        |
| BIGINT       | 8 字节                                   | (-9,223,372,036,854,775,808，9 223 372 036 854 775 807)      | (0，18 446 744 073 709 551 615)                              | 极大整数值      |
| FLOAT        | 4 字节                                   | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | 单精度 浮点数值 |
| DOUBLE       | 8 字节                                   | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |
| DECIMAL      | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 依赖于M和D的值                                               | 依赖于M和D的值                                               | 小数值          |

- int的存储宽度是4个Bytes，即32个bit，即2**32

- 无符号最大值为：4294967296-1

- 有符号最大值：2147483648-1

- 有符号和无符号的最大数字需要的显示宽度均为10，而针对有符号的最小值则需要11位才能显示完全，所以int类型默认的显示宽度为11是非常合理的

- 最后：整形类型，其实没有必要指定显示宽度，使用默认的就ok

**浮点类型**

定点数类型 DEC等同于DECIMAL

浮点类型：FLOAT DOUBLE

作用：存储薪资、身高、体重、体质参数等

```mysql
======================================
#FLOAT[(M,D)] [UNSIGNED] [ZEROFILL]

定义：
        单精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。m最大值为255，d最大值为30

有符号：
           -3.402823466E+38 to -1.175494351E-38,
           1.175494351E-38 to 3.402823466E+38
无符号：
           1.175494351E-38 to 3.402823466E+38


精确度： 
           **** 随着小数的增多，精度变得不准确 ****


======================================
#DOUBLE[(M,D)] [UNSIGNED] [ZEROFILL]

定义：
           双精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。m最大值为255，d最大值为30

有符号：
           -1.7976931348623157E+308 to -2.2250738585072014E-308
           2.2250738585072014E-308 to 1.7976931348623157E+308

无符号：
           2.2250738585072014E-308 to 1.7976931348623157E+308

精确度：
           ****随着小数的增多，精度比float要高，但也会变得不准确 ****

======================================
decimal[(m[,d])] [unsigned] [zerofill]

定义：
          准确的小数值，m是数字总个数（负号不算），d是小数点后个数。 m最大值为65，d最大值为30。


精确度：
           **** 随着小数的增多，精度始终准确 ****
           对于精确数值计算时需要用此类型
           decaimal能够存储精确值的原因在于其内部按照字符串存储。
```

验证

```mysql
mysql> create table t1(x float(256,31));
ERROR 1425 (42000): Too big scale 31 specified for column 'x'. Maximum is 30.
mysql> create table t1(x float(256,30));
ERROR 1439 (42000): Display width out of range for column 'x' (max = 255)
mysql> create table t1(x float(255,30)); #建表成功
Query OK, 0 rows affected (0.02 sec)

mysql> create table t2(x double(255,30)); #建表成功
Query OK, 0 rows affected (0.02 sec)

mysql> create table t3(x decimal(66,31));
ERROR 1425 (42000): Too big scale 31 specified for column 'x'. Maximum is 30.
mysql> create table t3(x decimal(66,30));
ERROR 1426 (42000): Too-big precision 66 specified for 'x'. Maximum is 65.
mysql> create table t3(x decimal(65,30)); #建表成功
Query OK, 0 rows affected (0.02 sec)

mysql> show tables;
+---------------+
| Tables_in_db1 |
+---------------+
| t1            |
| t2            |
| t3            |
+---------------+
rows in set (0.00 sec)



mysql> insert into t1 values(1.1111111111111111111111111111111); #小数点后31个1
Query OK, 1 row affected (0.01 sec)

mysql> insert into t2 values(1.1111111111111111111111111111111);
Query OK, 1 row affected (0.00 sec)

mysql> insert into t3 values(1.1111111111111111111111111111111);
Query OK, 1 row affected, 1 warning (0.01 sec)

mysql> select * from t1; #随着小数的增多，精度开始不准确
+----------------------------------+
| x                                |
+----------------------------------+
| 1.111111164093017600000000000000 |
+----------------------------------+
row in set (0.00 sec)

mysql> select * from t2; #精度比float要准确点，但随着小数的增多，同样变得不准确
+----------------------------------+
| x                                |
+----------------------------------+
| 1.111111111111111200000000000000 |
+----------------------------------+
row in set (0.00 sec)

mysql> select * from t3; #精度始终准确,d为30，于是只留了30位小数
+----------------------------------+
| x                                |
+----------------------------------+
| 1.111111111111111111111111111111 |
+----------------------------------+
row in set (0.00 sec)
```

##### 2.日期类型

表示时间值的日期和时间类型为DATETIME、DATE、TIMESTAMP、TIME和YEAR。

每个时间类型有一个有效值范围和一个"零"值，当指定不合法的MySQL不能表示的值时使用"零"值。

TIMESTAMP类型有专有的自动更新特性，将在后面描述。

作用：存储用户注册时间，文章发布时间，员工入职时间，出生时间，过期时间等

类型格式：

```mysql
        YEAR
            YYYY（1901/2155）

        DATE
            YYYY-MM-DD（1000-01-01/9999-12-31）

        TIME
            HH:MM:SS（'-838:59:59'/'838:59:59'）

        DATETIME

            YYYY-MM-DD HH:MM:SS（1000-01-01 00:00:00/9999-12-31 23:59:59    Y）

        TIMESTAMP

            YYYYMMDD HHMMSS（1970-01-01 00:00:00/2037 年某时）
```

示例：

```mysql
MariaDB [db1]> create table student(
    -> id int,
    -> name varchar(20),
    -> born_year year,
    -> birth date,
    -> class_time time,
    -> reg_time datetime);

MariaDB [db1]> insert into student values
    -> (1,'alex',"1995","1995-11-11","11:11:11","2017-11-11 11:11:11"),
    -> (2,'egon',"1997","1997-12-12","12:12:12","2017-12-12 12:12:12"),
    -> (3,'wsb',"1998","1998-01-01","13:13:13","2017-01-01 13:13:13");

MariaDB [db1]> select * from student;
+------+------+-----------+------------+------------+---------------------+
| id   | name | born_year | birth      | class_time | reg_time            |
+------+------+-----------+------------+------------+---------------------+
|    1 | alex |      1995 | 1995-11-11 | 11:11:11   | 2017-11-11 11:11:11 |
|    2 | egon |      1997 | 1997-12-12 | 12:12:12   | 2017-12-12 12:12:12 |
|    3 | wsb  |      1998 | 1998-01-01 | 13:13:13   | 2017-01-01 13:13:13 |
+------+------+-----------+------------+------------+---------------------+
```

注意：

```mysql
1. 单独插入时间时，需要以字符串的形式，按照对应的格式插入
2. 插入年份时，尽量使用4位值
3. 插入两位年份时，<=69，以20开头，比如50,  结果2050      
                >=70，以19开头，比如71，结果1971
MariaDB [db1]> create table t12(y year);
MariaDB [db1]> insert into t12 values  
    -> (50),
    -> (71);
MariaDB [db1]> select * from t12;
+------+
| y    |
+------+
| 2050 |
| 1971 |
+------+
```

| 类型      | 大小 (字节) | 范围                                                         | 格式                | 用途                     |
| :-------- | :---------- | :----------------------------------------------------------- | :------------------ | :----------------------- |
| DATE      | 3           | 1000-01-01/9999-12-31                                        | YYYY-MM-DD          | 日期值                   |
| TIME      | 3           | '-838:59:59'/'838:59:59'                                     | HH:MM:SS            | 时间值或持续时间         |
| YEAR      | 1           | 1901/2155                                                    | YYYY                | 年份值                   |
| DATETIME  | 8           | 1000-01-01 00:00:00/9999-12-31 23:59:59                      | YYYY-MM-DD HH:MM:SS | 混合日期和时间值         |
| TIMESTAMP | 4           | 1970-01-01 00:00:00/2038结束时间是第 **2147483647** 秒，北京时间 **2038-1-19 11:14:07**，格林尼治时间 2038年1月19日 凌晨 03:14:07 | YYYYMMDD HHMMSS     | 混合日期和时间值，时间戳 |

##### 3.字符串类型

字符串类型指CHAR、VARCHAR、BINARY、VARBINARY、BLOB、TEXT、ENUM和SET。该节描述了这些类型如何工作以及如何在查询中使用这些类型。

| 类型       | 大小                | 用途                            |
| :--------- | :------------------ | :------------------------------ |
| CHAR       | 0-255字节           | 定长字符串                      |
| VARCHAR    | 0-65535 字节        | 变长字符串                      |
| TINYBLOB   | 0-255字节           | 不超过 255 个字符的二进制字符串 |
| TINYTEXT   | 0-255字节           | 短文本字符串                    |
| BLOB       | 0-65 535字节        | 二进制形式的长文本数据          |
| TEXT       | 0-65 535字节        | 长文本数据                      |
| MEDIUMBLOB | 0-16 777 215字节    | 二进制形式的中等长度文本数据    |
| MEDIUMTEXT | 0-16 777 215字节    | 中等长度文本数据                |
| LONGBLOB   | 0-4 294 967 295字节 | 二进制形式的极大文本数据        |
| LONGTEXT   | 0-4 294 967 295字节 | 极大文本数据                    |

注意：char和varchar括号内的参数指的都是字符的长度。

```mysql
# char类型：定长，简单粗暴，浪费空间，存取速度快
    字符长度范围：0-255（一个中文是一个字符，是utf8编码的3个字节）
    存储：
        存储char类型的值时，会往右填充空格来满足长度
        例如：指定长度为10，存>10个字符则报错，存<10个字符则用空格填充直到凑够10个字符存储

    检索：
        在检索或者说查询时，查出的结果会自动删除尾部的空格，除非我们打开pad_char_to_full_length SQL模式（SET sql_mode = 'PAD_CHAR_TO_FULL_LENGTH';）

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# varchar类型：变长，精准，节省空间，存取速度慢
    字符长度范围：0-65535（如果大于21845会提示用其他类型 。mysql行最大限制为65535字节，字符编码为utf-8：https://dev.mysql.com/doc/refman/5.7/en/column-count-limit.html）
    存储：
        varchar类型存储数据的真实内容，不会用空格填充，如果'ab  ',尾部的空格也会被存起来
    强调：varchar类型会在真实数据前加1-2Bytes的前缀，该前缀用来表示真实数据的bytes字节数（1-2Bytes最大表示65535个数字，正好符合mysql对row的最大字节限制，即已经足够使用）
        如果真实的数据<255bytes则需要1Bytes的前缀（1Bytes=8bit 2**8最大表示的数字为255）
        如果真实的数据>255bytes则需要2Bytes的前缀（2Bytes=16bit 2**16最大表示的数字为65535）

    检索：
        尾部有空格会保存下来，在检索或者说查询时，也会正常显示包含空格在内的内容
```

备注：

```mysql
length： 查看字节数
char_length: 查看字符数
```

**char填充空格来满足固定长度，在检索或者说查询时，查出的结果会自动删除尾部的空格，然后修改sql_mode让其现出原形**

示例：

```mysql
mysql> create table t1(x char(5),y varchar(5));
Query OK, 0 rows affected (0.26 sec)

# char存5个字符，而varchar存4个字符
mysql> insert into t1 values('我是五 ','我是四 ');
Query OK, 1 row affected (0.05 sec)

mysql> SET sql_mode='';
Query OK, 0 rows affected, 1 warning (0.00 sec)

# 检索时，char查出的结果会自动删除尾部的空格，而varchar，存了多少，就显示多少
mysql> select x,char_length(x),y,char_length(y) from t1; 
+-----------+----------------+------------+----------------+
| x         | char_length(x) | y          | char_length(y) |
+-----------+----------------+------------+----------------+
| 我是五    |              3 | 我是四     |              4 |
+-----------+----------------+------------+----------------+
row in set (0.00 sec)

# 让char现出原形
mysql> SET sql_mode = 'PAD_CHAR_TO_FULL_LENGTH';
Query OK, 0 rows affected (0.00 sec)

# 这下子char原形毕露了......
mysql> select x,char_length(x),y,char_length(y) from t1;
+-------------+----------------+------------+----------------+
| x           | char_length(x) | y          | char_length(y) |
+-------------+----------------+------------+----------------+
| 我是五      |              5 | 我是四     |              4 |
+-------------+----------------+------------+----------------+
row in set (0.00 sec)


# char类型：3个中文字符+2个空格=11Bytes
# varchar类型:3个中文字符+1个空格=10Bytes
mysql> select x,length(x),y,length(y) from t1;
+-------------+-----------+------------+-----------+
| x           | length(x) | y          | length(y) |
+-------------+-----------+------------+-----------+
| 我是五      |        11 | 我是四     |        10 |
+-------------+-----------+------------+-----------+
row in set (0.00 sec)
```

**虽然 CHAR 和 VARCHAR 的存储方式不太相同,但是对于两个字符串的比较,都只比较其值,忽略 CHAR 值存在的右填充,即使将 SQL _MODE 设置为 PAD_CHAR_TO_FULL_ LENGTH 也一样,但这不适用于like.**

```mysql
mysql> CREATE TABLE names (myname CHAR(10));
Query OK, 0 rows affected (0.03 sec)

mysql> INSERT INTO names VALUES ('ike  ');
Query OK, 1 row affected (0.00 sec)

mysql> select * from names where myname='ike';
+------------+
| myname     |
+------------+
| ike        |
+------------+
1 row in set (0.00 sec)

mysql> select * from names where myname like 'ike';
+---------------------+-----------------------+
| myname LIKE 'Monty' | myname LIKE 'Monty  ' |
+---------------------+-----------------------+
|                   1 |                     0 |
+---------------------+-----------------------+
Empty set (0.00 sec)
```

总结：

![img](http://book.luffycity.com/python-book/assets/chapter8/%E5%AD%97%E7%AC%A6%E7%B1%BB%E5%9E%8B.png)

总结：

```
#常用字符串系列：char与varchar
规定长度后，char存取速度快，有几个存取几个，varchar每次存都需要先加1byte，增加了存取速度。
注：虽然varchar使用起来较为灵活，但是从整个系统的性能角度来说，char数据类型的处理速度更快，有时甚至可以超出varchar处理速度的50%。因此，用户在设计数据库时应当综合考虑各方面的因素，以求达到最佳的平衡

#其他字符串系列（效率：char>varchar>text）
TEXT系列 TINYTEXT TEXT MEDIUMTEXT LONGTEXT
BLOB 系列    TINYBLOB BLOB MEDIUMBLOB LONGBLOB 
BINARY系列 BINARY VARBINARY

text：text数据类型用于保存变长的大字符串，可以组多到65535 (2**16 − 1)个字符。
mediumtext：A TEXT column with a maximum length of 16,777,215 (2**24 − 1) characters.
longtext：A TEXT column with a maximum length of 4,294,967,295 or 4GB (2**32 − 1) characters.
```

##### 4.枚举类型与集合类型

字段的值只能在给定范围中选择，如单选框，多选框。

enum，单选：只能在给定的范围内选一个值，如：性别 sex 男male/女female

set，多选：在给定的范围内可以选择一个或一个以上的值（爱好1,爱好2,爱好3...）

示例：

```python
mysql> create table consumer(
    ->  id int,
    ->  name char(16),
    ->  sex enum('male','female','other'),  # 在指定范围内选一个
    ->  level enum('vip1','vip2','vip3'),  # 在指定范围内选一个
    ->  hobbies set('play','music','read','run')  # 在指定范围内选多个
    -> );
mysql> insert into consumer values
    -> (1,'java','male','vip2','music,read');
Query OK, 1 row affected (0.12 sec)

mysql> select * from consumer;
+------+------+------+-------+------------+
| id   | name | sex  | level | hobbies    |
+------+------+------+-------+------------+
|    1 | java | male | vip2  | music,read |
+------+------+------+-------+------------+
1 row in set (0.00 sec)

mysql> insert into consumer values
    -> (1,'python','xxxxx','vip2','music,read');
Query OK, 1 row affected, 1 warning (0.14 sec)

mysql> select * from consumer;
+------+--------+------+-------+------------+
| id   | name   | sex  | level | hobbies    |
+------+--------+------+-------+------------+
|    1 | java   | male | vip2  | music,read |
|    1 | python |      | vip2  | music,read |
+------+--------+------+-------+------------+
```

##### 5. 约束

约束条件与数据类型的宽度一样，都是可选参数。

作用：用于保证数据的完整性和一致性

分为：

- PRIMARY KEY (PK) ，标识该字段为该表的主键，可以唯一的标识记录。
- FOREIGN KEY (FK)， 标识该字段为该表的外键。
- NOT NULL ，标识该字段不能为空。
- UNIQUE KEY (UK)，标识该字段的值是唯一的。
- AUTO_INCREMENT，标识该字段的值自动增长（整数类型，而且为主键）。
- DEFAULT，为该字段设置默认值。
- UNSIGNED，无符号。
- ZEROFILL，使用0填充。

说明：

```mysql
1. 是否允许为空，默认NULL，可设置NOT NULL，字段不允许为空，必须赋值
2. 字段是否有默认值，缺省的默认值是NULL，如果插入记录时不给字段赋值，此字段使用默认值
sex enum('male','female') not null default 'male'
age int unsigned NOT NULL default 20 必须为正值（无符号） 不允许为空 默认是20
3. 是否是key
主键 primary key
外键 foreign key
索引 (index,unique...)
```

**not null与default**：

是否可空，not null - 不可空，null - 可空。

默认值，创建列时可以指定默认值，当插入数据时如果未主动设置，则自动添加默认值。

示例：

not null：

```mysql
mysql> create table t2(id int not null);  # 设置字段id不为空
mysql> desc t2;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| id    | int(11) | NO   |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
mysql> insert into t2 values(); #不能插入空
ERROR 1364 (HY000): Field 'id' doesn't have a default value
```

null：

```mysql
mysql> create table t1(id int);  # id字段默认可以插入空
mysql> desc t1;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| id    | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
mysql> insert into t1 values(); # 可以插入空
```

default：

```mysql
# 设置id字段有默认值后，则无论id字段是null还是not null，都可以插入空，插入空默认填入default指定的默认值
mysql> create table t3(id int default 1);
mysql> alter table t3 modify id int not null default 1;
```

综合：

```mysql
mysql> create table student(
    -> name varchar(20) not null,
    -> age int(3) unsigned not null default 18,
    -> sex enum('male','female') default 'male',
    -> hobby set('play','study','read','music') default 'play,music'
    -> );
mysql> desc student;
+-------+------------------------------------+------+-----+------------+-------+
| Field | Type                               | Null | Key | Default    | Extra |
+-------+------------------------------------+------+-----+------------+-------+
| name  | varchar(20)                        | NO   |     | NULL       |       |
| age   | int(3) unsigned                    | NO   |     | 18         |       |
| sex   | enum('male','female')              | YES  |     | male       |       |
| hobby | set('play','study','read','music') | YES  |     | play,music |       |
+-------+------------------------------------+------+-----+------------+-------+
```

**unique**：

设置唯一约束，不能重复。

示例：

```mysql
# 单列唯一
# 方式一：
create table department(
	id int unique,
	name char(10) unique
);
#方式二：
create table department(
	id int,
	name char(10),
	unique(id),
	unique(name)
);
mysql> insert into department values(1,'IT');
Query OK, 1 row affected (0.00 sec)
mysql> insert into department values(1,'IT');
ERROR 1062 (23000): Duplicate entry '1' for key 'id'

# 联合唯一
create table services(
	id int,
	ip char(15),
	port int,
	unique(id),
	unique(ip,port)
);

mysql> insert into services values
    -> (1,'192.168.11.10',80),
    -> (2,'192.168.11.10',81),
    -> (3,'192.168.11.13',80);
Query OK, 3 rows affected (0.12 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> insert into services values
    -> (4,'192.168.11.10',80);
ERROR 1062 (23000): Duplicate entry '192.168.11.10-80' for key 'ip'
```

**primary key**：

primary key字段的值不为空且唯一，存储引擎（innodb）:对于innodb存储引擎来说，一张表内必须有一个主键。

一张表中可以：

- 单列做主键
- 多列做主键（复合主键）
- 一张表中只能有一个主键

示例：

```mysql
mysql> # 单列主键
mysql> create table t17(
    ->  id int primary key,
    ->  name char(16)
    -> );
Query OK, 0 rows affected (0.85 sec)

mysql> insert into t17 values
    -> (1,'egon'),
    -> (2,'alex');
Query OK, 2 rows affected (0.06 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> insert into t17 values
    -> (2,'wxx');
ERROR 1062 (23000): Duplicate entry '2' for key 'PRIMARY'

mysql> desc t17;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| id    | int(11)  | NO   | PRI | NULL    |       |
| name  | char(16) | YES  |     | NULL    |       |
+-------+----------+------+-----+---------+-------+
2 rows in set (0.01 sec)
mysql> create table t18(
    ->  id int not null unique,
    ->  name char(16)
    -> );
Query OK, 0 rows affected (0.40 sec)

mysql> desc t18;  # not null + unique 等同于 primary key
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| id    | int(11)  | NO   | PRI | NULL    |       |
| name  | char(16) | YES  |     | NULL    |       |
+-------+----------+------+-----+---------+-------+
2 rows in set (0.01 sec)

mysql> # 复合主键
mysql> create table t19(
    ->  ip char(15),
    ->  port int,
    ->  primary key(ip,port)
    -> );
Query OK, 0 rows affected (0.95 sec)

mysql> insert into t19 values
    -> ('1.1.1.1',80),
    -> ('1.1.1.1',81);
Query OK, 2 rows affected (0.04 sec)
Records: 2  Duplicates: 0  Warnings: 0
mysql> insert into t19 values
    -> ('1.1.1.1',82);
ERROR 1062 (23000): Duplicate entry '1.1.1.1-82' for key 'PRIMARY'
mysql> desc t19;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| ip    | char(15) | NO   | PRI |         |       |
| port  | int(11)  | NO   | PRI | 0       |       |
+-------+----------+------+-----+---------+-------+
2 rows in set (0.01 sec)
```

**auto_increment**：

约束字段为自动增长，被约束的字段必须同时被key约束。

示例：

```python
# id为自增长
mysql> create table t20(
    ->  id int primary key auto_increme
    ->  name char(16)
    -> );
Query OK, 0 rows affected (0.38 sec)
mysql> desc t20;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(11)  | NO   | PRI | NULL    | auto_increment |
| name  | char(16) | YES  |     | NULL    |                |
+-------+----------+------+-----+---------+----------------+
2 rows in set (0.01 sec)

mysql> insert into t20(name) values
    -> ('egon'),
    -> ('alex'),
    -> ('wxx');
Query OK, 3 rows affected (0.12 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> insert into t20(id,name) values
    -> (7,'yuanhao');
Query OK, 1 row affected (0.12 sec)

# 指定id后，在指定的基础上自增长
mysql> insert into t20(name) values
    -> ('egon1'),
    -> ('egon2'),
    -> ('egon3');
Query OK, 3 rows affected (0.06 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from t20;
+----+---------+
| id | name    |
+----+---------+
|  1 | egon    |
|  2 | alex    |
|  3 | wxx     |
|  7 | yuanhao |
|  8 | egon1   |
|  9 | egon2   |
| 10 | egon3   |
+----+---------+
7 rows in set (0.00 sec)
```

修改步长及偏移量：

强调：起始偏移量<=步长

```mysql
show variables like 'auto_inc%';

#步长：
auto_increment_increment默认为1
#起始偏移量
auto_increment_offset默认1

#设置步长
set session auto_increment_increment=5;
set global auto_increment_increment=5;

#设置起始偏移量
set global auto_increment_offset=3;
强调：起始偏移量<=步长

mysql> show variables like 'auto_inc%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| auto_increment_increment | 5     |
| auto_increment_offset    | 3     |
+--------------------------+-------+
2 rows in set (0.00 sec)

create table t21(
	id int primary key auto_increment,
	name char(16)
);

insert into t21(name) values
('egon'),
('alex'),
('wxx'),
('yxx');
mysql> select * from t21;
+----+------+
| id | name |
+----+------+
|  3 | egon |
|  8 | alex |
| 13 | wxx  |
| 18 | yxx  |
+----+------+
```

清空表：

```mysql
# 如果有自增id，新增的数据，仍然是以删除前的最后一样作为起始。
mysql> delete from t20;
Query OK, 1 row affected (0.10 sec)

mysql> show create table t20 \G;
*************************** 1. row ***************************
       Table: t20
Create Table: CREATE TABLE `t20` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(16) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8
1 row in set (0.00 sec)

ERROR:
No query specified

mysql> select * from t20;
Empty set (0.00 sec)

mysql>  insert into t20(name) values
    ->  ('xxx');
Query OK, 1 row affected (0.21 sec)

mysql> select * from t20;
+----+------+
| id | name |
+----+------+
|  2 | xxx  |
+----+------+

# 数据量大，删除速度比上一条快，且直接从零开始，
mysql> truncate t20;
Query OK, 0 rows affected (0.46 sec)

mysql> insert into t20(name) values
    ->  ('xxx');
Query OK, 1 row affected (0.14 sec)

mysql> select * from t20;
+----+------+
| id | name |
+----+------+
|  1 | xxx  |
+----+------+
1 row in set (0.00 sec)
```

**foreign key**：

建立表之间的关系。

```mysql
# 建立表关系
# 先建被关联的表,并且保证被关联的字段唯一
create table dep(
	id int primary key,
	name char(16),
	comment char(50)
);

#再建立关联的表
create table emp(
	id int primary key,
	name char(10),
	sex enum('male','female'),
	dep_id int,
	foreign key(dep_id) references dep(id) 
	on delete cascade  # 同步删除
	on update cascade  # 同步更新
);
# 插入数据
# 先往被关联表插入记录
insert into dep values
(1,"IT","技术能力有限部门"),
(2,"销售","销售能力不足部门"),
(3,"财务","花钱特别多部门");

# 再往关联表插入记录
insert into emp values
(1,'egon','male',1),
(2,'alex','male',1),
(3,'wupeiqi','female',2),
(4,'yuanhao','male',3),
(5,'jinximn','male',2);

# 删除数据
delete from emp where dep_id=1;
delete from dep where id=1;
# 没有同步操作的情况下，先删/更新除关联的数据，再删除/更新被关联的数据，删除/更新表也是。
# 同步的情况下，删除/更新关联的数据，被关联的表也跟着删除/更新数据，删除/更新表也是。
```

**建表之间的关系**：

- 多对一
    - 左表的多条记录对应右表的一条记录，右表的多条记录对应左表的一条记录
    - 关联方式：foreign key
- 多对多
    - 左表的多条记录对应右表的多条记录，右表的多条记录对应左表的多条记录
    - 关联方式：foreign key + 一张新的表
- 一对一
    - 左表的一条记录对应右表的一条记录，右表的一条记录对应左表的一条记录
    - 关联方式：foreign key + unique

示例：多对一

```mysql
# 建表
create table press(
id int primary key auto_increment,
name varchar(20)
);

create table book(
id int primary key auto_increment,
name varchar(20),
press_id int not null,
foreign key(press_id) references press(id)
on delete cascade
on update cascade
);
# 建数据
insert into press(name) values
('北京工业地雷出版社'),
('人民音乐不好听出版社'),
('知识产权没有用出版社')
;

insert into book(name,press_id) values
('九阳神功',1),
('九阴真经',2),
('九阴白骨爪',2),
('独孤九剑',3),
('降龙十巴掌',2),
('葵花宝典',3)
;
```

示例：多对多

```mysql
# 建表
create table author(
id int primary key auto_increment,
name varchar(20)
);
# 这张表就存放作者表与书表的关系，即查询二者的关系查这表就可以了
create table author2book(
id int not null unique auto_increment,
author_id int not null,
book_id int not null,
constraint fk_author foreign key(author_id) references author(id)
on delete cascade
on update cascade,
constraint fk_book foreign key(book_id) references book(id)
on delete cascade
on update cascade,
primary key(author_id,book_id)
);

# 建数据
# 插入四个作者，id依次排开
insert into author(name) values('aa'),('bb'),('cc'),('dd');
# 每个作者与自己的代表作如下
aa: 
九阳神功
九阴真经
九阴白骨爪
独孤九剑
降龙十巴掌
葵花宝典
bb: 
九阳神功
葵花宝典
cc:
独孤九剑
降龙十巴掌
葵花宝典
dd:
九阳神功

insert into author2book(author_id,book_id) values
(1,1),
(1,2),
(1,3),
(1,4),
(1,5),
(1,6),
(2,1),
(2,6),
(3,4),
(3,5),
(3,6),
(4,1)
;
```

示例：一对一

```mysql
# 建表
create table customer(
id int primary key auto_increment,
name varchar(20) not null,
qq varchar(10) not null,
phone char(16) not null
);
create table student(
id int primary key auto_increment,
class_name varchar(20) not null,
customer_id int unique,  # 该字段一定要是唯一的
foreign key(customer_id) references customer(id)  # 外键的字段一定要保证unique
on delete cascade
on update cascade
);

# 建数据
#增加客户
insert into customer(name,qq,phone) values
('李飞机','31811231',13811341220),
('王大炮','123123123',15213146809),
('守榴弹','283818181',1867141331),
('吴坦克','283818181',1851143312),
('赢火箭','888818181',1861243314),
('战地雷','112312312',18811431230)
;
#增加学生
insert into student(class_name,customer_id) values
('脱产3班',3),
('周末19期',4),
('周末19期',5)
;
```

#### 4.数据库操作

##### 1.数据的增删改

在MySQL管理软件中，可以通过SQL语句中的DML语言来实现数据的操作，包括：

- 使用INSERT实现数据的插入
- UPDATE实现数据的更新
- 使用DELETE实现数据的删除
- 使用SELECT查询数据以及。

**插入数据INSERT**：

语法：

```
1. 插入完整数据（顺序插入）
    语法一：
    INSERT INTO 表名(字段1,字段2,字段3…字段n) VALUES(值1,值2,值3…值n);

    语法二：
    INSERT INTO 表名 VALUES (值1,值2,值3…值n);

2. 指定字段插入数据
    语法：
    INSERT INTO 表名(字段1,字段2,字段3…) VALUES (值1,值2,值3…);

3. 插入多条记录
    语法：
    INSERT INTO 表名 VALUES
        (值1,值2,值3…值n),
        (值1,值2,值3…值n),
        (值1,值2,值3…值n);

4. 插入查询结果
    语法：
    INSERT INTO 表名(字段1,字段2,字段3…字段n) 
                    SELECT (字段1,字段2,字段3…字段n) FROM 表2
                    WHERE …;
```

**更新数据UPDATE**：

语法：

```
语法：
    UPDATE 表名 SET
        字段1=值1,
        字段2=值2,
        WHERE CONDITION;

示例：
    update student set class_name='全栈开发' where id=1;
```

**删除数据DELETE**：

语法：

```
语法：
    DELETE FROM 表名 
        WHERE CONITION;

示例：
    DELETE FROM sutdent 
        WHERE id=1;
```

##### 2.单表查询

语法：

```
SELECT 字段1,字段2. FROM 表名
                   WHERE 条件
                   GROUP BY 分组条件
                   HAVING 筛选
                   ORDER BY 排序字段
                   LIMIT 限制条数
```

**关键字执行的优先级：**

```
重点中的重点：关键字的执行优先级
1.from  # 找到表:from
2.where  # 拿着where指定的约束条件，去表中过滤出数据
3.group by  # 将过滤出的数据进行分组group by，如果没有group by，则整体作为一组
4.having  # 将分组的结果进行having过滤
5.select  # 执行select
6.distinct # 去重
7.order by # 将结果按条件排序：order by
8.limit # 限制结果的显示条数
```

建表：

```
# 建表
create table employee(
id int not null unique auto_increment,
name varchar(20) not null,
sex enum('male','female') not null default 'male', #大部分是男的
age int(3) unsigned not null default 28,
hire_date date not null,
post varchar(50),
post_comment varchar(100),
salary double(15,2),
office int, #一个部门一个屋子
depart_id int
);
# 建数据
#三个部门：教学，销售，运营
insert into employee(name,sex,age,hire_date,post,salary,office,depart_id) values
('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33,401,1), #以下是教学部
('alex','male',78,'20150302','teacher',1000000.31,401,1),
('wupeiqi','male',81,'20130305','teacher',8300,401,1),
('yuanhao','male',73,'20140701','teacher',3500,401,1),
('liwenzhou','male',28,'20121101','teacher',2100,401,1),
('jingliyang','female',18,'20110211','teacher',9000,401,1),
('jinxin','male',18,'19000301','teacher',30000,401,1),
('成龙','male',48,'20101111','teacher',10000,401,1),

('歪歪','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
('丫丫','female',38,'20101101','sale',2000.35,402,2),
('丁丁','female',18,'20110312','sale',1000.37,402,2),
('星星','female',18,'20160513','sale',3000.29,402,2),
('格格','female',28,'20170127','sale',4000.33,402,2),

('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
('程咬金','male',18,'19970312','operation',20000,403,3),
('程咬银','female',18,'20130311','operation',19000,403,3),
('程咬铜','male',18,'20150411','operation',18000,403,3),
('程咬铁','female',18,'20140512','operation',17000,403,3)
;
```

**简单查询**：

```
#简单查询
    SELECT id,name,sex,age,hire_date,post,post_comment,salary,office,depart_id 
    FROM employee;

    SELECT * FROM employee;

    SELECT name,salary FROM employee;

#避免重复DISTINCT
    SELECT DISTINCT post FROM employee;    

#通过四则运算查询
    SELECT name, salary*12 FROM employee;
    SELECT name, salary*12 AS Annual_salary FROM employee;
    SELECT name, salary*12 Annual_salary FROM employee;

#定义显示格式
   CONCAT() 函数用于连接字符串
   SELECT CONCAT('姓名: ',name,'  年薪: ', salary*12)  AS Annual_salary 
   FROM employee;

   CONCAT_WS() 第一个参数为分隔符
   SELECT CONCAT_WS(':',name,salary*12)  AS Annual_salary 
   FROM employee;
```

**WHERE约束**：

where字句中可以使用：

- 比较运算符：><>= <= <> !=
- between 80 and 100 值在80到100之间
- in(80,90,100) 值是80或90或100
- ike 'egon%'
    pattern可以是%或_，
    %表示任意多字符
    _表示一个字符

- 逻辑运算符：在多个条件直接可以使用逻辑运算符 and or not

```
# 1:单条件查询：查询岗位为sale的员工
    SELECT name FROM employee
        WHERE post='sale';

# 2:多条件查询：查询岗位为老师以及工资大于10000的员工
    SELECT name,salary FROM employee
        WHERE post='teacher' AND salary>10000;

# 3:关键字BETWEEN AND：查询工资在10000到20000之间的员工
    SELECT name,salary FROM employee 
        WHERE salary BETWEEN 10000 AND 20000;

    SELECT name,salary FROM employee 
        WHERE salary NOT BETWEEN 10000 AND 20000;

# 4:关键字IS NULL(判断某个字段是否为NULL不能用等号，需要用IS)
# 查询岗位描述为空的员工
    SELECT name,post_comment FROM employee 
        WHERE post_comment IS NULL;
# 查询岗位描述不为空的员工
    SELECT name,post_comment FROM employee 
        WHERE post_comment IS NOT NULL;

    SELECT name,post_comment FROM employee 
        WHERE post_comment=''; 注意''是空字符串，不是null
    ps：
        执行
        update employee set post_comment='' where id=2;
        再用上条查看，就会有结果了

# 5:关键字IN集合查询：查询工资是3000或4000或9000的员工
    SELECT name,salary FROM employee 
        WHERE salary=3000 OR salary=4000 OR salary=9000 ;
# 查询工资是3000或4000或9000的员工
    SELECT name,salary FROM employee 
        WHERE salary IN (3000,3500,9000) ;
# 查询工资是3000或4000或9000之外的员工
    SELECT name,salary FROM employee 
        WHERE salary NOT IN (3000,3500,4000,9000) ;

# 6:关键字LIKE模糊查询
    通配符’%’：查询名字包括eg的员工信息
    SELECT * FROM employee 
            WHERE name LIKE 'eg%';

    通配符’_’：查询名字开头是al的四个字的员工信息
    SELECT * FROM employee 
            WHERE name LIKE 'al__';
```

**分组查询**：

什么是分组，为什么进行分组？

- 分组发生在where之后，即分组是基于where之后得到的记录而进行的

- 分组指的是：将所有记录按照某个相同字段进行归类，比如针对员工信息表的职位分组，或者按照性别进行分组等。

- 为何要分组呢？
        以组为单位进行统计

    ​	‘每’这个字后面的字段就是我们分组的依据

```
# 分组之后，只能取分组的字段，以及每个组聚合结果
set global sql_mode="ONLY_FULL_GROUP_BY"; 
```

```
单独使用GROUP BY关键字分组
    SELECT post FROM employee GROUP BY post;
    注意：我们按照post字段分组，那么select查询的字段只能是post，想要获取组内的其他相关信息，需要借助函数

GROUP BY关键字和GROUP_CONCAT()函数一起使用
    SELECT post,GROUP_CONCAT(name) FROM employee GROUP BY post;#按照岗位分组，并查看组内成员名
    SELECT post,GROUP_CONCAT(name) as emp_members FROM employee GROUP BY post;

GROUP BY与聚合函数一起使用
    select post,count(id) as count from employee group by post;#按照岗位分组，并查看每个组有多少人
```

示例：

```
mysql> select * from emp group by post; 
+----+------+--------+-----+------------+----------------------------+--------------+------------+--------+-----------+
| id | name | sex    | age | hire_date  | post                       | post_comment | salary     | office | depart_id |
+----+------+--------+-----+------------+----------------------------+--------------+------------+--------+-----------+
| 14 | 张野 | male   |  28 | 2016-03-11 | operation                  | NULL         |   10000.13 |    403 |         3 |
|  9 | 歪歪 | female |  48 | 2015-03-11 | sale                       | NULL         |    3000.13 |    402 |         2 |
|  2 | alex | male   |  78 | 2015-03-02 | teacher                    | NULL         | 1000000.31 |    401 |         1 |
|  1 | egon | male   |  18 | 2017-03-01 | 老男孩驻沙河办事处外交大使 | NULL         |    7300.33 |    401 |         1 |
+----+------+--------+-----+------------+----------------------------+--------------+------------+--------+-----------+
rows in set (0.00 sec)


#由于没有设置ONLY_FULL_GROUP_BY,于是也可以有结果，默认都是组内的第一条记录，但其实这是没有意义的

mysql> set global sql_mode='ONLY_FULL_GROUP_BY';
Query OK, 0 rows affected (0.00 sec)

mysql> quit #设置成功后，一定要退出，然后重新登录方可生效
Bye

mysql> use db1;
Database changed
mysql> select * from emp group by post; #报错
ERROR 1055 (42000): 'db1.emp.id' isn't in GROUP BY
mysql> select post,count(id) from emp group by post; #只能查看分组依据和使用聚合函数
+----------------------------+-----------+
| post                       | count(id) |
+----------------------------+-----------+
| operation                  |         5 |
| sale                       |         5 |
| teacher                    |         7 |
| 老男孩驻沙河办事处外交大使 |         1 |
+----------------------------+-----------+
rows in set (0.00 sec)
```

强调：

```
如果我们用unique的字段作为分组的依据，则每一条记录自成一组，这种分组没有意义
多条记录之间的某个字段值相同，该字段通常用来作为分组的依据
```

**聚合函数**：

- max
- min
- avg
- sum
- count

强调：没有group by则默认整体算作一组

示例：

```
# 1.查询岗位名以及岗位包含的所有员工名字
select post,group_concat(name) from employee group by post;
# 2.查询岗位名以及各岗位内包含的员工个数
select post,count(id) from employee group by post;
# 3.查询公司内男员工和女员工的个数
select sex,count(id) from employee group by sex;
# 4.查询岗位名以及各岗位的平均薪资
select post,avg(salary) from employee group by post;
5.查询岗位名以及各岗位的最高薪资
# select post,max(salary) from employee group by post;
6.查询岗位名以及各岗位的最低薪资
# select post,min(salary) from employee group by post;
7.查询男员工与男员工的平均薪资，女员工与女员工的平均薪资
# select sex,avg(salary) from employee group by sex;
```

**HAVING过滤**：

having和where的区别：

- 执行优先级：where > group by > having
- Where 发生在分组group by之前，因而Where中可以有任意字段，但是绝对不能使用聚合函数。
- Having发生在分组group by之后，因而Having中可以使用分组的字段，无法直接取到其他字段,可以使用聚合函数。

```
# 1.查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
select post,group_concat(name),count(id) from employee group by post having count(id) < 2;
# 2.查询各岗位平均薪资大于10000的岗位名、平均工资
select post,avg(salary) from employee group by post having avg(salary) > 10000;
# 3.查询各岗位平均薪资大于10000且小于20000的岗位名、平均工资
# select post,avg(salary) from employee group by post having avg(salary) > 10000 and avg(salary) <20000;
```

**排序查询**：

```
按单列排序
    SELECT * FROM employee ORDER BY salary;
    SELECT * FROM employee ORDER BY salary ASC;  # 升序
    SELECT * FROM employee ORDER BY salary DESC;  # 降序

按多列排序:先按照age排序，如果年纪相同，则按照薪资排序
    SELECT * from employee
        ORDER BY age,
        salary DESC;
```

示例：

```
# 1.查询所有员工信息，先按照age升序排序，如果age相同则按照hire_date降序排序
select * from employee ORDER BY age asc,hire_date desc;
# 2.查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资升序排列
select post,avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) asc;
# 3.查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资降序排列
select post,avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) desc;
```

**限制查询的记录数:LIMIT**：

```
示例：
    SELECT * FROM employee ORDER BY salary DESC 
        LIMIT 3;                    #默认初始位置为0 

    SELECT * FROM employee ORDER BY salary DESC
        LIMIT 0,5; #从第0开始，即先查询出第一条，然后包含这一条在内往后查5条

    SELECT * FROM employee ORDER BY salary DESC
        LIMIT 5,5; #从第5开始，即先查询出第6条，然后包含这一条在内往后查5条
```

示例：

```
# 显示第1-5条数据
mysql> select * from  employee limit 0,5;
# 显示第6-10条数据
mysql> select * from  employee limit 5,5;
# 显示第11-15条数据
mysql> select * from  employee limit 10,5;

```

**正则表达式查询**：

```
SELECT * FROM employee WHERE name REGEXP '^ale';

SELECT * FROM employee WHERE name REGEXP 'on$';
```

##### 3.多表查询