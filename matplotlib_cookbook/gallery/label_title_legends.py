# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

__author__ = 'JiaweiMao'
__version__ = '1.0.0'

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x, y, label='first line')  # label是可选的，用于设置线条注释
plt.plot(x2, y2, label='second')  # 添加第二个 plot

# 设置坐标轴标签
plt.xlabel('Plot Number')
plt.ylabel('Important var')

# 设置标题，如果要添加子标题，添加\n
plt.title('Interesting Graph\nsub title')

plt.legend()

plt.show()
