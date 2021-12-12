# Day35 notes

## 1. HTML简介

超文本标记语言（英语：HyperText Markup Language，简称：HTML）是一种用于创建网页的标准标记语言。标记语言是一种将文本（Text）以及文本相关的其他信息结合起来，展现出关于文档结构和数据处理细节的计算机文字编码。与文本相关的其他信息（包括例如文本的结构和表示信息等）与原来的文本结合在一起，但是使用标记（markup）进行标识。可以使用 HTML 来建立自己的 WEB 站点，HTML 运行在浏览器上，由浏览器来解析。

### 1.1 HTML文档的后缀名

- .html
- .htm

以上两种后缀名没有区别，都是静态网页后缀名，都可以使用。

### 1.2 什么是HTML?

HTML 是用来描述网页的一种语言。

- HTML 指的是超文本标记语言: **H**yper**T**ext **M**arkup **L**anguage
- HTML 不是一种编程语言，而是一种**标记**语言
- 标记语言是一套**标记标签** (markup tag)
- HTML 使用标记标签来**描述**网页
- HTML 文档包含了HTML **标签**及**文本**内容
- HTML文档也叫做 **web 页面**

HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

- HTML 标签是由*尖括号*包围的关键词，比如` <html>`
- HTML 标签通常是*成对出现*的，结束标签比开始标签多了一个`/`，比如 `<b>` 和`</b>`
- 标签对中的第一个标签是*开始标签*，第二个标签是结束标签，也称为开放，闭合标签
- 标签之间是可以嵌套的。例如：`div`标签里面嵌套`p`标签的话，那么`</p>`必须放在`</div>`的前面。
- HTML标签不区分大小写，`<h1>`和`<H1>`是一样的，但是我们通常建议使用小写，因为大部分程序员都以小写为准

HTML 是用来描述网页的一种语言。

- HTML 指的是超文本标记语言: **H**yper**T**ext **M**arkup **L**anguage
- HTML 不是一种编程语言，而是一种**标记**语言
- 标记语言是一套**标记标签** (markup tag)
- HTML 使用标记标签来**描述**网页
- HTML 文档包含了HTML **标签**及**文本**内容
- HTML文档也叫做 **web 页面**

### 1.3 HTML 标签特点

HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

- HTML 标签是由*尖括号*包围的关键词，比如` <html>`
- HTML 标签通常是*成对出现*的，结束标签比开始标签多了一个`/`，比如 `<b>` 和`</b>`
- 标签对中的第一个标签是*开始标签*，第二个标签是结束标签，也称为开放，闭合标签
- 标签之间是可以嵌套的。例如：`div`标签里面嵌套`p`标签的话，那么`</p>`必须放在`</div>`的前面。
- HTML标签不区分大小写，`<h1>`和`<H1>`是一样的，但是我们通常建议使用小写，因为大部分程序员都以小写为准

### 1.4 HTML文档结构

​	下面是一个可视化的HTML页面结构：![前端HTML](/Users/zhangzhiqiang/Desktop/web前端/img/前端HTML.png)

#### 1.4.1 HTML实例

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
	<title>HTML实例</title>
</head>
<body>
	<h1>标题1</h1>
	<p>段落1</p>

</body>
</html>
```

实例解析

- `<!DOCTYPE html>` 声明为 HTML5 文档
- `<html></html>`元素是 HTML 页面的根元素
- `<head> </head>`标签用于定义文档的头部，它是所有头部元素的容器。常见的头部元素有`<title>`、`<script>`、`<style>`、`<link>`和`<meta>`等标签，头部标签在下一节中会有详细介绍。
- `<title>` 元素描述了文档的标题
- `<body></body>`标签之间的内容是网页的主要内容，如`<h1>`、`<p>`、`<a>`、`<img>`等网页内容标签，在`<body>`标签中的内容（图中淡绿色部分内容）最终会在浏览器中显示出来。

### 1.5 HTML注释

无论我们学习什么编程语言，一定要重视的就是注释。

HTML中注释的格式:

```html
<!--这里是注释的内容-->
```

注意： 注释中可以直接使用回车换行。

并且我们习惯用注释的标签把HTML代码包裹起来。如：

```html
<!-- xx部分 开始 -->
    这里放你xx部分的HTML代码
