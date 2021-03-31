#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gevent import joinall, monkey, spawn; monkey.patch_all()
import time


def task(pid):
    time.sleep(0.5)
    print('Task %s done' % pid)


def syncronout():
    for i in range(10):
        task(i)


def asyncronout():
    g_l = [spawn(task, i) for i in range(10)]
    joinall(g_l)


if __name__ == '__main__':
    start = time.time()
    print('Sync')
    syncronout()
    print(time.time()-start)

    start = time.time()
    print('async')
    asyncronout()
    print(time.time()-start)
