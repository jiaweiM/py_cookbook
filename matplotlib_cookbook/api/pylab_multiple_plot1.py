# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

''' figure(1) 创建第一个Figure，可选命令，因为调用 subplot 时会自动创建Figure
subplot(211) (numrows, numcols, fignum), fignum 范围 [1,numrows*numcols],
如果 numrows*numcols<10,就可以不加逗号，即(211)等效于(2,1,1)，即2行1列第1个 plot.
'''
plt.figure(1)
plt.subplot(211)

'''包含两个系列，系列1:f(t1), (bo, 蓝色点图)， 系列2:f(t2), (k,黑色默认线图)'''
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)  # 2行1列，第2个plot
'''红色虚线图'''
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')

plt.show()
