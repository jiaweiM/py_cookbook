import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'Z:\MaoJiawei\phos\groups.csv', names=["Charge", "Segment", "Mass"], header=None)
fix, ax = plt.subplots()

groups = df.groupby("Segment")
# segment
group_0 = groups.get_group(0)
group_1 = groups.get_group(1)

ax.scatter(group_0.iloc[:, 0] - 0.2, group_0.iloc[:, 2], label="Lower Mass Segment")
ax.scatter(group_1.iloc[:, 0] + 0.2, group_1.iloc[:, 2], label="Upper Mass Segment")

ax.set_xlabel("Precursor Charge")
ax.set_ylabel("Precursor Mass")

ax.set_xticks([2, 3, 4, 5])
ax.set_yticks([1000, 2000, 3000, 4000])

ax.legend(loc="upper left")

fix.savefig("file.svg")
# plt.show()
