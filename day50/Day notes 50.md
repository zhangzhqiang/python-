# Day notes 50

## 今日内容

- jQuery位置信息
- jQuery事件
- jQuery的Ajax

### 1. jQuery位置信息

#### 1.宽度和高度

**获取宽度：**

```
.width()
```

描述：为匹配的元素集合中获取第一个元素的当前计算宽度值。这个方法不接受任何参数。

`.css(width)` 和 `.width()`之间的区别是后者返回一个没有单位的数值（例如，`400`），前者是返回带有完整单位的字符串（例如，`400px`）。当一个元素的宽度需要数学计算的时候推荐使用`.width()` 方法 。

**设置宽度：**

```
.width( value )
```

描述：给每个匹配的元素设置CSS宽度。

**获取高度：**

```
.height()
```

描述：获取匹配元素集合中的第一个元素的当前计算高度值。

- 这个方法不接受任何参数。

**设置高度：**

```
 .height( value )
```

描述：设置每一个匹配元素的高度值。

#### 2.内部宽和内部高

**获取内部宽：**

```
.innerWidth()
```

描述：为匹配的元素集合中获取第一个元素的当前计算宽度值,包括padding，但是不包括border。

ps:这个方法不适用于`window` 和 `document`对象，对于这些对象可以使用`.width()`代替。

**设置内部宽：**

```
.innerWidth(value);
```

描述： 为匹配集合中的每个元素设置CSS内部宽度。如果这个“value”参数提供一个数字，jQuery会自动加上像素单位（px）。

**获取内部高：**

```
.innerHeight();
```

描述：为匹配的元素集合中获取第一个元素的当前计算高度值,包括padding，但是不包括border。

ps:这个方法不适用于`window` 和 `document`对象，对于这些对象可以使用`.height()`代替。

**设置内部宽：**

```
.innerHeight(value);
```

描述： 为匹配集合中的每个元素设置CSS内部高度。如果这个“value”参数提供一个数字，jQuery会自动加上像素单位（px）。

#### 3.外部宽和外部高

**获取外部宽：**

```
 .outerWidth( [includeMargin ] )
```

描述：获取匹配元素集合中第一个元素的当前计算外部宽度（包括padding，border和可选的margin）

- includeMargin (默认: `false`)

    类型： `Boolean`

    一个布尔值，表明是否在计算时包含元素的margin值。

- 这个方法不适用于`window` 和 `document`对象，可以使用`.width()`代替

**设置外部宽：**

```
 .outerWidth( value )
```

描述： 为匹配集合中的每个元素设置CSS外部宽度。

**获取外部高：**

```
 .outerHeight( [includeMargin ] )
```

描述：获取匹配元素集合中第一个元素的当前计算外部高度（包括padding，border和可选的margin）

- includeMargin (默认: `false`)

    类型： `Boolean`

    一个布尔值，表明是否在计算时包含元素的margin值。

- 这个方法不适用于`window` 和 `document`对象，可以使用`.width()`代替

**设置外部高：**

```
 .outerHeight( value )
```

描述： 为匹配集合中的每个元素设置CSS外部高度。

### 2. jQuery事件

HTML中与JavaScript交互是通过事件驱动来实现的，例如鼠标点击事件、页面的滚动事件onscroll等等，可以向文档或者文档中的元素添加事件监听器来预订事件。想要知道这些事件是在什么时候进行调用的，就需要了解一下“事件流”的概念。

#### 2.1 事件流的概念

事件流描述的是从页面中接收事件的顺序，以流的顺序执行。

1.DOM事件流

“DOM2级事件”规定的事件流包括三个阶段：

1. 事件捕获阶段；

2. 处于目标阶段；

2. 事件冒泡阶段；

