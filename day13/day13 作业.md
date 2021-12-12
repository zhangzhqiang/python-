# Day13 作业

1. 第一题

    ```python
    #1.请为func函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先输入"before"，然后再执行func函数内部代码。
    
        def func():
            return 100 + 200
    
        val = func()'''
    
    # def wapper(arg):
    #     def inner(*args, **kwargs):
    #         print('before')
    #         return arg(*args, **kwargs)
    #     return inner
    #
    # @wapper
    # def func():
    #     return 100 + 200
    # val = func()
    # print(val)
    ```

2. 第二题

    ```python
    '''
    2.请为func函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先执行func函数内部代码，再输出"after"
    
        def func():
            return 100 + 200
    
        val = func()
    '''
    
    # def wapper(arg):
    #     def inner(*args, **kwargs):
    #         res = arg(*args, **kwargs)
    #         print(res)
    #         print('after')
    #     return inner
    #
    #
    # @wapper
    # def func():
    #     return 100 + 200
    #
    #
    # func()
    ```

3. 第三题

    ```python
    '''
    3.请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先执行func函数内部代码，再输出"after"
    
        def func(a1):
            return a1 + "傻叉"
    
        def base(a1, a2):
            return a1 + a2 + '傻缺'
    
        def base(a1, a2, a3, a4):
            return a1 + a2 + a3 + a4 + '傻蛋'
    '''
    
    # def wapper(arg):
    #     def inner(*args, **kwargs):
    #         res = arg(*args, **kwargs)
    #         print(res)
    #         print('after')
    #     return inner
    #
    # @wapper
    # def func(a1):
    #     return a1 + "傻叉"
    #
    # @wapper
    # def base(a1, a2):
    #     return a1 + a2 + '傻缺'
    #
    # @wapper
    # def base1(a1, a2, a3, a4):
    #     return a1 + a2 + a3 + a4 + '傻蛋'
    #
    # res = func('张三')
    #
    # res1 = base('王五', '是个')
    #
    # res2 = base1('老王', '你小子', '真的', '是个')
    ```

4. 第四题

    ```python
    """
    4.请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：将被装饰的函数执行5次，将每次执行函数的结果按照顺序放到列表中，最终返回列表。
    
        import random
    
        def func():
            return random.randint(1, 4)
    
        reuslt = func()  # 执行5次，并将每次执行的结果追加到列表最终返回给result
        print(result)
    """
    # 方式一:
    # import random
    #
    # def wapper(arg):
    #     lis = []
    #     def inner(*args, **kwargs):
    #         for i in range(5):
    #             lis.append(arg())
    #         return lis
    #     return inner
    #
    # @wapper
    # def func():
    #     return random.randint(1, 4)
    #
    #
    # result = func()  # 执行5次，并将每次执行的结果追加到列表最终返回给result
    # print(result)
    
    # 方式二:
    # import random
    #
    #
    # def wapper(arg):
    #     def inner(*args, **kwargs):
    #         lis = [arg(*args, **kwargs) for i in range(5)]
    #         return lis
    #     return inner
    #
    #
    # @wapper
    # def func():
    #     return random.randint(1, 4)
    #
    #
    # result = func()  # 执行5次，并将每次执行的结果追加到列表最终返回给result
    # print(result)
    ```

5. 第五题

    ```python
    """
    5.请为以下函数编写一个装饰器，添加上装饰器后可以实现：执行read_userinfo函时，
    先检查文件路径是否存在，如果存在则执行后，
    如果不存在则输入文件路径不存在，
    并且不再执行read_userinfo函数体中的内容，再将content变量的返回值为None。
    
        def read_userinfo(path):
            file_obj = open(path, mode='r', encoding='utf-8')
            data = file_obj.read()
            file_obj.close()
            return data
    
        content = read_userinfo('/usr/bin/xxx/xxx')
    
    
        温馨提示：如何查看一个路径是否存在？
        import os
        result = os.path.exists('路径地址')
    
        # result为True，则表示路径存在。
        # result为False，则表示路径不存在。
    """
    # import os
    #
    # result = os.path.exists('D:\Luffycity\study\Ike_code\day13')
    #
    #
    # def wapper(arg):
    #     def inner(*args, **kwargs):
    #         if result:
    #             arg(*args, **kwargs)
    #             # return True if result else False
    #             return True
    #         return False
    #
    #     return inner
    #
    # @wapper
    # def read_userinfo(path):
    #     file_obj = open(path, mode='r', encoding='utf-8')
    #     data = file_obj.read()
    #     file_obj.close()
    #     return data
    #
    #
    # content = read_userinfo(r'D:\Luffycity\study\Ike_code\day13\4.作业.py')
    # print(content)
    ```

