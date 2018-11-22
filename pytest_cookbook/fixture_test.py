import pytest


@pytest.fixture
def empty_list():
    """Returns a list with length 0"""
    return []


@pytest.fixture
def long_list():
    return [1, 2, 3]


def test_empty_list(empty_list):
    assert len(empty_list) == 0


def test_long_list(long_list):
    assert len(long_list) == 3


@pytest.mark.parametrize("va1,va2,sumValue", [
    (1, 2, 3),
    (4, 5, 9)
])
def test_sum(va1, va2, sumValue):
    assert va1 + va2 == sumValue


@pytest.mark.skip(reason="no way of currenly testing this")
def test_unknown():
    pass


