import numpy as np
import numpy.testing as nt
from numpy.linalg import norm


def test_L1():
    '''计算L1距离，即各个值的绝对值加和'''
    a = np.array([1, 2, 3])
    l1 = norm(a, 1)
    assert l1 == 6


def test_L2():
    '''计算L2距离，也就是欧式距离'''
    a = np.array([1, 2, 3])
    l2 = norm(a)
    nt.assert_almost_equal(l2, 3.74, 2)
