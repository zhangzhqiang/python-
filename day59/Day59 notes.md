# Day59 notes

## 今日内容

- Djanjo与Ajax

#### 1. Djanjo与Ajax

Ajax（Asynchronous Javascript And XML）翻译成中文就是“异步Javascript和XML”。即使用Javascript语言与服务器进行异步交互，传输的数据为XML（当然，传输的数据不只是XML,现在更多使用json数据）。

- 同步交互：客户端发出一个请求后，需要等待服务器响应结束后，才能发出第二个请求；
- 异步交互：客户端发出一个请求后，无需等待服务器响应结束，就可以发出第二个请求。

AJAX除了**异步**的特点外，还有一个就是：浏览器页面**局部刷新**；（这一特点给用户的感受是在不知不觉中完成请求和响应过程）

**优点：**

- AJAX使用Javascript技术向服务器发送异步请求
- AJAX无须刷新整个页面

**基于jquery的Ajax：**

index.html

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="http://ajax.aspnetcdn.com/ajax/jquery/jquery-2.1.4.min.js"></script>
</head>
<body>
<h2>this is index!</h2>
<button class="Ajax">Ajax</button>
<p class="content"></p>
<script>
    $(".Ajax").click(function () {
        // 发送Ajax请求
        $.ajax({
            url:"/test_ajax/",  // 请求url
            type:"get",  // 请求方式post
            success:function (data) {  //回调函数：某个动作执行结束再回来执行的函数
                console.log(data)

                $(".content").html(data)  // 显示到页面
            }
        })
    })
</script>
</body>
</html>
```

url.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('test_ajax/', views.test_ajax)
]
```

views.py

```python
from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):

    return render(request, 'index.html')


def test_ajax(request):
    return HttpResponse("hello world!")
```

