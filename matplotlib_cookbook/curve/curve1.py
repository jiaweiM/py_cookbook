import matplotlib.pyplot as plt

'''shows a curve Y=x**2 with X in the [0, 99] range.'''
X = range(100)
Y = [value ** 2 for value in X]

plt.plot(X, Y)
plt.show()
