# Day notes 32

## 今日内容

- 多表查询
- 权限管理

建表：

```mysql
# 建表
create table department(
id int,
name varchar(20) 
);

create table employee(
id int primary key auto_increment,
name varchar(20),
sex enum('male','female') not null default 'male',
age int,
dep_id int
);

# 插入数据
insert into department values
(200,'技术'),
(201,'人力资源'),
(202,'销售'),
(203,'运营');

insert into employee(name,sex,age,dep_id) values
('egon','male',18,200),
('alex','female',48,201),
('wupeiqi','male',38,201),
('yuanhao','female',28,202),
('liwenzhou','male',18,200),
('jingliyang','female',18,204)
;

# 查看表结构和数据
mysql> desc department;
+-------+-------------+------+-----+---------+-------+
| Field | Type | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id | int(11) | YES | | NULL | |
| name | varchar(20) | YES | | NULL | |
+-------+-------------+------+-----+---------+-------+

mysql> desc employee;
+--------+-----------------------+------+-----+---------+----------------+
| Field | Type | Null | Key | Default | Extra |
+--------+-----------------------+------+-----+---------+----------------+
| id | int(11) | NO | PRI | NULL | auto_increment |
| name | varchar(20) | YES | | NULL | |
| sex | enum('male','female') | NO | | male | |
| age | int(11) | YES | | NULL | |
| dep_id | int(11) | YES | | NULL | |
+--------+-----------------------+------+-----+---------+----------------+
```

### 1.多表连接查询

语法：

```mysql
SELECT 字段列表
    FROM 表1 INNER|LEFT|RIGHT JOIN 表2
    ON 表1.字段 = 表2.字段;
```

**内连接**：只连接匹配的行，找两张表共有的部分

```mysql
mysql> select employee.id,employee.name,employee.age,employee.sex,department.name from employee inner join department on employee.dep_id=department.id; 
+----+-----------+------+--------+--------------+
| id | name      | age  | sex    | name         |
+----+-----------+------+--------+--------------+
|  1 | egon      |   18 | male   | 技术         |
|  2 | alex      |   48 | female | 人力资源     |
|  3 | wupeiqi   |   38 | male   | 人力资源     |
|  4 | yuanhao   |   28 | female | 销售         |
|  5 | liwenzhou |   18 | male   | 技术         |
+----+-----------+------+--------+--------------+
```

**左外连接**：优先显示左表全部记录，在内连接的基础上增加左边有右边没有的结果

```mysql
mysql> select employee.id,employee.name,department.name as depart_name from employee left join department on employee.dep_id=department.id;
+----+------------+--------------+
| id | name       | depart_name  |
+----+------------+--------------+
|  1 | egon       | 技术         |
|  5 | liwenzhou  | 技术         |
|  2 | alex       | 人力资源     |
|  3 | wupeiqi    | 人力资源     |
|  4 | yuanhao    | 销售         |
|  6 | jingliyang | NULL         |
+----+------------+--------------+
```

**右外连接**：优先显示右表全部记录，在内连接的基础上增加右边有左边没有的结果

```mysql
mysql> select employee.id,employee.name,department.name as depart_name from employee right join department on employee.dep_id=department.id;
+------+-----------+--------------+
| id   | name      | depart_name  |
+------+-----------+--------------+
|    1 | egon      | 技术         |
|    2 | alex      | 人力资源     |
|    3 | wupeiqi   | 人力资源     |
|    4 | yuanhao   | 销售         |
|    5 | liwenzhou | 技术         |
| NULL | NULL      | 运营         |
+------+-----------+--------------+
```

**全外连接**：显示左右两个表全部记录，在内连接的基础上增加左边有右边没有的和右边有左边没有的结果

```mysql
select * from employee left join department on employee.dep_id = department.id
union
select * from employee right join department on employee.dep_id = department.id
;
#查看结果
+------+------------+--------+------+--------+------+--------------+
| id   | name       | sex    | age  | dep_id | id   | name         |
+------+------------+--------+------+--------+------+--------------+
|    1 | egon       | male   |   18 |    200 |  200 | 技术         |
|    5 | liwenzhou  | male   |   18 |    200 |  200 | 技术         |
|    2 | alex       | female |   48 |    201 |  201 | 人力资源     |
|    3 | wupeiqi    | male   |   38 |    201 |  201 | 人力资源     |
|    4 | yuanhao    | female |   28 |    202 |  202 | 销售         |
|    6 | jingliyang | female |   18 |    204 | NULL | NULL         |
| NULL | NULL       | NULL   | NULL |   NULL |  203 | 运营         |
+------+------------+--------+------+--------+------+--------------+

#注意 union与union all的区别：union会去掉相同的纪录
```

