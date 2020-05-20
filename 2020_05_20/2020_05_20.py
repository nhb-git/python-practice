#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/20/2020  06:01 PM 
# 文件名称   ：2020_05_20.py


def rgb(r, g, b):
    """
    The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

    Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here
    :param r:
    :param g:
    :param b:
    :return:
    """
    ####### way1 #####
    # def rgb(r, g, b):
    #     rgb_list = [r, g, b]
    #     for index, num in enumerate(rgb_list):
    #         if num > 255:
    #             num = 255
    #             rgb_list[index] = hex(num)[2:]
    #         elif num < 0:
    #             num = 0
    #             rgb_list[index] = '0' + hex(num)[2:]
    #         else:
    #             num = round(num)
    #             if len(hex(num)[2:]) < 2:
    #                 rgb_list[index] = '0' + hex(num)[2:]
    #             else:
    #                 rgb_list[index] = hex(num)[2:]
    #     return ''.join(item.upper() for item in rgb_list)

    ##### way2 ####
    # limit = lambda x: max(0, min(255, x))
    # return ('{:02X}' * 3).format(limit(r), limit(g), limit(b))

    ##### way3 ####
    def limit(num):
        if num < 0:
            return 0
        elif num > 255:
            return 255
        else:
            return round(num)
    return ('{:02X}'*3).format(limit(r), limit(g), limit(b))


def solution(args):
    """
    A format for expressing an ordered list of integers is to use a comma separated list of either

    individual integers
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
    Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
    :param args:
    :return:
    """
    # l = list()
    # l1 = list()
    # for num in args:
    #     if not l1:
    #         l1.append(num)
    #     else:
    #         if (num - 1) == l1[-1]:
    #             l1.append(num)
    #         else:
    #             if len(l1) > 2:
    #                 l.append(str(l1[0]) + '-' + str(l1[-1]))
    #                 l1 = list()
    #                 l1.append(num)
    #             else:
    #                 l.extend(str(num1) for num1 in l1)
    #                 l1 = list()
    #                 l1.append(num)
    # else:
    #     if len(l1) > 2:
    #         l.append(str(l1[0]) + '-' + str(l1[-1]))
    #     else:
    #         l.extend(str(num1) for num1 in l1)
    #
    # return ','.join(l)
    ########## way2 ##########
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)


print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
