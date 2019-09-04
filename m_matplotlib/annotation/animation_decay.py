# -*- coding: utf-8 -*-
"""
=====
Decay
=====

This example showcases a sinusoidal decay animation.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1
        yield t, np.sin(2 * np.pi * t) * np.exp(-t / 10.)
