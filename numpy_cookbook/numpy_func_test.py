import numpy as np

"""
arange([start,] stop[, step,], dtype=None)
[start,stop)之间按照step 生成数组，类似于 python的 range 函数.
如果 step 为小数，则推荐使用 linspace 函数.

"""

def np_sum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    print(a)
    print(b)
    print(c)