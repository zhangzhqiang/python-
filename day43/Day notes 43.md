# Day notes 43

## 今日内容

- JavaScript

### 1.JavaScript简介

web前端有三层：

- HTML：从语义的角度，描述页面的结构（搭建框架）
- CSS：从审美的角度，描述样式（美化页面）
- JavaScript：从交互的角度，描述行为（提升用户体验）

**历史背景介绍**：

布兰登 艾奇 1995年在网景公司 发明的JavaScript

一开始的JavaScrip叫LiveScript

同一个时期 比如 VBScript,JScript等，但是后来被JavaScript打败了，**现在的浏览器只运行一种脚本语言叫JavaScript**

**JavaScrit的发展**：

**2003**年之前，JavaScript被认为“牛皮鲜”，用来制作页面上的广告，弹窗、漂浮的广告。什么东西让人烦，什么东西就是JavaScript开发的。所以浏览器就推出了屏蔽广告功能。

**2004**年，JavaScript命运开始改变，那一年，**谷歌公司开始带头使用Ajax技术**，Ajax技术就是JavaScript的一个应用。并且，那时候人们逐渐开始提升用户体验了。Ajax有一些应用场景。比如，当我们在百度搜索框搜文字时，输入框下方的智能提示，可以通过Ajax实现。比如，当我们注册网易邮箱时，能够及时发现用户名是否被占用，而不用调到另外一个页面。

**2007**年乔布斯发布了第一款iPhone，这一年开始，用户就多了上网的途径，就是用移动设备上网。**JavaScript在移动页面中，也是不可或缺的**。并且这一年，互联网开始标准化，按照W3C规则三层分离，JavaScript越来越被重视。

**2010**年，人们更加了解**HTML5技术**，**HTML5推出了一个东西叫做Canvas**（画布），工程师可以在Canvas上进行游戏制作，利用的就是JavaScript。

**2011**年，**Node.js诞生**，使JavaScript能够开发服务器程序了。

React-native inoic

如今，**WebApp**已经非常流行，就是用**网页技术开发手机应用**。手机系统有iOS、安卓。比如公司要开发一个“携程网”App，就需要招聘三队人马，比如iOS工程师10人，安卓工程师10人，前端工程师10人。共30人，开发成本大；而且如果要改版，要改3个版本。现在，假设公司都用web技术，用html+css+javascript技术就可以开发App。也易于迭代（网页一改变，所有的终端都变了）。

虽然目前WebApp在功能和性能上的体验远不如Native App，但是“WebApp慢慢取代Native App”很有可能是未来的趋势。

**JavaScrit的组成**：

- **ECMAScript 5.0**：定义了js的语法标准： 包含变量 、表达式、运算符、函数、if语句 for循环 while循环、内置的函数
- **DOM** ：操作网页上元素的API。比如让盒子显示隐藏、变色、动画 form表单验证
- **BOM**：操作浏览器部分功能的API。比如刷新页面、前进后退、让浏览器自动滚动

### 2.JS基础（ECMAScript 5.0）

#### 1.JS的引入方式

内接式与外接式：

示例：

```js
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>js文件的引入</title>
	<!-- 内部式：js -->
	<script type="text/javascript">
		// 编写js代码
		alert('弹出框');
		console.log('控制台');
	</script>
	<!-- 外接式：引入js文本，代码写在引入的文本中 -->
	<script type="text/javascript" src="js_code/index.js"></script>
</head>
<body>
</body>
</html>
```

#### 2.调试方法

- alert为浏览器弹出框。
- console为浏览器F12控制台。

#### 2.代码注释

单行注释与多行注释：

示例：

```js
// 快捷键:Ctrl + /
// 单行注释：注释单行代码

/*
多行注释：注释多行代码
*/
```

#### 3.变量

- 变量定义：var就是一个**关键字**，用var来定义变量，关键字后面一定要有空格隔开。
- 变量赋值：等号表示赋值，将等号右边的值，赋值给左边的变量。
- 变量名：变量名要见名知意。

