import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=True)
spec = fig.add_gridspec(ncols=2, nrows=2)
anno_opts = dict(xy=(0.5, 0.5), xycoords='axes fraction',
                 va='center', ha='center')

ax1 = fig.add_subplot(spec[0, 0])
ax1.annotate('GridSpec[0, 0]', **anno_opts)
fig.add_subplot(spec[0, 1]).annotate('GridSpec[0, 1]', **anno_opts)
fig.add_subplot(spec[1, 0]).annotate('GridSpec[1, 0]', **anno_opts)
fig.add_subplot(spec[1, 1]).annotate('GridSpec[1, 1]', **anno_opts)

plt.show()
