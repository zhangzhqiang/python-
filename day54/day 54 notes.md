# Day 54 notes

## 1. 模板语法之变量

在Django模板中遍历复杂数据结构的关键是句点字符,语法:

```python
{{var_name}}
```

views.py

```python
from django.shortcuts import render
import datetime

# Create your views here.


def index(request):
    """
    模板语法:
        变量:{{}}
    :param request:
    :return:
    """
    name = 'ike'
    i = 10
    l = [11, 22, 33, 44]  # 列表
    info = {"name": "ike", "age": "23"}  # 字典
    b = True

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    alex = Person("alex", 333)  # 自定义类对象
    pq = Person("peiqi", 222)
    person_list = [pq, alex]
    date = datetime.date(2019, 6, 29)
    person_lis = []
return render(request, "index.html", locals())
```

template-index.html

```html
<p>字符串:{{ name }}</p>
<p>整型:{{ i }}</p>
<p>列表:{{ l }}</p>
<p>字典:{{ info }}</p>
<p>布尔:{{ b }}</p>
<p>类对象{{ alex }}</p>
<p>列表{{ person_list }}</p>
<p>日期:{{ date }}</p>

<hr>
<h3>深度查询</h3>
<p>{{ name }}</p>
<p>{{ i }}</p>
<p>{{ alex.name }}</p>
<p>{{ info.name }}</p>
<p>{{ person_list.1.name }}</p>
<p>{{ date.year }}</p>
```

注意:句点可以用来引用对象的方法,语法:

```python
<h2>dic.name.upper</h2>
```

## 2. 模板之过滤器{{}}

### 2.1 date:日期

语法:

```
{{obj|filter__name:param}}
```

例子:

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
    now = datetime.datetime.now()
    return render(request, "index.html", locals())
```

template-index.html

```python
<p>{{ now|date:'Y-m-d' }}</p>
```

### 2.2 default:输出

语法:

```
{{ value|default:"nothing" }}
```

如果一个变量True使用变量的值,否则使用给定的值,例如：

views.py

```python
from django.shortcuts import render
import datetime
def index(request):
    person_lis = []
    return render(request, "index.html", locals())
```

template-index.html

```python
<p>{{ person_lis|default:'是一个空列表' }}</p>
```

### 2.3 length:长度

语法:

```
{{ value|length }}
```

返回数据类型的长度,例如:

views.py

```
from django.shortcuts import render
import datetime
def index(request):
    len = {1, 2, 3, 6}
    return render(request, "index.html", locals())
```

template-index.html

```
<p>长度:{{ len|length }}</p>
```

### 2.4 slice:切片

语法:

```
{{ value|slice:"2:-1" }}
```

views.py

```
from django.shortcuts import render
import datetime
def index(request):
    len = {1, 2, 3, 6}
    return render(request, "index.html", locals())	
```

template-index.html

```
<p>{{ strting|slice:'::2' }}</p>
```

### 2.5 truncatechars:截断

语法:

```
{{ value|truncatechars:9 }}
```

如果字符串很长想要截断,就可以用truncatechars实现,截断的字符串将以可翻译的省略号序列（“...”）结尾.

views.py

```
from django.shortcuts import render
import datetime
def index(request):
    truncate_str = 'hello python world use it'
    return render(request, "index.html", locals())	