变量命名规范：

- 必须使用字母、下划线、$构成。
- 不能使用js中关键字和保留字来命名
- 严格区分大小写
- 长变量名尽量写成驼峰或以下划线连接

示例：

```js
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>变量</title>
	<script type="text/javascript">
		// 初始化变量：声明+赋值
		var x = 30;
		//声明变量
		var y;
		// 变量赋值
		y = 50;
		var name = 'ike';
		/*命名规则:
		1.必须使用字母、下划线、$开始
		2.多个英文字母：驼峰式
		3.不能使用js中关键字和保留字来命名
		4.严格区分大小写
		*/
		var _a = 40;
		var $ = 60;
		var z = 20;
		z = 30;
		alert(z)
	</script>
</head>
<body>
</body>
</html>
```

#### 4.数据类型

##### 基本数据类型

- 数值类型：number

    - 如果一个变量中，存放了数字，这个变量就是数值类型

    示例：

    ```js
    var a = 3;  //定义了一个变量a，并且赋值100
    var b = 1.23;
    var c = -1;
    var d = 6 / 0; 
    // typeof：检查当前变量的数据类型
    alert(typeof a);
    alert(typeof b);
    console.log(d); //Infinity 无限大
    alert(typeof d); //number 类型
    # 在javascript中，只要是数，都是数值类型，不区分整数、浮点数、正数、负数
    ```

- 字符串类型：string

    - 用单引号或双引号引起来的字符或数字等类型，称为字符串

    示例：

    ```js
    var name = 'asdf12';
    var en = '123';
    alert(typeof name);
    alert(typeof en);
    // 字符串 + 数值 相当于字符串的拼接
    console.log('我'+'哎'+1);
    // 小技巧  将数值类型转换成字符串类型
    var c = 10+'';
    console.log(typeof c);
    ```

- 布尔类型：boolean

    - 判断True或False

    示例：

    ```js
    var isShow = 1 > 1;
    console.log(isShow)
    console.log(typeof isShow);
    ```

- 未定义：undefined

    示例：

    ```js
    var  d1;
    console.log(d1); //值 是undefined
    console.log(typeof d1); //undefined 数据类型 
    ```

- 空对象：null

    示例：

    ```js
    var d = null; //空对象 object
    console.log(typeof d);
    ```

##### 引用数据类型

- 函数：Function

- Object

- 数组：Arrary

    - 示例：

    ```js
    // 创建
    var shopping = ['aaa','bbb','ccc']
    // alert(shopping);
    // alert(typeof shopping)
    
    var rand = ['android', 'apple',['1','2','3']]
    console.log(rand)
    // 访问
    var item = rand[2];
    console.log(item)
    // 修改
    rand[0] = '榴莲';
    console.log(rand);
    
    //访问数组的长度
    console.log('数组的长度是：' + rand.length);
    ```

- 字符串：String

- 日期：Date

##### 运算符

赋值运算符：

以var x = 12，y=5来演示示例：

![js赋值运算符](G:\homework\img\js赋值运算符.png)

算数运算符：

var a = 5，b=2

![js算数运算符](G:\homework\img\js算数运算符.png)

比较运算符：

var x = 5；

![js比较运算符](G:\homework\img\js比较运算符.png)

注意：==比较的是值的相同，===比较的是值和数据类型（内存地址）

示例：

```js
var x = 5;
var y = '5';

// == 比较的是值的相同
// === 等同于  比较的是值和数据类型（内存地址）
console.log(x==y) //true
console.log(typeof x)//number
console.log(typeof y)//sting
console.log(x===y)//false
```

示例：a++与++a

```js

//  先将a的值赋值给b输出，然后再对a++ a此时是6
var a = 5;
var b = a++;
console.log(a); //6
console.log(b); //5
```

