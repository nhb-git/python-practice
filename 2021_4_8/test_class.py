"""
类的最佳实践.
"""


class Employee:
    """ ... """
    POSITIONS = ('Superwiser', 'Manager', 'CEO')

    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department
        self.age = None

    def __str__(self):
        return 'Name' + self.name

    @classmethod
    def no_position_allowed(cls, position):
        """ ... """
        return [t for t in cls.POSITIONS if t != position]

    @staticmethod
    def c_positions(position):
        """静态方法.

        1. 一般与类有关系且没有使用实例属性时会设置为静态方法
        """
        return [t for t in cls.POSITIONS if t != position]

    @property
    def id_with_name(self):
        """ 属性.

        1. 需要确保必须具有返回值.
        """
        return self.id, self.name

    def age(self):
        """ 实例方法. """
        return self.age

    def _tt(self):
        """ 私有方法. """
        return self.name
