import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"Z:\MaoJiawei\phos\poff.csv", header=None, names=['Delta Charge', 'Mass Offset', "Frequency"])

fig = plt.figure(figsize=(10, 5.6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.bar(df.iloc[:, 1], df.iloc[:, 2], width=0.4)
ax.set_xlabel("m/z offset")
ax.set_ylabel("Frequency")

plt.show()