```js
// 先a++ 将a输出 在将输出的值赋值给b
var a = 5;
var b = ++a;
console.log(a); //6
console.log(b);//6
```

##### 数据类型的转换

**1.将number类型转换成string类型：**

隐式转换：

示例：

```js
// 隐式转换
var num = 1346.768;
console.log(''+num);
console.log(''.concat(num));
```

强制转换：

示例：

```js
// 强制类型转换
var num = 1346.768;
console.log(num.toString());
console.log(typeof num.toString());
console.log(String(num));
console.log(num.toFixed(2));
```

**2.将string类型转换成number类型：**

示例：

```js
var str = '131313.9254136';
// 字符串转换整型
console.log(parseInt(str));
// 字符串转换浮点型
console.log(parseFloat(str));
console.log(typeof parseFloat(str));
```

示例：NaN

```js
// NaN
var str1 = '1313.stssgg985'
console.log(Number(str1));// NaN Not a Number 是一个number类型
console.log(isNaN(str1));// 判断是否NaN
```

**3.解析字符串，并且返回整数和浮点型：**

示例：

```js
// parseInt() parseFloat() 解析字符串，并且返回整数和浮点型
console.log(parseInt(stringNum2));//13
console.log(parseFloat(stringNum2));//13.1313
```

#### 5.流程控制

**if：**

示例：

```js
var age = 20;
if(age > 18){
    // {}作为当前的作用域
    console.log('打印的内容');
}
console.log(22222); //这行代码照样执行
```

**if..else：**

示例：

```js
var age = 16;
if(age > 18){
    // {}作为当前的作用域
    console.log('打印的内容');
}else{
    console.log('好好学前端');
}
console.log(22222); //代码照样执行
```

**if..else if..else：**

示例：

```js
var age = 1313;
if (age == 18) {
    //{}相当于作用域
    console.log('打印的内容');
} else if (age == 30) {
    console.log('好好学前端');
} else {
    console.log('随便你了')
}
console.log('alex'); //下面的代码照样执行
```

**逻辑&&与：**必须两个条件都成立才算成立

示例：

```js
var sum = 401;
var math = 90;
if(sum>400 && math>=90){
console.log('清华大学录入成功')
}else{
alert('高考失利')
}
```

**逻辑||或：**有一个条件成立就算成立

示例：

```js
var sum = 400;
var math = 90;
if(sum>400 || math>=90){
    console.log('清华大学录入成功')
}else{
    alert('高考失利')
}
```

**三元运算：**

示例：

```js
var isres = 1 >2 ? '真的' : '假的';
alert(isres);
```

**for循环：**

示例：for循环遍历列表是最常用的对数据的操作

```js
//输出1~10之间的数
for(var i = 1;i<=10;i++){
     console.log(i)
 }
```

练习：输入1~100之间所有数之和

```js
var sum = 0;
for (var j = 1; j <= 100; j++) {
	sum += j
}
console.log(sum);
```

**break和continue：**

示例：

```js
var sum = 0;
for (var i = 1; i<=10;i++) {
    if (i === 8) {
        // break;//跳出当前循环
        continue;//跳过这次循环，进行下一次循环
    }
    sum +=1
}
console.log(sum)
```

**switch：**

示例：

```js
// switch语句 case表示一个条件，满足这个条件就会输出，直到遇到break跳出，如果你的breakb不写，那么程序会遇到下一个break停止。这个就是‘case穿透’
var gameScore = 'good';
switch (gameScore) {
    case 'good':
    	console.log('玩的很好');
    	break;
    case 'better':
    	console.log('玩的老牛逼');
    	break;
    case 'best':
    	console.log('恭喜你，吃鸡成功');
    	break;
    default:
    	console.log('很遗憾，被淘汰了');
    	break;
}
```

**while循环：**

循环三部曲：

- 初始化循环变量
- 判断循环条件
- 更新循环变量

示例：