```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title></title>
</head>

<body>
    <button id='btn'>按钮</button>
    <script type="text/javascript">
    var oBtn = document.getElementById('btn')
    // oBtn.onclick = function(){
    // 	alert(1);
    // };
    // 如果是true 则表示有捕获
    oBtn.addEventListener('click', function() {
        console.log('按钮处于捕获阶段');
        alert(1);
    }, true)
    document.body.addEventListener('click', function() {
        console.log('body处于捕获阶段');
    }, true)
    document.documentElement.addEventListener('click', function() {
        console.log('html处于捕获阶段');
    }, true)
    document.addEventListener('click', function() {
        console.log('文档处于捕获阶段');
    }, true)
     oBtn.addEventListener('click', function() {
        console.log('按钮处于冒泡阶段');
    }, false)
    document.body.addEventListener('click', function() {
        console.log('body处于冒泡阶段');
    }, false)
    document.documentElement.addEventListener('click', function() {
        console.log('html处于冒泡阶段');
    }, false)
    document.addEventListener('click', function() {
        console.log('文档处于冒泡阶段');
    }, false)
    </script>
</body>
</html>

/*打印结果：
文档处于捕获阶段
27-原生js的事件流.html:25 html处于捕获阶段
27-原生js的事件流.html:22 body处于捕获阶段
27-原生js的事件流.html:18 按钮处于捕获阶段
27-原生js的事件流.html:31 按钮处于冒泡阶段
27-原生js的事件流.html:34 body处于冒泡阶段
27-原生js的事件流.html:37 html处于冒泡阶段
27-原生js的事件流.html:40 文档处于冒泡阶段
*/
```

解释：

1、addEventListener：

addEventListener 是DOM2 级事件新增的指定事件处理程序的操作，这个方法接收3个参数：

- 要处理的事件名
- 作为事件处理程序的函数
- 一个布尔值
    - 最后这个布尔值参数如果是true，表示在捕获阶段调用事件处理程序；如果是false，表示在冒泡阶段调用事件处理程序。

2、document、documentElement和document.body三者之间的关系：

- document代表的是整个html页面；

- document.documentElement代表的是`<html>`标签；

- document.body代表的是`<body>`标签；

执行过程：

首先在事件捕获过程中，document对象首先接收到click事件，然后事件沿着DOM树依次向下，一层一层向下传播，直到找到事件的实际目标。也就是示例中的`btn`。

接着在事件冒泡过程中，事件开始时由最具体的元素（button标签）接收，然后逐级向上传播到较为不具体的节点鼻祖（document）。

需要注意的点：由于老版本的浏览器不支持事件捕获，因此在实际开发中需要使用事件冒泡，在由特殊需要时再使用事件捕获

补充知识了解即可：

1、IE中的事件流只支持“事件冒泡”，但是版本到了IE9+以后，实现了“DOM2级事件”，也就是说IE9+以后也可以在捕获阶段对元素进行相应的操作。

2、在DOM事件流中，实际的目标在“捕获阶段”不会接收到事件。而是在“处于目标阶段”被触发，并在事件处理中被看成“冒泡阶段”的一部分。然后，“冒泡阶段”发生，事件又传播回文档。

事件冒泡处理：event.stopPropagation();

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
	<style type="text/css">
		.father{
			width: 300px;
			height: 300px;
			background-color: red;
		}

	</style>
</head>
<body>
	<div class="father">
		<button>按钮</button>
		<a href="http://www.baidu.com">百度一下</a>
	</div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){

			// 给按钮绑定事件
			// 在所有的事件回调函数中 都会有默认的事件对象
			$('.father button').click(function(event){
				// 原生js的事件对象
				console.log(event);
				alert($(this).text());
				// 阻止事件冒泡
				event.stopPropagation();

			});

			$('a').click(function(e){
				// e.preventDefault();
				// e.stopPropagation();
				alert('a被点击了');
				// 相当于 e.preventDefault() 和 e.stopPropagation();
				return false;
			});

			$('.father').click(function(event){
				console.log(event);
				// alert('父亲被点击了');
				event.stopPropagation();
				// console.log('哈哈哈哈哈');

				// 既阻止了默认事件 又阻止了冒泡
				// return false;
			});
			
			$('body').click(function(e){
				console.log(e);
				e.stopPropagation();
				alert('body被点击了');
			})
		});
	</script>
