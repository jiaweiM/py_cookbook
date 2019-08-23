# -*- coding: utf-8 -*-

import test_numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2 * np.pi, 100)
Ya = np.sin(X)
Yb = np.cos(X)

# 两次调用 plot，生成两条曲线
plt.plot(X, Ya)
plt.plot(X, Yb)

plt.show()
