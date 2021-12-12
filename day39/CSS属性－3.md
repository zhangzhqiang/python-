# Day notes 39

## 今日内容

### 浮动与清除浮动

#### 标准流文档

文档元素在排版布局中，元素默认从左往右，从上往下，流式的排版布局，称这种布局为标准文档流。

##### 标准流文档下的围观现象

- 空白折叠现象
  - 多个空格会被合并成一个空格显示到浏览器页面中。img／盒子标签换行写，会发现每张图片／盒子之间有间隙，如果在一行内写img／盒子标签，就解决了这个问题，但是我们不会这样去写我们的html结构。这种现象称为空白折叠现象。
- 高矮不齐，底边对齐
  - 文字还有图片大小不一，都会让我们页面的元素出现高矮不齐的现象，但是在浏览器查看我们的页面总会发现底边对齐

- 自动换行，一行写不满，换行写
  - 如果在一行内写文字，文字过多，那么浏览器会自动换行去显示我们的文字

#### 浮动

浮动是css里面布局最多的一个属性，也是很重要的一个属性。

float：表示浮动的意思。它有四个值：

- none: 表示不浮动，默认
- left: 表示左浮动
- right：表示右浮动
- inherit：继承父元素的浮动属性

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文字环绕</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		.box1{
			width: 300px;
			height: 300px;
			background-color: red;
			float: left;
		}
		.box2{
			width: 300px;
			height: 300px;
			background-color: green;
			float: right;
		}
		span{
			width: 100px;
			height: 200px;
			float: left;
			background-color: purple;
		}
	</style>	
</head>
<body>
	<div class="box1"></div>
	<div class="box2"></div>
	<span>浮动</span>
</body>
</html>
```

我们会发现，三个元素并排显示，.box1和span因为是左浮动，紧挨在一起，这种现象贴边。.box2盒子因为右浮动，所以紧靠着右边。

浮动元素的四大特性：

- 文字环绕

```html
<!DOCTYPE html>
<html>
<head>
	<title>文字环绕</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		/*文字环绕，把图片设为浮动即可*/
		.box img{
			float: left;
		}
	</style>	
</head>
<body>
	<div class="box">
		<img src="img/title图片.png">
		<p>
			浙江人中出了一个经济学家，很了不起，他总结了浙江人的工作哲学：“宁做创业狼，不做打工狗”，当然这话说的很极端，很多打工的朋友都不乐意听，但是我们仔细想想，这位老兄的话还真有点道理呢。
			狼为了寻求自由，宁愿独立人格，自由思想，天天奔跑在大草原上，肆意的猎杀牛羊，尽可能的享受大自然提供的一切美味，吃饱后就躺在草地上，什么都不想，享受阳光和自由的空气，他们是草原的主宰，他们有的是尊严。不过当严寒来临时，他们必须学会抗拒暴风雪的寒冷，学会在厚厚的雪堆下面寻找猎物，时常忍受饥饿的痛苦，随时担心自己冻饿而死。狼的生活可谓一半是海水，一半是火焰。
			浙江人中出了一个经济学家，很了不起，他总结了浙江人的工作哲学：“宁做创业狼，不做打工狗”，当然这话说的很极端，很多打工的朋友都不乐意听，但是我们仔细想想，这位老兄的话还真有点道理呢。
			狼为了寻求自由，宁愿独立人格，自由思想，天天奔跑在大草原上，肆意的猎杀牛羊，尽可能的享受大自然提供的一切美味，吃饱后就躺在草地上，什么都不想，享受阳光和自由的空气，他们是草原的主宰，他们有的是尊严。不过当严寒来临时，他们必须学会抗拒暴风雪的寒冷，学会在厚厚的雪堆下面寻找猎物，时常忍受饥饿的痛苦，随时担心自己冻饿而死。狼的生活可谓一半是海水，一半是火焰。
			浙江人中出了一个经济学家，很了不起，他总结了浙江人的工作哲学：“宁做创业狼，不做打工狗”，当然这话说的很极端，很多打工的朋友都不乐意听，但是我们仔细想想，这位老兄的话还真有点道理呢。
			狼为了寻求自由，宁愿独立人格，自由思想，天天奔跑在大草原上，肆意的猎杀牛羊，尽可能的享受大自然提供的一切美味，吃饱后就躺在草地上，什么都不想，享受阳光和自由的空气，他们是草原的主宰，他们有的是尊严。不过当严寒来临时，他们必须学会抗拒暴风雪的寒冷，学会在厚厚的雪堆下面寻找猎物，时常忍受饥饿的痛苦，随时担心自己冻饿而死。狼的生活可谓一半是海水，一半是火焰。
		</p>
	</div>
