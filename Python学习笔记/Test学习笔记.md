# 测试学习笔记

## 第一章 Pytest相关

### 1.1 自动化测试框架简介

- unitest
- pytest
- robotframework

前两个框架主要运用在白盒单元测试，而robotframework主要运用在系统测试，pytest也可以用来做系统测试的自动化。

主要特点有：

- 用python编写测试用例，操作简单易上手
- 可以用文件系统目录层次对应手工测试用例层次结构
- 具有灵活的初始化清除机制
- 利用第三方插件可以生成高大上的测试报告

Pytest的功能很多，持续更新中

### 1.2 环境安装

终端执行安装pytest命令：

```python
pip3 install pytest
```

pytest是借助pytest-html插件生成测试测试报告， 不用自己编写生成报告代码，如下：

安装测试报告(pytest-html)命令：

```python
pip3 install pytest-html
```

生成测试报告：

```python
pytest trademark --html=report.html --self-contained-html
```

这个工具有个bug，测试目录、文件、类名如果有中文会显示乱码，修改site-packages\pytest_html\plugin.py代码

```python
 class TestResult:
      def __init__(self, outcome, report, logfile, config):
          self.test_id = report.nodeid.encode("utf-8").decode("unicode_escape")
 # 改为
 class TestResult:
 	def __init__(self, outcome, report, logfile, config):
 	# self.test_id = report.nodeid.encode("utf-8").decode("unicode_escape")
 	self.test_id = report.nodeid
```

使用allure2生成测试报告，生成的炫酷的测试报告，这是一个report框架，支持各种语言，也可以集成到Jenkins上。

安装allure：

```python
# https://github.com/allure-framework/allure2/releases
1.下载完后解压项目跟目录
2.也可以解压到自己习惯的目录下，把allure-2.10.0\bin目录添加到环境变量，目的是可以在任意位置执行bin目录下allure.bat脚本
```

安装pytest-allure-adaptor插件：

```python
pip3 install allure-pytest
```

生成xml格式的报告：

```python
pytest -sv --alluredir ./report  # (把目录放到当前目录下的report文件夹，也可以自己指定位置，根据个人习惯)
```

接着执行如下命令：

```python
allure generate report/ -o report/html
```

注：第一个report指的是生成xml格式的路径，后边的report可以自己指定在哪个目录生成html报告。

### 1.3 测试用例代码

首先，我们编写的测试用例代码文件， 必须以 `test_` 开头，或者以 `_test` 结尾，比如，我们创建一个 文件名为 `test_登录错误.py` ，放在目录 `trademark\trademark_case\申请商标` 下面。

其中 trademark是我们创建的自动化项目根目录。

代码如下：

```python
class Test_Apply:
    def test_apply001(self):
        print('用例apply001')
        assert 1 == 1

    def test_apply002(self):
        print('用例apply002')
        assert 2 == 2

    def test_apply003(self):
        print('用例apply003')
        assert 3 == 2
```

注：如果我们把测试用例存放在类中， 类名必须以 `Test` 为前缀的 `类` ，用例对应的方法必须以 `test` 为前缀的方法。

pytest 中用例的检查点 直接用 Python 的 assert 断言。

assert 后面的表达式结果为True，就是检查点通过，结果为False，就是检查点不通过。

### 1.4 执行测试用例

在终端cd到自己的根目录下，执行pytest即可。

 ![image](J:\homework\Python学习笔记\Test学习笔记.assets\tut_20200626162633_92.png) 

执行结果：显示找到3个测试项，2个执行通过，1个不通过。通过的用例是用一个绿色小点表示，不通过的用例用一个红色的F表示，并且会在后面显示具体不通过的用例和不通过的检查点，代码细节。

可以发现，用例代码中有些打印语句没有显示出内容。因为pytest 会 截获print打印的内容。如果我们希望显示测试代码中print的内容，因为这些打印语句在调试代码时很有用，可以加上命令行参数 -s 

如下：

```python
pytest -s
```

如果我们希望得到更详细的执行信息，包括每个测试类、测试函数的名字，可以加上参数 -v，这个参数可以和 -s 合并为 -sv，如下：

```python
pytest -sv
```

执行pytest时，如果命令行没有指定目标目录或者文件，他会自动搜索当前目录下所有符合条件的文件、类、函数。所以上边，就找到了3个测试方法，对应3个用例。我们目前项目根目录只有一个trademark_case目录用例存放测试用例，随着业务的增加，将来会有更多的目录，为了我们执行测试用例更灵活，防止pytest到其他目录中找测试用例，执行测试时，我们可以在命令行加上目标目录trademark_case，如下：

```python
pytest trademark_case -sv
```

### 1.5 初始化清除

#### 1.5.1 模块级别

模块级别的初始化、清除分别在整个模块的测试用例执行前后执行，并且只执行一次

定义setup_module和treardown_module全局函数，如下：

```python
# trademark_case.py
def setup_module():
	print('--初始化模块module--')
def teardown_module():
	print(--清除模块module--')
	
class Test_商标申请:
	def test_apply001(self):
		print('--用例apply001--')
		assert 1==1
	def test_apply002(self):
		print('--用例apply002--')
		assert 2==2
	def test_apply003(self):
		print('--用例apply003--')
		assert 3==2
		
class Test_商标申请2:
	def test_apply011(self):
		print('--用例apply011--')
		assert 1==1
	def test_apply012(self):
		print('--用例apply012--')
		assert 2==2
```

执行命令结果：

pytest trademark_case -s

```python
'''
trademark_case\申请商标\test_申请商标.py
--初始化模块module--
--用例apply001--
.--用例apply002--
.--用例apply003--
F--用例apply011--
.--用例apply012--
.--清除模块module - -
'''
```

#### 1.5.2 类级别

类级别的初始化、清除 分别 在整个类的测试用例 执行前后执行，并且只会执行1次

如下定义 setup_class 和 teardown_class 类方法

```python
# cases.py
def setup_module():
    print('\n *** 初始化-模块 ***')

def teardown_module():
    print('\n *** 清除-模块 ***')

class Test_错误密码:

    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')

    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')
        
    def test_C001001(self):
        print('\n用例C001001')
        assert 1 == 1
        
    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2
        
    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2

class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
        
    def test_C001022(self):
        print('\n用例C001022')
        assert 2 == 2
```

 执行命令 `pytest cases -s` ，运行结果如下 

```python
collected 5 items

cases\登录\test_错误登录.py
 *** 初始化-模块 ***

 === 初始化-类 ===

用例C001001
.
用例C001002
.
用例C001003
F
 === 清除 - 类 ===

用例C001021
.
用例C001022
.
 ***   清除-模块 ***
```

可以发现，类级别的初始化、清除 在 整个模块所有用例 执行前后 分别 `执行1次` 。

它主要是用来为该 `类` 中的所有测试用例做 `公共的` 初始化 和 清除

#### 1.5.3 方法级别

方法级别 的初始化、清除 分别 在类的 每个测试方法 执行前后执行，并且 `每个用例分别执行1次`

