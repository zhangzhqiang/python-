# Day notes 47

## 今日内容

- jQuery的选择器
- jQuery动画

### 1. jQuery基本选择器

- id选择器
    - 选择id为指定值的第一个元素
- 类选择器
    - 选择指定类名的所有元素
- 标签选择器
    - 选择指定标签名的所有元素

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        div{
            width: 100px;
            height: 100px;
            background-color: green;
            margin-top: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <button id="btn">操作</button>
    <div></div>
    <div></div>
    <div class="content"></div>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            // 获取dom元素
            var oBtn = $('#btn'); // 根据标id获取元素
            var oDiv = $('div'); // 根据标签名获取元素
            var oCls = $('.content');// 根据类名获取元素
            oBtn.click(function(){
                oDiv.show(3000);// 显示盒子
                oDiv.html('赵云'); // 设置内容
                oCls.html('马云');
            });
        })
    </script>
</body>
</html>
```

### 2. 层级选择器

- 后代选择器
    - 选择指定元素的后代元素
    - 符号为：空格
- 子代选择器
    - 选择指定元素的直接子元素
    - 符号为：>
- 紧邻选择器
    - 选择紧挨着的下一个元素
    - 符号为：+
- 兄弟选择器
    - 选择后面所有的兄弟元素
    - 符号为：~

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<ul class="lists">
		<li>
			方圆
			<ol>
			    <li>童文杰</li>
			</ol>
		</li>
		<li class="item">
			<a href="#">乔卫东</a>
		</li>
		<li class="item2">宋倩</li>
		<li>方一凡</li>
		<li>林磊儿</li>
		<li>乔英子</li>
	</ul>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 后代选择器  修改样式属性
			$('.lists li').css('color','green');
			// 子代选择器 所有指定儿子级别的元素
			$('.item > a').css({
				'color':'yellow',
				'background-color':'red'
			});
			// 紧邻选择器  只选中挨着最近的兄弟
			$('.item + li').css('color','pink');

			// 兄弟选择器  类名后的所有兄弟
			$('.item2~li').css('color','blue');
		});
	</script>
</body>
</html>
```

### 3. 基本过滤器

- :eq(index);
    - 选择索引index的元素
- :gt(index);
    - 选择索引大于index的元素
- :lt(index);
    - 选择索引小于index的元素
- odd
    - 选择索引为奇数的元素
- even
    - 选择索引为偶数的元素
- first
    - 选择第一个匹配的元素
- last
    - 选择最后一个匹配的元素

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<ul>
	    <li>1</li>
	    <li>2</li>
	    <li>3</li>
	    <li>4</li>
	</ul>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 1.:eq(index) 选择索引为index的元素
			$('ul li:eq(0)').css('background','red');
			// 2.:gt(index) 选择索引大于index的元素
			$('ul li:gt(0)').css('color','green');
			// 3.:lt(index) 选择索引小于index的元素
			$('ul li:lt(3)').css('color','yellow');
			// 4.odd 选择索引为奇数的元素
			$('ul li:odd').css('background','black');
			// 5.even 选择索引为偶数的元素
			$('ul li:even').css('background','green');
			// 6.first 选取第一个元素
			$('ul li:first').css('background','red');
			// 7.last 选择最后一个元素
			$('ul li:last').css('background','red');
		});
	</script>
