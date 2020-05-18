#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/18/2020  08:23 PM 
# 文件名称   ：2020_05_18.py


def comp(array1, array2):
    """
    Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

    Examples
    Valid arrays
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    :param array1:
    :param array2:
    :return:
    """
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda weight: (sum(int(c) for c in weight), weight)))

