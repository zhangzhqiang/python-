# Day11 作业

1. 第一题

    ```python
    '''
    列举 str、list、dict、set 中的常用方法（每种至少5个），并标注是否有返回值'''
    '''
    str:
        pop() # 有返回值
        aplit() # 有返回值
        strip() # 有返回值
        upper() # 有返回值
        lower() # 有返回值
        replace() # 有返回值
        startswith() # 有返回值
        endswith() # 有返回值
        join() # 有返回值
    list:
        count() # 有返回值
        copy() # 有返回值
        pop() # 有返回值
        index() # 有返回值
        append() # 无返回值
        extend() # 无返回值
        remove() # 无返回值
        clear() # 无返回值
        reverse() # 无返回值
        insert() # 无返回值
        sort() # 无返回值
    dict
        keys() # 有返回值
        values() # 有返回值
        items() # 有返回值
        get() # 有返回值
        clear() # 无返回值
        pop() # 无返回值
        update() # 无返回值
        copy() # 无返回值
    set
        add() # 无返回值
        discard() # 无返回值
        update() # 无返回值
        intersection() # 有返回值
        union() # 有返回值
        difference() # 有返回值
        symmetric_difference() # 有返回值
    '''
    ```

2. 第二题

    ```python
    '''列举你了解的常见内置函数 【面试题】'''
    '''
    数学相关:
        abs()   绝对值
        max()   最大值
        min()   最小值
        float() 浮点数
        sum()   求和
        divmod()商和余数
    强制转换:
        str()   转字符串
        int()   转数字
        list()  转列表
        set()   转集合
        dict()  转字典
        bool()  转布尔
    其他函数:
        len()   长度
        open()  打开文件
        type()  数据类型
        range() 遍历
        id()    内存地址
    输入输出:
        input() 输入
        print() 输出
    '''
    ```

3. 第三题

    ```python
    '''看代码分析结果
    
    def func(arg):
        return arg.replace('苍老师', '***')
    
    
    def run():
        msg = "Alex的女朋友苍老师和大家都是好朋友"
        result = func(msg)
        print(result)
    
    
    run()'''
    
    # Alex的女朋友***和大家都是好朋友
    ```

4. 第四题

    ```python
    '''看代码分析结果
    
    def func(arg):
        return arg.replace('苍老师', '***')
    
    
    def run():
        msg = "Alex的女朋友苍老师和大家都是好朋友"
        result = func(msg)
        print(result)
    
    data = run()
    print(data)'''
    
    # Alex的女朋友***和大家都是好朋友
    # None
    ```

5. 第五题

    ```python
    '''看代码分析结果
    
    DATA_LIST = []
    
    
    def func(arg):
        return DATA_LIST.insert(0, arg)
    
    
    data = func('绕不死你')
    print(data)
    print(DATA_LIST)'''
    
    # None
    # ['绕不死你']
    ```

6. 第六题

    ```python
    '''看代码分析结果
    
    def func():
        print('你好呀')
        return '好你妹呀'
    
    
    func_list = [func, func, func]
    
    for item in func_list:
        val = item()
        print(val)'''
    # 你好呀
    # 好你妹呀
    # 你好呀
    # 好你妹呀
    # 你好呀
    # 好你妹呀
    ```

7. 第七题

    ```python
    '''看代码分析结果
    
    def func():
        print('你好呀')
        return '好你妹呀'
    
    
    func_list = [func, func, func]
    
    for i in range(len(func_list)):
        val = func_list[i]()
        print(val)'''
    
    # 你好呀
    # 好你妹呀
    # 你好呀
    # 好你妹呀
    # 你好呀
    # 好你妹呀
    ```

8. 第八题

    ```python
    '''看代码写结果
    
    tips = "啦啦啦啦"
    
    
    def func():
        print(tips)
        return '好你妹呀'
    
    
    func_list = [func, func, func]
    
    tips = '你好不好'
    
    for i in range(len(func_list)):
        val = func_list[i]()
        print(val)'''
    # 你好不好
    # 好你妹呀
    # 你好不好
    # 好你妹呀
    # 你好不好
    # 好你妹呀
    ```

