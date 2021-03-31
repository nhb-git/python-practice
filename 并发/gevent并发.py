#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gevent import monkey; monkey.patch_all()
import time
import gevent


def eat(name):
    print('%s eat 1' % name)
    # gevent.sleep(2)
    time.sleep(2)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    # gevent.sleep(2)
    time.sleep(2)
    print('%s play 2' % name)


start = time.time()
g1 = gevent.spawn(eat, 'niuhaibao')
g2 = gevent.spawn(play, name='niuhaibao')
g1.join()
g2.join()
print('主')
print(time.time()-start)
