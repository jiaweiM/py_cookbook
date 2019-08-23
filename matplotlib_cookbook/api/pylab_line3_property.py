# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

lines = plt.plot(x, y, linewidth=3.0)  # 通过关键字参数设置线条宽度

plt.setp(lines, color='m', linewidth=1.0)  # setp() 命令，关键字参数风格
plt.setp(lines, 'linewidth', 4.0)  # MATLAB风格的命令

plt.show()
