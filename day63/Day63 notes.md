# Day63 notes

## 今日内容

- 用户认证

#### 1.用户认证

**auth模块**

```python
from django.contrib import auth
```

django.contrib.auth中提供了许多方法，这里主要介绍常用的三个：

- authenticate()

    提供了用户认证，即验证用户名以及密码是否正确,一般需要username password两个关键字参数
    如果认证信息有效，会返回一个 User 对象。authenticate()会在User 对象上设置一个属性标识那种认证后端认证了该用户，且该信息在后面的登录过程中是需要的。当我们试图登陆一个从数据库中直接取出来不经过authenticate()的User对象会报错的！！

```PYTHON
user = authenticate(username='someone',password='somepassword')
```

- login(HttpRequest, user)　　

    该函数接受一个HttpRequest对象，以及一个认证了的User对象
    此函数使用django的session框架给某个已认证的用户附加上session id等信息。

```PYTHON
from django.contrib.auth import authenticate, login

def my_view(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  if user is not None:
    login(request, user)
    # Redirect to a success page.
    ...
  else:
    # Return an 'invalid login' error message.
    ...
```

- logout(request) 注销用户

    该函数接受一个HttpRequest对象，无返回值。当调用该函数时，当前请求的session信息会全部清除。该用户即使没有登录，使用该函数也不会报错。

```python
from django.contrib.auth import logout

def logout_view(request):
  logout(request)
  # Redirect to a success page.
```

#### 2.User对象

User 对象属性：username， password（必填项）password用哈希算法保存到数据库。

**2.1 user对象的 is_authenticated()**

如果是真正的 User 对象，返回值恒为 True 。 用于检查用户是否已经通过了认证。
通过认证并不意味着用户拥有任何权限，甚至也不检查该用户是否处于激活状态，这只是表明用户成功的通过了认证。 这个方法很重要, 在后台用request.user.is_authenticated()判断用户是否已经登录，如果true则可以向前台展示request.user.name

要求：

- 用户登陆后才能访问某些页面
- 如果用户没有登录就访问该页面的话直接跳到登录页面
- 用户在跳转的登陆界面中完成登陆后，自动访问跳转到之前访问的地址

方法1:

```python
def my_view(request):
  if not request.user.is_authenticated():
    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
```

方法2:
django已经为我们设计好了一个用于此种情况的装饰器：login_requierd()

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
  ...
```

若用户没有登录，则会跳转到django默认的 登录URL '/accounts/login/ ' (这个值可以在settings文件中通过LOGIN_URL进行修改)。并传递 当前访问url的绝对路径 (登陆成功后，会重定向到该路径)。

**2.2 创建用户：**

使用 create_user 辅助函数创建用户:

```python
from django.contrib.auth.models import User
user = User.objects.create_user（username='',password='',email=''）
```

**2.3 check_password(passwd)：**
用户需要修改密码的时候 首先要让他输入原来的密码 ，如果给定的字符串通过了密码检查，返回 True

**2.4 修改密码：**
使用 set_password() 来修改密码

```python
user = User.objects.get(username='')
user.set_password(password='')
user.save
```

示例：视图

```python
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        # 如果验证成果返回user对象，否则返回None
        user = auth.authenticate(username=user, password=pwd)
        if user:
            # 登录成功后 request.user 为当前登录对象
            auth.login(request, user)

            # 获取next的值路径，如果有则跳转到对应的路径，如果没有则跳转到index路径
            next_url = request.GET.get("next", "/index/")
            return redirect(next_url)

    return render(request, "login.html")


@login_required  # 在settings中配置好登录路径(LOGIN_URL = "/login/")，登录前在该路径进行登录验证
def index(request):
    # print("request:user", request.user)
    # print("id", request.user.id)
    # print("anon", request.user.is_anonymous)
    #
    # # if request.user.is_anonymous:
    # if not request.user.is_authenticated:  # 是否通过验证
    #     return redirect("/login/")
    # # username = request.user.username
    # # return render(request, "index.html", {"username": username})

    # request.user.username 直接在模版中写
    return render(request, "index.html")


@login_required
def order(request):
    # if not request.user.is_authenticated:
    #     return redirect("/login/")
    return render(request, "order.html")


def logout(request):
    auth.logout(request)

    return redirect("/login/")


def reg(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user = User.objects.create_user(username=user, password=pwd)
        return redirect("/login/")

    return render(request, "reg.html")
```

模板：

1.index.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h3>Hi~, {{ request.user.username }}</h3>
<a href="/logout/">注销</a>
</body>
</html>
```

2.login.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h3>登录</h3>
<form action="" method="post">
    {% csrf_token %}
    用户名：<input type="text" name="user">
    密码：<input type="text" name="pwd">
    <input type="submit" value="submit">
</form>

</body>
</html>
```

3.order.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h3>order</h3>

</body>
</html>
```

4.reg.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h3>注册</h3>
<form action="" method="post">
    {% csrf_token %}
    用户名：<input type="text" name="user">
    密码：<input type="text" name="pwd">
    <input type="submit" value="submit">
</form>

</body>
</html>
```

