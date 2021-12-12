# Day60 notes

## 今日内容

- Django组件之分页器

#### 1. 分页器

```python
print(page2.has_next())            #是否有下一页
print(page2.next_page_number())    #下一页的页码
print(page2.has_previous())        #是否有上一页
print(page2.previous_page_number()) #上一页的页码

# 抛错
page=paginator.page(12)   # error:EmptyPage

page=paginator.page("z")   # error:PageNotAnInteger
```

模板：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>

<ul>
    {% for foo in curr_page %}
        <li>{{ foo.title }}:{{ foo.price }}</li>
    {% endfor %}
</ul>

<nav aria-label="Page navigation">
  <ul class="pagination">
    {#判断是否有上一页#}
    {% if curr_page.has_previous %}
        <li>
            <a href="?page={{ curr_page.previous_page_number }}" aria-label="Previous">
                <span aria-hidden="true">上一页</span>
            </a>
        </li>
    {% else %}
        <li class="disabled">
        <a href="" aria-label="Previous">
            <span aria-hidden="true">上一页</span>
        </a>
        </li>
    {% endif %}

    {#  加页码  #}
    {% for item in page_range %}
    {% if current_page == item%}
        <li class="active"><a href="?page={{ item }}">{{ item }}</a></li>
    {% else %}
        <li><a href="?page={{ item }}">{{ item }}</a></li>
    {% endif %}
    {% endfor %}

    {#判断是否有下一页#}
    {% if curr_page.has_next %}
        <li>
          <a href="?page={{ curr_page.next_page_number }}" aria-label="Next">
            <span aria-hidden="true">下一页</span>
          </a>
        </li>
    {% else %}
        <li class="disabled">
          <a href="" aria-label="Next">
            <span aria-hidden="true">下一页</span>
          </a>
        </li>
    {% endif %}
  </ul>
</nav>
</body>
</html>
```

视图：

```python
from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator, EmptyPage


# Create your views here.


def index(request):
    """
    批量导入：
    book_list = []
    for i in range(100):
        book = Book(title='book_%s' % i, price=i * i)
        book_list.append(book)
    Book.objects.bulk_create(book_list)  # 批量插入
    """
    book_list = Book.objects.all()

    # 分页器
    paginator = Paginator(book_list, 3)  # 每页显示10条数据
    print('count:', paginator.count)  # 数据总数
    print('num_pages:', paginator.num_pages)  # 总页数
    print('page_range:', paginator.page_range)  # 页码列表
    current_page = int(request.GET.get('page', 1))

    if paginator.num_pages > 11:
        if current_page - 5 < 1:
            page_range = range(1, 12)
        elif current_page + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages-10, paginator.num_pages + 1)
        else:
            page_range = range(current_page - 5, current_page + 6)
    else:
        page_range = range(current_page - 5, current_page + 6)
    try:

        curr_page = paginator.page(current_page)  # 第几页的page对象
        print(curr_page.object_list)  # 显示某一页的所有数据

        for i in curr_page:  # 遍历当前页的所有数据对象
            print(i)
    except EmptyPage as e:
        curr_page = paginator.page(1)
    return render(request, 'index.html', locals())
```

