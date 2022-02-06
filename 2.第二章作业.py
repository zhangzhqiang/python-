#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2022-01-03

"""开发程序对stock_data.txt进行以下操作：
程序启动后，给用户提供查询接口，允许用户重复查股票行情信息(用到循环)
允许用户通过模糊查询股票名，比如输入“啤酒”, 就把所有股票名称中包含“啤酒”的信息打印出来
允许按股票价格、涨跌幅、换手率这几列来筛选信息，比如输入“价格>50”则把价格大于50的股票都打印，输入“市盈率<50“，则把市盈率小于50的股票都打印，不用判断等于。
思路提示：加载文件内容到内存，转成dict or list结构，然后对dict or list 进行查询等操作。 这样以后就不用每查一次就要打开一次文件了，效率会高。"""

f = open("stock_data.txt", "r", encoding="utf-8")
query_columns = ["最新价", "涨跌幅", "换手率"]
columns = f.readline().split()
stock_data = {}

for line in f:
    line = line.strip().split()
    name = line[2]
    stock_data[name] = line  # 创建股票数据dict{name：data...}

for i in columns:
    print(i.center(4, " "), end="|")
print()
while True:
    count = 0
    cmd = input("输入查询指令>>:").strip()
    if len(cmd) == 0:
        continue
    for s_name in stock_data:
        if cmd in s_name:
            print(stock_data[s_name])
            count += 1

    if ">" in cmd:
        q_name, q_val = cmd.split('>')
        q_name = q_name.strip()
        q_val = float(q_val)
        if q_name in query_columns:
            q_name_index = columns.index(q_name)
            for s_name, s_vals in stock_data.items():
                if float(s_vals[q_name_index].strip('%')) > q_val:
                    print(s_vals)
                    count += 1
    elif "<" in cmd:
        pass
    if count > 0:
        print("匹配到%s条" % count)
