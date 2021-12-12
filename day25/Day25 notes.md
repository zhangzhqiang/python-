# Day25 notes

## 今日内容

- 认识线程
- 在python中操作进程
    1. multiprocessing模块
    2. Process类,完成进程的开启,销毁,基础操作
    3. Lock锁的概念
    4. 数据的安全问题

### 1、线程

#### 1.线程的特点

- 线程是进程中的一部分
- 每一个进程中至少有一个线程,线程是负责执行具体代码的
- 线程是计算机中能被CPU调度的最小单位(进程是负责圈资源的，线程负责执行具体代码)
- 一个进程的多个线程是可以共享这个进程的数据的，即数据共享

#### 2.线程的开销

- 线程的创建,也需要一些开销(一个存储局部变量的结构,记录状态)
    - 线程的创建、切换和销毁开销远远小于进程
    - 进程：数据隔离， 开销大，同时执行几段代码
    - 线程：数据共享，开销小，同时执行几段代码

#### 3.开启进程的两种方式

方式一：

```python
import time
from multiprocessing import Process


def task(name):
    print('%s is running' % name)
    time.sleep(3)
    print('%s is done' % name)


if __name__ == '__main__':
    # 在主进程下开启子进程
    p = Process(target=task, args=('紫禁城',))
    p = Process(target=task, kwargs={'name':'紫禁城'})
    p.start()  # 给操作系统发送一个信号
    # 异步--调用开启进程的方法,但是并不等待这个进程是否开启，只是负责通知操作系统进行，开启进程后，主进程和子进程，各自进行
    print('主进程/主线程')
```

- 几乎是t.start ()的同时就将线程开启了，然后先打印出了hello，证明线程的创建开销极小
- p.start ()将开启进程的信号发给操作系统后，操作系统要申请内存空间，让好拷贝父进程地址空间到子进程，开销远大于线程

方式二：使用面向对象重写Process方法

```python
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):  # 函数名必须是run
        print('%s is running!' % self.name)
        time.sleep(2)
        print('%s is done' % self.name)


if __name__ == '__main__':
    p = MyProcess('紫禁城')
    p.start()
    print('ok')
```

查看进程的pid和ppid：

示例：

```python
import os
import time
from multiprocessing import Process

# getpid查看自己的进程id，getppid查看他爹的进程id

def task():
    print('%s is running, parent is <%s>====%s' % (os.getpid(), os.getppid(), os.getppid()))
    time.sleep(3)
    print('%s is done, parent is <%s>=======%s' % (os.getpid(), os.getppid(), os.getppid()))


if __name__ == '__main__':
    p = Process(target=task,)
    p.start()  # 给操作系统发送一个信号
    print('主流程', os.getpid(), os.getppid())  # windows查看：tasklist | findstr pycharm
    
'''
结果：
主流程 12140 9932
11540 is running, parent is <12140>====12140
11540 is done, parent is <12140>=======12140
'''
```

- 在主进程下开启子进程，子进程的ppid就是主进程的pid

#### 4.进程的数据隔离

- 主进程没结束:等待子进程结束
- 在pycharm中启动的所有py程序都是pycharm的子进程
- 主进程会等待所有的子进程结束以后才结束，目的是为了回收资源，如果子进程执行结束，主进程没有回收资源，那么这个子进程会变成一个僵尸进程。

#### 5.主进程的结束逻辑

- 主进程的代码结束
- 所有的子进程结束
- 给子进程回收资源
- 主进程结束

进程开启的过程中windows和linux/ios之间的区别：

- window中，需要相当于在子进程中把主进程文件又从头到尾执行了一遍，除了放在if`__name__` == '`__main__`'下的代码
- linux中 不执行代码,而是把当前代码全部加载到内存，直接执行调用内存中的func函数

主程序的结束逻辑：

- 主进程的代码结束
- 所有的子进程结束
- 给子进程回收资源
- 主进程结束

#### 6.join方法

- 作用:阻塞,直到子进程结束就结束

- 把一个进程结束时间封装成一个join方法

- 执行join方法的效果就是阻塞，直到这个子进程执行结束就结束阻塞