```js
// 例子：打印 1~9之间的数
var i = 1; //初始化循环变量

while(i<=9){ //判断循环条件
    console.log(i);
    i = i+1; //更新循环条件
}
```

**do..while循环：**

示例：先做一次，再循环

```js
//不管有没有满足while中的条件do里面的代码都会走一次
var i = 3;//初始化循环变量
do{
    console.log(i)
    i++;//更新循环条件

}while (i<10) //判断循环条件
```

#### 6.函数

函数：就是把将一些语句进行封装，然后通过调用的形式，执行这些语句。

函数的作用：

- 解决大量的重复性的语句
- 简化编程，让编程模块化

示例：

```js
//声明
function 做饭(isBad){//形参
    if (isBad) {
        alert('点外卖')
    }else{
        alert('做饭了')
    }
}
var bad = true;	
//调用
做饭(bad);
做饭();
```

代码解释：

- function：是一个关键字。中文是“函数”、“功能”。
- 函数名字：命名规定和变量的命名规定一样。只能是字母、数字、下划线、美元符号，不能以数字开头。
- 参数：后面有一对小括号，里面是放参数用的。
- 大括号里面，是这个函数的语句。

**返回值:**

示例：

```js
// 函数表达式
var addition = function(a,b){
return a + b;
}
function subtraction(a,b){
return a - b;
}
function multiplication(a,b){
return a * b;
}
function division(a,b){
return a / b;
}

var r1 = addition(3,2);
var r2 = subtraction(3,2);
var r3 = multiplication(3,2);
var r4 = division(3,2);

console.log(r1);
console.log(r2);
console.log(r3);
console.log(r4);
```

**函数作用域：**

示例：

```js
<script type="text/javascript">
    var a = 1;//全局作用域
console.log(a);
function add(){
    var b=3;、、//局部作用域
    console.log(a);
}	
add();

</script>
```

**全局污染：**

示例：

```js
<script type="text/javascript" src="js_code/first.js"></script>
<script type="text/javascript" src="js_code/second.js"></script>
<script type="text/javascript">
    first();
second();
</script>
```

first.js

示例：

```js
(function(){
	var name = 'aaa';
	var hello = function(){
		alert('hello'+name);
	}
	window.first = hello;
})()
```

second.js

示例：

```js
(function(){
	var name = 'bbb';
	var hello = function(){
		alert('hello'+name);
	}
	window.second = hello;
})()
```

**对象object**

示例：

```js
var person={
    name:'ike',
    age:18,
    sex:'male',
    fav:function(a){
        alert('睡觉');
        return '舒服'+a
    }
}
console.log(person);
console.log(person.name)
console.log(person.fav(88))
```

#### 7.常用内置函数

##### 数组的操作方法

示例：升序

```js
var values = [1,15,16,18,2,3]
function compare(a,b){
    // if (a < b) {
    // 	return -1;
    // }else if (a > b){
    // 	return 1;
    // }else{
    // 	return 0;
    // }
    return a - b;  //简写
}
values.sort(compare);//升序
console.log(values);
```

示例：降序

```js
var values = [1,15,16,18,2.3]
function compare1(a,b){
    // if (a < b) {
    // 	return 1;
    // }else if (a > b){
    // 	return -1;
    // }else{
    // 	return 0;
    // }

    return b - a;//简写
}
values.sort(compare1);//降序
console.log(values);
```

示例：concat()数组合并

```js
// 1.concat()数组合并
var colors = ['red','blue']
var newColors = colors.concat('green');
newColors = newColors.concat({name:'ike'});
console.log(newColors);

var newcolors = colors.concat({name:'yellow'},['black','pink'])
console.log(newcolors);
```

示例：slice()返回数组的一段记录，顾头不顾尾

```js
// 2.slice()切片
newcolors = newcolors.slice(1,4);
console.log(newcolors)
```

示例：splice()

