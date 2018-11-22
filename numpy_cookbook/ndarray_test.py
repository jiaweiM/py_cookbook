# -*- coding: utf-8 -*-

import numpy as np
import sys
import time

__author__ = 'JiaweiMao'
__version__ = '1.0.0'


def test_ndarray_attributes():
    '''nparray 属性：
ndarray.ndim	数组的维数，即 rank 值
ndarray.shape	数组的大小，包含各个维度的尺寸的 tuple。如n行m列的矩阵，shape值为 (n, m)
ndarray.size	数组包含的总的元素数目
ndarray.dtype	数组包含元素的数据类型，NumPy 额外提供了 numpy.int32, int16 和 float64类型
ndarray.itemsize	数组包含元素的数据类型的字节大小。如 float64 对应8字节，complex32对应4字节
ndarray.data	包含实际的数组元素。一般不使用该属性，而使用索引方法。
    '''
    a = np.arange(15).reshape(3, 5)
    assert a.shape == (3, 5)
    assert a.dtype == 'int32'
    assert a.itemsize == 4
    assert a.size == 15


def test_create_list():
    '''通过list 创建 ndarray'''
    a = np.array([2, 3, 4])
    assert a.size == 3

    b = np.array([1.2, 3.5, 5.1])
    assert b.size == 3
    assert b.dtype == 'float64'


def test_create_doublearray():
    '''创建二维数组'''
    b = np.array([(1.5, 2, 3), (4, 5, 6)])
    assert b.dtype == 'float64'
    assert b.size == 6
    assert b.shape == (2, 3)


def test_createWithType():
    b = np.array([[1, 2], [3, 4]], dtype=complex)
    print(b)


def test_zeros():
    '''创建0数组'''
    a = np.zeros((3, 4))
    print(a)


def test_ones():
    a = np.ones((3))
    assert a[0] == 1


def test_minus():
    '''数组减法-各个元素分别相减'''
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    c = a - b
    print(c)


def test_size():
    '''从这儿可以看到，python 数组比 ndarray 尺寸要大很多'''
    l = range(1000)
    print(sys.getsizeof(5) * len(l))

    array = np.arange(1000)
    print(array.size * array.itemsize)


def test_speed():
    '''python list 比 numpy array 要慢许多'''
    SIZE = 100000
    l1 = range(SIZE)
    l2 = range(SIZE)

    a1 = np.arange(SIZE)
    a2 = np.arange(SIZE)

    start = time.time()
    result = [(x + y) for x, y in zip(l1, l2)]
    print("\npython list took:", (time.time() - start) * 1000)
    start = time.time()
    result = a1 + a2
    print("numpy array took", (time.time() - start) * 1000)
