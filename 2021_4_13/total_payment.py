"""
迭代器.
"""
import itertools


def get_total_payment():
    payments = Payment.objects.all()
    sum_amount = 0
    if payments.exists():
        for payment in payments.iterator():
            sum_amount += payment
    return sum_amount


# from itertools import combinations
# print(list(combinations(['12', '345', '67', '8910'], 2)))
class MultiplyByTwo:
    def __init__(self, num):
        self.num = num
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        return self.num * self.counter


# for num in MultiplyByTwo(500):
#     print(num)


# for num in itertools.count(1, 4):
#     print(num)
#     if num > 24:
#         break

# for num in range(1, 24, 4):
#     print(num)

# numbers = '114455566667'
# result = list()
# for num, length in itertools.groupby(numbers):
#     print(length)
#     result.append((len(list(length)), int(num)))
#
# print(*result)
# print(*[1, 2, 3], sep=',')


# data = range(1000)
# def using_yield():
#     def wrapper():
#         for d in data:
#             yield d
#     return list(wrapper())
#
# def using_list():
#     result = list()
#     for d in data:
#         result.append(d)
#     return result
# import time
# start_time = time.time()
# using_yield()
# print(time.time()-start_time)
# start_time = time.time()
# using_list()
# print(time.time()-start_time)
def flat_list(iter_values):
    """ ... """
    for item in iter_values:
        if hasattr(item, '__iter__'):
            yield from flat_list(item)
        else:
            yield item


print(list(flat_list([1, [2], [3, [4]]])))
print(list(zip([1, 2], [3, 4])))