<!-- xx部分 结束 -->
```

HTML注释的注意事项：

1. HTML注释不支持嵌套。
2. HTML注释不能写在HTML标签中。

### 1.6 head标签

`head`标签申明了文档的头部的信息，描述了文档的各种属性和信息，包括文档的标题、编码方式及URL等信息,这些信息大部分是用于提供索引,辩认或其他方面的应用（移动端）的等。 以下标签是可以用在`head`标签中的：

```html
<!DOCTYPE html>
<html>
<head>
	<title>HTML实例</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="">
	<style type="text/css"></style>
</head>
```

#### 1.6.1 title标签

`<title>`标签：在`<title>`和`</title`>标签之间的文字内容是网页的标题信息，它会显示在浏览器标签页的标题栏中。可以把它看成是一个网页的标题。主要用来告诉用户和搜索引擎这个网页的主要内容是什么，搜索引擎可以通过网页标题，迅速的判断出当前网页的主题。示例：

```html
<!DOCTYPE html>
<html>
	<head>
		<title>段落／语气／换行／无序／有序／定义／表格</title>
	</head>
</html>
```

![title图片](/Users/zhangzhiqiang/Desktop/web前端/img/title图片.png)

#### 1.6.2 meta标签

Meta标签介绍：

元素可提供有关页面的原信息（mata-information）,针对搜索引擎和更新频度的描述和关键词。

标签位于文档的头部，不包含任何内容。

提供的信息是用户不可见的。 meta标签的组成：meta标签共有两个属性，它们分别是http-equiv属性和name属性，不同的属性又有不同的参数值，这些不同的参数值就实现了不同的网页功能。

常用的meta标签：

- http-equiv属性

它用来向浏览器传达一些有用的信息，帮助浏览器正确地显示网页内容，与之对应的属性值为content，content中的内容其实就是各个参数的变量值。

```html
<!--重定向 2秒后跳转到对应的网址，注意分号-->
<meta http-equiv="refresh" content="2;URL=http://www.luffycity.com">
<!--指定文档的内容类型和编码类型 -->
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<!--告诉IE浏览器以最高级模式渲染当前网页-->
<meta http-equiv="x-ua-compatible" content="IE=edge">
```

- name属性

主要用于页面的关键字和描述，是写给搜索引擎看的，关键字可以有多个用 ‘,’号隔开，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的。

```html
<meta name="keywords" content="meta总结,html meta,meta属性,meta跳转">
<meta name="description" content="meta标签">
```

### 1.7 其他标签

```html
<!--标题-->
<title>标题标签</title>
<!--icon图标（网站的图标）-->
<link rel="icon" href="fav.ico">
<!--定义内部样式表-->
<style></style>
<!--引入外部样式表文件-->
<link rel="stylesheet" href="mystyle.css">
<!--定义JavaScript代码或引入JavaScript文件-->
<script src="myscript.js"></script>
```

### 1.8 body标签

想要在网页上展示出来的内容一定要放在`body`标签中。

`<h1>` - `<h6>` 标签可定义标题。`<h1>` 定义最大的标题。`<h6>` 定义最小的标题。 由于 h 元素拥有确切的语义，因此慎重地选择恰当的标签层级来构建文档的结构。不要利用标题标签来改变同一行中的字体大小。我们应当使用css来定义来达到漂亮的显示效果。 标题标签通常用来制作文章或网站的标题。

#### 1.8.1 标题标签`h1～h6`

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<h1>一级标题</h1>
  <h2>二级标题</h2>
	<h3>三级标题</h3>
	<h4>四级标题</h4>
	<h5>五级标题</h5>
	<h6>六级标题</h6>	
</body>
</html>
```

文本样式标签：主要对HTML页面中的文本进行修饰

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<h1>一级 <b>标题</b></h1>
	<h2>二级 <i>标题</i></h2>
	<h3>三级 <u>标题</u></h3>
	<h4>四级 <s>标题</s></h4>
	<h5>五级 <sup>标题</sup></h5>
	<h5>五级 <sub>标题</sub></h5>
	<h6> <em>六级</em> <strong>标题</strong></h6>	
