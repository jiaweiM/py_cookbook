import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# df = pd.read_csv(r"Z:\MaoJiawei\phos\poff.csv", header=None, names=[
                #  'Delta Charge', 'Mass Offset', "Frequency"])

x = np.array([-145.55, -145.54, -145.05, -145.04, -144.54, -
              144.04, -81.02, -80.52, -80.02, -8.5, 0, 0.49, 0.5, 1])
y = np.array([0.109965636, 0.140893471, 0.075601375, 0.178694158, 0.171821306, 0.120274914, 0.092783505,
              0.096219931, 0.065292096, 0.072164948, 0.261168385, 0.113402062, 0.154639175, 0.130584192])

fig = plt.figure(figsize=(10, 5.6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.bar(x , y, width=0.4)
ax.set_xlabel("m/z offset")
ax.set_ylabel("Frequency")

plt.show()
