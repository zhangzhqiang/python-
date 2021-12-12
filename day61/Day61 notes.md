# Day61 notes

## 今日内容

- forms组件

#### 1. forms组件

针对字段进行校验

示例：models.py

```python
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.EmailField()
    tel = models.CharField(max_length=32)
```

模板：渲染标签

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>
<div class="container">
    <div class="row">
        <div class="cal-md-6 col-lg-offset-3">

            <form action="" method="post">
                {% csrf_token %}
                <p>用户名：<input type="text" name="name"></p>
                <p>密码：<input type="text" name="pwd"></p>
                <p>确认密码：<input type="text" name="re_pwd"></p>
                <p>邮箱：<input type="text" name="email"></p>
                <p>电话：<input type="text" name="tel"></p>
                <input type="submit">
            </form>

            <hr>
            <h3>form组件渲染方式1</h3>
            <form action="" method="post" novalidate>
                {% csrf_token %}
                {# lable渲染字段名字，和input标签#}
                <p>{{ form.name.label }}{{ form.name }}</p>
                    <spqn class="pull-right error">{{ form.name.errors.0 }}</spqn>
                <p>{{ form.pwd.label }}{{ form.pwd }}</p>
                    <spqn class="pull-right error">{{ form.pwd.errors.0 }}</spqn>
                <p>{{ form.re_pwd.label }}{{ form.re_pwd }}</p>
                    <spqn class="pull-right error">{{ form.re_pwd.errors.0 }}</spqn><spqn class="pull-right error">{{ errors.0 }}</spqn>
                <p>{{ form.email.label }}{{ form.email }}</p>
                <spqn class="pull-right error">{{ form.email.errors.0 }}</spqn>
                    <p>{{ form.tel.label }}{{ form.tel }}</p>
                <spqn class="pull-right error">{{ form.tel.errors.0 }}</spqn>
                <input type="submit">
            </form>

            <hr>
            <h3>forms组件渲染方式2</h3>
            <form action="" method="post">
                {% csrf_token %}
                {% for field in form %}
                    <p>
                        <lable for="">{{ field.label }}</lable>
                        {{ field }}
                    </p>
                {% endfor %}
            </form>

            <hr>
            <h3>forms组件渲染方式3</h3>
            <form action="" method="post">
                {% csrf_token %}
{#             缺点不灵活：默认p标签，无法切换标签#}
                {{ form.as_p }}
                <input type="submit">
            </form>

        </div>
    </div>
</div>
</body>
</html>
```

视图：

```js
from django.shortcuts import render, HttpResponse

# Create your views here.
from app01.my_forms import *


def reg(request):
    """
    显示错误与重置输入信息功能
    :param request:
    :return:
    """
    if request.method == "POST":

        # form = UserForm({"name":"iker", "email": "123@163.com", "xxx": "alex"})

        form = UserForm(request.POST)  # form表单的name属性对应的值，应该与forms组件的字段名称一致

        print(form.is_valid())  # 返回一个布尔值，所有的值都校验通过
        if form.is_valid():  # 校验返回布尔值
            print(form.cleaned_data)  # 只打印校验成功的键值
        else:
            print(form.cleaned_data)  # 如果校验正确的都会打印出来
            # print(form.errors)  # 如果校验失败，会打印键值和错误信息
            # print(type(form.errors))
            #
            # print(form.errors.get("name"))
            # print(type(form.errors.get("name")))
            #
            # print(form.errors.get("name")[0])

            # 全局钩子错误
            # print(form.errors.get("__all__")[0])
            errors = form.errors.get("__all__")

            return render(request, "reg.html", locals())
        '''
        如果所有字段校验成功：
            则form.cleaned_data:{"name":"ike", "email":"123@163.com"}
            form.errors 如果校验失败，会打印键值和错误信息
        如果校验的字段不包含：
            forms组件与form表单所有字段的校验都成功，多出的字段不会去校验
            键值必须和字段一致
        '''
        # print(request.POST)

    form = UserForm()  # 未绑定数据
    return render(request, "reg.html", locals())
```

form文件：

```python
from django import forms
from django.forms import widgets
from app01.models import UserInfo
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


class UserForm(forms.Form):
    name = forms.CharField(min_length=4, label="用户名",
                           error_messages={"required": "该字段不能为空"},
                           widget=widgets.TextInput(attrs={"class": "form-control"}))
    pwd = forms.CharField(min_length=4, label="密码",
                          widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                          error_messages={"required": "该字段不能为空", "invalid": "格式错误"}
                          )
    re_pwd = forms.CharField(min_length=4, label="确认密码",
                             widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                             error_messages={"required": "该字段不能为空", "invalid": "格式错误"})
    email = forms.EmailField(label="邮箱",
                             error_messages={"required": "该字段不能为空", "invalid": "格式错误"},
                             widget=widgets.TextInput(attrs={"class": "form-control"}))
    tel = forms.CharField(label="手机号",
                          widget=widgets.TextInput(attrs={"class": "form-control"}),
                          error_messages={"required": "手机号不能为空"})

    # 局部钩子
    def clean_name(self):
        val = self.cleaned_data.get("name")
        ret = UserInfo.objects.filter(name=val)

        if not ret:
            return val
        else:
            raise ValidationError("该用户已注册！")

    def clean_tel(self):
        val = self.cleaned_data.get("tel")
        if len(val) == 11:
            return val
        else:
            raise ValidationError("手机号格式错误")

    # 全局钩子
    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")

        if pwd and re_pwd:
            if pwd == re_pwd:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致！")
        else:
            return self.cleaned_data
```

