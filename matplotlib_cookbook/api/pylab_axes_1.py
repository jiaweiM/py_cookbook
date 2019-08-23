# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

__author__ = 'JiaweiMao'
__version__ = '1.0.0'

'''手动放置坐标轴位置'''

dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt #colored noise


