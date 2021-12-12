# 前端CSS

### CSS简介：

CSS是指层叠样式表(Cascading Style Sheets)，样式定义如何显示HTML元素，样式通常又会存在于样式表中。也就是说把HTML元素的样式都统一收集起来写在一个地方或一个CSS文件里。

### CSS优势：

- 内容与表现分离
- 网页的变现统计，容易修改
- 丰富的样式，使页面布局更加灵活
- 减少网页代码量，增加网页浏览器速度，节省网络宽带
- 运用独立页面的CSS，有利于网页被搜索引擎收录

#### CSS基础语法：

css语法可以分为两部分：

- 1.选择器
- 2.声明

声明由属性和值组成，多个声明之间用分号进行分隔。

语法：

```html
选择器{
	样式1;
	样式2;
	......
}
```

例子：

```html
<!DOCTYPE html>
<html>
<head>
	<title>css样式声明</title>
	<!-- css样式：选择符和声明构成
	声明：属性名(color)和属性值(orange)
		  -->
	<style type="text/css">
		span{
			color: orange;
			font-size: 30px;
		}
	</style>
</head>
<body>
	<p>

		<span>小猪佩琦</span>
		喜欢 <span>吃炸鸡</span>
	</p>
</body>
</html>
```

#### css注释：

注释是代码之母

注释快捷键：alt＋／

```
/*这是注释*/
```

#### css中引用样式：

- 内联式
- 嵌入式
- 外部式
  - 链接式
  - 导入式

1.内联式

```html
<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<!-- 1.内联试 -->
	<p style="color: red">
		文本是什么颜色？
	</p>
</body>
</html>
```

2.嵌入式

```html
<!DOCTYPE html>
<html>
<head>
	<style type="text/css">
		h3{
			color: green;
		}
	</style>
</head>
<body>
	<h3>
		小猪佩琦🐷
	</h3>
</body>
</html>
```

3.外部式

html文件

```html
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="css/css_嵌入式.css">
</head>
<body>
	<p style="color: red">
		文本是什么颜色？
	</p>
	<h4>
		中华人民共和国
	</h4>
</body>
</html>
```

对应的css文件

```html
h4{
	color:blue;
}

p{
	color: red;
	font-size: 20px;
	font-weight: bold;
}
```

### 基本选择器：

在一个HTML页面中会有很多的元素，不同的元素可能有不同的样式，某些元素又需要设置相同的样式，选择器就是用来从HTML页面中查找特定的元素，找到元素之后就可以为它们设置样式了，选择器为样式规则指定一个作用范围。

##### 基础选择器包括：

- 标签(元素)选择器
- 类(class)选择器
- id(身份证号)选择器

##### 标签选择器：

解释：通过标签名来选择元素;

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>css的基础选择器-标签选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo4.css">
</head>
<body>
	<div id="container">
		<h3 class="active title">永恒课题</h3>
		<p>
			7月16日出版的第14期《求是》 <span class="active">杂志发表习近平总书记的重要文章</span>《增强推进党的政治建设的自觉性和坚定性》。 <span id="pq">文章强调：“党的政治建设是一个永恒课题，来不得半点松懈。</span>
		</p>
		<p>
			”并对抓好、落实党的政治建设提出了明确要求，具有很强的政治性、思想性和指导性。新华社 <span id="jj">《学习进行时》</span>以摘要形式梳理其中要点，和您一起学习。
		</p>
	</div>
</body>
</html>
```

css文件：

```html
p{
	color:red;
}
```

将所有p标签的字体设置为红色。

##### id选择器：

解释：通过标签的id值选择元素;

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>css的基础选择器-标签选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo4.css">
</head>
<body>
	<div id="container">
		<h3 class="active title">永恒课题</h3>
		<p>
			7月16日出版的第14期《求是》 <span class="active">杂志发表习近平总书记的重要文章</span>《增强推进党的政治建设的自觉性和坚定性》。 <span id="pq">文章强调：“党的政治建设是一个永恒课题，来不得半点松懈。</span>
		</p>
		<p>
			”并对抓好、落实党的政治建设提出了明确要求，具有很强的政治性、思想性和指导性。新华社 <span id="jj">《学习进行时》</span>以摘要形式梳理其中要点，和您一起学习。
		</p>
	</div>
</body>
</html>
```

css文件

