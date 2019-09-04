# -*- coding: utf-8 -*-

import test_numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(1024, 2)

'''scatter 工作和 plt.plot() 类似，'''
plt.scatter(data[:, 0], data[:, 1])
plt.show()
