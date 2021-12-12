# Day notes 45

## 今日内容

- DOM

### 1.DOM简介

**概念：**

所谓DOM,全称 Docuemnt Object Model 文档对象模型，毫无疑问，此时要操作对象，什么对象？文档对象

在文档中一切皆对象，比如html,body,div,p等等都看做对象，那么我们如何来点击某个盒子让它变色呢？

DOM 为文档提供了结构化表示，并定义了如何通过脚本来访问文档结构。目的其实就是为了能让js操作html元素而制定的一个规范。

**解析过程：**

HTML加载完毕，渲染引擎会在内存中把HTML文档，生成一个DOM树，getElementById是获取内中DOM上的元素节点。然后操作的时候修改的是该元素的**属性**。

**DOM骨架树（一切皆是节点）**

![DOM](G:\homework\img\DOM.png)

- **元素节点**：HMTL标签。
- **文本节点**：标签中的文字（比如标签之间的空格、换行）
- **属性节点**：：标签的属性

整个html文档就是一个文档节点。所有的节点都是Object。

**DOM的作用：**

- 找对象（元素节点）
- 设置元素的属性值
- 设置元素的样式
- 动态创建和删除元素
- 事件的触发响应：事件源、事件、事件的驱动程序

获取其他DOM的三种方式：

示例：

```js
// 1.document.getElementById()
var doc = document.getElementById('class_list');
console.log(doc);
console.log(typeof doc);

// 2.docuemnt.getElementsByTagName()获取出来的是一个节点对象节点集合
var olis = document.getElementsByTagName('li');
console.log(olis);
for (var i = 0;i < olis.length;i++) {
    console.log(olis[i])
}
console.log(typeof olis);

// 3.document.getElementByClassNmae('item')
var ootem= document.getElementsByClassName('item');
console.log(ootem);
for (var i = 0;i < ootem.length;i++) {
    console.log(ootem[i])
}
```

示例：遍历对象节点集合

```js
// 1.document.getElementById()
var doc = document.getElementById('class_list');
console.log(doc);
console.log(typeof doc);

// 2.docuemnt.getElementsByTagName()获取出来的是一个节点对象节点集合
var olis = document.getElementsByTagName('li');
console.log(olis);
for (var i = 0;i < olis.length;i++) {
    console.log(olis[i])
}
console.log(typeof olis);

// 3.document.getElementByClassNmae('item')
var ootem= document.getElementsByClassName('item');
console.log(ootem);
for (var i = 0;i < ootem.length;i++) {
    console.log(ootem[i])
}
```

示例：设置属性值

```html
<!DOCTYPE html>
<html>
<head>
	<title>class_list2</title>
	<style type="text/css">
		#box{
			color: red;
		}
	</style>
</head>
<body>
		<h2>你要买什么课程</h2>
	<p title="轻选择购买的课程" id="box">本课程是web全栈课程</p>
	<ul id="class_list">
		<li class="item">javascript</li>
		<li class="item">css</li>
		<li>Dom</li>
	</ul>
	<script type="text/javascript">
		var op = document.getElementsByTagName('p')[0];
		// 设置属性值 有一个必须的参数，这个节点对象的名字
		var title = op.getAttribute('title');
		console.log(title);

		// 设置属性值：setAttribute(name,value)
		op.setAttribute('id','box');
	</script>
</body>
</html>
```

### 2.节点属性

在文档对象模型中，每一个节点都是一个对象，DOM节点有三个重要的属性

1. nodeName：节点的名称
2. nodeValue：节点的值
3. nodeType：节点的类型

一.nadeName属性：节点的名称是只读

	1.元素节点的nodeName与标签名相同
	2.属性节点的nodeName与属性的名称相同
	3.文本节点的nodeName永远是#text
	4.文档节点的nodeName永远是#document

二.nodeValue属性：节点的值

	1.元素节点的nodeValue是undefinede或null
	2.文本节点的nodeValue是文本自身
	3.属性节点的nodeValue是属性的值

3.nodeType属性：节点的类型，是只读的

