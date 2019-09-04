import pytest
import os
import socket

"""
get From:
https://www.geeksforgeeks.org/10-essential-python-tips-tricks-programmers/
"""


def test_in_place_swap():
    x, y = 10, 20
    assert x == 10
    assert y == 20
    x, y, = y, x
    assert x == 20
    assert y == 10


def test_reverse_string():
    a = "GeeksForGeeks"
    b = a[::-1]
    assert b == 'skeeGroFskeeG'


def test_join_list():
    a = ["Geeks", "For", "Geeks"]
    b = " ".join(a)
    assert b == 'Geeks For Geeks'


def test_comparison_chaining():
    n = 10
    result = 1 < n < 20
    assert result
    result = 1 > n <= 9
    assert not result


def test_module_path():
    print(os)
    print(socket)


def test_most_frequent():
    '''find the most frequent value in a list'''
    test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
    assert max(set(test), key=test.count) == 4
