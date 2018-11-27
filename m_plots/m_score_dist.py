import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'Z:\MaoJiawei\dataset-2\result\open_0.01_v7.1\cp_intensify_msfragger^raw_deltaMasses.csv',
                 header=None)
# df.columns = ['Title', 'Delta Mass', 'Hyper score', 'Hyper score']
# print(df.columns)


xValues = df[2]
yValues = df[3]

delta_scores = xValues - yValues
delta_scores.sort_values(ascending=True, inplace=True)
indexes = np.arange(1, len(delta_scores) + 1)

fig, ax = plt.subplots()
ax.plot(indexes, delta_scores, 'o')

plt.show()
