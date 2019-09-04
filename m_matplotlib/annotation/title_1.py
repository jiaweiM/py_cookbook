# -*- coding: utf-8 -*-
import test_numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-4, 4, 1024)
Y = 0.5 * (X + 4.) * (X + 1.) * (X - 2.)


plt.title("A polynomial") # 设置标题
plt.plot(X, Y, c='k')
plt.show()
