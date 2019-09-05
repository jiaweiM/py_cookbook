import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'Z:\MaoJiawei\phos\groups.csv', header=None)
fix, ax = plt.subplots()

groups = df.groupby("1")

ax.scatter(df[0], df[2])
ax.set_xlabel("Precursor Charge")
ax.set_ylabel("Precursor Mass")

print(df)
plt.show()
