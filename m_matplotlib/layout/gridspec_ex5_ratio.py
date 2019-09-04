import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=True)
widths = [2, 3, 1.5]
heights = [1, 3, 2]

spec = fig.add_gridspec(ncols=3, nrows=3, width_ratios=widths, height_ratios=heights)
for row in range(3):
    for col in range(3):
        ax = fig.add_subplot(spec[row, col])
        label = 'Width: {}\nHeight: {}'.format(widths[col], heights[row])
        ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')
plt.show()
