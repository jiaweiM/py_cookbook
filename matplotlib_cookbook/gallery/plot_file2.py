# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

with open("my_data.txt", 'r') as f:
    X, Y = zip(*[[float(s) for s in line.split()] for line in f])

plt.plot(X, Y)
plt.show()