9. 第九题

    ```python
    '''看代码写结果
    
    def func():
        return '烧饼'
    
    
    def bar():
        return '豆饼'
    
    
    def base(a1, a2):
        return a1() + a2()
    
    
    result = base(func, bar)
    print(result)'''
    
    # 烧饼豆饼
    ```

10. 第十题

    ```python
    '''看代码写结果
    
    def func():
        return '烧饼'
    
    
    def bar():
        return '豆饼'
    
    
    def base(a1, a2):
        return a1 + a2
    
    
    result = base(func(), bar())
    print(result)'''
    
    # 烧饼豆饼
    ```

11. 第十一题

    ```python
    '''看代码写结果
    
    v1 = lambda :100
    print(v1())
    
    v2 = lambda vals: max(vals) + min(vals)
    print(v2([11,22,33,44,55]))
    
    v3 = lambda vals: '大' if max(vals)>5 else '小'
    print(v3([1,2,3,4]))'''
    # 100
    # 66
    # 小
    ```

12. 第十二题

    ```python
    '''看代码写结果
    
    def func():
        num = 10
        v4 = [lambda :num+10,lambda :num+100,lambda :num+100,]
        for item in v4:
            print(item())
    func()'''
    
    # 20
    # 110
    # 110
    ```

13. 第十三题

    ```python
    '''看代码写结果
    
    for item in range(10):
        print(item)
        
    print(item)'''
    # 0 1 2 3 4 5 6 7 8 9 9
    ```

14. 第十四题

    ```python
    '''看代码写结果
    
    def func():
        for item in range(10):
            pass
        print(item)
    func()'''
    
    # 9
    ```

15. 第十五题

    ```python
    '''看代码写结果
    
    item = '老男孩'
    def func():
        item = 'alex'
        def inner():
            print(item)
        for item in range(10):
            pass
        inner()
    func()'''
    
    # 9
    ```

16. 第十六题

    ```python
    '''看代码写结果【新浪微博面试题】
    
    def func():
        for num in range(10):
            pass
        v4 = [lambda :num+10,lambda :num+100,lambda :num+100,]
        result1 = v4[1]()
        result2 = v4[2]()
        print(result1,result2)
    func()'''
    
    # 109 109
    ```

17. 第十七题

    ```python
    '''通过代码实现如下转换
    
    二进制转换成十进制：v = '0b1111011'
    十进制转换成二进制：v = 18
    八进制转换成十进制：v = '011'
    十进制转换成八进制：v = 30
    十六进制转换成十进制：v = '0x12'
    十进制转换成十六进制：v = 87'''
    
    '''
    # 二进制转换成十进制
    v = '0b1111011'
    print(int(v, base=2))
    
    # 十进制转换成二进制
    v = 18
    print(bin(v))
    
    # 八进制转换成十进制
    v = '011'
    print(int(v,base=8))
    
    # 十进制转换成八进制
    v = 30
    print(oct(v))
    
    # 十六进制转换成十进制
    v = '0x12'
    print(int(v, base=16))
    
    # 十进制转换成十六进制
    v = 87
    print(hex(v))
    '''
    ```

18. 第十八题

    ```python
    '''请编写一个函数实现将IP地址转换成一个整数。【面试题】
    
    如 10.3.9.12 转换规则为二进制：
            10            00001010
             3            00000011
             9            00001001
            12            00001100
    再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？'''
    ip = '10.3.9.12'
    
    
    def func(ip):
        a = ip.split('.')
        s = ''
        lis = []
        for i in a:
            i = bin(int(i))[2:].rjust(8, '0')  # 转换为二进制
            lis.append(i)
        return s.join(lis)
    
    
    k = func(ip)
    print(int(k, base=2))
    ```