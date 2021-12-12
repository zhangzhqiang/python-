# Day notes 46

## 今日内容

- jQuery介绍

### 1.jQuery介绍

jQuery是一个快速，小巧，功能丰富的JavaScript库。它通过易于使用的API在大量浏览器中运行，使得HTML文档遍历和操作，事件处理，动画和Ajax更加简单。通过多功能性和可扩展性的结合，jQuery改变了数百万人编写JavaScript的方式。另外它只是封装了js的dom的操作和ajax，其它的未封装。所以js是包含jquery的。由此可见，jquery的出现，使我们更加容易操作DOM。

**核心思想：write less,do more 写的少 做的多**

#### 1.1 jQuery的作用

用js写代码的时候，会遇到一些问题：

- window.onload事件有事件覆盖的问题，因此只能写一个事件
- 代码容错性差
- 浏览器兼容性问题
- 书写复杂，代码量多，看上去比较乱
- 动画效果实现复杂

jQuery完美的解决了以上问题。学习jQuery就是学习怎么用jQuety操作DOM，学习jQuery封装好的功能接口。

#### 1.2 jQuery的特点

- 链式编程：调用方法时可以连起来写，比如`.show()`和`.html()`可以连写成`.show().html()`。
- 隐式迭代：隐式对应的是显式。隐式迭代的意思是：在方法的内部进行循环遍历，而不用我们自己再进行循环，简化我们的操作，方便我们调用。

**jQuery符号：**

- jQuery 使用 `$` 符号原因：书写简洁、相对于其他字符与众不同、容易被记住
- `$` 代表的就是jQuery

示例：

```javascript
  <script src="jquery-3.3.1.js"></script>
    <script>
        console.log($);
        console.log(jQuery);
        console.log($===jQuery);// True
    </script>
```

**jQuery参数：**

- jQuery 里面的 `$` 函数，根据传入参数的不同，进行不同的调用，实现不同的功能。返回的是jQuery对象。

- jQuery这个js库，除了`$` 之外，还提供了另外一个函数：jQuery。jQuery函数跟 `$` 函数的关系：`jQuery === $`。

示例：

```js
$(); // 调用上面我们自定义的函数$

$(document）.ready(function(){}); // 调用入口函数

$(function(){}); // 调用入口函数，简单写法

$("#btn") // 获取id属性为btnShow的元素

$("div") // 获取所有的div标签元素
```

**jQuery的第一个demo**

示例：

```html
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
    <button>操作</button>
    <div></div>
    <div></div>
    <div></div>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            // 获取dom元素
            var oBtn = $('button'); // 根据标签名获取元素
            var oDiv = $('div'); // 根据标签名获取元素
            oBtn.click(function(){
                oDiv.show(3000);// 显示盒子
                oDiv.html('赵云'); // 设置内容
            });// 事件是通过方法绑定的
        })
    </script>
</body>
</html>
```

#### 1.3 入口函数对比

**jQuery入口函数与js入口函数的区别**：

区别一：书写个数不同：

- Js 的入口函数只能出现一次，出现多次会存在事件覆盖的问题。
- jQuery 的入口函数，可以出现任意多次，并不存在事件覆盖问题。

区别二：执行时机不同：

- Js的入口函数是在所有的文件资源加载完成后，才执行。
    - 这些文件资源包括：页面文档、外部的js文件、外部的css文件、图片等。
- jQuery的入口函数，是在文档加载完成后，就执行。
    - 文档加载完成指的是：DOM树加载完成后，就可以操作DOM了，不用等到所有的外部资源都加载完成。

**文档加载的顺序：从上往下，边解析边执行。**

示例：js入口函数

```js
// 原生js的入口函数。页面上所有内容(文本，图片)加载完毕，才执行。
window.onload = function () {
    alert(1);
}
```

示例：jQuery入口函数

方式一：

```js
// 等待文档资源加载完成之后调用此方法
$(document).ready(function(){
    alert(1);
});
```

方式二：

```js
// 2.jquery简便写法入口函数
$(function(){
    alert(2);
});
```

方式三：

```js
$(window).ready(function(){
    // 表示文档，图片资源加载完成之后调用
    console.log(3);
});
$(window).ready(function(){
    // 表示文档，图片资源加载完成之后调用，而且不会覆盖
    console.log(4);
});
```

#### 1.4 js DOM对象和jQuery对象对比

通过 jQuery 获取的元素是一个**伪数组**，数组中包含着原生JS中的DOM对象

**区别：**

- 通过原生 js 获取这些元素节点的方式

示例：

```js
var myBox = document.getElementById("app");           //通过 id 获取单个元素
var boxArr = document.getElementsByClassName("box");  //通过 class 获取的是伪数组
var divArr = document.getElementsByTagName("div");    //通过标签获取的是伪数组
```

- 通过 jQuery 获取这些元素节点的方式

示例：

```js
//获取的是伪数组，里面包含着原生 JS 中的DOM对象
console.log($('#app'));// 通过 id 获取单个元素
console.log($('.box'));// 通过 class 获取的是伪数组
console.log($('div'));// 通过标签获取的是伪数组
```

**相互转换：**

- jQuery对象转为js DOM对象：

示例：

```js
$(function(){
    // 获取jquery对象
    console.log($('#box2'));

    // 获取js对象
    var oDiv2 = document.getElementById('box2');
    console.log(oDiv2);

    // jquery==>js对象
    console.log($('#box2')[0]);// 推荐使用这种
    console.log($('#box2').get(0));
});
```

- js DOM 对象 转为jQuery对象：

示例：

```js
$(function(){
    // 获取jquery对象
    console.log($('#box2'));

    // 获取js对象
    var oDiv2 = document.getElementById('box2');
    console.log(oDiv2);

    // js对象==>jquery对象 $(js对象)
    console.log($(oDiv2));
});
```

总结：

- 如果是jquery对象一定要调用jquery的属性和方法
- 如果是js对象一定要调用的是js的属性和方法

示例：

```js
// 入口函数
$(function(){
    // 事件三步走： 事件源  事件  事件驱动程序
    // jquery如何获取dom   
    // jquery的标签选择器
    console.log($('div'));
    // js对象
    // $('div')[0].onclick
    // jquery内部自己遍历 
    $('div').click(function(){
        // alert(1);
        // this指的是js对象
        console.log(this.innerText);
        console.log($(this).text())
        // $(this).hide(300);
    });
    // 2.类选择器
    console.log($('.box'))
    // 3.id选择器
    console.log($('#box'))
});
</script>
```

