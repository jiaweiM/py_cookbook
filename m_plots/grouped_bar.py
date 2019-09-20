import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv(r"Z:\MaoJiawei\phos\ions.csv", header=None,
                 names=["Ion Type", "Charge", "Ion", "Low Freq", "High Freq"])
df.sort_values(by='Ion Type', inplace=True)

fig = plt.figure(figsize=(10, 5.6))

labels = df.iloc[:, 0]
x = np.arange(len(labels))
width = 0.35

ax = fig.add_axes([0.1, 0.25, 0.8, 0.7])
ax.bar(x - width / 2, df.iloc[:, 3], width, label='Lower Segment')
ax.bar(x + width / 2, df.iloc[:, 4], width, label='Higher Segment')

ax.set_ylabel('Frequency')
ax.set_xticks(x)
ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_xticklabels(labels, rotation='vertical')
ax.legend()

fig.tight_layout()
plt.show()
