# Day26 notes

## 今日内容

- 多线程

### 线程

#### 1.什么是线程

进程只是用来把资源集中到一起（进程只是一个资源单位，或者说资源集合），而线程才是cpu上的执行单位。

线程的特点：

- 线程是进程中的一部分
- 每一个进程中至少有一个线程,线程是负责执行具体代码的
- 线程是计算机中能被CPU调度的最小单位(进程是负责圈资源的，线程负责执行具体代码)
- 一个进程的多个线程是可以共享这个进程的数据的，即数据共享

线程的开销：

- 线程的创建,也需要一些开销(一个存储局部变量的结构,记录状态)
    - 线程的创建、切换和销毁开销远远小于进程
    - 进程：数据隔离， 开销大，同时执行几段代码
    - 线程：数据共享，开销小，同时执行几段代码

#### 2.开启线程的两种方式：

multiprocess模块的完全模仿了threading模块的接口，二者在使用层面，有很大的相似性。

方式一：

```python
import time
import random
from threading import Thread


def piao(name):
    print('%s piaoing' % name)
    time.sleep(random.randrange(1, 5))
    print('%s piao end' % name)


if __name__ == '__main__':
    t1 = Thread(target=piao, args=('ike',))
    t1.start()
    print('主线程')
```

方式二：面向对象

```python
import time
import random
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s piaoing' % self.name)

        time.sleep(random.randrange(1, 5))
        print('%s piao end' % self.name)


if __name__ == '__main__':
    t1 = MyThread('egon')
    t1.start()
    print('主') 
```

#### 3.进程与线程的区别

1. 同一个进程内的多个线程共享该进程内的地址空间
2. 创建线程的开销要远小于创建进程的开销（创建一个进程，就是创建一个车间，涉及到申请空间，而且在该空间内建至少一条流水线，但创建线程，就只是在一个车间内造一条流水线，无需申请空间，所以创建开销小）

**3.1 开进程的开销远大于开线程**：

1.主进程下开子进程：

```python
import time
from multiprocessing import Process


def piao(name):
    print('%s running' % name)
    time.sleep(2)
    print('%s running end' % name)


if __name__ == '__main__':
    p1=Process(target=piao,args=('ike',))
    p1.start()
    print('主进程')
    
'''
执行结果：
主线程
ike running
ike running end
'''
```

备注：p.start ()将开启进程的信号发给操作系统后，操作系统要申请内存空间，让好拷贝父进程地址空间到子进程，开销远大于线程

2.主线程下开子线程：

```python
import time
from threading import Thread

def piao(name):
    print('%s running' % name)
    time.sleep(2)
    print('%s running end' % name)


if __name__ == '__main__':

    t1 = Thread(target=piao, args=('egon',))
    t1.start()
    print('主线程')
```

备注：几乎是t.start ()的同时就将线程开启了，然后先打印出了ike running，证明线程的创建开销极小

示例：同一进程内的多个线程共享该进程的地址空间

**3.2 进程与线程的地址空间**：

1.进程之间的地址空间是隔离的：

```python
from multiprocessing import Process

n = 100

def task():
    global n
    n = 0

if __name__ == '__main__':
    p1=Process(target=task,)
    p1.start()
    p1.join()

    print('主进程', n)
```

备注：进程p已经将自己的全局的n改成了0，但改的仅仅是它自己的,查看父进程的n仍然为100

2.同一进程内开启的多个线程是共享该进程地址空间的：

```python
from threading import Thread

n = 100

def task():
    global n
    n = 0

if __name__ == '__main__':

    t1 = Thread(target=task, )
    t1.start()
    t1.join()

    print('主线程', n)

```

备注： 查看结果为0,因为同一进程内的线程之间共享进程内的数据

**3.3 进程与线程的PID**：

1.开启多个进程,每个进程的PID都不一样：

```python
from multiprocessing import Process, current_process
import os


def task():
    # print(current_process().pid)
    print('子进程PID:%s  父进程的PID:%s' % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    p1 = Process(target=task, )
    p1.start()

    # print('主线程',current_process().pid)
    print('主线程PID:', os.getpid())
    
    
'''
结果：
主线程PID: 9996
子进程PID: 8900  父进程的PID: 9996
'''
```

