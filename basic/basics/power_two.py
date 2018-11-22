# -*- coding: utf-8 -*-

class PowTwo:
    '''Class to implement an iterator of powers of two'''

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


def test_custom_it():
    a = PowTwo(4)
    i = iter(a)
    assert 1 == next(i)
    assert 2 == next(i)
    assert 4 == next(i)
    assert 8 == next(i)
    assert 16 == next(i)
