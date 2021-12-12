# Day62 notes

## 今日内容

- cookie与session

#### 1. cookie与session

生活中我们登陆一些网站经常都是以登录状态才可以访问，但是每个功能都是独立的，cookie与session简单的来说就是帮助我们保持登录状态，在登录的状态下访问更多的网页。

总结：

我们知道HTTP协议是无状态协议，也就是说每个请求都是独立的！无法记录前一次请求的状态。但HTTP协议中可以使用Cookie来完成会话跟踪！在Web开发中，使用session来完成会话跟踪，session底层依赖Cookie技术。

##### 1.Cookie概述

Cookie翻译成中文是小甜点，小饼干的意思。在HTTP中它表示服务器送给客户端浏览器的小甜点。其实Cookie是key-value结构，类似于一个python中的字典。随着服务器端的响应发送给客户端浏览器。然后客户端浏览器会把Cookie保存起来，当下一次再访问服务器时把Cookie再发送给服务器。 Cookie是由服务器创建，然后通过响应发送给客户端的一个键值对。客户端会保存Cookie，并会标注出Cookie的来源（哪个服务器的Cookie）。当客户端向服务器发出请求时会把所有这个服务器Cookie包含在请求中发送给服务器，这样服务器就可以识别客户端了！

**Cookie规范**

- Cookie大小上限为4KB；
- 一个服务器最多在客户端浏览器上保存20个Cookie；
- 一个浏览器最多保存300个Cookie；
    上面的数据只是HTTP的Cookie规范，但在浏览器大战的今天，一些浏览器为了打败对手，为了展现自己的能力起见，可能对Cookie规范“扩展”了一些，例如每个Cookie的大小为8KB，最多可保存500个Cookie等！但也不会出现把你硬盘占满的可能！

注意，不同浏览器之间是不共享Cookie的。也就是说在你使用IE访问服务器时，服务器会把Cookie发给IE，然后由IE保存起来，当你在使用FireFox访问服务器时，不可能把IE保存的Cookie发送给服务器。一个Cookie对应一个浏览器。

**Cookie与HTTP头**
Cookie是通过HTTP请求和响应头在客户端和服务器端传递的：

- Cookie：请求头，客户端发送给服务器端；
- 格式：Cookie: a=A; b=B; c=C。即多个Cookie用分号离开； Set-Cookie：响应头，服务器端发送给客户端；
- 一个Cookie对象一个Set-Cookie： 
    - Set-Cookie: a=A Set-Cookie: b=B Set-Cookie: c=C

**Cookie的覆盖**
如果服务器端发送重复的Cookie那么会覆盖原有的Cookie，例如客户端的第一个请求服务器端发送的Cookie是：Set-Cookie: a=A；第二请求服务器端发送的是：Set-Cookie: a=AA，那么客户端只留下一个Cookie，即：a=AA。

**django中的cookie语法：**

设置cookie：

```python
rep = HttpResponse(...) 或 rep ＝ render(request, ...) 或 rep ＝ redirect()  
rep.set_cookie(key,value,...)
rep.set_signed_cookie(key,value,salt='加密盐',...)
```

获取cookie：

```python
request.COOKIES
```

删除cookie：

```python
response.delete_cookie("cookie_key",path="/",domain=name)
```

示例：视图

```python
def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user = UserInfo.objects.filter(user=user, pwd=pwd).first()
        if user:
            '''
            响应体：
            '''
            reponse = HttpResponse("Success!")
            # 设置cookies,15秒以后不再保存cookies
            # reponse.set_cookie("is_login", True, max_age=50)
            reponse.set_cookie("is_login", True)

            import datetime
            # 设置具体的时间内有效
            # data = datetime.datetime(year=2019, month=7, day=13, hour=15, minute=32, second=10)
            # reponse.set_cookie("username", user.user, expires=data)
            # 设置有效路径
            reponse.set_cookie("username", user.user, path="/index/")
            return reponse

    return render(request, 'login.html')


def index(request):
    print(request.COOKIES)
    # 获取cookies的值
    get_is_login = request.COOKIES.get("is_login")
    # 判断cookies是否存在
    if get_is_login:
        # 获取cookies设置的名字
        username = request.COOKIES.get("username")
        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        last_now = request.COOKIES.get("last_visit_time", "")
        response = render(request, "index.html", {"username": username, "last_now": last_now})
        # 设置最后一次登录时间
        response.set_cookie("last_visit_time", now)
        return response

    else:
        return render(request, "login.html")

def test(request):
    print(request.COOKIES)

    return HttpResponse("test测试")
```

