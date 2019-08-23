# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

A = [5., 30., 45., 22.]
B = [5., 25., 50., 20.]

X = range(4)

plt.bar(X, A, color='b')
# bottom 用于指定 column 的起始值
plt.bar(X, B, color='r', bottom=A)
plt.show()
