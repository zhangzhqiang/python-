# Day14 作业

1. 第一题

    ```python
    '''为函数写一个装饰器，在函数执行之后输入 after
    @wrapper
    def func():
        print(123)
    func()'''
    # def wrapper(arg):
    #     def inner(*args, **kwargs):
    #         res = arg(*args, **kwargs)
    #         print('after')
    #         return res
    #     return inner
    #
    #
    # @wrapper
    # def func():
    #     print(123)
    #
    # func()
    ```

2. 第二题

    ```python
    '''为函数写一个装饰器，把函数的返回值 +100 然后再返回。
    @wrapper
    def func():
        return 7
    result = func()
    print(result)'''
    
    # def wrapper(arg):
    #     def inner(*args, **kwargs):
    #         res = arg(*args, **kwargs)
    #         return res + 100
    #     return inner
    #
    #
    # @wrapper
    # def func():
    #     return 7
    #
    # result = func()
    # print(result)
    ```

3. 第三题

    ```python
    '''为函数写一个装饰器，根据参数不同做不同操作。
    
    flag为True，则 让原函数执行后返回值加100，并返回。
    flag为False，则 让原函数执行后返回值减100，并返回。
    
    @x(True)
    def f1():
        return 11
    
    @x(False)
    def f2():
        return 22
    '''
    
    # def x(flag):
    #     def warpper(arg):
    #         def inner(*args, **kwargs):
    #             if flag:
    #                 return arg(*args, **kwargs) + 100
    #             return arg(*args, **kwargs) - 100
    #         return inner
    #     return warpper
    #
    #
    # @x(True)
    # def f1():
    #     return 11
    #
    # @x(False)
    # def f2():
    #     return 22
    #
    # res = f1()
    # print(res)
    #
    # res1 = f2()
    # print(res1)
    ```

4. 第四题

    ```python
    '''写一个脚本，接收两个参数。
    
    第一个参数：文件
    第二个参数：内容
    请将第二个参数中的内容写入到 文件（第一个参数）中。
    
    # 执行脚本： python test.py oldboy.txt 你好'''
    # import sys
    # a = sys.argv
    # with open(a[1],mode="w",encoding="utf-8") as f1:
    #     f1.write(a[2])
    ```

5. 第五题

    ```python
    '''递归的最大次数是多少？'''
    # 1000次
    ```

6. 第六题

    ```python
    '''看代码写结果
    
    print("你\n好")
    print("你\\n好")
    print(r"你\n好")'''
    
    # 你
    # 好
    # 你\n好
    # 你\n好
    
    ```

7. 第七题

    ```python
    '''写函数实现，查看一个路径下所有的文件【所有】。'''
    # import os
    # def inner(path):
    #     file = os.walk(path)
    #     for a, b, c in file:
    #         for item in c:
    #             path1 = os.path.join(a, item)
    #             print(path1)
    #
    # inner(r'E:\Android_Nox\Nox_share')
    ```

8. 第八题

    ```python
    '''写代码
    
    path = r"D:\code\test.pdf"
    
    # 请根据path找到code目录下所有的文件【单层】，并打印出来。'''
    
    # import os
    # path = r"D:\code\test.pdf"
    # val = os.path.dirname(path)  # 获取上一级目录
    # for item in os.listdir(val):
    #     print(item)
    ```

9. 第九题

    ```python
    '''使用python/C上机编程解决以下题目，其中1和2任选其一，3和4任选其一。
    【题目】 1
    斐波契纳数列1,2.3,5,12.21.........据这样的规律，编程求出400万以内最大的斐波契纳数,并求出它是第几个斐波契纳数。'''
    
    # def func(a, b):
    #     index = 0
    #     while b < 4000000:
    #         a, b = b, a + b
    #         index += 1
    #     print(index)
    #     print(b)
    #
    # func(0, 1)
    
    '''【题目】 2
    上机编程实现以下功能:
    dicta= {"a":1,"b":2,"c":3, "d":4, "f:"hello" } dictb= {"b":3,"d":5, "e":7, "m":9, "K": "world"}
    要求写一段代码，实现两个字典的相加，
    不同的key对应的值保留，相同的key对应的值相加后保留，如果是字符串就拼接，如上示例得到结果为: 
    dictc= {"a":1,"b":5,"c":3, "d":9,"e":7, "m”:9, "f': "hello", "k": "world"}
    dicta= {"a":1,"b":2,"c":3, "d":4, "f":"hello"}
    dictb= {"b":3,"d":5, "e":7, "m":9, "K": "world"}'''
    
    # dicta = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 'hello'}
    # dictb = {'b': 3, 'd': 5, 'e': 7, 'm': 9, 'k': 'world'}
    # v1 = set(dicta.keys())
    # v2 = set(dictb.keys())
    # v3 = v1.union(v2)
    # dic = {}
    # for i in v3:
    #     vala = dicta.get(i)
    #     valb = dictb.get(i)
    #     if type(vala) == type(valb):
    #         dic[i] = vala + valb
    #     elif not vala:
    #         dic[i] = valb
    #     else:
    #         dic[i] = vala
    #
    # print(dic)
    ```

