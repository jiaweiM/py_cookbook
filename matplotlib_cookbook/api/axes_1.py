# -*- coding: utf-8 -*-
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0, 1, 100)
Y = np.sin(X * np.pi * 2)

fig = plt.figure()
gs = gridspec.GridSpec(2, 1)
ax = plt.subplot(gs[0, 0])
ax.plot(X, Y)
ax.set_title('a sine wave')
ax.set_ylabel('volts')

plt.show()
