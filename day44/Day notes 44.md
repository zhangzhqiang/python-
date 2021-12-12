# Day notes 44

## 今日内容

- BOM

### BOM简介

浏览器对象模型。

- 操作**浏览器部分功能**的API。比如让浏览器自动滚动。

BOM骨架图

![BOM](G:\homework\img\BOM.png)

- **window对象是BOM的顶层(核心)对象**，所有对象都是通过它延伸出来的，也可以称为window的子对象。
- DOM是BOM的一部分。

**window对象**

- window对象是JavaScript中的顶级对象
- 全局变量、自定义函数也是window对象的属性和方法
- window对象下的属性和方法调用时，可以省略window

**弹出系统对话框：**

```js
// 方式一
window.alert('Mjj');
// 方式二
var a = window.confirm('你确定要离开网站吗？')
console.log(a);
// 方式三
var b = window.prompt('请输入你早晨吃了什么？');
console.log(b);
```

**打开窗口、关闭窗口：**

```js
window.open('https://www.baidu.com/');
```

示例：

```js
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>

        <!--行间的js中的open() window不能省略-->
        <button onclick="window.open('https://www.baidu.com/')">百度一下</button>

        <button>打开百度</button>
        <button onclick="window.close()">关闭</button>
        <button>关闭</button>

    </body>
    <script type="text/javascript">

        var oBtn = document.getElementsByTagName('button')[1];
        var closeBtn = document.getElementsByTagName('button')[3];

        oBtn.onclick = function(){

            //打开空白页面
            open('https://www.baidu.com',"_self")
        }
        closeBtn.onclick = function(){
            if(confirm("是否关闭？")){
                close();
            }
        }
    </script>
</html>
```

**location对象**

location相当于浏览器地址栏，可以将url解析成独立的片段。

###### location对象的属性

- href：跳转
- hash：返回url中#后面的内容，包含#
- host：主机名，包括端口
- hostname：主机名
- pathname url：中的路径部分
- protocol：协议 一般是http、https
- search：查询字符串

示例：

```js
<!DOCTYPE html>
<html>
<head>
	<title>location对象</title>
</head>
<body>
	<form>
		<span>luffy</span>
	</form>
	<script type="text/javascript">
    var oSpan = document.getElementsByTagName("span")[0];
	oSpan.onclick = function () {
        location.href = "http://www.luffycity.com";   //点击span时，跳转到指定链接
    }
	</script>
</body>
</html>
```

**location对象**

示例：

```js
// 1. 2秒之后跳转到百度首页
setTimeout(function(){
    setTimeout(function(){
        // location.href = 'https://www.baidu.com';
        location.replace('https://www.baidu.com');
        location.reload();
    },2000)
})
```

**navigator对象**

window.navigator 的一些属性可以获取客户端的一些信息。

- userAgent：系统，浏览器

- platform：浏览器支持的系统，win/mac/linux

    ```javascript
    console.log(navigator.userAgent);
    console.log(navigator.platform);
    ```

**history对象**

1、后退：

- history.back()
- history.go(-1)：0是刷新

2、前进：

- history.forward()
- history.go(1)

用的不多。因为浏览器中已经自带了这些功能的按钮。