</body>
</html>
```

#### 2.2 jQery常用事件

鼠标事件：

- click()：鼠标单击触发事件
- dbclick()：鼠标双击触发事件
- mousedown()：鼠标按下触发事件
- mouseup()：鼠标弹起触发事件
- mousemove()：鼠标移动触发事件
- mouseover()：鼠标移入触发事件
- mouseout()：鼠标移出触发事件
    - 移入和移出是指被选元素或当前元素的子元素
- mouseenter()：鼠标进入触发事件
- nouseleave()：鼠标离开触发事件
    - 进入和离开是指被选元素，不包括子元素
- focus()：鼠标聚焦触发事件
- blur()：失去焦点触发事件
- keydown()：键盘按下触发事件
- keyup：键盘弹起触发事件

表单事件：

- change()：表单元素发生改变的时候触发事件
    - 此事件仅限于input、textarea、select元素
- select()：文本元素发生改变的时候触发事件
    - 此事件仅限于input、type类型为text和textarea表单元素
- submit()：表单元素发生改变的时候触发事件

示例：鼠标移入和进入事件

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
	<style type="text/css">
		.father{
			width: 200px;
			height: 200px;
			background-color:red;
		}
		.child{
			width: 50px;
			height: 50px;
			background-color: green;
		}
	</style>
</head>
<body>
	<div class="father">
		<p class="child">
			alex
		</p>
	</div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		
		$(function(){
			// 鼠标穿过被选元素和被选元素的子元素 会触发此事件
			// $('.father').mouseover(function(event) {
			// 	console.log('移入了');
			// });
			// $('.father').mouseout(function(event) {
			// 	console.log('移出了');
			// });
			// 鼠标只穿过被选元素会触发此事件
			$('.father').mouseenter(function(event) {
				console.log('进入了');
			});
			$('.father').mouseleave(function(event) {
				console.log('离开了');
			});
		});
	</script>
</body>
</html>
```

示例：鼠标单击双击事件

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<button>按钮</button>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 两次 单击中间的时间差是300毫秒 ，如果小于300毫秒 表示双击
			// 遇到的问题：是双击  调用了两次单击
			var timer = null;
			var count  = 0;
			// 解决这个单双击冲突问题
			$('button').click(function(event) {
				// console.log(1);
				console.log(timer);
				// 取消第一次延时未执行的 方法
				clearTimeout(timer);
				// 如果是双击事件 要阻止 两次单击事件的调用 
				timer = setTimeout(function(){
					count++;
					// console.log(count);
					// console.log('单击了');
				},300)
			});
			$('button').dblclick(function(event) {
				// 取消的是第二次延时未执行方法
				console.log(timer);
				clearTimeout(timer);
				console.log('双击了');
			});
		});
	</script>
</body>
</html>
```

示例：鼠标焦点与键盘按下事件

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<input type="text" name="user">
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		
		$(function(){
			// 加载页面时 让输入框 获得焦点
			$('input[type=text]').focus();

			setTimeout(function(){
				$('input[type=text]').blur();
			},2000)

			$('input[type=text]').focus(function(){
				console.log('获取焦点');
			});
			$('input[type=text]').blur(function(){
				console.log('失去焦点');
			});

			// 键盘按键事件 
			$('input').keyup(function(e){
				console.log(e.keyCode);
				// 键码
				switch (e.keyCode) {
					case 13:
						console.log('回车键调用了');
						console.log($(this).val());
						// 未来与后端进行交互
						break;
					case 27:
						console.log('回车键调用了');
						console.log($(this).val());
						// 未来与后端进行交互
						break;
					default:
						// statements_def
						break;
				}
			})
		});
	</script>
</body>
</html>
```

示例：表单事件

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<form action="http://www.baidu.com/s" method="get">
		<input type="text" name="wd">
		<input type="submit">
	</form>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		
		$(function(){
			// 文本选中的时候会调用
			$('input[type=text]').select(function(){
				console.log('内容选中了');
			});
			// 原生js的onsubmit事件
			$('form').submit(function(e){
				e.preventDefault();
				// 未来 自己去发请求  往百度发请求 ajax技术
				console.log('form被submit了');
			});
			$('input[type=text]').change(function(){
				console.log('内容被修改了');
			})
		});
	</script>
</body>
</html>
```

#### 2.3 事件委托

通俗的讲，事件就是onclick，onmouseover，onmouseout，等就是事件，委托就是让别人来做，这个事件本来是加在某些元素上的，然而你却加到别人身上来做，完成这个事件。

举例：比如卖房子会委托中介，客户只要把房子信息告诉中介就可了。

**原理：**

- 利用冒泡的原理，把事件加到父级上，触发执行效果。

 **作用：**

- 性能要好
- 针对新创建的元素，直接可以拥有事件

**事件源 :**

- 跟this作用一样(他不用看指向问题，谁操作的就是谁),event对象下的

**使用情景：**

- 为DOM中的很多元素绑定相同事件；
- 为DOM中尚不存在的元素绑定事件； 

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
	    <li class="item">wusir</li>
	</ul>
	<button>添加</button>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			/*
			$('ul>li').click(function(){
				alert($(this).text());
			});
			*/	

			// 2.再执行这段代码
			// 事件委托  （看时机  如果是未来追加的元素 建议使用 事件委托来绑定事件）
			// 原理： 利用冒泡的原理，把事件加到父级上，触发执行效果。
			$('ul').on('click','li',function(e){
				alert($(this).text());
			});

			// 1.先执行这段代码：
			// 未来 动态的 往ul中追加了li标签
			// 未来追加的li标签 自己完成不了click事件，那么这个时候考虑“事件委托(代理)”
			$('button').click(function(event) {
				$('ul').append('<li>黑gril</li>')
			});

		});
	</script>
</body>
</html>
```