</body>
</html>
```

总结：

```
1. <b>加粗</b>
2. <i>斜体</i>
3. <u>下划线</u>
4. <s>删除线</s>
5. <sup>上标</sup>
6. <sub>下标</sub>
7. <strong>强调：斜体</strong>
8. <em>强调：粗体</em>
一般强调我们习惯用strong标签来强调
```

#### 1.8.2 段落标签`p`

`<p></p>`paragraph的简写。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<h2>段落标签</h2>
	<p>售后政策</p>
	<p>小米服务</p>
	<p>自主服务</p>
	<p>我不知道</p>
</body>
</html>
```

`<br>`标签用来将内容换行，其在HTML网页上的效果相当于我们平时使用word编辑文档时使用回车换行。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<h2>换行标签</h2>
	作为子民我愿以此身终生报效国家， <br>大丈夫建功立业何须活着返回家园。
</body>
</html>
```

#### 1.8.3 列表标签`ul`

`<ul>`：unordered lists的缩写 无序列表。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
   <!-- 无序列表 type可以定义无序列表的样式-->
    <ul type="circle">
        <li>我的账户</li>
        <li>我的订单</li>
        <li>我的优惠券</li>
        <li>我的收藏</li>
        <li>退出</li>
    </ul>
</body>
</html>
```

ul标签的属性：列表标识类型

- disc：实心圆(默认值)
- circle：空心圆
- square：实心矩形
- none：不显示标识

#### 1.8.4 列表标签`ol`

`<ol>`：ordered listsde的缩写 有序列表。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<!-- 有序列表 type可以定义有序列表的样式 -->
    <ol type="a">
        <li>我的账户</li>
        <li>我的订单</li>
        <li>我的优惠券</li>
        <li>我的收藏</li>
        <li>退出</li>
    </ol>
</body>
</html>
```

ol标签的属性：列表标识类型

- 1：数字
- a：小写字母
- A：大写字母
- i：小写罗马字符
- I：大写罗马字符

列表表示的起始编号默认为1

#### 1.8.5 列表标签`dl`

html `<dl> <dt> <dd>`是一组合标签，使用了dt dd最外层就必须使用dl包裹，此组合标签我们也又叫表格标签，与table表格类似组合标签，故名我们也叫dl表格。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<!-- <dl> 标签用于定义列表类型标签 -->
	<dl>
		<dt>帮助中心</dt>
		<dd>账户管理</dd>
		<dd>购物指南</dd>
		<dd>订单操作</dd>
	</dl>
</body>
</html>
```

#### 1.8.6 表格标签`table`

表格由`<table>` 标签来定义。每个表格均有若干行（由 `<tr>` 标签定义），每行被分割为若干单元格（由`<td>`标签定义）。字母 td 指表格数据（table data），即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。

``` html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<table border="1" cellspacing="0">
		<!-- 标题 -->
		<caption>商品清单</caption>
		<!-- 表格头 -->
		<thead>
			<!-- 表格行 -->
			<tr>
				<!-- 表格头里的列：［th］ -->
				<th>产品名称</th>
				<th>品牌</th>
				<!-- 横向合并：合并列数 -->
				<th colspan="2">数量和入库时间</th>
			</tr>
		</thead>
		<!-- 表格主体 -->
		<tbody>
			<!-- 表格行 -->
			<tr>
				<!-- 表格体里列：［td］ -->
				<td>电视机</td>
				<td>小米</td>
				<td>200</td>
				<td>2018-09</td>
			</tr>
			<tr>
				<td>电冰箱</td>
				<!-- 纵向合并：合并行数 -->
				<td rowspan="2">海尔</td>
				<td>900</td>
				<td>2018-06</td>
			</tr>
				<tr>
				<td>电冰箱</td>
				<td>900</td>
				<td>2018-06</td>
			</tr>
		</tbody>
		<!-- 表格底部 -->
		<tfoot>
			<tr>
				<td colspan="4">备注</td>
			</tr>
		</tfoot>
	</table>
</body>
</html>
```

表格架构：

- table：表格
  - caption：标题
  - thead：表格头
    - tr：表格头中的行
      - th：表格头中的单元格
  - tbody：表格体
    - tr：表格体中的行
      - td：表格体中的单元格
  - tfoot：表格底部

合并：

- rowspan：合并行（竖着合并）
- colspan：合并列（横着合并）