- 在多个子进程中使用join

```python
def task():
    print('%s is running, parent is <%s>====%s' % (os.getpid(), os.getppid(), os.getppid()))
    time.sleep(3)
    print('%s is done, parent is <%s>=======%s' % (os.getpid(), os.getppid(), os.getppid()))


if __name__ == '__main__':
    p = Process(target=task,)
    p.start()  # 给操作系统发送一个信号

    p.join()  # 子进程先执行
    print('主流程', os.getpid(), os.getppid())
    print(p.pid)
```

多个子进程：

```python
def task(name, n):
    print('%s is running' % name)
    time.sleep(n)


if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=task, args=('紫禁城1', 5))
    p2 = Process(target=task, args=('紫禁城2', 3))
    p3 = Process(target=task, args=('紫禁城3', 2))
    p4 = Process(target=task, args=('紫禁城4', 1))

    p_l = [p1, p2, p3, p4]
    for p in p_l:
        p.start()
    for p in p_l:
        p.join()
    print('主进程', (time.time()-start))
```

#### 7.守护进程

daemon把进程设置为守护进程

守护进程会在主进程代码执行结束后就终止

- 需要强调的是：运行完毕并非终止运行
- 对主进程来说，运行完毕指的是主进程代码运行完毕
- 主进程在其代码结束后就已经算运行完毕了（守护进程在此时就被回收），然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束

示例一：

```python
from multiprocessing import Process
import time


def task(name):
    print('%s is running' % name)
    time.sleep(2)


if __name__ == '__main__':
    p = Process(target=task, args=('子进程',))
    p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    p.start()

    p.join()
    print('主')  # 只要终端打印出这一行内容，那么守护进程p也就跟着结束掉了
```

示例二：

```python
def Foo():
    print(123)
    time.sleep(1)
    print('end123')


def Bar():
    print(456)
    time.sleep(2)
    print('end456')


if __name__ == '__main__':
    p1 = Process(target=Foo)
    p2 = Process(target=Bar)

    p1.daemon = True
    p1.start()
    p2.start()
    print('main---------')
```

#### 8.互斥锁

互斥锁的原理，就是把并发改成穿行，降低了效率，但保证了数据安全不错乱

```python
# 由并发变成了串行,牺牲了运行效率,但避免了竞争
import time
from multiprocessing import Process, Lock


def task(name, mentu):
    mentu.acquire()  # 加锁
    print('%s 1' % name)
    time.sleep(1)
    print('%s 2' % name)
    time.sleep(2)
    print('%s 3' % name)
    time.sleep(3)
    mentu.release()  # 解锁


if __name__ == '__main__':
    mentu = Lock()
    for i in range(3):
        p = Process(target=task, args=('进程%s' % i, mentu))
        p.start()

```

练习一：模拟抢票

```python
# 把文件db.txt的内容重置为：{"count":1}

def search(name):
    time.sleep(1)
    dict = json.load(open('db.json', 'r', encoding='utf-8'))
    print('<%s>查看到剩余票数{%s}' % (name, dict['count']))


def get(name):
    time.sleep(1)
    dict = json.load(open('db.json', 'r', encoding='utf-8'))
    if dict['count'] > 0:
        dict['count'] -= 1
        json.dump(dict, open('db.json', 'w', encoding='utf-8'))
        print('<%s> 购票成功!' % name)
    else:
        print('没有足够的票!')


def task(name, mutex):
    search(name)
    with mutex:  # 相当于lock.acquire(),执行完自代码块自动执行lock.release()
        get(name)


if __name__ == '__main__':
    mutex = Lock()
    for i in range(10):  # 模拟10个人并发抢票
        p = Process(target=task, args=('路人%s' % i, mutex))
        p.start()
```

1. 在数据安全的基础上,才考虑效率问题
2. 同步存在的意义:数据的安全性
3. 在主进程中实例化 mutex = Lock()
4. 把这个锁传递给子进程
5. 在子进程中,对需要加锁的代码进行 with lock:with lock相当于lock.acquire()和lock.release
6. 在进程中需要加锁的场景:
    1. 共享的数据资源(文件,数据库)
    2. 对资源进行修改,删除操作
