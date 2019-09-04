# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('Some numbers')
plt.show()

'''x 范围是[0-3]，因为当你给plot()的数据只有一项，其默认为y值，x值则为数组索引
ylabel("a_label") 用于设置 y 轴标签
'''