备注：主进程和子进程不属于同一个进程

2.在主进程下开启多个线程,每个线程都跟主进程的PID一样：

```python
from threading import Thread
import os


def task():
    print('子线程PID: %s' % (os.getpid()))


if __name__ == '__main__':
    t1 = Thread(target=task, )
    t1.start()

    print('主线程PID:', os.getpid())
    
    
'''
结果：
子线程PID: 9528
主线程PID: 9528
'''
```

备注：因为他们同属于一个进程

#### 4.Thread对象的其他属性

- getName()：获取线程名
- setName()：设置线程名
- is_alive()：查看线程是否存活
- active_count()：获取线程活跃数
- enumerate()：当前活跃的线程对象
- currentThread()：获取当前的线程变量

示例：

```python
from threading import Thread, currentThread, active_count, enumerate
import time


def task():
    print('%s is running ' % currentThread().getName())
    time.sleep(2)
    print('%s is done ' % currentThread().getName())


if __name__ == '__main__':
    t = Thread(target=task, name='子线程')
    t.start()

    # 设置子线程名字， 默认Thread-1
    t.setName('儿子线程')

    # 设置主线程名字，默认MainThread
    currentThread().setName('主线程1')

    # 查看线程是否存活
    t.join()  # 执行这行代码后，线程已运行完，返货就是False
    print(t.is_alive())

    # 线程活跃数
    print(active_count())

    # 当前活跃的线程对象
    print(enumerate())

    # 当前的线程变量
    print('主线程', currentThread())
    print('主线程', currentThread().getName())
```

#### 5.守护线程

守护线程会在主线程代码执行结束后就终止

- 需要强调的是：运行完毕并非终止运行
    - 对主进程来说，运行完毕指的是主进程代码运行完毕
    - 对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程全部运行完毕，主线程才算运行完毕
    - 主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束

示例一：

```python
from threading import Thread
import time


def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)


if __name__ == '__main__':
    t = Thread(target=sayhi, args=('egon',))
    # 必须在t.start()之前设置  同等于 t.daemon = True
    t.setDaemon(True)
    t.start()

    print('主线程')
    print(t.is_alive())
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

因为非守护线程没有运行完，所以打印了end123

#### 6.GIL解释器锁

##### 1.GIL锁介绍

GIL本质就是一把互斥锁，既然是互斥锁，所有互斥锁的本质都一样，都是将并发运行变成串行，以此来控制同一时间内共享数据只能被一个任务所修改，进而保证数据安全。

**保护不同的数据的安全，就应该加不同的锁。**

每次执行python程序，都会产生一个独立的进程。例如python test.py，python aaa.py，python bbb.py会产生3个不同的python进程。

示例：

```python
#test.py内容
import os,time
print(os.getpid())
time.sleep(1000)

#打开终端执行
python3 test.py

#在windows下查看
tasklist |findstr python

#在linux下下查看
ps aux |grep python
```

在一个python进程内，不仅有自己编写代码开启的主线程或由该线程开启的其他线程，另外还有解释器开启的垃圾回收等解释器级别的线程，总之，所有线程都是运行在这一个进程内。

- 所有数据都是共享的，这其中代码作为一种数据也是被所有线程共享的
    - 自己写的代码
    - Cpython解释器的代码
- 所有线程任务，都需要将代码当做参数传递给解释器的代码去执行，即所有的线程想要运行自己的任务，首先要解决的问题是能访问到解释器的代码

案例：

解释器的代码是所有线程共享的，所有Cpython垃圾回收线程也可能访问到解释器代码而去执行，这样就会导致一个问题：

- 相对于同一个数据，比如：100
- 开启多个线程：线程1执行x=100，而Cpython垃圾回收线程执行的回收的操作，这样就会冲突

解决这个问题就是加GIL锁处理，保证python解释器同一时间只能执行一个任务的代码，如图：

![GIL解释器锁](G:\homework\img\GIL解释器锁.png)

##### 2.GIL与LOCK的区别

共同点：将并发运行变成串行，锁的目的是为了保护共享的数据，同一时间只能有一个线程来修改共享的数据。

结论：保护不同的数据就应该加不同的锁。

总结：GIL 与Lock是两把锁，保护的数据不一样

- GIL是解释器级别的，保护的就是解释器级别的数据，比如垃圾回收的数据
- Lock保护自己开发的程序的数据，分工明确

- 所以GIL不负责自己开发的程序的数据，只能由自己去加锁处理

分析：

1. GIL锁相当于一个权限，比如有10个线程，自己写的程序有加了lock锁
2. 这10个线程都去抢GIL锁，肯定有一个1抢到，比如线程1，即拿到权限，然后去执行，执行就会拿到lock.acquire()
3. 很有可能由于各种因素，线程1还未执行完毕就被线程2抢到权限了，然后线程2执行，然后线程2发现lock锁还在线程1那，还没释放，所以就阻塞了，被迫线程2交出权限，即释放GIL
4. 线程1又夺回权限，开始上一次暂停的位置继续执行，直到lock锁被释放lock.release()
5. 其他的线程重复执行这一系列的步骤

示例：

```python
from threading import Thread, Lock
import time


