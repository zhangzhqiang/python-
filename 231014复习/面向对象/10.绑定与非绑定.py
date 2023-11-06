#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/7

class MySQL:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # @staticmethod
    # def from_conf():
    #     return MySQL('192.168.1.203', 9090)

    @classmethod  # 哪个类来调用,就将哪个类当做第一个参数传入
    def from_conf(cls):
        return cls('192.168.1.203', 9090)

    def __str__(self):
        return '就不告诉你'


class Mariadb(MySQL):
    def __str__(self):
        return '<%s:%s>' % (self.host, self.port)


m = Mariadb.from_conf()
print(m)  # classmethod：<192.168.1.203:9090>	staticmethod：就不告诉你
