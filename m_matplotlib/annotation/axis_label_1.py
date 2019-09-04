# -*- coding: utf-8 -*-
import test_numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

plt.title("Power curve for airfoil KV873")
plt.xlabel("Air speed")
plt.ylabel("Total draw")

plt.plot(X, Y, c='k')
plt.show()
