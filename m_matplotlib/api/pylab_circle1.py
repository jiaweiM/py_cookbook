# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

'''除了 x, y 成对参数，还可以提供第三个参数，用于设置图标类型和颜色
默认值 'b-'，即蓝色实线
'''
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # r-red, o-circle
plt.axis([0, 6, 0, 20])  # 设置坐标轴范围 [xmin, xmax, ymin, ymax]
plt.show()
