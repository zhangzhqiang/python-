# Day notes 41

## 今日内容

### 1.雪碧图技术

雪碧图的场景

- 静态图片，不随用户信息变化而变化
- 小图片，图片比较小(2-3kb)
- 加载量比较大
  - 一些大图不建议使用雪碧图

优点：

- 有效的减少了HTTP请求数量
- 加速内容显示

优点解释：

每请求一次，就会和服务器链接一次，建立链接需要额外的时间开销，采用雪碧图技术，减少了HTTP请求次数。

原理：

通过css的背景属性的background－position来控制雪碧图的显示。

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>css sprite雪碧图技术</title>
	<style type="text/css">
		div{
			width: 25px;
			height: 25px;
			display: inline-block;
			/*35 ＊ 895*/
			background: url('img/xbt.png') no-repeat 0 0;
			/*控制背景图大小*/
			background-size: 17.5px 447.5px;
		}
		.sprite{
			background-position: 0 0;
		}
		.sprite2{
			background-position: 0 -33px;
		}
		.sprite3{
			background-position: 0 -66px;
		}
		.sprite4{
			background-position: 0 -99px;
	</style>
</head>
<body>
	<div class="sprite"></div>
	<div class="sprite2"></div>
	<div class="sprite3"></div>
	<div class="sprite4"></div>
</body>
</html>
```

备注：测量好图片x，y轴的距离，通过background-position属性进行设置即可。

