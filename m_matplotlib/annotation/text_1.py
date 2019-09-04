# -*- coding: utf-8 -*-

import test_numpy as np
import matplotlib.pyplot as plt

'''
add annotation at any location
'''
X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

plt.text(-0.5, -0.25, "Brackmard minimum") # 坐标是文本的左下角位置

plt.plot(X, Y, c='k')
plt.show()
