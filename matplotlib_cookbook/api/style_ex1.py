import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")
data = np.random.randn(50)

with plt.style.context(('dark_background')):
    plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
plt.show()