</body>
</html>
```

### 4. 属性选择器

- $('li[id]')
    - 选择id标签包含id属性的元素
- $('li[class=what]')
    - 选择li标签class属性值为what的元素

- $('li[class!=what]')
    - 选择li标签class属性值不为what的元素
- $('input[name^=user]')
    - 选择input标签name属性值为user开头的元素
- $('input[name$=222]')
    - 选择input标签name属性值为222结尾的元素
- $('button[class*=btn]')
    - 选择button标签class属性值包含btn的元素
- `$('input[name][name=lastname]')`
    - 选择input标签name属性并且属性值为lastname的元素

示例：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
         <div id="box">
            <h2 class="title">属性元素器</h2>
            <!--<p class="p1">我是一个段落</p>-->
            <ul>
                <li id="li1">第一个li标签</li>
                <li class="what" id="li2">第二个li标签</li>
                <li class="what">第三个li标签</li>
                <li class="heihei">第四个li标签</li>
            </ul>
            <form action="" method="post">
            	<span>
            		<input name="username" type='text' value="1" checked="checked" />
            	</span>
                
                <span>
                	<input name="username1111" type='text' value="2" />
                </span>
                <input name="username2222" type='text' value="3" />
                <input name="username3333" type='text' value="4" />
                <button class="btn-default">按钮1</button>
                <button class="btn-info">按钮2</button>
                <button class="btn-success">按钮3</button>
                <button class="btn-danger">按钮4</button>
                <input type="text" name="lastname">
            </form>
        </div>
    </body>
    <script src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(function(){
            //标签名[属性名] 查找所有含有id属性的该标签名的元素
            $('li[id]').css('color','red');
            //匹配给定的属性是what值得元素
            $('li[class=what]').css('font-size','30px');
            //[attr!=value] 匹配所有不含有指定的属性，或者属性不等于特定值的元素
            $('li[class!=what]').css('font-size','50px');
            //匹配给定的属性是以某些值开始的元素
            $('input[name^=username]').css('background','gray');
            //匹配给定的属性是以某些值结尾的元素
            $('input[name$=222]').css('background','greenyellow');
            //匹配给定的属性是以包含某些值的元素
            $('button[class*=btn]').css('background','red');
            // 匹配指定的属性都符合的元素
            $('input[name][name=lastname]').css('background','yellow');
        })
    </script>
</html>
```

### 5. 筛选选择器

- find
    - 查找指定元素的所有后代元素，相当于所有子孙后代
- children
    - 查找指定元素的直接子元素，相当于亲生儿子元素
- sibligs
    - 查找所有兄弟的元素，不包含自己
- parent
    - 查找父元素

示例：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <div id="box">
            <p class="p1">
                <span>我是第一个span标签</span>
                <span>我是第二个span标签</span>
                <span>我是第三个span标签</span>
            </p>
            <button>按钮</button>
        </div>
        <ul>
            <li class="list">2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
        </ul>
    </body>
    <script src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        //获取第n个元素 数值从0开始
        $('span').eq(1).css('color','blue');

        //获取第一个元素 :first :last    点语法  ：get方法 和set方法
        $('span').last().css('color','greenyellow');
        $('span').first().css('color','greenyellow');

        //查找span标签的父元素（亲的）
   $('span').parent('.p1').css({"width":'200px','height':'200px',"background":'red'});

        //选择所有的兄弟元素（不包括自己）
        $('.list').siblings('li').css('color','red');

        //查找所有的后代元素
        $('div').find('button').css('background','yellow');

        //不写参数代表获取所有子元素。
        $('ul').children().css("background", "green");
        $('ul').children("li").css("margin-top", 10);
    </script>
</html>
```

示例：siblings用法

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
	<style type="text/css">
		button{
			width: 100px;
			height: 40px;
		}
	</style>
</head>
<body>
	<button>按钮1</button>
	<button>按钮2</button>
	<button>按钮3</button>
	<button>按钮4</button>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		
		$(function(){
			// 内部遍历
			$('button').click(function() {
				// 选项卡
				$(this).css('background','red').siblings('button').css('background','transparent');
				console.log($(this).css('background','red'));
			});
		});
	</script>
</body>
</html>
```

### 6. jQuery动画

jQuery提供的一组网页中常见的动画效果，这些动画是标准的、有规律的效果；同时还提供给我们了自定义动画的功能。

#### 6.1 显示和隐藏

**显示动画效果：**

显示动画用show方法实现。

方式一：无参数，默认是默认是normal  400ms。其实这个方法的底层就是通过`display: block;`实现的。

```
  $("div").show();
```

方式二：通过控制元素的宽高、透明度、display属性，逐渐显示，2秒后显示完毕。

```
$('div').show(3000);
```

方式三：和方式二类似，也是通过控制元素的宽高、透明度、display属性，逐渐显示。

```
 $("div").show("slow");
```

参数可以是：

