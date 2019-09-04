# -*- coding: utf-8 -*-

'''
In the following script, we display two sets of points, A and B, drawn from two bivariate
Gaussian distributions. Each set has its own color. We call pyplot.scatter() twice,
once for each point set, as shown in the following script:
'''
import test_numpy as np
import matplotlib.pyplot as plt

A = np.random.standard_normal((100, 2))
A += np.array((-1, -1))  # Center the distrib. at <-1, -1>

B = np.random.standard_normal((100, 2))
B += np.array((1, 1))  # Center the distrib. at <1, 1>

plt.scatter(A[:, 0], A[:, 1], color='.25')
plt.scatter(B[:, 0], B[:, 1], color='.75')

plt.show()
