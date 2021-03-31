#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gevent实现异步请求socket的客户端
"""
from gevent import monkey; monkey.patch_all()
from socket import *
import threading


def client(host, port):
    c = socket(AF_INET, SOCK_STREAM)
    c.connect((host, port))

    count = 0
    while count < 1000:
        c.send(('%s say hello %s' % (threading.current_thread().getName(), count)).encode('utf-8'))
        msg = c.recv(1024)
        print(msg)
        count += 1


if __name__ == '__main__':
    for i in range(700):
        t = threading.Thread(target=client, args=('127.0.0.1', 8080))
        t.start()
