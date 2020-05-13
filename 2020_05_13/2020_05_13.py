#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/13/2020  10:13 PM 
# 文件名称   ：2020_05_13.PY
import string


def alphabet_position(text):
    """
    Welcome.

    In this kata you are required to, given a string, replace every letter with its position in the alphabet.

    If anything in the text isn't a letter, ignore it and don't return it.

    "a" = 1, "b" = 2, etc.

    Example
    alphabet_position("The sunset sets at twelve o' clock.")
    Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

    :param text:
    :return:
    """
    return ' '.join([str(string.ascii_lowercase.index(s.lower())+1) for s in text if s.lower() in string.ascii_lowercase])
