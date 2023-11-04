#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/4

import re
# re1 = re.search("a*", "daaaaabc")
# print(re1)
#
# re2 = re.findall("ab{1,3}","abb abc abbcbbb abbbbbbbbb")
# print(re2)

text = "我的名字叫joker，我喜欢北京，记住我的名字joker"
data_list = re.findall("joker", text)
print(data_list)

