# Day noets 37

## 今日内容

### CSS属性－1

- font-family 11

`font-family`可以把多个字体名称作为一个‘回退’系统来保存。意思就是如果浏览器不支持第一种字体，则会自动去尝试下一个字体，以此类推

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>字体属性</title>
	<style type="text/css">
		/*字体备选方案顺序依次*/
		body{
			font-family: "Hoefler Text","Arial";
		}
	</style>
</head>
<body>
	python 课程
</body>
</html>
```

如果设置成`inherit`，则表示继承父元素的字体

- font-size 11

设置字体大小

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>字体属性</title>
	<style type="text/css">
		body{
			font-size: 30px;
		}
	</style>
</head>
<body>
	python 课程
</body>
</html>
```

- color 11

设置字体颜色

支持三红颜色值：

- 颜色的名称，比如：red
- 设置rgb值，比如：rgb(255,255,255)

- 十六进制值，比如：#FF6700
- rgba中的a表示透明度，值在0-1之间，比如：rgba(255,0,0,.5)

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>字体属性</title>
	<style type="text/css">
		body{
			/*red，green，blue设置颜色*/
			color: rgb(255,255,0);
			/*a：表示透明度0-1之间的数*/
			color: rgba(255,0,0,.5);
			/*十六进制表示法*/
			color: #FF6700;
			/*颜色名称*/
			color: red;
		}
	</style>
</head>
<body>
	python 课程
</body>
</html>
```

- font-style

设置字体样式

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>字体属性</title>
	<style type="text/css">
		body{
			/*字体样式*/
			font-style: italic;
		}
	</style>
</head>
<body>
	python 课程
</body>
</html>
```

- font-weight 11

设置字体粗细

|   值    |                      描述                      |
| :-----: | :--------------------------------------------: |
| normal  |                默认值，标准粗细                |
|  bold   |                      粗体                      |
| bolder  |                      更粗                      |
| lighter |                      更细                      |
| 100~900 | 设置具体粗细，400等同于normal，而700等同于bold |
| inherit |             继承父元素字体的粗细值             |

示例：html

```html
<!DOCTYPE html>
<html>
<head>
	<title>字体属性</title>
	<style type="text/css">
		body{
			/*字体粗细取100-900之间的数*/
			font-weight: 900;
			/*粗体*/
			font-weight: bold;
			/*更粗*/
			font-weight: bolder;
			/*默认粗细，标准*/
			font-weight: normal;
			/*更细*/
			font-weight: lighter;
		}
	</style>
</head>
<body>
	python 课程
</body>
</html>
```

- line-height 11

设置行高

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性和字体属性示例</title>
	<style type="text/css">
		div{
			line-height: 70px;
		}
	</style>
</head>
<body>
	<div class="box">
		<a href="https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.11.4b1311d9qvNbqS&q=%E6%97%B6%E5%B0%9A%E5%A5%97%E8%A3%85&cat=16&style=grid&seller_type=taobao">
			休闲运动套装女夏2019新款时尚撞色宽松T恤束脚裤休闲显瘦两件套
		</a>
		<p>$ <span>655.00</span></p>

	</div>
	
</body>
</html>
```

- text-decoration 11

设置文本的修饰，下划线／上划线／删除线

|      值      |                 描述                  |
| :----------: | :-----------------------------------: |
|     none     |        默认。定义标准的文本。         |
|  underline   |         定义文本下的一条线。          |
|   overline   |         定义文本上的一条线。          |
| line-through |       定义穿过文本下的一条线。        |
|   inherit    | 继承父元素的text-decoration属性的值。 |

示例：html

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性和字体属性示例</title>
	<style type="text/css">
		.box span{
			/*删除线*/
			text-decoration: line-through;
			/*下划线*/
			text-decoration: underline;
			/*上划线*/
			text-decoration: overline;
			/*默认为标准文本*/
			text-decoration: none;
			/*继承父类元素的值*/
			text-decoration: inherit;
		}
	</style>
</head>
<body>
	<div class="box">
		<a href="https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.11.4b1311d9qvNbqS&q=%E6%97%B6%E5%B0%9A%E5%A5%97%E8%A3%85&cat=16&style=grid&seller_type=taobao">
			休闲运动套装女夏2019新款时尚撞色宽松T恤束脚裤休闲显瘦两件套
		</a>
		<p>$ <span>655.00</span></p>
	</div>
</body>
</html>
```

- text-index

设置文本缩进

