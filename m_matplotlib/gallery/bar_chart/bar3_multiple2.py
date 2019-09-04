# -*- coding: utf-8 -*-

import test_numpy as np
import matplotlib.pyplot as plt

'''前面的例子自己控制 bar 的位置不开心，下面是进化版'''
data = [[5., 25., 50., 20.],
        [4., 23., 51., 17.],
        [6., 22., 52., 19.]]
color_list = ['b', 'g', 'r']
gap = .8 / len(data)
# enumerate,同时返回 row and its index.
for i, row in enumerate(data):
    X = np.arange(len(row))

    plt.bar(X + i * gap, row,
            width=gap,
            color=color_list[i % len(color_list)])
plt.show()
