# Day56 notes

## 1. ORM简介

对象关系映射（Object Relational Mapping，简称ORM）模式是一种为了解决面向对象与关系数据库存在的互不匹配的现象的技术.

- ORM是通过使用描述对象和数据库之间映射的元数据，将程序中的对象自动持久化到关系数据库中
- 一种简单的方案是采用硬编码方式，为每一种可能的数据库访问操作提供单独的方法,ORM提供了对数据库的映射,不用直接编写SQL代码,只需操作对象就能对数据库操作数据

ORM的方法论基于三个核心原则： 

- 简单：以最基本的形式建模数据。
- 传达性：数据库结构被任何人都能理解的语言文档化
- 精确性：基于数据模型创建正确标准化了的结构。 

![img](https://hcdn1.luffycity.com/data/python-book/10102/08.png)

```python
#sql中的表                                                      

#创建表:
CREATE TABLE employee(                                     
	d INT PRIMARY KEY auto_increment ,                    
	name VARCHAR (20),                                     
	gender BIT default 1,                                  
	birthday DATA ,                                         
	department VARCHAR (20),                               
	salary DECIMAL (8,2) unsigned,                         
	);
#sql中的表纪录                                                  
#添加一条表纪录:                                                         
INSERT employee (name,gender,birthday,salary,department)         
VALUES   ("alex",1,"1985-12-12",8000,"保洁部");               
#查询一条表纪录:                                                           
SELECT * FROM employee WHERE age=24;                               
#更新一条表纪录:                                                           
UPDATE employee SET birthday="1989-10-24" WHERE id=1;              
#删除一条表纪录:                                                          
DELETE FROM employee WHERE name="alex"                             
# python的类
class Employee(models.Model):
     id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=32)
     gender=models.BooleanField()
     birthday=models.DateField()
     department=models.CharField(max_length=32)
     salary=models.DecimalField(max_digits=8,decimal_places=2)
# python的类对象
#添加一条表纪录:
emp=Employee(name="alex",gender=True,birthday="1985-12-12",epartment="保洁部")
emp.save()
#查询一条表纪录:
Employee.objects.filter(age=24)
#更新一条表纪录:
Employee.objects.filter(id=1).update(birthday="1989-10-24")
#删除一条表纪录:
Employee.objects.filter(name="alex").delete()
```

## 2. Django使用mysql数据库

1. 创建模型

![1561902414017](C:\Users\ike\AppData\Roaming\Typora\typora-user-images\1561902414017.png)

在工程下新建app01项目,在项目下的models.py中创建模型:

```python
from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 自增,主键
    title = models.CharField(max_length=32, unique=True)  # varchar类型,唯一约束
    pub_date = models.DateField()  # 存日期
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 浮点型,最大八位保留两位小数
    publish = models.CharField(max_length=32)  # varchar类型

    def __str__(self):
        return self.title
```

2. 字段

    ```python
    <1> CharField
    	字符串字段, 用于较短的字符串.
        CharField 要求必须有一个参数 maxlength, 用于从数据库层和Django校验层限制该字段所允许的最大字符数.
    <2> IntegerField
    	#用于保存一个整数.
    <3> FloatField
    	一个浮点数. 必须 提供两个参数:
            参数    描述
            max_digits    总位数(不包括小数点和符号)
            decimal_places    小数位数
            举例来说, 要保存最大值为 999 (小数点后保存2位),你要这样定义字段:
                models.FloatField(..., max_digits=5, decimal_places=2)
                要保存最大值一百万(小数点后保存10位)的话,你要这样定义:
                    models.FloatField(..., max_digits=19, decimal_places=10)
                    admin 用一个文本框(<input type="text">)表示该字段保存的数据.
    <4> AutoField
    	一个 IntegerField, 添加记录时它会自动增长. 你通常不需要直接使用这个字段;
    	自定义一个主键：my_id=models.AutoField(primary_key=True)
    	如果你不指定主键的话,系统会自动添加一个主键字段到你的 model.
    <5> BooleanField
    	A true/false field. admin 用 checkbox 来表示此类字段.
    <6> TextField
    	一个容量很大的文本字段.
        admin 用一个 <textarea> (文本区域)表示该字段数据.(一个多行编辑框).
    <7> EmailField
    	一个带有检查Email合法性的 CharField,不接受 maxlength 参数.
    <8> DateField
    	一个日期字段. 共有下列额外的可选参数:
            Argument    描述
            auto_now    当对象被保存时,自动将该字段的值设置为当前时间.通常用于表示 "last-modified" 时间戳.
            auto_now_add    当对象首次被创建时,自动将该字段的值设置为当前时间.通常用于表示对象创建时间.
            （仅仅在admin中有意义...)
    <9> DateTimeField
    	一个日期时间字段. 类似 DateField 支持同样的附加选项.
    <10> ImageField
    	类似 FileField, 不过要校验上传对象是否是一个合法图片.#它有两个可选参数:height_field和width_field,
        如果提供这两个参数,则图片将按提供的高度和宽度规格保存.    
    <11> FileField
        一个文件上传字段.
        要求一个必须有的参数: upload_to, 一个用于保存上载文件的本地文件系统路径. 这个路径必须包含 strftime #formatting,
        该格式将被上载文件的 date/time
        替换(so that uploaded files don't fill up the given directory).
        admin 用一个<input type="file">部件表示该字段保存的数据(一个文件上传部件) .
        注意：在一个 model 中使用 FileField 或 ImageField 需要以下步骤:
           （1）在你的 settings 文件中, 定义一个完整路径给 MEDIA_ROOT 以便让 Django在此处保存上传文件.
           (出于性能考虑,这些文件并不保存到数据库.) 定义MEDIA_URL 作为该目录的公共 URL. 要确保该目录对
           WEB服务器用户帐号是可写的.
           （2） 在你的 model 中添加 FileField 或 ImageField, 并确保定义了 upload_to 选项,以告诉 Django
           使用 MEDIA_ROOT 的哪个子目录保存上传文件.你的数据库中要保存的只是文件的路径(相对于 MEDIA_ROOT).
           出于习惯你一定很想使用 Django 提供的 get_<#fieldname>_url 函数.举例来说,如果你的 ImageField
           叫作 mug_shot, 你就可以在模板中以 {{ object.#get_mug_shot_url }} 这样的方式得到图像的绝对路径.
    <12> URLField
         用于保存 URL. 若 verify_exists 参数为 True (默认), 给定的 URL 会预先检查是否存在( 即URL是否被有效装入且没有返回404响应).
         admin 用一个 <input type="text"> 文本框表示该字段保存的数据(一个单行编辑框)
    <13> NullBooleanField
          类似 BooleanField, 不过允许 NULL 作为其中一个选项. 推荐使用这个字段而不要BooleanField 加 null=True 选项
          admin 用一个选择框 <select> (三个可选择的值: "Unknown", "Yes" 和 "No" ) 来表示这种字段数据.
    <14> SlugField
    	"Slug" 是一个报纸术语. slug 是某个东西的小小标记(短签), 只包含字母,数字,下划线和连字符.
    	#它们通常用于URLs若你使用 Django 开发版本,你可以指定 maxlength. 若 maxlength 未指定, Django 会使用默认长度: 50.  
    	#在以前的 Django 版本,没有任何办法改变50 这个长度.这暗示了 db_index=True.它接受一个额外的参数: prepopulate_from, which is a list of fields from which to auto-#populate the slug, via JavaScript,in the object's admin form: models.SlugField(prepopulate_from=("pre_name", "name"))prepopulate_from 不接受 DateTimeFields.
    <13> XMLField
    	一个校验值是否为合法XML的 TextField,必须提供参数: schema_path, 它是一个用来校验文本的 RelaxNG schema #的文件系统路径.
    <14> FilePathField
           可选项目为某个特定目录下的文件名. 支持三个特殊的参数, 其中第一个是必须提供的.
           参数    描述
           path    必需参数. 一个目录的绝对文件系统路径. FilePathField 据此得到可选项目.
           Example: "/home/images".
           match    可选参数. 一个正则表达式, 作为一个字符串, FilePathField 将使用它过滤文件名.
           注意这个正则表达式只会应用到 base filename 而不是
           路径全名. Example: "foo.*\.txt^", 将匹配文件 foo23.txt 却不匹配 bar.txt 或 foo23.gif.
           recursive可选参数.要么 True 要么 False. 默认值是 False. 是否包括 path 下面的全部子目录.
           这三个参数可以同时使用.
           match 仅应用于 base filename, 而不是路径全名. 那么,这个例子:
           FilePathField(path="/home/images", match="foo.*", recursive=True)
           ...会匹配 /home/images/foo.gif 而不匹配 /home/images/foo/bar.gif
    <15> IPAddressField
           一个字符串形式的 IP 地址, (i.e. "24.124.1.30").
    <16> CommaSeparatedIntegerField
           用于存放逗号分隔的整数值. 类似 CharField, 必须要有maxlength参数.
    ```

3. 参数

    ```python
    (1)null
    如果为True，Django 将用NULL 来在数据库中存储空值。 默认值是 False.
    (2)blank
    如果为True，该字段允许不填。默认为False。
    要注意，这与 null 不同。null纯粹是数据库范畴的，而 blank 是数据验证范畴的。
    如果一个字段的blank=True，表单的验证将允许该字段是空值。如果字段的blank=False，该字段就是必填的。
    (3)default
    字段的默认值。可以是一个值或者可调用对象。如果可调用 ，每有新对象被创建它都会被调用。
    (4)primary_key
    如果为True，那么这个字段就是模型的主键。如果你没有指定任何一个字段的primary_key=True，
    Django 就会自动添加一个IntegerField字段做为主键，所以除非你想覆盖默认的主键行为，
    否则没必要设置任何一个字段的primary_key=True。
    (5)unique
    如果该值设置为 True, 这个数据字段的值在整张表中必须是唯一的
    (6)choices
    由二元组组成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项。 如果设置了choices ，默认的表单将是一个选择框而不是标准的文本框，<br>而且这个选择框的选项就是choices 中的选项。
    ```

4. settings配置

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':'bms',     　　 　  # 要连接的数据库，连接前需要创建好
            'USER':'root',　　　　　　  # 连接数据库的用户名
            'PASSWORD':'',　　　　　　  # 连接数据库的密码
            'HOST':'127.0.0.1',       # 连接主机，默认本级
            'PORT'：3306    　　　     #  端口 默认3306
        }
    }
    ```

    注意1：

    NAME即数据库的名字，在mysql连接前该数据库必须已经创建，而上面的sqlite数据库下的db.sqlite3则是项目自动创建 USER和PASSWORD分别是数据库的用户名和密码。设置完后，再启动我们的Django项目前，我们需要激活我们的mysql。然后，启动项目，会报错：no module named MySQLdb 。这是因为django默认你导入的驱动是MySQLdb，可是MySQLdb 对于py3有很大问题，所以我们需要的驱动是PyMySQL 所以，我们只需要找到项目名文件下的**init**,在里面写入:

    ```python
    import pymysql
    pymysql.install_as_MySQLdb()
    ```

    最后通过两条数据库迁移命令即可在指定的数据库中创建表:

    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```

    注意2:

    确保配置文件中的INSTALLED_APPS中写入我们创建的app名称

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        "book"
    ]
    ```

    注意3:

    如果报错如下

    ```
    django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.3 or newer is required; you have 0.7.11.None
    ```

    MySQLclient目前只支持到python3.4，因此如果使用的更高版本的python，需要修改如下：

    找到F:\program\python36\Lib\site-packages\django\db\backends\mysql路径注释掉下面代码

    ```
    if version < (1, 3, 3):
         raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)
    ```

    注意4: 

    如果想打印orm转换过程中的sql，需要在settings中进行如下配置:

    ```python
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console':{
                'level':'DEBUG',
                'class':'logging.StreamHandler',
            },
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['console'],
                'propagate': True,
                'level':'DEBUG',
            },
        }
    }
    ```

## 3. 单表操作

新建数据:

```python
# =======================添加表记录=======================

