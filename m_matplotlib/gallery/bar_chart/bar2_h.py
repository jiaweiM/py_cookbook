# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

data = [5., 25., 50., 20.]
plt.barh(range(len(data)), data)

plt.show()
