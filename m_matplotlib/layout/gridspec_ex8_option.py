import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=False)
gs1 = fig.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48, wspace=0.05)

ax1 = fig.add_subplot(gs1[:-1, :])
ax2 = fig.add_subplot(gs1[-1, :-1])
ax3 = fig.add_subplot(gs1[-1, -1])

gs2 = fig.add_gridspec(nrows=3, ncols=3, left=0.55, right=0.98, hspace=0.05)
fig.add_subplot(gs2[:, :-1])
fig.add_subplot(gs2[:-1, -1])
fig.add_subplot(gs2[-1, -1])

plt.show()
