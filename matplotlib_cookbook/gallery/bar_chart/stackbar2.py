# -*- coding: utf-8 -*-
'''
When stacking more than two set of values, the code gets less pretty as follows
'''

import test_numpy as np
import matplotlib.pyplot as plt

A = np.array([5., 30., 45., 22.])
B = np.array([5., 25., 50., 20.])
C = np.array([1., 2., 1., 1.])
X = np.arange(4)
plt.bar(X, A, color='b')
plt.bar(X, B, color='g', bottom=A)
plt.bar(X, C, color='r', bottom=A + B)

plt.show()