```html
以下常用的集中节点类型：
元素类型		节点类型
元素            1
属性            2
文本            3
注释	          8
文档            9
```
示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>节点属性</title>
</head>
<body>
	<div id="box" title="我是文档">我是一个文本节点<!-- 我是注释 --></div>
	<script type="text/javascript">
		// 1.元素节点
		var odiv = document.getElementById('box');
		// DIV|null|1
		console.log(odiv.nodeName + '|' + odiv.nodeValue + '|'+ odiv.nodeType);

		// 2.属性节点
		var attrNode = odiv.attributes[0];
		// id|box|2
		console.log(attrNode.nodeName + "|" + attrNode.nodeValue + "|" + attrNode.nodeType);

		// 3.文本节点
		var textNode = odiv.childNodes[0];
		// #text|我是一个文本节点|3
		console.log(textNode.nodeName + "|" + textNode.nodeValue + "|" + textNode.nodeType);

		// 4.注释节点
		var commentNode = odiv.childNodes[1];
		// #comment| 我是注释 |8
		console.log(commentNode.nodeName + "|" + commentNode.nodeValue + "|" + commentNode.nodeType);
		// 5.文档节点 9
		console.log(document.nodeType);
	</script>
</body>
</html>
```

节点对象常用属性：

示例：缺点--标签不能换行

```html
<div class="xiongdi1">我是上兄弟</div><div id="father"><p>iker</p><p>ikeer2</p></div><div class="xiongdi">我是兄弟</div>

<script type="text/javascript">
    var ofather = document.getElementById('father');
    console.log(ofather.childNodes);// 获得元素的集合
    console.log(ofather.childNodes[0]);// 获得集合的第一个
    console.log(ofather.firstChild);// 获得第一个元素
    console.log(ofather.lastChild);// 获得最后一个元素
    console.log(ofather.childNodes[ofather.childNodes.length-1]);// 获得最后一个元素
    console.log(ofather.parentNode);// 获得父元素

    console.log(ofather.nextSibling);// 获得后边挨着的元素
    console.log(ofather.previousSibling);//获得上一个元素
</script>
```

示例：解决标签不能换行

```html
<div class="xiongdi1">我是上兄弟</div>
	<div id="father">
		<p>iker</p>
		<p>ikeer2</p>
	</div>
	<div class="xiongdi">我是兄弟</div>
	<script type="text/javascript">
		 function get_childNodes(fatherNode){
		 	var nodes = fatherNode.childNodes;
			var arr = [];
			for (var i = 0; i < nodes.length; i++) {
				if (nodes[i].nodeType === 1) {
					arr.push(nodes[i]);
				}
			}
			return arr;
		}
		var childnodes = get_childNodes(ofather);
		console.log(childnodes);
	</script>
```

示例：获取下一个div

```html
<div class="xiongdi1">我是上兄弟</div>
	<div id="father">
		<p>iker</p>
		<p>ikeer2</p>
	</div>
	<div class="xiongdi">我是兄弟</div>
	<script type="text/javascript">
		function get_nextSibling(x) {
			var y = x.nextSibling;
			while (y && y.nodeType != 1){
				y = y.nextSibling;
			}
			return y;
		}
		console.log(get_nextSibling(ofather));
	</script>
```

### 3.节点方法

```js
动态的操作节点：
1.创建节点 createElement()
2.插入节点 appendChild()	  insertBefore(newNode,node)
3.删除节点 removeChild()
4.替换节点 replaceChild(newNode,node)
5.创建文本节点 createTextNode()
```
插入节点有两种方式，它们的含义是不同的。

方式1：

```
 父节点.appendChild(新的子节点);
```

解释：父节点的最后插入一个新的子节点。

方式2：

```
父节点.insertBefore(新的子节点,作为参考的子节点);
```

解释：

- 在参考节点前插入一个新的节点。
- 如果参考节点为null，那么他将在父节点最后插入一个子节点。

删除节点

格式如下：

```
  父节点.removeChild(子节点);
