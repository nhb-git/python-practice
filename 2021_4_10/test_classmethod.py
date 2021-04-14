"""
类方法的使用.
"""


class User:
    """ ... """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def using_string(cls, name_str):
        """ ... """
        first, second = map(str, name_str.split(' '))
        student = cls(first, second)
        return student


data = User.using_string('Larry Page')
print(data.last_name)
