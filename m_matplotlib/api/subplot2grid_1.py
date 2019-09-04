# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

'''
subplot2grid 功能类似于 subplot()
但是一个 subplot 可以占据多个 cell.
'''
ax = plt.subplot2grid((2, 2), (0, 0))  # 需要指定 grid shape和 subplot location,等价于 subplot(2,2,1)

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

plt.show()
