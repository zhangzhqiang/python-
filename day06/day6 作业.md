# Day6 作业

1. 第一题

   ```python
   """
   列举你了解的字典中的功能（字典独有）。
   """
   # keys/values/items/get/update/pop
   ```

2. 第二题

   ```python
   '''列举你了解的集合中的功能（集合独有）。
   '''
   # add/discard/update/insersection/union/difference/symmetric_difference
   ```

3. 第三题

   ```python
   """列举你了解的可以转换为 布尔值且为False的值。"""
   # 0/""/[]/{}/set()/None
   ```

4. 第四题

   ```python
   """请用代码实现
   
   info = {'name':'王刚蛋','hobby':'铁锤'}
   循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出。
   循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出
   （如果key不存在，则获取默认“键不存在”，并输出）。 注意：无需考虑循环终止（写死循环即可）"""
   info = {'name': '王刚蛋', 'hobby': '铁锤'}
   # 示例一:
   while True:
       msg = input('>>>:')
       message = info.get(msg)
       print(message)
   # 示例二:
   info = {'name': '王刚蛋', 'hobby': '铁锤'}
   while True:
       msg = input('>>>:')
       message = info.get(msg, '键不存在')
       print(message)
   ```

5. 第五题

   ```python
   """请用代码验证 "name" 是否在字典的键中？
   
   info = {'name':'王刚蛋','hobby':'铁锤','age':'18',...100个键值对}"""
   info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18'}
   msg = info.get('name', '不存在')
   print(msg)
   ```

6. 第六题

   ```python
   """请用代码验证 "alex" 是否在字典的值中？
   
   info = {'name':'王刚蛋','hobby':'铁锤','age':'18',...100个键值对}"""
   
   info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18'}
   
   for v in info.values():
       if v == 'alex':
           print('存在')
       else:
           print('不存在')
   ```

7. 第七题

   ```python
   """有如下:
   请得到 v1 和 v2 的交集并输出
   请得到 v1 和 v2 的并集并输出
   请得到 v1 和 v2 的 差集并输出
   请得到 v2 和 v1 的 差集并输出"""
   v1 = {'武沛齐', '李杰', '太白', '景女神'}
   v2 = {'李杰', '景女神'}
   print(v1.intersection(v2))  # 交集
   print(v1.union(v2))  # 并集
   print(v1.difference(v2))  # 差集
   print(v2.difference(v1))  # 差集
   ```

8. 第八题

   ```python
   """循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）"""
   lis = []
   while True:
       msg = input('>>>:')
       if msg.upper() == 'N':
           break
       else:
           lis.append(msg)
   print(lis)
   ```

9. 第九题

   ```python
   """循环提示用户输入，并将输入内容添加到集合中（如果输入N或n则停止循环）"""
   se = set()
   while True:
       msg = input('>>>:')
       if msg.upper() == 'N':
           break
       else:
           se.add(msg)
   print(se)
   
   ```

10. 第十题

    ```python
    """v1 = {'alex','武sir','肖大'}
    v2 = []
    
    # 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）"""
    v1 = {'alex', '武sir', '肖大'}
    v2 = []
    while True:
        msg = input('>>>:')
        if msg.upper() == 'N':
            break
        elif msg in v1:
            v2.append(msg)
        else:
            v1.add(msg)
    print(v1)
    print(v2)
    ```

11. 第十一题

    ```python
    """判断以下值那个能做字典的key ？那个能做集合的元素？
    
    1   可以
    -1  可以
    ""  可以
    None    可以
    [1,2]   不可以
    (1,)    可以
    {11,22,33,4}    不可以
    {'name':'wupeiqi','age':18} 不可以
    """
    ```

12. 第十二题

    ```python
    '''is 和 == 的区别？'''
    # is是比较内存地址的, ==是比较两个值的
    ```

13. 第十三题

    ```python
    '''type使用方式及作用？'''
    # type是用来查看数据类型的
    ```

14. 第十四题

    ```python
    '''id的使用方式及作用？'''
    # id是用来查看内存地址的
    ```

