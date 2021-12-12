# Day nots 49

## 今日内容

- 对DOM文档的操作

### 1.DOM文档的操作

#### **一.插入操作：**

##### 知识点1：父子之间

语法：追加某元素，在父元素中添加新的子元素。子元素可以为：stirng | element（js对象） | jquery元素

```
父元素.append(子元素)
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div class="wuSir">wusir</div>
	<div class="box"></div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			var oP = document.createElement('p');
			oP.innerText = '基友';
			// 1.父子之间 父.append(子)  子.appendTo(父)
			// 子元素：可以是 一个string、jsDOM对象、jquery对象
			$('.box').append('alex');// 可以插入普通的文本
			$('.box').append('<h2>alex</h2>');// 可以插入标签+文本
			$('.box').append(oP); // 插入一个jsDom对象
			$('.box').append($('.wusir')); // 如果插入的是一个jquery对象 相当于是一个移动操作
		});
	</script>
</body>
</html>
```

##### 知识点2：父子之间

语法：追加到某元素，子元素添加到父元素，要添加的元素同样既可以是stirng 、element(js对象) 、 jquery元素

```
子元素.appendTo(父元素)
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div class="wuSir">wusir</div>
	<div class="box"></div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			$('<p>天霸</p>').appendTo('.box').click(function(event) {
				$(this).css({
					width:100,
					height:100,
					backgroundColor:'red'
				}).text('wuSir');

			});;
		});
	</script>
</body>
</html>
```

##### 知识点3：父子之间

语法：前置添加， 添加到父元素的第一个位置

```javascript
父元素.prepend(子元素)；
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<ul>
		<li>alex</li>
	</ul>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// prepend()   prependTo()
			//1. prepend() 插入 子级的第一个元素
			$('ul').prepend('<好>wusir</li>');
			});
		});
	</script>
</body>
</html>
```

##### 知识点4：父子之间

语法：前置添加， 添加到父元素的第一个位置

```javascript
子元素.prependTo(父元素)；
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<ul>
		<li>alex</li>
	</ul>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			$('<li>村长</li>').prependTo('ul').click(function() {
				alert(this.innerText);
			});
		});
	</script>
</body>
</html>
```

##### 知识点5：兄弟之间

语法：在匹配的元素之后插入内容 

```javascript
兄弟元素.after(要插入的兄弟元素)；
要插入的兄弟元素.inserAfter(兄弟元素)；
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <ul>
        <li class="item">alex</li>
    </ul>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        // es6的模板字符串   tab键上面那个符号  反引号 ``,使用${变量名}插入变量
        var title = "百度一下下";
        $('.item').after(`<li>
			<a href="#">${title}</a>
		</li>`);
        $('<li>wusir</li>').insertAfter('.item');
    </script>
</body>
</html>
```

##### 知识点6：兄弟之间

语法：在匹配的元素之前插入内容 

```javascript
兄弟元素.before(要插入的兄弟元素)；
要插入的兄弟元素.inserBefore(兄弟元素)；
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <ul>
        <li class="item">alex</li>
    </ul>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        var title = "百度一下下";
 	 	$('.item').before(`<li>
			<a href="#">${title}</a>
		</li>`);
		 $('<li>wusir</li>').insertBefore('.item');
    </script>
</body>
</html>
```

#### 二.替换操作：

##### 知识点1：

语法：将所有匹配的元素替换成指定的string、js对象、jquery对象。

```
$(selector).replaceWith(content);
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div class="box">
		<h2>alexsb</h2>
		<h2>alexsb</h2>
		<h3>wusirddb</h3>
	</div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 页面中获取的DOM对象.replaceWith(替换的内容)
			$('h2').replaceWith('<span>圆圆</span>');
		});
	</script>
</body>
</html>
```

##### 知识点2：

语法：替换所有。将所有的h2标签替换成p标签。

```
$('<p>哈哈哈</p>').replaceAll('h2');
```

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div class="box">
		<h2>alexsb</h2>
		<h2>alexsb</h2>
		<h3>wusirddb</h3>
	</div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			$('<p style = "color:red;">黑girl</p>').replaceAll('span');
		});
	</script>
</body>
</html>
```

#### 三.删除操作：

##### 知识点1：

语法：删除节点后，事件也会删除（简言之，删除了整个标签）

```
$(selector).remove(); 
```

示例：

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div class="box">
        <p style="font-size: 20px;font-weight: 600;">alex</p>
    </div>
    <button>删除</button>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        $('button').click(function() {
        	  alert(1);
            // remove() 删除节点后 事件也会删除  删除了整个标签
            console.log($(this).remove());
            var jqBtn = $(this).remove();
            $('.box').prepend(jqBtn);
        })
    });
    </script>
</body>
</html>
```

##### 知识点2：

语法：删除节点后，事件会保留

```
$(selector).detach(); 
```

示例：

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div class="box">
        <p style="font-size: 20px;font-weight: 600;">alex</p>
    </div>
    <button>删除</button>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        $('button').click(function() {
        	  alert(1);
            // detach() 删除节点后 事件会保留
            var jqBtn = $(this).detach();
            $('.box').prepend(jqBtn);
        })
    });
    </script>
</body>
</html>
```

##### 知识点3：

语法：清空选中元素中的所有后代节点

```
$(selector).empty(); 
```

示例：

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div class="box">
        <p style="font-size: 20px;font-weight: 600;">alex</p>
    </div>
    <button>删除</button>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        $('button').click(function() {
        	  alert(1);
        	  // 清空选中元素中的所有后代节点
			$('.box').empty();
        })
    });
    </script>
</body>
</html>
```

