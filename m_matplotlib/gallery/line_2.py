# -*- coding: utf-8 -*-

"""正弦和余弦函数"""

import numpy as np
import matplotlib.pyplot as plt

# Create a new figure of size 8x6 inch, using 100 dots per inch
fig = plt.figure(figsize=(8, 6), dpi=100)

# Create a new subplot from a grid of 1x1
ax = fig.add_subplot(111)

x = np.linspace(-np.pi, np.pi, 256)
c = np.cos(x)
s = np.sin(x)

# plot cosine using blue color with a continuous line of width 1
ax.plot(x, c, color='blue', lw=1.0, linestyle='-')

# plot sine using green color with a continuous line of width 1
ax.plot(x, s, color='green', lw=1.0, linestyle='-')

# set x limits
ax.set_xlim(-4.0, 4.0)


plt.show()