# 方式一:
book_obj = Book(id=1, title='Python红宝书', price=100, pub_date='2019-06-29', publish='人民出版社')
book_obj.save()

# 方式二: create返回值就是当前生成的对象记录,也就是表添加的记录
book_obj = Book.objects.create(title='Linux黄宝书', price=200, pub_date='2019-06-30', publish='人民出版社')
print(book_obj.title, book_obj.price)
```

查询数据:

```python
# =======================查询表记录API====================
'''
1.方法的返回值
2.方法的调用者
:param request:
:return:
'''
# 1.all方法:返回值一个queryset对象
book_list = Book.objects.all()
print(book_list)  # <QuerySet [<Book: Python红宝书>, <Book: Linux蓝宝书>]>
for i in book_list:
    print(i.title, i.price)

    print(book_list[1].title)

# 2.first,last 调用者:queryset对象  返回值:model对象
book = Book.objects.all().first()  # book = Book.objects.all()[0]
book = Book.objects.all().last()  # # book = Book.objects.all()[-1]

# 3.filter  调用者:queryset对象  返回值:queryset对象
book_list = Book.objects.filter(price=100)  # all取到的全部的数据,filter取到的是筛选后的数据
book1 = Book.objects.filter(price=100).first()

# 4.get  有且只有一个查询结果时才有意义,否则会报错  返回值:model对象
book_obj = Book.objects.get(price=136)
print(book_obj)