</body>
</html>
```

现象：所谓字围效果，当div浮动，p不浮动，div遮盖住了p，div的层级提高，但是p中的文字不会被遮盖，此时就形成了字围效果。

- 脱离了标准文档流

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动的现象</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		div{
			width: 200px;
			height: 200px;
			color: #fff;
		}
		div.left{
			background-color: red;
			float: left;
		}
		div.right{
			width: 300px;
			background-color: green; 
		}
	</style>
</head>
<body>
  <body>
	<!-- 浮动的现象：
			1.文字环绕
			2.脱离了标准文档流
			3.浮动元素互相贴靠
			4.浮动元素收缩现象 -->
	 <div class="left">左边的盒子</div>
	<div class="right">右边的盒子</div>
	<div class="center">最优的盒子</div>
</body>
</html>
```

现象：红色盒子压盖住了绿色的盒子，就是红色的盒子脱离的标准流，飘到了绿色盒子的上边

总结：所有的标签一旦设置浮动，就能够并排，并且都不区分行内、块状元素，都能够设置宽高

- 浮动元素互相贴靠

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动的现象</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		div{
			width: 200px;
			height: 200px;
			color: #fff;
		}
		div.left{
			background-color: red;
			float: left;
		}
		div.right{
			background-color: green; 
			float: left;
		}
		div.center{
			background-color: orange;
			float: left;
		}
	</style>
</head>
<body>
  <body>
	<!-- 浮动的现象：
			1.文字环绕
			2.脱离了标准文档流
			3.浮动元素互相贴靠
			4.浮动元素收缩现象 -->
	 <div class="left">左边的盒子</div>
	<div class="right">右边的盒子</div>
	<div class="center">最优的盒子</div>
</body>
</html>
```

现象：如果都设置了向一个方向浮动，就会产生互相贴靠

- 浮动元素收缩现象

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动的现象</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		div{
			height: 200px;
			color: #fff;
		}
		div.left{
			background-color: red;
			float: left;
		}
		div.right{
			background-color: green; 
		}
		div.center{
			background-color: orange;
		}
	</style>
</head>
<body>
  <body>
	<!-- 浮动的现象：
			1.文字环绕
			2.脱离了标准文档流
			3.浮动元素互相贴靠
			4.浮动元素收缩现象 -->
	 <div class="left">左边的盒子</div>
	<div class="right">右边的盒子</div>
	<div class="center">最优的盒子</div>
</body>
</html>
```

收缩：一个浮动元素。如果没有设置width，那么就自动收缩为文字的宽度（这点跟行内元素很像）

注意：关于浮动，我们一定要遵循一个原则，永远不是一个盒子单独浮动，要浮动就要一起浮动。另外，有浮动，一定要清除浮动。

#### 浮动元素的破坏性

在页面布局的时候，每个结构中父元素的高度，我们一班不会设置。

在网页开发中，我们写完页面后，根据需求我们肯定会在之前写好的页面中增加或修改页面，比如：修改图片的高度，增加一点内容，如果我们每一个地方去增加或修改必定会影响我们的开发效率。

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动元素的破坏性与清除</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		.father{
			/*子元素浮动 父盒子一般不设置高度*/
      /*出现这种问题，我们要清除浮动带来影响*/
			border: 1px solid red;
		}
		.child1{
			width: 200px;
			height: 100px;
			background-color: green;
			float: left;
		}
		.child2{
			width: 200px;
			height: 100px;
			background-color: orange;
			float: right;
		}
		.header{
			width: 100%;
			height: 100px;
			background-color: purple;
		}
	</style>
