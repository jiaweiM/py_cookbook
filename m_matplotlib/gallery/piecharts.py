# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2, ]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

''''''
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,  # 加阴影
        explode=(0, 0.1, 0, 0), # 设置延伸出来的部分
        autopct= '%1.1f%%'   # adds the percentage to the pie
        )

# 设置标题，如果要添加子标题，添加\n
plt.title('Interesting Graph\nsub title')
plt.show()
