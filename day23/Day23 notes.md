# Day23 notes

## 今日内容

- 网络编程

### 网络编程

计算机基础知识：

我们开发的软件都是应用软件，应用软件必须应用于操作系统上，操作系统必须运行硬件上，应用软件是无法直接应用到硬件上的，应用软件对硬件的操作必须调用操作系统的接口，由操作系统操控硬件。

#### 1、网络应用开发架构：

- C/S架构
    - C指的是client（客户端）
    - S值得是server（服务端）
- B/S架构
    - B指的是browser（浏览器）
    - S值得是server（服务端）

比如一个登陆功能的流程：

- 用户输入账号和密码后，存放于客户端内存地址中，然后调用接口将数据发送给操作系统
- 客户端操作系统收到数据后，按照客户端软件指定的协议，调用网卡发送数据
- 网络传输数据
- 服务端软件调用系统接口，将数据从客户端操作系统的内存拷贝到自己的内存
- 服务端操作系统收到指令后，使用与客户端相同的协议，从网卡接收数据，然后拷贝给服务端软件

#### 2、TCP/IP的基础知识：

Transmission Control Protocol/Internet Protocol的简写，中译名为传输控制协议/因特网互联协议，又名网络通讯协议，是Internet最基本的协议、Internet国际互联网络的基础。

TCP/IP五层协议：

- 物理层

    - 主要是基于电器特性发送高低电压(电信号)，高电压对应数字1，低电压对应数字0

- 数据链路层

    - 协议：两台物理设备之间对于要发送的内容，长度和顺序做的一些规范
    - mac地址：每一块网卡上都有一个全球唯一的mac地址
    - 交换机：是连接多台机器并帮助通讯的物理设备，只可以识别mac地址

- 网络层

    - ip地址：

        - ipv4协议，位的点分十进制，32位的2进制表示，范围：0.0.0.0 ~ 255.255.255.255

        - ipv6协议，8位的冒分十六制，128位十进制来表示 (点分十进制不足以表示)，范围：0:0:0:0:0:0:0:0 ~ FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF

        - ip使用：

            - 如果一个ip地址想被所有人都看到，这个ip地址是必须要申请的，即公网IP

            - 提供内网ip，供局域网使用：

                192.168.0.0 - 192.168.255.255

                172.16.0.0 - 172.31.255.255

                10.0.0.0 - 10.255.255.255

        - 网关ip:一个局域网的网络出口，访问局域网以外的区域都需要经过路由器的网关

        - 网段： 一般是一个末尾为0的地址段

        - 子网掩码： 判断两个机器是否在同一个网段，子网掩码不能单独存在，它必须结合IP地址一起使用

    - 交换机实现的arp协议：

        - 通过ip地址和子网掩码获取一台机器的mac地址
        - 交换机工作原理：收到一个请求，通知所有连接他的ip地址，获取对应ip地址的mac地址并返回给请求的ip地址

    - ip地址可以确认一台机器，port端口可以确认一台机器的一个应用，一般有65535个端口

    - 一般实现互联，使用127.0.0.1 是自己的地址，不过交换机 ip地址是可以过交换机的

- 传输层：https://www.cnblogs.com/cnike/p/10726069.html

    - 传输层功能：建立端口到端口的通信
    - TCP协议：
        - 面向连接的，可靠，但是慢，可以实现全双工通信，即双方都是实时的，区别于半双工（传呼机）
        - 无边界，流式传输
        - 具体的连接方式，在建立连接的时候，需经过三次握手，即请求方向服务器发送链接请求是第一次，服务器同意并向请求方发送链接请求是第二次，请求方通过是第三次，即三次握手。
        - 具体的断开连接方式，需要经过四次挥手，即请求方向服务器发送断开请求是第一次，服务器同意是第二次，服务器向请求方发送断开请求是第三次，请求方通过是第四次。
        - 在建立连接的时候，tcp协议发送的每一条信息都会有回执，而且为了保证数据的完整性，还会有重传机制，即发送不过去的，会自动再次发送
        - 长连接：会一直占用双方的端口
        - 能够传输的数据长度几乎没有限制
        - IO操作 I: input O:output 输入输出都是相对内存来说
            - write send 输出 output
            - read recv 输入 input
    - UDP协议：
        - 面向数据报的，无连接，速度很快，类似于发短信，能实现一对一，多对一，一对多的高效通讯
        - 由于没有回执，对于发送信息和接受信息的双方来说，可能存在丢失消息的情况
        - 能够传递的长度有限，是根据数据传递设备的位置有关系

