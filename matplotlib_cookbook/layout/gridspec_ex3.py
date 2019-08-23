import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(3, 3)
fig_ax1 = fig.add_subplot(gs[0, :])
fig_ax1.set_title('gs[0, :]')
fig_ax2 = fig.add_subplot(gs[1, :-1])
fig_ax2.set_title('gs[1:, :-1]')
fig_ax3 = fig.add_subplot(gs[1:, -1])
fig_ax3.set_title('gs[1:, -1]')
fig_ax4 = fig.add_subplot(gs[-1, 0])
fig_ax4.set_title('gs[-1, 0]')
fig_ax5 = fig.add_subplot(gs[-1, -2])
fig_ax5.set_title('gs[-1, -2]')

plt.show()
