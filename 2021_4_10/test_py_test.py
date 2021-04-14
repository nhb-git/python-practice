"""
测试模块的使用
"""
import pytest


def sum_numbers(x, y):
    """ ... """
    return x + y


def test_sum_numbers():
    assert sum_numbers(3, 4) == 7


if __name__ == '__main__':
    pytest.main(['-q', 'test_py_test.py'])