```html
#pq{
	color: blue;
}
#jj{
	color: orange;
}
```

将所有id值pq标签的字体设置为蓝色，将所有id值jj标签的字体设置为橘色

注意⚠️：id的值式唯一的

##### 类选择器：

解释：通过标签的类选择元素：

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>css的基础选择器-标签选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo4.css">
</head>
<body>
	<div id="container">
		<h3 class="active title">永恒课题</h3>
		<p>
			7月16日出版的第14期《求是》 <span class="active">杂志发表习近平总书记的重要文章</span>《增强推进党的政治建设的自觉性和坚定性》。 <span id="pq">文章强调：“党的政治建设是一个永恒课题，来不得半点松懈。</span>
		</p>
		<p>
			”并对抓好、落实党的政治建设提出了明确要求，具有很强的政治性、思想性和指导性。新华社 <span id="jj">《学习进行时》</span>以摘要形式梳理其中要点，和您一起学习。
		</p>
	</div>
</body>
</html>
```

css文件

```html
.active{
	color: red;
}
.title{
	font-size: 30px;
}
```

把所有类为active的值的字体颜色设置为黑色，把所有类为title的值的字体大小设置为30px

##### 类选择器去重使用：

一个html文件设置的属性可能有很多重复的样式，如果把所有相同的样式都设置，会产生很多冗余的代码，所以我们可以把重复样式类的值写到一个类里边，以逗号分隔，这样就会减少css的代码量。

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>类选择器去重使用</title>
	<link rel="stylesheet" type="text/css" href="css/demo5.css">
</head>
<body>
	<!-- 绿色 20px -->
	<p class="lv big">欢迎</p>
	<!-- 绿色 粗 -->
	<p class="lv blg">欢迎</p>
	<!-- 粗 20px -->
	<p class="blg big">欢迎</p>
</body>
</html>
```

css文件

```html
.lv{
	color: green;
}
.big{
	font-size: 20px;
}
.blg{
	font-weight: bold;
}
```

把类为lv的值的颜色设置为绿色，类为big的值的字体大小设置成20px，类为blg的字体设置为粗体。

### 高级选择器：

高级选择器：

- 后代选择器
- 子代选择器
- 组合选择器
- 交集选择器
- 伪类选择器

##### 后代选择器：

解释：后代选择器从根元素一直往后查找并设置

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>高级选择器－后代／子代／交集选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo6.css">
</head>
<body>
	<h3>我在人民广场吃着炸鸡</h3>
	<div class="wrap">
		<p>
			<a href="#">小圆圈</a>
		</p>
		<a href="#">world</a>
	</div>
	<div>
		<a href="＃">hello world</a>
	</div>
	<a href="＃">OK</a>
	<span>在干嘛呢？</span>
	<span>工作忙吗？</span>

	<h2 class="met">web</h2>
</body>
</html>
```

css文件

```html
.wrap a{
	color: red;
}
```

把类的值为wrap的所有后代中a标签的字体颜色设置为红色

##### 子代选择器：

解释：从div的字元素中找到p标签设置

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>高级选择器－后代／子代／交集选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo6.css">
</head>
<body>
	<h3>我在人民广场吃着炸鸡</h3>
	<div class="wrap">
		<p>
			<a href="#">小圆圈</a>
		</p>
		<a href="#">world</a>
	</div>
	<div>
		<a href="＃">hello world</a>
	</div>
	<a href="＃">OK</a>
	<span>在干嘛呢？</span>
	<span>工作忙吗？</span>

	<h2 class="met">web</h2>
</body>
</html>
```

css文件

```html
.wrap >a{
	color: yellow;
}
```

把类的值为wrap的直接子元素中找到a标签，设置字体为黄色

##### 组合选择器：

解释：把设置相同的选择器用逗号隔开设置

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>高级选择器－后代／子代／交集选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo6.css">
</head>
<body>
	<h3>我在人民广场吃着炸鸡</h3>
	<div class="wrap">
		<p>
			<a href="#">小圆圈</a>
		</p>
		<a href="#">world</a>
	</div>
	<div>
		<a href="＃">hello world</a>
	</div>
	<a href="＃">OK</a>
	<span>在干嘛呢？</span>
	<span>工作忙吗？</span>

	<h2 class="met">web</h2>
