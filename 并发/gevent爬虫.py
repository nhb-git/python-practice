#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gevent import monkey; monkey.patch_all()
import time
import gevent
import requests


def get_url(url):
    print('GET: %s' % url)
    response = requests.get(url)
    if response.status_code == 200:
        print('%d bytes received from %s' % (len(response.text), url))


start = time.time()
gevent.joinall([
    gevent.spawn(get_url, 'https://www.python.org/'),
    gevent.spawn(get_url, 'https://www.baidu.com/'),
    gevent.spawn(get_url, 'https://github.com/')
])
stop = time.time()
print('run time is %s', (stop-start))

print('--------------------------------')
s = time.time()
requests.get('https://www.python.org/')
requests.get('https://www.baidu.com/')
requests.get('https://github.com/')
t = time.time()
print('串行时间>>', (t-s))
