# Day notes 40

## 今日内容

### 1.定位

定位分为三种：

- 相对定位
- 绝对定位
- 固定定位

这三种定位，每一种都暗藏玄机，所以要挨个进行分析。

#### 相对定位

相对定位：不脱离标准文档流，可以调整元素

现象和使用：

- 如果对当前元素仅仅设置了相对定位，那么它和其它标准流的盒子没什么区别
- 设置相对定位后，才可以使用四个方向的属性： top、bottom、left、right

所以说相对定位 在页面中没有什么太大的作用。影响我们页面的布局。我们不要使用相对定位来做压盖效果。

用途：

1.微调元素位置

2.做绝对定位的参考（父相子绝）绝对定位会说到此内容。

参考点：

以原来的位置作为参考点，进行移动

```html
<!DOCTYPE html>
<html>
<head>
	<title>相对定位</title>
	<style type="text/css">
		div{
			width: 200px;
			height: 200px;
			color: #fff;
		}
		div.one{
			background-color: red;
			position: relative;
			top: 30px;
			left: 100px;
		}
		div.two{
			background-color: green;
			left: 40px;
			bottom: 50px;
		}
		div.three{
			background-color: blue;
		}
	</style>
</head>
<body>
	<!-- 相对定位：
			不脱离标准文档流，可以调整元素
		 参考点：
			以原来的位置为参考点 -->
	<div class="one">one</div>
	<div class="two">two</div>
	<div class="three">three</div>
</body>
</html>
```

#### 绝对定位

特性：

- 脱标，不在页面上占位置
- 压盖现象，层级提高，意思相当于飘起来
- 不区分行内，块级元素，都能设置宽高

参考点：

相对于最近非static(默认静态)祖先元素定位，如果没有非static祖先元素，那么以页面根元素左上角进行定位。

网站中做站，经常用到的是父相子绝，但是不仅仅是父相子绝，父绝子绝 ，父固子绝,都是以父辈元素为参考点，也就是上面所说的非static元素。

注意⚠️：父绝子绝，没有实战意义，做站的时候不会出现父绝子绝。因为绝对定位脱离标准流，影响页面的布局。相反‘父相子绝’在我们页面布局中，是常用的布局方案。因为父亲设置相对定位，不脱离标准流，子元素设置绝对定位，仅仅的是在当前父辈元素内调整该元素的位置。

绝对定位的盒子无视父辈的padding！

```html
<!DOCTYPE html>
<html>
<head>
	<title>绝对定位</title>
	<style type="text/css">
		body{
			border: 1px solid orange;
		}
		.grandfather{
			border: 1px solid purple;
			position: relative;
			top: 20px;
			left: 30px;
		}
		.father{
			border: 1px solid black;
			margin-left: 40px;
			margin-top: 20px;
			position: relative;
			top: 30px;
			left: 60px;
		}
		.one,.two,.three{
			width: 200px;
			height: 200px;
			color: #fff;
		}
		div.one{
			background-color: red;
			position: absolute;
			top: 200px;
			left: 200px;
		}
		div.two{
			background-color: green;
			width: 400px;
			/*position: absolute;*/
		}
		div.three{
			background-color: blue;
		}
	</style>
</head>
<body>
	<!-- 特点：
			1.脱离标准文档流，不在页面上占位置
			2.压盖现象，层级提高 
		 参考点：
			相对于最近非static祖先元素定位，如果没有非static祖先元素，那么以页面根元素左上角进行定位
		 网站中的：子绝父相-->
	<div class="grandfather">
		<div class="father">
			<div class="one">one</div>
			<div class="two">two</div>
			<div class="three">three</div>
		</div>
	</div>
</body>
</html>
```

#### 固定定位

固定定位：固定当前的元素不回随着页面滚动而滚动

特性：

- 脱标
- 压盖现象，层级提高
- 一旦设置固定定位，在页面中滚动网页，固定不变

参考点：

以浏览器的边角作为参考点

