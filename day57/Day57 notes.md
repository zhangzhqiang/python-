# Day57 notes

## 今日内容

### 1. 多表创建

### 2. 多表查询

## 详细内容

##### 1.创建表

- 作者表：包含姓名和年龄字段
- 作者详情表：包含生日，手机号，地址字段
- 出版社表：包含出版社名称，城市，邮箱字段
- 书籍表：包含书籍名称，出版日期，价格字段

###### 1.1 ORM建表语句

```python
from django.db import models

# Create your models here.
'''
Book＝＝＝Publish  一对多
Author＝＝＝AuthorDetail 一对一
'''

# 作者表
class Author(models.Model):
    nid = models.AutoField(primary_key=True)  # 如果写了就用写的，没写自动添加
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    # 与AuthorDetail建立一对一的关系
    authorDetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


# 作者详情表
class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField(null=True)
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)


# 出版社表
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


# 书籍表
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    read_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)

    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish = models.ForeignKey(to="Publish", to_field="nid", on_delete=models.CASCADE)
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors = models.ManyToManyField(to='Author')

    '''
    多对多建立关系语句等同于以下语句：
    class Book2Author(models.Model):
        nid = models.AutoField(primary_key=True)
        book = models.ForeignKey(to="Book")
        author = models.ForeignKey(to=Author)
    '''

    def __str__(self):
        return self.title

```

###### 1.2 对应关系

- 一对一：作者表与作者详情表之间是一对一的关系，详情表补充作者的信息。
- 多对一：书籍表和出版社表是一对多的关系，出版社可以出版多本书，但是一本书职能有一个出版社。
- 多对多：书籍表和作者表是多对多的关系，一本书可能有多个作者，一个作者可能出版多本书。

###### 1.3 注意事项：

- 表的命名：app名称_表的名称，是根据表中的原数据自动生成的
- id字段如果没有写会自动添加，写了就用写的id
- 外键字段，Django会在字段名上自动补充"_id"形成新的字段名
- 上例中的建表语句使用PostgreSQL语法格式，Django会根据settings中指定的数据库类型来使用相应的SQL语句
- 定义号建表语句后，告诉Django使用这些表，需要在settings中的INSTALLED_APPS添加models.py，Django会自动添加，例如：'app01.apps.App01Config'
- 外键字段ForeignKey有一个null=True的设置，设置好后，允许外键接受空值NULL，可以给它赋值None
- 表之间建立关系的时候，加上on_delete=models.CASCADE参数，否则会报错，意思是：主外关系键中，级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
- 多对多的关系语句：authors = models.ManyToManyField(to='Author')这条语句会生成第五张表多对多的关系表，这条语句可以写在多对多任意一张表中，生成的表名book会根据这条语句所在的表中进行变动，比如：app01_book_authors
- 一对一的关系语句可以写在对应的人意一张表中
- 一对多的关系语句必须写在多的表中

执行数据库迁移语句会生成五张表：

- python3 manage.py makemigrations
- python3 migrate

##### 2. 添加表纪录

###### 2.1 一对多的关系

```python
# 普通添加表纪录
info = AuthorDetail.objects.create(birthday='2019-01-09', telephone='119', addr='南京')
pub = Publish.objects.create(name="人民出版社", email="123@qq.com", city="北京")
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝绑定一对多的关系添加＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
# 方式一
    # 为book表绑定Publish关系
    book_obj = Book.objects.create(title="雪山飞狐", price=300, publishDate="2019-01-02", publish_id=1)
    print(book_obj.title)

# 方式二
    pub_obj = Publish.objects.filter(nid=1).first()
    book_obj = Book.objects.create(title="水浒传", price=400, publishDate="2019-01-02", publish=pub_obj)
    
    print(book_obj.publish)  # 打印与这本书籍关联的出版社对象，在models对应的表中加__str__可以打印出来
    print(book_obj.publish.name)
    print(book_obj.publish.email)
    print(book_obj.title)
    print(book_obj.price)
    print(book_obj.publishDate)

    # 查询西游记这本书的出版社对应的邮箱
    book_obj = Book.objects.filter(title="西游记")[0]  # 也可以first()取值
    print(book_obj.publish.email)
```

