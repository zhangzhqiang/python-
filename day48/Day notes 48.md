# Day notes 48

## 今日内容

- jQery属性操作

### 1. jQery属性操作

jQery的属性操作模块分为四个部分：HTML属性操作，DOM属性操作，类样式操作和值操作。

- HTML属性操作：是对HTML文档中的属性进行读取，设置和移除操作。比如attr()、removeAttr()
- DOM属性操作：对DOM元素的属性进行读取，设置和移除操作。比如prop()、removeProp()
- 类样式操作：是指对DOM属性className进行添加，移除操作。比如addClass()、removeClass()、toggleClass()
- 值操作：是对DOM属性value进行读取和设置操作。比如html()、text()、val()

#### 1.1 HTML属性操作

**1.attr()：**设置属性值或者返回被选元素的属性值

示例：获取值：attr()设置一个属性值的时候，只是获取值

```js
<div title = 'tit1' class="active"></div>
console.log($('div').attr('class'));// active
```

示例：设置值的两种方式

```js
// 方式一：
// 设置 属性的时候 不要使用此方式来设置类名  不建议
$('div').attr('class','box1 box2');
// 方式二：
$('a').attr({
    "href":"http://www.baidu.com",
    title:'哈哈哈哈'
});
```

**2.removeAttr()：**移除属性

示例：

```js
// 移除标签的属性
$('div').removeAttr('title id');
```

#### 1.2 DOM属性操作

**1.prop()：** 设置或返回被选元素的属性和值。

- 当该方法用于**返回**属性值时，则返回第一个匹配元素的值。

- 当该方法用于**设置**属性值时，则为匹配元素集合设置一个或多个属性/值对。

语法：

返回属性的值：

```js
$(selector).prop(property)
```

设置属性和值：

```javascript
$(selector).prop(property,value)
```

设置多个属性和值：

```javascript
$(selector).prop({property:value, property:value,...})
```

示例：

```js
// 返回属性值
console.log($('input[type=radio]').prop('checked'));

// 设置属性值
$('input[type=radio]').eq(0).prop('aaaaa','11121111');
console.log($('input[type=radio]').eq(0))
```

**2.removeProp()：**移除属性值

示例：

```js
// 移除属性值
$('input[type=radio]').eq(0).removeProp('aaaaa');
console.log($('input[type=radio]').eq(0))
```

attr()和prop()的使用：

1. 是有true,false两个属性使用prop();

2. 其他则使用attr();

#### 1.3 类样式操作

**1.addClass：**为每个匹配的元素添加指定的类名。

```javascript
$('div').addClass("box");// 追加一个类名到原有的类名
```

还可以为匹配的元素添加多个类名

```javascript
$('div').addClass("box box2");// 追加多个类名
```

**2.removeClass：**从所有匹配的元素中删除全部或者指定的类。

 移除指定的类（一个或多个）

```javascript
$('div').removeClass('box')；
```

移除全部的类

```javascript
$('div').removeClass();
```

**3.toggleClass：**如果存在（不存在）就删除（添加）一个类。

语法：toggleClass('box')

```javascript
$('span').click(function(){
    // 动态的切换class类名为addr
    $(this).toggleClass('addr')
})
```

可以通过添加删除类名，来实现元素的显示隐藏

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
		}
		.hidden{
			display: none;
		}
	</style>
</head>
<body>
	<button id="btn">隐藏</button>
	<div class="box"></div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			var isShow = true;
			$('#btn').click(function(){
				/*
				1.通过控制类样式属性对盒子显示隐藏
				if (isShow) {
					$('.box').css('display','none');
					isShow = false;
					$(this).text('显示');
				}else{
					$('.box').css('display','block');
					isShow = true;
					$(this).text('隐藏');
				}
				*/
                
				// 2.通过控制类名  addClass() removeClass()
				// 谨记：如果是操作类名  一定要使用addClass 和removeClass 不要使用attr()
				if (isShow) {
					// className +=' hidden'
					$('.box').addClass('hidden active yyy uuu ooo ppp');
					isShow = false;
					$(this).text('显示');
				}else{
					$('.box').removeClass('hidden yyy uuu ooo ppp');
					isShow = true;
					$(this).toggleClass('addr');
					$(this).text('隐藏');
				}
			})
		});
	</script>
</body>
</html>
```

#### 1.4 值操作

**html()：**html() 是获取选中标签元素中所有的内容

语法：

```javascript
$('#box').html();
```

设置值：设置该元素的所有内容，会替换掉，标签中原来的内容。

```javascript
$('#box').html('<a href="https://www.baidu.com">百度一下</a>');
```

**text()：**获取匹配元素包含的文本内容

语法：

```javascript
$('#box').text();
```

设置值：设置该所有的文本内容

```javascript
$('#box').text('<a href="https://www.baidu.com">百度一下</a>');
```

**注意：值为标签的时候，不会被渲染为标签元素，只会被当做值渲染到浏览器中。**

**val()：**用于表单控件中获取值，比如input textarea select等等

设置值：

```javascript
$('input').val('设置了表单控件中的值')；
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
	<p id="box">
		wuSir
	</p>
	<div class="box">
		外边
		<span>里边</span>
	</div>
	<input type="text" value="123">
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 只获取文本的内容  text() innerText
			// trim()清除前后的空格
			console.log($('#box').text().trim());

			// 设置文本的内容
			$('#box').text('<h2> 武sir  </h2>');

			// 获取标签和文本的内容 html() innerHTML
			console.log($('.box').html().trim());

			// 设置
			$('.box').html('<a href="https://www.baidu.com">百度一下</a>');

			// 获取表单input中的值
			console.log($('input').val());

			// 清空input输入框中的内容
			$('input').val('');
        
			// 设置input输入框中的内容
			$('input').val('哈哈哈哈');
		});
	</script>
</body>
</html>
```