</body>
</html>
```

css文件

```html
h3, span{
	color: gray;
	font-size: 14px;
}
```

把所有类的值为h3和span的标签的字体颜色设置为灰色，字体大小设置为14px

##### 交集选择器：

解释：提取两个选择器共同的部分进行设置

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>高级选择器－后代／子代／交集选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo6.css">
</head>
<body>
	<h3>我在人民广场吃着炸鸡</h3>
	<div class="wrap">
		<p>
			<a href="#">小圆圈</a>
		</p>
		<a href="#">world</a>
	</div>
	<div>
		<a href="＃">hello world</a>
	</div>
	<a href="＃">OK</a>
	<span>在干嘛呢？</span>
	<span>工作忙吗？</span>

	<h2 class="met">web</h2>
</body>
</html>
```

css文件

```html
h2{
	color: red;
}
.met{
	font-weight: lighter;
}
h2.met{
	font-size: 14px;
}
```

说明：如果类的值为h2和met的标签设置字体大小为14px，我们就可以提取两个标签共同的部分进行设置

语法：

```html
选择器1.选择器2{
	共同的样式;
}
```

##### 伪类选择器：

常见的几种伪类选择器。

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>伪类选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo7.css">
</head>
<body>
	<a href="#">小圆圈</a>
	<span>小米商城</span>
	<div>
		<span>小米手机</span>
	</div>
</body>
</html>

```

css文件

```h
/*没有被访问过a的状态*/
a:link{
	color: orange;
}
/*访问过后的状态*/
a:visited{
	color: green;
}
/*鼠标悬浮的状态,可以应用所有标签*/
a:hover{
	color: black;
}
/*鼠标摁住时的状态*/
a:active{
	color: yellow;
}
/*鼠标悬浮的状态,可以应用所有标签*/
span:hover{
	color: red;
}
/*鼠标悬浮的状态,可以应用所有标签*/
div:hover{
	background-color: green;
}
/*鼠标悬浮的状态,可以应用所有标签*/
div:hover span{
	color: white;
}
```

##### 伪元素：

常用的几种伪元素：

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>伪类选择器</title>
	<link rel="stylesheet" type="text/css" href="css/demo7.css">
</head>
<body>
	<a href="#">小圆圈</a>
	<span>小米商城</span>
	<div>
		<span>小米手机</span>
	</div>
	<p>我不知道</p>
</body>
</html>
```

css文件

```html
/*文本的首字符设置特殊样式*/
p:first-letter{
	font-size: 48px;
}
/*在标签的前面插入新的内容*/
span:before {
  content: "*";
  color: red;
}
/*在标签的后面插入新的内容*/
p:after {
  content: "?";
  color: red;
}
```

- p标签的首字符设置字体大小为48px
- 在span标签的前面插入新的内容，样式为‘＊’，字体颜色为红色
- 在p标签的最后插入新的内容，样式为‘？’，字体颜色为红色

##### 继承性：

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>继承性</title>
	<link rel="stylesheet" type="text/css" href="css/demo8.css">
</head>
<body>
	<div>
		<ul>
			<li>
				<p>这是继承了吗？</p>
			</li>
		</ul>
	</div>
</body>
</html>
```

css文件

```
body{
	color: red;
	font-size: 30px;
	border: 1px solid red;
}
```

css给根元素设置字体颜色为红色，字体大小为30px，并设置一个宽度为1px，实线，颜色为红色的方框线，在body下的元素都继承了body的样式；

### 选择器的优先级

我们现在已经学过了很多的选择器，也就是说我们从HTML中找一个元素的方法有很多种，既然有很多种，就会产生优先级。

例如：如果通过不同的选择器找到了相同的元素，并设置不同的样式，浏览器会怎么渲染呢？

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>选择器权重</title>
	<style type="text/css">
		/*001*/
		div{
			color: red;
		}
		/*010*/
		.b{
			color: purple;
		}
		/*100*/
		#b{
			color: orange;
		}
		/*003 3个标签相加*/
		html body div{
			color: blue;
		}
    /*数选择器的数量：
			内联选择器1000－id选择器100－类选择器10－元素选择器1
			*/
	</style>
</head>
<body>
	<div>a</div>
	<div class="b" id="b" style="color: green;">we</div>
</body>
</html>
```

选择器的权重规则：

- 内联选择器的权重为1000
- id选择器的权重为100
- 类选择器的权重为10
- 元素(标签)选择器的权重为1