- slow 慢：600ms
- normal 正常：400ms
- fast 快：200ms

方式四：

```
 //show(毫秒值，回调函数;
    $("div").show(5000,function () {
        alert("动画执行完毕！");
    });
```

解释：动画执行完后，立即执行回调函数。

**总结：**

上面的四种方式几乎一致：参数可以有两个，第一个是动画的执行时长，第二个是动画结束后执行的回调函数。

**隐藏动画效果：**

隐藏动画用hide方法实现和show方法用法一样。

#### 6.2 显示隐藏动画

显示和隐藏的来回切换采用的是toggle()方法：就是先执行show()，再执行hide()。

```js
 $(selector).toggle(speed, callback);
```

示例：显示，隐藏，以及显示隐藏

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
			background-color:red;
			display: none;
		}
	</style>
</head>
<body>
	<button id="show">显示</button>
	<button id="hide">隐藏</button>
	<button id="toggle">开关式动画</button>
	<div class="box"></div>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			// 显示动画
			$('#show').click(function(){
				// 如果是一个按钮控制盒子显示隐藏 那么得需要去控制isShow这个变量

				// show(动画的时间，fn)   
				// 默认是normal  400ms   slow  600ms  fast 200ms
				$('.box').show('slow',function(){
					$(this).text('alex');
				});
			});
			// 隐藏
			$('#hide').click(function(){

				$('.box').hide('slow');
			});
			// 开关式的显示隐藏动画
			$('#toggle').click(function(){
				// 玩动画 就跟玩定时器一样  先关动画 再开动画
				$('.box').stop().toggle(2000);
			})
		});
	</script>
</body>
</html>
```

#### 6.4 滑入和滑出

**滑入动画效果：**（类似于生活中的卷帘门）

```
$(selector).slideDown(speed, 回调函数);
```

解释：下拉动画，显示元素。

注意：省略参数或者传入不合法的字符串，那么则使用默认值：400毫秒

**滑出动画效果：** 

```
 $(selector).slideUp(speed, 回调函数);
```

解释：上拉动画，隐藏元素。

#### 6.5 滑入滑出动画

滑入和画出的来回切换采用的是slideToggle()方法：就是先执行show()，再执行slideUp()。

```
 $(selector).slideToggle(speed, callback);
```

示例：滑入、滑出、以及滑入滑出

```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
    .box {
        width: 200px;
        height: 200px;
        background-color: red;
        display: none;
    }
    </style>
</head>

<body>
    <button id="slideDown">卷帘门下拉</button>
    <button id="slideUp">卷帘门上拉</button>
    <button id="toggleSlide">开关式动画</button>
    <div class="box"></div>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        // 滑入
        $('#slideDown').click(function() {
        		$('.box').slideDown(200);
        });
        // 滑出
        $('#slideUp').click(function() {
     		$('.box').slideUp(600);
        });
        // 开关式的显示隐藏动画
        $('#toggleSlide').click(function() {
          	$('.box').stop().slideToggle(1000);
        })
    });
    </script>
</body>
</html>
```

#### 6.5 淡入和淡出

**淡入动画效果：**让元素以淡淡的进入视线的方式展示出来

```
 $(selector).fadeIn(speed, callback);
```

**淡出动画效果：**让元素以渐渐消失的方式隐藏起来

```
$(selector).fadeOut(1000);
```

#### 6.6 淡入淡出动画

淡入淡出的来回切换采用的是fadeToggle()方法：就是先执行fadeIn()，再执行fadeOut()。

淡入淡出效果：通过改变透明度，切换匹配元素的显示或隐藏状态。

```
 $(selector).fadeToggle('fast', callback);
```

示例：淡入、淡出、以及淡入淡出

```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
    .box {
        width: 200px;
        height: 200px;
        background-color: red;
        display: none;
    }
    </style>
</head>

