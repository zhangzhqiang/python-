# Day55 notes

## 1. 视图函数

一个视图函数,简称视图,是一个简单的Python函数,它接收web请求并返回web响应.响应有多种方式,可以是HTML文件,一个重定向,一张图片等等.

注意:

- 无论视图本身包含什么逻辑,都要返回相应
- 视图函数代码写咋吃哪里没有要求,只要在Python目录下就可以
- 为了代码整洁性以及可读性,程序员约定将试图函数放到views.py文件中

urls.py

```python
from django.contrib import admin
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"index/", views.index),
    re_path(r'login/', views.login)
]
```

views.py

```python
from django.shortcuts import HttpResponse, render, redirect
def index(request):
    print('请求方法:', request.method)
    import time
    ctime = time.time()
    return render(request, 'index.html', {"timer": ctime})
```

代码解释:

- 我们从 django.shortcuts模块导入了HttpResponse类,以及Python的time库
- 定义了index函数,它就是一个视图函数,函数名与urls.py文件中导入的文件名要一致,两个文件要互相映射,函数名定义一定要见名知意
- 视图会返回一个HttpResponse对象,其中包含生成的响应

## 2. HttpReques对象

request属性:

Django将请求报文中的请求头,请求行,以及请求体封装成request类中的属性.除了特殊说明的之外,其他均为只读的.

```python
'''
1.request.GET
　　获取到一个类似于字典的对象,包含HTTP GET的所有参数。
2.request.POST
　　获取到一个类似于字典的对象,包含HTTP POST的所有参数
　　POST请求可以带有空的POST字典,如果通过HTTP POST方法发送一个表单,但是表单中没有任何的数据,QueryDict对象依然会被创建。因此,不应该使用if request.POST来检查使用的是否是POST方法;应该使用if request.method == "POST"
另外:如果使用POST上传文件的话，文件信息将包含在 FILES 属性中。
    注意:键值对的值是多个的时候,比如checkbox类型的input标签,select标签,需要用:
request.POST.getlist("hobby")获取值
3.request.body
　　获取到一个字符串,代表请求报文的主体.在处理非HTTP形式的报文时非常有用，例如：二进制图片、XML,Json等。
　　但是，如果要处理表单数据的时候,推荐还是使用 request.POST .
4.request.path
　　获取到一个字符串,表示请求的路径组件（不含域名和get请求参数）.
　　例如："/music/bands/the_beatles/"
5.request.get_full_path
	获取到一个字符串,表示请求的路径组件,包含get请求参数.
6.request.method
　　获取到一个字符串，表示请求使用的HTTP方法.必须使用大写。
　　例如："GET"、"POST"
7.request.encoding
　　获取到一个字符串,表示提交的数据的编码方式（如果为 None 则表示使用 DEFAULT_CHARSET 的设置，默认为 'utf-8'）。
   这个属性是可写的，你可以修改它来修改访问表单数据使用的编码。
   接下来对属性的任何访问（例如从 GET 或 POST 中读取数据）将使用新的 encoding 值。
   如果你知道表单数据的编码不是 DEFAULT_CHARSET ，则使用它。
8.request.META
 　　获取到一个标准的Python字典,包含所有的HTTP头部.具体的头部信息取决于客户端和服务器，下面是一些示例：
    CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
    CONTENT_TYPE —— 请求的正文的MIME 类型。
    HTTP_ACCEPT —— 响应可接收的Content-Type。
    HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
    HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
    HTTP_HOST —— 客服端发送的HTTP Host 头部。
    HTTP_REFERER —— Referring 页面。
    HTTP_USER_AGENT —— 客户端的user-agent 字符串。
    QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。
    REMOTE_ADDR —— 客户端的IP 地址。
    REMOTE_HOST —— 客户端的主机名。
    REMOTE_USER —— 服务器认证后的用户。
    REQUEST_METHOD —— 一个字符串，例如"GET" 或"POST"。
    SERVER_NAME —— 服务器的主机名。
    SERVER_PORT —— 服务器的端口（是一个字符串）。
 　　从上面可以看到，除 CONTENT_LENGTH 和 CONTENT_TYPE 之外，请求中的任何 HTTP 首部转换为 META 的键时，
    都会将所有字母大写并将连接符替换为下划线最后加上 HTTP_  前缀。
    所以，一个叫做 X-Bender 的头部将转换成 META 中的 HTTP_X_BENDER 键。
9.request.FILES
　　获取到一个类似于字典的对象，包含所有的上传文件信息。
   FILES 中的每个键为<input type="file" name="" /> 中的name，值则为对应的数据。
　　注意，FILES 只有在请求的方法为POST 且提交的<form> 带有enctype="multipart/form-data" 的情况下才会
   包含数据。否则，FILES 将为一个空的类似于字典的对象。
10.request.COOKIES
　　获取到一个标准的Python 字典，包含所有的cookie。键和值都为字符串。
11.request.session
 　　一个既可读又可写的类似于字典的对象，表示当前的会话。只有当Django 启用会话的支持时才可用。
12.request.user(用户认证组件下使用)
　　一个 AUTH_USER_MODEL 类型的对象，表示当前登录的用户。
　　如果用户当前没有登录，user 将设置为 django.contrib.auth.models.AnonymousUser 的一个实例。你可以通过 is_authenticated() 区分它们。
    例如：
    if request.user.is_authenticated():
        # Do something for logged-in users.
    else:
        # Do something for anonymous users.
     　　user 只有当Django 启用 AuthenticationMiddleware 中间件时才可用。
     -------------------------------------------------------------------------------------
    匿名用户
    class models.AnonymousUser
    django.contrib.auth.models.AnonymousUser 类实现了django.contrib.auth.models.User 接口，但具有下面几个不同点：
    id 永远为None。
    username 永远为空字符串。
    get_username() 永远返回空字符串。
    is_staff 和 is_superuser 永远为False。
    is_active 永远为 False。
    groups 和 user_permissions 永远为空。
    is_anonymous() 返回True 而不是False。
    is_authenticated() 返回False 而不是True。
    set_password()、check_password()、save() 和delete() 引发 NotImplementedError。
    New in Django 1.8:
    新增 AnonymousUser.get_username() 以更好地模拟 django.contrib.auth.models.User。
'''
```

