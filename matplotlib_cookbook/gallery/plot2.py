# -*- coding: utf-8 -*-
'''plot the binomial x^2-2x+1 in the [-3,2] interval using 200 points'''

import test_numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3, 2, 200)
Y = X ** 2 - 2 * X + 1

plt.plot(X, Y)
plt.show()
