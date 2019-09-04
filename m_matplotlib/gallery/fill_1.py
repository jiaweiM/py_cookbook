# -*- coding: utf-8 -*-

"""
==================
A simple Fill plot
==================

This example showcases the most basic fill plot a user can do with matplotlib.
"""
import test_numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

fig, ax = plt.subplots()

# 定义 zorder，是为了保证 grid 不会覆盖在 Polygon 上
ax.fill(x, y, zorder=10)

# 打开网格，
ax.grid(True, zorder=5)
plt.show()
