#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2023/11/11

"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

"""


# 解题思路
"""
两重遍历，第一重遍历所有元素（对应数值为nums(i)），第二重遍历列表中i之后的所有元素（对应数值为nums(i+j+1)），
并在此进行判断，若nums(i)+nums(j+i+1)等于目标值target，则返回[i, j+i+1]作为结果，
并继续进行遍历，以确保输出所有的答案。
"""



nums = [3,2,4]
target = 6
class SumTo:
    def to_sum(self):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

ret = SumTo()
ret1 = ret.to_sum()
print(ret1)