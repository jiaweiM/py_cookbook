# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('example.csv', delimiter=',', unpack=True)
plt.plot(x, y, label='Loaded from file')

# 设置坐标轴标签
plt.xlabel('x')
plt.ylabel('y')

# 设置标题，如果要添加子标题，添加\n
plt.title('Interesting Graph\nsub title')
plt.legend()

plt.show()
