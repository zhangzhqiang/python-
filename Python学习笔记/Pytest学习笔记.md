# Pytest学习笔记

## 第一章 Pytest简介

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

注意：这里清除环境的代码就是 yield 之后的代码。 这是一个生成器，具体的说明参见视频讲解。



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

