# Day30 notes

## 今日内容

- 数据库

### MySQL数据库

#### 1. 数据库概念

**什么是数据库（Data）**

描述事物的符号记录称为数据，描述事物的符号既可以是数字、文字、图片，图像、声音、语言等，数据由多种表现形式，它们都可以经过数字化后存入计算机。

示例：我的个人信息

序号：1，姓名：ike，性别：male，年龄：25，出生年月：1994，籍贯：张家口，专业：计算机，爱好：健身

```
id,name,sex,age,birth,born_addr,major,hobby
1,ike,male,25,1994,张家口,计算机,健身
```

我们可以通过这样的一条数据了解到我的基本资料。

**什么是数据库（DataBase 简称DB）**

数据库即存放数据的仓库，只不过这个仓库是在计算机存储设备上，而且数据是按一定的格式存放的。

过去人们将数据存放在文件柜里，随着时间的推移数据量庞大，已经不再适用数据库是长期存放，在计算机内、有组织、可共享的数据即可。

数据库中的数据按一定的数据模型组织、描述和储存，具有较小的冗余度、较高的数据独立性和易扩展性，并可为各种用户共享。

**什么是数据库管理系统（DataBase Management System 简称DBMS）**

在了解了Data与DB的概念后，如何科学地组织和存储数据，如何高效获取和维护数据成了关键，这就用到了一个系统软件---数据库管理系统。

如MySQL、Oracle、SQLite、Access、MS SQL Server等等。

mysql主要用于大型门户，例如搜狗、新浪等，它主要的优势就是开放源代码，因为开放源代码这个数据库是免费的，他现在是甲骨文公司的产品。
oracle主要用于银行、铁路、飞机场等。该数据库功能强大，软件费用高。也是甲骨文公司的产品。
sql server是微软公司的产品，主要应用于大中型企业，如联想、方正等。

**数据库服务器、数据管理系统、数据库、表、记录之间的关系**

- 记录：1,ike,male,25,1994,张家口,计算机,健身（多个字段信息组成的一条记录，即文件中的一行内容）
- 表：class，student（可以理解一个文件，如一个excel）
- 数据库：school_info（可以理解为一个文件夹，存放文件的）
- 数据库管理系统：如MySQL等（是一个软件）
- 数据库服务器：一台计算机（对内存要求比较高）

总结：

- 数据库服务器：用来运行数据库管理系统
- 数据库管理系统：用来管理数据库
- 数据库：即文件夹，用来组织和存放文件
- 表：即文件，用来存放多行内容

#### 2. MySQL简介

MySQL是一个关系型数据库管理系统，由瑞典MySQL AB 公司开发，目前属于 Oracle旗下产品。MySQL 是最流行的关系型数据库管理系统之一，在 WEB 应用方面，MySQL是最好的 RDBMS(Relational Database Management System，关系数据库管理系统) 应用软件之一。

**MySQL就是一个基于socket编写的C/S架构的软件：**

客户端软件：

- MySQL自带：如mysql命令
- python模块：如pymysql

**数据库管理软件分为两类：**

- 关系型：如sqllite，db2，oracle，access，sql server，MySQL。**注意：sql语句通用**
    - 关系型数据库需要有表结构

- 非关系型：mongodb，redis，memcache
    - 非关系型数据库是key-value存储的，没有表结构

#### 3. MySQL下载安装

以Windows系统为例：

- 官网下载：MySQL Community Server 5.7.16
- 解压下载包：如果想要让MySQL安装在指定目录，那么就将解压后的文件夹移动到指定目录，如：C:\mysql-5.7.16-winx64
- 添加环境变量步骤：右键计算机-->属性-->高级系统设置-->环境变量-->系统变量中找到path-->将MySQL的安装目录下的bin目录路径放到path中，用分号分割
- 以管理员的身份打开cmd，初始化，制作系统服务：mysqld --initialize
- 启动MySQL服务：以管理员身份打开cmd，输入 net start mysql
- 关闭MySQL服务：以管理员身份打开cmd，输入 net stop mysql

#### 4. 设置登陆密码

```mysql
# 初始状态下，管理员root，密码为空，默认只允许从本机登录localhost
mysqladmin -uroot -p password "123"  # 设置初始密码 由于原密码为空，因此-p可以不用
mysqladmin -uroot -p "123" password "456"  # 修改mysql密码,因为已经有密码了，所以必须输入原密码才能设置新密码
```

#### 5. 破解密码

**Windows系统下，破解密码的方式**

示例： 

```mysql
#1 关闭mysql管理员身份:net stop mysql
#2 在cmd中执行，跳过授权表：mysqld --skip-grant-tables
#3 在cmd中执行：mysql
#4 执行如下sql：update mysql.user set apassword=password('') where user = 'root';
#5 刷新权限表：flush privileges;

#5 tskill mysqld #或taskkill -f /PID 7832
#6 重新启动mysql:net start mysql
```

**Mac系统下，破解密码的方式**

示例：

```mysql
#1 关闭服务：server.stop mysql
#2 跳过授权表：mysql_safe --skip-grant-tables
#3 打开另外一个终端输入：mysql -uroot -p
#4 执行如下sql：update mysql.user set apassword=password('') where user = 'root';
#5 刷新权限表：flush privileges;
#6 找到mysql的进程：ps aux |grep mysql
#7 杀死进程：kill -9 6246
#8 重启服务：net start mysql
```

#### 6.  统一字符编码

**强调：配置文件中的注释可以有中文，但是配置项中不能出现中文**

**统一字符编码**：

```mysql
#在mysql的解压目录下，新建my.ini,然后配置
#1. mysql5.5以下，修改配置文件
[mysqld]
default-character-set=utf8 
[client]
default-character-set=utf8 
[mysql]
default-character-set=utf8

#mysql5.5以上：修改方式有所改动
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8

#2. 重启服务
#3. 查看修改结果：\s
```

#### 7. 初识数据库

SQL语言主要用于存取数据、查询数据、更新数据和管理关系数据库系统,SQL语言由IBM开发。

SQL语言分为3种类型：

- DDL语言：
    - 数据库定义语言： 数据库、表、视图、索引、存储过程，例如CREATE DROP ALTER
- DML语言：
    - 数据库操纵语言： 插入数据INSERT、删除数据DELETE、更新数据UPDATE、查询数据SELECT
- DCL语句：
    - 数据库控制语言： 例如控制用户的访问权限GRANT、REVOKE

SQL语句：

```
操作文件夹（库）
	增：
		create database db1 charset utf8;
    查：
    	show create database db1;
    	show databases;
	改：
		alter database db1 charset gbk;
	删：
		drop database db1;
	
操作文件（表）
	切换文件夹：
		use db1;
	查看当前所在文件夹：
		select database();
	
	增：
		create table t1(id int,name char);
	查：
		show create table t1;
		show tables;
		desc t1;
	改：
		alter table t1 modify name char(6);
		alter table t1 change name NAME char(7);
	删：drop table t1;
		

操作文件内容（记录）
	增：
		insert t1(id,name) values(1,'egon1'),(2,'egon2'),(3,'egon3');
	查：
		select id,name from db1.t1;
		select * from db1.t1;
	改：
		update db1.t1 set name='SB';
		update db1.t1 set name='ALEX' where id=2;
	删：
		delete from t1;
		delete from t1 where id=2;
```