# 5.exclude  排除满足条件的数据  调用者:queryset对象  返回值:queryset对象
book1 = Book.objects.exclude(price=136)
print(book1)

# 6.order_by排序  调用者:queryset对象  返回值:queryset对象
res = Book.objects.all().order_by('-price')  # order_by('-price')为降序排  默认为升序
print(res)

# 7.rereverse对查询结果反向排序  调用者:queryset对象  返回值:queryset对象
res = Book.objects.all().order_by('-price').reverse()
print(res)

# 8.count统计  调用者:queryset对象 返回值:int
res = Book.objects.all().count()
print(res)

# 9.exist判读是否包含  调用者:queryset对象 返回值:bool
res = Book.objects.all().exists()
print(res)
if res:
    print('OK~~~')

# 10.values  调用者:queryset对象  返回值:queryset对象
res = Book.objects.all().values('price', 'title')
print(res)  # <QuerySet [{'price': Decimal('100.00')}, {'price': Decimal('136.00')}, {'price': Decimal('100.00')}]>

"""
temp = []
for obj in Book object.all()
	temp.append({
    "price": obj.price
    "title": obj.title
    })
    """

# 11.valuse_list  调用者:queryset对象  返回值:queryset对象
res = Book.objects.all().values_list('price')
print(res)  # <QuerySet [(Decimal('100.00'),), (Decimal('136.00'),), (Decimal('100.00'),)]>

