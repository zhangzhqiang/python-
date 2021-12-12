# Day28 notes

## 今日内容

- IO模型

### 1.阻塞IO

socket默认情况下都是blocking，一个典型的读操作流程是这样的：![阻塞IO](G:\homework\img\阻塞IO.png)

当用户进程调用了recvfrom这个系统调用，kernel就开始了IO的第一个阶段：准备数据。对于network io来说，很多时候数据在一开始还没有到达，这个时候kernel就要等待足够的数据到来。

用户这边整个进程会被阻塞，当kernel一直等到数据准备好了，它就会将数据从kernel中拷贝到用户内存，然后kernel返回结果，用户进程才能解除blokck状态，重新运作起来。

**所以，blocking IO的特点就是IO执行的两个阶段（等待数据和拷贝数据两个阶段），都被block了。**

```
几乎所有的程序员第一次接触到的网络编程都是从listen\(\)、send\(\)、recv\(\) 等接口开始的，
使用这些接口可以很方便的构建服务器/客户机的模型。然而大部分的socket接口都是阻塞型的
ps：
所谓阻塞型接口是指系统调用（一般是IO接口）不返回调用结果并让当前线程一直阻塞
只有当该系统调用获得结果或者超时出错时才返回。
```

示例：

服务端：

```python
from socket import *
from threading import Thread


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()


server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)

while True:
    print('starting...')
    conn, addr = server.accept()

    t = Thread(target=communicate, args=(conn,))
    t.start()

server.close()
```

客户端：

```python
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

while True:
    msg = input('>>: ').strip()
    if not msg: continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()
```

实际上，除非特别指定，几乎所有的IO接口 ( 包括socket接口 ) 都是阻塞型的。这给网络编程带来了一个很大的问题，如在调用recv(1024)的同时，线程将被阻塞，在此期间，线程将无法执行任何运算或响应任何的网络请求。

一个简单的解决方案：

```
在服务器端使用多线程（或多进程）。多线程（或多进程）的目的是让每个连接都拥有独立的线程（或进程），
这样任何一个连接的阻塞都不会影响其他的连接。
```

该方案的问题是：

```
开启多进程或都线程的方式，在遇到要同时响应成百上千路的连接请求，则无论多线程还是多进程都会严重占据系统资源，
降低系统对外界响应效率，而且线程与进程本身也更容易进入假死状态。
```

改进方案：

```
很多程序员可能会考虑使用“线程池”或“连接池”。“线程池”旨在减少创建和销毁线程的频率，
其维持一定合理数量的线程，并让空闲的线程重新承担新的执行任务。“连接池”维持连接的缓存池，尽量重用已有的连接、
减少创建和关闭连接的频率。这两种技术都可以很好的降低系统开销，都被广泛应用很多大型系统，如websphere、tomcat和各种数据库等。
```

改进后方案其实也存在着问题：

```
“线程池”和“连接池”技术也只是在一定程度上缓解了频繁调用IO接口带来的资源占用。而且，所谓“池”始终有其上限，
当请求大大超过上限时，“池”构成的系统对外界的响应并不比没有池的时候效果好多少。所以使用“池”必须考虑其面临的响应规模，
并根据响应规模调整“池”的大小。
```

**对应上例中的所面临的可能同时出现的上千甚至上万次的客户端请求，“线程池”或“连接池”或许可以缓解部分压力，但是不能解决所有问题。总之，多线程模型可以方便高效的解决小规模的服务请求，但面对大规模的服务请求，多线程模型也会遇到瓶颈，可以用非阻塞接口来尝试解决这个问题。**

### 2.非阻塞IO

通过设置socket使其变为non-blocking。当对一个non-blocking socket执行读操作时，流程是这个样子：![非阻塞IO](G:\homework\img\非阻塞IO.png)

非阻塞的recvform系统调用调用之后，进程并没有被阻塞，内核马上返回给进程，如果数据还没准备好，此时会返回一个error。进程在返回之后，可以干点别的事情，然后再发起recvform系统调用。重复上面的过程，循环往复的进行recvform系统调用。这个过程通常被称之为轮询。

