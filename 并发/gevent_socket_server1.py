#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gevent异步实现socket服务端
"""
# 猴子补丁必须要在导入socket模块前执行才能实现异步
from gevent import monkey; monkey.patch_all()
from socket import *
import gevent


def talk(conn, addr):
    """服务端的聊天主任务"""
    try:
        while True:
            res = conn.recv(1024)
            print('client {}:{} msg:{}'.format(addr[0], addr[1], res))
            conn.send(res.upper())
    except Exception as e:
        print(e)
    finally:
        conn.close()


def server(host, port):
    s = socket(AF_INET, SOCK_STREAM)
    # 操作系统会在进程或socket关闭后立刻释放端口
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        gevent.spawn(talk, conn, addr)


if __name__ == '__main__':
    server('127.0.0.1', 8080)