#### 1.8.7 超链接标签`a`

超级链接`<a>`标记代表一个链接点，是英文anchor（锚点）的简写。它的作用是把当前位置的文本或图片连接到其他的页面、文本或图像。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<!-- href：超链接地址 -->
	<!-- title：鼠标悬停时的提示语 -->
	<!-- target=_self：为在当前窗口打开
		 target=_blank：为在新的窗口打开
		-->
		<p id="top"></p>
    <a href="http://www.baidu.com" target="_blank" title="点击一下，了解更多">百度一下</a>
    <a href="a.zip">下载包</a>
    <a href="13870492666@163.com">联系我们</a>
    <!-- 返回页面顶部的内容 -->
    <a href="#">跳转到顶部</a>

    <!-- 返回某个id -->
    <a href="#p1">跳转到p1</a>
    <!-- javascript:alert(1)是表示在触发<a>默认动作时，执行一段JavaScript代码;
	而 javascript:表示什么都不执行，这样点击<a>时就没有任何反应。 -->
    <a href="javascript:alert(1)">内容</a>
    <a href="javascript:;">内容</a>
    <p>向下滚动</p>
    <p>向下滚动</p<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<!-- href：超链接地址 -->
	<!-- title：鼠标悬停时的提示语 -->
	<!-- target=_self：为在当前窗口打开
		 target=_blank：为在新的窗口打开
		-->
		<p id="top"></p>
    <a href="http://www.baidu.com" target="_blank" title="点击一下，了解更多">百度一下</a>
    <a href="a.zip">下载包</a>
    <a href="13870492666@163.com">联系我们</a>
    <!-- 返回页面顶部的内容 -->
    <a href="#">跳转到顶部</a>

    <!-- 返回某个id -->
    <a href="#p1">跳转到p1</a>
    <!-- javascript:alert(1)是表示在触发<a>默认动作时，执行一段JavaScript代码;
	而 javascript:;表示什么都不执行，这样点击<a>时就没有任何反应。 -->
    <a href="javascript:alert(1)">内容</a>
    <a href="javascript:;">内容</a>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
    <p>向下滚动</p>
		<a href="#top">回到顶部</a>
</body>
</html>	
```

备注：

- href：超链接地址
- title：鼠标悬停时的提示语
- target=**_self**：为在当前窗口打开
- target=**_blank**：为在新的窗口打开

链接其他表现形式：

- 目标文档为下载资源：
  - 例如：href属性值，指定的文件名.rar/zip，就是下载操作(rar、zip等)

- 电子邮件链接:
  - 前提：计算机中必须安装邮件客户端，并且配置好了邮件相关信息。 例如：`<a href="13870492666@163.com">联系我们</a>`

- 返回页面顶部的空链接或具体id值的标签:
  - 例如：`<a href="#">内容</a>`或`<a href="#id值">内容</a>`

- javascript:是表示在触发`<a>`默认动作时，执行一段JavaScript代码:
  - 例如：`<a href="javascript:alert()">内容</a>`

- javascript:;表示什么都不执行，这样点击`<a>`时就没有任何反应:
  - 例如：`<a href="javascrip:;">`内容</a

#### 1.8.8 图片标签`img`

使用`<img/>`标签在网页中插入图片；

语法：`<img src="图片地址" alt="图片加载失败时显示的内容" title = "提示信息" />`

```html
<!DOCTYPE html>
<html>
<head>
	<title>img标签</title>
</head>
<body>
	<!-- 相对路径：
		.／1.png
		..／1.png
		...／1.png
	 -->
	<!-- 绝对路径：
		/Users/zhangzhiqiang/Desktop/web前端/img/1.png
	 -->
	 <p>
 	描述该图片内容的信息,
	<span>与行内元素展示的标签,<span>
    <span>与行内元素展示的标签<span>
	</p>
	<img src="./1.png" width="600" height="500" alt="加载失败显示字符" title="鼠标悬浮显示标题">