##### 2.Session概述

Session是服务器端技术，利用这个技术，服务器在运行时可以 为每一个用户的浏览器创建一个其独享的session对象，由于 session为用户浏览器独享，所以用户在访问服务器的web资源时 ，可以把各自的数据放在各自的session中，当用户再去访问该服务器中的其它web资源时，其它web资源再从用户各自的session中 取出数据为用户服务。

**django中session语法：**

```python
1、设置Sessions值
          request.session['session_name'] ="admin"
2、获取Sessions值
          session_name = request.session["session_name"]
3、删除Sessions值
          del request.session["session_name"]
4、flush()
     删除当前的会话数据并删除会话的Cookie。
     这用于确保前面的会话数据不可以再次被用户的浏览器访问
5、get(key, default=None)
  fav_color = request.session.get('fav_color', 'red')  
6、pop(key)
  fav_color = request.session.pop('fav_color')  
7、keys()
8、items()  
9、setdefault()  
10 用户session的随机字符串
        request.session.session_key

        # 将所有Session失效日期小于当前日期的数据删除
        request.session.clear_expired()

        # 检查 用户session的随机字符串 在数据库中是否
        request.session.exists("session_key")

        # 删除当前用户的所有Session数据
        request.session.delete("session_key")

        request.session.set_expiry(value)
            * 如果value是个整数，session会在些秒数后失效。
            * 如果value是个datatime或timedelta，session就会在这个时间后失效。
            * 如果value是0,用户关闭浏览器session就会失效。
            * 如果value是None,session会依赖全局session失效策略。
```

session配置：

```python
# Django默认支持Session，并且默认是将Session数据存储在数据库中，即：django_session 表中。

# 配置 settings.py

    SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）

    SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
    SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
    SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
    SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
    SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
    SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
    SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
```

示例：视图

```python
def login_session(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user = UserInfo.objects.filter(user=user, pwd=pwd).first()

        if user:
            import datetime
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.session["is_login"] = True
            request.session["username"] = user.user

            request.session["last_visit_time"] = now

            # TODO：今天看到cookie 和 session 设置和获取值
            # 显示登录人的姓名，登录时间
            # 一个浏览器对应一个服务器
            # 重复登录一个浏览器生成一个随机字符串，session－data会更新至最后一次

            '''
            if request.COOKIE.get("sessionid"):
                更新
                在django－sessoin表中创建一条记录
                    session－key         session－data
                    12asda               更新数据：｛"is_login":True, "username":"ike"｝
            else:
                三步骤：
                    1.生成一个随机字符串：12asda
                    2.response.set_cookies("sessionid",12asda)
                    3.在django－sessoin表中创建一条记录
                        session－key     session－data
                        12asda          ｛"is_login":True, "username":"ike"｝
            '''
            return HttpResponse("登录成功")

    return render(request, "login.html")


def index_session(request):
    print("验证", request.session.get("is_login"))

    '''
    
    三步骤：
        1.request.COOKIE.get("session")
        2.django-session表中过滤数据：
            在django－session表中添加数据：
            session－key             session－data
            12asda          ｛"is_login":True, "username":"ike"｝
            obj = django-session.objects.filter(session-key=12asda).first()
        3.取出session字典
            obj ＝ session-data.get("is_login")
    '''
    is_login = request.session.get("is_login")
    if not is_login:
        return redirect("/login_session/")

    username = request.session.get("username")
    last_visit_time = request.session.get("last_visit_time")

    return render(request, "index.html", {"username": username, "last_visit_time": last_visit_time})


def logout(request):
    # del request.session["is_login"]
    request.session.flush()
    '''
    randon_str = request.COOKIE.get("sessionid")
    django_session.objects.filter(session_key=randon_str).delete()
    response.delete_cookie("sessionid", randon_str)
    '''

    return redirect("/login_session/")
```

模板：index.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h3>hi {{ username }}</h3>
<p>上次登录时间：{{ last_visit_time }}</p>
<a href="/logout/">注销</a>
</body>
</html>
```

login.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<form action="" method="post">
    {% csrf_token %}
    用户名：<input type="text" name="user">
    密码：<input type="text" name="pwd">
    <input type="submit">
</form>
</body>
</html>
```

