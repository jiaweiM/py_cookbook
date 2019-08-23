# -*- coding: utf-8 -*-
"""
====================
Horizontal bar chart
====================
Axes.barh(bottom, width, height=0.8, left=None, **kwargs)
This example showcases a simple horizontal bar chart.
"""

import matplotlib.pyplot as plt
import test_numpy as np

fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# 等距的 y 值，条形图的位置
y_pos = np.arange(len(people))
# x 值，即条形度的长度
performance = 3 + np.random.rand(len(people))
# 用于 error bar
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center', color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)

ax.invert_yaxis()  # labels read top-to-bottom

ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()
