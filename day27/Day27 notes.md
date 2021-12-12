# Day27 notes

## 今日内容

- 协程

### 协程

是单线程下的并发，又称微线程，纤程。英文名Coroutine。一句话说明什么是协程：**协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的。**

强调：

- python的线程属于内核级别的，即由操作系统控制调度，线程遇到IO就会被迫切换到其他线程运行
- 单线程内开启协程，一旦遇到io，就会从应用程序级别（也就是自己写的程序）控制切换，以此来提升效率

对比操作系统控制线程的切换，用户在单线程内控制协程的切换

优点：

- 协程的切换开销更小，属于程序级别的切换，操作系统完全感知不到，因而更加轻量级、
- 单线程内就可以实现并发的效果，最大限度地利用cpu

缺点：

- 协程的本质是单线程下，无法利用多核，可以是一个程序开启多个进程，每个进程内开启多个线程，每个线程内开启协程

- 协程指的是单个线程，因而一旦协程出现阻塞，将会阻塞整个线程

总结：

1. 必须在只有单线程里实现协程
2. 修改共享数据不需要加锁
3. 用户程序里自己保存多个控制流的上下文栈

附加：一个协程遇到IO操作自动切换到其它协程（如何实现检测IO，yield、greenlet都无法实现，就用到了gevent模块（select机制）

#### 1.greenlet模块

如果我们想要实现在多个线程任务之间切换，使用yield生成器之间切换很麻烦，而使用greenlet模块可以很简单的实现。

示例：

```python
from greenlet import greenlet


def eat(name):
    print('%s eat 1' % name)
    g2.switch('egon')
    print('%s eat 2' % name)
    g2.switch()


def play(name):
    print('%s play 1' % name)
    g1.switch()
    print('%s play 2' % name)


g1 = greenlet(eat)
g2 = greenlet(play)

# 可以在第一次switch时传入参数，以后都不需要
g1.switch('egon')
```

greenlet只是提供了一种比generator更加便捷的切换方式，当切到一个任务执行时如果遇到io，那就原地阻塞，仍然是没有解决遇到IO自动切换来提升效率的问题。

示例：

```python
import time
from greenlet import greenlet


def eat(name):
    print('%s eat 1' % name)
    time.sleep(10)
    g2.switch('aaa')
    print('%s eat 2' % name)
    g2.switch()


def play(name):
    print('%s play 1' % name)
    g1.switch()
    print('%s play 2' % name)


g1 = greenlet(eat)
g2 = greenlet(play)

# 可以在第一次switch时传入参数，以后都不需要
g1.switch('aaa')
```

#### 2.gevent模块

Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是**Greenlet**, 它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。

用法：

- g1=gevent.spawn(func,1,,2,3,x=4,y=5)创建一个协程对象g1，spawn括号内第一个参数是函数名，如eat，后面可以有多个参数，可以是位置实参或关键字实参，都是传给函数eat的

- g2=gevent.spawn(func2)
- g1.join()  # 等待g1结束
- g2.join()  # 等待g2结束

- 或者上述两步合作一步：gevent.joinall([g1,g2])
- g1.value # 拿到func1的返回值

**遇到IO阻塞时会自动切换任务**：

示例：

```python
# pip3 install gevent
from gevent import monkey;
import gevent
import time
monkey.patch_all()


def eat(name):
    print('%s eat 1' % name)
    # gevent.sleep(3)
    time.sleep(3)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    # # gevent.sleep(4)
    time.sleep(4)
    print('%s play 2' % name)


start_time = time.time()
g1 = gevent.spawn(eat, 'aaa')
g2 = gevent.spawn(play, 'bbb')

g1.join()
g2.join()
stop_time = time.time()
print(stop_time - start_time)
```

示例中：

- gevent.sleep(3)模拟的是gevent识别IO阻塞

- time.sleep(3)或其他的阻塞，gevent是不能直接识别的，需要打补丁后就可以识别了

    ```python
    from gevent import monkey
    monkey.patch_all()
    ```

- monkey.patch_all()必须放到被打补丁者的前面

或者我们直接写成：**要用gevent，需要将from gevent import monkey;monkey.patch_all()放到文件的开头**

```
from gevent import monkey;monkey.patch_all()
import gevent
import time

def eat(name):
    print('%s eat 1' % name)
    time.sleep(3)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    time.sleep(4)
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'aaa')
g2 = gevent.spawn(play, 'bbb')

gevent.joinall([g1, g2])
print('zhu')
```

通过gevent实现单线程下的socket并发:

示例：

服务端：

```python
# 基于gevent实现
from gevent import monkey, spawn; monkey.patch_all()
from socket import *


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()


def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        spawn(communicate, conn)

    server.close()


if __name__ == '__main__':
    g = spawn(server, '127.0.0.1', 8090)
    g.join()

```

客户端：多线程并发多个客户端

```python
from threading import Thread
from socket import *
import threading

def client(server_ip,port):
    c=socket(AF_INET,SOCK_STREAM)  # 套接字对象一定要加到函数内，即局部名称空间内，放在函数外则被所有线程共享，则大家公用一个套接字对象，那么客户端端口永远一样了
    c.connect((server_ip,port))

    count=0
    while True:
        c.send(('%s say hello %s' %(threading.current_thread().getName(),count)).encode('utf-8'))
        msg=c.recv(1024)
        print(msg.decode('utf-8'))
        count+=1
if __name__ == '__main__':
    for i in range(500):
        t=Thread(target=client,args=('127.0.0.1',8090))
        t.start()
```