轮询检查内核数据，直到数据准备好，再拷贝数据到进程，进行数据处理。需要注意，拷贝数据整个过程，进程仍然是属于阻塞的状态。

**所以，在非阻塞式IO中，用户进程其实是需要不断的主动询问kernel数据准备好了没有。**

示例：

服务端：

```python
from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8083))
server.listen(5)
server.setblocking(False)
print('starting...')

rlist = []
wlist = []
while True:

    try:
        conn, addr = server.accept()
        rlist.append(conn)
        print(rlist)
    except BlockingIOError:
        # print('干其他的活')

        # 收消息
        del_rlist = []
        for conn in rlist:
            try:
                data = conn.recv(1024)
                if not data:
                    del_rlist.append(conn)
                    continue
                wlist.append((conn, data.upper()))
            except BlockingIOError:
                continue
            except Exception:
                conn.close()
                del_rlist.append(conn)

        # 发消息
        del_wlist = []
        for item in wlist:
            try:
                conn = item[0]
                data = item[1]
                conn.send(data)
                del_wlist.append(item)
            except BlockingIOError:
                pass

        for item in del_wlist:
            wlist.remove(item)

        for conn in del_rlist:
            rlist.remove(conn)

server.close()
```

客户端：

```python
	from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8083))

while True:
    msg = input('>>: ').strip()
    if not msg: continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()
```

**非阻塞IO模型绝不被推荐！**

优点：

- 能够在等待任务完成的时间里干其他活了（包括提交其他任务，也就是 “后台” 可以有多个任务在”同时“执行）。

缺点：

- 循环调用recv()将大幅度推高CPU占用率。
- 任务完成的响应延迟增大了，因为每过一段时间才去轮询一次read操作，而任务可能在两次轮询之间的任意时间完成。这会导致整体数据吞吐量的降低。

**此外，在这个方案中recv()更多的是起到检测“操作是否完成”的作用，实际操作系统提供了更为高效的检测“操作是否完成“作用的接口，例如select()多路复用模式，可以一次检测多个连接是否活跃。**

### 3.多路复用IO

IO multiplexing这个词可能有点陌生，但是如果我说select/epoll，大概就都能明白了。有些地方也称这种IO方式为**事件驱动IO**(event driven IO)。

select/epoll的好处就在于单个process就可以同时处理多个网络连接的IO。它的基本原理就是select/epoll这个function会不断的轮询所负责的所有socket，当某个socket有数据到达了，就通知用户进程。![多路复用IO](G:\homework\img\多路复用IO.png)

当用户进程调用了select，那么整个进程会被block，而同时，kernel会“监视”所有select负责的socket，当任何一个socket中的数据准备好了，select就会返回。这个时候用户进程再调用read操作，将数据从kernel拷贝到用户进程。这个图和blocking IO的图其实并没有太大的不同，事实上还更差一些。因为这里需要使用两个系统调用\(select和recvfrom\)，而blocking IO只调用了一个系统调用\(recvfrom\)。但是，用select的优势在于它可以同时处理多个connection。

**注意：**

- **如果处理的连接数不是很高的话，使用select/epoll的web server不一定比使用multi-threading + blocking IO的web server性能更好，可能延迟还更大。select/epoll的优势并不是对于单个连接能处理得更快，而是在于能处理更多的连接。**

- **在多路复用模型中，对于每一个socket，一般都设置成为non-blocking，但是，如上图所示，整个用户的process其实是一直被block的。只不过process是被select这个函数block，而不是被socket IO给block。**

**结论: select的优势在于可以处理多个连接，不适用于单个连接**

示例：

服务端：

