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
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
    # return ' '.join(str(string.ascii_lowercase.index(s.lower())+1) for s in text if s.lower() in string.ascii_lowercase)


def is_isogram(s):
    """
    An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
    is_isogram("Dermatoglyphics" ) == true
    is_isogram("aba" ) == false
    is_isogram("moOse" ) == false # -- ignore letter case
    :param s:
    :return:
    """
    return len(s) == len(set(s.lower()))


def validate_pin(pin):
    # way1
    # if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
    #     return True
    # else:
    #     return False

    # way2
    # return len(pin) in (4, 6) and pin.isdigit()

    # way3
    import re
    return bool(re.match(r'^(\d{4}|\d{6})$', pin))


def longest(s1, s2):
    """
    Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

    each taken only once - coming from s1 or s2.
    Examples:
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    longest(a, b) -> "abcdefklmopqwxy"

    a = "abcdefghijklmnopqrstuvwxyz"
    longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
    :param s1:
    :param s2:
    :return:
    """
    return ''.join(sorted(set(s1+s2)))
