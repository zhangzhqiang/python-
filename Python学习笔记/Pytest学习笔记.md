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

 ![image](J:\homework\Python学习笔记\Pytest学习笔记.assets\tut_20200626162633_92.png) 

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

 ![img](J:\homework\Python学习笔记\Pytest学习笔记.assets\1437068-20200214160557341-574663931.png) 

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

