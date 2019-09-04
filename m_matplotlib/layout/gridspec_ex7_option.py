import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=False)
gs = fig.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48, wspace=0.05)

ax1 = fig.add_subplot(gs[:-1, :])
ax2 = fig.add_subplot(gs[-1, :-1])
ax3 = fig.add_subplot(gs[-1, -1])

plt.show()