6. 第六题

    ```python
    '''
    6.请为以下user_list函数编写一个装饰器，
    校验用户是否已经登录，登录后可以访问，未登录则提示：请登录后再进行查看，然后再给用户提示：系统管理平台
    【1.查看用户列表】【2.登录】并选择序号。
    
        # 此变量用于标记，用户是否已经登录。
        #    True,已登录。
        #    False,未登录(默认)
        CURRENT_USER_STATUS = False
    
        def user_list():
            """查看用户列表"""
            for i in range(1, 100):
                temp = "ID:%s 用户名：老男孩-%s" % (i, i,)
            print(temp)
    
        def login():
            """登录"""
            print('欢迎登录')
            while True:
                username = input('请输入用户名（输入N退出）：')
                if username == 'N':
                    print('退出登录')
                    return
                password = input('请输入密码：')
                if username == 'alex' and password == '123':
                    global CURRENT_USER_STATUS
                    CURRENT_USER_STATUS = True
                    print('登录成功')
                    return
                print('用户名或密码错误，请重新登录。')
    
        def run():
            func_list = [user_list, login]
            while True:
                print("""系统管理平台
                1.查看用户列表；
                2.登录""")
                index = int(input('请选择：'))
                if index >= 0 and index < len(func_list):
                    func_list[index-1]()
                else:
                    print('序号不存在，请重新选择。')
    
        run()
    '''
    
    # CURRENT_USER_STATUS = False
    #
    #
    # def login():
    #     """登录"""
    #     print('欢迎登录')
    #     while True:
    #         username = input('请输入用户名（输入N退出）：')
    #         if username == 'N':
    #             print('退出登录')
    #             return
    #         password = input('请输入密码：')
    #         if username == 'alex' and password == '123':
    #             global CURRENT_USER_STATUS
    #             CURRENT_USER_STATUS = True
    #             print('登录成功')
    #             return
    #         print('用户名或密码错误，请重新登录。')
    #
    #
    # def run():
    #     func_list = [user_list, login]
    #     while True:
    #         print("""系统管理平台
    #         1.查看用户列表；
    #         2.登录""")
    #         index = int(input('请选择：'))
    #         if index >= 0 and index < len(func_list):
    #             func_list[index - 1]()
    #         else:
    #             print('序号不存在，请重新选择。')
    #
    #
    # def func(arg):
    #     def inner(*args, **kwargs):
    #         return arg(*args, **kwargs) if CURRENT_USER_STATUS == True else print("请登录后再进行查看")
    #     return inner
    #
    #
    # @func
    # def user_list():
    #     """查看用户列表"""
    #     for i in range(1, 100):
    #         temp = "ID:%s 用户名：老男孩-%s" % (i, i,)
    #         print(temp)
    #
    #
    # run()
    ```

7. 第七题

    ```python
    """
    7.看代码写结果
    
        v = [lambda: x for x in range(10)]
        print(v)
        print(v[0])
        print(v[0]())
    """
    # 10个lambda内存地址
    # 第1个lambda内存地址
    # 9
    ```

8. 第八题

    ```python
    """
    8.看代码写结果
    
        v = [i for i in range(10, 0, -1) if i > 5]
    """
    # 不会输出，v值为10，9，8，7，6
    ```

9. 第九题

    ```python
    """
    9.看代码写结果
    
        data = [lambda x: x * i for i in range(10)]  # 新浪微博面试题
        print(data)
        print(data[0](2))
        print(data[0](2) == data[8](2))
    """
    # 10个lambda内存地址
    # 9
    # True
    ```

10. 第十题

    ```python
    """
    10.请用列表推导式实现，踢出列表中的字符串，然后再将每个数字加100，最终生成一个新的列表保存。
    
        data_list = [11, 22, 33, "alex", 455, 'eirc']
        new_data_list = [...]  # 请在[]中补充代码实现。
    """
    # data_list = [11, 22, 33, "alex", 455, 'eirc']
    # print([i + 100 for i in data_list if type(i) == int])
    ```

11. 第十一题

    ```python
    11.请使用字典推导式实现，将如果列表构造成指定格式字典.
    
        data_list = [
            (1, 'alex', 19),
            (2, '老男', 84),
            (3, '老女', 73)
        ]
        # 请使用推导式将data_list构造生成如下格式：
        info_list = {
            1: ('alex', 19),
            2: ('老男', 84),
            3: ('老女', 73)
        }
    """
    data_list = [(1, 'alex', 19), (2, '老男', 84), (3, '老女', 73)]
    print({data_list[item][0]: data_list[item][1:] for item in range(len(data_list))})
    
    ```

    