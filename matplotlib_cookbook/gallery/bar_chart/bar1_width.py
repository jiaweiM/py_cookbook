# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

data = [5., 25., 50., 20.]

# bar 的默认厚度为 0.8,调整到1.0后，bar 之间就没有空隙了
plt.bar(range(len(data)), data, width=1.)
plt.show()