### 3.jQuery的Ajax

AJAX = 异步的javascript和XML（Asynchronous Javascript and XML）

简言之，在不重载整个网页的情况下，AJAX通过后台加载数据，并在网页上进行显示。

通过 jQuery AJAX 方法，您能够使用 HTTP Get 和 HTTP Post 从远程服务器上请求文本、HTML、XML 或 JSON - 同时您能够把这些外部数据直接载入网页的被选元素中。

**jquery的$.ajax()方法**：

```js
/*
jquery的$.ajax()方法 是做ajax技术经常使用的一个方法。

它的参数很多，总会有一些初学者记不住，在这里，演示几个经常使用的参数。后面讲django会详细讲ajax技术的原理。大家先把每个参数做个笔记。
参数如下： 

1.url: 要求为String类型的参数，（默认为当前页地址）发送请求的地址。

2.type: 要求为String类型的参数，请求方式（post或get）默认为get。注意其他http请求方法，例如put和delete也可以使用，但仅部分浏览器支持。

3.timeout: 要求为Number类型的参数，设置请求超时时间（毫秒）。此设置将覆盖$.ajaxSetup()方法的全局设置。

4.async: 要求为Boolean类型的参数，默认设置为true，所有请求均为异步请求。如果需要发送同步请求，请将此选项设置为false。注意，同步请求将锁住浏览器，用户其他操作必须等待请求完成才可以执行。

5.cache: 要求为Boolean类型的参数，默认为true（当dataType为script时，默认为false），设置为false将不会从浏览器缓存中加载请求信息。

6.data: 要求为Object或String类型的参数，发送到服务器的数据。如果已经不是字符串，将自动转换为字符串格式。get请求中将附加在url后。防止这种自动转换，可以查看　　processData选项。对象必须为key/value格式，例如{foo1:"bar1",foo2:"bar2"}转换为&foo1=bar1&foo2=bar2。如果是数组，JQuery将自动为不同值对应同一个名称。例如{foo:["bar1","bar2"]}转换为&foo=bar1&foo=bar2。

7.dataType: 要求为String类型的参数，预期服务器返回的数据类型。如果不指定，JQuery将自动根据http包mime信息返回responseXML或responseText，并作为回调函数参数传递。可用的类型如下：

 

　　xml：返回XML文档，可用JQuery处理。

　　html：返回纯文本HTML信息；包含的script标签会在插入DOM时执行。

　　script：返回纯文本JavaScript代码。不会自动缓存结果。除非设置了cache参数。注意在远程请求时（不在同一个域下），所有post请求都将转为get请求。

　　json：返回JSON数据。

　   jsonp：JSONP格式。使用SONP形式调用函数时，例如myurl?callback=?，JQuery将自动替换后一个“?”为正确的函数名，以执行回调函数。

　　text：返回纯文本字符串。

8.beforeSend： 要求为Function类型的参数，发送请求前可以修改XMLHttpRequest对象的函数，例如添加自定义HTTP头。在beforeSend中如果返回false可以取消本次ajax请求。XMLHttpRequest对象是惟一的参数。 function(XMLHttpRequest){ this; //调用本次ajax请求时传递的options参数 } 9.complete：

要求为Function类型的参数，请求完成后调用的回调函数（请求成功或失败时均调用）。参数：XMLHttpRequest对象和一个描述成功请求类型的字符串。 function(XMLHttpRequest, textStatus){ this; //调用本次ajax请求时传递的options参数 }

10.success：

　　要求为Function类型的参数，请求成功后调用的回调函数，有两个参数。

　　(1)由服务器返回，并根据dataType参数进行处理后的数据。

　　(2)描述状态的字符串。 function(data, textStatus){ //data可能是xmlDoc、jsonObj、html、text等等 

11.error: 要求为Function类型的参数，请求失败时被调用的函数。该函数有3个参数，即XMLHttpRequest对象、错误信息、捕获的错误对象(可选)。ajax事件函数如下： function(XMLHttpRequest, textStatus, errorThrown){ //通常情况下textStatus和errorThrown只有其中一个包含信息 this; //调用本次ajax请求时传递的options参数 }

12.contentType： 要求为String类型的参数，当发送信息至服务器时，内容编码类型默认为"application/x-www-form-urlencoded"。该默认值适合大多数应用场合。

13.dataFilter： 要求为Function类型的参数，给Ajax返回的原始数据进行预处理的函数。提供data和type两个参数。data是Ajax返回的原始数据，type是调用jQuery.ajax时提供的dataType参数。函数返回的值将由jQuery进一步处理。 function(data, type){ //返回处理后的数据 return data; }

14.dataFilter： 要求为Function类型的参数，给Ajax返回的原始数据进行预处理的函数。提供data和type两个参数。data是Ajax返回的原始数据，type是调用jQuery.ajax时提供的dataType参数。函数返回的值将由jQuery进一步处理。 function(data, type){ //返回处理后的数据 return data; }

15.global： 要求为Boolean类型的参数，默认为true。表示是否触发全局ajax事件。设置为false将不会触发全局ajax事件，ajaxStart或ajaxStop可用于控制各种ajax事件。

16.ifModified： 要求为Boolean类型的参数，默认为false。仅在服务器数据改变时获取新数据。服务器数据改变判断的依据是Last-Modified头信息。默认值是false，即忽略头信息。

17.jsonp： 要求为String类型的参数，在一个jsonp请求中重写回调函数的名字。该值用来替代在"callback=?"这种GET或POST请求中URL参数里的"callback"部分，例如{jsonp:'onJsonPLoad'}会导致将"onJsonPLoad=?"传给服务器。

18.username： 要求为String类型的参数，用于响应HTTP访问认证请求的用户名。

19.password： 要求为String类型的参数，用于响应HTTP访问认证请求的密码。

20.processData： 要求为Boolean类型的参数，默认为true。默认情况下，发送的数据将被转换为对象（从技术角度来讲并非字符串）以配合默认内容类型"application/x-www-form-urlencoded"。如果要发送DOM树信息或者其他不希望转换的信息，请设置为false。

21.scriptCharset： 要求为String类型的参数，只有当请求时dataType为"jsonp"或者"script"，并且type是GET时才会用于强制修改字符集(charset)。通常在本地和远程的内容编码不同时使用
*/
```