request常用方法:

```python
'''
1.request.get_full_path()
　　返回path,如果可以将加上查询字符串。
　　例如："/music/bands/the_beatles/?print=true"
2.request.is_ajax()
　　如果请求是通过XMLHttpRequest发起的，则返回True，方法是检查 HTTP_X_REQUESTED_WITH 相应的首部是否是字符串'XMLHttpRequest'。
　　大部分现代的 JavaScript 库都会发送这个头部。如果你编写自己的 XMLHttpRequest 调用（在浏览器端）,你必须手工设置这个值来让is_ajax()可以工作。
　　如果一个响应需要根据请求是否是通过AJAX 发起的，并且你正在使用某种形式的缓存例如Django 的 cache middleware，
   你应该使用 vary_on_headers('HTTP_X_REQUESTED_WITH') 装饰你的视图以让响应能够正确地缓存。
'''
```

## 3. HttpResponse对象

响应对象主要有三种形式：

- HttpResponse() 

    - 括号内直接跟一个具体的字符串作为响应体，比较直接很简单.

- render() 

    - 就是将一个模板页面中的模板语法进行渲染，最终渲染成一个html页面作为响应体

    ```python
    return render(request, 'template_name', {"context": context})
    # 返回一个渲染后的HttpResponse对象和给定的模板和一个给定的上下文字典。
    ```

    参数:

    - request： 用于生成响应的请求对象。
    - template_name：要使用的模板的完整名称，可选的参数
    - context：添加到模板上下文的一个字典。默认是一个空字典。如果字典中的某个值是可调用的，视图将在渲染模板之前调用它。

- redirect()

    - 传递要重定向的一个硬编码的URL

        ```python
        def login(request):
            if request.method == 'POST':
                user = request.POST.get('user')
                pwd = request.POST.get('pwd')
                if user == 'alex' and pwd == '123':
                	# 重定向
                    return redirect("/index/")
            return render(request, 'login.html')
        ```

    补充:

    ```python
    '''
    1.301和302的区别。
    301和302状态码都表示重定向，就是说浏览器在拿到服务器返回的这个状态码后会自动跳转到一个新的URL地址，这个地址可以从响应的Location首部中获取.(用户看到的效果就是他输入的地址A瞬间变成了另一个地址B)——这是它们的共同点。他们的不同在于。
    301表示旧地址A的资源已经被永久地移除了（这个资源不可访问了），搜索引擎在抓取新内容的同时也将旧的网址交换为重定向之后的网址；
    302表示旧地址A的资源还在（仍然可以访问），这个重定向只是临时地从旧地址A跳转到地址B，搜索引擎会抓取新的内容而保存旧的网址。 
    所以302好于301
    2.重定向原因：
    （1）网站调整（如改变网页目录结构）；
    （2）网页被移到一个新地址；
    （3）网页扩展名改变(如应用需要把.php改成.Html或.shtml)。
    这种情况下，如果不做重定向，则用户收藏夹或搜索引擎数据库中旧地址只能让访问客户得到一个404页面错误信息，访问流量白白丧失；再者某些注册了多个域名的网站，也需要通过重定向让访问这些域名的用户自动跳转到主站点等。
    '''
    ```

    

