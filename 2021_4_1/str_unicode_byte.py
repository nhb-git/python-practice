"""
str/unicode/byte 的特性.
"""
# unicode的作用是为每个字符提供唯一id，不区分语言
# unicode为每个字符提供的数字称为代码点, 十六进制的数字


# 编码，将任何字符串映射到位模式, 最常见的方式有ASCII、ISO-8859-1  、UTF-8
# 编码是将字符串或unicode字符序列转换为字节的过程
def get_all_users_age(total_users=1000):
    """..."""
    age = []
    for id in total_users:
        user_obj = access_db_to_get_users_by_id(id)
        age.append([user.name, user.age])
    return age