作用：

- 返回顶部栏
- 固定导航栏
- 页面小广告

```html
<!DOCTYPE html>
<html>
<head>
	<title>固定定位</title>
	<style type="text/css">
		.box{
			width: 100px;
			height: 100px;
			background-color: red;
			color: #fff;
		}
		#one{
			position: fixed;
			top: 80px;
			left: 20px;
		}
		.outher{
			width: 300px;
			height: 200px;
			overflow: scroll;
			padding-left: 200px;
		}
	</style>
</head>
<body>
	<div class="outher">
		<p>
			【环球时报-环球网报道 记者 张骜】香港激进示威者连日来制造事端，外媒关注到我国防部新闻发言人吴谦日前在被问及解放军应对香港目前形势发展的表态。26日，在外交部例行记者会上，有记者就美国国务卿蓬佩奥在接受媒体采访谈及中国解放军驻港部队等相关问题提问。对此，中国外交部发言人华春莹进行了驳斥
		</p>
		<p>
			华春莹说，我注意到了蓬佩奥担心驻港部队是否介入以及香港近期发生事态的一系列表态，我们之前一直强调中央政府支持特区政府依法履职，依法采取措施，维护香港的稳定、安全与繁荣。前几天我强调过，香港是中国的香港，中国绝不会允许任何外国势力插手和干预香港事务。对于现在有些外界人士对驻港部队的关切和言论，国防部新闻发言人已经就驻港部队依法履职尽职尽责做出了明确的表态。
		</p>
		<div class="box" id="one">one</div>
	</div>
</body>
</html>
```

#### 浮动和定位给行内元素带来的现象

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动和定位给行内元素带来的现象</title>
	<style type="text/css">
		span{
			/*float: left;*/
			position: fixed;
			background-color: red;
			width: 200px;
			height: 200px;
			/*
			总结：
				设置浮动，绝对定位，固定定位都可以给行内标签设置宽高
				相对定位不改变标签属性。
				不是只有通过display转换成block才能设置标签
			*/
		}
	</style>
</head>
<body>
	<span>我是行内元素</span>
</body>
</html>
```

总结：

- 设置浮动，绝对定位，固定定位都可以给行内标签设置宽高
- 相对定位不改变标签属性
- 不是只有通过display转换成块级标签才能设置标签

#### z-index

z-index非常简单，它有四大特性，每个特性你记住了，页面布局就不会出现找不到盒子的情况

- z-index 值表示层级高低，数值大的压盖住数值小的
- 只有定位了的元素，才能有z-index,也就是说，不管相对定位，绝对定位，固定定位，都可以使用z-index，而浮动元素不能使用z-index
- z-index值没有单位，就是一个正整数，默认的z-index值为0，如果都没有z-index值，或者z-index值一样，那么谁写在HTML后面，谁的层级高。定位了的元素，层级永远高于没有定位的元素
- 从父现象：父亲怂了，儿子再牛逼也没用

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>z-index的讲解</title>
	<style type="text/css">
		.a{
			position: relative;
			width: 200px;
			height: 40px;
			background-color: #C3FFFB;
			border: 3px solid #3962FE;
			z-index: 1;

		}
		.b{
			position: relative;
			width: 200px;
			height: 40px;
			background-color: #C3FFFB;
			border: 3px solid #3962FE;
			top: -30px;
			left: 50px;
			z-index: 10000;

		}
		.c{
			position: relative;
			width: 200px;
			height: 40px;
			background-color: #C3FFFB;
			border: 3px solid #3962FE;
			top: -50px;
			left: 100px;
			/*默认值为auto*/
			/*z-index: auto;*/
			z-index:10;
		}
	</style>
</head>
<body>
	<div style="position: relative;z-index: 15;">
		<div class="a">A</div>
	</div>
	
	<div style="position: relative;z-index: 10;">
		<div class="b">B</div>
	</div>
	<div class="c">C</div>
</body>
</html>
```