7. 加锁之后能保证数据的安全性,但是也降低了程序的执行效率

**互斥锁与join的区别**：

- 互斥锁和join都是把并发变成串行
- join是把所有的代码都变成串行，互斥锁是把部分的代码变成串行

#### 9.队列

进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的。

**创建队列的类（底层就是以管道和锁定的方式实现）**：

```python
Queue([maxsize]):创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
```

**参数介绍：**

```python
maxsize是队列中允许最大项数，省略则无大小限制。
但需要明确：
    1、队列内存放的是消息而非大数据
    2、队列占用的是内存空间，因而maxsize即便是无大小限制也受限于内存大小
```

**主要方法介绍：**

```
q.put方法用以插入数据到队列中。
q.get方法可以从队列读取并且删除一个元素。
```

**队列的使用**：

```python
from multiprocessing import Process,Queue

q=Queue(3)

#put ,get ,put_nowait,get_nowait,full,empty
q.put(1)
q.put(2)
q.put(3)
print(q.full())  # 判断是否满了
# q.put(4)  # 再放就阻塞住了，卡死

print(q.get())
print(q.get())
print(q.get())
print(q.empty())  # 判断是否空了
# print(q.get())  # 再取就阻塞住了，卡死
```

#### 10.生产者与消费者模型

**为什么要使用生产者消费者模型**

生产者指的是生产数据的任务，消费者指的是处理数据的任务，在并发编程中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

**什么是生产者和消费者模式**

生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。

- 这个阻塞队列就是用来给生产者和消费者解耦的

```python
from multiprocessing import Process, Queue
import time


def producer(q):
    for i in range(3):
        res = '包子%s' % i
        time.sleep(0.5)
        print('生产者生产了%s' % res)

        q.put(res)


def consumer(q):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(1)
        print('消费者吃了%s' % res)


if __name__ == '__main__':
    # 容器
    q = Queue()

    # 生产者们
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=producer, args=(q,))
    p3 = Process(target=producer, args=(q,))

    # 消费者们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    q.put(None)
    q.put(None)
    print('主')
```

上述在有多个生产者和多个消费者时，我们则需要用一个很low的方式去解决,有几个消费者就需要发送几次结束信号：相当low！

#### 11.**JoinableQueue([maxsize])**

```
这就像是一个Queue对象，但队列允许项目的使用者通知生成者项目已经被成功处理。通知进程是使用共享的信号和条件变量来实现的。
```

**参数介绍**：

```
maxsize是队列中允许最大项数，省略则无大小限制。
```

**方法介绍**：

```
JoinableQueue的实例p除了与Queue对象相同的方法之外还具有：
q.task_done()：使用者使用此方法发出信号，表示q.get()的返回项目已经被处理。如果调用此方法的次数大于从队列中删除项目的数量，将引发ValueError异常
q.join():生产者调用此方法进行阻塞，直到队列中所有的项目均被处理。阻塞将持续到队列中的每个项目均调用q.task_done（）方法
```

基于JoinableQueue实现生产者消费者模型：

```python
from multiprocessing import Process, JoinableQueue
import time


def producer(q):
    for i in range(2):
        res = '包子%s' % i
        time.sleep(0.5)
        print('生产者生产了%s' % res)

        q.put(res)
    q.join()


def consumer(q):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(1)
        print('消费者吃了%s' % res)
        q.task_done()


if __name__ == '__main__':
    # 容器
    q = JoinableQueue()

    # 生产者们
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=producer, args=(q,))
    p3 = Process(target=producer, args=(q,))

    # 消费者们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    c1.daemon = True
    c2.daemon = True

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    print('主')

```

总结：

- 程序中有两类角色

```
一类负责生产数据（生产者）
一类负责处理数据（消费者）
```

- 引入生产者消费者模型为了解决的问题是

```
平衡生产者与消费者之间的速度差
程序解开耦合
```

- 如何实现生产者消费者模型

```
生产者<--->队列<--->消费者
```