def work():
    global n
    lock.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    n = 100
    l = []
    for i in range(100):
        p = Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()

    print(n)
# 结果为0，由原来的并发执行变成串行，牺牲了执行效率保证了数据安全，不加锁则结果可能为99
```

##### 3.GIL与多线程

- 多线程用于IO密集型
- 多进程用于计算密集型
- 单核：
    - 计算密集型适用一个进程下开多个线程，因为没有多核并行计算，单核创建进程增加开销
    - IO密集型适用一个进程下开多个线程，因为单核创建进程增加开销，切进程的速度慢于开线程
- 多核：
    - 计算密集型适用开多个进程，因为可以并行计算
    - IO密集型适用一个进程下开多个线程，因为再多的核也解决不了IO问题

总结：现在的计算机基本上都是多核，python对于计算密集型的任务开多线程的效率并不能带来多大性能上的提升，甚至不如串行(没有大量切换)，但是，对于IO密集型的任务效率还是有显著提升的。

示例一：**如果并发的多个任务是计算密集型：多进程效率高**

```python
# 计算密集型：用多进程
from multiprocessing import Process
from threading import Thread
import os, time

# 模拟计算密集型
def work():
    res = 0
    for i in range(100000000):
        res *= i


if __name__ == '__main__':
    l = []
    print(os.cpu_count())  # 本机为8核
    start = time.time()
    for i in range(8):
        p = Process(target=work)  # 耗时14s多
        # p = Thread(target=work)  # 耗时47s多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop = time.time()
    print('run time is %s' % (stop - start))
```

示例二：**如果并发的多个任务是I/O密集型：多线程效率高**

```python
# IO密集型：用多线程
from multiprocessing import Process
from threading import Thread
import threading
import os, time


# 模仿IO密集型
def work():
    time.sleep(2)


if __name__ == '__main__':
    l = []
    print(os.cpu_count())  # 本机为8核
    start = time.time()
    for i in range(400):
        # p = Process(target=work)  # 耗时15.140多,大部分时间耗费在创建进程上
        p = Thread(target=work)  # 耗时2.066多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop = time.time()
    print('run time is %s' % (stop - start))
```

#### 7.死锁与递归锁

##### 7.1死锁

是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，这些永远在互相等待的进程称为死锁进程。

互斥锁只能acquire一次，只有释放了这次才能进行继续进行下去。

死锁示例：

```python
from threading import Thread, Lock
import time

mutexA = Lock()
mutexB = Lock()


class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)

        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        mutexB.release()

        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        time.sleep(0.1)

        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)
        mutexA.release()

        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
'''
结果：
Thread-1 拿到了A锁
Thread-1 拿到了B锁
Thread-1 拿到了B锁
Thread-2 拿到了A锁
'''
```

备注：Thread-1第二次拿到了B，但是一直没释放，这种现象就是死锁现象。

##### 7.2递归锁

在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock。

RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require，直到一个线程所有的acquire都被release，其他的线程才能获得资源。

递归锁与互斥锁的区别：

- 递归锁可以连续acquire多次
- 互斥锁只能acquire一次

递归锁示例：

```python
# 递归锁:可以连续acquire多次，每acquire一次计数器+1，只有计数为0时，才能被抢到acquire
from threading import Thread, RLock
import time

