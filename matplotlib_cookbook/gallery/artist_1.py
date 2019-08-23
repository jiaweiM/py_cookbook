# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
'''创建Axes对象(Subplot 是Axes的子类)'''
ax = fig.add_subplot(2, 1, 1)

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
'''创建Line2D实例，并添加到 Axes.lines 列表'''
line, = ax.plot(t, s, color='blue', lw=2)

plt.show()