"""
values:
   <QuerySet [{'price': Decimal('100.00')}, {'price': Decimal('136.00')}, {'price': Decimal('100.00')}]>
values_list:
   <QuerySet [(Decimal('100.00'),), (Decimal('136.00'),), (Decimal('100.00'),)]>
"""

# 12.distinct去重  调用者:queryset对象  返回值:queryset对象
res = Book.objects.all().values_list('price').distinct()
print(res)
```

模糊查询:

```python
# =======================查询表记录之模糊查询====================
res = Book.objects.filter(price__gt=100, price__lt=200)
print(res)
res = Book.objects.filter(title__endswith='书')  # 以什么结尾,title__startswith同理
print(res)
res = Book.objects.filter(title__contains='n')  # 包含
print(res)
res = Book.objects.filter(title__icontains='l')  # 包含  不区分大小写
print(res)
res = Book.objects.filter(price__in=[100, 136])  # 满足这几个条件
print(res)
res = Book.objects.filter(pub_date__year=2019, pub_date__month=6)  # 日期查询
print(res)
```

删除数据:

```python
# =======================删除记录和修改记录=======================
# 1.delete 删除  调用者:queryset对象 model对象
res = Book.objects.filter(price=136).delete()
print(res)  # (1, {'app01.Book': 1})个数以及表的个数

