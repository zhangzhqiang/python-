# Day notes 42

## 今日内容

- 如何制作圆、圆环、半圆
- 盒子模型阴影
- 网页常见布局-单列布局
- 网页常见布局-多列布局
- 行内、块元素水平垂直居中

### 1.圆的制作

- border－radius：设置盒子模型圆角

示例：圆

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框属性</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
			/*切一个圆形*/
			border-radius: 50%;
		}
	</style>
</head>
<body>
	<div class="box"></div>
</body>
</html>
```

示例：圆环、半圆

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框属性</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 100px;
			/*切一个半圆*/
			border-top-left-radius: 100px;
			border-top-right-radius: 100px;
			border: 5px solid purple;
		}
	</style>
</head>
<body>
	<div class="box"></div>
</body>
</html>
```

### 2.盒子阴影

- box－shadow：设置当前盒子模型阴影

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>边框阴影</title>
	<style type="text/css">
		.shandow{
			position: relative;
			width: 200px;
			height: 200px;
			margin: 50px auto;
			background-color: purple;
		}
		.shandow:hover{
			top: 3px;
			/*1.水平偏移方向
			  2.垂直偏移方向
			  3.阴影的模糊程度
			  4.阴影的颜色
			  5.默认outset外设，可以设置为inset内设
			*/
			box-shadow: 0 15px 20px red;
		}
	</style>
</head>
<body>
	<div class="shandow"></div>
</body>
</html>
```

### 3.单列布局

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>网页常见布局方案－单列布局</title>
	<style type="text/css">
		*{
			margin: 0;
			height: 100%;
		}
		.header{
			width: 100%;
			height: 60px;
			line-height: 60px;
			text-align: center;
			background-color: #000;
		}
		.container{
			width: 1200px;
			margin: 0 auto;
		}
		.header .container{
			height: 60px;
			background-color: orange;
		}
		.wrap{
			width: 100%;
			height: 100%
		}
		.wrap .container{
			height: 100%;
			background-color: red;
		}
		.foot{
			width: 100%;
			height: 100%;
		}
		.foot .container{
			height: 100px;
			background-color: green;
		}
	</style>
</head>
<body>
	<!-- 头部 -->
	<div class="header">
		<div class="container">头部</div>
	</div>
	<!-- 主体内容 -->
	<div class="wrap">
		<div class="container">主体内容</div>
	</div>
	<!-- 脚部 -->
	<div class="foot">
		<div class="container">脚步</div>
	</div>
</body>
</html>
```

### 4.多列布局

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>网页常见布局方案－多列布局</title>
	<style type="text/css">
		*{
			margin: 0;
			height: 100%;
		}
		.header{
			width: 100%;
			height: 60px;
			line-height: 60px;
			text-align: center;
			background-color: #000;
		}
		.container{
			width: 1200px;
			margin: 0 auto;
		}
		.header .container{
			height: 60px;
			background-color: orange;
		}
		.wrap{
			width: 100%;
			height: 100%
		}
		.wrap .container{
			height: 100%;
		}
		.wrap .left{
			width: 10%;
			height: 100%;
			float: left;
			background-color: yellowgreen;
		}
		.wrap .right{
			width: 10%;
			height: 100%;
			float: right;
			background-color: yellow;
		}
		.wrap .center{
			height: 100%;
			background-color: purple;
			margin: 0 130px;
		}
		.foot{
			width: 100%;
			height: 100%;
		}
		.foot .container{
			height: 100px;
			background-color: green;
		}
	</style>
</head>
<body>
	<!-- 头部 -->
	<div class="header">
		<div class="container">头部</div>
	</div>
	<!-- 主体内容 -->
	<div class="wrap">
		<div class="container">
			<div class="left"></div>
			<div class="right"></div>
			<div class="center">
				主体内容
			</div>
		</div>
	</div>
	<!-- 脚部 -->
	<div class="foot">
		<div class="container">脚步</div>
	</div>
</body>
</html>
```

### 5.行内/块元素，水平垂直居中

**1.行内元素水平垂直居中**

- display: table-cell：转换成单元格形式
- vertical-align: middle：垂直方向排列设置

```html
/*方式一：水平垂直居中*/
text-align: center;
/*等于盒子模型的高度*/
/*line-height: 200px;*/