</body>
</html>
```

⚠️注意：

- src设置的图片地址可以是本地的地址也可以是一个网络地址

- 图片的格式可以是png、jpg和gif

- alt属性的值会在图片加载失败时显示在网页上

- 还可以为图片设置宽度(width)和高度(height)，不设置就显示图片默认的宽度和高度
- 与行内元素在一行内显示
- 可以设置宽度和高度
- span标签可以单独摘出某块内容，结合css设置相应的样式

#### 1.8.9 表单标签`form`

表单是一个包含表单元素的区域，允许用户在表单中输入内容；

语法：

```
<form>允许出现表单控件</form>
```

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>form标签</title>
</head>
<body>
	<form action="https://www.baidu.com/" method="post" enctype="multipart/form-data ">
		<!-- 文本框 -->
		<p>
			用户名:
			<input type="text" name="username" placeholder="请输入用户名" readonly >
		</p>
		<p>
			密码：
			<input type="password" name="pwd" placeholder="请输入密码">
		</p>
		<p>
			确认密码：
			<input type="re_password" name="re_pwd" placeholder="确认密码" disabled>
		</p>
		<p>
			<label for="yzm">验证码：</label>
			<input type="text" name="yzm" id="yzm" placeholder="输入验证码">
		</p>
		<!-- 单选框 -->
		<p>
			性别：
			<!-- checked默认选中 -->
			<!-- radio单选框 -->
			男：<input type="radio" name="sex" checked="">
			女：<input type="radio" name="sex">
		</p>
		<p>
			提交:
			<input type="submit" name="sub">
		</p>
		<hr>
		<!-- 多选框 -->
		<p>
			课程多选：
			<!-- checkbox复选框 -->
			web前端<input name="pd" type="checkbox" checked="">
			python开发<input name="kf" type="checkbox" name="">
			linux编程<input name="bc" type="checkbox" name="">
		</p>
		<hr>
		<!-- 下拉单选 -->
		<p>
			下拉框实现单选：
			<select>
				<!-- selected 默认选中项 -->
				<option>html</option>
				<option>css</option>
				<option selected="python">python</option>
				<option>vue</option>
			</select>
		</p>
		<hr>
		<!-- 下拉多选 -->
		<p>
			<!--滚动列表 multiple设置以后实现多选效果，ctrl+鼠标左键进行多选-->
			下拉框实现多选：
			<select multiple="multiple">
				<option>html</option>
				<option>css</option>
				<option selected="python">python</option>
				<option>vue</option>
				<option>linux</option>
				<option>c</option>
				<option>java</option>
				<option>ruby</option>
				<option>go</option>
			</select>
		</p>
		<hr>
		<!-- textarea -->
		<p>
			个人描述：
			<!-- 超出文本框可以滚动列表 -->
			<textarea rows="10" cols="30">
			</textarea>
		</p>
		<!-- 上传文件 -->
		<p>
			上传文件：
			<input type="file" name="textfile">
		</p>
		<!-- 按钮 -->
		<p>
			<input type="submit" name="zc" value="立即注册">
			<input type="reset" name="cz" value="重置">
			<input type="button" name="an" value="普通按钮">
			<input type="hidden" name="hi" value="隐藏按钮">
			<input type="image" src="./1.png" name="submit" title="百度一下">
		</p>
	</form>
</body>
</html>
```

示例解释：

- form表单标签

  - action：表单提交时的动作，提交给服务器处理程序的地址
  - accept—charset：提交表单中使用的字符集
  - name：识别表单的名称

  - method：定义表单提交时的方式
    - get：明文提交，数据显示在地址上，安全性低，提交最大为2KB
    - post：隐式提交，数据显示在Form Data里，安全性高，无大小限制
  - enctype：
    - `application/x-www-form-urlencoded`所有字符都可以提交给服务器，不允许上传文件，默认
    - `multipart/form-data`将文件以二进制提交给服务器
    - `text/plain `只允许提交普通字符，特殊字符和文件都无法提交，在发邮件时要设置这种类型
  - target：action属性中地址的mubiao，默认：_self

  ⚠️注意：如果有文件需要提交给服务器，methdo必须为post请求方式，enctype必须为multipart/form-data。

