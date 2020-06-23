#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/23/2020  8:12 AM 
# 文件名称   ：2020_06_23.py


"""
2020_06_23 1
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 测试例子
s = Solution()
print(s.two_sum([3, 3], 6))
"""


# 2020_06_23 1
class Solution:
    def two_sum(self, nums_list, target):
        m = dict()
        for index, num in enumerate(nums_list):
            other_num = target - num
            other_index = m.get(other_num, None)
            if isinstance(other_index, int):
                return [other_index, index]
            else:
                m[num] = index


"""
2020_06_23 2
两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""