如下定义 setup_method 和 teardown_method 实例方法

```python
# cases.py
def setup_module():
    print('\n *** 初始化-模块 ***')

def teardown_module():
    print('\n ***   清除-模块 ***')

class Test_错误密码:

    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')

    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')
        
    def setup_method(self):
        print('\n --- 初始化-方法  ---')

    def teardown_method(self):
        print('\n --- 清除  -方法 ---')
        
    def test_C001001(self):
        print('\n用例C001001')
        assert 1 == 1
        
    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2
        
    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2

class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
        
    def test_C001022(self):
        print('\n用例C001022')
        assert 2 == 2
```

 执行命令 `pytest cases -s` ，运行结果如下 

```python
collected 5 items

cases\登录\test_错误登录.py
 *** 初始化-模块 ***

 === 初始化-类 ===

 --- 初始化-方法  ---

用例C001001
.
 --- 清除  -方法 ---

 --- 初始化-方法  ---

用例C001002
.
 --- 清除  -方法 ---

 --- 初始化-方法  ---

用例C001003
F
 --- 清除  -方法 ---

 === 清除 - 类 ===

用例C001021
.
用例C001022
.
 ***   清除-模块 ***
```

可以发现，方法级别的初始化、清除 在 整个模块所有用例 执行前后 分别 `执行一次` 

#### 1.5.4 目录级别

目标级别的 初始化清除，就是针对整个目录执行的初始化、清除。

我们在需要初始化的目录下面创建 一个名为 `conftest.py` 的文件，里面内容如下所示

```python
import pytest 

@pytest.fixture(scope='package',autouse=True)
def st_emptyEnv():
    print(f'\n#### 初始化-目录甲')
    yield
    
    print(f'\n#### 清除-目录甲')
```

<font color="red">**注意：这里清除环境的代码就是 yield 之后的代码。 这是一个生成器，具体的说明参见视频讲解。**</font>

我们可以在多个目录下面放置这样的文件，定义该目录的初始化清除。

pytest 在执行测试时，会层层调用。

但是我发现了pytest一个重要的bug： 清除操作并不一定会在该目录最后一个测试用例执行完进行调用。