选择器权重深入：

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>css选择器权重深入</title>
	<style type="text/css">
		/*001*/
		p{
			color: gray;
		}
		/*003*/
		div div p{
			color: yellow;
		}
		/*010*/
		.wrap3{
			color: purple;
		}
		/*011*/
		div .wrap3{
			color: black;
		}
		/*011*/
		div div .wrap3{
			color:  blue;
		}
		/*120*/
		.wrap1 #box2 .wrap3{
			color: green;
		}
		/*继承来的属性，权重非常低，几乎为0*/
		#box1 #box2{
			color: red;
		}
		/*继承来的属性低于选中标签的效果*/
		.container{
			color: red;
			font-size: 14px;
		}
		.container ul li{
			color: #000;
			font-size: 16px;
		}
	</style>
</head>
<body>
	<div class="wrap1" id="box1">
		<div class="wrap2" id="box2">
			<p class="wrap3" id="box3">
				到底是什么颜色？
			</p>
		</div>
	</div>
	<div class="container">
		<ul>
			<li>
				小米手机
			</li>
		</ul>
	</div>
</body>
</html>
```

注意⚠️：还有一种不讲道理的`!import`方式来强制让样式生效，这样不推荐使用，因为这样是破坏自然规律的一种写法，大量使用这中写法无法进行维护的，破坏自然规律！

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>!important讲解</title>
	<style type="text/css">
		div{
			color: purple !important;
		}
		#a{
			color: green !important;
		}
		/*都有!import，看权重*/
	</style>
</head>
<body>
	<div class="a" id="a">颜色</div>
</body>
</html>
```

如果div样式不加`!important`显示颜色为绿色，如果加了则显示紫色，如果都加了，则看权重，此时例子中显示的是绿色；

























































































### CSS的优点

- 节省时间
- 页面加载速度快
- 易于维护
- 多设备兼容性

## 总结：

选择器{

​	属性:值;

}

作用：选中页面上的元素(标签)，设置对应的样式

- 基础选择器

  - 对页面中相同的元素，设置共同的属性

- id选择器

  - 任何元素都可以设置id
  - id是唯一的，并且不能重复，表示选中的是有特性的元素

- class选择器

  - 任何元素都可以设置类
  - 一个元素中可以设置多个类
  - 一定要有"归类的概念，公共类的想法"，选中的页面元素，设置相同的属性

- 高级选择器

  - 后代
    - div p{}
  - 子代
    - div > p{}
  - 组合
    - 选择器1，选择器2，选择器3{}
  - 交集
    - 选择器1 选择器2{两个选择器交集的部分}
  - 伪类
    - a标签
    - 爱恨准则 LoVe HAte
      - a：link{}没有被访问过的状态
      - a：visited{}访问过后的状态
      - a：hover{}鼠标悬浮状态
      - a：active{}鼠标按住时的状态

  注意：hover可以应用于任何的元素

  ## 总结：字体属性和文本属性

  ### 字体属性：

  1.字体

  - font-family:"微软雅黑"，“宋体，。。。”

  2.字体大小

  - font-size:20px;
  - 像素单位：px，em，rem
  - px：绝对单位，一旦设置了，不管网页如何变化始终如一
  - em：相对单位，dangqian某块区域的字体大小，比如给p标签设置了字体大小20px，那么1em＝20px
  - rem：相对单位，主要应用于移动端

  3.字体颜色

  - color：red
  - 颜色表示法：
    - 单词表示法red，green，yellow，purple。
    - rgb()表示法
    - rgba() :
      - a：alpha表示透明度
    - 十六进制表示法
      - ＃ff6700

  4.字体样式

  - font-style
    - normal：默认的字体
    - italic：斜体

  5.字体粗细

  - font-weight：
    - bold：粗的字体
    - 100-900，默认400

  ### 文本属性：

  1.文本修饰

  - text-decoration
  - underline下划线
  - none无线
  - overline上划线
  - line－through删除线
  - 
    - 

  2.文本缩进

  - text-indent
    - 单位建议使用em，相对当前字体大小进行缩进

  3.行高

  - 行与行之间的距离
    - line-height
      - px，em，rem

  4.文字间距／单词间距

  - letter-spacing
  - word-spacing

  5.文本的对齐方式

  - text-align
    - left左对齐
    - right右对齐
    - center居中使用最多





