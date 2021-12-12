# Day53 notes

## 1. 静态文件配置

- settings.py写入下列代码

    ```python
    STATIC_URL = '/static/'  # 别名
    
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]
    ```

    html模板
    
    ```python
<link rel="stylesheet" href="/static/css/login.css">  # 以别名开头
    ```

    按照STATICFILES_DIRS列表的进行查找
    
    - html文件引入时导入的link标签路径/static/文件名称
    - 在项目根目录创建static文件夹，包含常见的css,js,img,plugins等插件

## 2. 路由配置---位置参数

```python
from django.contrib import admin
from django.urls import path, re_path
from frist_demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^articles/2003/$', views.special_case_2003),  # 以什么开头以什么结尾
    re_path(r'^articles/([0-9]{4})/$', views.year_archive),  # 结尾0-9传入四位数(/2019),传入两个参数,多对一
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),  # 结尾0-9传入四位数和2位数(/2019/06),传入3个参数,多对一
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail)  # 传入4个参数参数
]
```

```
/articles/2003/  # 匹配第一个模式
/articles/2019/  # 匹配第二个模式
/articles/2019/06/  # 匹配第三个模式
/articles/2019/06/26/  # 匹配第四个模式
/articles/2019/6/  # 不匹配任何模式
```

注意:

- 参数要与列表中的写的参数匹配--比如(/articles/2019/3/)不匹配列表中的任何模式
- 每个正则表达式前面的'r' 是可选的但是建议加上,它告诉Python 这个字符串是“原始的”,都不应该转义

## 3. 路由配置---有名分组(关键字参数)

```python
from django.contrib import admin
from django.urls import path, re_path
from frist_demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive), 
]
```

```python
/articles/2019/06/ 请求将调用views.month_archive(request, year='20195', month='06')函数，而不是views.month_archive(request, '2019', '06').
```

这个实现与前面的示例完全相同，只有一个细微的差别：捕获的值作为关键字参数而不是位置参数传递给视图函数.

## 4. 路由配置---分发

frist_demo.urls.py

```python
from django.urls import path, re_path, include
from frist_demo import views

urlpatterns = [
    re_path(r'^articles/2003/$', views.special_case_2003),
    re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive), 
    re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive), 
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail) 
]
```

untitled.urls.py

```python
from django.contrib import admin
from django.urls import path, re_path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"frist_demo/", include("frist_demo.urls")) # 第一种
]
```

- 把untitled.urls.py文件里的内容复制到frist_demo.urls.py文件里

- 在untitled.urls.py里导入include函数,匹配到frist_demo/路径,找到urls文件

- 这样就可以通过http://127.0.0.1:8080/frist_demo/articles/...匹配frist_demo.urls.py文件中urlpatterns列表中的模式了

    但是url地址中每次都需要输入frist_demo,我们可以通过正则匹配,用第二种方法就可以实现

    - http://127.0.0.1:8080/frist_demo/articles/2003/08/

## 4.路由配置---反向解析

### 1. 在模板中反向解析

login.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

{#模板语法之一反向解析{%  %}#}
<form action="{% url 'Log' %}" method="post">
    用户名 <input type="text" name="user">
    密码 <input type="pswd" name="pwd">
    <input type="submit">
</form>

</body>
</html>
```

urls.py

```python
from django.urls import path, re_path, include
from frist_demo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='Log')
]
```

views.py

```python
from django.shortcuts import render, HttpResponse
def login(request):

    print(request.method)
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print(request.POST)

        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == 'ike' and pwd == '123':
            return HttpResponse('success!')
        else:
            return HttpResponse('username or password error!')
```

- html 文件中以{%  %}语法匹配路径,html中路径不需要修改,永远都是获取最新的.
- urls文件中login路径可以随便修改,在html文件中永远获取到最新路径这就是反向解析.

### 2.在脚本中反向解析

untitled.urls.py

```python
from django.urls import path, re_path, include
urlpatterns = [
	re_path(r"^", include("frist_demo.urls"))
]
```

frist_demo.urls.py

```python
from django.urls import path, re_path, include
from frist_demo import views

urlpatterns = [
    re_path(r'^articles/2003/$', views.special_case_2003, name='sc_2003'),  # 起个别名 name = 'sc_2003'
    re_path(r'^articles/([0-9]{4})/$', views.year_archive, name='y_a'),  # 起个别名
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive, name='y_m_d'),  # 起个别名
    re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail)
]
```

views.py

```python
def special_case_2003(request):

    url = reverse('sc_2003')  # 反向解析
    url = reverse("y_a")  # 反向解析
    url = reverse(("y_m_d"))  # 反向解析
    print(url)
    return HttpResponse('special_case_2003')
