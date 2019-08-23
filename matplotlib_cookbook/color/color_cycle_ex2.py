import matplotlib.pyplot as plt

"""
从色轮选择颜色
"""

years = list(range(2009, 2017))
android = [6.8, 67.22, 220.67, 451.62, 761.29, 1004.68, 1160.21, 1271.02]
ios = [24.89, 46.6, 89.27, 130.13, 150.79, 191.43, 225.85, 216.07]
microsoft = [15.03, 12.38, 8.76, 16.94, 30.71, 35.13, 26.74, 6.94]

plt.plot(years, android, label='Android', c='C2')
plt.plot(years, ios, label='iOS', c='C0')
plt.plot(years, microsoft, label='Microsoft', C='C1')
plt.legend()
plt.show()
