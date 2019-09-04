# -*- coding: utf-8 -*-

import test_numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data2.txt')

# data.T 将2D数组的行和列进行了转换，这样就可以对列进行迭代
for column in data.T:
    plt.plot(data[:, 0], column)

plt.show()
