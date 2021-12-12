# Day64 notes

## 今日内容

- 中间件

#### 1.中间件

##### 1.1 中间件的概念

中间件顾名思义，是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出。因为改变的是全局，所以需要谨慎实用，用不好会影响到性能。
如果你想修改请求，例如被传送到view中的HttpRequest对象。 或者你想修改view返回的HttpResponse对象，这些都可以通过中间件来实现。
可能你还想在view执行之前做一些操作，这种情况就可以用 middleware来实现。
Django默认的Middleware：每一个中间件都有具体的功能。

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

##### 1.2 自定义中间件

中间件中一共有四个方法：

- process_request

- process_view

- process_exception
- process_response

当用户发起请求的时候会依次经过所有的的中间件，这个时候的请求时process_request,最后到达views的函数中，views函数处理后，在依次穿过中间件，这个时候是process_response,最后返回给请求者。

我们也可以自己定义一个中间件，我们可以自己写一个类。

示例：视图

```python
def index(request):

    print("index")

    return HttpResponse("hello")
```

自定义中间件1：process_request和process_response

```python
from django.middleware.security import SecurityMiddleware


class CustomerMiddleware(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware1 process_request")

    def process_response(self, request, response):
        print("CustomerMiddleware1 process_response")
        return response


class CustomerMiddleware2(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware2 process_request..")

    def process_response(self, request, response):
        print("CustomerMiddleware2 process_response")

        return response
```

注意：如果当请求到达请求2的时候直接不符合条件返回，即return HttpResponse("Md2中断")，程序将把请求直接发给中间件2返回，然后依次返回到请求者。

流程图：![中间件1](G:\homework\img\中间件1.png)

自定义中间件2：process_view

```python
from django.middleware.security import SecurityMiddleware


class CustomerMiddleware(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware1 process_request")

    def process_response(self, request, response):
        print("CustomerMiddleware1 process_response")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('CustomerMiddleware1 process_view')


class CustomerMiddleware2(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware2 process_request..")

    def process_response(self, request, response):
        print("CustomerMiddleware2 process_response")

        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
		
        print('======>', callback)
        print('======>', request)
        print('CustomerMiddleware2 process_view')
        # response=callback(request,*callback_args,**callback_kwargs)
        # return response
```

当最后一个中间的process_request到达路由关系映射之后，返回到中间件1的process_view，然后依次往下，到达views函数，最后通过process_response依次返回到达用户。

注意：process_view如果有返回值，会越过其他的process_view以及视图函数，但是所有的process_response都还会执行。

流程图：![中间件2](G:\homework\img\中间件2.png)

之定义中间件3：process_exception

```python
from django.middleware.security import SecurityMiddleware


class CustomerMiddleware(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware1 process_request")

    def process_response(self, request, response):
        print("CustomerMiddleware1 process_response")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('CustomerMiddleware1 process_view')

    def process_exception(self):
        print("CustomerMiddleware1 process_exception...")


class CustomerMiddleware2(SecurityMiddleware):

    def process_request(self, request):
        print("CustomerMiddleware2 process_request..")

    def process_response(self, request, response):
        print("CustomerMiddleware2 process_response")

        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):

        print('======>', callback)
        print('======>', request)
        print('CustomerMiddleware2 process_view')

    def process_exception(self):
        print("CustomerMiddleware2 process_exception...")
```

当views出现错误时：

流程图：![中间件3](G:\homework\img\中间件3.png)

