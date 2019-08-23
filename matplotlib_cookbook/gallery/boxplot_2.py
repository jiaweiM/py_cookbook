# -*- coding: utf-8 -*-

'''多个 boxplot'''

import test_numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100, 5)

plt.boxplot(data)

plt.show()
