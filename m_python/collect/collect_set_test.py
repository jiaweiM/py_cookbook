import pytest


def test_ctr():
    myset = {1, 2, 3}
    print(myset)


def test_union():
    a = {1, 2, 3}
    b = {2, 3, 4}
    c = a.union(b)

    print(c)
    print(a)
    print(b)
