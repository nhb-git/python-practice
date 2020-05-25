#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/25/2020  6:39 PM 
# 文件名称   ：2020_05_25.py


def pig_it(text):
    #### way 1 ####
    # l = list()
    # for item in text.split():
    #     if item.isalpha():
    #         l.append(item[1:]+item[0]+'ay')
    #     else:
    #         l.append(item)
    # return ' '.join(l)
    #### way 2 ####
    return ' '.join(item[1:]+item[0]+'ay' if item.isalpha() else item for item in text.split())
