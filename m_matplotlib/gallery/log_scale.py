# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 10)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, x ** 2, x, np.exp(x))
axes[0].set_title('Normal scale')

axes[1].plot(x, x ** 2, x, np.exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)")

plt.show()