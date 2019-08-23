import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

"""
这是一个灰度值设置不合适，输出不好看的例子
"""

# Prepare 4 lines with different slopes
x = np.linspace(0, 200, 100)  # Prepare 100 evenly spaced numbers from
# 0 to 200
y1 = x * 2
y2 = x * 3
y3 = x * 4
y4 = x * 5
# Set line width to 2 for clarity
mpl.rcParams['lines.linewidth'] = 2
# Draw the 4 lines
# this line is too faint
plt.plot(x, y1, label='2x', c='0.9')  # light grey
# this line is barely visible
plt.plot(x, y2, label='3x', c='0.99')  # very faint grey line
# these two lines have too little contrast and may be confusing
plt.plot(x, y3, label='4x', c='0.4')  # grey
plt.plot(x, y4, label='5x', c='0.45')  # slightly lighter grey

plt.legend()
plt.show()
