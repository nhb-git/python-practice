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
