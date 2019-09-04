# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]

plt.scatter(x, y, label='skitscat', color='k', marker='*', s=100)  # marker 设置散点形状，默认为圆形;s，设置散点大小

# 设置坐标轴标签
plt.xlabel('x')
plt.ylabel('y')

# 设置标题，如果要添加子标题，添加\n
plt.title('Interesting Graph\nsub title')
plt.legend()

plt.show()
