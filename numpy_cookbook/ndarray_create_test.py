import numpy as np


def test_empty():
    a = np.empty([3, 2], dtype=np.int32)  # array with shape=(3, 2), values of the array are random
    assert a.shape == (3, 2)
    assert a.dtype == np.int32

    a = np.empty([3, 3])
    assert a.dtype == np.float64


def test_zeros():
    x = np.zeros(5)
    print(x)


def test_ones():
    a = np.ones(5)
    print(a)

def test_d1():
    a = np.array([2, 3, 4])
    assert a.shape == (3,)


def test_d2():
    '''多维数组'''
    a = np.array([[1, 2], [3, 4]])
    assert a.shape == (2, 2)


def test_d2_empty():
    '''指定最小的维度'''
    a = np.array([1, 2, 3, 4, 5], ndmin=2)
    assert a.shape == (1, 5)


def test_complex():
    '''复数数组'''
    a = np.array([1, 2, 3], dtype=complex)
    assert a[0] == 1. + 0.j