我已经在github上给pytest 的开发人员提交了bug report， [点击这里查看](https://github.com/pytest-dev/pytest/issues/7416) 

在我看来，这个问题是非常大的。

因为，一个目录下的用例执行完后，该清除的数据没有清除，这可能会导致其他目录下的用例执行失败。

所以在这个问题解决前，白月黑羽推荐大家先不要使用这种 目录级别 的初始化清除。

### 1.6 挑选用例执行

pytest可以灵活的挑选测试用例执行

**1. 指定一个模块**

可以像这样只挑选一个模块执行 

```python
pytest cases\登录\test_错误登录.py
```

**2. 指定目录**

 可以像这样只挑选一个目录执行 

```python
pytest cases
```

 也可以指定多个目录 

```python
pytest cases1  cases2\登录
```

**3. 指定模块里面的函数或类**

指定一个类

```python
pytest cases\登录\test_错误登录.py::Test_错误密码
```

也可以指定类里面的方法 

```python
pytest cases\登录\test_错误登录.py::Test_错误密码::test_C001001
```

**4. 根据名字**

可以使用 命令行参数 -k 后面加名字来挑选要执行的测试项

比如像这样后面跟测试函数名字的一部分：

```python
pytest -k C001001 -s
```

注意，-k 后面的名字

- 可以是测试函数的名字，可以是类的名字，可以是模块文件名，可以是目录的名字

- 是大小写敏感的

- 不一定要完整，只要能有部分匹配上就行

- 可以用 not 表示选择名字中不包含，比如

  ```python
  pytest -k "not C001001" -s
  ```

-  可以用 and 表示选择名字同时包含多个关键字，比如 

  ```python
  pytest -k "错 and 密码2" -s
  ```

-  可以用 or 表示选择名字 包含指定关键字之一即可，比如 

  ```python
  pytest -k "错 or 密码2" -s
  ```

**5. 根据标签**

可以这样给 某个方法加上标签 webtest 

```python
import pytest

class Test_错误密码2:

    @pytest.mark.webtest
    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
```

然后，可以这样运行指定标签的用例 

```python
pytest cases -m webtest -s
```

也可以这样给整个类加上标签 

```python
@pytest.mark.webtest
class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
```

 当然标签也支持中文 

```python
@pytest.mark.网页测试
class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
```

然后，运行命令行指定的标签

```python
pytest cases -m 网页测试 -s
```

 可以这样同时添加多个标签 

```python
@pytest.mark.网页测试
@pytest.mark.登录测试
class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 
```

 可以这样定义一个全局变量 pytestmark 为 `整个模块文件` 设定标签 

```python
import pytest
pytestmark = pytest.mark.网页测试
```

 如果你需要定义多个标签，可以定义一个列表

```python
import pytest
pytestmark = [pytest.mark.网页测试, pytest.mark.登录测试]
```

---

## 第二章 移动端相关

### 2.1 adb命令大全

由于adb命令实在太多,网上搜索一大把,但是讲的都不是很详细,因工作需要所以打算自己整理一份出来,免得每次都去百度,供大家使用!觉得好的可以收藏,记得免费评分哦!
         adb是什么?：adb的全称为Android Debug Bridge，就是起到调试桥的作用。通过adb我们可以在Eclipse中方面通过DDMS来调试Android程序，说白了就是debug工具。adb的工作方式比较特殊，采用监听Socket TCP 5554等端口的方式让IDE和Qemu通讯，默认情况下adb会daemon相关的网络端口，所以当我们运行Eclipse时adb进程就会自动运行。
      adb有什么用?：借助adb工具，我们可以管理设备或手机模拟器的状态。还可以进行很多手机操作，如安装软件、系统升级、运行shell命令等等。其实简而言说，adb就是连接Android手机与PC端的桥梁，可以让用户在电脑上对手机进行全面的操作。

```powershell
# 1.显示当前运行的全部模拟器
adb devies

# 2. 启动ADB
adb start-server

# 3.停止ADB
adb kill-server

# 4.安装应用程序  示例：adb install --r D:\mm.apk
adb install -r apk文件
-l # 锁定该程序
-r # 重新安装该程序，保存数据
-s # 安装在SD卡内，而不是设备内部存储

# 5.卸载应用程序  示例：adb uninstall com.tencent.mm
adb uninstall packagename
-k #不删除程序运行所产生的数据和缓存目录(如软件的数据库文件)

# 6.将手机设备中的文件copy到本地计算机
adb pull 设备目录 本地目录
例:adb pull /sdcard/mm.txt D:\(讲内存卡根目录的txt文件copy到D盘根目录) 

# 7.将本地计算机的文件copy到手机设备中
adb push 本地目录 手机设备目录
例：adb push D:\mm.txt /sdcard

# 8.查看adb命令帮助信息
adb help

# 9. 截屏
adb shell screencap -p 截图文件路径

# 10.查看指定包名应用的数据库存储信息（包括存储的SQL语句）
adb shell dumpsys dbinfo packagename

# 11.查看指定的进程或则进程id的内存信息  
adb shell dumpsys meminfo[packagename/pid]可以查看进程当前的内存情况
例:adb shell dumpsys meminfo com.tencent.mm

# 12.查看指定包名应用的详细信息(相当于AndroidMainfest.xml中内容)
adb shell dumpsys [packagename]例:adb shell dumpsys com.tencent.mm

# 13.查看当前应用的activity信息adb shell dumpsys activity top查看bug报告：
adb bugreport

# 14.列出手机装的所有apk包名
adb shell pm list packages
系统应用:adb shell pm list packages -s
第三方应用:adb shell pm list packages -3
使用grep过滤 :adb shell pm list packages | grep qq

# 15.清除应用缓存信息:
adb shell pm clear [packagename]

# 16.通过adb启动应用程序页面
adb shell am start -n[包名+activity名]
例:adb shell am start -n com.tencent.mm/.ui.SplashAcitvity
强制停止应用有些时候应用卡死了，需要强制停止，则执行以下命令：
adb shell am force-stop <packagename>// 
如：adb shell am force-stop cn.androidstar.demo

# 17.记录无线通讯日志：   
一般来说，无线通讯的日志非常多，在运行时没必要去记录，但我们还是可以通过命令，设置记录：
adb shell
logcat -b radio

# 18.获取设备的ID和序列号：
adb get-product
adb get-serialno

# 19.访问数据库SQLite3    
adb shell
     sqlite3  # cd system/sd/data //进入系统内指定文件夹
# ls //列表显示当前文件夹内容
# rm -r xxx //删除名字为xxx的文件夹及其里面的所有文件
# rm xxx //删除文件xxx
# rmdir xxx //删除xxx的文件夹

# 20.导出设备信息
adb get-serialno > 序列号.txt
adb shell cat /sys/class/net/wlan0/address > MAC地址.txt
adb shell getprop ro.product.model > 设备型号.txt
adb shell getprop ro.build.version.release> 系统版本.txt
adb shell pm list packages -s > 系统应用的所有包名.txt
adb shell pm list packages -3 > 第三方应用包名.txt
adb shell wm size > 屏幕分辨率.txt
adb shell wm density > 屏幕密度.txt
adb shell cat /proc/cpuinfo > CPU信息.txt
adb shell pm list permissions -f > 权限.txt
adb shell pm list users -f > 用户.txt

# 21.重启adb reboot
还有2个非常有用的命令:
1.备份adb backup
[-f <file>] [-apk|-noapk][-shared|-noshared] [-all] [-system|nosystem] [<packages...>]
例:adb backup -f mm.ab -noapk -noshared -nosystemcom.tencent.mm  # 你可以使用的最基本的命令是很简单的

adb backup -all
它将使用默认方式备份应用和设备的数据（不包含apk）到当前目录下并保存为文件backup.ab

这个命令有可能不对每个设置都有效，如果你出现像这种 "adb: cannot open file ./backup.ab"的错误，使用 adb backup -all -fC:\backup.ab来代替，其中路径C:\可根据喜好替换

对各个参数的解释：
-f <file>
用这个来选择备份文件存储在哪里，例如-f /backup/mybackup.ab将会使文件存储在根磁盘（Windows的C盘等等）下一个名为backup的文件夹里，并且备份文件名为mybackup.ab
-apk|-noapk
这个决定是否在备份里包含apk或者仅仅只备份应用数据，个人推荐使用-apk以免有的应用在应用市场找不到，如果不使用则默认的是-noapk
-shared|-noshared
这个参数用于决定是否备份设备共享的SD card内容，默认是-noshare，主要包括内部存储中的音乐、图片和视频，因此为保险起见，建议加上-share
-all
这个参数是一种简单地表达“所有应用”的说法，package参数可以选择备份单独的应用，如果你不是备份某个应用，使用-all备份整个系统
-system|-nosystem
这个参数决定-all标签是否包含系统应用，默认的是-system，根据情况可选择是否用-nosystem
<packages...>
如果你知道应用安装包的名称（例如com.google.android.apps.plus），就可以使用该参数备份特定应用。
3.当决定如何执行备份后，输入你喜欢的命令，在华为G700上测试，使用命令
adb backup -apk -all
2.使用run-as在非root情况获取沙盒数据(前提是开启debuggable模式)
1.   shell@android:/data $ run-as com.your.package
2.   run-as com.your.package
3.   shell@android:/data/data/com.your.package $ cd /data/data/com.your.package  
4.  cd /data/data/com.your.package
5.  shell@android:/data/data/com.your.package $ ls  
6.   ls  
7.   cache  
8.  databases
9. lib  
10. shared_prefs  
11. shell@android:/data/data/com.your.package $ cd databases  
12. cd databases  
13. shell@android:/data/data/com.your.package/databases $ ls  
14. yourpackagename.db  
15. $ cat preferences.db > /mnt/sdcard/yourpackagename.db   
将你要访问的package目录下的db文件拷贝到sdcard中，这样就可以正常访问了！ 对文件进行增删
法1:adb shell "run-aspackage.name chmod 666 /data/data/package.name/databases/file"
adb pull /data/data/package.name/databases/file .
adb shell "run-aspackage.name chmod 600 /data/data/package.name/databases/file"
adb exec-out run-as package.name cat databases/file > file
法2:> adb shellshell $ run-as com.example.packageshell $ chmod 666 databases/fileshell $ exit                                             
'run-as'shell $ cp /data/data/package.name/databases/file /sdcard/shell $ run-as com.example.packageshell $ chmod 600 databases/file> adb pull /sdcard/file .

更新一些反编译常用命令:
1.查看当前进程的内存的加载情况啊:
cat /proc/7654/maps 查看当前进程内存的映射情况
2.查看当前应用使用的端口号信息:
cat /proc/[pid]/net/tcp
3.查看进程的状态信息:
cat /proc/[pid]/status可以通过该命令获取到当前进程的包名,PID,PPID等等重要信息(比较实用的命令)
4.查看一个dex文件的详细信息
dexdump [dex文件路径]
5.使用aapt命令获取apk的清单文件
aapt dump xmltree [apk包] [需要查看的资源文件xml]
例:aapt  dump xmltree mm.apk AndroidMainfest.xml > demo.txt(讲mm应用中的AndroidMainfest.xml文件导入到新建的demo.txt文本中)
这里可能大家有个误区,aapt命令是与adb命令不是同一个命令,如果要使用和adb一样需要配置环境变量,也可以在SDK的build-tools文件夹内,shift+右键在此处打开命令窗口使用该命令!
```

---

## 第三章 Locust

提到性能测试，大部分小伙伴想到的就是LR和jmeter这种工具，小编一直不太喜欢写这种工具类的东西，我的原则是能用代码解决的问题，尽量不去用工具。
python里面也有一个性能测试框架Locust，本篇简单的介绍Locust的基本使用，希望越来越多的小伙伴能一起爱上它！

**Locust简介**

Locust是一款易于使用的分布式用户负载测试工具。它用于对网站（或其他系统）进行负载测试，并确定系统可以处理多少并发用户。
这个想法是，在测试期间，一群蝗虫（Locust）会攻击你的网站。您定义了每个蝗虫Locust（或测试用户）的行为，并且实时地从Web UI监视群集过程。这将有助于您在让真正的用户进入之前进行测试并识别代码中的瓶颈。
Locust完全基于事件，因此可以在一台计算机上支持数千个并发用户。与许多其他基于事件的应用程序相比，它不使用回调。相反，它通过**协程（gevent）机制**使用轻量级过程。每个蝗虫蜂拥到你的网站实际上是在自己的进程内运行（或者是greenlet，这是正确的）。这允许您在Py​​thon中编写非常富有表现力的场景，而不会使代码复杂化。

**gevent是第三方库，通过greenlet实现协程。greenlet是python的并行处理的一个库。 python 有一个非常有名的库叫做 stackless ，用来做并发处理， 主要是弄了个叫做tasklet的微线程的东西， 而greenlet 跟stackless的最大区别是greenlet需要你自己来处理线程切换， 就是说，你需要自己指定现在执行哪个greenlet再执行哪个greenlet。**

### 3.1 locust环境配置

**Windows环境下安装**

 Locust支持Python 2.7, 3.4, 3.5, and 3.6的版本，小编的环境是python3.6直接用pip安装就行

```python
pip3 install locust
```

安装成功后验证

```python
(venv) H:\Locust\locust1202>locust -V
locust 2.5.1.dev20
```

 如果您需要最新最好的 Locust 版本并且迫不及待地等待下一个合适的版本，您可以像这样安装一个开发版本： 

```python
pip3 install -U --pre locust
```

 每次将分支合并到 master 时，都会发布开发版本。 

**Linux环境下安装**

1、运行&开发环境（CentOS Linux release 8）

- 安装：python 3.6+

2、pip 命令安装

```
pip install locust
```

3、查看 Locust 的版本号，出现如下正常回显表示安装成功

```
[work@ip-10-0-41-78 ~]$ locust -V
locust 1.0.3
```

**升级你的 Locust**

```
pip install --upgrade locust
```

### 3.2 入门

locust里面请求是基于requests的，每个方法请求和requests差不多，请求参数、方法、响应对象和requests一样的使用，之前学过requests库的，这里就非常简单了

- requests.get 对应client.get
- requests.post 对应client.post

Locust 测试本质上是一个 Python 程序。这使得它非常灵活，特别擅长实现复杂的用户流。但它也可以做简单的测试，所以让我们从这个开始： 

```python
from locust import HttpUser, task, between


class QuickStartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/cnike/p/10783949.html")
        self.client.get("/cnike/p/10726706.html")
```

终端执行命令,运行后编辑器出现两行 ：

- -f 参数是指定运行的脚本
- --host 是指定运行项目的host地址，这里用的https://www.cnblogs.com，代码里面get访问的是"/cnike/p/10783949.html"，拼接起来就是完整地址了 

```python
(venv) H:\Locust\locust1202>locust -f demo1.py --host=https://www.cnblogs.com
[2021-12-25 12:34:20,632] DESKTOP-C09SST2/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 (accepting connections from all network interfaces)
[2021-12-25 12:34:20,660] DESKTOP-C09SST2/INFO/locust.main: Starting Locust 2.5.1.dev20
```

8089是该服务启动的端口号。由于是在本机上搭建的locust，所以可以直接在浏览器输入http://localhost:8089/打开，
如果是在其它机器上搭建的locust服务，那就通过http://其它机器IP:8089/打开 

![1640407817809](J:\homework\Python学习笔记\Test学习笔记.assets\1640407817809.png)

> - Number of users to simulate  设置虚拟用户总数
> - Hatch rate (users spawned/second)  每秒启动虚拟用户数
> - 点击Start swarming  开始运行性能测试

![1640407277999](J:\homework\Python学习笔记\Test学习笔记.assets\1640407277999.png)

> 三个图表分别是
>
> - 吞吐量/每秒响应事务数（rps）实时统计
> - 平均响应时间/平均事务数实时统计
> - 虚拟用户数运行
>
> **Type**
>
> - 请求的类型，在 HttpUser 中，常见的有 Get 和 Post
> - 如果是自定义 Client ，Type 同样也可自定义
>
> **Name**
>
> - 在 HttpUser 中，是请求中的 name 参数，如果未定义 name，这里将是请求的接口路径
> - 如果路径中包含变量参数，大部分情况下都建议在脚本中指定一下 name，除非你想对不同的传参分别进行独立的统计
>
> **Requests**
>
> - 表示成功发出请求的数量，并不是成功处理请求的数量
>
> **Fails**
>
> - 表示请求处理失败的数量
>
> **Median**
>
> - 表示所有请求响应时间的中位数
>
> **90%ile**
>
> - 表示所有请求响应时间的90%百分位数
>
> **Average / Min / Max**
>
> - 表示所有请求响应时间的平均值 / 最小值 / 最大值
>
> **Average size**
>
> - 表示所有响应的size平均值
>
> **Current RPS**
>
> - 表示每秒创建的请求数
>
> **Current Failures / s**
>
> - 表示每秒创建请求的失败数量

![1640407766332](J:\homework\Python学习笔记\Test学习笔记.assets\1640407766332.png)

每秒请求总数：如果上下波动较大，说明性能不稳定

- 每秒总的请求数，也需要看趋势
- 有没有某些时刻，请求数大幅度波动

![1640407777866](J:\homework\Python学习笔记\Test学习笔记.assets\1640407777866.png)

响应时间：黄色为最大时间，绿色为最小时间。一般3-5秒为最佳，超过10秒为较差，最大值如果持续高位就需要进行性能优化。 

- 接口响应时间，主要看趋势，是否平稳
- 有无某些时刻，响应时间有大幅度波动

![1640407785854](J:\homework\Python学习笔记\Test学习笔记.assets\1640407785854.png)

虚拟用户数

- 两秒钟有上了一个虚拟用户（线程），且一直是一个线程

> #### Charts 图表
>
> 如果你对比 LoadRunner 或者 Jmeter，你一定会对 Locust 所提供的结果图形之“简陋”感到震惊，想要学习 Locust 的结果图表大约只要3分钟。
>
>  首先来看看  **“每秒请求数”**，也就是**“total_requests_per_second”**，横轴为时间轴，纵轴为每秒请求的数量（请求处理通过的）： 
>
> 再来看看 **“响应时间”**，也就是**“response_times_(ms)”**，横轴为时间轴，纵轴为以毫秒为单位的响应时间，需要注意的是，图表上面两根线并不是表示平均值，而是响应时间的“中位数”和“95%百分位数值”：
>
> 最后看看**“运行中的用户”**，也就是**“number_of_users”**，横轴为时间轴，纵轴为时间所对应的“用户数”：  
>
> #### Failures 失败日志
>
> 脚本请求产生的异常响应、失败都可以在这里看到
>
> #### Exceptions 异常日志
>
> 脚本运行抛出的异常可以在这里看到
>
> #### Download Data 下载原始数据
>
> 内容和 Statistics 的一致

### 3.3 一个简单的脚本

案例：一个用户登录胡，随机的访问指定页面的测试脚本

**首先：**

- 将以 100% 的概率通过login接口执行登录操作；

**然后：**

- 有25%的概率按照顺序访问/hello页面和/world页面
- 有75%的概率访问/item页面（这里会传一个动态id）

| 任务       | 目标         | 操作                 | 参数              | 条件                   |
| ---------- | ------------ | -------------------- | ----------------- | ---------------------- |
| 100%       | 接口：login  | 发送登录请求         | username,password |                        |
| 25% - stp1 | 页面：/index | 浏览 index 页面      | /                 |                        |
| 25% - stp2 | 页面：/view  | 浏览 view 页面       | /                 |                        |
| 75%        | 页面：/item  | 浏览指定项目id的页面 | id                | 随机浏览id值范围为1~11 |

脚本实现：

```python
import os
import random
from locust import HttpUser, task, between


class QuickStartUser(HttpUser):
    wait_time = between(5, 9)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    @task
    def index_page(self):
        self.client.get("/studentcenter/adv/GetAdvertList", headers=self.header)

    @task(3)
    def view_item(self):
        item_id = random.randint(1, 11)
        self.client.get("/StudentCenter/Navigation/menu?bust=1640683458756&id=%s&_=1640683458093" % item_id, headers=self.header, name="/item")

    def on_start(self):
        data = {"loginName": "zzq283814", "passWord": "283814zzq"}
        self.client.post("/Account/UnitLogin", headers=self.header, data=data)


if __name__ == '__main__':
    os.system("locust -f aopeng.py --host=https://learn.open.com.cn")
```

脚本解释：

```python
import random
from locust import HttpUser, task, between
```

> 导入 random 用于后续随机数生成使用
> 从 locust 导入 HttpUser 用于提供http操作的方法
> 从 locust 导入 task 用于任务的规划设定
> 从 locust 导入 between 用于控制任务之间的延迟停顿 

```python
class QuickstartUser(HttpUser):
```

> 定义一个所需模拟的用户类（在这里，我们需要模拟的是HTTP用户）所以，继承了 HttpUser。
> HttpUser 为我们所需模拟的用户类了 HTTP 客户端属性，该属性是 HttpSession 的实例，可以用于向被测试系统发出 HTTP 请求 

```python
 wait_time = between(5, 9) 
```

> 定义了一个等待时间的函数，可以使用户执行每个任务以后，随机的等待了5~9秒。
> 在本节案例脚本里面，分别有：index_page 和 view_item 两个任务。 

```python
@task
def index_page(self):
    self.client.get("/studentcenter/adv/GetAdvertList", headers=self.header)

@task(3)
def view_item(self):
	item_id = random.randint(1, 11)
	self.client.get("/StudentCenter/Navigation/menu?bust=1640683458756&id=%s&_=1640683458093" % item_id, headers=self.header, name="/item")
```

> 在定义的两个任务  index_page 和 view_item 通过装饰器控制了他们执行的权重为1：3，你可以理解为在每轮迭代的循环中，index_page将有25%的概率被执行，而view_item将有75%的概率被执行，执行index_page时，将有两个页面按访问请求，分别是 /index_page 和 /view_item

```python
@task(3)
def view_item(self):
	item_id = random.randint(1, 11)
	self.client.get("/StudentCenter/Navigation/menu?bust=1640683458756&id=%s&_=1640683458093" % item_id, headers=self.header, name="/item")
```

> 在 view_item 任务中，通过使用1~11的随机查询参数加载动态URL。为了不在 Locust 的统计信息中获得 11 个单独的条目。
> 为了把这个动态 URL 的所有响应样本作为一个整体进行统计，使用 name 参数将所有这些请求分组到名为“ / item”的条目下。
> 只有定义了 @task 的任务才会被执行。 

```python
def on_start(self):
    data = {"loginName": "zzq283814", "passWord": "283814zzq"}
    self.client.post("/Account/UnitLogin", headers=self.header, data=data)
```

> 在这里，我们声明了一个 on_start，用于模拟用户启动的时候，每个用户必须执行的初始化操作，在此，它是一个 login 接口请求。

![1640693892429](J:\homework\Python学习笔记\Test学习笔记.assets\1640693892429.png)

1. Fails

- 先观察请求失败的数量
- 一般请求通过率需要99.99%，达不到标准需要跟开发沟通

2. Current RPS 和 Average（ms）

- Current RPS 每秒请求数，分析是否达到预期标准
- 如果 current RPS 达到标准，分析下 Average（平均响应时间）是否达到预期标准
- 如果有 没有达标项，需要跟开发沟通

3. Average size

- 请求数据大小是分析网络的标准之一
- 如果请求大小过大，可能会造成网络问题，发现可以跟开发沟通

### 3.4 脚本开发入门(1)

#### 1. 脚本基本构成

一个Locust测试脚本iu是一个普通的python文件，它的基本组成十分简单：

- **定义用户类型**

  所有用户的属性都需要集成自User Class，我们最常用的 **HttpUser** 也是如此，你也可以定义一个如TcpUser，或者 WebSocketUser，甚至基于你测试的业务系统做一个， 例如 QQUser，但是最终都必须继承至 User Class，类似于过去 LoadRunner、Jmeter 的选择应用的通讯协议或选择请求插件。

- **等待时间的方法**

  声明一个等待时间的方法，用于确定模拟用户在任务之间执行的等待停留时间。Locust 附带了一些内置函数用于返回等待时间的方法，包括：

  1. between：在指定范围内的随机；
  2. constant：基于响应到下一次请求之间的固定的等待时间；
  3. constant_pacing：基于请求到下一次请求的固定间隔时间 ;

- **主机属性**

  用于定义测试的主机信息，比如 [http://www.cnblogs.com](http://www.cnblogs.com/)，如果在脚本中没有定义，那在命令行启动测试或 WebUI 中将作出定义 

- **任务属性**

  用于定义任务的执行逻辑，你可以定义多个任务，让模拟的用户按照不同任务的权重配置随机执行，也可以让任务按照你的编排顺序执行 

#### 2. 脚本入门开发

我们采用循序渐进的方式来，你不需要特别关注下面的每个范例所具备的实际意义，只需要关心脚本的结构 

```python
from locust import HttpUser, task, between


class QuickStartUser(HttpUser):
    wait_time = between(5, 10)

    @task(2)
    def open_blog(self):
        self.client.get("/cnike")

    @task
    def open_links(self):
        self.client.get("/cnike/p/10783949.html")
        self.client.get("/cnike/p/10726706.html")

    def on_start(self):
        self.client.get("/")
```

脚本实现：

- 把 User 替换为 HttpUser
- 通过 @task，配置了两个函数的执行权重分别为 2：1
- 在 open_blog 函数内，任务是模拟用户打开我的博客首页路径（Host + "/cnike/"，即：
  https://www.cnblogs.com/cnike/）
- 在 open_links 函数内，任务是模拟用户依次浏览 2 篇博客，注意，在这2篇博客的浏览过程中，是没有时间间隔的
- 定义了每次任务结束以后，随机等待时间的间隔区间仍然为 5~10 秒

执行命令

```python
locust -f 2.blogs.py
```

![1640697665150](J:\homework\Python学习笔记\Test学习笔记.assets\1640697665150.png)

从上面的运行情况可以发现

- 标注1：作为 on_start 任务的内容，请求主机根目录只执行了 1 次（# Requests）
- 标注2：open_links 任务内依次访问 2 篇博文的执行顺序是可控的，并且同在一个任务内，次数也是一致
- 权重控制 2：1，实际的执行比例约为 20%：10%，但是随着场景执行时间越来越长，会越来越趋近于 2:1

**现在我们对这个脚本进行一些修改，让它更像一个真实的用户访问行为：**

- 任务等待时间：任务之间按照特定的等待时间进行间隔
- 步骤等待时间：在任务内加入步骤之间的时间间隔
- 参数化：文章页面参数
- 任务：按照顺序的方式执行
- 自定义 Locust 发出的 HTTP 请求头

### 3.5 脚本开发入门(2)

接上： 现在我们对这个脚本进行一些修改，让它更像一个真实的用户访问行为 

**1. 任务等待时间：任务之间按照特定的等待时间进行间隔**

Locust 的任务之间等待时间控制包括：

方法1：between 类，指定范围内随机（5~10秒）等待 

```python
wait_time = between(5, 10)
```

方法2：constant 类，从上一次响应结束后，等待特定时间（3秒），再发起下一次请求 

```python
wait_time = constant(3)
```

方法3：constant_pacing 类，从上一次请求发起后，等待特定时间（3秒），再发起下一次请求，如果上一次请求的响应时间大于指定的时间（3秒），则在响应后立即发起下一次请求 

```python
wait_time = constant_pacing(3)
```

**2. 步骤等待时间：在任务内加入步骤之间的时间间隔**

方法1：从 time 导入 sleep 类即可

```python
from locust import HttpUser, task, between
from time import sleep


class QuickStartUser(HttpUser):
    wait_time = between(5, 10)

    @task(2)
    def open_blog(self):
        self.client.get("/cnike")

    @task
    def open_links(self):
        self.client.get("/cnike/p/10783949.html")
        sleep(1 )
        self.client.get("/cnike/p/10726706.html")
        sleep(1 )

    def on_start(self):
        self.client.get("/")
```

**3. 参数化：从页面解析博客文章 ID**

由上面 open_links 任务的内容可知，10783949、10726706 是文章 ID，但是随着日后博客内容的增删改，这些博客链接可能随之失效、新增，因此为了让我们的脚本行为更符合一个真实用户的访问行为，现需要脚本在打开我博客的首页后从首页的页面源码中，解析出文章链接进行点击。所以在下面的脚本中，我将会：

1. 导入 re，在 open_blog 任务中对博客的页面html源码进行解析，获得文章列表的url
2. 在 open_links 任务中，对 open_blog 任务解析得出的文章url列表进行遍历访问

```python
import re
from locust import HttpUser, task, constant


class CnBlogUser(HttpUser):
    wait_time = constant(3)

    @task(2)
    def open_blog(self):
        with self.client.get("/cnike/") as resp:
            print(resp)
            if resp.status_code < 300:
                pattern = re.compile(r'<a href="(.*)" class="c_b_p_desc_readmore">')
                self.url_list = pattern.findall(resp.text)
            else:
                pass

    @task(1)
    def open_links(self):
        # 由于权重配置，无法确保 open_links 任务执行时 self.urlList 包含文章链接列表
        for url in self.url_list:
            self.client.get(url)

    def on_start(self):
        self.client.get("/")
```

但是，上面脚本存在一个问题，由于当前任务的执行是依据权重配置执行的，无法保证 open_blog 和 open_links 的先后执行顺序。当然，你也可以把 open_blog 和 open_links 两个任务内的工作合并为一个任务就可以达到顺序执行的目的。 

**3. 任务控制：按照顺序的方式执行（SequentialTaskSet 类）**

主要步骤：

- 导入 SequentialTaskSet 类
- 创建一个 任务类，继承自 SequentialTaskSet，在里面编排好任务执行的顺序
- 在 cnblogUser 类内部，通过 tasks 转载需要执行的任务

```python
import re
from locust import HttpUser, task, constant, SequentialTaskSet


# 继承 SequentialTaskSet 的一个任务类，内部编排好任务的执行顺序
class TaskCase(SequentialTaskSet):

    # 初始化
    def on_start(self):
        self.client.get("/")

    # @task 装饰器说明下面是一个任务
    @task
    def open_blog(self):
        with self.client.get("/cnike/") as resp:
            if resp.status_code < 300:
                pattern = re.compile(r'<a href="(.*)" class="c_b_p_desc_readmore">')
                self.urlList = pattern.findall(resp.text)
            else:
                pass

    @task
    def open_links(self):
        for url in self.urlList:
            self.client.get(url)


# 继承 httpUser
class CnBlogUser(HttpUser):
    tasks = [TaskCase]
    wait_time = constant(3)
```

至此，任务执行顺序将为：on_start -> open_blog -> open_links，执行压测场景看看 

![1640703670039](J:\homework\Python学习笔记\Test学习笔记.assets\1640703670039.png)

由上面的结果，可以看到，虚拟用户实现了 打开博客首页，进入我的博客并解析页面上的文章链接，再逐个访问，但是，浏览多篇文章本质上只是不同的文章id传参请求，没有在结果中分别统计的需要，因此我们给请求指定一下name，进行合并统计。

```python
@task
def open_links(self):
    for url in self.urlList:
        self.client.get(url, name="open_link")
```

再次执行，可见多篇文章遍历访问的请求响应已经被合并统计 

![1640703996146](J:\homework\Python学习笔记\Test学习笔记.assets\1640703996146.png)

### 3.6 脚本开发入门(3)

**在前面的两节里面，我们已经演示了 Locust 的：**

- 脚本的基本构成
- 脚本的初始化：on_start
- 脚本的任务规划：通过 @task 装饰器实现
- 任务的控制：按权重执行、按顺序执行
- 等待的控制：任务之间的3种间隔、步骤之间采用sleep
- 响应的解析：状态码、响应正文（requests 库）
- Web UI 中发起压测

接下来主要是对 Locust 脚本种实现 HTTP 请求的进一步演示 

**在绝大部分的测试场景下，HTTP 请求需要进行一些处理才能满足我们的测试需求，例如：**

- 在调试过程中，打印 HTTP 响应信息
- 对 HTTP 响应进行断言 / 结果标记
- 修改 Locust 发出的默认 HTTP 请求头信息，以满足系统的要求
- 对 HTTP 的 接口响应（Json 格式）进行解析

**示例：输出响应调试信息**

在下面的脚本中，你可以多尝试几个 host，执行这个脚本，看看 Locust 打印的调试信息和你浏览器反馈的页面是不是一致的。

```python
from locust import HttpUser, task, constant, SequentialTaskSet


class TaskCase(SequentialTaskSet):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    @task
    def search_page(self):
        data = {"loginName": "zzq283814", "passWord": "283814zzq"}
        with self.client.post("/Account/UnitLogin", headers=self.header, data=data) as resp:
            # HTTP 响应状态码
            print(resp.status_code)

            # HTTP 响应头
            print(resp.headers)

            # HTTP 响应正文（需要对文本字符串做提取时）
            print(resp.text)

            # HTTP 响应正文（需要对文件、图片做提取时）
            print(resp.content)


class CustomUser(HttpUser):
    tasks = [TaskCase]
    wait_time = constant(5)

```

执行命令：

```python
locust -f 3.cnblogs.py --host=https://learn.open.com.cn
```

打印如下：

```python
(venv) H:\Locust\locust1202>locust -f 3.cnblogs.py
[2021-12-28 23:18:05,660] DESKTOP-C09SST2/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 (accepting connections from all network interfaces)
[2021-12-28 23:18:05,675] DESKTOP-C09SST2/INFO/locust.main: Starting Locust 2.5.1.dev20
[2021-12-28 23:18:18,104] DESKTOP-C09SST2/INFO/locust.runners: Ramping to 3 users at a rate of 1.00 per second
200
{'Date': 'Tue, 28 Dec 2021 15:18:12 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '102', 'Connection': 'keep-alive', 'Cache-Control': 'private', 'X-AspNetMvc-Version': '4.0', 'X-AspNet-Version': '4.0.30319', 'X-Via-JSL': '88b83ec,-', 'S
et-Cookie': '__jsluid_s=cbe181d32773b7efa0a3b19dbb9d5b58; max-age=31536000; path=/; HttpOnly; SameSite=None; secure', 'X-Cache': 'bypass'}
{
  "status": 1,
  "message": "设备指纹异常，请刷新页面重新提交",
  "data": null
}
b'{\r\n  "status": 1,\r\n  "message": "\xe8\xae\xbe\xe5\xa4\x87\xe6\x8c\x87\xe7\xba\xb9\xe5\xbc\x82\xe5\xb8\xb8\xef\xbc\x8c\xe8\xaf\xb7\xe5\x88\xb7\xe6\x96\xb0\xe9\xa1\xb5\xe9\x9d\xa2\xe9\x87\x8d\xe6\x96\xb0\xe6\x8f\x90\xe4\xba\xa4",\r\n  "data": null\r\n}'

```

#### 1. 基于状态码判断

当把 **catch_response** 参数 设置为 **True** 时，你可以手动控制在 Locust 的统计信息中报告的内容，例如下面的基于状态码判断 

```python
from locust import HttpUser, task, constant, SequentialTaskSet


class TaskCase(SequentialTaskSet):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    @task
    def search_page(self):
        data = {"loginName": "zzq283814", "passWord": "283814zzq"}
        with self.client.post("/Account/UnitLogin", headers=self.header, data=data, catch_response=True) as resp:
            if resp.status_code == 200:
                print("success")
                resp.success()
            else:
                # 否则输出响应报文进一步排查
                resp.failure(resp.text)


class CustomUser(HttpUser):
    tasks = [TaskCase]
    wait_time = constant(5)
```

#### 2. 基于响应报文判断

基于响应的状态码判断业务请求是否正确处理不够严谨，错误页面并不一定会以404状态码返回，错误的业务响应通常也是200，所以，这时候你可能还想对响应报文做进一步校验以确定请求是否处理成功 

```python
from locust import HttpUser, task, constant, SequentialTaskSet


class TaskCase(SequentialTaskSet):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    @task
    def search_page(self):
        data = {"loginName": "zzq283814", "passWord": "283814zzq"}
        with self.client.post("/Account/UnitLogin", headers=self.header, data=data, catch_response=True) as resp:
            if 'data' in resp.text:
                print("success")
                resp.success()
            else:
                # 否则输出响应报文进一步排查
                resp.failure(resp.text)


class CustomUser(HttpUser):
    tasks = [TaskCase]
    wait_time = constant(5)
```

#### 3. 基于响应时间判断

有时候过慢的响应时间也可以算作一种不可接受的错误，譬如你肯定就无法忍受人工客服电话那头为了查询你的个人信息还让你等上个半分钟，那一头的呼叫中心也无法忍受为了查询一个用户信息导致坐席干等阻塞半分钟，所以还可以这样处理： 

```python
from locust import HttpUser, task, constant, SequentialTaskSet


class TaskCase(SequentialTaskSet):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    @task
    def search_page(self):
        data = {"loginName": "zzq283814", "passWord": "283814zzq"}
        with self.client.post("/Account/UnitLogin", headers=self.header, data=data, catch_response=True) as resp:
            # 如果响应时间大于 3 秒标记为响应失败
            if resp.elapsed.total_seconds() > 3:
                resp.failure("Request took too long")
            else:
                # 否则不做业务判断直接标记为成功
                resp.success()


class CustomUser(HttpUser):
    tasks = [TaskCase]
    wait_time = constant(5)
```

一个 HTTP 请求不能被正确处理，无非三点原因：

- HTTP 请求头错误，自定义一个 HTTP 请求头即可
- HTTP 请求报文内容错误，检查 url、参数格式、业务参数
- 会话状态丢失，检查 session、cookie，在 Locust 中大部分情况下都自动保持会话































## 附录 注意事项

### 1.自动化等待时间优化

1. 强制等待

```python
'''
设置固定休眠时间，单位为秒。 由python的time包提供, 导入 time 包后就可以使用。
缺点：不智能，使用太多的sleep会影响脚本运行速度。
'''

import time
sleep(10)  #等待10秒
```

2.  隐式等待:implicitly_wait() 

说明：隐式等待是全局的是针对所有元素，设置等待时间如10秒，如果10秒内出现，则继续向下，否则抛异常。可以理解为在10秒以内，不停刷新看元素是否加载出来。

使用场景：隐式等待只需要声明一次，一般在打开浏览器后进行声明。声明之后对整个drvier的生命周期都有效，后面不用重复声明。隐式等待存在一个问题，那就是程序会一直等待整个页面加载完成，也就是一般情况下你看到浏览器标签栏那个小圈不再转，才会执行下一步，但有时候页面想要的元素早就在加载完成了，但是因为个别js之类的东西特别慢，仍得等到页面全部完成才能执行下一步。

```python
'''
由webdriver提供的方法，一旦设置，这个隐式等待会在WebDriver对象实例的整个生命周期起作用，
它不针对某一个元素，是全局元素等待，即在定位元素时，需要等待页面全部元素加载完成，才会执行下一个语句。
如果超出了设置时间的则抛出异常。
'''
driver.implicitly_wait(10) # 隐式等待10秒
```

<font color="red"> 需要特别说明的是：隐性等待对整个driver的周期都起作用，所以只要设置一次即可，有人把隐性等待当成了sleep在用，走哪儿都来一下… </font>

3.  显示等待:WebDriverWait() 

说明：显示等待是单独针对某个元素，设置一个等待时间如5秒，每隔0.5秒检查一次是否出现，如果在5秒之前任何时候出现，则继续向下，超过5秒尚未出现则抛异常。显示等待与隐式等待相对，显示等待必须在每个需要等待的元素前面进行声明。

使用场景：当打开一个新页面，执行第一个元素操作的时候；当某一步操作会引发页面的加载，并且加载的内容包含了下一步需要操作的元素。一句话，就是当某个元素有加载过程的时候，就需要加上显示等待。

```python
from selenium.webdriver.support.wait import WebDriverWait

WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)

'''
driver: 传入WebDriver实例，即我们上例中的driver
timeout: 超时时间，等待的最长时间（同时要考虑隐性等待时间）
poll_frequency: 调用until或until_not中的方法的间隔时间，默认是0.5秒
ignored_exceptions: 忽略的异常，如果在调用until或until_not的过程中抛出这个元组中的异常，则不中断代码，继续等待，如果抛出的是这个元组外的异常，则中断代码，抛出异常。默认只有NoSuchElementException。
until
method: 在等待期间，每隔一段时间调用这个传入的方法，直到返回值不是False
message: 如果超时，抛出TimeoutException，将message传入异常
until_not 与until相反，until是当某元素出现或什么条件成立则继续执行，until_not是当某元素消失或什么条件不成立则继续执行，参数也相同，不再赘述。
'''
```

看了以上内容基本上很清楚了，调用方法如下：

```python
WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)
```

可执行方法包含：

expected_conditions是selenium的一个模块，其中包含一系列可用于判断的条件：

```python
from selenium.webdriver.support import expected_conditions as EC
```

 ![img](J:\homework\Python学习笔记\Test学习笔记.assets\1437068-20200214160557341-574663931.png) 

```python
# 判断当前页面标题是否为title
title_is(title)
title：	# 期望的页面标题判断当前页面标题是否包含titletitle_contains(title)
title：	# 期望的页面标题判断此定位的元素是否存在presence_of_element_located(locator)
locator：# 元素的定位信息判断页面网址中是否包含urlurl_contains(url)
url：	# 期望的页面网址判断页面网址是否为urlurl_to_be(url)
url：	# 期望的页面网址判断页面网址不是urlurl_changes(url)
url：	# 期望的页面网址判断此定位的元素是否可见visibility_of_element_located(locator)
locator：	# 元素的定位信息判断此元素是否可见visibility_of(element)
element：	# 所获得的元素判断此定位的一组元素是否至少存在一个presence_of_all_elements_located(locator)
locator：	# 元素的定位信息判断此定位的一组元素至少有一个可见visibility_of_any_elements_located(locator)
locator：	# 元素的定位信息判断此定位的一组元素全部可见visibility_of_all_elements_located(locator)
locator：	# 元素的定位信息判断此定位中是否包含text_的内容text_to_be_present_in_element(locator, text_)
locator：	# 元素的定位信息text_：期望的文本信息判断此定位中的value属性中是否包含text_的内容text_to_be_present_in_element_value(locator, text_)
locator：	# 元素的定位信息text_：期望的文本信息判断定位的元素是否为frame，并直接切换到这个frame中frame_to_be_available_and_switch_to_it(locator)
locator：	# 元素的定位信息判断定位的元素是否不可见invisibility_of_element_located(locator)
locator：	# 元素的定位信息判断此元素是否不可见invisibility_of_element(element)
element：	# 所获得的元素判断所定位的元素是否可见且可点击element_to_be_clickable(locator)
locator：	# 元素的定位信息判断此元素是否不可用staleness_of(element)
element：	# 所获得的元素判断该元素是否被选中element_to_be_selected(element)
element：	# 所获得的元素判断定位的元素是否被选中element_located_to_be_selected(locator)
locator：	# 元素的定位信息判断该元素被选中状态是否和期望状态相同element_selection_state_to_be(element,Boolean)
element：所获得的元素Boolean：期望的状态（True/False）	# 判断定位的元素被选中状态是否和期望状态相同element_located_selection_state_to_be(locator,Boolean)
locator：	# 元素的定位信息Boolean：期望的状态（True/False）判断当前浏览器页签数量是否为numnumber_of_windows_to_be(num)
num：	# 期望的页签数量判断此handles页签不是唯一打开的页签new_window_is_opened(handles)
handles：	# 页签判断是否会出现alert窗口警报alert_is_present()
```

### 2. 黑盒测试、白盒测试、单元测试、集成测试、系统测试、验收测试的区别与联系

黑盒测试、白盒测试、单元测试：开发人员在不同的开发阶段要做的事

黑盒测试、集成测试、系统测试：测试人员在测试周期内做的工作

验收测试：一般事用户/产品做的工作

**1. 黑盒测试**

不考虑程序内部结构和逻辑结构，主要是用来测试系统的功能是否满足需求规格说明书。

**2. 白盒测试**

主要应用在单元测试阶段，主要是对代码级的测试，针对程序内部逻辑构成，测试手段有：语句覆盖、判定覆盖、条件覆盖、路径覆盖、条件组合覆盖。

**3. 单元测试**

单元测试粒度最小，一般由开发小组次啊用白盒方式来测试，主要测试单元是否复符合"设计"。 一般来说，要根据实际情况去判定其具体含义，如C语言中单元指一个函数，Java里单元指一个类，图形化的软件中可以指一个窗口或一个菜单等。总的来说，单元就是人为规定的最小的被测功能模块。单元测试是在软件开发过程中要进行的最低级别的测试活动，软件的独立单元将在与程序的其他部分相隔离的情况下进行测试。 

**4. 集成测试**

集成测试界于单元测试和系统测试之间，起到"桥梁租用"，既验证"设计"又验证"需求"，主要用来测试模块之间的接口，同时还要测试一些主要业务功能。把多个已经测试过的单元组合到一起，测试他们之间的接口和功能。

**5. 系统测试**

粒度最大， 一般由独立测试小组采用黑盒方式来测试，主要测试系统是否符合“需求规格说明书”。  在经过以上各阶段测试确认之后，把系统完整地模拟客户环境来进行的测试。  其目的是通过与系统的需求相比较，发现所开发的系统与用户需求不符或矛盾的地方，从而提出更加完善的方案.。它的的任务是尽可能彻底地检查出程序中的错误，提高软件系统的可靠性。

**6. 验收测试**

验收测试与系统测试相似，主要区别是测试人员不同，验收测试由用户/产品执行。 