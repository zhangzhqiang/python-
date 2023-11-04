#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/4

import configparser

config = configparser.ConfigParser()
config.read("test.ini")

# 读取
# ret = config.sections()
# print(ret)

# 指定读取节点的key
# opt = config.options("group2")
# print(opt)

# 指定读取节点的key，values
# opt2 = config.items("group2")
# print(opt2)

# val = config.get('group1','k1')
# print(val)

# ret = config.remove_section("group1")
# print(ret)
# config.write(open("test.ini", "w"))

# ret = config.has_section("aaa")
# print(ret)

# ret1 = config.add_section("bbb")
# print(ret)
# config.write(open("test.ini", "w"))

# config.set("bbb", "k1", "v1")
# config.write(open("test.ini", "w"))

import logging

logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%Y/%m/%d %H:%M:%S %p")
logging.warning('is when this event was logged.')

# LOG = logging.getLogger("chat.gui")
# print(LOG)