示例：这个是需要与后台交互的，后台必须启动才能有效果

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<form >
		<input type="text" name="user">
		<input type="submit" name="">
	</form>
	<!-- <div class="box"></div> -->
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){

			$('form').submit(function(e){
				// 阻止form表单的默认事件
				e.preventDefault();
				var userVal = $('input[name=user]').val();
				console.log(userVal);
				
				// 与你后端交互
				$.ajax({
					url:"http://localhost:8800/create",
					type:'post',
					data:{
						"name":userVal
					},
					success:function(data){
						console.log(data);
					},
					error:function(err){
						console.log(err);
					}
				})
			})
		})
	</script>
</body>
</html>
```

和风天气请求示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div class="tmp"></div>
	<div class="city"></div>
	<img src="" alt="">
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			$.ajax({
				url:'https://free-api.heweather.com/s6/weather/now?location=beijing&key=4693ff5ea653469f8bb0c29638035976',
				type:"get",
				success:function (data) {
					console.log(data.HeWeather6[0].now.tmp);
					// 温度
					var tmp = data.HeWeather6[0].now.tmp;
					// 城市
					var city = data.HeWeather6[0].basic.location;
					// 天气状况码
					var cond_code= data.HeWeather6[0].now.cond_code;

					// 后面方法的参数使用的是es6的模板字符串拼接的变量
					$('.tmp').text(`${tmp}℃`);
					$('.city').text(city);
					// 后面的地址是使用的和风天气的天气状况cdn资源。您也可以使用本地图片加载
					$('img').attr('src',`https://cdn.heweather.com/cond_icon/${cond_code}.png`);
				}
			})
		});
	</script>
</body>
</html>
```

