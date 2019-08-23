import matplotlib.pyplot as plt
import numpy as np

oxi_psms = (50892, 24435, 25124, 26642, 26335, 29010, 28736)
oxi_labels = ('Closed', "Open", 'Decon', 'CF', 'MSFragger', 'Open-pFind', 'Decon-MSFragger')

width = 0.35  # the width of the bars

ind = np.arange(len(oxi_psms))
fig, ax = plt.subplots(figsize=(6, 4))

oxi_psms = np.array(oxi_psms) / max(oxi_psms)
bar1 = ax.bar(ind, oxi_psms, width, color=('C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6'))

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('PSMs (%)')
# ax.set_title('Oxidation')
ax.set_xticks(ind)
ax.set_xticklabels(oxi_labels, rotation=45, ha='right')

# remove spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_bounds(0, 1)


def autolabel(rects):
    for index in np.arange(1, len(rects)):
        rect = rects[index]
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%.2f' % height,
                ha='center', va='bottom')
    # for rect in rects:
    #     height = rect.get_height()
    #     ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
    #             '%.2f' % height,
    #             ha='center', va='bottom')


autolabel(bar1)

plt.tight_layout()
plt.savefig(r"Z:\MaoJiawei\dataset-2\result\msfragger_20180316\open_0.01\m_test\count.png", dpi=150)
plt.show()
