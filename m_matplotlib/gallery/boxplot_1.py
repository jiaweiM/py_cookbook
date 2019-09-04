# -*- coding: utf-8 -*-

'''
显示均值，四分之一值，最大最小值
Boxplot allows you to compare distributions of values by conveniently showing the median,
quartiles, maximum, and minimum of a set of values.
'''

import test_numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)

plt.boxplot(data)
plt.show()