mutexB = mutexA = RLock()


class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)

        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        mutexB.release()

        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        time.sleep(7)

        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)
        mutexA.release()

        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
```

#### 8.信号量

信号量也是一把锁，信号量可以指定一个数，比如：5。

互斥锁与信号量对比：

- 互斥锁同一时间只能有一个任务去抢到锁执行
- 信号量是根据指定的数的任务去抢锁执行

示例：

```python
from threading import Thread, Semaphore, currentThread
import time, random

# 管理一个内置的计数器
sm = Semaphore(3)

# 计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()
def task():
    
    # 每当调用acquire()时内置计数器-1
    # sm.acquire()
    # print('%s in' %currentThread().getName())

    # 调用release() 时内置计数器+1
    # sm.release()
    with sm:
        print('%s in' % currentThread().getName())
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task)
        t.start()

```

#### 9. Even事件

Python提供了Event对象用于线程间通信，它是由线程设置的信号标志，在初始情况下，Event对象中的信号标志被设置为假，如果有线程等待一个Event对象, 而这个Event对象的标志为假，那么这个线程将会被一直阻塞直至该标志为真。一个线程如果将一个Event对象的信号标志设置为真,它将唤醒所有等待这个Event对象的线程。

```
from threading import Event

event.isSet()：返回event的状态值；

event.wait()：如果 event.isSet()==False将阻塞线程；

event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；

event.clear()：恢复event的状态值为False。
```

示例一：学生上课

```python
from threading import Thread, Event
import time

event = Event()


# event.wait()
# event.set()


def student(name):
    print('学生%s 正在听课' % name)
    event.wait(0.5)
    print('学生%s 课间活动' % name)


def teacher(name):
    print('老师%s 正在授课' % name)
    time.sleep(3)
    event.set()


if __name__ == '__main__':
    stu1 = Thread(target=student, args=('Python',))
    stu2 = Thread(target=student, args=('PHP',))
    stu3 = Thread(target=student, args=('Java',))
    t1 = Thread(target=teacher, args=('Go',))

    stu1.start()

    stu2.start()
    stu3.start()
    t1.start()
```

示例二：数据库验证

```python
from threading import Thread, Event, currentThread
import time

event = Event()


def conn():
    n = 0
    while not event.is_set():
        if n == 3:
            print('%s try too many times' % currentThread().getName())
            return
        print('%s try %s' % (currentThread().getName(), n))
        event.wait(0.5)
        n += 1

    print('%s is connected' % currentThread().getName())


def check():
    print('%s is checking' % currentThread().getName())
    time.sleep(5)
    event.set()


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=conn)
        t.start()
    t = Thread(target=check)
    t.start()
```

#### 10.计时器

这个类实现了隔一段调用函数，在Timer调用的函数中，进行设置。Timer是Thread的一个派生类。

示例：验证码更新验证功能

```python
from threading import Timer
import random


class Code:
    def __init__(self):
        self.make_cache()

    def make_cache(self, interval=5):
        self.cache = self.make_code()
        print(self.cache)
        self.t = Timer(interval, self.make_cache)
        self.t.start()

    def make_code(self, n=4):
        res = ''
        for i in range(n):
            s1 = str(random.randint(0, 9))
            s2 = chr(random.randint(65, 90))
            res += random.choice([s1, s2])
        return res

    def check(self):
        while True:
            code = input('请输入你的验证码>>: ').strip()
            if code.upper() == self.cache:
                print('验证码输入正确')
                self.t.cancel()
                break


obj = Code()
obj.check()
```

#### 11.线程队列

三种不同的用法：

先进先出：queue.Queue

```python
import queue

q = queue.Queue(3)  # 先进先出->队列

q.put('first')
q.put(2)
q.put('third')
# q.put(4, block=False)  # 等同于q.put_nowait(4)
# q.put(4, block=True, timeout=3)  # block默认为True

print(q.get())
print(q.get())
print(q.get())
# print(q.get(block=False))  # 等同于q.get_nowait()

print(q.get(block=True, timeout=3))
```

堆栈--先进后出：queue.LifoQueue

```python
import queue
q = queue.LifoQueue(3)  # 后进先出->堆栈
q.put('first')
q.put(2)
q.put('third')