/*方式二：水平垂直居中*/
text-align: center;
/*转换成单元格形式*/
display: table-cell;
/*垂直方向-排列方式：三个值：1.top 2.middle 3.bottom */
vertical-align: middle;
```

完整代码：

```html
<!DOCTYPE html>
<html>
<head>
	<title>行内元素水平垂直居中</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
			color: #fff;

			/*方式一：水平垂直居中*/
			text-align: center;
			/*等于盒子模型的高度*/
			/*line-height: 200px;*/

			/*方式二： 转换成单元格形式*/
			display: table-cell;
			/*垂直方向-排列方式：三个值：1.top 2.middle 3.bottom */
			vertical-align: middle;
		}
		td{
			width: 100px;
			height: 100px;
			background-color: green;
			text-align: center;
			vertical-align: middle;
		}
	</style>
</head>
<body>
	<div class="box">
		ike的博客
	</div>
	<table>
		<th>
			<td>Mjj</td>
		</th>
	</table>
</body>
</html>
```

**2.块级元素水平垂直居中**

方式一：positon+margin

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>块级元素水平垂直居中</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
			position: relative;
		}
		.child{
			width: 100px;
			height: 100px;
			background-color: green;
			position: absolute;
			margin: auto;
			left: 0;
			right: 0;
			top: 0;
			bottom: 0;
		}
		td{
			width: 100px;
			height: 100px;
			background-color: orange;
			vertical-align: middle;
			text-align: center;
		}
		span{
			display: inline-block;
			width: 50px;
			height: 50px;
			background-color: red;
			line-height: 50px;
		}
	</style>
</head>
<body>
	<!-- positon+margin -->
	<div class="box">
		<div class="child"></div>
	</div>
	<table>
		<th>
			<td>
				<span>
					ABC
				</span>
			</td>
		</th>
	</table>
</body>
</html>
```

方式二：

示例：display：table-cell

```html
<!DOCTYPE html>
<html>
<head>
	<title>块级元素水平垂直居中二</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
			display: table-cell;
			vertical-align: middle;
			text-align: center;
		}
		.child{
			width: 100px;
			height: 100px;
			background-color: green;
			display: inline-block;
			line-height: 100px;
		}
		td{
			width: 100px;
			height: 100px;
			background-color: orange;
			vertical-align: middle;
			text-align: center;
		}
		span{
			display: inline-block;
			width: 50px;
			height: 50px;
			background-color: red;
			line-height: 50px;
		}
	</style>
</head>
<body>
<!-- display：table-cell -->
	<div class="box">
		<div class="child">块垂直居中</div>
	</div>
	<table>
		<th>
			<td>
				<span>
					ABC
				</span>
			</td>
		</th>
	</table>
</body>
</html>
```

方式三：

示例：只通过定位实现

```html
<!DOCTYPE html>
<html>
<head>
	<title>块级元素水平垂直居中三</title>
	<style type="text/css">
		.box{
			width: 200px;
			height: 200px;
			background-color: red;
			display: table-cell;
			vertical-align: middle;
			text-align: center;
		}
		.child{
			width: 100px;
			height: 100px;
			background-color: green;
			display: inline-block;
			line-height: 100px;
		}
		td{
			width: 100px;
			height: 100px;
			background-color: orange;
			vertical-align: middle;
			text-align: center;
		}
		span{
			display: inline-block;
			width: 50px;
			height: 50px;
			background-color: red;
			line-height: 50px;
		}
		.wrap{
			width: 200px;
			height: 200px;
			background-color: purple;
			position: relative;
		}
		.xiongda{
			width: 100px;
			height: 100px;
			background-color: yellow;
			position: absolute;
			top: 50%;
			left: 50%;
			margin-left: -50px;
			margin-top: -50px;
		}
	</style>
</head>
<body>	
	<div class="box">
		<div class="child">块垂直居中</div>
	</div>
	<table>
		<th>
			<td>
				<span>
					ABC
				</span>
			</td>
		</th>
	</table>
	<!-- 纯定位实现 -->
	<div class="wrap">
		<div class="xiongda"></div>
	</div>
</body>
</html>
```

