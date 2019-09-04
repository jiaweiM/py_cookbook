# -*- coding: utf-8 -*-
import numpy as np

'''
randn(d0, d1,..., dn)
生成满足标准正态分布的浮点数数组，对应 shape(d1,d2,...,dn)
'''
def test_randn():
    n = np.random.randn()
    print(n)