###### 2.2 多对多的关系

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝绑定多对多的关系＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
# 新建一本书
    book_obj = Book.objects.create(title="金瓶梅", price=400, publishDate="2019-07-16", publish_id=1)
    # 新建两个作者
    alex = Author.objects.get(name="alex")
    egon = Author.objects.get(name="egon")
    # 绑定多对多关系的API，三种任选其一
    book_obj.authors.add(alex, egon)
    book_obj.authors.add(1, 2)
    book_obj.authors.add(*[1, 2])
		
    # 解除多对多的关系
    book = Book.objects.filter(nid=8).first()
    # book.authors.remove(2)
    # book.authors.remove(*[1, 2])
    # 全部解除
    # book.authors.clear()
    # 查询主键为8的所有作者的名字＝＝＝关键点
    print(book.authors.all().values("name"))  # queryset:与这本书关联的所有作者对象集合
```

##### 3. 跨表查询

###### 3.1 基于对象的跨表查询(子查询)

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝基于对象的跨表查询(子查询)＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
'''
正向查询按字段，反向查询按表名
'''
		# 一对多正向查询：查询金瓶梅这本书的出版社的名字
    book_obj = Book.objects.filter(title="金瓶梅").first()
    print(book_obj.publish)  # 与这本书关联的出版社对象
    print(book_obj.publish.name)

    # 一对多反向查询：查询人民出版社出版过的书籍
    publish = Publish.objects.filter(name="人民出版社").first()
    ret = publish.book_set.all()  # [obj1, obj2, obj3, obj4...]
    print(ret)

    # 多对多正向查询：查询金瓶梅这本书所有的作者的名字
    book_obj = Book.objects.filter(nid=9).first()
    author_list = book_obj.authors.all()  # queryset对象
    for author in author_list:
        print(author)

    # 多对多反向查询：查询alex出版过的书籍
    alex = Author.objects.filter(name='alex').first()
    book_list = alex.book_set.all()
    for book in book_list:
        print(book)

    # 一对一正向查询：查询alex的手机号
    alex = Author.objects.filter(name="alex").first()
    print(alex.authorDetail.telephone)

    # 一对一反向查询：查询手机号为119的作者的名字和年龄
    tel = AuthorDetail.objects.filter(telephone='119').first()
    print(tel.author.name)
    print(tel.author.age)
```

###### 3.2 基于双下划线的跨表查询

