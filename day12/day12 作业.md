# Day12 作业

1. 第一题

    ```python
    '''写出三元运算的基本格式及作用？'''
    # 条件成立的结果 if 条件 else 条件不成立的结果
    # 把逻辑简单的判断语句一行表示出来
    ```

2. 第二题

    ```python
    '''什么是匿名函数？'''
    # lambda表达式
    ```

3. 第三题

    ```python
    '''尽量多的列举你了解的内置函数？【默写】'''
    输入输出:
        input
        print
    强制转换:
        int
        str
        list
        bool
        set
        dict
        tuple
    进制转换:
        bin
        oct
        int
        hex
    数学相关:
        max
        min
        sum
        abs
        float
        divmod
    其他函数:
        len
        type
        id
        open
        range
    ```

4. 第四题

    ```python
    '''filter/map/reduce函数的作用分别是什么？'''
    # filter对序列中的元素进行筛选
    # map训话执行序列中的每一个元素
    # reduce对序列中的所有元素求和
    ```

5. 第五题

    ```python
    '''看代码写结果
    
    def func(*args,**kwargs):
        print(args,kwargs)
        
    # a. 执行 func(12,3,*[11,22]) ，输出什么？
    # b. 执行 func(('alex','武沛齐',),name='eric')'''
    
    # (12,3,11,22){}
    # ()('alex','武沛齐'),){'name':'eric'}
    ```

6. 第六题

    ```python
    '''看代码分析结果
    
    def func(arg):
        return arg.pop(1)
    
    result = func([11,22,33,44])
    print(result)'''
    # 22
    ```

7. 第七题

    ```python
    '''看代码分析结果
    
    func_list = []
    
    for i in range(10):
        func_list.append(lambda :i)
    
    v1 = func_list[0]()
    v2 = func_list[5]()
    print(v1,v2)'''
    # 9 9
    ```

8. 第八题

    ```python
    '''看代码分析结果
    
    func_list = []
    
    for i in range(10):
        func_list.append(lambda x:x+i)
    
    v1 = func_list[0](2)
    v2 = func_list[5](1)
    print(v1,v2)'''
    # 11 10
    ```

9. 第九题

    ```python
    '''看代码分析结果
    
    func_list = []
    
    for i in range(10):
        func_list.append(lambda x:x+i)
    
    for i in range(0,len(func_list)):
        result = func_list[i](i)
        print(result)'''
    '''
    0
    2
    4
    6
    8
    10
    12
    14
    16
    18
    '''
    ```

10. 第十题

    ```python
    '''看代码分析结果
    
    def f1():
        print('f1')
    
    def f2():
        print('f2')
        return f1
    
    func = f2()
    result = func()
    print(result)'''
    
    # f2
    # f1
    # None
    ```

11. 第十一题

    ```python
    '''看代码分析结果【面试题】
    
    def f1():
        print('f1')
        return f3()
    
    def f2():
        print('f2')
        return f1
    
    def f3():
        print('f3')
    
    func = f2()
    result = func()
    print(result)'''
    
    # f2
    # f1
    # f3
    # None
    ```

12. 第十二题

    ```python
    '''看代码分析结果
    
    name = '景女神'
    
    def func():
        def inner():
            print(name)
        return inner()
    
    v = func()
    print(v)'''
    # 景女神
    # None
    ```

13. 第十三题

    ```python
    '''看代码分析结果
    
    name = '景女神'
    
    def func():
        def inner():
            print(name)
            return "老男孩"
        return inner()
    
    v = func()
    print(v)'''
    # 景女神
    # 老男孩
    ```

14. 第十四题

    ```python
    '''看代码分析结果
    
    name = '景女神'
    
    def func():
        def inner():
            print(name)
            return '老男孩'
        return inner
    
    v = func()
    result = v()
    print(result)'''
    # 景女神
    # 老男孩
    ```

15. 第十五题

    ```python
    '''看代码分析结果
    
    def func():
        name = '武沛齐'
        def inner():
            print(name)
            return '老男孩'
        return inner
    
    v1 = func()
    v2 = func()
    print(v1,v2)'''
    # 返回inner函数
    ```

16. 第十六题

    ```python
    '''看代码写结果
    
    def func(name):
        def inner():
            print(name)
            return '老男孩'
        return inner
    
    v1 = func('金老板')
    v2 = func('alex')
    print(v1,v2)'''
    
    # 返回inner函数
    ```

17. 第十七题

    ```python
    '''看代码写结果
    
    def func(name=None):
        if not name:
            name= '武沛齐'
        def inner():
            print(name)
            return '老男孩'
        return inner
    
    v1 = func()
    v2 = func('alex')
    print(v1,v2)'''
    
    # 返回inner函数
    ```

18. 第十八题

    ```python
    '''看代码写结果【面试题】
    
    def func(name):
        v = lambda x:x+name
        return v
    
    v1 = func('武沛齐')
    v2 = func('alex')
    v3 = v1('银角')
    v4 = v2('金角')
    print(v1,v2,v3,v4)'''
    
    # v1,v2返回v函数 银角武沛齐 金角alex
    ```

19. 第十九题

    ```python
    '''看代码写结果
    
    NUM = 100
    result = []
    for i in range(10):
        func = lambda : NUM      # 注意：函数不执行，内部代码不会执行。
        result.append(func)
    
    print(i)
    print(result)
    v1 = result[0]()
    v2 = result[9]()
    print(v1,v2)'''
    
    # 9 列表中10个func函数 100 100
    ```

20. 第二十题

    ```python
    '''看代码写结果【面试题】
    
    result = []
    for i in range(10):
        func = lambda : i      # 注意：函数不执行，内部代码不会执行。
        result.append(func)
    
    print(i)
    print(result)
    v1 = result[0]()
    v2 = result[9]()
    print(v1,v2)'''
    # 9 列表中10个func函数 9 9
    ```

21. 第二十一题

    ```python
    '''看代码分析结果【面试题】
    
    def func(num):
        def inner():
            print(num)
        return inner
    
    result = []
    for i in range(10):
        f = func(i)
        result.append(f)
    
    print(i)
    print(result)
    v1 = result[0]()
    v2 = result[9]()
    print(v1,v2)'''
    
    # 9 列表中10个finner函数 0 9 None None
    ```

    

22. 第一题