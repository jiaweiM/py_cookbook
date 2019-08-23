# -*- coding: utf-8 -*-

'''
Each point of the dataset is stored in a comma-separated list of values. The last column that
gives the label of each point is a string that can take three possible values—Iris-virginica,
Iris-versicolor, and Iris-Vertosa. We read this file using NumPy's numpy.loadtxt
function. The color of points will depend on their label, and we will display them with just one
call to pyplot.scatter() as follows
'''

import test_numpy as np
import matplotlib.pyplot as plt

label_set = (
    b'Iris-setosa',
    b'Iris-versicolor',
    b'Iris-virginica'
)


def read_label(label):
    return label_set.index(label)

data = np.loadtxt('iris.data',
                  delimiter=',',
                  converters={4: read_label})

color_set = ('.00', '.50', '.75')
color_list = [color_set[int(label)] for label in data[:, 4]]
plt.scatter(data[:, 0], data[:, 1], color=color_list)

plt.show()
