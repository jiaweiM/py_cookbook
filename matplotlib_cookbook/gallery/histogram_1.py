# -*- coding: utf-8 -*-

'''
Histograms are graphical representations of a probability distribution. In fact, a histogram
is just a specific kind of a bar chart. We could easily use matplotlib's bar chart function
and do some statistics to generate histograms. However, histograms are so useful that
matplotlib provides a function just for them. In this recipe, we are going to see how to
use this histogram function.
'''

import test_numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(1000)

# 设置 bin 后，会自动将整个数据平均划分为20份，然后对数据分组，根据数据量绘图
plt.hist(X, bins=20)

plt.show()
