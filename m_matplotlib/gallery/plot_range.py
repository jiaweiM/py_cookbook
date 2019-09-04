# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 10)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, x ** 2, x, x ** 3)
axes[0].set_title("default axes ranges")

axes[1].plot(x, x ** 2, x, x ** 3)
axes[1].axis('off')
axes[1].set_title("tight axes")

axes[2].plot(x, x ** 2, x, x ** 3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("custom axes range");

plt.show()
