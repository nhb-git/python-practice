"""
集合特性测试.
"""
# 1. 散列实现的集合，需要经常访问的性能特别好
# 2. 集合可以实现去重
data = {'first', 'second', 'third', 'fourth', 'fifth'}
if 'fourth' in data:
    print('Found the data.')
