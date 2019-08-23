# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('example.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='Loaded from file')

# 设置坐标轴标签
plt.xlabel('x')
plt.ylabel('y')

# 设置标题，如果要添加子标题，添加\n
plt.title('Interesting Graph\nsub title')
plt.legend()

plt.show()
