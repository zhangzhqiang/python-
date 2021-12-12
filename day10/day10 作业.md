# Day10 作业

1. 第一题

    ```
    '''写函数，函数可以支持接收任意数字（位置传参）并将所有数据相加并返回。'''
    def count_num(*args):
        count = 0
        for i in args:
            count += i
        return count
    
    
    res = count_num(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(res)
    ```

2. 第二题

    ```python
    '''看代码写结果
    
    def func():
        return 1,2,3
    
    val = func()
    print( type(val) == tuple )
    print( type(val) == list )'''
    
    # True False
    ```

3. 第三题

    ```python
    '''看代码写结果
    
    def func(*args,**kwargs):
        pass
    
    # a. 请将执行函数，并实现让args的值为 (1,2,3,4)
    # b. 请将执行函数，并实现让args的值为 ([1,2,3,4],[11,22,33])
    # c. 请将执行函数，并实现让args的值为 ([11,22],33) 且 kwargs的值为{'k1':'v1','k2':'v2'}
    # d. 如执行 func(*{'武沛齐','金鑫','女神'})，请问 args和kwargs的值分别是？
    # e. 如执行 func({'武沛齐','金鑫','女神'},[11,22,33])，请问 args和kwargs的值分别是？
    # f. 如执行 func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})，请问 args和kwargs的值分别是？'''
    
    # # a.
    # def func(*args, **kwargs):
    #     return args, kwargs
    # print(func(1, 2, 3, 4))
    # # b.
    # print(func([1, 2, 3, 4], [11, 22, 33]))
    # # c.
    # print(func([11, 22], 33, {'k1': 'v1', 'k2': 'v2'}))
    # # d. args = ('女神', '金鑫', '武沛齐') kwargs没有值
    # # e. args = ({'武沛齐','金鑫','女神'},[11,22,33])  kwargs没有值
    # # f. args = ('武沛齐', '金鑫', '女神', [11, 22, 33])  kwargs = {'k1': '栈'}
    ```

4. 第四题

    ```python
    '''看代码写结果
    
    def func(name,age=19,email='123@qq.com'):
        pass
    
    # a. 执行 func('alex') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
    # b. 执行 func('alex',20) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
    # c. 执行 func('alex',20,30) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
    # d. 执行 func('alex',email='x@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
    # e. 执行 func('alex',email='x@qq.com',age=99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
    # f. 执行 func(name='alex',99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
    # g. 执行 func(name='alex',99,'111@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分'''
    
    # a. 可执行,name='alex,age=19,email='123@qq.com
    # b. 可执行,name='alex,age=20,email='123@qq.com
    # c. 可执行,name='alex,age=20,email=20
    # d. 可执行,name='alex,age=19,email=x@qq.com
    # e. 可执行,name='alex,age=99,email=x@qq.com
    # f. 不可执行,name是位置参数,不能在关键字参数后边
    # g. 不可执行,name是位置参数,不能在关键字参数后边
    ```

5. 第五题

    ```python
    '''看代码写结果
    
    def func(users,name):
        users.append(name)
        return users
    
    result = func(['武沛齐','李杰'],'alex')
    print(result)'''
    
    # ['武沛齐', '李杰', 'alex']
    ```

6. 第六题

    ```python
    '''看代码写结果
    
    def func(v1):
        return v1* 2
    
    def bar(arg):
        return "%s 是什么玩意？" %(arg,)
    
    val = func('你')
    data = bar(val)
    print(data)'''
    
    # 你你 是什么玩意？
    ```

7. 第七题

    ```python
    '''看代码写结果
    
    def func(v1):
        return v1* 2
    
    def bar(arg):
        msg = "%s 是什么玩意？" %(arg,)
        print(msg) 
    
    val = func('你')
    data = bar(val)
    print(data)'''
    
    # 打印: 你你 是什么玩意？  返回: None
    ```

8. 第八题

    ```python
    '''看代码写结果
    
    v1 = '武沛齐'
    
    def func():
        print(v1)
        
    func()
    v1 = '老男人'
    func()'''
    
    # 武沛齐 老男人
    ```

9. 第九题

    ```python
    '''看代码写结果
    
    v1 = '武沛齐'
    
    def func():
        v1 = '景女神'
        def inner():
            print(v1)
        v1 = '肖大侠'
        inner()
    func()
    v1 = '老男人'
    func()'''
    
    # 肖大侠  肖大侠
    ```

10. 第十题

    ```python
    '''看代码写结果【可选】
    
    def func():
        data = 2*2
        return data
    
    new_name = func
    val = new_name()
    print(val)
    
    # 注意：函数类似于变量，func代指一块代码的内存地址。'''
    # 4
    ```

11. 第十一题

    ```python
    '''看代码写结果【可选】
    
    def func():
        data = 2*2
        return data
    
    data_list = [func,func,func]
    for item in data_list:
        v = item()
        print(v)
    
    # 注意：函数类似于变量，func代指一块代码的内存地址。'''
    
    # 4 4 4
    
    ```

12. 第十二题

    ```python
    '''看代码写结果（函数可以做参数进行传递）【可选】
    
    def func(arg):
        arg()
        
    def show():
        print('show函数')
    
    func(show)'''
    
    # show函数
    
    ```

    