15. 第十五题

    ```python
    '''看代码写结果并解释原因
    
    v1 = {'k1':'v1','k2':[1,2,3]}
    v2 = {'k1':'v1','k2':[1,2,3]}
    
    result1 = v1 == v2 
    result2 = v1 is v2 
    print(result1)
    print(result2)'''
    # 打印结果:True  False
    # 第一个是比较v1和v2的值,第二个是比较v1和v2的内存地址
    ```

16. 第十六题

    ```python
    """看代码写结果并解释原因
    
    v1 = {'k1':'v1','k2':[1,2,3]}
    v2 = v1
    
    result1 = v1 == v2 
    result2 = v1 is v2 
    print(result1)
    print(result2)"""
    # 打印结果:True  False
    # result1比较的是v1和v2的值,result2比较的是v1和v2的内存地址
    
    ```

17. 第十七题

    ```python
    """看代码写结果并解释原因
    
    v1 = {'k1':'v1','k2':[1,2,3]}
    v2 = v1
    
    v1['k1'] = 'wupeiqi'
    print(v2)"""
    
    # 打印结果:{'k1': 'wupeiqi', 'k2': [1, 2, 3]}
    # v1赋值给v2,v2指向v1的内存地址,v1修改属于在内部修改
    ```

18. 第十八题

    ```python
    """看代码写结果并解释原因
    
    v1 = '人生苦短，我用Python'
    v2 = [1,2,3,4,v1]
    
    v1 = "人生苦短，用毛线Python"
    
    print(v2)"""
    
    # 打印结果:[1,2,3,4,人生苦短，我用Python]
    # v2列表中指向v1的内存地址,下边v1从新开辟了一个新的内存地址,和上边的没关系
    ```

19. 第十九题

    ```python
    """看代码写结果并解释原因
    
    info = [1,2,3]
    userinfo = {'account':info, 'num':info, 'money':info}
    
    info.append(9)
    print(userinfo)
    
    info = "题怎么这么多"
    print(userinfo)"""
    # 打印结果:{'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}
    #         {'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}
    # userinfo指向的是info的内存地址,info追加属于在内部追加,下边的info是开辟一个新的内存地址
    ```

20. 第二十题

    ```python
    """看代码写结果并解释原因
    
    info = [1,2,3]
    userinfo = [info,info,info,info,info]
    
    info[0] = '不仅多，还特么难呢'
    print(info,userinfo)"""
    
    # info 第一个元素都换成了'不仅多,还特么难呢',info[0]在内部修改没有开辟一个新的内存空间
    ```

21. 第二十一题

    ```python
    """看代码写结果并解释原因
    
    info = [1,2,3]
    userinfo = [info,info,info,info,info]
    
    userinfo[2][0] = '闭嘴'
    print(info,userinfo)"""
    
    # userinfo[2][0] 等同于 info[0],userinfo和info指向的是一块内存地址
    ```

22. 第二十二题

    ```python
    """看代码写结果并解释原因
    
    info = [1,2,3]
    user_list = []
    for item in range(10):
        user_list.append(info)
        
    info[1] = "是谁说Python好学的？"
    
    print(user_list)"""
    
    # [1, '是谁说Python好学的？', 3]打印10次
    # user_list循环10次追加info,user_list指向的是info的内存地址,所以info[1]修改后,user_list里边也会修改
    ```

23. 第二十三题

    ```python
    """看代码写结果并解释原因
    
    data = {}
    for i in range(10):
        data['user'] = i
    print(data)"""
    # 字典是可变数据类型,字典中键是不可变的,所以循环10次每次都覆盖上一次的值
    ```

24. 第二十四题

    ```python
    """看代码写结果并解释原因
    
    data_list = []
    data = {}
    for i in range(10):
        data['user'] = i
        data_list.append(data)
    print(data_list)"""
    
    # 列表中打印10个{'user': 9},字典是可变数据类型,data内存地址中的值都被9覆盖
    ```

25. 第二十五题

    ```python
    """看代码写结果并解释原因
    
    data_list = []
    for i in range(10):
        data = {}
        data['user'] = i
        data_list.append(data)
    print(data_list)"""
    
    # [{'user': 0}, {'user': 1}, {'user': 2}, {'user': 3}, {'user': 4}, {'user': 5}, {'user': 6}, {'user': 7}, {'user': 8}, {'user': 9}]
    # 每次循环,data都会形成一个新的内存地址,data_list列表中每形成一次都会追加进去
    ```