- 应用层

    - 我们开发的软件都在应用层

#### 3、Socket（套接字）

- Socket是应用层与传输层的中间软件抽象层，**它是一组接口**，可以帮我们完成所有信息的组织和拼接

- 通过socket建立起2台机器的连接后，本质上socket只干2件事，一是收数据，一是发数据，没数据时就等着。

- 通过python的socket模块完成socket的功能

示例：

服务端：

```python
import socket

# 基于网络通信,基于TCP协议
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定之前加,内存中有,重复使用端口
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定服务器地址
phone.bind(('127.0.0.1', 8083))

# 开始监听
phone.listen(5)
while True:
    # 等待接收数据
    conn, client_addr = phone.accept()

    while True:
        try:
            # 接收数据
            data = conn.recv(1024)
            # 打印接收到的数据
            print('Client recv:', data)
            # 服务端收不到数据,就直接break
            if not data:  
                break
            # 回复消息
            response = input('>>>:').strip()
            conn.send(response.encode())
            # 打印回复消息
            print('Server send:', response)
        except ConnectionResetError:
            print('客户端强制关闭')
            break

    conn.close()

phone.close()
```

客户端：

```python
import socket

# 基于网络通信,基于TCP协议
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器地址
phone.connect(('127.0.0.1', 8083))

while True:
    # 给服务端发送消息
    msg = input('>>>:').strip()
    if not msg: continue
    phone.send(msg.encode('utf-8'))
    # 接收服务端消息
    data = phone.recv(1024)
    # 打印服务端消息
    print(data)

phone.close()
```

#### 4、粘包现象

示例：

服务端：

```python
import socket
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 8083))  # 0-65535:0-1024个操作系统使用,1024以后随便用

phone.listen(5)

print('staring...')
while True:
    conn, client_addr = phone.accept()  # 接收链接对象
    print(client_addr)

    # 5.收 发消息
    while True:  # 通信循环
        try:
            # 1.收命令
            cmd = conn.recv(1024)  # 1.单位:bytes 2.1024代表最大接受1024个bytes
            # if not data:break  # 适用于linux操作系统  如果没有接收,break 客户端强制关闭
            print('客户端的数据', cmd)

            # 2.执行命令,拿到结果
            obj = subprocess.Popen(cmd.decode('gbk'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            # 正确的命令
            stdout = obj.stdout.read()
            # 错误的命令
            stderr = obj.stderr.read()

            # 3.把命令的结果返回个客户端
            print(len(stdout)+len(stderr))
            conn.send(stdout+stderr)

        except ConnectionResetError:  # 适用于windows系统
            print('客户端强制关闭')
            break

    conn.close()

phone.close()
```

客户端：

```python
import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8083))

# 3.发 收消息
while True:
    # 1.发命令
    cmd = input('>>>:').strip()  # msg = ''  输入空
    if not cmd:continue  # 不能输入空
    phone.send(cmd.encode('gbk'))  # phont.send(b'')

    # 2.拿到命令的结果,并打印
    data = phone.recv(1024)  # 1024是一个坑
    print(data.decode('gbk'))

# 4.关闭
phone.close()
```

操作：

- 启动服务端和客户端
- 命令行输入dir，然后再输入tasklist，最后输入dir看结果
- 此时产生粘包现象

粘包的产生分析：