</head>
<body>
	<div class="father clearfix">
		<div class="child1">儿子</div>
		<div class="child2">二儿子</div>
	</div>
	<div class="header"></div>
</body>
</html>
```

现象：如果不给父盒子设置一个高度，那么浮动子元素是不会填充父盒子的高度，那么`header`的盒子会覆盖到第一个盒子的位置上，影响页面布局。

浮动元素确实能实现页面元素并排的效果，这是它的好处，同时它还带来了页面布局极大的错乱，要清除浮动。

常用的清除浮动的方法：

- 给父盒子设置高度

  - 缺点：使用不灵活，后期不易维护
  - 应用：网页中盒子固定高度区域，比如固定导航栏

  示例：html文件

  ```html
  <!DOCTYPE html>
  <html>
  <head>
  	<title>浮动元素的破坏性与清除</title>
  	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
  	<style type="text/css">
  		.father{
        /*给第一个父盒子设置一个高度*/
     		height: 100px;
  			border: 1px solid red;
  		}
  		.child1{
  			width: 200px;
  			height: 100px;
  			background-color: green;
  			float: left;
  		}
  		.child2{
  			width: 200px;
  			height: 100px;
  			background-color: orange;
  			float: right;
  		}
  		.header{
  			width: 100%;
  			height: 100px;
  			background-color: purple;
  		}
  	</style>
  </head>
  <body>
  	<div class="father clearfix">
  		<div class="child1">儿子</div>
  		<div class="child2">二儿子</div>
  	</div>
  	<div class="header"></div>
  </body>
  </html>
  ```

- 内墙法

  - 有三个值：
    - left：当前元素左边不允许有浮动元素
    - right：当前元素右边不允许有浮动元素
    - both：当前元素左右两边不允许有浮动元素
  - 规则：在最后一个浮动元素的后面加一个空的块级元素，并且设置该属性clear：both
  - 缺点：结果冗余，网页中有很多这种情况，每个地方都加一遍代码就会冗余。

  示例：html文件

  ```html
  <!DOCTYPE html>
  <html>
  <head>
  	<title>浮动元素的破坏性与清除</title>
  	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
  	<style type="text/css">
  		.father{
  			border: 1px solid red;
  		}
  		.child1{
  			width: 200px;
  			height: 100px;
  			background-color: green;
  			float: left;
  		}
  		.child2{
  			width: 200px;
  			height: 100px;
  			background-color: orange;
  			float: right;
  		}
  		.header{
  			width: 100%;
  			height: 100px;
  			background-color: purple;
  		}
      /*给浮动元素的后面加一个空的div，
      并且该元素不浮动，然后设置clear：both*/
      .clear{
  			clear: both;
  		}
  	</style>
  </head>
  <body>
  	<div class="father clearfix">
  		<div class="child1">儿子</div>
  		<div class="child2">二儿子</div>
  		<!-- 第二种方法 clear:both -->
  		<div class="clear"></div>
  	</div>
  	<div class="header"></div>
  </body>
  </html>
  ```

- 伪元素清除法(常用)

  - 示例：html文件

  ```html
  <!DOCTYPE html>
  <html>
  <head>
  	<title>浮动元素的破坏性与清除</title>
  	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
  	<style type="text/css">
  		.father{
  			border: 1px solid red;
  		}
  		.child1{
  			width: 200px;
  			height: 100px;
  			background-color: green;
  			float: left;
  		}
  		.child2{
  			width: 200px;
  			height: 100px;
  			background-color: orange;
  			float: right;
  		}
  		.header{
  			width: 100%;
  			height: 100px;
  			background-color: purple;
  		}
      /*给浮动子元素的父盒子，
      也就是不浮动元素，添加一个clearfix的类，然后设置*/
      .clearfix::after{
        /*必须要写这三句话*/
  			content: ' ';
  			display: block;
  			clear: both;
  		}
  	</style>
  </head>
  <body>
  	<div class="father clearfix">
  		<div class="child1">儿子</div>
  		<div class="child2">二儿子</div>
  	</div>
  	<div class="header"></div>
  </body>
  </html>
  ```

- overlow:hidden清除(常用)

其实它是一个BFC区域：BFC (Block Formtting Context) 

 https://blog.csdn.net/riddle1981/article/details/52126522

规则：计算BFC(块级盒子)高度时，浮动元素(两边的盒子)也参与计算

形成BFC的条件：除了overflow:visitable的属性值

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动元素的破坏性与清除</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		.father{
      /*BFC (Block Formtting Context) 区域 
      一条规则：计算BFC(块级盒子)高度时，浮动元素(两边的盒子)也参与计算
			形成BFC的条件：除了overflow:visitable的属性值*/
   		overflow: hidden;
			border: 1px solid red;
		}
		.child1{
			width: 200px;
			height: 100px;
			background-color: green;
			float: left;
		}
		.child2{
			width: 200px;
			height: 100px;
			background-color: orange;
			float: right;
		}
		.header{
			width: 100%;
			height: 100px;
			background-color: purple;
		}
	</style>
</head>
<body>
	<div class="father clearfix">
		<div class="child1">儿子</div>
		<div class="child2">二儿子</div>
	</div>
	<div class="header"></div>
</body>
</html>
```

