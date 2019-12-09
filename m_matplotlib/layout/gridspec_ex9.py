import numpy as np
from itertools import product
import matplotlib.pyplot as plt


def squiggle_xy(a, b, c, d, i=np.arange(0.0, 2 * np.pi, 0.05)):
    return np.sin(i * a) * np.cos(i * b), np.sin(i * c) * np.cos(i * d)


fig = plt.figure(figsize=(8, 8), constrained_layout=False)

