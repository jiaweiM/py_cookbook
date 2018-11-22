import numpy as np
import matplotlib.pyplot as plt

'''
https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py
'''

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)  # x locations for the groups
width = 0.35  # width of the bars: can also be len(x) sequence

p1 = plt.bar(x=ind, height=menMeans, width=width, yerr=menStd)
p2 = plt.bar(x=ind, height=womenMeans, width=width, bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', "Women"))

plt.show()
