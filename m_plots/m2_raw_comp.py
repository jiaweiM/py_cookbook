import matplotlib.pyplot as plt
import numpy as np

tol = [0.01, 0.05, 0.1, 0.5]

x = [0.01, 0.05, 0.1, 0.5]
comp_psm = [550840, 419063, 357961, 300704]
comp_seq = [125962, 107376, 95995, 85696]
comp_pro = [11278, 10870, 10510, 10158]

raw_psm = [554185, 301013, 220124, 138964]
raw_seq = [118198, 75222, 59697, 43425]
raw_pro = [11187, 9858, 9222, 8188]

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True)

ax1.plot(x, comp_psm)
ax1.plot(x, raw_psm)

ax2.plot(x, comp_seq)
ax2.plot(x, raw_seq)

ax3.plot(x, comp_pro)
ax3.plot(x, raw_pro)

ax3.set_xlabel('MS2 Tolerance')
ax2.set_ylabel("Count")
# ax3.set_xticklabels(tol)

fig.tight_layout()

plt.show()
