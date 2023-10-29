#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/10/21

# user_ip_dict = {}
# with open("access.log", "r", encoding="utf-8") as file_boj:
#     for line in file_boj:
#         user_ip = line.split(" - - ")[0]
#         if user_ip not in user_ip_dict:
#             user_ip_dict[user_ip] = 1
#         else:
#             user_ip_dict[user_ip] += 1
#     print(user_ip_dict)

# 2.ini 文件操作
import configparser

config = configparser.ConfigParser()
config.read("my.ini", encoding="utf-8")

# 1.获取所有节点
# ret = config.sections()
# print(ret)

# 2.获取节点下的值
ret = config.items("client")
print(ret)

# 3.获取节点下的键对应的值
# ret = config.get("mysqld_safe", "log-error")
# print(ret)

# 4.检查节点下是否有值
# ret = config.has_section("mysqld")
# print(ret)

# 5.添加节点
config.add_section("linux")
# print(config.sections())

# 6.删除节点
# config.read("my.ini", encoding="utf-8")
# config.remove_section("linux")
# ret = config.sections()
# print(ret)

# 7.删除节点中的值
config.remove_option("client", "default-character-set")
ret1 = config.items("client")
print(ret1)