<body>
    <button id="fadeIn">淡入动画</button>
    <button id="fadeOut">淡出动画</button>
    <button id="fadeToggle">开关式动画</button>
    <div class="box"></div>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
    $(function() {
        // 淡入
        $('#fadeIn').click(function() {
        		$('.box').fadeIn(1000);
        });
        // 淡出
        $('#fadeOut').click(function() {
                // 第二个参数都是有回调函数
     		$('.box').fadeOut(1000);
        });
        // 开关式的淡入淡出
        $('#fadeToggle').click(function() {
          	$('.box').stop().fadeToggle(1000);
        })
    });
    </script>
</body>
</html>
```

#### 6.7 自定义动画

语法：

```
 $(selector).animate({params}, speed, callback);
```

作用：执行一组CSS属性的自定义动画。

- 第一个参数表示：要执行动画的CSS属性（必选）
- 第二个参数表示：执行动画时长（可选）
- 第三个参数表示：动画执行完后，立即执行的回调函数（可选）

示例：

```js
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
	<style type="text/css">
		div{
			width: 100px;
			height: 100px;
			background-color: red;
			position: absolute;
			bottom: 0;
			left: 0;
		}
	</style>
</head>
<body>
	<div></div>
	<button>动画吧</button>
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
				$('button').click(function(event) {
					/* Act on the event */
					// animate({队列的属性},时间,fn)
						var json = {
							width:200,
							height: 200,
							top: 200,
							left : 500,
							"border-radius":200,
						};
						var json2 = {
							width: 0,
							height: 0,
							top: 0,
							left: 2000,
						}
						$('div').stop().animate(json,2000,function(){
							$('div').stop().animate(json2,1000,function(){
								alert('已添加购物车')
							})
						});
				});
		});
	</script>
</body>
</html>
```

#### 6.8 停止动画

```
$(selector).stop(true, false);
```

**里面的两个参数，有不同的含义。**

第一个参数：

- true：后续动画不执行。
- false：后续动画会执行。

第二个参数：

- true：立即执行完成当前动画。
- false：立即停止当前动画。

PS：参数如果都不写，默认两个都是false。实际工作中，直接写stop()用的多。

**菜单下拉案例：**

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        * {
            margin: 0;
            padding: 0;
        }
        ul {
            list-style: none;
        }
        .wrap {
            width: 330px;
            height: 30px;
            margin: 100px auto 0;
            padding-left: 10px;
            background-color: pink;
        }
        .wrap li {
            background-color: green;
        }
        .wrap > ul > li {
            float: left;
            margin-right: 10px;
            position: relative;
        }
        .wrap a {
            display: block;
            height: 30px;
            width: 100px;
            text-decoration: none;
            color: #000;
            line-height: 30px;
            text-align: center;
        }
        .wrap li ul {
            position: absolute;
            top: 30px;
            display: none;
        }
    </style>
</head>
<body>
<div class="wrap">
    <ul>
        <li>
            <a href="javascript:void(0);">一级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">二级菜单2</a></li>
                <li><a href="javascript:void(0);">二级菜单3</a></li>
                <li><a href="javascript:void(0);">二级菜单4</a></li>
            </ul>
        </li>
        <li>
            <a href="javascript:void(0);">二级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">二级菜单2</a></li>
                <li><a href="javascript:void(0);">二级菜单3</a></li>
                <li><a href="javascript:void(0);">二级菜单4</a></li>
            </ul>
        </li>
        <li>
            <a href="javascript:void(0);">三级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">三级菜单2</a></li>
                <li><a href="javascript:void(0);">三级菜单3</a></li>
                <li><a href="javascript:void(0);">三级菜单4</a></li>
            </ul>
        </li>
    </ul>
</div>
  <script src="./jquery-3.3.1.js"></script>
    <script>
        //入口函数
        $(function () {
            //需求：鼠标放入一级li中，让他里面的ul显示。移开隐藏。
            var jqli = $(".wrap>ul>li");

            //绑定事件  mouseenter 鼠标进入 mouseleave  鼠标离开
            // js  onmouseover onmouseout  
            jqli.mouseenter(function () {
                $(this).children("ul").stop().slideDown(1000);
            });
            //绑定事件(移开隐藏)
            jqli.mouseleave(function () {
                $(this).children("ul").stop().slideUp(1000);
            });
        });
    </script>
</body>
</html>
```