Django 提供了一种直观而高效的方式在查询(lookups)中表示关联关系，它能自动确认 SQL JOIN 联系。要做跨关系查询，就使用两个下划线来链接模型(model)间关联字段的名称，直到最终链接到你想要的 model 为止。

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝基于双下划线的跨表查询(join查询)＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
'''
正向查询按字段，反向查询按表名小写用来告诉ORM引擎用哪张表
'''
		# 方式一：一对多正向查询：查询金瓶梅这本书的出版社名称
    book_obj = Book.objects.filter(title='金瓶梅').values('publish__name')
    print(book_obj)

    # 方式二：一对多反向查询：查询出版过金瓶梅的书籍名称
    ret = Publish.objects.filter(book__title='金瓶梅').values('name')
    print(ret)

    # 方式一：多对多正向查询：查询西游记这本书的所有作者的名字(join)
    # 需求：通过Book表join与其关联的Author表，按字段authors通过ORM引擎join book_authors 和 author表
    ret = Book.objects.filter(title='西游记').values('authors__name')
    print(ret)

    # 方式二：多对多反向查询：查询西游记这本书的所有作者(join)
    # 需求：通过Author表join与其关联的Book表，按表名小写book通过ORM引擎join book_authors 和 book表
    ret = Author.objects.filter(book__title='西游记').values('name')
    print(ret)

    # 方式一：一对一正向查询：查询egon的手机号
    # 需求：通过Author表join与其关联的AuthorDetail表，按字段authorDetail通过ORM引擎join AuthorDetail表
    ret = Author.objects.filter(name='egon').values('authorDetail__telephone')
    print(ret)

    # 方式二：一对一反向查询：查询egon的手机号
    # 需求：通过AuthorDetail表join与其关联的Author表，按表名小写author通过ORM引擎join Author表
    ret = AuthorDetail.objects.filter(author__name='egon').values('telephone')
    print(ret)

    # 方式一：
    # 进阶练习：查询手机号110开头的作者出版过的所有书籍名称以及书籍出版社名称
    # 需求：通过Book表join与其关联的AuthorDetail表，Book与AuthorDetail无关联，所以必须连续跨表
    ret = Book.objects.filter(authors__authorDetail__telephone__startswith='110').values('title', 'publish__name')
    print(ret)

    # 方式二：
    # 进阶练习：查询手机号110开头的作者出版过的所有书籍名称以及书籍出版社名称
    # 需求：通过Book表join与其关联的AuthorDetail表，Book与AuthorDetail无关联，所以必须连续跨表
    ret = Author.objects.filter(authorDetail__telephone__startswith='110').values('book__title', 'book__publish__name')
    print(ret)
```

总结：

```python
"""
＝＝＝＝＝＝＝＝＝＝＝＝＝基于对象的跨表查询(子查询)＝＝＝＝＝＝＝＝＝＝＝＝＝
正向查询：关联属性在A表中 A－－－>B
返向查询：关联属性在A表中 B－－－>A
一对多查询：
    正向查询：按字段
    反向查询：按表名小写_set.all()
    
                        book_obj.publish
    Book(关联属性：publish)<－－－－－－－－－>Publish
                        publish_obj.book_set.all()  # queryset
    
多对多查询：
    正向查询：按字段
    反向查询：按表名小写_set.all()    
                        book_obj.objects.all()                
    Book(关联属性：authors)<－－－－－－－－－>Author
                        author_obj.book_set.all()  # queryset
                        
一对一查询：
    正向查询：按字段
    反向查询：按表名小写
    
                              alex.authordetail                
    Author(关联属性：authorDetail)<－－－－－－－－－>AuthorDetail
                              authordetail.author  # queryset
                        
＝＝＝＝＝＝＝＝＝＝＝＝＝基于双下划线的跨表查询(join查询)＝＝＝＝＝＝＝＝＝＝＝＝＝
    正向查询：按字段
    反向查询：按表名小写

"""
```

###### 3.3 聚合查询

aggregate()是QuerySet 的一个终止子句，意思是说，它返回一个包含一些键值对的字典。键的名称是聚合值的标识符，值是计算出来的聚合值。键的名称是按照字段和聚合函数的名称自动生成出来的。如果你想要为聚合值指定一个名称。

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝聚合查询 aggregate＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
'''
聚合返回是一个字典，不再是queryset
'''
    from django.db.models import Avg, Max, Min, Count

    # 查询所有书籍的平均价格
    ret = Book.objects.all().aggregate(avg_price=Avg('price'),
                                       max_price=Max('price'),
                                       min_price=Min('price'),
                                       Count_price=Count('price'))
    print(ret)
```

###### 3.4 分组查询

annotate()为调用的QuerySet中每一个对象都生成一个独立的统计值（统计方法用聚合函数）。

在models.py中新建Emp表：