- 表单控件

  - input组传统属性：

    - type：
      - button：可点击按钮
      - text：明文显示输入的数据
      - password：密文显示用户输入的数据，一般用在密码输入
      - radio：单选按钮
      - checkbox：复选框
      - submit：功能固定化，负责将表中的表单提交给服务器
      - file：上传文件
      - hidden：隐藏输入字段，用户看不到
      - image：图像形式的提交按钮
      - reset：重置按钮，会清除表单中的所有数据
    - value：input元素设定值，checkbox或radio必须设置value属性
    - name：规定input的名称，提交到服务器后的表单进行标识
    - readonly：输入字段为只读，与text或password元素配合使用
    - disabled：输入字段为禁用，无法与hidden一起使用
    - size：输入字段大小，统计字符，与text或password元素配合使用
    - maxlength：输入字段的长度
    - accept：规定文件上传的类型
    - alt：图片无法显示时，提供备选信息，只能与type="image"元素配合使用
    - src：提交按钮显示的图像URL，与text或password元素配合使用
    - checked：页面加载时/后预选的input元素，通过javascript进行设置

  - input组新增属性：

    - autocomplete：浏览器应该自动完成表单，默认开启
    - autofocus：页面加载时，域自动获得焦点
    - novalidate：提交表单时不验证form或input域
    - height：规定image类型的input标签的图像高度，用于image类型的input标签
    - width：规定image类型的input标签的图像宽度，用于image类型的input标签
    - list：在表单控件输入数据时可用的一个选项列表
    - min：规定输入域所允许的最大值
    - max：规定输入域所允许的最小值
    - step：规定合法的数字间隔
    - multiple：规定按住ctrl按键，输入字段可以选择多个值，用于type="email"和"file"的input元素
    -  pattern：用于验证input域的模式。模型pattern是正则表达式
    - placeholder：提供占位符文字，描述输入域所期待的值。占位符会在输入域为空时显示出现，在输入域获得焦点时消失
    - required：规定必须在提交之前填写输入域
    - form：规定输入域所属的一个或多个表单，form属性必须和所属表单的id
    - formaction：重写表单的action属性
    - formenctype：重写表单的enctype属性
    - formmethod：重写表单的method属性
    - formnovalidate：重写表单的novalidate属性
    - formtarget：重写表单的target属性

  - select和option选项框：

    - select属性

      - size：取值大于1位滚动列表，否则为下拉框
      - multiple：设置多选

    - option属性

      - value：选项的值
      - selected：预选中

      ⚠️注意：如果不设置selected属性的话，那么选项框中的第一个值默认被选中

  - textarea文本域：允许用户在表单中录入多行数据的控件

    - cols：指定文本区域的列数，变相设置当前元素的宽度
    - rows：指定文本区域的行数，变相设置当前元素的高度

  - lable：关联文本与表达的元素，点击文本时，如同点击表单元素一样

#### 1.9 其它标签

##### 1.9.1 换行标签`br`

`<br>`标签用来将内容换行，其在HTML网页上的效果相当于我们平时使用word编辑文档时使用回车换行。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>h1-h6标签</title>
</head>
<body>
	<h2>换行标签</h2>
	作为子民我愿以此身终生报效国家， <br>大丈夫建功立业何须活着返回家园。
</body>
</html>
```

##### 1.9.2 分割线`hr`

`<hr>`标签用来在HTML页面中创建水平分隔线，通常用来分隔内容。

```html
<!DOCTYPE html>
<html>
<head>
	<title>段落／语气／换行／无序／有序／定义／表格</title>
</head>
<body>
	<h2>段落标签</h2>
	<p>售后政策</p>
	<p>小米服务</p>
	<p>自主服务</p>
	<p>我不知道</p>
	<hr>

	<h2>定义列表－definition list</h2>
		<dl>
			<dt>帮助中心</dt>
			<dd>账户管理</dd>
			<dd>购物指南</dd>
			<dd>订单操作</dd>
		</dl>
	<hr>
</body>
</html>
```

##### 1.9.3 特殊符号

浏览器在显示的时候会移除源代码中多余的空格和空行。 所有连续的空格或空行都会被算作一个空格。需要注意的是，HTML代码中的所有连续的空行（换行）也被显示为一个空格。

```html
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>路飞符号</title>
    </head>
    <body>

        <p>帮助有志向的年轻人


            通过努力学习获得
            体面的   	工作  和    生活！
            &hearts;A &clubs;A &spades;A &diams;A
        </p>
    </body>
</html>
```

[特殊符号对照表](http://tool.chinaz.com/Tools/HtmlChar.aspx)

