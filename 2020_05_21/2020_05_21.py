#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/21/2020  1:17 PM 
# 文件名称   ：2020_05_21.py


def dict_str(string):
    d = dict()
    for s in string.lower():
        if d.get(s):
            d[s] += 1
        else:
            d[s] = 1
    return d


def first_non_repeating_letter(string):
    """
    Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

    For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

    As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

    If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
    """
    #### way1 ####
    # d = dict_str(string)
    # for s in string:
    #     if d.get(s.lower()) == 1:
    #         return s
    # else:
    #     return ''
    #### way2 ####
    string_lower = string.lower()
    for index, s in enumerate(string):
        if string_lower.count(s.lower()) == 1:
            return string[index]
    else:
        return ''


class radd(int):
    def __call__(self,n):
        return radd(self+n)