```js
// 3.splice() 删除、插入、替换
var names = ['张三','李四','王五','赵柳'];
// 删除前两个数，从0开始，顾头不顾尾
names.splice(1,2);
console.log(names);
// 插入:在一个不删任何元素进行插入
// names.splice(1,0,'aaa','bbb');
// console.log(names)
// 替换：替换李四
names.splice(1,1,'你哈o');
console.log(names)
```

示例：pop()移除数组的最后一个元素

```js
var arr = ['张三','李四','王文','赵六'];
arr.pop();
console.log(arr);//["张三", "李四"，"王文"]
```

示例：push() 向数组最后添加一个元素

```js
var arr = ['张三','李四','王文','赵六'];
arr.push('小马哥');
console.log(arr);//["张三", "李四"，"王文"，"赵六"，"小马哥"]
```

示例：shift()移除数组的第一个元素

```js
var arr = ['张三','李四','王文','赵六'];
var first = arr.shift()
console.log(arr)
```

示例：unshift()向数组第第一个元素添加

```js
var arr = ['张三','李四','王文','赵六'];
var first = arr.unshift()
console.log(arr)
```

示例：indexOf lastIndexOf查找索引

```js
// 位置查询：indexOf正序  lastIndexOf倒序
var names = ['张三','mjj','王五','mjj','赵丽'];
alert(names.indexOf('mjj'));//1
alert(names.lastIndexOf('mjj'));//3
alert(names.indexOf('mjj',2));//3
alert(names.lastIndexOf('mjj',2));//1
alert(names.lastIndexOf('mjjsss',2));//-1
```

示例：reverse() 翻转数组

```js
var names = ['alex','xiaoma','tanhuang','angle'];
//4.反转数组
names.reverse();
console.log(names);
```

示例：join() 将数组中元素使用指定的字符串连接起来，它会形成一个新的字符串

```js
var score = [98,78,76,100,0];
var str = score.join('|');
console.log(str);//"98|78|76|100|0"
```

示例：sort对数组排序

```js
var names = ['alex','xiaoma','tanhuang','abngel'];
names.sort();
console.log(names)；// ["alex", "angle", "tanhuang", "xiaoma"]
```

示例：判断是否为数组：isArray()

```js
 布尔类型值 = Array.isArray(被检测的值) ;
```

示例：filter()

```js
var number = [1,2,3,6,5,4,19,4,20];
var filterresult = number.filter(function(item,index,array){
    console.log('item:'+item);
    console.log('index:'+index);
    console.log('array'+array);
})
```

示例：map()

```js
var number = [1,2,3,6,5,4,19,4,20];
var mapresult = number.map(function(item,index,array){
    return item*2;
})
console.log(mapresult);
```

示例：map练习

```js
var oldArray=[
    {
        name:'aaa',
        age:17
    },
    {
        name:'bbb',
        age:18
    },
    {
        name:'ccc',
        age:27
    }
];
// 方式一：
// var newName=[];
// var newAge=[];
// for (var i=0;i<oldArray.length;i++) {
// 	var myname = oldArray[i].name;
// 	var myage = oldArray[i].age;
// 	newName.push(myname);
// 	newAge.push(myage);
// }
// console.log(newName);
// console.log(newAge)

// 方式二：
var newName = oldArray.map(function(item,index){
    return item.name
})

var newAge = oldArray.map(function(item,index){
    return item.age
})

console.log(newName);
console.log(newAge)
```

示例：for循环遍历

```js
var number = [1,2,3,6,5,4,19,4,20];
for (var i = 0; i < number.length; i++) {
    console.log(mapresult[i]);
}
```

示例：forEach循环遍历

```js
var number = [1,2,3,6,5,4,19,4,20];
number.forEach(function(item,index,array){
    console.log(item)
})
```

##### Date日期对象

示例：

