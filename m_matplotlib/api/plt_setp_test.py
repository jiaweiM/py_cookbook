import matplotlib.pyplot as plt

"""
setp(), getp(), 分别设置和获得 artist 对象的属性。
"""

line, = plt.plot([1, 2, 3])
plt.setp(line, linestyle='--')
