# Day notes 38

## 今日内容

### CSS属性－2

#### 块级元素和行内元素的分类：

在HTML中，将标签分为文本级和容器级两类标签。

从HTML看标签分为：

- 文本级标签：a，span，p，br，i，u，em，strong，label
- 容器级标签：div，h系列，ol，ul，table，form，li，dt，dd

备注：为什么说p时文本级标签呢？因为p里面只能放文字，图片，表单元素，p里面不能放h和ul，p里面也不能放p标签。

从CSS看标签标签分类：

- 行内元素：除了p之外，所有的文本级标签，都是行内元素。p是个文本级，但是是个块级元素。

- 块级元素：所有的容器级标签都是块级元素，还有p标签。

行内元素/块级元素/行内块元素的区别：

行内元素：

- 与其他行内元素在一行显示

- 不能设置宽高。默认的宽高，就时文字的宽高

  ```html
  <!DOCTYPE html>
  <html>
  <head>
  	<title></title>
  	<style type="text/css">
  		a,span{
  			background-color: purple;
  			font-size: 30px;
  			width: 300px;
  			height: 300px;
  		}
  	</style>
  </head>
  <body>
   	<a href="#">百度一下</a>
  	<span>小圆圈</span>
  	<strong>粗的</strong>
  	<em>斜体</em>		
  </body>
  </html>
  ```

块级元素：

- 独占一行，不能与其它任何元素在一行显示

- 可以设置宽高。如果不设置宽，那么宽度默认为父亲的宽

  ```html
  <!DOCTYPE html>
  <html>
  <head>
  	<title></title>
  	<style type="text/css">
  		div{
  			background-color: green;
  			width: 200px;
  			height: 200px;
  		}
  		p{
  			background-color: red;
  		}
  	</style>
  </head>
  <body>
   	<div>MJJ</div>
  	<p>我是一个段落</p>
  	<h1>段落</h1>
  	<ul>
  		<li>小米商城</li>
  	</ul>	
  </body>
  </html>
  ```

行内块元素：

- 在一行内显示

- 可以设置宽高

  ```html
  <!DOCTYPE html>
  <html>
  <head>
  	<title></title>
  	<style type="text/css">
  		input{
  			width: 200px;
  			height: 200px;
  		}
  		img{
  			width: 200px;
  		}
  	</style>
  </head>
  <body>
   	<input type="" name="username">
  	<input type="" name="pswd">
  	<img src="./img/1.png">
  	<img src="./img/1.png">
  </body>
  </html>
  ```

块级元素和行内元素的互相转换：

我们可以通过`display`属性将块级元素和行内元素进行相互转换。display即“显示模式”。

##### 行内元素转换为块级元素：

```html
<!DOCTYPE html>
<html>
<head>
	<title>display属性</title>
	<style type="text/css">
		span,a{
			display: block;
			background-color: green;
			width: 100px;
			/*height: 40px;*/
			/*text-align: center;水平居中
			line-height:控制文本垂直居中*/
			text-align: center;
			line-height: 40px;
		}
	</style>
</head>
<body>
	<span>我是行内元素</span>
	<a href="#">点我一下试试</a>
</body>
</html>
```

一旦给一个行内元素设置`display:block`那么这个标签立即成为块级标签，此时它和一个div没有区别，block是“块”的意思，也就是说：

- 此时这个span，a标签能够设置宽度、高度
- 此时这个span独占一行，别人无法和他一排显示
- 如果不设置宽度，默认为父亲的宽

##### 块级元素可以转换为行内元素：

```html
<!DOCTYPE html>
<html>
<head>
	<title>display属性</title>
	<style type="text/css">
		div{
			background-color: red;
			width: 200px;
			height: 200px;
			/*块级转行内 none为隐藏*/
			display: inline;
		}
	</style>
</head>
<body>
	<div>我是一个块元素</div>
</body>
</html>
```

一旦给一个块级元素设置`display:inline`那么这个标签立即成为行内标签，此时它和一个span标签没有区别，inline是“行内”的意思，也就是说：

- 此时这个div不能设置宽度、高度
- 此时这个div可以和其它标签在一行显示

#### 盒模型

在CSS中，"box model"这一术语是用来设计和布局时使用，然后在网页中基本上都会显示一些方方正正的盒子。我们称为这种盒子叫盒模型。

##### 盒模型的属性

width：内容的宽度

height: 内容的高度

padding：内边距，边框到内容的距离

border: 边框，就是指的盒子的宽度

margin：外边距，盒子边框到附近最近盒子的距离

##### padding

padding：就是内边距的意思，它是边框到内容之间的距离。

注意：padding的区域是有背景颜色的。并且背景颜色和内容的颜色一样。也就是说background-color这个属性填充所有的border以内的区域。

##### padding的设置

padding有四个方向，分别描述四个方向的padding。

1.写小属性，分别设置不同方向的padding

```html
<!DOCTYPE html>
<html>
<head>
	<title>padding的讲解</title>
	<style type="text/css">
		div{
			width: 180px;
			height: 180px;
			background-color: green;

			/*分别设置*/
			padding-top: 20px;
			padding-left: 20px;
			padding-bottom: 20px;
			padding-right: 50px;
		}
	</style>
</head>
<body>
	<!-- 内边距：盒子边框到内容的距离 -->
	<div>mjj</div>
</body>
</html>
```

2.写综合属性，用空格隔开