```

解释：**用父节点删除子节点**。必须要指定是删除哪个子节点。

如果我想删除自己这个节点，可以这么做：

```
node1.parentNode.removeChild(node1);
```

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>节点方法</title>
	<style type="text/css">
		.active{
			color: red;
			font-size: 30px;
		}
	</style>
</head>
<body>
	<div id="box">
		<p id="active">ike</p>
	</div>
	<!-- 
	动态的操作节点：
	1.创建节点 createElement()
	2.插入节点 appendChild()	  insertBefore(newNode,node)
	3.删除节点 removeChild()
	4.替换节点 replaceChild(newNode,node)
	5.创建文本节点 createTextNode()
	 -->
	 <script type="text/javascript">
	 	var oDiv = document.getElementById('box');
	 	var oAtive = document.getElementById('active');

	 	var newNode = document.createElement('p');
	 	var newNode2 = document.createElement('p');
	 	var newNode3 = document.createElement('a');

	 	console.log(newNode === newNode2)


	 	newNode.setAttribute('class','active');
	 	oDiv.appendChild(newNode);
	 	// 第一个参数是新插入的节点，第二个参数是参考点
		oDiv.appendChild(newNode2, oAtive);
	 	// newNode = null; // 释放对象
	 	var textNode = document.createTextNode('alex');
	 	newNode.appendChild(textNode);

		// 仅仅设置文本内容
	 	newNode.innerHTML = '<a href="#">alex@163.com</a>';
	 	newNode2.innerHTML = '<a href="#">学前端</a>';
	 	newNode3.setAttribute('href', 'http://www.baidu.com')
	 	newNode3.innerHTML = '百度一下';
	 	// newNode.innerText = '<a href="#">alex@163.com</a>';

	 	// 删除操作
	 	// oDiv.removeChild(oAtive);

	 	// 替换操作
	 	oDiv.replaceChild(newNode3,oAtive)
	 </script>
</body>
</html>
```

### 4.动态操作样式

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>动态操作样式</title>
	<style type="text/css">
		.highLight{
			background-color: blue;
			color: red;
			width: 250px;
			height: 250px;
			text-align: center;
			line-height: 250px;
		}
	</style>
</head>
<body>
	<p id="box" class="highLight">鹿鼎记</p>
	<script type="text/javascript">
		// nodeObj.style
		var op = document.getElementById('box');、
		// 直接操作样式属性
		// console.log(op.style);
		// op.style.color = 'blue';
		// op.style.backgroundColor = 'red';
		// op.style.width = '250px';
		// op.style.height = '250px';
		// op.style.textAlign = 'center';
		// op.style.lineHeight = '250px';

		// 通过控制属性的类名来控制样式
		op.setAttribute('class','highLight');
	</script>
</body>
</html>
```

### 5.事件

事件三要素：

- 找到触发的事件对象
- 事件
- 事件处理程序

比如：我用手去按开关，灯亮了。

这件事情里，找到触发的事件对象是：手。事件是：按开关。事件处理程序是：灯的开和关。

总结：谁引发的后续事件，谁就是事件源。

**总结如下：**

- 事件源：引发后续事件的html标签。
- 事件：js已经定义好了
- 事件驱动程序：对样式和html的操作，也就是DOM

**代码书写步骤如下：**

- 获取事件源：`document.getElementById(“box”);`
- 绑定事件： 事件源box.事件onclick = function(){ 事件驱动程序 };
- 书写事件驱动程序：关于DOM的操作

**样式属性操作：**

所谓样式属性，就是对之前所讲解的style标签中的属性进行操作，并且通过js控制盒模型的属性（width,height等），控制盒子的显示隐藏（display:none|block）,控制盒子的颜色切换（background：red|green）等等。

操作文档对象，要遵循事件三步走：

- 获取事件源
- 事件
- 事件驱动程序

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>事件</title>
	<style type="text/css">
		#box{
			width: 100px;
			height: 100px;
			background-color: blue;
		}
	</style>
</head>
<body>
    <!--行内绑定-->
	<div id="box" onclick="add()"></div>
	<script type="text/javascript">
		var oDiv = document.getElementById('box');

		var isBlue = true;
        // 绑定事件的第一种方式
		oDiv.onclick = function(){
			// alert('事件被触发了');

			if (isBlue) {
				// this指向了当前的元素节点对象
				this.style.backgroundColor = 'red';
				isBlue = false;
			}else{
				this.style.backgroundColor = 'yellow';
				isBlue = true;
			}
		};

        //绑定事件的第二种方式
		// oDiv.onclick = add;
		// function add(){
		// 	alert('事件被触发了');
		// }
		
		// 一般使用这种方式（推荐使用这种）
		// var add = function(){
		// 	alert('事件被触发了');
		// }
	</script>
</body>
</html>
```

