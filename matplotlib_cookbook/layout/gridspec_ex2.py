import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure(constrained_layout=True)
spec = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)
fig_ax1 = fig.add_subplot(spec[0, 0])
fig_ax2 = fig.add_subplot(spec[0, 1])
fig_ax3 = fig.add_subplot(spec[1, 0])
fig_ax4 = fig.add_subplot(spec[1, 1])

plt.show()
