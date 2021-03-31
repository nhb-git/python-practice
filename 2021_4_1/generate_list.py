"""
生成器和列表，优先考虑使用生成器，节省内存
生成器能提高代码可读性?
"""
def get_all_users_age(total_users=1000):
    """..."""
    age = []
    for id in total_users:
        user_obj = access_db_to_get_users_by_id(id)
        age.append([user.name, user.age])
    return age


def get_all_users_age1():
    """..."""
    all_users = 10000000
    for id in all_users:
        user_obj = access_db_to_get_users_by_id(id)
        yield user.name, user.age