### 2.子查询

- 子查询是将一个查询语句嵌套在另一个查询语句中。
- 内层查询语句的查询结果，可以为外层查询语句提供查询条件。
- 子查询中可以包含：IN、NOT IN、ANY、ALL、EXISTS 和 NOT EXISTS等关键字。
- 还可以包含比较运算符：= 、 !=、> 、<等。

**带IN关键字的子查询**：

```mysql
#查询平均年龄在25岁以上的部门名
select id,name from department
    where id in 
        (select dep_id from employee group by dep_id having avg(age) > 25);

#查看技术部员工姓名
select name from employee
    where dep_id in 
        (select id from department where name='技术');

#查看不足1人的部门名
select name from department
    where id in 
        (select dep_id from employee group by dep_id having count(id) <=1);
```

**带比较运算符的子查询**：比较运算符：=、!=、>、>=、<、<=、<>

```mysql
#查询大于所有人平均年龄的员工名与年龄
mysql> select name,age from emp where age > (select avg(age) from emp);

#查询大于部门内平均年龄的员工名、年龄
select t1.name,t1.age from emp t1
inner join 
(select dep_id,avg(age) avg_age from emp group by dep_id) t2
on t1.dep_id = t2.dep_id
where t1.age > t2.avg_age;
```

**带EXISTS关键字的子查询**：

EXISTS关字键字表示存在。在使用EXISTS关键字时，内层查询语句不返回查询的记录。

而是返回一个真假值。True或False

当返回True时，外层查询语句将进行查询；当返回值为False时，外层查询语句不进行查询

```mysql
# department表中存在dept_id=200，Ture
mysql> select * from employee
    ->     where exists
    ->         (select id from department where id=200);
+----+------------+--------+------+--------+
| id | name       | sex    | age  | dep_id |
+----+------------+--------+------+--------+
|  1 | egon       | male   |   18 |    200 |
|  2 | alex       | female |   48 |    201 |
|  3 | wupeiqi    | male   |   38 |    201 |
|  4 | yuanhao    | female |   28 |    202 |
|  5 | liwenzhou  | male   |   18 |    200 |
|  6 | jingliyang | female |   18 |    204 |
+----+------------+--------+------+--------+

# department表中不存在dept_id=205，False
mysql> select * from employee
    ->     where exists
    ->         (select id from department where id=205);
Empty set (0.00 sec)
```

### 3.权限管理

```mysql
# 授权表
user  # 该表放行的权限，针对：所有数据，所有库下所有表，以及表下的所有字段
db  # 该表放行的权限，针对：某一数据库，该数据库下的所有表，以及表下的所有字段
tables_priv  # 该表放行的权限。针对：某一张表，以及该表下的所有字段
columns_priv  # 该表放行的权限，针对：某一个字段

创建账号
# 本地账号
create user 'egon1'@'localhost' identified by '123'; # mysql -uegon1 -p123
# 远程帐号
create user 'egon2'@'192.168.31.10' identified by '123'; # mysql -uegon2 -p123 -h 服务端ip
create user 'egon3'@'192.168.31.%' identified by '123'; # mysql -uegon3 -p123 -h 服务端ip
create user 'egon3'@'%' identified by '123'; # mysql -uegon3 -p123 -h 服务端ip
```

示例：

```mysql
常用权限有：select,update,alter,delete
all可以代表除了grant之外的所有权限

# 针对所有库的授权:*.*
grant all on *.* to 'egon1'@'localhost';  # 在user表中可以查到egon1用户的所有权限
grant select on *.* to 'egon1'@'localhost';  # 只在user表中可以查到egon1用户的select权限
revoke select on *.* from 'egon1'@'localhost';  # 删除egon1表中的select权限

# 针对某一数据库：db1.*
grant select on db1.* to 'egon1'@'localhost';  # 只在db1表中可以查到egon1用户的select权限
revoke select on db1.* from 'egon1'@'localhost';  # 删除db1表中egon1用户的select权限

# 针对某一个表：db1.t2
grant select on db1.t2 to 'egon1'@'localhost';  # 只在tables_priv表中可以查到egon1用户的select权限
revoke select on db1.t2 from 'egon1'@'localhost';# 删除tables_priv表中的egon1用户的权限

# 针对某一个字段
grant select(id,name),update(age) on db1.t2 to 'egon1'@'localhost';  # 只在columns_priv表中可以查到egon1用户的id，name字段的查看权限，age的修改权限
```