```python
class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
```

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝分组查询 annotate＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
'''
返回值是queryset
'''
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝单表分组查询：
    # 示例一：
    # 查询每一个部门的名称以及员工的平均薪水
    # SQL: select dep,Avg(salary) from emp group by dep
    # 单表分组查询的ORM语法：单表模型.objects.values('group by的字段').annotate(聚合函数('统计字段'))
    ret = Emp.objects.values('dep').annotate(avg_salary=Avg('salary'))
    print(ret)

    # 示例二：
    # 查询每一个省份的名称以及员工数
    ret = Emp.objects.values('province').annotate(c=Count('id'))
    print(ret)

    # 补充知识点：
    # 在但表分组下，按着主键进行group by是没有任何意义
    ret = Emp.objects.all()
    print(ret)  # select * from emp
    ret = Emp.objects.values('name')
    print(ret)  # select name from emp
    Emp.objects.values('id').annotate(avg_salary=Avg('salary'))
    Emp.objects.all().annotate(avg_salary=Avg('salary'))
    
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝多表分组查询：
    # 示例1:查询每一个出版社的名称及出版的书籍个数
    # 方式一：
    ret = Publish.objects.values('name').annotate(count_book=Count('book__title'))
    print(ret)
    # 方式二:(推荐)
    ret = Publish.objects.values('nid').annotate(count_book=Count('book__title')).values('name', 'count_book')
    print(ret)

    # 方式三：另一种玩法
    ret = Publish.objects.all().annotate(count_book=Count('book__title')).values('name', 'count_book', 'city')
    print(ret)
    ret = Publish.objects.annotate(count_book=Count('book__title')).values('name', 'count_book', 'city')
    print(ret)

    # 示例2:查询每一个作者的名字以及出版过的书籍的最高价格
    ret = Author.objects.values('pk').annotate(mac_p=Max('book__price')).values('name', 'mac_p')
    print(ret)

    # 示例3:查询每一个书籍的名称以及对应的作者个数
    ret = Book.objects.values('pk').annotate(c=Count('authors__name')).values('title', 'c')
    print(ret)
    
    """
    总结跨表分组的模型：
    每一个的表模型.objects.values("pk").annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")
    每一个的表模型.objects.annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")
    每一个的表模型.objects.all().annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")
    """
```

练习：

```python
# 练习1:统计每一本以雪山开头的书籍的作者个数：
    ret = Book.objects.filter(title__startswith='雪山').values('pk').annotate(c=Count('authors__nid')).values('title', 'c')
    print(ret)

    # 练习2:统计不止一个作者的书籍
    ret = Book.objects.values('pk').annotate(c=Count('authors__nid')).filter(c__gt=1).values('title', 'c')
    print(ret)

    # 练习3:根据一本图书作者数量的多少对查询集 QuerySet进行排序:
    ret = Book.objects.all().annotate(c=Count('authors__name')).order_by('c')
    print(ret)

    # 练习4:查询各个作者出的书的总价格:
    ret = Author.objects.values('pk').annotate(c=Sum('book__price')).values('name', 'c')
    print(ret)
```

###### 3.5 F查询与Q查询

F查询：Django支持F()对象之间以及F()对象和常数之间的加减乘除和取模以及修改的操作。

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝F查询＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
    from django.db.models import F, Q
    # 统计评论数大于阅读数的书籍
    ret = Book.objects.filter(comment_num__gt=F('read_num'))
    print(ret)

    # 每本书籍加10
    Book.objects.all().update(price=F('price')+10)
```

Q查询：filter()等方法中的关键字参数查询都是一起进行“AND”的。如果你需要执行更复杂的查询，你可以使用Q对象。

```python
'''
＝＝＝＝＝＝＝＝＝＝＝＝＝Q查询＝＝＝＝＝＝＝＝＝＝＝＝＝
'''
    # Q对象可以使用&(and) 和|(or) 操作符组合起来使用也可以分开使用，~Q(取反)
    # 查询名字为西游记或价格等于430的书籍
    ret = Book.objects.filter(Q(title='西游记') | Q(price=430))
    print(ret)

    # 查询名字不等于水浒传价格等于430阅读量大于2000的书籍
    ret = Book.objects.filter(~Q(title='水浒传') & Q(price=230), read_num__gt=2000)
    print(ret)
```

