# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

data = [5., 25., 50., 20.]

# bar 的默认厚度为 0.8
plt.bar(range(len(data)), data)
plt.show()