Book.objects.filter(price=100).first().delete()

```

修改数据:

```python
# 1.update修改  调用者:queryset对象
Book.objects.filter(title='Go黄宝书').update(title='人生苦短!go')
```

## 4. Django中mysql数据库使用步骤总结:

- 创建一个mysql数据库; 

    ```python
    creat database 数据库名;
    ```

- 在setting中配置,Django 链接Mysql数据库,INSTALLED_APPS中写入我们创建的app名称;

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':'bms',     　　 　  # 要连接的数据库，连接前需要创建好
            'USER':'root',　　　　　　  # 连接数据库的用户名
            'PASSWORD':'',　　　　　　  # 连接数据库的密码
            'HOST':'127.0.0.1',       # 连接主机，默认本级
            'PORT'：3306    　　　     #  端口 默认3306
        }
    }
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        "book"
    ]
    ```

- 在项目的__init__文件夹中写入代码;

    ```python
    import pymysql
    pymysql.install_as_MySQLdb()
    ```

- 创建表(在app01下的models.py中写类,建表语句);

    ```python
    from django.db import models
    
    # Create your models here.
    
    
    class Book(models.Model):
        id = models.AutoField(primary_key=True)  # 自增,主键
        title = models.CharField(max_length=32, unique=True)  # varchar类型,唯一约束
        pub_date = models.DateField()  # 存日期
        price = models.DecimalField(max_digits=8, decimal_places=2)  # 浮点型,最大八位保留两位小数
        publish = models.CharField(max_length=32)  # varchar类型
    
        def __str__(self):
            return self.title
    ```

- 执行数据迁移两条命令;

    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```

- urls.py文件中设计url;

    ```python
    from django.contrib import admin
    from django.urls import path, re_path
    from app01 import views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('addbook/', views.addbook),
        path('books/', views.books),
        re_path(r"books/(\d+)/delete", views.delbook),  # delbook(request,1)
        re_path(r"books/(\d+)/change", views.changebook),  # delbook(request,1)
    ]
    ```

- views.py文件中写函数

    ```python
    def changebook(request, id):
        book_obj = Book.objects.filter(id=id).first()
        if request.method == 'POST':
            title = request.POST.get('title')
            price = request.POST.get('price')
            date = request.POST.get('date')
            publish = request.POST.get('publish')
            Book.objects.filter(id=id).update(title=title, price=price, pub_date=date, publish=publish)
            return redirect('/books/')
    
        return render(request, "changebook.html", {"book_obj": book_obj})
    ```

- 写模板

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    
        <link rel="stylesheet" href="/static/bs/css/bootstrap.css">
        <style>
            .container{
                margin-top: 100px;
            }
            .btn{
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
    
    <h3>编辑书籍</h3>
    
    <div class="container">
         <div class="row">
             <div class="col-md-6 col-md-offset-3">
                 <form action="" method="post">
                     {% csrf_token %}
                     <div>
                         <label for="">书籍名称</label>
                         <input type="text" class="form-control" name="title" value="{{ book_obj.title }}">
                     </div>
                     <div>
                         <label for="">价格</label>
                         <input type="text" class="form-control" name="price" value="{{ book_obj.price }}">
                     </div>
                     <div>
                         <label for="">出版日期</label>
                         <input type="date" class="form-control" name="date" value="{{ book_obj.pub_date|date:'Y-m-d' }}">
                     </div>
                     <div>
                         <label for="">出版社</label>
                         <input type="text" class="form-control" name="publish" value="{{ book_obj.publish }}">
                     </div>
    
                     <input type="submit" class="btn btn-success pull-right">
    
    
                 </form>
             </div>
         </div>
    </div>
    
    </body>
    </html>
    ```