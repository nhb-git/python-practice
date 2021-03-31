"""
使用namedtuple特性.
"""
from collections import namedtuple


# 使用前提是不想改变里面的值
# Point = namedtuple('Point', ['x', 'y', 'z'])
# point = Point(x=3, y=4, z=5)
# print(point.x)
# point.y
# point.z

# 通常以元组返回数据，可以考虑用namedtuple，使代码更具有可读性
def get_user_info(user_obj):
    user = get_data_from_db(user_obj)
    Userinfo = namedtuple('Userinfo', ['first_name', 'last_name', 'age'])
    user_info = Userinfo(first_name=user['first_name'],
                         last_name=user['last_name'],
                         age=user['age'])
    return user_info