示例：html

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－缩进</title>
	<!-- 文本缩进：px是一个绝对单位，你设置多少像素就会显示多少像素
		em是一个相对单位，相对当前字体大小进行缩进 -->
	<style type="text/css">
		p{
			text-indent: 2em;
			text-indent: 32px;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

- font

设置综合属性

示例：html

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－缩进</title>
	<style type="text/css">
		p{
		/*字体大小／行高/字体综合属性*/
    font: 20px/2 "Helvetica Neue",Helvetica,Arial,"Microsoft Yahei","Hiragino Sans GB","Heiti SC","WenQuanYi Micro Hei",sans-serif;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

- letter-spacing

设置文字之间的距离

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－缩进</title>
	<style type="text/css">
		p{
      /*调整文字之间的距离*/
			letter-spacing: 5px;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

- word-spacing

设置英文单词之间的距离

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－缩进</title>
	<style type="text/css">
		p{
      /*调整英文单词之间的距离*/
			word-spacing: 10px;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

- text-align  11

设置文本对齐

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－缩进</title>
	<style type="text/css">
		div{
			/*设置文本对齐center／right／left默认left*/
			text-align: center;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

对齐样式：

|   值    |      描述       |
| :-----: | :-------------: |
|  left   | 左边对齐 默认值 |
|  right  |     右对齐      |
| center  |    居中对齐     |
| justify |    两端对齐     |

注意：行高一定要大于字体大小，否则字体会大于行高页面显示不美观

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－缩进</title>
	<style type="text/css">
		div{
			/*注意⚠️：行高一定要大于字体大小*/
			line-height: 40px;
			font-size: 30px;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

#### 背景系列：

设置背景样式

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>文本属性－缩进</title>
	<style type="text/css">
		p{
			/*设置背景颜色*/
			background-color: red;
			/*设置背景图像*/
			background-image: url('img/1.png');
			/*设置背景图片尺寸*/
			background-size: 380px 860px;
			/*如何重复背景图像*/
			background-repeat: no-repeat;
			/*设置背景图像是否固定或者随着页面的其余部分滚动*/
			background-attachment: fixed;
			/*设置图像位置*/
			background-position: center;
		}
	</style>
</head>
<body>
	<p>
		hello world，美国人正费尽心思制造排外情绪。部分美国民众间歇性的本土主义情绪爆发，实在令人尴尬。当代美国人对这个世界本来就十分无知，再加上各种社交媒体和非主流小报胡乱揣测、臆想和制造幻觉，使问题更加严重。这些编造故事里的反派主角多半是中国，还有俄罗斯、伊朗和古巴等“邪恶国家”。按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了。但委内瑞拉没有资格成为美国的敌人。而身患“敌人缺乏综合征”的美国军工复合体却找到了解药——中国，所以才有了上述荒诞的故事。由于苏联出人意料地缴械投降，美国军工复合体不仅失去了“魔鬼般”的对手，也失去了财富来源。如今他们欣喜地看到了中国崛起，就像发现了新宝藏。
	</p>
	<div>
		按其说法，他们的影响力都已进入委内瑞拉这个距美国南海岸仅1600英里的“社会主义国家”了
	</div>
</body>
</html>
```

常用背景相关属性：

|         属性          |                       描述                       |
| :-------------------: | :----------------------------------------------: |
|   background-color    |              规定要使用的背景颜色。              |
|   background-image    |              规定要使用的背景图像。              |
|    background-size    |               规定背景图片的尺寸。               |
|   background-repeat   |              规定如何重复背景图像。              |
| background-attachment | 规定背景图像是否固定或者随着页面的其余部分滚动。 |
|  background-position  |               规定背景图像的位置。               |
|        inherit        |    规定应该从父元素继承background属性的设置。    |

`background-repeat`取值范围：

|    值     |                       描述                        |
| :-------: | :-----------------------------------------------: |
|  repeat   |    默认。背景图像将在垂直方向和水平方向重复。     |
| repeat-x  |            背景图像将在水平方向重复。             |
| repeat-y  |            背景图像将在垂直方向重复。             |
| no-repeat |              背景图像将仅显示一次。               |
|  inherit  | 规定应该从父元素继承background-repeat属性的设置。 |

`background-attachment`取值范围：

|   值    |                         描述                          |
| :-----: | :---------------------------------------------------: |
| scroll  |   默认值。背景图像会随着页面其余部分的滚动而移动。    |
|  fixed  |      当页面的其余部分滚动时，背景图像不会移动。       |
| inherit | 规定应该从父元素继承background-attachment属性的设置。 |

`background-position`取值范围：

|                              值                              |                             描述                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| top left  top center  top right  center left  center center  center right  bottom left  bottom center  bottom right | 如果只设置了一个关键词，那么第二个值就是"center"。 默认值：0% 0%。 |
|                            x% y%                             | 第一个值是水平位置，第二个值是垂直位置。 左上角是 0% 0%。右下角是 100% 100%。 如果只设置了一个值，另一个值就是50%。 |
|                          xpos ypos                           | 第一个值是水平位置，第二个值是垂直位置。 左上角是 0 0。单位是像素 (0px 0px) 或任何其他的 CSS 单位。 如果只设置了一个值，另一个值就是50%。 可以混合使用`%`和`position`值。 |

示例：html文件

```html
<!DOCTYPE html>
<html>
<head>
	<title>背景属性</title>
	<style type="text/css">
		.bg{
			width: 1200px;
			height: 1300px;
			border: 3px solid green;
			background-color: red;
			background-image: url('images/scholl_flower.jpeg');
			/*默认repeat*/  
      /*平铺方式:*/
			background-repeat:no-repeat; 
			/*背景定位: 综合写法*/
			/*background-position: 50px 100px;*/
			/*具体值：单个写法*/
			/*background-position-x: 100px;*/
			/*background-position-y: 200px; */

			/*关键字：top right center bottom left*/
			/*background-position: top center;*/

			/*百分比：0% 50% 100%*/
			/*计算规则：水平百分比的值＝容器宽度的百分比－背景图片宽度的百分比*/
			background-position: 50% 50%;
		}
	</style>
</head>
<body>
	<div class="bg">
		<p style="color: #fff;">这是一个八十年代的美女</p>
	</div>
</body>
</html>
```

小米案例：

```html
<!DOCTYPE html>
<html>
<head>
	<title>小米背景定位案例</title>
	<meta charset="utf-8">
	<style type="text/css" charset="utf-8">
		.bgi{
			width: 100%;
			height: 658px;
			/*综合写法*/
			background: url('img/mibg.png') no-repeat center top;

			/*单个写*/
			/*background-image: url('img/mibg.png');*/
			/*平铺方式*/
			/*background-repeat: no-repeat;*/
			/*图片定位*/
			/*background-position: center top;*/
		}
	</style>
</head>
<body>
	<div class="bgi"></div>
</body>
</html>
```

