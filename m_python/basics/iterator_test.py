import pytest


def test_it():
    a_list = [4, 6, 8, 9]
    a_it = iter(a_list)
    assert next(a_it) == 4
    assert next(a_it) == 6
    assert a_it.__next__() == 8
    assert a_it.__next__() == 9

    for a in a_it:
        print(a)

    with pytest.raises(StopIteration):
        next(a_it)


class PowTwo:
    """Class to implement on iterator of powers of two"""

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


def test_for():
    a = PowTwo(3)
    for val in a:
        print(val)
