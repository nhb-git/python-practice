from gevent import monkey; monkey.patch_all()
import time
import gevent
import requests


url = 'https://segmentfault.com/a/1190000006945621'
L = list()

def hello(i):
    L.append(requests.get(url).text)


start_time = time.time()
tasks = [gevent.spawn(hello, i) for i in range(50)]
gevent.joinall(tasks)
# for i in range(50):
#     hello(i)
end_time = time.time()
print(len(L))
# print(L)
print(end_time-start_time)