```js
// UTC 1970.1.1 到 285616年
// Date日期对象
var now = new Date();
console.log(now)
// 指定参数
var xmas = new Date('December 25,1995 13:00:30');
console.log(xmas)
var xmas = new Date(1995,11,25);
console.log(xmas)
var xmas = new Date(1995,11,25,14,25,0);
console.log(xmas)
```

示例：获取时间

```js
var now = new Date();
// 常用方法
console.log(now.getDate());// 获取月份的第几天
console.log(now.getMonth());// 获取当前月份要加1
console.log(now.getFullYear());// 获取年
console.log(now.getDay());// 获取天 0代表周日
console.log(now.getHours());// 获取小时
console.log(now.getMinutes());// 获取分钟
console.log(now.getSeconds());// 获取小时
```

示例：日期格式化

```js
var now = new Date();
console.log(now.toDateString());// 星期 月 日 年
console.log(now.toTimeString());//时 分 秒 时区
// 常用方法
console.log(now.toLocaleDateString());//2019/8/16
console.log(now.toLocaleTimeString());//上午9:51:29
console.log(now.toLocaleString());//2019/8/16 上午9:53:37
console.log(now.toUTCString());//Fri, 16 Aug 2019 01:52:34 GMT
```

示例：数字时钟格式的时间

```js
function nowNumTime(){
    var now = new Date();
    var hour = now.getHours();
    var minute = now.getMinutes();
    var second = now.getSeconds();

    var temp = '' + (hour > 12 ? hour - 12 : hour);
    if (hour === 0) {
        temp = '12';
    }
    temp = temp+(minute < 10 ? ':0':":")+ minute;
    temp = temp+(second < 10 ? ':0':":")+ second;
    temp = temp+(hour >= 12? ' P.M':" A.M");
    console.log(temp);
    return temp;
}
var nownum = nowNumTime();
console.log(nownum)
```

##### Math对象

示例：

```js
console.log(Math.E);// 2.718281828459045
console.log(Math.LN10);// 2.302585092994046
console.log(Math.LN2);// 0.6931471805599453
console.log(Math.PI);// 3.141592653589793
console.log(Math.SQRT2);// 1.4142135623730951
```

示例：max()、min()方法

```js
var arr = [1,2,3,6,52,41,89];
var max = Math.max.apply(null,arr);
var min = Math.min.apply(null,arr);
console.log(max);
console.log(min);
```

示例：关于小数位数的问题

```js
var num = 24.3;
console.log(Math.ceil(num));// 天花板函数
console.log(Math.floor(num));// 地板函数
console.log(Math.round(num));// 标准的四舍五入函数
```

示例：随机数

```js
// 随机数 random()    0 <= random <1
console.log(Math.random());
```

练习：获取min到max之间的整数(1-100)

```js
// 1.获取min到max之间的整数(1-100)
function rand(max,min){
    return Math.floor(Math.random()*((max-min)+min));
}
var val = rand(100,1);
console.log(val);
```

练习：

```js
// 1.获取min到max之间的整数(1-100)
function rand(max,min){
    return Math.floor(Math.random()*(max-min)+min);
}
// 2.获取随机颜色 rgb(0~255,0~255,0~255)
function randomColor(){
    var r = rand(0,256),g = rand(0,256),b = rand(0,256);
    // 模板字符串  Tab键上边的按钮
    var result = `rgb(${r},${g},${b})`;
    return result;
}
var rc = randomColor();
console.log(rc);
document.body.style.backgroundColor = rc;
// 3.随机验证码 四位 数字+字母(大写)
function creatCode(){
    // 设置默认的空的字符串
    var code = '';
    var codeLength = 4;
    var randomCode = [0,1,2,3,4,5,6,7,8,9,'A','V','G','H','J','I','K','O','L','P']
    for (var i = 0; i < codeLength; i++) {
        // 设置随机范围0~20
        var index = rand(0,20);
        code += randomCode[index];
    }
    return code;
}
var rancode = creatCode();
console.log(rancode);
document.write(`<h1>${rancode}</h1>`);
```



