#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time


def consumer():
    """接收数据做处理"""
    while True:
        x = yield
        print('处理了数据: ', x)


def producer():
    """生产数据"""
    g = consumer()
    next(g)
    for i in range(3):
        print('发送了数据: ', i)
        g.send(i)


if __name__ == '__main__':
    producer()