```html
<!DOCTYPE html>
<html>
<head>
	<title>padding的讲解</title>
	<style type="text/css">
		div{
			width: 180px;
			height: 180px;
			background-color: green;

			/*综合设置*/
			/*四个值：上 右 下 左*/
			padding: 10px 20px 30px 40px;
			/*三个值：上 右左 下*/
			padding: 20px 30px 40px;
			/*两个值：上下 左 右*/
			padding: 20px 30px;
			/*一个值：上 下 左 右*/
			padding: 20px;
		}
	</style>
</head>
<body>
	<!-- 内边距：盒子边框到内容的距离 -->
	<div>mjj</div>
</body>
</html>
```

##### 清除html默认样式

一些标签默认有padding，比如ul标签，有默认的padding－left值。

那么我们一般在做栈的时候，是要清除页面标签中默认的padding和margin。以便于我们更好的去调整元素的位置。

例如：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>清除html变迁元素的默认样式</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
</head>
<body>
	<p>我是一个段落</p>	
	<p>我是一个段落</p>
	<ul>
		<li>pop</li>
	</ul>
	<input type="text" name="">
</body>
</html>
```

CSS文件

```css
body,p,ul,ol,dl,dt{
	margin: 0;
	padding: 0;
}
ul,ol{
	list-style: none;
}
input{
	border: none;
	outline: none;
}
a{
	text-decoration: none;
}
```

我们要使用并集选择器来选中页面中应有的标签

```
https://meyerweb.com/eric/tools/css/reset/
```

##### border

border:边框的意思，描述盒子的边框

border有三个要死：粗细 线性样式 颜色

```
border:solid
```

- 如果颜色不写，默认是黑色

- 如果粗细不写，不显示边框
- 如果只写线性样式，默认的有上下左右3px的宽度，样式为实体

##### border的设置

1.按照三要素来写border

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框border</title>
	<style type="text/css">
		.border{
      width: 200px;
			height: 200px;
			/*按照三要素来编写border*/
			border-width: 4px;
			border-style: solid dotted double dashed;
			border-color: green red purple yellow;			
		}
	</style>
</head>
<body>
	<!-- 三要素：粗细width／样式style／颜色color -->
	<div class="border"></div>
	<input type="text" name="" class="username">
</body>
</html>
```

2.按照方向来写border

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框border</title>
	<style type="text/css">
		.border{
      width: 200px;
			height: 200px;
			/*按照方向来编写border*/
			border-top-width: 10px;
			border-top-color: red;
			border-top-style: solid;

			border-right-width: 10px;
			border-right-color: yellow;
			border-right-style: dotted;

			border-bottom-width: 10px;
			border-bottom-color: purple;
			border-bottom-style: double;

			border-left-width: 10px;
			border-left-color: green;
			border-left-style:dashed;			
		}
	</style>
</head>
<body>
	<!-- 三要素：粗细width／样式style／颜色color -->
	<div class="border"></div>
	<input type="text" name="" class="username">
</body>
</html>
```

按照方向的另一种方法：

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框border</title>
	<style type="text/css">
		.border{
      width: 200px;
			height: 200px;
			/*按照方向来编写border*/
			border-top: 10px solid red;
			border-right: 10px dotted yellow;
			border-bottom: 10px double purple;
			border-left: 10px dashed green;			
		}
	</style>
</head>
<body>
	<!-- 三要素：粗细width／样式style／颜色color -->
	<div class="border"></div>
	<input type="text" name="" class="username">
</body>
</html>
```

3.清除边框的默认样式

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框border</title>
	<style type="text/css">
		input{
			/*清除默认样式*/
			border: none;
			/*或者*/
			/*border: 0;*/

			/*清除外线*/
			outline: none;
		}
		.username{
			width: 180px;
			height: 40px;
			font-size: 20px;
			padding-left: 20px;
			border: 1px solid red;
		}
		.username:hover{
			border: 1px solid orange;
		}
	</style>
</head>
<body>
	<!-- 三要素：粗细width／样式style／颜色color -->
	<div class="border"></div>
	<input type="text" name="" class="username">
</body>
</html>
```

##### margin

margin：外边距的意思。表示边框到最近盒子的距离

```html
<!DOCTYPE html>
<html>
<head>
	<title>外边距 margin</title>
	<style type="text/css">
		span{
			background-color: red;
		}
		.xiongda{
			/*盒子右边移动20px*/
			margin-right: 20px;
		}
		.xionger{
			/*盒子左边移动100px*/
			margin-left: 100px;
		}
		div{
			width: 200px;
			height: 200px;
		}

		/*margin垂直方向会出现外边距合并 外边距塌陷 大的吞并小的*/
		.box1{
			background-color: red;
			/*盒子下边移动30px*/
			margin-bottom: 30px;
		}
		.box2{
			background-color: green;
			/*盒子上边移动100px*/
			margin-top: 100px;
		}
	</style>
</head>
<body>
	<!-- 外边距：一个盒子到另一个盒子的距离 -->
	<span class="xiongda">熊大</span>
	<span class="xionger">熊二</span>

	<div class="box1"></div>
	<div class="box2"></div>
</body>
</html>
```

注意：垂直方向会出现外边距塌陷。

比如：box1设置盒子向下移动30px，box2设置盒子向上移动100px，这两个盒子之间的距离是100px，覆盖了小的30px。

##### 盒模型的计算

如果一个盒子设置了padding，border，width，height，margin。

盒子的真实宽度=width+2＊padding+2＊border

盒子的真实高度=height+2＊padding+2＊border

注意：标准盒模型，width不等于盒子真实的宽度，如果要保持盒子真实的宽度，那么家padding就咬剪去width，相反减padding就一定要加width，真实高度一样设置。



