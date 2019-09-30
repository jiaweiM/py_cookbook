import numpy as np
import numpy.testing as nt


def test_arange():
    """
    arange([start,] stop[, step,], dtype=None)
    [start,stop)之间按照step 生成数组，类似于 python的 range 函数.
    如果 step 为小数，则推荐使用 linspace 函数.
    """
    a = np.arange(0, 3)
    b = np.array([0, 1, 2])
    nt.assert_array_equal(a, b)


def test_arange2():
    a = np.arange(4, 10)
    nt.assert_array_equal(a, np.array([4, 5, 6, 7, 8, 9]))


def test_arange_step():
    a = np.arange(0, 12, 3)
    nt.assert_array_equal(a, np.array([0, 3, 6, 9]))

    b = np.arange(0, 6, 1.2)
    nt.assert_array_almost_equal(b, np.array([0., 1.2, 2.4, 3.6, 4.8]), 2)


def test_reshape():
    """
    将数组重新组合成新的 shape
    """
    a = np.arange(0, 12).reshape(3, 4)
    nt.assert_array_equal(a, np.array([[0, 1, 2, 3],
                                       [4, 5, 6, 7],
                                       [8, 9, 10, 11]]))


def test_linspace():
    a = np.linspace(2.0, 3.0, num=5)  # num, 生成数的数目，默认 50
    nt.assert_array_almost_equal(a, np.array([2., 2.25, 2.5, 2.75, 3.]), 3)

    a = np.linspace(2.0, 3.0, num=5, endpoint=False)  # endpoint 是否包含最后一个值
    nt.assert_array_almost_equal(a, np.array([2., 2.2, 2.4, 2.6, 2.8]), 2)

    # 以 (samples, step) 的形式，同时返回 step
    a = np.linspace(2.0, 3.0, num=5, retstep=True)
    nt.assert_almost_equal(a[1], 0.25, 3)


def np_sum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    print(a)
    print(b)
    print(c)
