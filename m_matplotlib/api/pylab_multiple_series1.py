# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#
t = np.arange(0.0, 5.0, 0.2)  # 生成等差数列

'''绘制三条线，y=x(r--,红色虚线图), y=x^2(bs,红色方形图), y=x^3(g^,绿色正三角)'''
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
plt.show()
