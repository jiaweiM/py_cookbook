import matplotlib.pyplot as plt
import numpy as np


def f(t):
    'A damped exponential，阻尼指数'
    s1 = np.cos(2 * np.pi * t)
    e1 = np.exp(-t)
    return s1 * e1


t1 = np.arange(0.0, 5.0, .2)
l = plt.plot(t1, f(t1), 'ro')
plt.setp(l, markersize=30) # 设置 marker 的大小
plt.setp(l, markerfacecolor='C0') # 设置 marker 颜色

plt.show()
