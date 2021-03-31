#!/usr/bin/env python3
"""
python 变量命名
1. 小写
2. _ 下划线分隔
"""
# 1.
names = 'Python'
job_title = 'software engineer'

# 2. 当希望类中的变量不被外部访问时，应以单下划线开头访问


class Test:
    _book = {}

    def _get_data():
        pass

    # 名称改写
    def __path():
        pass
#
# t = Test()
# print(dir(t))

# 3. 定义一个传入用户id返回用户对象的函数
# 3.1 传递的id很明确，用户的id，而非其他的id
# 3.2 希望获得的输出是个用户对象

def get_user_by(user_id):
    pass


# 4. 使用全部的大写字母定义常量
AGE = 31
NAME = 'niuhai'

# 5. 表达式和语句
users = [{'first_name': 'niu', 'age': 30},
         {'fist_name': 'haib', 'age': 40}
         ]

users = sorted(users, key=lambda user: user['first_name'].lower())


# 以上这段代码无法解决字典是否合法和键值丢失的问题
def get_user_name(users):
    return users['first_name'].lower()


# 函数的功能应该尽量单一，明确化
def get_sorted_dic(users):
    if not isinstance(users, dict):
        raise ValueError('...')
    if not len(users):
        raise ValueError('...')

    users_by_name = sorted(users, key=get_user_name)
    return users_by_name


# 偏向于使用join连接字符串，性能更优
','.join(['a', 'b'])


# None
# val is Bool
if val:
    pass
if val is None:
    pass

if val is not None:
    pass

# 确保函数中任何退出的地方都有返回值
def cal_interest(principle, time, rate):
    if principle < 0:
        return None
    else:
        return (principle * time * rate) / 100

# 对字符串做前缀和后缀检查时应该使用startswith和endswith
data = 'hello, how are you doing?'
if data.startswith('hello'):
    pass

# 使用with时建议使用函数来操作除获取和释放资源以外的操作

#connection
class NewProtocol:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __enter__(self):
        self._client = socket()
        self._client.connect((self.host, self.port))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.close()

# 文档字符串，函数、类、模块
# 列表推导，当大于1个循环和多个条件判断时应考虑不使用列表推导
# 1. 性能好 2. 可读性高  3. 书写简单

# lambda表达式不推荐进行赋值应有def函数代替
def read_file(file_name):
    """Read the file line by line."""
    with open(file_name) as fread:
        for line in fread:
            yield line


# 异常，假设这段代码中有错误发生时添加异常
def division(dividend, divisor):
    """Perform arithmetic division."""
    try:
        return dividend / divisor
    except ZeroDivisionError as zero:
        raise ZeroDivisionError("Please ... 0")


# finally, 比较适合回收资源

# 自定义异常类
class ReplyError(Exception):
    """..."""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)

    def __repr__(self):
        return 'ReplyError(' + str(self.msg) + ')'