10. 第十题

    ```python
    '''10.以下的代码的输出将是什么:'''
    
    # def extendList(val, list=[]):
    #     list.append(val)
    #     return list
    #
    #
    # listl = extendList(10)
    # list2 = extendList(123, [])
    # list3 = extendList("a")
    # print(listl, list2, list3)
    # [10, 'a'] [123] [10, 'a']
    ```

11. 第十一题

    ```python
    '''
    11:
    1.选出以下表达式表述正确的选项:
    A:{1: 0, 2: 0, 3: 0}
    B: {'a':0, 'b':0, 'c':0}
    C: {(1,2):0, (4,3):0}
    D: {[1,2):0, [4,3]:0}
    E: {1,2):0, {4,3):0}'''
    # 答：b
    
    '''
    2.tupleA = ('a','b','c','d','e')
    tupleB = (1, 2, 3, 4, 5)
    res = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
    写出由tupleA
    和tupleB
    得到res
    的具体实现过程'''
    
    # tupleA = ('a','b','c','d','e')
    # tupleB = (1, 2, 3, 4, 5)
    # res = {}
    # for i in range(len(tupleA)):
    #     res[tupleA[i]] = tupleB[i]
    # print(res)
    '''
    3.python代码获取命令行参数:'''
    # 答：sys.argv
    
    '''
    4.已知ip = '192.168.0.100'
    代码实现提取ip
    的各部分并写入列表'''
    # p = []
    # ip = '192.168.0.100'
    # ip = ip.split(".")
    # p.extend(ip)
    # print(p)
    
    '''
    5.已知AList = ['a', 'b', 'c']
    将AList转化为'a,b,c' 的实现过程'''
    # AList = ['a', 'b', 'c']
    # AList = ",".join(AList)
    # print(AList)
    
    
    '''
    6.
    已知StrA = "1234A6FASKKSJLSKWLM<SJKL9O"
    (1)如何获取最后两个字符?'''
    # StrA = "1234A6FASKKSJLSKWLM<SJKL9O"
    # Strb = StrA[-2:]
    # print(Strb)
    
    
    '''
    (2)如何获取第二个和第三个字符?'''
    # Strb = StrA[1:3]
    # print(Strb)
    
    '''
    7.已知Alist = [1, 2, 3, 1, 3, 1, 2, 1, 3] 如何根据Alist
    得到[1, 2, 3]'''
    # Alist = [1, 2, 3, 1, 3, 1, 2, 1, 3]
    # Alist = Alist[0:3]
    # print(Alist)
    
    '''
    编程题(5题):
    1.编写一个函数, 这个函数接受一个文件夹名称作为参数, 显示文件夹中文件的路径，以及其中包含文件夹中文件的路径'''
    # def tt(arg):
    #     import os
    #     d = os.walk(arg)
    #     for a, b, c in d:
    #         for f in c:
    #             print(a, f)
    #     pass
    # tt("D:\PycharmProjects")
    
    
    '''
    2.1000以内的完美数(如果 - 个数恰好等于它的因子之和, 则称该数为完美数)
    eg: 6 = 1 * 2 * 3 = 1 + 2 + 3'''
    
    # # 方式一:
    # for i in range(1, 1001):
    #     list1 = []
    #     for j in range(1, i):
    #         if i % j == 0:
    #             list1.append(j)
    #     if sum(list1) == i:  # sum函数求和
    #         print(i)
    # # 方式二:
    # for i in range(1, 1001):
    #     er = 0
    #     for h in range(1, i):
    #         if i % h == 0:
    #             er += h
    #     if er == i:
    #         print(er)
    
    '''3.有A.txt 和 B.txt两个文件,使用多进程池方式分别读取这连个文件'''
    
    '''
    4.输入两个列表, alist, bls, 依次顺序比较两个list中的元素，
    如果alist的元素大于blist的元素, 返回alist;
    如果alist的元素小于blist的元素, 返回blist;
    如果两个list的所有元素都相等返回alist, 否则返回blist;
    '''
    # i = 0
    # alis = [3, 4, 5, 6, 7, 8]
    # blist = [2, 3, 4, 5, 6, 7]
    # for pol in range(len(alis)):
    #     if alis[pol] > blist[pol]:
    #         i += 1
    #     else:
    #         i -= 1
    # if i < 0:
    #     print(blist)
    # else:
    #     print(alis)
    #
    # i = 0
    # alis = [3, 4, 5, 6, 7, 8]
    # blist = [2, 3, 4, 5, 6, 7]
    # for pol in range(len(alis)):
    #     if alis[pol] > blist[pol]:
    #         i += 1
    #     else:
    #         i -= 1
    # if i == 0:
    #     print(alis)
    # else:
    #     print(blist)
    
    
    '''
    一个大小为100G的文件etl_logtxt, 要读取文件中的内容, 写出具体过程代码。
    '''
    
    # def kop():
    #     with open("elt_log.txt", mode="r", encoding="utf-8") as f:
    #         for i in f:
    #             print(i)
    # kop()
    ```

    