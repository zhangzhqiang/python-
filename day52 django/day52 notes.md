# Day52 notes

## 1. 内容概要

- web框架的本质
- django的下载安装使用

## 2. 内容回顾

- python基础
- 面向对象
- 网络编程
- 并发编程
- 数据库
- 前端
- TCP/IP五层模型
    - 应用层
    - 传输层
    - 网络层
    - 数据链路层
    - 物理层

- socket(位于应用程序和传输层之间的虚拟层一组接口)

## 3.详细内容

### 1. HTTP协议简介

- HTTP协议(请求和应答,应用层协议)

    - 状态码
        - 1xx 消息
        - 2xx 成功
        - 3xx 重定向
        - 4xx 请求错误
        - 5xx 服务端的错误
    - 请求方式8种(常用的2种)
        - get  获取一个页面,图片
        - post  提交数据

    - url

        http://www.cnblogs.com/maple-shaw/articles/9060408.html

        url包括(协议 域名和端口 HTTP（80） HTTPS(443) 路径 参数)

        ```python
        # http://www.luffycity.com:80/news/index.html?id=250&page=1
        1.http	协议
        2.www.luffycity.com	域名
        3.80	端口
        4.news/index.html	路径
        5.?id=250&page=1	参数
        ```

- get与post请求

    - GET请求提交的数据会放在URL之后，以?分割URL和传输数据，参数之间以&相连， POST方法是把提交的数据放在HTTP包的Body中.
    - GET请求提交的数据大小有限制（因为浏览器对URL的长度有限制），而POST请求提交的数据没有限制.
    - GET与POST请求在服务端获取请求数据方式不同。
    - GET请求提交数据，会带来安全问题，比如一个登录页面，通过GET请求提交数据时，用户名和密码将出现在URL上，如果页面可以被缓存或者其他人可以访问这台机器，就可以从历史记录获得该用户的账号和密码.

- 请求格式![1561477190047](C:\Users\ike\AppData\Roaming\Typora\typora-user-images\1561477190047.png)

    请求首行与请求头的部分用\r\n分隔,请求头与请求体以\r\n\r\n分隔

- 响应格式![1561477206961](C:\Users\ike\AppData\Roaming\Typora\typora-user-images\1561477206961.png)



### 2. web框架

- C/S 是客户端/服务器端程序
- B/S 是浏览器端/服务器端应用程序,WEB应用程序一般是B/S模式
- 百度的服务器 socket服务端
    1. 创建socket服务端
    2. 绑定IP和端口
    3. 监听
    4. 等待链接
    5. 接收数据
    6. 返回数据
    7. 断开链接
- 浏览器socket客户端
    1. 创建socket服务端
    2. 绑定IP和端口
    3. 发送数据
    4. 接收数据
    5. 断开链接

- wb框架------>socket服务端

    Web框架（Web framework）是一种开发框架，用来支持动态网站、网络应用和网络服务的开发。这大多数的web框架提供了一套开发和部署网站的方式，也为web行为提供了一套通用的方法。web框架已经实现了很多功能，开发人员使用框架提供的方法并且完成自己的业务逻辑，就能快速开发web应用了。浏览器和服务器的是基于HTTP协议进行通信的。也可以说web框架就是在以上十几行代码基础张扩展出来的，有很多简单方便使用的方法，大大提高了开发的效率。

```python
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8901))
sock.listen(5)

while True:
    print('server waiting....')
    # conn客户端的套接字
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print('data', data)

    # 读取文件
    with open('login.html', 'r')as f:
        data = f.read()

    # http协议/版本/ 状态码/ 成功
    conn.send(("HTTP/1.1 200 OK\r\nContent-type:text\r\n\r\n%s" % data).encode('gbk'))
    conn.close()

```

- wagiref模块

    wagiref（Web Server Gateway Interface）的简称，封装了socket服务端与客户端的交互，我们可以直接调用其功能，省去了大量的时间,并且判断不同老师能返回不同内容

    ```python
    from wsgiref.simple_server import make_server
    
    
    def application(eviron, start_response):
    
        # 按着http请求协议解析数据:eviron
        # 按着http响应协议组装数据:start_response
        print(eviron)
        print(type(eviron))
    
        # 专注与web业务开发
        # 获取当前路径
        path = eviron.get('PATH_INFO')
        start_response('200 OK', [('Content-Type', 'text/html')])
        if path == '/login':
            with open('login.html', 'r')as f:
                data = f.read()
            return [data.encode('gbk')]
        elif path == '/index.html':
            with open('index.html', 'r')as f:
                data = f.read()
            return [data.encode('gbk')]
    
    
    # 封装socket链接前三步
    httped = make_server("", 8061, application)
    
    # 等待用户链接 conn,addr = sock.accept()
    httped.serve_forever()
    ```

### 3. django的下载与基本命令

1. 下载django：

    ```python
    pip3 install django
    ```

2. 创建一个django project

    ```python
    django-admin.py startproject mysite
    ```

    会创建一个mysite的项目，目录结构如下：

    ```python
    |---manage.py  # django项目里的工具,可以通过它调用django shell和数据库等,管理django站点
    |---mysite  # 文件夹
    	|---_init__.py  # 初始化文件
    	|---settings.py  # 包含了项目的默认配置,包括数据库信息及其他的一些配置信息
    	|---urls.py  # 负责把url模式影协到应用程序,url根配置
    	|---wsgi.py  # 内置runserver命令的WSGI应用配置
    ```

3. 在mysite目录下创建应用

    ```python
    python manage.py startapp blog
    ```

    ```python
    blog
    |---_init__.py
    |---admin.py
    |---apps.py
    |---models.py
    |---tests.py
    |---views.py
    |---migrations
    	|---__init__.py
    ```

4. 启动django项目

    ```
    python manage.py runserver 8080
    ```

    这样我们的django就启动起来了！我们可以访问:http://127.0.0.1:8080

5. django基础必备三件套:

    - HttpResponse内部传入一个字符串参数,返回给浏览器

        ```python
        from django.shortcuts import HttpResponse
        def index(request):
            # 业务逻辑代码
            return HttpResponse("hello,world!")
        ```

    - render除request参数外还接收一个待渲染的模板文件一个保存具体数据的字典参数,将数据填充进模板文件,最后把结果返回给浏览器.

        ```python
        from django.urls import reverse
        
        def timer(request):
        	# 业务逻辑
            return render(request,"timer.html",{"date":ctime})
        ```

    - redirect 接受一个URL参数，表示跳转到指定的URL。

        ```python
        from django.shortcuts import redirect
        def index(request):
            # 业务逻辑代码
            return redirect("/home/")
        ```

