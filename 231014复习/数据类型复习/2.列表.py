#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/10/14

# user = ["张三", "李四", 89]
# # print(len(user))
# print(user[1])


# 录入用户名和密码
# users = []
# for i in range(0, 2):
#     name = input('username and password:').strip()
#     users.append(name)
# print(users)
#
# # 用户名和密码校验
#
# user = input('username:').strip()
# pwd = input('password:').strip()
# if user == users[0] and pwd == users[1]:
#     print("登录成功")
# else:
#     print("用户名或密码错误")

import copy

# # 练习1
# v1 = [1, 2, 3]
# v2 = copy.copy(v1)
# print(id(v1), id(v2))
# print(v1 == v2)  # true
# print(v1 is v2)  # false
# print(v1[0] is v2[0])  # true

# v1 = [1, 2, 3]
# v2 = copy.deepcopy(v1)
# print(id(v1), id(v2))
# print(v1 == v2)  # true
# print(v1 is v2)  # false
# print(v1[0] is v2[0])  # true

import copy


#
# v1 = (1, 2, 3, 4)
# v2 = copy.copy(v1)
# print(id(v1), id(v2))
#
# v3 = copy.deepcopy(v1)
# print(id(v1), id(v3))

# v1 = (1, 2, 3, [1, 2, 3], 4)
# v2 = copy.copy(v1)
# print(id(v1), id(v2))
# v3 = copy.deepcopy(v1)
# print(id(v1), id(v3))
# print(id(v1[3]), id(v3[3]))
# print(v2)
# print(v3)

# v1 = [1, 2, 3, [1, 2, 3], 4]
# v2 = copy.copy(v1)
# print(id(v1), id(v2))
# v3 = copy.deepcopy(v1)
# print(id(v1), id(v3))
# print(id(v1[3]), id(v3[3]))


# class Solution:
#     def twoSum(self, nums, target):
#         dict = {}
#         for i in range(len(nums)):
#             if target - nums[i] not in dict:
#                 dict[nums[i]] = i
#                 print(dict)
#             else:
#                 return [dict[target - nums[i]], i]
#         print(dict)
#
#
# ret = Solution()
# ret_new = ret.twoSum([2, 7, 11, 15, 19], 13)
# print(ret_new)
