# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

__author__ = 'JiaweiMao'
__version__ = '1.0.0'

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 80, 70, 64, 34, 12, 12, 34, 56]
# ids = [x for x in range(len(population_ages))]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)


# 设置坐标轴标签
plt.xlabel('x')
plt.ylabel('y')

# 设置标题，如果要添加子标题，添加\n
plt.title('Interesting Graph\nsub title')
plt.legend()

plt.show()