- 发送的数据小于TCP发送缓冲区的空间，TCP将多次写入缓冲区的数据一起发出去，产生粘包

    服务端：

    ```python
    import socket
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9903))
    server.listen(5)
    
    conn, addr = server.accept()
    
    
    res1 = conn.recv(1024)
    print('第一次', res1)
    
    res2 = conn.recv(10)
    print('第二次', res2)
    ```

    客户端：

    ```python
    import socket
    import time
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9903))
    
    client.send('hello'.encode('utf-8'))
    client.send('world'.encode('utf-8'))
    ```

- 接收数据没收干净，导致数据滞留在接收管道中，产生粘包

    服务端：

    ```python
    import socket
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9903))
    server.listen(5)
    
    conn, addr = server.accept()
    
    
    res1 = conn.recv(3)
    print('第一次', res1)
    
    res2 = conn.recv(10)
    print('第二次', res2)
    ```

    客户端：

    ```python
    import socket
    import time
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9903))
    
    client.send('hello'.encode('utf-8'))
    client.send('world'.encode('utf-8'))
    ```

补充问题：

- 为何说tcp是可靠传输，udp是不可靠传输

    - tcp在数据传输时，发送端先把数据发送到自己的缓存中，然后协议控制将缓存中的数据发往另一端，另一端返回一个ack=1，发送端则清理缓存中的数据，对端返回ack=0，则重新发送数据，所以tcp是可靠的

    - 而udp发送数据，对端是不会返回确认信息的，因此不可靠

- send与recv对比

    - recv：服务端等待数据到服务器的操作系统缓存区，耗时长，由服务器操作系统缓存器拷贝到服务端程序
    - send：客户端程序把数据拷贝到操作系统缓存区

#### 5、解决粘包问题

示例：方式一

服务端

```python
import socket
import struct
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 8088))

phone.listen(5)

print('staring...')
while True:
    conn, client_addr = phone.accept()  # 接收链接对象
    print(client_addr)

    while True:
        try:
            cmd = conn.recv(1024)
            print('客户端的数据', cmd)

            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            # 第一步:把报头(固定长度)发给客户端
            total_size = len(stdout)+len(stderr)
            header = struct.pack('i', total_size)

            # 第二步:发报头发个客户端
            conn.send(header)

            # 第三步:再发送真实的数据
            conn.send(stdout+stderr)

        except ConnectionResetError:
            print('客户端强制关闭')
            break

    conn.close()

phone.close()
```

客户端：

```python
import socket
import struct  

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8088))

while True:
    cmd = input('>>>:').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))

    # 第一步:先收报头
    header = phone.recv(4)

    # 第二步:从报头中解析出对帧数数据的描述信息(数据的长度)
    total_size = struct.unpack('i', header)[0]

    # 第三步:接收真实的数据
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:
        res = phone.recv(1024)
        recv_data += res
        recv_size += len(res)
        print(recv_data.decode('utf-8'))

phone.close()
```

方式二：

服务端：

```python
import json
import socket
import struct  # 该模块可以把一个类型，如数字，转成固定长度的bytes
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 8083))

phone.listen(5)

print('staring...')
while True:
    conn, client_addr = phone.accept()  # 接收链接对象
    print(client_addr)

    while True:
        try:
            cmd = conn.recv(1024)  # 接收命令
            print('客户端的数据', cmd)

            obj = subprocess.Popen(cmd.decode('utf-8'),  # 该系统命令必须是字符串格式，所以必须进行解码
            					   shell=True,
                                   stdout=subprocess.PIPE,  # 正确命令输出结果
                                   stderr=subprocess.PIPE)  # 错误命令输出结果
            stdout = obj.stdout.read()  # 从管道中读取正确的结果
            stderr = obj.stderr.read()  # 从管道中读取错误的结果
            # 第一步:制作报头，把报头(固定长度)发给客户端  # 模拟文件的上传和下载，则报头中应该包括文件名，文件的大小，文件的md5值....
            header_dic = {
                'filename': 'a.txt',
                'md5': 'xxx',
                'total_size': len(stdout)+len(stderr)  # 真实数据的总大小
            }
            header_json = json.dumps(header_dic)  # 将报头这种数据类型即字典转换成json格式(是一种json格式的字符串)，可以基于网络传输
            header_bytes = header_json.encode('utf-8')  # 将json格式的字符串转换成bytes,基于网络进行传输给客户端

            # 第二步:先发送报头的长度
            conn.send(struct.pack('i', len(header_bytes)))  # 通过struct模块将报头的长度转换成固定长度的bytes大小（i格式是4个字节大小），并将固定报头长度 发送给客户端

            # 第三步:再发送报头
            conn.send(header_bytes)  # 将报头的内容发送给客户端

            # 第四步:再发送真实的数据
            conn.send(stdout+stderr)  # 将正确和错误的真实数据发送给客户端

        except ConnectionResetError:
            print('客户端强制关闭')
            break

    conn.close()

phone.close()
```