```python
from socket import *
import select

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8083))
server.listen(5)
server.setblocking(False)
print('starting...')

rlist = [server, ]
wlist = []
wdata = {}

while True:
    rl, wl, xl = select.select(rlist, wlist, [], 0.5)
    print('rl', rl)
    print('wl', wl)

    for sock in rl:
        if sock == server:
            conn, addr = sock.accept()
            rlist.append(conn)
        else:
            try:
                data = sock.recv(1024)
                if not data:
                    sock.close()
                    rlist.remove(sock)
                    continue
                wlist.append(sock)
                wdata[sock] = data.upper()
            except Exception:
                sock.close()
                rlist.remove(sock)

    for sock in wl:
        data = wdata[sock]
        sock.send(data)
        wlist.remove(sock)
        wdata.pop(sock)

server.close()
```

客户端：

```python
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8083))

while True:
    msg = input('>>: ').strip()
    if not msg: continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()
```

**select监听fd变化的过程分析：**

```
用户进程创建socket对象，拷贝监听的fd到内核空间，每一个fd会对应一张系统文件表，内核空间的fd响应到数据后，就会发送信号给用户进程数据已到；
用户进程再发送系统调用，比如（accept）将内核空间的数据copy到用户空间，同时作为接受数据端内核空间的数据清除，这样重新监听时fd再有新的数据又可以响应到了（发送端因为基于TCP协议所以需要收到应答后才会清除）。
```

**该模型的优点：**

```
相比其他模型，使用select() 的事件驱动模型只用单线程（进程）执行，占用资源少，不消耗太多 CPU，同时能够为多客户端提供服务。
如果试图建立一个简单的事件驱动的服务器程序，这个模型有一定的参考价值。
```

**该模型的缺点：**

```
首先select()接口并不是实现“事件驱动”的最好选择。因为当需要探测的句柄值较大时，select()接口本身需要消耗大量时间去轮询各个句柄。
很多操作系统提供了更为高效的接口，如linux提供了epoll，BSD提供了kqueue，Solaris提供了/dev/poll，…。
如果需要实现更高效的服务器程序，类似epoll这样的接口更被推荐。遗憾的是不同的操作系统特供的epoll接口有很大差异，所以使用类似于epoll的接口实现具有较好跨平台能力的服务器会比较困难。
其次，该模型将事件探测和事件响应夹杂在一起，一旦事件响应的执行体庞大，则对整个模型是灾难性的。
```

**selectors模块**：

除了Select可以实现IO多路复用，还有poll和epoll模块可以实现，它们的不同点是：

Select最多可以监听1024个连接，且管理多个描述符也是进行轮询，根据描述符的状态进行处理，但select在linux,windows,mac上都有

poll解决select的监听个数限制，但是依旧是轮询方式。

epoll解决了轮询问题，可以直接拿到就绪的套接字，但是Windows不支持。

好在我们有selectors模块，帮我们默认选择当前平台下最合适的。

示例：

服务端：

```python
from socket import *
import selectors

sel = selectors.DefaultSelector()  # 设置不同平台默认的selectoer
server_fileobj = socket(AF_INET, SOCK_STREAM)
server_fileobj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_fileobj.bind(('127.0.0.1', 8088))
server_fileobj.listen(5)


def accept(server_fileobj, mask):
    conn, addr = server_fileobj.accept()
    sel.register(conn, selectors.EVENT_READ, read)  # 将套接字放入监听列表，并绑定read函数


def read(conn, mask):
    try:
        data = conn.recv(1024)
        if not data:
            print('closing', conn)
            sel.unregister(conn)  # 将套接字从监听列表中移除，不再监听
            conn.close()
            return
        conn.send(data.upper() + b'_SB')
    except Exception:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


server_fileobj.setblocking(False)  # 设置socket的接口为非阻塞
# 相当于网select的读列表里append了一个文件句柄server_fileobj,并且绑定了一个回调函数accept
sel.register(server_fileobj, selectors.EVENT_READ, accept)

while True:
    events = sel.select()  # 检测所有的fileobj，是否有完成wait data的，开始监听
    for sel_obj, mask in events:
        callback = sel_obj.data  # 获得套接字绑定的函数，如果是server_fileobj，callback=accpet 
        # 执行绑定的函数，sel_obj.fileobj就是拿到的套接字，如果是server_fileobj，相当于accpet(server_fileobj，mask)
        callback(sel_obj.fileobj, mask)
```