示例一：计算器和登录验证

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="http://ajax.aspnetcdn.com/ajax/jquery/jquery-2.1.4.min.js"></script>
</head>
<body>
<h3>this is index!</h3>
<button class="Ajax">Ajax</button>
<hr>
{#<form action="" method="">#}
{#    <input type="text" name="user">#}
{#    <input type="text" name="pwd">#}
{#    <input type="submit">#}
{#</form>#}

<input type="text" id="num1"> +
<input type="text" id="num2"> =
<input type="text" id="ret">
<button class="cal">计算</button>

<hr>

<form action="">
    用户名:<input type="text" id="user">
    密码:<input type="password" id="pwd">
    <input type="button" value="提交" class="login_btn"><span class="error"></span>
</form>
<script>
    // Ajax计算求值
    $('.cal').click(function () {
        $.ajax({
            url:'/cal/',
            type:'post',
            data:{
                'n1':$('#num1').val(),
                'n2':$('#num2').val(),
            },
            success:function (data) {
                $('#ret').val(data)
            }
        })
    })

    // 登录验证
    $(".login_btn").click(function () {
        $.ajax({
            url:"/login/",
            type:"post",
            data:{
                'user':$("#user").val(),
                'pwd':$("#pwd").val()
            },
            success:function (data) {
                console.log(data);  //打印数据
                console.log(typeof data);  //打印数据类型

                var data = JSON.parse(data); //反序列化 object
                console.log(data);  //打印数据
                console.log(typeof data);  //打印数据类型
                // 用户名和密码匹配跳转到百度
                if (data.user){
                    location.href="http://www.baidu.com"
                }
                else {
                    $(".error").html(data.msg).css({"color":"red", "margin-left": "10px"})
                }
            }
        })

    })
</script>
</body>
</html>
```

##### 1.1 文件上传

**一、请求头ContentType**

ContentType指的是请求体的编码类型，常见的类型共有3种：

- application/x-www-form-urlencoded

    - 这应该是最常见的 POST 提交数据的方式了。浏览器的原生表单，如果不设置 enctype 属性，那么最终就会以 application/x-www-form-urlencoded 方式提交数据。求类似于下面这样（无关的请求头在本文中都省略掉了）：

    ```js
    POST http://www.example.com HTTP/1.1
    Content-Type: application/x-www-form-urlencoded;charset=utf-8
    
    user=yuan&age=22
    ```

- multipart/form-data
    - 这又是一个常见的 POST 数据提交的方式。我们使用表单上传文件时，必须让表单的 enctype 等于 multipart/form-data。示例：

        ```js
        POST http://www.example.com HTTP/1.1
        Content-Type:multipart/form-data;
        ```

- application/json
    - application/json 这个 Content-Type 作为响应头大家肯定不陌生。实际上，现在越来越多的人把它作为请求头，用来告诉服务端消息主体是序列化后的 JSON 字符串。由于 JSON 规范的流行，除了低版本 IE 之外的各大浏览器都原生支持 JSON.stringify，服务端语言也都有处理 JSON 的函数，使用 JSON 不会遇上什么麻烦。
        JSON 格式支持比键值对复杂得多的结构化数据，这一点也很有用。记得我几年前做一个项目时，需要提交的数据层次非常深，我就是把数据 JSON 序列化之后来提交的。不过当时我是把 JSON 字符串作为 val，仍然放在键值对里，以 x-www-form-urlencoded 方式提交。

上面提到的这两种 POST 数据的方式，都是浏览器原生支持的，而且现阶段标准中原生表单也只支持这两种方式（通过 元素的 enctype 属性指定，默认为 application/x-www-form-urlencoded。其实 enctype 还支持 text/plain，不过用得非常少）。
随着越来越多的 Web 站点，尤其是 WebApp，全部使用 Ajax 进行数据交互之后，我们完全可以定义新的数据提交方式，给开发带来更多便利。

**二、基于form表单和Ajax的文件上传**

示例：视图

```python
def file_put(request):
    if request.method == 'POST':
        # print("body", request.body)  # 请求报文中的请求体
        print("post", request.POST)  # if contentType == urlencode的时候,request.POST才有数据

        print(request.FILES)

        file_obj = request.FILES.get('avatar')
        with open(file_obj.name, 'wb')as f:
            for line in file_obj:
                f.write(line)
        return HttpResponse("OK")

    return render(request, 'file_put.html')
```

模板：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="http://ajax.aspnetcdn.com/ajax/jquery/jquery-2.1.4.min.js"></script>
</head>
<body>
<h3>简单的form</h3>
<form action="" method="post">
    用户名<input type="text" name="user">
    密码 <input type="password" name="pwd">
    <input type="submit">
</form>

<hr>

<h3>基于form表单的文件上传</h3>
<form action="" method="post" enctype="multipart/form-data">
    用户名 <input type="text" name="user">
    头像 <input type="file" name="avatar">
    <input type="submit">
</form>

<hr>

<h3>基于Ajax文件上传</h3>
<form action="" method="post">
    用户名<input type="text" id="user">
    头像 <input type="file" id="avatar">
    <input type="button" class="btn" value="ajax">
</form>

<script>
    // json序列化
    $(".btn").click(function () {
        $.ajax({
            url:"",
            type:"post",
            contentType:"application/json",
            data:JSON.stringify({  //json序列化
                a:1,
                b:2
            }),
            success:function (data) {
                console.log(data)
            }
        })
    })
    $(".btn").click(function () {
        $.ajax({
            url:"",
            type:"post",
            data:{
                a:1,
                b:2
            },
            success:function (data) {
                console.log(data)
            }
        })
    })

    // ajax上传文件
    $(".btn").click(function () {
        var formata = new FormData();
        formata.append("user", $("#user").val());
        formata.append("avatar", $("#avatar")[0].files[0]);
        $.ajax({
            url:"",
            type:"post",
            contentType:false,  //
            processData:false,  //
            data:formata,
            success:function (data) {
                console.log(data)
            }
        })
    })
</script>
</body>
</html>
```

