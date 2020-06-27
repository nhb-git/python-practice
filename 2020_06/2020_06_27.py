#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/27/2020  12:07 PM 
# 文件名称   ：2020_06_27.py


"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""


# way 1
def removeDuplicates(nums):
    length = len(nums)
    first_index = length - 2

    while first_index >= 0:
        second_index = first_index + 1
        if nums[first_index] == nums[second_index]:
            del nums[second_index]
        first_index -= 1

    return len(nums)

# way 2
def removeDuplicates1(nums):
    for index in range(len(nums)-1, 0, -1):
        if nums[index] == nums[index-1]:
            nums.pop(index)
    return len(nums)


"""
两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""


"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""


def removeElement(nums, val):
    for index in range(len(nums)-1, -1, -1):
        if nums[index] == val:
            nums.pop(index)
    return len(nums)