客户端：

```python
from socket import *

c = socket(AF_INET, SOCK_STREAM)
c.connect(('127.0.0.1', 8088))

while True:
    msg = input('>>: ')
    if not msg: continue
    c.send(msg.encode('utf-8'))
    data = c.recv(1024)
    print(data.decode('utf-8'))
```



### 4.异步IO

asynchronous IO其实用得不多，从内核2.6版本才开始引入。先看一下它的流程：![异步IO](G:\homework\img\异步IO.png)

用户进程发起read操作之后，立刻就可以开始去做其它的事。而另一方面，从kernel的角度，当它受到一个asynchronous read之后，首先它会立刻返回，所以不会对用户进程产生任何block。然后，kernel会等待数据准备完成，然后将数据拷贝到用户内存，当这一切都完成之后，kernel会给用户进程发送一个signal，告诉它read操作完成了。

### 5.IO模型比较分析

四个IO Model的区别：

- blocking和non-blocking的区别
    - 前面的介绍中其实已经很明确的说明了这两者的区别。调用blocking IO会一直block住对应的进程直到操作完成，而non-blocking IO在kernel还准备数据的情况下会立刻返回。
- synchronous IO和asynchronous IO的区别
    - 同步I/O操作导致请求进程被阻塞，直到I/O操作完成；异步I/O操作不会阻塞请求进程。

按照这个定义，四个IO模型可以分为两大类（同步阻塞，异步不阻塞）：

定义：

```
A synchronous I/O operation causes the requesting process to be blocked until that I/O operationcompletes;  
An asynchronous I/O operation does not cause the requesting process to be blocked;
```

- blocking IO，non-blocking IO，IO multiplexing都属于synchronous IO这一类，阻塞
- asynchronous I/O后一类，不阻塞

```
有人可能会说，non-blocking IO并没有被block啊。这里有个非常“狡猾”的地方，定义中所指的”IO operation”是指真实的IO操作，
就是例子中的recvfrom这个system call。non-blocking IO在执行recvfrom这个system call的时候，如果kernel的数据没有准备好，
这时候不会block进程。但是，当kernel中数据准备好的时候，recvfrom会将数据从kernel拷贝到用户内存中，这个时候进程是被block了，
在这段时间内，进程是被block的。而asynchronous IO则不一样，当进程发起IO 操作之后，就直接返回再也不理睬了，直到kernel发送一个信号，
告诉进程说IO完成。在这整个过程中，进程完全没有被block。
```

### 6.socket_server模块

示例：

服务端实现并发：

```python
import socketserver


class MySocket(socketserver.BaseRequestHandler):
    def handle(self):
        """
        并发业务逻辑
        :return:
        """
        while True:
            client_data = self.request.recv(1024)
            if client_data.decode('utf-8') == 'exit':
                print('客户端断开连接，等待新的客户端连接')
                break
            print('接收数据>>:', client_data.decode('utf-8'))
            response = input('响应数据>>:').strip()
            self.request.sendall((response).encode('utf-8'))
        self.request.close()


# 封装了这三步：1.self.socket  2.self.socket.bind  3.self.socket.listen(5)
server = socketserver.ThreadingTCPServer(('127.0.0.1', 8081), MySocket)

server.serve_forever()
```

客户端：

```PYTHON
import socket
ip_port = ('127.0.0.1', 8081)
sock = socket.socket()
sock.connect(ip_port)
print('客户端启动：')


while True:
    inp = input('发送数据>>:')
    sock.sendall(inp.encode('utf-8'))
    if inp == 'exit':
        break
    server_response = sock.recv(1024)
    print('服务端响应数据>>:', server_response.decode('utf-8'))

sock.close()
```