overflow属性规定当内容溢出元素框时发生的事情。

说明：这个属性定义溢出元素内容区的内容会如何处理。如果值为 scroll，不论是否需要，用户代理都会提供一种滚动机制。因此，有可能即使元素框中可以放下所有内容也会出现滚动条。

overflow的5个值：

| 值      | 描述                                                     |
| :------ | :------------------------------------------------------- |
| visible | 默认值。内容不会被修剪，会呈现在元素框之外。             |
| hidden  | 内容会被修剪，并且其余内容是不可见的。                   |
| scroll  | 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。 |
| auto    | 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。 |
| inherit | 规定应该从父元素继承 overflow 属性的值。                 |

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>overflow</title>
	<style type="text/css">
		body{
			overflow: scroll;
		}
		.box{
			width: 300px;
			height: 300px;
			border: 1px solid red;
			overflow: hidden;
		}
	</style>
</head>
<body>
	<div class="box">
		中华民族创造了灿烂的中华文明，为人类作出了卓越贡献，成为世界上伟大的民族。鸦片战争后，由于西方列强的入侵和封建统治的腐败，中国逐渐陷入半殖民地半封建社会的黑暗深渊，中国人民经历了战乱频仍、山河破碎、民不聊生的深重苦难。自强不息的中华民族从未放弃对美好梦想的向往和追求。习近平总书记指出：“实现中华民族伟大复兴，就是中华民族近代以来最伟大的梦想。”为了实现这个伟大梦想，中国人民和无数仁人志士进行了千辛万苦的探索和不屈不挠的斗争。可是，从太平天国运动、戊戌变法到义和团运动，一次次奋起抗争都失败了。孙中山先生领导的辛亥革命，虽然结束了统治中国几千年的君主专制制度，对推动中国社会进步具有重大意义，但也未能改变旧中国半殖民地半封建的社会性质和中国人民的悲惨命运。近代中国历史表明，旧式农民战争和软弱的资产阶级革命都不可能完成中华民族救亡图存和反帝反封建的历史任务，更不可能承担起实现民族复兴的历史使命。
	</div>
</body>
</html>
```

规则：计算BFC(块级盒子)高度时，浮动元素(两边的盒子)也参与计算

形成BFC的条件：除了overflow:visitable的属性值

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>浮动元素的破坏性与清除</title>
	<link rel="stylesheet" type="text/css" href="css/demo_10.css">
	<style type="text/css">
		.father{
   		overflow: hidden;
			border: 1px solid red;
		}
		.child1{
			width: 200px;
			height: 100px;
			background-color: green;
			float: left;
		}
		.child2{
			width: 200px;
			height: 100px;
			background-color: orange;
			float: right;
		}
		.header{
			width: 100%;
			height: 100px;
			background-color: purple;
		}
	</style>
</head>
<body>
	<div class="father clearfix">
		<div class="child1">儿子</div>
		<div class="child2">二儿子</div>
	</div>
	<div class="header"></div>
</body>
</html>
```

