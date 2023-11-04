#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/4

import json

data = [
    {
        "id": 1,
        "name": "joker人",
        "age": 18
    },
    {
        "id": 1,
        "name": "iker",
        "age": 18
    },
]

print(type(data))

ret = json.dumps(data)
print(ret)  # [{"id": 1, "name": "joker\u4eba", "age": 18}, {"id": 1, "name": "iker", "age": 18}]
print(type(ret))  # <class 'str'>

ret = json.dumps(data, ensure_ascii=False)
print(ret)  # '[{"id": 1, "name": "joker", "age": 18}, {"id": 1, "name": "iker", "age": 18}]

