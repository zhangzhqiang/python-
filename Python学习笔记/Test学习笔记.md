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

可以发现，类级别的初始化、清除在整定义类的前后分别 `执行1次` 。

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

可以发现，方法级别的初始化、清除每个方法前后分别 `执行一次` 。

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

### 3.2 快速入门

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

终端执行命令，运行后编辑器出现两行 ：

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

案例：一个用户登录，随机的访问指定页面的测试脚本

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
> 只有定义了 @task 的任务才会被执行。  **@task**接受一个可选的权重参数，可用于指定任务的执行率。在以下示例中，*task2*被选中的机会是*task1 的*两倍： 

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
  3. constant_pacing： 确保任务每 X 秒（最多）运行一次的自适应时间（它是constant_throughput的数学倒数）；  
  4. constant_throughput： 确保任务每秒运行（最多）X 次的自适应时间；

- **主机属性**

  用于定义测试的主机信息，比如 [http://www.cnblogs.com](http://www.cnblogs.com/)，如果在脚本中没有定义，那在命令行启动测试或 WebUI 中将作出定义。 通常，这是在 Locust 的 Web UI 或命令行中指定的`--host`，在 locust 启动时使用该 选项。 

- **任务属性**

  User 类可以使用@task装饰器将任务声明为它的方法，但也可以使用*tasks*属性指定任务，用于定义任务的执行逻辑，你可以定义多个任务，让模拟的用户按照不同任务的权重配置随机执行，也可以让任务按照你的编排顺序执行 
  
- **权重属性**

  如果文件中存在多个用户类，并且没有在命令行中指定用户类，Locust 将生成相同数量的每个用户类。您还可以通过将它们作为命令行参数传递来指定要从同一个 locustfile 使用哪些用户类： 

  ```python
  locust -f locust_file.py WebUser MobileUser
  ```

- **环境属性**

  environment 对用户正在运行的 的引用。使用它与环境或其 runner 包含的环境进行交互。例如，从任务方法中停止跑步者：

  ```python
  self.environment.runner.quit()
  ```

  如果在独立的 locust 实例上运行，这将停止整个运行。如果在工作节点上运行，它将停止该特定节点。

  **on_start 和 on_stop 方法**

  用户（和TaskSets可以声明一个 on_start 方法和/或  on_stop 方法。User on_start 在开始运行时会调用它的方法，on_stop 在它停止运行时会调用它的 方法 。对于 TaskSet，该 on_start 方法在模拟用户开始执行该 TaskSet on_stop 时调用，并在模拟用户停止执行该 TaskSet 时 interrupt() 调用（当被调用时，或者用户被杀死时）。

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

<img src="J:\homework\Python学习笔记\Test学习笔记.assets\1640697665150.png" alt="1640697665150"  />

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

当把 **catch_response** 参数 设置为 **True** 时, 您可以使用catch_response参数、with语句 ，你可以手动控制在 Locust 的统计信息中报告的内容，例如下面的基于状态码判断 

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

**对 HTTP 的 接口响应（Json 格式）进行解析**

在对服务接口执行压测过程中，响应报文如果是以Json作为数据格式返回，取值会更加方便，以下面以接口为例： 

```python
from locust import HttpUser, task, constant, SequentialTaskSet
import json


class TaskCase(SequentialTaskSet):

    @task
    def search_page(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
        with self.client.get(
                "/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=10&page_start=0",
                headers=header) as resp:
            resp_json = json.loads(resp.text)
            print(resp_json["subjects"])


class CustomUser(HttpUser):
    tasks = [TaskCase]
    wait_time = constant(5)


if __name__ == '__main__':
    import os

    os.system("locust -f 4.test1.py --host=https://movie.douban.com/")

```

### 3.7 脚本入门开发(4)

以下主要介绍Locust执行参数化的方法，参数化的目的无非就是以下几种：

- 模拟用户在不同场景下的传参差异化，比如说所有并发对同一个订单执行支付，也许你需要检验这样是否能发现到一些别的异常，但这是不符合性能测试需求的

- 满足业务对用户传参的约束条件，比方说你如果压测的是即时通讯的消息收发，即便支持多终端在线，但大量并发登录一个账号也是是不符合实际的

- 满足系统对用户传参的约束条件

对一个参数执行参数化，首先得分清楚这个参数是属于 **“基础数据”** 还是 **“业务数据”** ，比如 性别、省份、年月日，这些可以归纳为基础数据，而对于与被测试系统业务有一定关联性的，你可以归为业务数据，例如 账号密码、userId、orderId。 通常来说，基础数据 的数据范围是相对数量固定的、内容有限的，即便切换测试环境也不影响的，所以一般在脚本中内实现随机抽取，例如：

```python
import random

sex = random.choice(['男性', '女性'])
year = random.randint(1949,2020)
```

而业务数据动辄几百上千条，相对来说数量和内容都是可变的，则应该通过读取外部文件实现（注意：Locust 的负载是通过 单进程 + 多协程 的实现，并非 多进程 + 多线程）。 

**1. 从 CSV 中读取参数实现参数化**

```powershell
# user_info.csv
aaa,123
bbb,123
ccc,123
```

```python
from locust import HttpUser, task, constant, SequentialTaskSet
import queue


class TaskCase(SequentialTaskSet):

    @task
    def login(self):
        user = self.user.user_list.get()

        ret = self.client.get("/login")
        aa = ret.headers['Set-Cookie']
        csrf1 = aa.split(";")[0].split("=")[1]
        csrf2 = aa.split(";")[0]
        header = {
            "Cookie": csrf2}

        data = {
            "user": user["username"],
            "pwd": user["password"],
            "csrfmiddlewaretoken": csrf1
        }

        ret = self.client.post(
            "/login/", headers=header, data=data)

        print(ret.status_code)
        # 登录后的一系列操作
        self.user.user_list.put_nowait(user)


class ApiUser(HttpUser):
    wait_time = constant(0)
    tasks = [TaskCase]

    user_list = queue.Queue()
    with open("./user_info.csv") as file:
        for line in file:
            userInfo = line.split(',')
            data = {
                "username": userInfo[0],
                "password": userInfo[1]
            }

            user_list.put_nowait(data)

if __name__ == '__main__':
    import os

    os.system("locust -f test1.py --host=http://127.0.0.1:8000/")
```

**实现效果**

登录3个用户，a、b、c三个用户，执行登录

### 3.8 其他属性

#### 3.8.1 @task装饰器

当负载测试开始时，将为每个模拟用户创建一个 User 类的实例，并且他们将开始在自己的绿色线程中运行。当这些用户运行时，他们选择他们执行的任务，睡一会儿，然后选择一个新任务等等。

这些任务是普通的 Python 可调用项，如果我们对拍卖网站进行负载测试，它们可以执行诸如“加载起始页”、“搜索某些产品”、“出价”等操作。 为用户添加任务的最简单方法是使用  @task 装饰器。

```python
@task
def index_page(self):
    self.client.get("/studentcenter/adv/GetAdvertList", headers=self.header)

@task(3)
def view_item(self):
	item_id = random.randint(1, 11)
	self.client.get("/StudentCenter/Navigation/menu?bust=1640683458756&id=%s&_=1640683458093" % item_id, headers=self.header, name="/item")
```

 **@task** 接受一个可选的权重参数，可用于指定任务的执行率。在以下示例中，*task2*被选中的机会是task1的3倍

#### 3.8.2 @tag装饰器

通过使用 @tag 装饰器标记任务，您可以使用`--tags`和`--exclude-tags`参数对在测试期间执行的任务进行挑剔。考虑以下示例： 

```python
from locust import User, constant, task, tag

class MyUser(User):
    wait_time = constant(1)

    @tag('tag1')
    @task
    def task1(self):
        pass

    @tag('tag1', 'tag2')
    @task
    def task2(self):
        pass

    @tag('tag3')
    @task
    def task3(self):
        pass

    @task
    def task4(self):
        pass
```

```powershell
--tags tag1   --tags tag2 tag3：
如果您使用 开始此测试，则在测试期间只会执行task1和task2。如果以 开头，则只会执行task2和task3。 
--exclude-tags：
会以完全相反的方式表现。所以，如果你开始测试 ，只有 TASK1 ，TASK2 和 task4 将被执行。排除总是胜过包含，所以如果一个任务有一个你已经包含的标签和一个你已经排除的标签，它就不会被执行。--exclude-tags tag3
```

#### 3.8.2 侦听器

如果你想运行一些设置代码作为测试的一部分，通常将它放在 locustfile 的模块级别就足够了，但有时你需要在运行中的特定时间做一些事情。为了这个需求，Locust 提供了事件钩子。 

 如果您需要在负载测试开始或停止时运行一些代码，您应该使用  on_test_start 和 on_test_stop 事件。您可以在 locustfile 的模块级别为这些事件设置侦听器： 

```python
from locust import events

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")
```

该 init 事件在每个 Locust 进程开始时触发。这在分布式模式中特别有用，在这种模式下，每个工作进程（而不是每个用户）都需要有机会进行一些初始化。例如，假设您有一些全局状态，所有从此进程生成的用户都需要： 

```python
from locust import events
from locust.runners import MasterRunner

@events.init.add_listener
def on_locust_init(environment, **kwargs):
    if isinstance(environment.runner, MasterRunner):
        print("I'm on master node")
    else:
        print("I'm on a worker or standalone node")
```

```python
import time
from locust import HttpUser, task, between, events
import urllib3
from locust.contrib.fasthttp import FastHttpLocust

urllib3.disable_warnings()


@events.test_start.add_listener
def on_test_start(**kwargs):
    print('===测试最开始提示===')


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print('===测试结束了提示===')


class TestTask(HttpUser):
    wait_time = between(1, 5)

    # host = 'https://www.baidu.com'

    def on_start(self):
        print('这是SETUP，每次实例化User前都会执行！')

    @task(1)
    def getBaidu(self):
        self.client.get(url="/", verify=False)

    def on_stop(self):
        print('这是TEARDOWN，每次销毁User实例时都会执行！')


if __name__ == "__main__":
    import os

    os.system("locust -f locust1.py --host=https://www.baidu.com")
```

执行结果：

```powershell
===测试最开始提示===
[2021-12-29 18:48:50,820] DESKTOP-C09SST2/INFO/locust.runners: Ramping to 1 users at a rate of 1.00 per second
[2021-12-29 18:48:50,821] DESKTOP-C09SST2/INFO/locust.runners: All users spawned: {"TestTask": 1} (1 total users)
这是SETUP，每次实例化User前都会执行！
这是TEARDOWN，每次销毁User实例时都会执行！
===测试结束了提示===
```

#### 3.8.3 HttpUser类

HttpUser是最常用的User，它添加了一个 client用于发出Http请求的属性。

```python
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(5, 15)

    @task(4)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about/")
```

#### 3.8.4 weight 属性

如果文件中存在多个 locust 类，并且在命令行上未指定 locust;

则每个新的实例都会从现有 locust 类中随机选择。

如果不想这么做，您可以从同一文件中指定要使用的 locust；

如下所示：

```python
$ locust -f locust_file.py WebUserLocust MobileUserLocust
```

如果希望让某个 locust 类经常被执行，可以在这些类上设置一个 weight 属性。

举例来说，PC 浏览用户的可能性是手机端用户的三倍，可以像下面这种设置：

```python
class WebUserLocust(Locust):    
    weight = 3    
    ...

class MobileUserLocust(Locust):    
    weight = 1    
    ...
```

### 3.9 配置

**环境配置**

大多数可以通过命令行参数设置的选项也可以通过环境变量设置。例子：

```python
$ LOCUST_LOCUSTFILE=custom_locustfile.py locust
```

**配置文件**
配置文件路径：~/.locust.conf		./locust.conf     可以使用 --config 标志指定一个附加文件

示例：

```python
# master.conf in current directory
locustfile = locust_files/my_locust_file.py
headless = true
master = true
expect-workers = 5
host = http://target-system
users = 100
spawn-rate = 10
run-time = 10m
```

```python
locust --config=master.conf
```

**配置选项**

| 命令行                      | 环境                             | 配置文件                  | 描述                                                         |
| --------------------------- | -------------------------------- | ------------------------- | ------------------------------------------------------------ |
| `-f`, `--locustfile`        | `LOCUST_LOCUSTFILE`              | `locustfile`              | 要导入的 Python 模块文件，例如“../other.py”。默认值：locustfile |
| `-H`, `--host`              | `LOCUST_HOST`                    | `host`                    | 主机按以下格式进行负载测试：[http](http://10.21.32.33/) : [//10.21.32.33](http://10.21.32.33/) |
| `-u`, `--users`             | `LOCUST_USERS`                   | `users`                   | 并发 Locust 用户的峰值数量。主要与 –headless 或 –autostart 一起使用。可以在测试期间通过键盘输入 w、W（生成 1、10 个用户）和 s、S（停止 1、10 个用户）更改 |
| `-r`, `--spawn-rate`        | `LOCUST_SPAWN_RATE`              | `spawn-rate`              | 产生用户的速率（每秒用户数）。主要与 –headless 或 –autostart 一起使用 |
| `--hatch-rate`              | `LOCUST_HATCH_RATE`              | `hatch-rate`              | ==抑制==                                                     |
| `-t`, `--run-time`          | `LOCUST_RUN_TIME`                | `run-time`                | 在指定的时间后停止，例如（300s、20m、3h、1h30m 等）。仅与 –headless 或 –autostart 一起使用。默认永远运行。 |
| `--web-host`                | `LOCUST_WEB_HOST`                | `web-host`                | 将 Web 界面绑定到的主机。默认为“*”（所有接口）               |
| `--web-port`, `-P`          | `LOCUST_WEB_PORT`                | `web-port`                | 运行网络主机的端口                                           |
| `--headless`                | `LOCUST_HEADLESS`                | `headless`                | 禁用 Web 界面，并立即开始测试。使用 -u 和 -t 来控制用户数量和运行时间 |
| `--autostart`               | `LOCUST_AUTOSTART`               | `autostart`               | 立即开始测试（不禁用 Web UI）。使用 -u 和 -t 来控制用户数量和运行时间 |
| `--autoquit`                | `LOCUST_AUTOQUIT`                | `autoquit`                | 在运行完成 X 秒后完全退出 Locust。仅与–autostart 一起使用。默认是保持 Locust 运行，直到您使用 CTRL+C 将其关闭 |
| `--headful`                 | `LOCUST_HEADFUL`                 | `headful`                 | ==抑制==                                                     |
| `--web-auth`                | `LOCUST_WEB_AUTH`                | `web-auth`                | 为 Web 界面启用基本身份验证。应按以下格式提供：用户名：密码  |
| `--tls-cert`                | `LOCUST_TLS_CERT`                | `tls-cert`                | 用于通过 HTTPS 提供服务的 TLS 证书的可选路径                 |
| `--tls-key`                 | `LOCUST_TLS_KEY`                 | `tls-key`                 | 用于通过 HTTPS 提供服务的 TLS 私钥的可选路径                 |
| `--master`                  | `LOCUST_MODE_MASTER`             | `master`                  | 设置 locust 以分布式模式运行，此进程作为主进程               |
| `--master-bind-host`        | `LOCUST_MASTER_BIND_HOST`        | `master-bind-host`        | locust master 应该绑定的接口（主机名、ip）。仅在使用 –master 运行时使用。默认为 *（所有可用接口）。 |
| `--master-bind-port`        | `LOCUST_MASTER_BIND_PORT`        | `master-bind-port`        | locust master 应该绑定的端口。仅在使用 –master 运行时使用。默认为 5557。 |
| `--expect-workers`          | `LOCUST_EXPECT_WORKERS`          | `expect-workers`          | 在开始测试之前，master 应该连接多少工人（仅当使用 –headless/autostart 时）。 |
| `--expect-workers-max-wait` | `LOCUST_EXPECT_WORKERS_MAX_WAIT` | `expect-workers-max-wait` | 在放弃之前，主人应该等待工人连接多长时间。默认永远等待       |
| `--worker`                  | `LOCUST_MODE_WORKER`             | `worker`                  | 设置 locust 以分布式模式运行，此进程作为工作线程             |
| `--master-host`             | `LOCUST_MASTER_NODE_HOST`        | `master-host`             | 用于分布式负载测试的locust master的主机或IP地址。仅在与 –worker 一起运行时使用。默认为 127.0.0.1。 |
| `--master-port`             | `LOCUST_MASTER_NODE_PORT`        | `master-port`             | locust master 使用的连接端口用于分布式负载测试。仅在与 –worker 一起运行时使用。默认为 5557。 |
| `-T`, `--tags`              | `LOCUST_TAGS`                    | `tags`                    | 要包含在测试中的标签列表，因此只会执行具有任何匹配标签的任务 |
| `-E`, `--exclude-tags`      | `LOCUST_EXCLUDE_TAGS`            | `exclude-tags`            | 要从测试中排除的标签列表，因此只会执行没有匹配标签的任务     |
| `--csv`                     | `LOCUST_CSV`                     | `csv`                     | 将当前请求统计信息以 CSV 格式存储到文件中。设置此选项将生成三个文件：[CSV_PREFIX]_stats.csv、[CSV_PREFIX]_stats_history.csv 和 [CSV_PREFIX]_failures.csv |
| `--csv-full-history`        | `LOCUST_CSV_FULL_HISTORY`        | `csv-full-history`        | 将每个统计条目以 CSV 格式存储到 _stats_history.csv 文件。您还必须指定“–csv”参数以启用此功能。 |
| `--print-stats`             | `LOCUST_PRINT_STATS`             | `print-stats`             | 在控制台打印统计信息                                         |
| `--only-summary`            | `LOCUST_ONLY_SUMMARY`            | `only-summary`            | 只打印汇总统计信息                                           |
| `--reset-stats`             | `LOCUST_RESET_STATS`             | `reset-stats`             | 生成完成后重置统计信息。在分布式模式下运行时，应在 master 和 worker 上都设置 |
| `--html`                    | `LOCUST_HTML`                    | `html`                    | 存储 HTML 报告文件                                           |
| `--skip-log-setup`          | `LOCUST_SKIP_LOG_SETUP`          | `skip-log-setup`          | 禁用 Locust 的日志记录设置。相反，配置由 Locust 测试或 Python 默认值提供。 |
| `--loglevel`, `-L`          | `LOCUST_LOGLEVEL`                | `loglevel`                | 在调试/信息/警告/错误/关键之间进行选择。默认为信息。         |
| `--logfile`                 | `LOCUST_LOGFILE`                 | `logfile`                 | 日志文件的路径。如果未设置，日志将转到 stderr                |
| `--exit-code-on-error`      | `LOCUST_EXIT_CODE_ON_ERROR`      | `exit-code-on-error`      | 设置当测试结果包含任何失败或错误时使用的进程退出代码         |
| `-s`, `--stop-timeout`      | `LOCUST_STOP_TIMEOUT`            | `stop-timeout`            | 在退出之前等待模拟用户完成任何正在执行的任务的秒数。默认是立即终止。该参数只需要在运行 Locust 分布式时为 master 进程指定。 |

### 3.10 执行模式

**1. Web UI 模式：**

在这个模式下，你可以通过 Web 控制场景的执行、实时的了解被测试应用性能表现趋势，但是 Locust 没有提供主流压测工具那样的丰富图表，你能看到的只有：

- 每秒发出的请求数
- 请求的响应事件
- 运行中的“用户数”

其实，从性能测试的角度来看，图表只要足够表示负载的增加对性能趋势的影响、事件关系就足够了。

**2. 命令行模式：**

- 脚本开发调试过程中，出于工作效率的目的，建议使用该模式
- 如果你使用了远程主机作为负载机，不想麻烦运维同学开通端口权限，可以使用命令行模式运行压测

```python
locust --headless --users 10 --spawn-rate 1 -H http://your-server.com
```

你可以在没有 Web UI 的情况下运行 locust - 例如，如果你想在一些自动化流程中运行它，比如 CI 服务器 - 通过将`--headless`标志与`-u`and一起使用`-r`： 

```python
locust -f locust_files/my_locust_file.py --headless -u 1000 -r 100
```

 `-u`指定生成的用户数，并`-r`指定生成速率（每秒启动的用户数）。 

在测试运行时，您可以手动更改用户计数，即使在启动完成后也是如此。按 w 添加 1 个用户或按 W 添加 10。按 s 删除 1 或按 S 删除 10。 

**2.1 设置测试时间限制：**

如果要指定测试的运行时间，可以使用`--run-time`或 来完成`-t`：

```python
$ locust -f --headless -u 1000 -r 100 --run-time 1h30m
```

一旦时间到，Locust 将关闭。

**2.2 允许任务在关闭时完成迭代：**

默认情况下，locust 会立即停止您的任务（甚至无需等待请求完成）。如果你想让你的任务完成它们的迭代，你可以使用.`--stop-timeout ` 

```python
locust -f --headless -u 1000 -r 100 --run-time 1h30m --stop-timeout 99
```

**2.3 在没有 Web UI 的情况下运行 Locust 分布式：**

如果要在没有 Web UI 的情况下运行 Locust 分布式，则应`--expect-workers`在启动主节点时指定该选项，以指定预期连接的工作节点数。然后它会等到许多工作节点连接后才开始测试。

**2.4 控制 Locust 进程的退出代码**

在 CI 环境中运行 Locust 时，您可能希望控制 Locust 进程的退出代码。您可以通过设置实例的来在测试脚本 process_exit_code 中执行此操作 Environment。

下面是一个示例，如果满足以下任何条件，则将退出代码设置为非零：

- 超过 1% 的请求失败
- 平均响应时间大于200毫秒
- 响应时间的第 95 个百分位数大于 800 毫秒

```python
import logging
from locust import events

@events.quitting.add_listener
def _(environment, **kw):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 1%")
        environment.process_exit_code = 1
    elif environment.stats.total.avg_response_time > 200:
        logging.error("Test failed due to average response time ratio > 200 ms")
        environment.process_exit_code = 1
    elif environment.stats.total.get_response_time_percentile(0.95) > 800:
        logging.error("Test failed due to 95th percentile response time > 800 ms")
        environment.process_exit_code = 1
    else:
        environment.process_exit_code = 0
```

**2.5 以 CSV 格式检索测试统计信息**

您可能希望通过 CSV 文件使用 Locust 结果。在这种情况下，有两种方法可以做到这一点。

首先，当使用 Web UI 运行 Locust 时，您可以在“下载数据”选项卡下检索 CSV 文件。

其次，您可以使用一个标志运行 Locust，该标志将定期保存三个 CSV 文件。如果您计划使用以下`--headless`标志以自动方式运行 Locust，这将特别有用：

```python
$ locust -f examples/basic.py --csv=example --headless -t10m
```

这些文件将被命名为`example_stats.csv`,`example_failures.csv`和`example_history.csv` （使用时`--csv=example`）。前两个文件将包含整个测试运行的统计信息和失败情况，每个统计信息条目（URL 端点）各占一行，聚合行占一行。该`example_history.csv` 会得到新行*电流*（10秒滑动窗口）在整个试运行期间追加统计。默认情况下，只有 Aggregate 行会定期附加到历史统计数据中，但如果 Locust 以该`--csv-full-history`标志启动，则每次写入统计数据时都会为每个 stats 条目（和 Aggregate）附加一行（默认情况下每 2 秒一次） .

如果您希望更快（或更慢）写入，您还可以自定义写入的频率：

```python
import locust.stats
locust.stats.CSV_STATS_INTERVAL_SEC = 5 # default is 1 second
locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 60 # Determines how often the data is flushed to disk, default is 10 seconds
```

### 3.11 分布式负载

运行 Locust 的单个进程可以模拟相当高的吞吐量。对于一个简单的测试计划，它应该能够每秒发出数百个请求，如果使用 FastHttpUser 则可以发出数千个请求。

但是，如果您的测试计划很复杂，或者您想要运行更多负载，则需要扩展到多个进程，甚至可能是多台机器。

为此，您使用该`--master`标志以主模式启动 Locust 的一个实例，并使用该标志启动多个工作器实例`--worker`。如果 worker 与 master 不在同一台机器上，您可以`--master-host`将它们指向运行 master 的机器的 IP/主机名。

主实例运行 Locust 的 Web 界面，并告诉工作人员何时产生/停止用户。工作人员运行您的用户并将统计信息发送回主人。主实例本身不运行任何用户。

运行 Locust 分布式时，master 和 worker 机器都必须有 locustfile 的副本。

示例：

以主模式启动

```python
locust -f my_locustfile.py --master
```

然后在每个工人上（用主机的 IP替换，或者如果您的工人与主机在同一台机器上，则完全省略参数）： 

```python
locust -f my_locustfile.py --worker --master-host=192.168.254.132
```

> **--master**
>
> 将蝗虫设置为主模式。Web 界面将在此节点上运行。
>
> **--worker**
>
> 将蝗虫设置为工人模式。
>
> **--master-host=X.X.X.X**
>
> 可选地与`--worker`设置主节点的主机名/IP一起使用（默认为 127.0.0.1）
>
> **--master-port=5557**
>
> 可选地与 with`--worker`一起设置主节点的端口号（默认为 5557）。
>
> **--master-bind-host=X.X.X.X**
>
> 可选择与`--master`. 确定主节点将绑定到的网络接口。默认为 *（所有可用接口）。
>
> **--master-bind-port=5557**
>
> 可选择与`--master`. 确定主节点将侦听哪些网络端口。默认为 5557。
>
> **--expect-workers=X**
>
> 用 启动主节点时使用`--headless`。在开始测试之前，主节点将等待 X 个工作节点连接。

### 3.12 Doocker中运行

假如 locustfie.py存在于当前工作目录中：

```python
docker run -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py
```

这是一个示例 Docker Compose 文件，可用于启动主节点和工作节点： 

```
version: '3'

services:
  master:
    image: locustio/locust
    ports:
     - "8089:8089"
    volumes:
      - ./:/mnt/locust
    command: -f /mnt/locust/locustfile.py --master -H http://master:8089
  
  worker:
    image: locustio/locust
    volumes:
      - ./:/mnt/locust
    command: -f /mnt/locust/locustfile.py --worker --master-host master
```

上面的 compose 配置可用于使用以下命令启动一个主节点和 4 个工作节点：

```python
docker-compose up --scale worker=4
```

拥有依赖第三方 python 包的测试脚本是很常见的。在这些情况下，您可以使用官方 Locust docker 镜像作为基础镜像：

```python
FROM locustio/locust
RUN pip3 install some-python-package
```

### 3.13 提高HTTP请求性能

Locust 的默认 HTTP客户端 是使用 `python-requests`来实现的，它提供了许多python开发人员都熟悉的API。

因此，在通常情况下，我们建议您使用这个作为 HttpLocust 的默认。

但是，如果你打算真实的跑一个大规模测试，Locust有一个备用的HTTP客户端 `FastHttpLocust`，它使用 `geventhttpclient` 代替 `requests`。

这个http客户端的速度提高非常明显，经过测试发现HTTP请求的性能提高了5到6倍（还是非常给力的）。

但是这并不意味每个CPU内核可以模拟的用户数量会增加5到6倍，因为这还取决于负载测试脚本的多方面因素。

但是，如果你的 `locust` 脚本在执行HTTP请求时花费了大量的CPU时间，切换到 `FastHttpLocust` 会让你看到明显的性能提升。

**注意：这是属于提高你的HTTP请求的性能，只做这一件事，和其它流程中的性能是没关系的；** 

**如何使用FastHttpLocust**

First, you need to install the geventhttplocust python package:

首先，您需要安装 `geventhttplocust` 的python包：

```python
pip install geventhttpclient
```

然后，您只将FastHttpLocust而不是HttpLocust子类化：

```python
from locust import TaskSet, task
from locust.contrib.fasthttp import FastHttpLocust
class MyTaskSet(TaskSet):
    @task
    def index(self):
        response = self.client.get("/")
class MyLocust(FastHttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 60000
```

注意：与使用**python-requests**的默认HttpLocust相比，`FastHttpLocust`的实现API会不同。这取决于如何使用HttpClient，FastHttpLocust可能无法完全替代HttpLocust。 

**API：**

> ### 类 FastHttpSession(`base_url`, `**kwargs`)
>
> - `__init__(base_url, **kwargs)`
>
>   - x.__init__(…) 初始化x; 参见help（type（x））进行签名
>
> - `get(path, **kwargs)`
>
>   - 发送一个GET请求
>
> - `head(path, **kwargs)`
>
>   - 发送HEAD请求
>
> - `options(path, **kwargs)`
>
>   - 发送一个OPTIONS请求
>
> - `patch(path, data=None, **kwargs)`
>
>   - 发送POST请求
>
> - `post(path,data=None, **kwargs)`
>
>   - 发送POST请求
>
> - `put(path, data=None, **kwargs)`
>
>   - 发送一个PUT请求
>
> - `request(method, path, name=None, data=None, catch_response=False, stream=False, headers=None, auth=None, **kwargs)`
>
>   发送和HTTP请求返回`locust.contrib.fasthttp.FastResponse`对象。

| 参数           | is_necessary | 说明                                                         |
| :------------- | :----------- | :----------------------------------------------------------- |
| method         | 必须         | 新Request对象的方法。                                        |
| path           | 必须         | 将与指定的基本主机URL并置的路径。也可以是完整URL，在这种情况下，将请求完整URL，并且忽略基本主机。 |
| name           | 可选         | 一个参数，可以指定为在Locust的统计信息中用作标签，而不是URL路径。这可用于在Locust的统计信息中将请求的不同URL分组为单个条目。 |
| catch_response | 可选         | 布尔型参数，如果已设置，则可用于发出请求，以返回上下文管理器以用作with语句的参数。即使响应代码正常（2xx），也可以根据响应的内容将请求标记为失败。相反的方法也可行，即使没有响应代码（即500或404），也可以使用catch_response来捕获请求，然后将其标记为成功。 |
| 数据           | 可选         | 在请求正文中发送的字典或字节。                               |
| 标头           | 可选         | 与请求一起发送的HTTP 标头字典。                              |
| auth           | 可选         | 身份验证（用户名，密码）元组，以启用基本HTTP身份验证。       |
| stream         | 可选         | 如果设置为true，则不会立即使用响应主体，而是可以通过访问Response对象上的stream属性来使用它。将流设置为True的另一个副作用是，在Locust报告的请求时间中不会考虑下载响应内容的时间。 |

类 FastResponse(`ghc_response`, `request=None`, `sent_request=None`)

- content
  - 必要时解压缩并缓冲接收到的正文。小心大文件！
- headers= None
  - 包含响应头的类对象字典
- text
  - 以解码字符串的形式返回响应的文本内容（python2上的unicode）

### 3.14 日志设置

**日志记录**

Locust带有基本的日志记录配置，可以选择采用 `--loglevel` 和 `/` 或 `--logfile` 修改配置。

如果要控制日志记录配置，则可以提供 `--skip-log-setup` 标志，该标志将忽略其他参数。

**Options**

`--skip-log-setup`

禁用 Locust 的日志记录设置。用 Locust 测试 或 Python默认设置提 供配置。

`--loglevel`

在 DEBUG/INFO/WARNING/ERROR/CRITICAL 选择。默认值为 INFO 。 简写为`-L`。

`--logfile`

日志文件的路径。如果未设置，则日志将转到 stdout/stderr。

### 3.15 Locust API

#### 3.15.1 Locust 类

```python
class Locust
```

表示要被孵化并攻击要进行负载测试的系统的“用户”。

该用户的行为由 `task_set` 属性定义，该属性应指向一个 `TaskSet` 类。

此类通常应由定义某种客户端的类继承。

例如，当对 `HTTP` 系统进行负载测试时，您可能想使用 `HttpUser` 类。

##### 1. between

```python
wait_time = between(5, 10)
```

between 类，指定范围内随机（5~10秒）等待 

##### 2. constant

```python
wait_time = constant(3)
```

执行 Locust 任务之间的最短等待时间

##### 3.constant_pacing

```python
wait_time = constant_pacing(3)
```

constant_pacing 类，从上一次请求发起后，等待特定时间（3秒），再发起下一次请求，如果上一次请求的响应时间大于指定的时间（3秒），则在响应后立即发起下一次请求 

##### 4. task_set

```python
task_set = None
```

定义此 Locust 的执行行为的 TaskSet 类

##### 5. wait_function

```python
wait_function()
```

用于计算 Locust 任务执行之间的等待时间的函数（以毫秒为单位）

##### 6. weight

```python
weight = 10
```

locust 选择该 Locust 的可能性。

weight 越高，选择它的机会就越大。

#### 3.15.2 HttpLocust 类

```python
class HttpUser
```

表示要被孵化并攻击要进行负载测试的系统的 HTTP “用户”。

该用户的行为由 task_set 属性定义，该属性应指向一个 `TaskSet` 类。

此类在实例化时创建一个客户端属性，该属性是一个 HTTP 客户端，支持在请求之间保持用户会话。

##### 1. client

```
client  = None
```

在 Locust 实例化后创建的 HttpSession 实例。客户端支持 cookie，因此保持 HTTP 请求之间的会话。

#### 3.15.3 TaskSet 类

```python
classTaskSet(parent)
```

定义 Locust 用户将执行的一组任务的类。

当 TaskSet 开始运行时，它将从 task 属性中选择一个任务，执行该任务，并调用其 wait_function 来定义睡眠时间。默认为 min_wait 和 max_wait 毫秒之间的均匀分布的随机数。然后它将安排另一个任务执行，依此类推。

TaskSet 可以嵌套，这意味着 TaskSet 的 task 属性可以包含另一个 TaskSet。如果嵌套 TaskSet 计划执行，则将从当前正在执行的 TaskSet 中实例化并调用它。然后，当前正在运行的 TaskSet 中的执行将移交给嵌套的 TaskSet，它将继续运行，直到它抛出 InterruptTaskSet 异常为止，该异常在`TaskSet.interrupt()`调用时完成 。（然后执行将在第一个 TaskSet 中继续）。

##### 1. client

引用 `client` 根 Locust 实例的属性。

##### 2. interrupt

```python
interrupt(reschedule=True)
```

中断 TaskSet 并将执行控制移交给父 TaskSet。

如果 **reschedule** 为 True（默认值），则父 Locust 将立即重新安排并执行新任务

此方法不应由根 TaskSet（立即附加到 Locust 类的 task_set 属性的那个）调用，而应在层次结构中更深的嵌套 TaskSet 类中调用。

##### 3. locust

```python
locust = None
```

实例化 TaskSet 时，将引用根 Locust 类实例

##### 4. max_wait

```python
max_wait = None
```

执行 Locust 任务之间的最长等待时间。可用于覆盖在根 Locust 类中定义的 **max_wait** ，如果未在 TaskSet 上设置，则将使用它。

##### 5. min_wait

```python
min_wait = None
```

执行 Locust 任务之间的最短等待时间。可用于覆盖在根 Locust 类中定义的 **min_wait** ，如果未在 TaskSet 上设置，则将使用它们。

##### 6. parent

```python
parent = None
```

实例化 TaskSet 时，将引用父 `TaskSet` 或 `Locust` 类实例。对于嵌套 TaskSet 类很有用。

##### 7. schedule_task

```python
schedule_task(task_callable, args=None, kwargs=None, first=False)
```

将任务添加到 Locust 的任务执行队列中。

| 参数          | 说明                                                      |
| :------------ | :-------------------------------------------------------- |
| task_callable | Locust 任务计划                                           |
| args          | 将传递给可调用任务的参数                                  |
| kwargs        | 将传递给可调用任务的关键字参数的字典。                    |
| first         | 可选关键字参数。如果为 True，则将任务放在队列中的第一位。 |

##### 8. tasks

```python
tasks= []
```

带有代表 Locust 用户任务的 python 可调用对象的列表。

如果任务是列表，则将随机选择要执行的任务。

如果任务是一个包含两个元组的（可调用，整数）列表，或者是一个{`callable：int`}字典，则将随机选择要执行的任务，但是将根据每个任务的相应 int 值对它们进行加权。因此，在以下情况下，选择 ThreadPage 的可能性是 write_post 的十五倍：

```
class ForumPage(TaskSet):    tasks = {ThreadPage:15, write_post:1}
```

##### 9. wait_function

```python
wait_function= None
```

在 Locust 任务执行之间用于计算等待时间的函数（以毫秒为单位）。可用于覆盖在根 Locust 类中定义的 `wait_function` ，如果未在 TaskSet 上设置，则将使用它。

#### 3.15.4 task decorator

##### 1.task

```python
task(weight=1)
```

用作便捷装饰器，以便能够为类中的 TaskSet 内联声明任务。例：

```python
class ForumPage(TaskSet):    
    
	@task(100)    
	def read_thread(self):        
	pass    
	
	@task(7)    
	def create_thread(self):        
	pass
```

#### 3.15.5 TaskSequence 类

```python
class TaskSequence(parent)
```

定义 Locust 用户将执行的任务序列的类。

当 TaskSequence 开始运行时，它将从 task 属性中选择索引中的任务，执行该任务，并调用其 `wait_function` 来定义睡眠时间。默认为 `min_wait` 和 `max_wait` 毫秒之间的均匀分布的随机数。

然后，它将安排 索引 + 1％len（tasks）任务执行，依此类推。

TaskSequence 可以与 TaskSet 嵌套，这意味着 TaskSequence 的 task 属性可以包含 TaskSet 实例以及其他 TaskSequence 实例。

如果嵌套的 TaskSet 被安排执行，它将从当前正在执行的 TaskSet 中实例化并调用。然后，当前正在运行的 TaskSet 中的执行将移交给嵌套的 TaskSet，它将继续运行，直到它抛出 InterruptTaskSet 异常为止，该异常在 TaskSet.interrupt() 调用时完成 。

（然后执行将在第一个 TaskSet 中继续）。

在此类中，应将任务定义为列表，或仅使用 @seq_task 装饰器定义任务

##### 1. client

引用 `client` 根 Locust 实例的属性。

##### 2. interrupt

```python
interrupt(reschedule=True)
```

中断 TaskSet 并将执行控制移交给父 TaskSet。

如果 reschedule 为 True（默认值），则父 Locust 将立即重新安排并执行新任务

此方法不应由根 TaskSet（立即附加到 Locust 类的 task_set 属性的那个）调用，而应在层次结构中更深的嵌套 TaskSet 类中调用。

##### 3. schedule_task

```python
schedule_task(task_callable, args=None, kwargs=None, first=False)
```

将任务添加到 Locust 的任务执行队列中。

| 参数          | 说明                                                      |
| :------------ | :-------------------------------------------------------- |
| task_callable | Locust 任务计划                                           |
| args          | 将传递给可调用任务的参数                                  |
| kwargs        | 将传递给可调用任务的关键字参数的字典。                    |
| first         | 可选关键字参数。如果为 True，则将任务放在队列中的第一位。 |

#### 3.15.6 seq_task decorator

```
seq_task(order)
```

用作便捷装饰器，以便能够为类中的 TaskSequence 内联声明任务。

例如：

```python
class NormalUser(TaskSequence):   

	@seq_task(1)    
	def login_first(self):        
	pass    
	
	@seq_task(2)    
	@task(25) 
	# You can also set the weight in order to execute the task for `weight` times one after another.    
	def then_read_thread(self):        
	pass    
	
	@seq_task(3)    
	def then_logout(self):        
	pass
```

#### 3.15.7 HttpSession 类

```python
HttpSession(base_url, *args, **kwargs)
```

用于执行 Web 请求和在请求之间保留（会话）Cookie 的类（以便能够登录和注销网站）。

记录每个请求，以便 Locust 可以显示统计信息。

这是 `python-request` 的 `requests.Session` 类的稍微扩展的版本，大多数情况下，该类的工作原理完全相同。但是，发出请求的方法 (get, post, delete, put, head, options, patch, request)

现在可以采用 url 参数，该参数仅是 URL 的路径部分，在这种情况下，URL 的主机部分将被添加带有通常从 Locust 类的 host 属性继承的 `HttpSession.base_url` 。

每个发出请求的方法还带有两个附加的可选参数，这些参数是 Locust 特定的，并且在 **python-requests** 中不存在。这些是： 

| 参数               | is_necessary | 说明                                                         |
| :----------------- | :----------- | :----------------------------------------------------------- |
| **name**           | （可选）     | 一个参数，可以指定为在 Locust 的统计信息中用作标签，而不是 URL 路径。这可用于在 Locust 的统计信息中将请求的不同 URL 分组为单个条目。 |
| **catch_response** | （可选）     | 布尔型参数，如果已设置，则可用于发出请求，以返回上下文管理器以用作 with 语句的参数。即使响应代码正常（2xx），也可以根据响应的内容将请求标记为失败。相反的方法也可行，即使没有响应代码（即 500 或 404），也可以使用 catch_response 来捕获请求，然后将其标记为成功。 |

##### 1. `__init__`

```
__init__(base_url, *args, **kwargs)
```

x.__init__(…) 初始化 x; 参见 help（type（x））进行签名

##### 2. delete

```
delete(url, **kwargs)
```

发送一个 DELETE 请求。返回 `Response` 对象。

| 参数       | 说明                       |
| :--------- | :------------------------- |
| url        | 新 `Request` 对象的 URL 。 |
| `**kwargs` | 可选参数 `request` 。      |

 返回类型 ：requests.Response

##### 3. get

```
get(url, **kwargs)
```

发送 GET 请求。返回 `Response` 对象。

| 参数       | 说明                       |
| :--------- | :------------------------- |
| url        | 新 `Request` 对象的 URL 。 |
| `**kwargs` | 可选参数 `request` 。      |

**返回类型** ：requests.Response

##### 4. head

```
head(url, **kwargs)
```

发送 HEAD 请求。返回 `Response` 对象。

| 参数       | 说明                       |
| :--------- | :------------------------- |
| url        | 新 `Request` 对象的 URL 。 |
| `**kwargs` | 可选参数 `request` 。      |

**返回类型** ：requests.Response

##### 5. options

```
options(url, **kwargs)
```

发送一个 OPTIONS 请求。返回 `Response` 对象。

| 参数       | 说明                       |
| :--------- | :------------------------- |
| url        | 新 `Request` 对象的 URL 。 |
| `**kwargs` | 可选参数 `request` 。      |

**返回类型** ：requests.Response

##### 6. patch

```
patch(url, data=None, **kwargs)
```

发送 PATCH 请求。返回 `Response` 对象。

| 参数       | 说明                                                         |
| :--------- | :----------------------------------------------------------- |
| url        | 新 `Request` 对象的 URL 。                                   |
| data       | （可选）字典，元组列表，字节或要在的正文中发送的类似文件的对象 `Request` 。 |
| `**kwargs` | 可选参数 request。                                           |

**返回类型** ：requests.Response

##### 7. post

```
post(url, data=None, json=None, **kwargs)
```

发送 POST 请求。返回 `Response` 对象。

| 参数       | 说明                                                         |
| :--------- | :----------------------------------------------------------- |
| url        | 新 `Request` 对象的 URL 。                                   |
| data       | （可选）字典，元组列表，字节或要在的正文中发送的类似文件的对象 `Request` 。 |
| json       | （可选）要发送的正文的 json `Request` 。                     |
| `**kwargs` | 可选参数 request。                                           |

**返回类型** ：requests.Response

##### 8. put

```
put（url，data = None，** kwargs ）
```

发送一个 PUT 请求。返回 `Response` 对象。

| 参数       | 说明                                                         |
| :--------- | :----------------------------------------------------------- |
| url        | 新 `Request` 对象的 URL 。                                   |
| data       | （可选）字典，元组列表，字节或要在的正文中发送的类似文件的对象 `Request` 。 |
| `**kwargs` | 可选参数 request。                                           |

**返回类型** ：requests.Response

##### 9. request

```
request（method，url，name = None，catch_response = False，** kwargs ）
```

构造并发送 `requests.Request`。返回 `requests.Response` 对象。

| 参数                    | 说明                                                         |
| :---------------------- | :----------------------------------------------------------- |
| method                  | 新 Request 对象的方法。                                      |
| url                     | 新 Request 对象的 URL 。                                     |
| name                    | （可选）一个参数，可以指定为在 Locust 的统计信息中用作标签，而不是 URL 路径。这可用于在 Locust 的统计信息中将请求的不同 URL 分组为单个条目。 |
| catch_response          | （可选）布尔型参数，如果已设置，则可用于发出请求，以返回上下文管理器以用作 with 语句的参数。即使响应代码正常（2xx），也可以根据响应的内容将请求标记为失败。相反的方法也可行，即使没有响应代码（即 500 或 404），也可以使用 catch_response 来捕获请求，然后将其标记为成功。 |
| params                  | （可选）要在查询字符串中发送的字典或字节 Request。           |
| data                    | （可选）要在中发送的字典或字节 Request。                     |
| headers                 | （可选）与一起发送的 HTTP 标头字典 Request                   |
| cookies                 | （可选）与一起发送的 Dict 或 CookieJar 对象 Request。        |
| files                   | （可选）多部分编码上传的字典。‘filename’: file-like-objects  |
| auth                    | （可选）Auth 元组或可调用以启用基本 / 摘要 / 自定义 HTTP 身份验证。 |
| timeout(float or tuple) | （可选）在放弃之前，等待服务器发送数据的时间，以秒为单位，以 float 或（连接超时，读取超时）tuple 为单位。 |
| allow_redirects(bool)   | （可选）默认情况下设置为 True。                              |
| proxies                 | （可选）字典到代理 URL 的映射协议。                          |
| stream                  | （可选）是否立即下载响应内容。默认为 False。                 |
| verify                  | （可选）如果为 True，将验证 SSL 证书。也可以提供 CA_BUNDLE 路径。 |
| cert                    | （可选）如果为 String，则为 ssl 客户端证书文件（.pem）的路径。如果是元组，（“证书”，“密钥”）配对。 |

#### 3.15.8 Response 类

该类实际上位于 python-requests 库中，因为这是 Locust 用来发出 HTTP 请求的方法，但是由于在编写 Locust 负载测试时它是如此的重要，因此该类已包含在 locust 的 API 文档中。您也可以 `Response` 在请求文档中查看 该类 。

class Response

该 Response 对象，包含服务器对 HTTP 请求的响应。

##### 1. apparent_encoding

由 chardet 库提供的表观编码。

##### 2. close()

将连接释放回池。一旦调用了此方法，就 `raw` 不能再次访问基础对象。

注意：通常不需要显式调用。

##### 3. content

响应的内容，以字节为单位。

##### 4. cookies

```python
cookies= None
```

服务器发送回的 Cookie 的 CookieJar。

##### 5. elapsed

`elapsed` *= None*

从发送请求到响应到达之间经过的时间（以时间增量为单位）。此属性专门测量发送请求的第一个字节与完成头解析之间的时间。因此，通过使用响应内容或 stream 关键字参数的值不会受到影响。

##### 6. encoding

```python
encoding = None
```

访问 **r.text** 时进行编码以进行解码。

##### 7. headers

```python
headers= None
```

不区分大小写的响应标题字典。

例如，`headers['content-encoding']`将返回`'Content-Encoding'`响应头的值。

##### 8. history

```python
history= None
```

Response 请求历史记录中的对象列表。任何重定向响应都将在此处结束。

该列表从最早的请求到最新的请求进行排序。

##### 9. is_permanent_redirect

如果此响应是重定向的永久版本之一，则为 True。

##### 10. is_redirect

如果此响应是格式正确的 HTTP 重定向，并且可能已经被自动处理（由`Session.resolve_redirects()`），则为 true 。

##### 11. iter_content

```python
iter_content（chunk_size = 1，decode_unicode = False ）
```

遍历响应数据。当在请求上设置 stream = True 时，这避免了立即将内容读取到内存中以获得较大响应。块大小是它应读入内存的字节数。由于解码可以发生，这不一定是返回的每个项目的长度。

chunk_size 必须为 int 或 None 类型。值 None 将根据 stream 的值而有所不同。stream = True 将以到达接收到的块的大小读取数据。如果 stream = False，则将数据作为单个块返回。

如果 decode_unicode 为 True，将根据响应使用最佳可用编码对内容进行解码。

##### 12. iter_lines

```python
iter_lines(chunk_size=512, decode_unicode=False, delimiter=None)
```

遍历响应数据，一次一行。当在请求上设置 stream = True 时，这避免了立即将内容读取到内存中以获得较大响应。

> 注意：此方法不是可重入的安全方法。

##### 13. json

```
json(**kwargs)
```

返回响应的 json 编码内容（如果有）。

| Item       | 参数       | 说明                                              |
| :--------- | :--------- | :------------------------------------------------ |
| Parameters | `**kwargs` | Optional arguments that json.loads takes.         |
| Raises     | ValueError | If the response body does not contain valid json. |

##### 14. links

返回响应的已解析头链接（如果有）。

##### 15. next

如果存在重定向请求，则为重定向链中的下一个请求返回 `PreparedRequest` 。

##### 16. ok

如果 status_code 小于 400，则返回 True；否则，则返回 False。

此属性检查响应的状态码是否在 400 到 600 之间，以查看是否存在客户端错误或服务器错误。如果状态码在 200 到 400 之间，则返回 True。这不是检查响应代码是否为 `200 OK`.

##### 17. raise_for_status()

Raises stored `HTTPError`, if one occurred.

##### 18. reason

```python
reason= None
```

HTTP 状态响应的文字原因，例如 “Not Found” or “OK”.

##### 19. request

```python
request= None
```

`PreparedRequest`这是响应的对象。

##### 20. status_code

```python
status_code= None
```

响应的 HTTP 状态的整数代码，例如 404 或 200。

##### 21. text

```python
text
```

响应的内容，以 unicode 表示。

如果 **Response.encoding** 为 **None** ，将使用猜测编码 `chardet` 。

响应内容的编码仅基于 HTTP 头确定，该字母遵循 RFC 2616。如果可以利用非 HTTP 知识来更好地猜测编码，则应`r.encoding` 在访问此属性之前进行适当的设置。

##### 22. url

```python
url= None
```

响应的最终 URL 位置。

#### 3.15.9 ResponseContextManager 类

```python
classResponseContextManager(response)
```

Response 类还可以用作上下文管理器，该类提供了手动控制 HTTP 请求是否应在 Locust 统计信息中标记为成功还是失败的能力。

此类是 Response 带有两个附加方法的的子类： `success` 和 `failure` 。

##### 1. failure

```python
failure(exc)
```

将响应报告为失败。

exc 可以是 python 异常，也可以是字符串，在这种情况下，它将包装在 CatchResponseError 中。

Example:

```python
with self.client.get("/", catch_response=True) as response:    
	if response.content == b"":        
	response.failure("No data")
```

##### 2. success

```python
success()
```

报告响应成功

Example:

```python
with self.client.get("/does/not/exist", catch_response=True) as response:    
	if response.status_code == 404:        
	response.success()
```

#### 3.15.10 InterruptTaskSet 异常

```python
exceptionInterruptTaskSet(reschedule=True)
```

抛出任务时会打断 locust 的异常

#### 3.15.11 Event hooks

The event hooks are instances of the **locust.events.EventHook** class:

事件钩子 是 `locust.events.EventHook` 类的实例：

```python
class EventHook
```

简单事件类，用于为 Locust 中的不同类型的事件提供钩子。

这是使用 EventHook 类的方法：

```python
my_event = EventHook()
def on_my_event(a, b, **kw):    
	print "Event was fired with arguments: %s, %s" % (a, b)
	my_event += on_my_eventmy_event.fire(a="foo", b="bar")
```

如果 reverse 为 True，则处理程序将以插入时的相反顺序运行

#### 3.15.12 Available hooks

**locust.events**模块下提供以下事件挂钩：

```python
request_success= <locust.events.EventHook object>
```

成功完成请求后，将触发 `request_success` 。

监听器应采用以下参数：

- request_type：使用的请求类型方法
- name：所调用 URL 的路径（如果在调用客户端时使用，则覆盖名称）
- response_time：响应时间（以毫秒为单位）
- response_length：响应的内容长度

```python
request_failure= <locust.events.EventHook object>
```

请求失败时会触发 `request_failure`

使用以下参数触发事件：

- request_type：使用的请求类型方法
- name：所调用 URL 的路径（如果在调用客户端时使用，则覆盖名称）
- response_time：引发异常之前的时间（以毫秒为单位）
- exception：抛出的异常实例

```python
locust_error= <locust.events.EventHook object>
```

当在 Locust 类的执行中发生异常时，将触发 locust_error。

使用以下参数触发事件：

- locust_instance：发生异常的 Locust 类实例
- exception：抛出的异常
- tb：追溯对象（来自 sys.exc_info（）[2]）

```python
report_to_master= <locust.events.EventHook object>
```

当 Locust 在–slave 模式下运行时，将使用 `report_to_master` 。它可用于将数据附加到定期发送给主服务器的字典。要将报表发送到主服务器时会定期触发。

注意，键 “stats” 和 “errors” 由 Locust 使用，不应被覆盖。

使用以下参数触发事件：

- client_id：正在运行的 Locust 进程的客户端 ID。
- data：数据字典，可以修改以附加应发送到主数据库的数据。

```python
slave_report= <locust.events.EventHook object>
```

当 Locust 在 **master** 模式下运行时，将使用 `slave_report` ；当主服务器从 **Locust** 从属服务器收到报告时，将触发 `slave_report` 。

此事件可用于聚集来自 Locust 从属服务器的数据。

使用以下参数触发事件：

- client_id：报告 Locust 从属的客户端 ID
- data：数据字典与从属节点的数据

```python
hatch_complete= <locust.events.EventHook object>
```

产生所有 Locust 用户后会触发 hatch_complete。

使用以下参数触发事件：

- user_count：已孵化的用户数

```python
quitting= <locust.events.EventHook object>
```

Locust 进程退出时触发退出。



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