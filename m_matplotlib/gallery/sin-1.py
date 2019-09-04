# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import math

# create a list T witn numbers from 0 to 99
T = range(100)

# rescaling the values stored in T so that x goes from 0 to 2 pi
X = [(2 * math.pi * t) / len(T) for t in T]
Y = [math.sin(value) for value in X]

plt.plot(X, Y)
plt.show()
