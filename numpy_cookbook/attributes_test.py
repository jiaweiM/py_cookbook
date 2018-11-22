import numpy as np
import numpy.testing as nt


def test_ndim():
    '''维度的数目'''
    array = np.array([[1, 2, 3], [2, 3, 4]])

    # 数组维度
    assert array.ndim == 2
    # 行数和列数
    assert array.shape == (2, 3)
    # 元素个数
    assert array.size == 6

    array = np.array([0, 1, 2, 3, 4])
    assert array.shape == (5,)
    assert array.dtype == np.int32


def test_shape():
    '''返回 tuple，为每个维度的大小'''
    a = np.array([0, 1, 2, 3])
    assert a.shape == (4,)

    a = np.array([[1, 2, 3], [4, 5, 6]])
    assert a.shape == (2, 3)


def test_reshape():
    '''通过修改 shape 属性，对数组 reshape'''
    a = np.array([[1, 2, 3], [4, 5, 6]])
    a.shape = (3, 2)
    nt.assert_array_equal(a, np.array([[1, 2], [3, 4], [5, 6]]))


def test_reshape_reshape():
    '''通过reshape 函数对数组 reshape'''
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = a.reshape(3, 2)
    nt.assert_array_equal(b, np.array([[1, 2], [3, 4], [5, 6]]))


def test_itemsize():
    '''数据类型大小'''
    x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
    assert x.itemsize == 1

    x = np.array([1, 2, 3, 4, 5], dtype=np.float32)
    assert x.itemsize == 4


def test_shape_op():
    a = np.arange(24).reshape(2, 3, 4)
    np.ravel(a)

    print(a)
