#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from greenlet import greenlet


def eat(name):
    print('%s eat 1' % name)
    g2.switch(name)
    print('%s eat 2' % name)
    g2.switch(name)


def play(name):
    print('%s play 1' % name)
    g1.switch(name)
    print('%s play 2' % name)


start = time.time()
g1 = greenlet(eat)
g2 = greenlet(play)

g1.switch('niuhaibao')

# 顺序执行的时间要比切换执行用的时间少了很多
print(time.time()-start)
start = time.time()
eat('niuhaibao')
play('niuhaibao')
print(time.time()-start)
