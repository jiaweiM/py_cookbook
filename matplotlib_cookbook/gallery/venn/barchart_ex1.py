# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

__author__ = 'JiaweiMao'
__version__ = '1.0.0'

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

'''绘制柱状图'''
plt.bar(x, y, label='Bars1', color='r')  # label 可选，默认颜色挺好，也可以通过可选参数color设置颜色
plt.bar(x2, y2, label='Bars2', color='c')

# 设置坐标轴标签
plt.xlabel('x')
plt.ylabel('y')

# 设置标题，如果要添加子标题，添加\n
plt.title('Interesting Graph\nsub title')
plt.legend()

plt.show()