客户端：

```python
import json
import socket
import struct

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8083))

while True:
    cmd = input('>>>:').strip()
    if not cmd:continue  # 输入的命令不能为空
    phone.send(cmd.encode('utf-8'))  # 将字符串形式的命令转换成bytes类型，发送给服务端

    # 第一步:先收报头长度
    header_size = struct.unpack('i', phone.recv(4))[0]  # 将服务端打包过来报头的长度进行解包(是一个元组，第一个值是报头的大小)，解析出报头的长度

    # 第二步:再收报头
    header_bytes = phone.recv(header_size)  # 已接收报头的长度，可以通过报头的长度来接收bytes类型的报头

    # 第三步:从报头中解析出对帧数数据的描述信息
    header_json = header_bytes.decode('utf-8')  # 将bytes类型的报头的解码成json格式的字符串
    header_dic = json.loads(header_json)  # 将json格式的字符串反序列化成字典，也就是拿到了字典形式的报头
    print(header_dic)
    total_size = header_dic['total_size']  # 拿到字典形式的报头，就可以通过key值，取到服务端发送真实数据的总大小

    # 第四步:接收真实的数据
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:  # 循环接收真实数据
        res = phone.recv(1024)  # 每次接收数据的大小1024个字节
        recv_data += res  # 每次接收的真实数据拼接到空字符串中
        recv_size += len(res)  # 每循环一次接收的大小加每次接收真实数据的大小的长度
        print(recv_data.decode('utf-8'))  # 接收完真实数据将其解码打印

phone.close()
```

步骤解析：

服务端：

1. 把报头做成字典，包含将要发送的详细信息

2. 把字典通过序列化转换成一个json字符串

3. 把json字符串编码成bytes类型

4. 通过struct模块打包bytes类型的报头长度发送给客户端

5. 再发送bytes类型的报头

6. 再发送真实数据

客户端：

1. 收报头的长度，通过struck解包报头
2. 再收报头
3. 把收到的报头解码
4. 通过反序列化转成字典格式
5. 从字典中的key取出数据
6. 循环接收数据

#### 6、UDP协议不会粘包

示例：

服务端：

```python
from socket import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('127.0.0.1', 8089))

res1 = server.recvfrom(1)
print('第一次', res1)

res2 = server.recvfrom(1024)
print('第二次', res2)

server.close()
```

客户端：

```python
from socket import *

client = socket(AF_INET, SOCK_DGRAM)


client.sendto(b'hello', ('127.0.0.1', 8089))
client.sendto(b'world', ('127.0.0.1', 8089))

client.close()

```

练习：

服务端：

```python
from socket import *

server = socket(AF_INET, SOCK_DGRAM)  # UDP协议
server.bind(('127.0.0.1', 8088))

while True:
    data, client = server.recvfrom(1024)
    print(data)

    server.sendto(data.upper(), client)

server.close()
```

客户端：

```python
from socket import *

client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('>>:').strip()
    client.sendto(msg.encode('gbk'), ('127.0.0.1', 8088))

    data, server_addr = client.recvfrom(1024)
    print(data, server_addr)

client.close()
```