#### 8.字符串的操作方法

示例：chartAt() 返回指定索引的位置的字符

```javascript
var str = 'hello world';
console.log(str.charAt(1));//获取指定的字符
```

示例：concat 返回字符串值，表示两个或多个字符串的拼接

```javascript
console.log(str.concat('你好','ike'));//拼接字符串
```

示例：replace(a,b) 将字符串a替换成字符串b

```javascript
var a = '1234567755';
var newStr = a.replace("4567","****");
console.log(newStr);//123****755
```

示例：indexof() lastIndexOf() 查找字符的下标，如果找到返回字符串的下标，找不到则返回-1

```javascript
var str = 'hello world';
console.log(str.indexOf('o'));//4
console.log(str.lastIndexOf('o'));//7
console.log(str.indexOf('o',6));//7
console.log(str.lastIndexOf('o',6));//4
```

示例：切片

```javascript
var str = 'hello world';
console.log(str.substring(2))
console.log(str.slice(2));
// 第一个参数是起始的位置，第二个参数是结束的位置，顾头不顾尾
console.log(str.slice(2,4));
console.log(str.substring(2,6))

```

示例：split('a',1) 以字符串a分割字符串，并返回新的数组。如果第二个参数没写，表示返回整个数组，如果定义了个数，则返回数组的最大长度

```javascript
var  str =  '我的天呢,a是嘛,你在说什么呢?a哈哈哈';
console.log(str.split('a'));//["我的天呢,", "是嘛,你在说什么呢?", "哈哈哈"]
```

示例：substr(statr,end) 左闭右开

```javascript
var str = 'hello world';
console.log(str.substr(2));
// 第二个参数是返回的字符数
console.log(str.substr(2,4));
```

示例：toLowerCase()转小写

```javascript
var str1 = 'HELLO WORLD';
console.log(str1.toLowerCase());
```

示例：toUpperCase()转大写

```javascript
var str = 'hEllo world';
console.log(str.toUpperCase());
```

示例：length获取字符串长度，拼接字符串

```js
str = 'hEllo world';
console.log(str.length);//获取字符串的长度
```

示例：trim()清空空格

```js
var str = '     hello world   ';
console.log(str);
console.log(str.trim());//清楚前后空格
```

示例：字符串练习

```js
//查找当前字符e在字符串中的所有位置
var str = 'He unfolded the map and set it on the floor.';
var arr = [];
var pos = str.indexOf('e');
console.log(pos);
while(pos > -1){
    // 找到当前e字符对应的位置
    arr.push(pos);
    pos = str.indexOf('e', pos+1)
}
console.log(arr)
```

特别：

```javascript
//1.将number类型转换成字符串类型
var num = 132.32522;
var numStr = num.toString()
console.log(typeof numStr)
//四舍五入
var newNum = num.toFixed(2)
console.log(newNum)
```

#### 10.globle对象的编码和解码

示例：编码

```js
// URI 通用资源标识符
var uri = 'http://www.baidu.cn/web index.html?name=ike';
// encodeURI只能识别空格，其他特殊字符不能识别
console.log(encodeURI(uri))
// encodeURIComponent编码使用最多的方法
console.log(encodeURIComponent(uri));
```

示例：解码

```js
var uri1 = 'http%3A%2F%2Fwww.baidu.cn%2Fweb%20index.html%3Fname%3Dike';
// 只能解析空格
console.log(decodeURI(uri1));// http%3A%2F%2Fwww.baidu.cn%2Fweb index.html%3Fname%3Dike
// 特殊符号都能解析
console.log(decodeURIComponent(uri1));// http://www.baidu.cn/web index.html?name=
```

#### 11.window对象

示例：

```js
// window对象相对于globle对象，全局的数据类型都挂载到window
var a = 3;
console.log(window.a);
function hello(){
    alert(window.a);
}
window.hello();
```

