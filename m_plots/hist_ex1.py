import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"Z:\MaoJiawei\phos\poff.csv", header=None, names=['Delta Charge', 'Mass Offset', "Frequency"])

plt.stem(df.iloc[:, 1], df.iloc[:, 2], use_line_collection=True)

plt.show()
