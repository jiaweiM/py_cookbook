# -*- coding: utf-8 -*-

import test_numpy as np
import matplotlib.pyplot as plt

# reads a text file and return s a NumPy 2D array
data = np.loadtxt('my_data.txt')

# given the first column of data as X coordinates and the second column of data as y coordinates
plt.plot(data[:, 0], data[:, 1])
plt.show()