**鼠标事件：**

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>onmouseover()和onmouseout()事件</title>
	<style type="text/css">
		#box{
			width: 200px;
			height: 200px;
			background-color: red;
		}
	</style>
</head>
<body>
	<div id="box"></div>
	<script type="text/javascript">
		// 1.找开关	2.按一下	3.灯亮了

		// 1.找到触发的事件对象	2.事件	3.事件处理程序
        // 1.获取事件源
		var oDiv = document.getElementById('box');
		// 2.鼠标滑过事件
        // 2.绑定事件(悬停事件：鼠标进入到事件源中立即出发事件)
		oDiv.onmouseover = function(){
            // 3.书写事件驱动程序(修改src)
			this.style.backgroundColor = 'green';
		}
		// 3.鼠标移开事件
        // 2.绑定事件(悬停事件：鼠标进入到事件源中立即出发事件)
		oDiv.onmouseout = function(){
            // 3.书写事件驱动程序(修改src)
			this.style.backgroundColor = 'blue';
		}
	</script>
</body>
</html>
```

**表单控件上的事件：**

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>表单控件上的事件</title>
	<style type="text/css">
		.text{
			color: red;
			font-size: 10px;
		}
	</style>
</head>
<body>
	<form action="">
		<p class="name">
			<label for="username">用户名：</label>
			<input type="text" name="user" id="username">
			<span></span>
		</p>
		<p class="pwd">
			<label for="pwd">密码：</label>
			<input type="password" name="pwd" id="pwd">
		</p>
		<input type="submit" name="">
	</form>

	<script type="text/javascript">
        // 1.获取事件源(事件对象，在文档中一切的标签都是对象)
		var userName = document.getElementById('username');
        // 创建一个span标签
		var newNode = document.createElement('span');
        // 2.事件
		userName.onfocus = function(){
			console.log('请输入用户名');
             // 3.事件驱动程序  
			newNode.innerHTML = '请输入用户名';
            // 给span标签设置元素
			newNode.setAttribute('class','text');
			userName.parentNode.appendChild(newNode);
		}
		userName.onblur = function(){
			console.log('请输入正确的用户名');
			newNode.innerHTML = '请输入正确的用户名';
			newNode.setAttribute('class','text');
			userName.parentNode.appendChild(newNode);
		}
	</script>
</body>
</html>
```

**内容选中事件和改变事件：**

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>内容选中事件和内容改变事件</title>
</head>
<body>
	<textarea cols="30" rows="10">阿拉基分散发</textarea>
	<input type="text" name="" value="修改这里">
	<script type="text/javascript">
		var textArea = document.getElementsByTagName('textarea')[0];
		var inputObj = document.getElementsByTagName('input')[0];

		textArea.onselect = function(){
			console.log('内容被选中！');
		}
		inputObj.onchange = function(){
			console.log('内容被改变了！')
		}
		inputObj.oninput = function(){
			console.log('内容实时被改变了！');
			console.log(this.value);
		}

	</script>
</body>
</html>
```

**窗口事件：**

示例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>窗口加载事件</title>
	<script type="text/javascript">
		/*
	setTimeout(function(){
		var oDiv = document.getElementById('box');
		oDiv.onclick = function(){
		this.innerHTML = ('alex');
	}
},0)
*/
	// 等待文档元素加载完成之后才会调用onload()
	window.onload = function(){
		var oDiv = document.getElementById('box');
		oDiv.onclick = function(){
			this.innerHTML = 'alex';
		}
	}
	</script>
</head>
<body>
	<div id="box">夹杂史蒂夫</div>
</body>
</html>
```

