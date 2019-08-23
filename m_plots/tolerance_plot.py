import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

total_count = [1033794, 1097757, 1107669, 1116319]
target_count = [884135, 843450, 819229, 787480]
decoy_count = [149659, 254307, 288440, 328839]
id_count = [620003, 440872, 363561, 283440]

ratio = np.array(decoy_count) / np.array(total_count)

x = np.arange(4)
width = 0.20
space = 0.05

total_color = 'tab:blue'
decoy_color = 'tab:red'
id_color = 'tab:green'

fig, ax = plt.subplots()


def killion(x, pos):
    'The two args are the value and tick position'
    return '%1.f K' % (x * 1e-3)


formatter = FuncFormatter(killion)

bar1 = ax.bar(x - width - space, total_count, width, label='Total count', color=total_color)
ax.set_ylabel('Count')
ax.set_xticks(x)
ax.set_xticklabels(('0.01', '0.05', '0.1', '0.5'))
ax.set_xlabel('MS2 Tolerance')
ax.yaxis.set_major_formatter(formatter)

# ax.plot(x - width - space, total_count, color=total_color, linestyle='-.')

ax2 = ax.twinx()
bar2 = ax2.bar(x, ratio, width, label='Decoy ratio', color=decoy_color)
ax2.set_ylabel('Ratio', color=decoy_color)
ax2.tick_params(axis='y', labelcolor=decoy_color)
# ax2.set_ybound(0, 0.35)

ax2.plot(x, ratio, color=decoy_color, linestyle='-.')

bar3 = ax.bar(x + width + space, id_count, width, label='1% FDR target count', color=id_color)
ax.plot(x + width + space, id_count, color=id_color, linestyle='-.')

bars, labels = ax.get_legend_handles_labels()
bars2, labels2 = ax2.get_legend_handles_labels()
# ax2.legend(bars + bars2, labels + labels2, loc=0)

plt.savefig(r"Z:\MaoJiawei\dataset-2\result\msfragger_20180316\open_tolerance_test\tol.png", dpi=150)

# plt.show()
