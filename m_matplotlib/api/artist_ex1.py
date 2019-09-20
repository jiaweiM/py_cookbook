import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax = fig.add_subplot(2, 1, 1)  # two rows, one columns, first plot

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
line, = ax.plot(t, s, color='blue', lw=2)
plt.show()