```

在frist_demo.urls.py中给列表中的模块起个别名,就可以实现在脚本中反向解析

注意:

- views文件中反向解析后,不走return代码,直接反给自己的函数,也就是列表中模块的函数.

## 5. 路由控制---名称空间

命名空间（英语：Namespace）是表示标识符的可见范围,我们在开发项目时，会经常使用name属性反解出URL，当不小心在不同的app的urls中定义相同的name时，可能会导致URL反解错误，为了避免这种事情发生，引入了命名空间。
pro的urls.py

```python
from django.urls import path, re_path, include
urlpatterns = [
	re_path(r"^app01/", include(("frist_demo.urls", 'app01'))),  # 取一个名称空间的别名app01
    re_path(r"^app02/", include(("app02.urls", 'app02'))),  # 取一个名称空间的别名app02

]
```

frist_demo.urls

```python
from django.urls import path, re_path, include
from frist_demo import views
urlpatterns = [
    re_path("index/", views.index, name='index') # frist_demo中的视图函数
]
```

app02.urls

```python
rom django.urls import path, re_path, include
from app02 import views
urlpatterns = [
        re_path("index/", views.index, name='index')  # app02中的视图函数
]
```

frist_demo.views

```python
from django.shortcuts import render, HttpResponse
def index(request):
	return HttpResponse(reverse("app01:index"))  # 反转找到pro中的名称空间别名
```

app02.views

```python
from django.shortcuts import reverse, HttpResponse
def index(request):
    return HttpResponse(reverse("app02:index"))  # 反转找到pro中的名称空间别名
```

## 6. Django2.0版的path

### 1. Django自带转换器

```python
urlpatterns = [
re_path('articles/(?P<year>[0-9]{4})/', year_archive),
re_path('article/(?P<article_id>[a-zA-Z0-9]+)/detail/', detail_view),
re_path('articles/(?P<article_id>[a-zA-Z0-9]+)/edit/', edit_view),
re_path('articles/(?P<article_id>[a-zA-Z0-9]+)/delete/', delete_view),
]
```

问题:

- 函数 year_archive 中year参数是字符串类型的,因此需要先转化为整数类型的变量值,在视图函数逻辑中year=int(year)就可以转换.有没有一种方法，在url中Django自动完成.
- 三个路由中article_id都是同样的正则表达式，但是你需要写三遍，当之后article_id规则改变后，需要同时修改三处代码，那么有没有一种方法，只需修改一处即可.

示例:

```
from django.urls import path  
from . import views  
urlpatterns = [  
    path('articles/2003/', views.special_case_2003),  
    path('articles/<int:year>/', views.year_archive),  
    path('articles/<int:year>/<int:month>/', views.month_archive),  
    path('articles/<int:year>/<int:month>/<slug>/', views.article_detail),  
]
```

基本规则:

- 使用尖括号(<>)从url中捕获值
- 捕获值中可以包含一个转化器类型（converter type），比如使用捕获一个整数变量。如果没有转化器，将匹配任何字符串，当然也包括了 / 字符
- 无需添加前导斜杠。比如:  articles/   前边不需要添加斜杠

Django默认支持以下5个转化器:

- str,匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式
- int,匹配正整数，包含0
- slug,匹配字母、数字以及横杠、下划线组成的字符串
- uuid,匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00，这个基本上很少用
- path,匹配任何非空字符串，包含了路径分隔符

### 2. 注册自定义转换器

对于一些复杂或者复用的需要，可以定义自己的转化器。转化器是一个类或接口，它的要求有三点：

- regex 类属性，字符串类型

- to_python(self, value) 方法，value是由类属性 regex 所匹配到的字符串，返回具体的Python变量值，以供Django传递到对应的视图函数中。

- to_url(self, value) 方法，和 to_python 相反，value是一个具体的Python变量值，返回其字符串，通常用于url反向引用。

url_convert.py

```python
class MonConvert:
    regex = "[0-9]{2}"

    def to_python(self, value):
        return int(value)  # 转换为int类型

    def to_url(self, value):  # 反向解析
        return '%04d' % value
```

使用register_converter 将其注册到URL配置中

```python
from frist_demo.url_convert import MonConvert
# 注册自定义url转换器
register_converter(MonConvert, "mm")
urlpatterns = [
	path("articles/<mm:month>", views.path_month)
]
```

path_month.py

```python
def path_month(request, month):
    print(month, type(month))

    return HttpResponse("path month...")
```