print(q.get())
print(q.get())
print(q.get())
```

优先级队列：queue.PriorityQueue

```python
import queue

q = queue.PriorityQueue(3)  # 优先级队列

q.put((10, 'one'))
q.put((40, 'two'))
q.put((30, 'three'))

print(q.get())
print(q.get())
print(q.get())
```

备注：存储数据时可设置优先级的队列

#### 12.进程池与线程池

基于多进程或多线程实现并发的套接字通信，这种实现方式的致命缺陷是：服务的开启的进程数或线程数都会随着并发的客户端数目地增多而增多，这会对服务端主机带来巨大的压力，甚至于不堪重负而瘫痪。于是我们必须对服务端开启的进程数或线程数加以控制，让机器在一个自己可以承受的范围内运行，这就是进程池或线程池的用途。例如进程池，就是用来存放进程的池子，本质还是基于多进程，只不过是对开启进程的数目加上了限制。

```
ThreadPoolExecutor：线程池，提供异步调用
ProcessPoolExecutor: 进程池，提供异步调用
```

基本方法：

```python
1、submit(fn, *args, **kwargs)
异步提交任务

2、map(func, *iterables, timeout=None, chunksize=1) 
取代for循环submit的操作

3、shutdown(wait=True) 
相当于进程池的pool.close()+pool.join()操作
wait=True，等待池内所有任务执行完毕回收完资源后才继续
wait=False，立即返回，并不会等待池内的任务执行完毕
但不管wait参数为何值，整个程序都会等到所有任务执行完毕
submit和map必须在shutdown之前

4、result(timeout=None)
取得结果

5、add_done_callback(fn)
回调函数
```

示例一：进程池

```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os, time, random


def task(name):
    print('name:%s pid:%s run' % (name, os.getpid()))
    time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    pool=ProcessPoolExecutor(4)

    for i in range(10):
        pool.submit(task, 'egon%s' % i)
    # 相当于进程池的pool.close()+pool.join()操作
    pool.shutdown(wait=True)

    print('主')
```

示例二：线程池

```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os, time, random


def task(name):
    print('name:%s pid:%s run' % (name, os.getpid()))
    time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)

    for i in range(10):
        pool.submit(task, 'egon%s' % i)
    # 相当于进程池的pool.close()+pool.join()操作
    pool.shutdown(wait=True)

    print('主')
```

#### 13.map方法

map取代了for循环+submit

示例：

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import os, time, random


def task(n):
    print('%s is runing' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n ** 2


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=3)

    # for i in range(11):
    #     future=executor.submit(task,i)

    executor.map(task, range(1, 3))  # map取代了for+submit
```

#### 14.调用的两种方式

同步调用：提交完任务后，就在原地等待任务执行完毕，拿到结果，再执行下一行代码,导致程序是串行执行

示例：

```python
from concurrent.futures import ThreadPoolExecutor
import time
import random


def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(3, 5))
    res = random.randint(7, 13) * '#'
    return {'name': name, 'res': res}


def weigh(shit):
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了 《%s》kg' % (name, size))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)

    shit1 = pool.submit(la, 'aaa').result()
    weigh(shit1)

    shit2 = pool.submit(la, 'bbb').result()
    weigh(shit2)

    shit3 = pool.submit(la, 'ccc').result()
    weigh(shit3)
```

回调机制：可以为进程池或线程池内的每个进程或线程绑定一个函数，该函数在进程或线程的任务执行完毕后自动触发，并接收任务的返回值当作参数，该函数称为回调函数。

示例：

```python
from concurrent.futures import ThreadPoolExecutor
import time
import random


def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(3, 5))
    res = random.randint(7, 13) * '#'
    return {'name': name, 'res': res}


def weigh(shit):
    # 拿到结果
    shit = shit.result()
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了 《%s》kg' % (name, size))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)

    pool.submit(la, 'aaa').add_done_callback(weigh)

    pool.submit(la, 'bbb').add_done_callback(weigh)

    pool.submit(la, 'ccc').add_done_callback(weigh)
# la拿到的是一个返回对象obj，需要用obj.result()拿到结果
```