```

template-index.html

```
{#截断字符#}
<p>{{ truncate_str|truncatechars:6 }}</p>
{#阶段单词#}
<p>{{ truncate_str|truncatewords:2 }}</p>
```

### 2.6 filesizeformat:文件大小

语法:

```
{{value|filesizeformat}}
```

获取文件大小,例如:
views.py

```
from django.shortcuts import render
import datetime
def index(request):
    file_size = 123456
    return render(request, "index.html", locals())	
```

template-index.html

```
<p>{{ file_size|filesizeformat }}</p>
```

### 2.7 safe:关闭转义

语法:

```
{{ value|safe}}
```

Django中关闭HTML的自动转义,例如:

views.py

```
from django.shortcuts import render
import datetime
def index(request):
    link = "<a href>click</a>"
    return render(request, "index.html", locals())	
```

template-index.html

```
<p>{{ link|safe }}</p>
```

## 3. 模板之标签{% %}

### 3.1 for标签

遍历每一个元素,例如:

views.py

```
from django.shortcuts import render
import datetime
def index(request):
    l = [11, 22, 33, 44]  # 列表
    info = {"name": "ike", "age": "23"}  # 字典
    return render(request, "index.html", locals())	
```

template-index.html

```
<h3>for循环标签--列表</h3>
{% for i in l %}
    <p>{{ i }}</p>
{% endfor %}

<h3>for循环标签--字典</h3>
{% for k,v in info.items %}
    <p>{{ k }}:{{ v }}</p>
{% endfor %}
```

可以利用`{% for obj in list reversed %}`反向完成循环.

注：循环序号可以通过｛｛forloop｝｝显示

```
forloop.counter            The current iteration of the loop (1-indexed)
forloop.counter0           The current iteration of the loop (0-indexed)
forloop.revcounter         The number of iterations from the end of the loop (1-indexed)
forloop.revcounter0        The number of iterations from the end of the loop (0-indexed)
forloop.first              True if this is the first time through the loop
forloop.last               True if this is the last time through the loop
```

例子:

views.py

```
from django.shortcuts import render
import datetime
def index(request):
    l = [11, 22, 33, 44]  # 列表
    info = {"name": "ike", "age": "23"}  # 字典
    return render(request, "index.html", locals())	
```

template-index.html

```
<h3>for循环标签--列表</h3>
{% for i in l %}
    <p>{{ forloop.counter }} {{ i }}</p>
{% endfor %}

<h3>for循环标签--字典</h3>
{% for k,v in info.items %}
    <p>{{ forloop.counter0 }}{{ k }}:{{ v }}</p>
{% endfor %}
```

for ... empty:

for 标签带有一个可选的`{% empty %}` 从句，以便在给出的组是空的或者没有被找到时，可以有所操作.

```
{% for person in null_list %}
    <p>{{ forloop.counter0 }} {{ person.name }},{{ person.age }}</p>
    {% empty %}
    <p>列表为空</p>
{% endfor %}
```

### 3.2 if 标签

`{% if %}`会对一个变量求值，如果它的值是“True”（存在、不为空、且不是boolean类型的false值），对应的内容块会输出.

views.py

```
from django.shortcuts import render
import datetime
def index(request):
	num = 60
    return render(request, "index.html", locals())	
```

template-index.html

```
{% if num > 100 or num < 0 %}
    <p>无效</p>
{% elif num > 80 and num < 100 %}
    <p>优秀</p>
{% else %}
    <p>凑活吧</p>
{% endif %}
```

### 3.3 with标签

给复杂的变量起个别名

views.py

```
from django.shortcuts import render
import datetime
def index(request):
	num = 60
    return render(request, "index.html", locals())	
```

template-index.html

```
{% with info.name as num %}
    {{ num }}

{% endwith %}
```

### 3.4 csrf_token标签

Django中间件拦截,无法访问POST请求,用这个标签通过拦截

这个标签用于跨站请求伪造保护

views.py

```
def login(request):
    if request.method == 'POST':
        return HttpResponse('OK')
    return render(request, 'login.html')
```

template-login.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<form action="" method="post">
    {% csrf_token %}
    用户名:<input type="text" name="user">
    密码: <input type="text" name="pwd">
    <input type="submit">
</form>
</body>
</html>
```

### 3.5 自定义标签和过滤器

- 在settings中的INSTALLED_APPS配置当前app,不然Django无法找到自定义的simple_tag.
- 在app中创建templatetags模块(注:模块名只能是templatetags)
- 创建一个.py文件,比如:my_tag.py

settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01'
]
```

my_tag_filter.py

```
# 自定义一个标签

from django import template

# 必须是这个变量
register = template.Library()


# 自定义过滤器:
@register.filter
def multi_filter(x, y):
    return x * y


# 自定义标签
@register.simple_tag()
def multi_tag(x, y, z):
    return x * y * z
```

template-login.html

```html
<hr>
<h3>自定义过滤器调用</h3>
{#导包my_tag_filte.py#}
{% load my_tag_filter %}

{#过滤器只能实现两个参数#}
<p>{{ i|multi_filter:20 }}</p>

<hr>
<h3>自定义标签调用</h3>
{#自定义标签可以是多个参数#}
{% multi_tag 7 9 8%}

<hr>
<h3>自定义过滤器可以用于if流程判断,自定义标签不可以</h3>
{% if i|multi_filter:20 > 100 %}
    <p>100</p>
{% else %}
    <p>{{ i }}</p>

{% endif %}
```

注意:自定义过滤器可以用于if流程判断,自定义标签不可以

### 3.6 模板继承

Django模版引擎中最强大也是最复杂的部分就是模版继承了.模版继承可以让您创建一个基本的“骨架”模版,它包含您站点中的全部元素,并且可以定义能够被子模版覆盖的 blocks.

advertise.html---带标题的面板

```html
<div class="action">
    <div class="panel panel-danger">
        <div class="panel-heading">Panel heading without title</div>
        <div class="panel-body">
            Panel content
        </div>
    </div>
    <div class="panel panel-warning">
        <div class="panel-heading">Panel heading without title</div>
        <div class="panel-body">
            Panel content
        </div>
    </div>
    <div class="panel panel-success">
        <div class="panel-heading">Panel heading without title</div>
        <div class="panel-body">
            Panel content
        </div>
    </div>
</div>
```

base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {#在base中加的block越多越好#}
    {% block title %}

    {% endblock %}
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .header {
            width: 100%;
            height: 50px;
            background: #369;
        }
    </style>
</head>
<body>

<div class="header"></div>
<div class="container">
    <div class="row">
        <div class="col-md-3">
            {#导入advertise.html#}
            {% include 'advertise.html' %}
        </div>
        <div class="col-md-9">
            {% block con %}
                <h1>content</h1>
            {% endblock %}
        </div>
    </div>
</div>


</body>
</html>
```

这个模板,我们叫做base.html,它定义类一个简单的html骨架,这也是父模板,子模板可以通过block继承父模板的内容.

index.html

```
{#extends必须是第一个标签#}
{% extends 'base.html' %}

{% block title %}
    <title>orders标签</title>
{% endblock %}

{% block con %}
    {#加载父类block内容#}
    {{ block.super }}
    <h1>订单</h1>
{% endblock con %}
```

extends 标签是这里的关键,它告诉模版引擎，这个模版“继承”了另一个模版,当模版系统处理这个模版时，

- 首先，它将定位父模版——在此例中，就是“base.html”
- 版引擎将注意到 base.html 中的两个 block 标签,并用子模版中的内容来替换这些block

使用继承的提示:

- 如果你在模版中使用 `{% extends %}` 标签，它必须是模版中的第一个标签.其他的任何情况下，模版继承都将无法工作.
- 在base模版中设置越多的 `{% block %}` 标签越好.如果子模板不填充block内容,就会继承父模板中block内容,所以在继承父模板中的block内容我们可以看情况填充.
- 如果在模板中存在很多重复性的内容,那就意味着我们可以把这些内容写到父模板中的`{% block %}` ,然后去调用.

- 继承父模板block的内容,我们在写的时候不想把父模板内容覆盖掉,我们可以在子模板写入`{{ block.super }}`,继保留了父模板的内容,也写入了子模板的内容.

- 为了更好的可读性,你也可以给你的`{% endblock %}` 标签一个 名字 .例如：

    ```
    {% block content %}
    ...
    {% endblock content %}
    ```

- 不能在一个模板中定义多个相同的block标签.