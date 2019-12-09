import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_csv(r"Z:\MaoJiawei\phos\poff.csv", header=None, names=[
#  'Delta Charge', 'Mass Offset', "Frequency"])

x = np.array([-186.0936051,
              -16.0080520,
              -18.0090585,
              0,
              2.001006506,
              162.081527,
              186.0936051,
              202.1016571,
              204.1026636,
              206.1036701,
              364.1831841,
              366.1841906,
              368.1851972,
              656.3301341
              ])
y = np.array([0.203508772,
              0.526315789,
              0.171929825,
              0.824561404,
              0.614035088,
              0.214035088,
              0.185964912,
              0.638596491,
              0.561403509,
              0.18245614,
              0.41754386,
              0.410526316,
              0.18245614,
              0.326315789,
              ])

fig = plt.figure(figsize=(10, 5.6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.bar(x, y, width=1.2)
ax.set_xlabel("m/z offset")
ax.set_ylabel("Frequency")

plt.show()
